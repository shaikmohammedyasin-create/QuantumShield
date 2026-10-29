# QuantumShield — Demo Checklist

## Pre-Demo (10 minutes before)

- [ ] Confirm production URLs load: https://quantumshield-seven.vercel.app (frontend), https://quantumshield-b5j2.onrender.com/health (backend). Hit `/health` first to warm Render (free tier cold-start).
- [ ] Clear browser cache or use incognito to avoid stale state.
- [ ] Open tabs in order: Dashboard, New Scan, Inventory, Findings, Risk, Migration, CBOM, Reports.
- [ ] Have `submission/screenshots/` open as fallback if the deployed backend is slow.
- [ ] Have the demo script printed or visible on a second screen.

## Exact Actions

1. Open production URL.
2. Show **Dashboard** (Overview) — KPI cards and risk distribution.
3. Start a **Scan** — show pipeline stages + progress.
4. Show **Cryptographic Inventory** — filter by quantum status.
5. Open a **Finding** — show asset parameters, Shor/Grover impact, Mosca check, risk card, code viewer.
6. Open **Risk Center** — show threat exposure gauge, 5-factor formula breakdown, risk-ranked table.
7. Open **Migration** — show the Classical → Hybrid → PQC pipeline and update migration status.
8. Open **CBOM** — show schema verification banner, components tree, raw JSON.
9. Generate/download a **Report** (HTML or PDF).
10. Return to **Dashboard** and close with business value.

## DO NOT Click During Demo

- Do not click "Settings" unless specifically asked about risk weights or CBOM strictness.
- Do not trigger long external scans from the demo.
- Do not open the Terminal tab unless showing logs.
- Do not run any destructive or reset actions.
- Do not expose any API keys, secrets, or private keys.
- Do not navigate to the local SIH repository (read-only test input).
