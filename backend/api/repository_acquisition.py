"""
QuantumShield — Secure Repository Acquisition Layer.

Architectural Flow:
GitHub HTTPS URL / Local Directory / Configured Scan Target
  ↓
Strict URL Validation & SSRF Guard (Reject HTTP, non-GitHub, localhost, private IPs, shell injection)
  ↓
Repository Acquisition Strategy:
  - If configured local repository (QUANTUMSHIELD_LOCAL_SCAN_ROOT) or alias ("sih", "local"): resolve directly (read-only).
  - If local directory or pinned test target: validate path boundaries.
  - If GitHub HTTPS URL: download controlled ZIP archive over HTTPS (with Zip Slip & Decompression Bomb protections).
  ↓
Temporary Isolated Workspace (tempfile.mkdtemp)
  ↓
AST Discovery & Quantum Cryptographic Analysis (state.run_scan)
  ↓
Deterministic Cleanup on Exit (shutil.rmtree in finally)
"""
import ipaddress
import os
import re
import shutil
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from contextlib import contextmanager
from typing import Optional, Tuple
from fastapi import HTTPException
from app.pipeline import PRUNE_DIRS


# Safety constraints
MAX_ARCHIVE_BYTES = 200 * 1024 * 1024      # 200 MB compressed cap
MAX_EXTRACTED_BYTES = 1024 * 1024 * 1024   # 1 GB uncompressed cap
MAX_FILE_COUNT = 20000                     # Max files extracted
DOWNLOAD_TIMEOUT = 45                     # Max seconds to wait for download
PINNED_TARGETS_DIR = os.path.abspath("tests/external_targets")


def _load_env_file():
    """Load key-value pairs from .env file into os.environ if not already set."""
    env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
    if os.path.exists(env_file):
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k and k not in os.environ:
                            os.environ[k] = v
        except Exception:
            pass


_load_env_file()


def is_remote_scan_enabled() -> bool:
    """Check if outbound remote repository scanning is permitted in this deployment mode."""
    val = os.getenv("REMOTE_SCAN_ENABLED", "true").strip().lower()
    return val in ("1", "true", "yes", "on")


def get_configured_local_scan_root() -> Optional[str]:
    """
    Retrieve the verified path to the configured local scan repository,
    read from the QUANTUMSHIELD_LOCAL_SCAN_ROOT environment variable.
    """
    val = os.getenv("QUANTUMSHIELD_LOCAL_SCAN_ROOT")
    if val:
        cleaned = val.strip().strip('"').strip("'")
        if os.path.isdir(cleaned):
            return os.path.abspath(cleaned)
    return None


class AcquisitionError(HTTPException):
    """Structured, safe acquisition error with error code and stage context."""
    def __init__(self, error_code: str, message: str, status_code: int = 400):
        super().__init__(
            status_code=status_code,
            detail={
                "error": error_code,
                "message": message,
                "stage": "repository_acquisition"
            }
        )


class AcquiredWorkspace:
    """Represents a validated local or temporary workspace ready for AST cryptographic analysis."""
    def __init__(
        self,
        scan_target: str,
        display_name: str,
        is_temporary: bool,
        temp_root: Optional[str] = None
    ):
        self.scan_target = scan_target
        self.display_name = display_name
        self.is_temporary = is_temporary
        self.temp_root = temp_root


def _is_private_or_local_host(hostname: str) -> bool:
    """SSRF protection: determine if hostname resolves to localhost or private network."""
    lowered = hostname.lower().strip("[]")
    if lowered in ("localhost", "127.0.0.1", "::1", "0.0.0.0"):
        return True
    try:
        ip = ipaddress.ip_address(lowered)
        return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved
    except ValueError:
        pass
    return False


