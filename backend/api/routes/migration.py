"""
Migration Guidance Route Handler.
GET /api/migration - Deterministic PQC transition recommendations based on NIST FIPS 203/204/205.
"""
import json
from pathlib import Path
from typing import Dict

from fastapi import APIRouter, HTTPException

from backend.api.state import state
from backend.api.schemas import (
    MigrationResponse,
    MigrationItem,
    MigrationTrackingItem,
    MigrationTrackingSummary,
    MigrationStatusUpdate,
)

router = APIRouter(prefix="/api/migration", tags=["migration"])

STATUS_FILE = Path(__file__).resolve().parents[2] / "data" / "migration_status.json"
VALID_STATUSES = {"Not Started", "Planned", "In Progress", "Migrated", "Verified"}

CANDIDATE_STATUSES = {"Vulnerable", "Weakened", "Legacy-broken"}


def _load_tracking_status() -> Dict[str, str]:
    if not STATUS_FILE.exists():
        return {}
    try:
        with STATUS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items()}
    except (json.JSONDecodeError, OSError):
        pass
    return {}


def _save_tracking_status(data: Dict[str, str]) -> None:
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with STATUS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@router.patch("/status")
def update_migration_status(payload: MigrationStatusUpdate):
    if payload.status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail=f"Invalid status: {payload.status}")
    status_map = _load_tracking_status()
    status_map[payload.key] = payload.status
    _save_tracking_status(status_map)
    return {"success": True, "key": payload.key, "status": payload.status}


@router.get("", response_model=MigrationResponse)
def get_migration_guidance():
    assets = state.assets
    seen = set()
    items = []

    for a in sorted(assets, key=lambda x: x.risk_score, reverse=True):
        sig = (a.algorithm, a.usage.value)
        if sig not in seen and a.recommendation:
            seen.add(sig)
            target = a.recommendation.split(":")[-1].strip() if ":" in a.recommendation else a.recommendation
            strategy = "Hybrid Transition (Dual-Cert/KEM)" if a.hybrid_option else "Direct Primitive Replacement"
            items.append(MigrationItem(
                algorithm=a.algorithm,
                primitive=a.usage.value,
                risk_score=round(a.risk_score, 1),
                risk_band=a.risk_band,
                recommended_target=target,
                migration_strategy=strategy,
                standard=a.standard or "NIST PQC Standards",
                effort=a.migration_effort or "Moderate",
                migration_path=a.migration_path or []
            ))

    standards_dict = {
        "FIPS_203": "NIST FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)",
        "FIPS_204": "NIST FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)",
        "FIPS_205": "NIST FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA)",
        "SP_800_56C": "NIST SP 800-56C Rev 2: Recommendation for Key-Derivation Methods in Key-Establishment Schemes",
    }

    # Calculate actual summary metrics across active scanned codebase
    imm_assets = [a for a in assets if a.quantum_status.value == "Vulnerable"]
    hyb_assets = [a for a in assets if a.hybrid_option]
    dep_assets = [a for a in assets if a.quantum_status.value == "Legacy-broken"]
    comp_assets = [
        a for a in assets
        if a.quantum_status.value in ("Safe", "PQC-ready") or a.quantum_vuln_class.value == "QUANTUM_SAFE"
    ]

    summary = {
        "immediate_count": len(imm_assets),
        "immediate_algos": sorted(list(set(a.algorithm for a in imm_assets))),
        "hybrid_count": len(hyb_assets),
        "hybrid_algos": sorted(list(set(a.algorithm for a in hyb_assets))),
        "deprecate_count": len(dep_assets),
        "deprecate_algos": sorted(list(set(a.algorithm for a in dep_assets))),
        "compliant_count": len(comp_assets),
        "compliant_algos": sorted(list(set(a.algorithm for a in comp_assets))),
    }

    tracking_status = _load_tracking_status()
    tracking = []
    for idx, a in enumerate(
        [x for x in assets if x.quantum_status.value in CANDIDATE_STATUSES]
    ):
        key = f"{a.rule_id or ''}|{a.file_path}|{a.line_number}"
        rec = a.recommendation or ""
        target = rec.split(":")[-1].strip() if ":" in rec else rec
        tr = MigrationTrackingItem(
            id=idx,
            rule_id=a.rule_id or "",
            algorithm=a.algorithm,
            primitive=a.primitive,
            file_name=Path(a.file_path).name,
            file_path=a.file_path,
            line_number=int(a.line_number),
            risk_band=a.risk_band,
            recommendation=target if target else rec,
            status=tracking_status.get(key, "Not Started"),
        )
        tracking.append(tr)

    counts = {"Migrated": 0, "Verified": 0, "In Progress": 0, "Planned": 0, "Not Started": 0}
    for t in tracking:
        if t.status in counts:
            counts[t.status] += 1
    total = len(tracking)
    migrated = counts["Migrated"]
    verified = counts["Verified"]
    progress_percent = round((migrated + verified) / total * 100, 1) if total > 0 else 0.0
    tracking_summary = MigrationTrackingSummary(
        total=total,
        migrated=migrated,
        verified=verified,
        in_progress=counts["In Progress"],
        planned=counts["Planned"],
        not_started=counts["Not Started"],
        progress_percent=progress_percent,
    )

    return MigrationResponse(
        matrix=items,
        standards=standards_dict,
        summary=summary,
        tracking=tracking,
        tracking_summary=tracking_summary,
    )