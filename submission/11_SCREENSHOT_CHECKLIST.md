# QuantumShield — Screenshot Checklist

## Recommended Screenshots (target: submission/screenshots/)

| # | Filename | Screen / Focus |
|---|---|---|
| 01 | `01_dashboard.png` | Dashboard overview (KPIs, risk distribution, recent findings) |
| 02 | `02_scan.png` | New Scan configuration + pipeline progress |
| 03 | `03_inventory.png` | Crypto Inventory filtered by quantum status |
| 04 | `04_findings.png` | Finding Inspector (algorithm, parameters, evidence, risk card, code viewer) |
| 05 | `05_risk_center.png` | Risk Center (threat gauge, 5-factor formula, ranked table) |
| 06 | `06_migration.png` | Migration pipeline (Classical → Hybrid → PQC) |
| 07 | `07_cbom.png` | CBOM Inspector (schema verification banner + components tree) |
| 08 | `08_reports.png` | Reports & Evidence Deliverables list |

## Capture Guidance

- **Source:** Production deployment at https://quantumshield-seven.vercel.app (preferred) or local run.
- **Browser:** Use a clean profile / incognito; set viewport to 1920×1080 or 1440×900.
- **Clean UI:** Hide browser clutter (bookmarks bar, extensions, devtools, console).
- **Content:** Ensure at least one completed scan is loaded so inventory/findings/risk CBOM data is populated.
- **Naming:** Use exactly the filenames listed so the deck and README stay consistent.

## Existing E2E Screenshots (in `tests/results/`)

The repository already contains `e2e_01_dashboard.png` … `e2e_11_finding_inspector.png`. These can be used as a starting set; verify they are from the most recent build before submission.

## Capture Method

- Automated: use browser automation (screenshot tool) to capture the production UI.
- Manual: use OS screenshot tools (Snipping Tool / Cmd+Shift+4) with clean viewport.
- Save to `submission/screenshots/` and commit only the final, reviewed set (keep the directory free of temp captures).