def validate_github_url(url: str) -> Tuple[str, str, Optional[str]]:
    """
    Strictly validates a GitHub repository URL.
    Returns (owner, repo, optional_ref).
    Rejects HTTP, private IPs, non-GitHub hosts, and command injection characters.
    """
    if not url or not isinstance(url, str):
        raise AcquisitionError("INVALID_URL", "Repository URL must be a non-empty string.")

    cleaned = url.strip().strip('"').strip("'")
    if len(cleaned) > 500:
        raise AcquisitionError("URL_TOO_LONG", "Repository URL exceeds maximum allowed length of 500 characters.")

    # Reject shell metacharacters and control characters
    if re.search(r"[\s;&|`$\n\r<>!]", cleaned):
        raise AcquisitionError("MALFORMED_URL", "Repository URL contains forbidden control or command characters.")

    try:
        parsed = urllib.parse.urlparse(cleaned)
    except Exception:
        raise AcquisitionError("MALFORMED_URL", "Unable to parse repository URL.")

    # Scheme validation: HTTPS ONLY
    if parsed.scheme.lower() == "http":
        raise AcquisitionError(
            "INSECURE_SCHEME",
            "Insecure HTTP protocol is not permitted. Please use secure HTTPS (https://github.com/...)."
        )
    if parsed.scheme.lower() != "https":
        raise AcquisitionError(
            "UNSUPPORTED_SCHEME",
            f"Unsupported URL scheme '{parsed.scheme}'. Only HTTPS GitHub URLs are supported."
        )

    # Host validation: github.com or www.github.com
    hostname = (parsed.hostname or "").lower()
    if not hostname:
        raise AcquisitionError("MISSING_HOSTNAME", "Repository URL has no hostname.")

    if _is_private_or_local_host(hostname):
        raise AcquisitionError(
            "SSRF_PROHIBITED",
            "Scanning localhost, loopback, or private internal network endpoints is prohibited."
        )

    if hostname not in ("github.com", "www.github.com"):
        raise AcquisitionError(
            "UNSUPPORTED_HOST",
            f"Host '{hostname}' is not supported. Remote acquisition currently supports public repositories on github.com."
        )

    # Path validation: /owner/repo[/tree/ref]
    path_segments = [s for s in parsed.path.strip("/").split("/") if s]
    if len(path_segments) < 2:
        raise AcquisitionError(
            "MALFORMED_GITHUB_URL",
            "Invalid GitHub URL structure. Expected format: https://github.com/owner/repository"
        )

    owner = path_segments[0]
    repo = path_segments[1]
    if repo.endswith(".git"):
        repo = repo[:-4]

    ident_pattern = r"^[a-zA-Z0-9_.-]+$"
    if not re.match(ident_pattern, owner) or not re.match(ident_pattern, repo):
        raise AcquisitionError(
            "INVALID_IDENTIFIERS",
            "GitHub owner or repository name contains invalid characters."
        )

    ref = None
    if len(path_segments) >= 4 and path_segments[2] in ("tree", "blob"):
        ref = path_segments[3]
        if not re.match(ident_pattern, ref):
            ref = None

    return owner, repo, ref


def _resolve_pinned_target(owner: str, repo: str) -> Optional[str]:
    """Check if the repository is already pre-pinned in tests/external_targets."""
    if not os.path.isdir(PINNED_TARGETS_DIR):
        return None
    for name in (repo.lower(), f"{owner.lower()}_{repo.lower()}"):
        candidate = os.path.join(PINNED_TARGETS_DIR, name)
        if os.path.isdir(candidate) and any(f != ".git" for f in os.listdir(candidate)):
            return os.path.abspath(candidate)
    for name in ("cpython", "openssl", "openssh"):
        if name in repo.lower():
            candidate = os.path.join(PINNED_TARGETS_DIR, name)
            if os.path.isdir(candidate) and any(f != ".git" for f in os.listdir(candidate)):
                return os.path.abspath(candidate)
    return None


