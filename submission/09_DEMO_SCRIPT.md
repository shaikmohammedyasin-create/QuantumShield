# QuantumShield — Demo Script (5 minutes)

## 0:00–0:30 | The Problem

*"Security teams cannot see their own cryptography. Key exchange and digital signatures are embedded across source code, certificates, manifests, and server configuration, yet most organizations have no asset-level inventory. Add a quantum computer, and Harvester-Now-Decrypt-Later becomes the weakest word in your threat model..."*

## 0:30–1:00 | QuantumShield Overview

*"QuantumShield turns a codebase into a cryptographic risk intelligence pipeline."*
*"It discovers, normalizes, and classifies cryptographic assets, scores them by risk, and prescribes a NIST-mapped post-quantum migration strategy — entirely offline."*
*"This is the public workstation..."* (walk through the production UI in 20 seconds).

## 1:00–2:00 | Run a Scan

*"Let's scan a representative environment."*
1. Open **New Scan**.
2. Choose the local/test corpus path (or the pre-loaded sample-project target).
3. Start scan.
4. Point out the scan pipeline stages and progress bar.
5. Land on **Inventory** when the scan completes.

## 2:00–2:40 | Cryptographic Inventory + Findings

*"The inventory lists every algorithm, usage, location, and owner."*
1. Filter **Quantum Status = SHOR_BROKEN**.
2. Click one **Finding** (e.g., RSA-2048 in crypto_sample.py).
3. Show highlighted line, algorithm parameters, evidence snippet, Mosca check, and risk card.

## 2:40–3:20 | Risk Center

*"Risk ranking forces a migration priority."*
1. Open **Risk Center**.
2. Show 5-factor breakdown with weighted values.
3. Point out top prioritized assets.
4. Emphasize explainability: *"Every score traces to inputs that an auditor can see."*

## 3:20–4:00 | Migration

*"From finding to migration plan."*
1. Open **Migration**.
2. Highlight pipeline stages (Classical → Hybrid → Pure PQC).
3. Map RSA finding to ML-KEM-768 and AES to AES-256-GCM.
4. Show status update capability.

## 4:00–4:30 | CBOM & Reports

*"The artifacts travel with the team."*
1. Open **CBOM** and show schema validation banner (valid) + raw JSON peek.
2. Generate and download a report (HTML or PDF).
3. Show download list / copy CBOM export.

## 4:30–5:00 | Impact & Closing

*"QuantumShield doesn't patch vulnerabilities — it does the first step that every PQC program needs but lacks: an asset-level, explainable, offline inventory with a migration order."*
*"Open source implementation, FastAPI plus React, production-deployed at [Vercel URL], and fully runnable offline."*
*"Thank you."*

## Notes for Narration

- Keep PII/hr details out; product code only.
- Demos pivot quickly; have screenshots in `submission/screenshots/` ready if the deployed backend is slow on Render (free tier may cold-start).
- Never show keys/credentials.
- Close by stating the exact verified metrics (71 tests, 100% precision/OSS metrics, 0 CBOM errors, 6 report formats).
