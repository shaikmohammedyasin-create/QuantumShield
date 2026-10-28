"""
Automated unit tests for QuantumShield Repository Acquisition Layer.
Verifies URL validation, SSRF protection, Zip-Slip guard, archive safety,
mocked remote acquisition, temporary workspace cleanup, and local scan root resolution.
"""
import io
import os
import sys
import tempfile
import urllib.error
import zipfile
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.api.repository_acquisition import (
    validate_github_url,
    acquire_repository,
    AcquisitionError,
    _safe_extract_zip,
    get_configured_local_scan_root
)
from app.pipeline import run_full_scan


def test_valid_github_url():
    owner, repo, ref = validate_github_url("https://github.com/shaikmohammedyasin-create/QuantumShield")
    assert owner == "shaikmohammedyasin-create"
    assert repo == "QuantumShield"
    assert ref is None


def test_valid_github_url_with_git_and_branch():
    owner, repo, ref = validate_github_url("https://github.com/owner/my-repo.git/tree/develop")
    assert owner == "owner"
    assert repo == "my-repo"
    assert ref == "develop"


def test_http_url_rejected():
    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("http://github.com/owner/repo")
    assert exc.value.detail["error"] == "INSECURE_SCHEME"


def test_non_github_host_rejected():
    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("https://gitlab.com/owner/repo")
    assert exc.value.detail["error"] == "UNSUPPORTED_HOST"


def test_localhost_ssrf_rejected():
    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("https://localhost/owner/repo")
    assert exc.value.detail["error"] == "SSRF_PROHIBITED"

    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("https://127.0.0.1/owner/repo")
    assert exc.value.detail["error"] == "SSRF_PROHIBITED"


def test_private_ip_ssrf_rejected():
    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("https://192.168.1.100/owner/repo")
    assert exc.value.detail["error"] == "SSRF_PROHIBITED"

    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("https://10.200.1.5/owner/repo")
    assert exc.value.detail["error"] == "SSRF_PROHIBITED"


def test_malformed_url_command_injection_rejected():
    with pytest.raises(AcquisitionError) as exc:
        validate_github_url("https://github.com/owner/repo;ls")
    assert exc.value.detail["error"] == "MALFORMED_URL"


def test_repository_not_found_error():
    err = urllib.error.HTTPError("https://api.github.com", 404, "Not Found", {}, None)
    with patch("urllib.request.urlopen", side_effect=err):
        with pytest.raises(AcquisitionError) as exc:
            with acquire_repository("https://github.com/unknown-org-99/non-existent-repo-99"):
                pass
        assert exc.value.detail["error"] == "REPOSITORY_NOT_FOUND"
        assert exc.value.status_code == 404


def test_download_timeout_error():
    with patch("urllib.request.urlopen", side_effect=TimeoutError("Request timed out")):
        with pytest.raises(AcquisitionError) as exc:
            with acquire_repository("https://github.com/slow-org/slow-repo"):
                pass
        assert exc.value.detail["error"] == "NETWORK_TIMEOUT"