def _download_github_archive(owner: str, repo: str, ref: Optional[str], dest_zip: str) -> None:
    """Download repository archive over HTTPS with size and timeout guards."""
    headers = {
        "User-Agent": "QuantumShield-Cryptographic-Scanner/1.0",
        "Accept": "application/vnd.github.v3+json, application/zip"
    }

    ref_suffix = f"/{ref}" if ref else ""
    urls_to_try = [
        f"https://api.github.com/repos/{owner}/{repo}/zipball{ref_suffix}",
        f"https://codeload.github.com/{owner}/{repo}/zip/refs/heads/{ref or 'main'}",
        f"https://codeload.github.com/{owner}/{repo}/zip/refs/heads/master",
    ]

    downloaded = False
    last_error_code = "DOWNLOAD_FAILED"
    last_error_msg = f"Failed to acquire repository archive for '{owner}/{repo}'."

    for url in urls_to_try:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as response:
                if response.status not in (200, 302):
                    continue

                total_bytes = 0
                with open(dest_zip, "wb") as f_out:
                    while True:
                        chunk = response.read(64 * 1024)
                        if not chunk:
                            break
                        total_bytes += len(chunk)
                        if total_bytes > MAX_ARCHIVE_BYTES:
                            raise AcquisitionError(
                                "ARCHIVE_TOO_LARGE",
                                f"Repository archive exceeds maximum permitted size of {MAX_ARCHIVE_BYTES // (1024 * 1024)} MB. For very large codebases, use local folder scanning or ZIP upload.",
                                status_code=413
                            )
                        f_out.write(chunk)

                if total_bytes > 0:
                    downloaded = True
                    break

        except AcquisitionError:
            raise
        except urllib.error.HTTPError as e:
            if e.code == 404:
                last_error_code = "REPOSITORY_NOT_FOUND"
                last_error_msg = f"GitHub repository '{owner}/{repo}' was not found or is private. Please verify the URL."
            elif e.code == 403:
                last_error_code = "RATE_LIMIT_OR_FORBIDDEN"
                last_error_msg = "GitHub API rate limit exceeded or access forbidden. Please try again shortly or upload a ZIP archive."
            elif e.code == 429:
                last_error_code = "RATE_LIMIT_EXCEEDED"
                last_error_msg = "GitHub rate limit reached. Please use local folder scanning or ZIP upload."
            continue
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_error_code = "NETWORK_TIMEOUT"
            last_error_msg = f"Connection to GitHub timed out or failed: {str(e)}"
            continue

    if not downloaded or not os.path.exists(dest_zip) or os.path.getsize(dest_zip) == 0:
        raise AcquisitionError(last_error_code, last_error_msg, status_code=404 if last_error_code == "REPOSITORY_NOT_FOUND" else 502)


def _safe_extract_zip(zip_path: str, extract_dir: str) -> str:
    """Extracts ZIP archive with Zip-Slip, decompression bomb, and file-count protections."""
    real_extract_dir = os.path.realpath(extract_dir)

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            members = zf.infolist()

            if len(members) > MAX_FILE_COUNT:
                raise AcquisitionError(
                    "ARCHIVE_TOO_MANY_FILES",
                    f"Repository contains {len(members)} files, which exceeds the {MAX_FILE_COUNT} files security threshold.",
                    status_code=413
                )

            total_uncompressed = sum(m.file_size for m in members)
            if total_uncompressed > MAX_EXTRACTED_BYTES:
                raise AcquisitionError(
                    "ARCHIVE_EXTRACTED_TOO_LARGE",
                    f"Uncompressed repository contents ({total_uncompressed // (1024 * 1024)} MB) exceed the {MAX_EXTRACTED_BYTES // (1024 * 1024)} MB safety cap.",
                    status_code=413
                )

            for member in members:
                # Zip-Slip Guard
                member_target = os.path.realpath(os.path.join(extract_dir, member.filename))
                if not member_target.startswith(real_extract_dir):
                    raise AcquisitionError(
                        "ZIP_SLIP_ATTEMPT",
                        "Security violation: Archive contains relative path traversal entries (Zip Slip).",
                        status_code=400
                    )

                # Skip pruned directories (.git, node_modules, venv, etc.)
                parts = [p.lower() for p in member.filename.replace("\\", "/").split("/") if p]
                if any(p in PRUNE_DIRS for p in parts):
                    continue

                zf.extract(member, extract_dir)

    except zipfile.BadZipFile:
        raise AcquisitionError("CORRUPT_ARCHIVE", "Downloaded archive is corrupted or not a valid ZIP file.", status_code=400)

    entries = [os.path.join(extract_dir, e) for e in os.listdir(extract_dir)]
    dirs = [e for e in entries if os.path.isdir(e)]
    if len(dirs) == 1 and len(entries) == 1:
        return dirs[0]
    return extract_dir


def _validate_local_path(path: str) -> str:
    """Validate a server-local filesystem path (rejects traversal and system roots)."""
    cleaned = path.strip().strip('"').strip("'")
    if ".." in cleaned:
        raise AcquisitionError("PATH_TRAVERSAL", "Path traversal tokens ('..') are prohibited.", status_code=400)

    # Check if this matches configured local scan root
    local_root = get_configured_local_scan_root()
    if local_root and os.path.normcase(os.path.abspath(cleaned)) == os.path.normcase(local_root):
        return local_root

    if os.name != "nt" and len(cleaned) >= 2 and cleaned[1] == ":" and cleaned[0].isalpha():
        raise AcquisitionError(
            "CONTAINER_PATH_MISMATCH",
            f"Windows host path '{cleaned}' cannot be read directly inside Linux/Docker. Use 'Select Folder' in the UI to choose the folder directly from your PC.",
            status_code=400
        )

    norm = os.path.abspath(os.path.normpath(cleaned))
    if not os.path.exists(norm):
        raise AcquisitionError("PATH_NOT_FOUND", f"Target directory does not exist on disk: {norm}", status_code=404)

    drive, rest = os.path.splitdrive(norm)
    rest_lower = rest.lower().replace("/", "\\")
    forbidden_roots = ("\\", "", "\\windows", "\\system32", "\\program files", "\\program files (x86)", "\\etc", "\\root", "\\sys", "\\proc")
    if rest_lower in forbidden_roots or rest_lower.startswith(forbidden_roots[2:]):
        raise AcquisitionError("ROOT_PATH_PROHIBITED", "Scanning operating system root directories is prohibited for security.", status_code=400)

    return norm


@contextmanager
def acquire_repository(source: str, use_corpus: bool = False, default_corpus_path: Optional[str] = None):
    """
    Context manager that acquires and prepares a repository workspace for scanning.
    Yields an AcquiredWorkspace object.
    Guarantees cleanup of temporary directories on exit (success, failure, or cancellation).
    Treats all local directories strictly as READ-ONLY.
    """
    source_clean = source.strip() if source else ""
    temp_dir: Optional[str] = None

    try:
        # Case 1: Pre-packaged controlled test corpus
        if use_corpus or source_clean == "test_corpus":
            corpus_target = default_corpus_path or os.path.abspath("test_corpus")
            yield AcquiredWorkspace(
                scan_target=corpus_target,
                display_name="controlled test_corpus",
                is_temporary=False
            )
            return

        # Case 2: Configured local target alias (e.g. "sih", "local", "sih26164", "ecdat")
        local_aliases = {"sih", "sih26164", "ecdat", "ecdat-sih2026", "local", "local_target", "configured_local", "local_sih"}
        if source_clean.lower() in local_aliases:
            local_root = get_configured_local_scan_root()
            if local_root:
                yield AcquiredWorkspace(
                    scan_target=local_root,
                    display_name=f"Configured Local Repository ({os.path.basename(local_root)})",
                    is_temporary=False
                )
                return
            else:
                raise AcquisitionError(
                    "LOCAL_ROOT_NOT_CONFIGURED",
                    "QUANTUMSHIELD_LOCAL_SCAN_ROOT environment variable is not configured or target directory does not exist.",
                    status_code=400
                )

        # Case 3: Remote GitHub HTTPS URL
        if source_clean.startswith("http://") or source_clean.startswith("https://"):
            owner, repo, ref = validate_github_url(source_clean)

            # Check if this URL corresponds to the configured local repository
            url_lower = source_clean.lower()
            if "sih" in url_lower or "ecdat" in url_lower:
                local_root = get_configured_local_scan_root()
                if local_root:
                    yield AcquiredWorkspace(
                        scan_target=local_root,
                        display_name=f"{owner}/{repo} [local: {os.path.basename(local_root)}]",
                        is_temporary=False
                    )
                    return

            # Check if a pinned local copy exists (instant air-gap evaluation)
            pinned = _resolve_pinned_target(owner, repo)
            if pinned:
                yield AcquiredWorkspace(
                    scan_target=pinned,
                    display_name=f"{owner}/{repo} (cached)",
                    is_temporary=False
                )
                return

            # Check if remote scanning is permitted
            if not is_remote_scan_enabled():
                raise AcquisitionError(
                    "REMOTE_SCAN_DISABLED",
                    "Outbound remote repository scanning is disabled by administrator policy (air-gapped mode). Please use local folder scanning or ZIP upload.",
                    status_code=403
                )

            # Create isolated temporary directory
            temp_dir = tempfile.mkdtemp(prefix="qs_git_")
            archive_zip = os.path.join(temp_dir, f"{owner}_{repo}.zip")
            extract_dir = os.path.join(temp_dir, "workspace")
            os.makedirs(extract_dir, exist_ok=True)

            _download_github_archive(owner, repo, ref, archive_zip)
            scan_dir = _safe_extract_zip(archive_zip, extract_dir)

            yield AcquiredWorkspace(
                scan_target=scan_dir,
                display_name=f"https://github.com/{owner}/{repo}",
                is_temporary=True,
                temp_root=temp_dir
            )
            return

        # Case 4: Local directory path
        local_target = _validate_local_path(source_clean)
        yield AcquiredWorkspace(
            scan_target=local_target,
            display_name=os.path.basename(local_target) or local_target,
            is_temporary=False
        )

    finally:
        # Guarantee zero residual files in temporary workspace
        if temp_dir and os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except Exception:
                pass