def test_zip_slip_protection():
    tmp_dir = tempfile.mkdtemp(prefix="qs_slip_test_")
    zip_path = os.path.join(tmp_dir, "malicious.zip")
    extract_dir = os.path.join(tmp_dir, "extract")
    os.makedirs(extract_dir, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, "w") as zf:
            zf.writestr("../../evil.txt", "malicious payload")

        with pytest.raises(AcquisitionError) as exc:
            _safe_extract_zip(zip_path, extract_dir)
        assert exc.value.detail["error"] == "ZIP_SLIP_ATTEMPT"
    finally:
        import shutil
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_archive_too_many_files():
    tmp_dir = tempfile.mkdtemp(prefix="qs_bomb_test_")
    zip_path = os.path.join(tmp_dir, "many_files.zip")
    extract_dir = os.path.join(tmp_dir, "extract")
    os.makedirs(extract_dir, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, "w") as zf:
            for i in range(5005):
                zf.writestr(f"file_{i}.txt", "content")

        with pytest.raises(AcquisitionError) as exc:
            _safe_extract_zip(zip_path, extract_dir)
        assert exc.value.detail["error"] == "ARCHIVE_TOO_MANY_FILES"
        assert exc.value.status_code == 413
    finally:
        import shutil
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_corrupt_archive():
    tmp_dir = tempfile.mkdtemp(prefix="qs_corrupt_test_")
    zip_path = os.path.join(tmp_dir, "bad.zip")
    extract_dir = os.path.join(tmp_dir, "extract")
    os.makedirs(extract_dir, exist_ok=True)

    try:
        with open(zip_path, "wb") as f:
            f.write(b"NOT A VALID ZIP HEADER")

        with pytest.raises(AcquisitionError) as exc:
            _safe_extract_zip(zip_path, extract_dir)
        assert exc.value.detail["error"] == "CORRUPT_ARCHIVE"
    finally:
        import shutil
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_remote_scanning_disabled_mode():
    with patch("backend.api.repository_acquisition.is_remote_scan_enabled", return_value=False):
        with pytest.raises(AcquisitionError) as exc:
            with acquire_repository("https://github.com/any-owner/any-repo"):
                pass
        assert exc.value.detail["error"] == "REMOTE_SCAN_DISABLED"
        assert exc.value.status_code == 403


def test_configured_local_scan_root_resolution():
    tmp_repo = tempfile.mkdtemp(prefix="qs_local_sih_")
    try:
        # Create a sample file
        with open(os.path.join(tmp_repo, "crypto.py"), "w") as f:
            f.write("import hashlib\nh = hashlib.sha256().hexdigest()")

        with patch.dict(os.environ, {"QUANTUMSHIELD_LOCAL_SCAN_ROOT": tmp_repo}):
            # Test 1: alias 'sih'
            with acquire_repository("sih") as ws:
                assert ws.scan_target == tmp_repo
                assert ws.is_temporary is False

            # Test 2: alias 'local'
            with acquire_repository("local") as ws:
                assert ws.scan_target == tmp_repo

            # Test 3: URL matching SIH
            with acquire_repository("https://github.com/shaikmohammedyasin-create/ECDAT-SIH2026") as ws:
                assert ws.scan_target == tmp_repo
                assert ws.is_temporary is False
    finally:
        import shutil
        shutil.rmtree(tmp_repo, ignore_errors=True)


def test_successful_remote_acquisition_and_ast_scan():
    # Build a valid mock zip in memory
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("test-repo-main/crypto_test.py", "from cryptography.hazmat.primitives.asymmetric import rsa\nk = rsa.generate_private_key(65537, 2048)")
    mock_zip_bytes = buf.getvalue()

    mock_resp = MagicMock()
    mock_resp.status = 200
    mock_resp.read.side_effect = [mock_zip_bytes, b""]
    mock_resp.__enter__.return_value = mock_resp

    with patch("urllib.request.urlopen", return_value=mock_resp):
        with acquire_repository("https://github.com/mock-org/crypto-sample") as ws:
            assert ws.is_temporary is True
            temp_root = ws.temp_root
            assert os.path.isdir(ws.scan_target)

            # Run actual AST engine on acquired repo
            assets, metrics = run_full_scan(ws.scan_target)
            assert len(assets) >= 1
            assert assets[0].algorithm == "RSA"
            assert assets[0].quantum_status.value == "Vulnerable"

        # Verify temporary workspace is completely cleaned up
        assert not os.path.exists(temp_root), "Temporary workspace must be cleaned up on context exit!"


def test_existing_local_folder_scan_regression():
    with acquire_repository("test_corpus") as ws:
        assert ws.is_temporary is False
        assert os.path.isdir(ws.scan_target)
        assets, metrics = run_full_scan(ws.scan_target)
        assert len(assets) == 25
