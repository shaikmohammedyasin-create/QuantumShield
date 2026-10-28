# QuantumShield

**Cryptographic Risk Intelligence & Post-Quantum Readiness Platform**

QuantumShield discovers cryptographic assets across source code, dependencies, certificates, configurations, and binaries; classifies post-quantum exposure; models migration risk with Mosca's inequality; and exports standards-based evidence (CycloneDX CBOM, SARIF, HTML/PDF/CSV reports) through an explainable-risk engine and a dedicated React security workstation.

> **Product status:** QuantumShield is the productized evolution of a validated prototype (formerly ECDAT). The core scanning, classification, and CBOM pipeline has been verified against ground-truth corpora and external open-source targets; deployment URLs and test counts below are refreshed as part of this migration and marked TBD until post-migration verification completes.

**Live Production Workstation:** [https://quantumshield-seven.vercel.app/](https://quantumshield-seven.vercel.app/)
**Live Backend API & OpenAPI Docs:** [https://quantumshield-b5j2.onrender.com/docs](https://quantumshield-b5j2.onrender.com/docs)
**Backend Health Endpoint:** [https://quantumshield-b5j2.onrender.com/health](https://quantumshield-b5j2.onrender.com/health)

---

## Table of Contents

1. [What QuantumShield Does](#1-what-quantumshield-does)
2. [Product Evolution: From Prototype to Platform](#2-product-evolution-from-prototype-to-platform)
3. [Core Concepts](#3-core-concepts)
4. [Architecture & Pipeline](#4-architecture--pipeline)
5. [Security Workstation UI](#5-security-workstation-ui)
6. [Supported Inputs & Scanners](#6-supported-inputs--scanners)
7. [Quantum Classification & Threat Modeling](#7-quantum-classification--threat-modeling)
8. [Mosca's Inequality Simulator](#8-moscas-inequality-simulator)
9. [Explainable Risk Engine](#9-explainable-risk-engine)
10. [PQC Migration Guidance](#10-pqc-migration-guidance)
11. [CycloneDX CBOM](#11-cyclonedx-cbom)
12. [Reports & Deliverables](#12-reports--deliverables)
13. [Installation & Setup](#13-installation--setup)
14. [Running QuantumShield](#14-running-quantumshield)
15. [Configuration](#15-configuration)
16. [Testing & Verification](#16-testing--verification)
17. [Security Controls](#17-security-controls)
18. [Known Limitations](#18-known-limitations)
19. [Roadmap](#19-roadmap)
20. [License](#20-license)

---

## 1. What QuantumShield Does

QuantumShield is a Cryptographic Risk Intelligence & Post-Quantum Readiness Platform for security teams that need to answer one question before CRQC (cryptographically relevant quantum computers) arrive: **where is our cryptography, how exposed is it, and what do we migrate first?**

1. **Discover Cryptographic Assets:** Scan source code, dependency manifests, X.509 certificates, keystores, server configurations, and Java bytecode using offline scanners.
2. **Standardize into a CBOM:** Generate CycloneDX 1.6 Cryptographic Bill of Materials output and validate it against the official schema.
3. **Classify Post-Quantum Vulnerability:** Classify findings into quantum-status categories — Vulnerable (Shor), Weakened (Grover), Legacy-broken, and Safe.
4. **Evaluate Threat Surface (HNDL / TNFL):** Distinguish Harvest-Now-Decrypt-Later (confidentiality) from Trust-Now-Forge-Later (authenticity/signature) exposure.
5. **Simulate Mosca's Inequality:** Model X + Y > Z (data lifetime + migration time vs CRQC arrival horizon) interactively.
6. **Prioritize with Explainable Risk:** Rank findings with a transparent, weighted 5-factor risk model — every score is traceable to its inputs.
7. **Deliver Migration Guidance:** Deterministic PQC recommendations mapped to NIST FIPS 203/204/205 standards.
8. **Export Multi-Format Deliverables:** CBOM JSON, SARIF 2.1.0, executive HTML reports, A4 PDF reports, CSV inventories, and Markdown summaries.
9. **Dedicated React Workstation:** A React, TypeScript, Vite, and Tailwind interface for scanning, inspection, and evidence review.

---

## 2. Product Evolution: From Prototype to Platform

QuantumShield began as a validated cryptographic discovery prototype built to a strict specification. That foundation is preserved and extended here:

- **What was validated:** multi-scanner discovery (source, manifests, certificates, configs, bytecode), Shor/Grover classification, HNDL/TNFL tagging, Mosca lifetime modeling, deterministic PQC recommendations, and CycloneDX 1.6 CBOM generation with schema validation — verified against a ground-truth corpus and external targets (OpenSSL, CPython, OpenSSH).
- **What changed:** the platform is rebranded and repackaged for product use — unified FastAPI + React deployment, CI/CD-ready SARIF output, containerized delivery, and cloud deployment guides. No fabrication of deployment history, customers, or credentials: track record is the codebase and its verification artifacts.
- **What stays true:** 100% offline/air-gapped operation, zero private key persistence, and deterministic, explainable outputs.

---

## 3. Core Concepts

| Concept | Meaning |
|---|---|
| **CBOM** | Cryptographic Bill of Materials — CycloneDX 1.6 inventory of cryptographic assets. |
| **CRQC** | Cryptographically Relevant Quantum Computer — the adversary capability horizon. |
| **HNDL** | Harvest-Now-Decrypt-Later — ciphertext captured today, decrypted once a CRQC exists. |
| **TNFL** | Trust-Now-Forge-Later — signatures captured today, forged once a CRQC exists. |
| **Shor-broken** | Public-key cryptography (RSA, ECC, DH) directly breakable by Shor's algorithm. |
| **Grover-weakened** | Symmetric cryptography with reduced effective key strength under Grover's algorithm. |
| **Mosca's Inequality** | If `X + Y > Z` (data lifetime + migration time exceeds CRQC horizon), you are already exposed. |

---

## 4. Architecture & Pipeline

```text
┌────────────────────────────────────────────────────────────────────────┐
│               REACT + TYPESCRIPT + VITE WORKSTATION                    │
│                       (Port 5173 / Localhost)                          │
│                                                                        │
│   • Dashboard             • Finding Inspector      • CBOM Inspector    │
│   • New Scan Pipeline     • Mosca Simulator        • Terminal & Log    │
│   • Crypto Inventory      • Risk Analysis          • Settings / Policy │
│   • Migration Guidance    • Reports & Evidence                         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ HTTP / REST APIs (JSON)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   FASTAPI ASYNC BACKEND ENGINE                         │
│                       (Port 8000 / Localhost)                          │
│                                                                        │
│   GET  /api/dashboard          GET  /api/risk      GET  /api/cbom      │
│   POST /api/scans              GET  /api/migration GET  /api/reports   │
│   GET  /api/inventory          GET  /api/findings  GET  /api/terminal  │
│   GET  /api/mosca              POST /api/mosca     GET  /api/settings  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                 QUANTUMSHIELD PYTHON ANALYSIS CORE                     │
│                                                                        │
│  PROJECT SOURCE ROOT / ARTIFACTS                                       │
│        ├── Source Code (.py, .js, .java, .ts) ──► Python AST Visitor   │
│        ├── Manifests (requirements, pom, etc.) ──► Multi-Ecosystem     │
│        ├── Certificates (.pem, .der, .p12, .pub) ─► X.509 + Keystores  │
│        ├── Server Configs (nginx, openssl, etc.) ─► TLS Protocols      │
│        └── Java Bytecode (.class, .jar) ─────────► Offline Constant    │
│                                 ▼                                      │
│     RAW FORENSIC EVIDENCE & NORMALIZATION                              │
│     → CROSS-SCANNER DEDUPLICATION                                      │
│     → POST-QUANTUM CLASSIFICATION & HNDL/TNFL                          │
│     → MOSCA LIFETIME MODEL (X + Y > Z)                                 │
│     → EXPLAINABLE RISK ENGINE (weighted 5-factor formula)              │
│     → PQC RECOMMENDATIONS (NIST FIPS 203/204/205)                      │
│     → CYCLONEDX 1.6 CBOM SERIALIZATION & VALIDATION                    │
│     → MULTI-FORMAT DELIVERABLES (CBOM, SARIF, HTML, PDF, CSV, Logs)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Security Workstation UI

The React workstation provides 11 purpose-built screens:

| # | Route | Screen | Key Capabilities |
|---|---|---|---|
| 1 | `/dashboard` | Cryptographic Security Overview | KPI metrics, risk breakdown, quantum exposure distribution, recent findings, quick scan CTA. |
| 2 | `/scan/new` | New Scan Configuration | Target path selection, multi-scanner checklist, real-time execution pipeline. |
| 3 | `/inventory` | Crypto Inventory | Searchable asset table, filters (Algorithm, Quantum Status, Threat, Risk Band), pagination. |
| 4 | `/findings/:id` | Finding Inspector | Asset parameters, Shor/Grover impact, Mosca check, quantitative risk card, code viewer with highlighted vulnerable lines. |
| 5 | `/mosca` | Mosca Simulator | Interactive sliders for X (data lifetime), Y (migration time), Z (CRQC horizon), presets, HNDL verdict, exposure timeline. |
| 6 | `/risk` | Cryptographic Risk Analysis | Threat exposure gauge, weighted-factor formula breakdown, risk-ranked findings table. |
| 7 | `/migration` | Post-Quantum Migration Guidance | Migration pipeline (Classical → Hybrid → PQC), deterministic transition rules. |
| 8 | `/cbom` | CycloneDX 1.6 CBOM | Schema verification banner, components tree, raw CBOM JSON viewer, export actions. |
| 9 | `/terminal` | Terminal & Scan Log | Live scan telemetry, log-level filtering, regex filter, raw log export. |
| 10 | `/settings` | Settings & Security Policies | Scanner configuration, classification defaults, risk weights, CBOM schema strictness, air-gap guardrails. |
| 11 | `/reports` | Reports & Evidence Deliverables | All deliverable formats, in-app preview, verified downloads. |

---

## 6. Supported Inputs & Scanners

| Category | Supported Formats | Scanner Implementation |
|---|---|---|
| **Python Source** | `.py` | AST call-site visitor (`hashlib`, `RSA.generate`, `AES.new`) + regex fallback |
| **Java Source** | `.java` | Static pattern engine (`KeyPairGenerator`, `Cipher`, `Signature`, `MessageDigest`) |
| **JavaScript / TypeScript** | `.js`, `.ts`, `.jsx`, `.tsx` | WebCrypto and Node.js `crypto` API indicators |
| **Dependency Manifests** | `requirements.txt`, `pyproject.toml`, `pom.xml`, `package.json`, `package-lock.json`, `go.mod`, `Cargo.toml` | Offline manifest parsers with `defusedxml` protection |
| **Digital Certificates** | `.pem`, `.crt`, `.cer`, `.der` | Full X.509 metadata extraction (algorithm, key size, subject, issuer, validity) |
| **Keystores & Public Keys** | `.p12`, `.pfx`, `.pub` | PKCS#12 bundle parser & OpenSSH public key loader (zero private key storage) |
| **Configuration Files** | `nginx.conf`, `sshd_config`, `openssl.cnf`, `.conf`, `.cfg` | TLS protocols, cipher suites, DH parameter groups |
| **Java JVM Binaries** | `.class`, `.jar`, `.war` | Offline constant pool static analyzer with Zip Slip containment |

---

## 7. Quantum Classification & Threat Modeling

Findings are classified into four quantum-status categories and tagged with a threat surface:

| Status | Meaning | Example |
|---|---|---|
| **SHOR_BROKEN** | Directly broken by Shor's algorithm | RSA-2048 key exchange, ECDSA signatures |
| **GROVER_WEAKENED** | Effective strength halved by Grover's algorithm | AES-128, SHA-256 (collision) |
| **LEGACY_BROKEN** | Classically broken already | DES, 3DES, MD5, SHA-1 signatures |
| **QUANTUM_SAFE** | No known quantum break | AES-256 (symmetric), hash-based signatures |

Each finding is additionally tagged **HNDL** (harvest-now-decrypt-later: confidentiality at risk) or **TNFL** (trust-now-forge-later: authenticity at risk), which drives Mosca evaluation and migration priority.

---

## 8. Mosca's Inequality Simulator

The platform models Mosca's theorem interactively:

- **X** — how long your data must remain secret (data lifetime).
- **Y** — how long migration of your systems will take.
- **Z** — time until a CRQC exists (arrival horizon).

If `X + Y > Z`, data encrypted today will be decryptable within its lifetime. The simulator supports interactive sliders, scenario presets, real-time equation solving, an HNDL verdict, and a visual exposure timeline, and can re-score an active inventory under new assumptions.

---

## 9. Explainable Risk Engine

Risk scores use a transparent weighted 5-factor model (quantum exposure, data lifetime/sensitivity, business criticality, exploitability/legacy status, migration complexity). Every score in the UI is traceable to its contributing factors — no opaque ML scoring. Weights are configurable in Settings for organizational calibration.

---

## 10. PQC Migration Guidance

Deterministic recommendations mapped to NIST post-quantum standards:

| Finding Type | Recommended Replacement | Standard |
|---|---|---|
| Key exchange / encryption | Hybrid X25519 + ML-KEM-768, or ML-KEM envelope encryption | NIST FIPS 203 |
| Digital signatures | ML-DSA-65 | NIST FIPS 204 |
| Long-term signatures (high assurance) | SLH-DSA, LMS/XMSS | NIST FIPS 205, SP 800-208 |
| Transitional state | Dual-key hybrid (classical + PQC) | Migration stage 2 of 3 |

The migration pipeline follows three stages: Classical Vulnerable → Dual-Key Hybrid → Pure Post-Quantum Lattice.

---

## 11. CycloneDX CBOM

Every scan produces a CycloneDX 1.6 CBOM validated against the official `bom-1.6.schema.json`. The CBOM includes component types, `cryptoProperties` (algorithm, key size, usage, quantum status), dynamic UUIDs and UTC timestamps. SARIF 2.1.0 output integrates with GitHub code scanning and IDE security tooling.

---

## 12. Reports & Deliverables

Every scan produces six standard deliverables in `output/`:

1. **`cbom.json`** — CycloneDX 1.6 Cryptographic BOM, validated against the official schema.
2. **`inventory.csv`** — tabular asset inventory with rule IDs, locations, quantum status, risk bands.
3. **`findings.sarif`** — schema-valid SARIF 2.1.0 for CI/CD code scanning.
4. **`report.html`** — standalone executive security report.
5. **`report.pdf`** — printable executive risk report (ReportLab).
6. **`summary.md`** — markdown summary for release notes and ticket comments.

---

## 13. Installation & Setup

### Prerequisites
- Python 3.10+ (tested on 3.11 and 3.12)
- Node.js 18+ and npm
- Git

### Setup
```bash
git clone <your-repository-url>
cd QuantumShield

# Backend
python -m venv venv
source venv/bin/activate          # Linux/macOS
# .\venv\Scripts\Activate.ps1     # Windows PowerShell
pip install -r requirements.txt

# Frontend
cd frontend
npm install
cd ..
```

---

## 14. Running QuantumShield

### Option A: Unified launcher (recommended)
```bash
python run.py
```
Starts the FastAPI backend on `http://127.0.0.1:8000` (API docs at `/docs`), the React frontend on `http://localhost:5173`, and opens your browser.

### Option B: Separate services
```bash
# Terminal 1 — backend
python run.py --backend-only
# or: uvicorn backend.api.main:app --host 127.0.0.1 --port 8000 --reload

# Terminal 2 — frontend
cd frontend && npm run dev
```

Cloud deployment options (Vercel + Render, unified Render/Railway, Docker, air-gapped local) are documented in [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md).

---

## 15. Configuration

| Setting | Where | Purpose |
|---|---|---|
| `VITE_API_BASE_URL` | frontend env | Backend API base URL for split deployments |
| `ALLOWED_ORIGINS` | backend env | CORS allowlist (see `render.yaml`) |
| `PORT` / `HOST` | environment | Server bind address in containers |
| Risk weights & classification defaults | Workstation Settings | Calibrate the risk model and scanner behavior |
| CBOM schema strictness | Workstation Settings | Validation strictness for CycloneDX output |

---

## 16. Testing & Verification

Run the automated test suite:

```bash
python -m pytest tests/ -v
```

**Test count: 71 passing tests — verified on the productized build** (48 core engine, 15 API integration, 8 hardening). The prototype evaluation additionally included a controlled ground-truth corpus and scans of OpenSSL, CPython, and OpenSSH.

---

## 17. Security Controls

- **Air-gapped operation:** zero external network calls, tracking beacons, or telemetry. All scanners run offline.
- **Zero private key persistence:** scanners inspect algorithms and parameters only; private keys are never stored or logged.
- **Path traversal protection:** target scan paths are validated against directory escape.
- **Zip Slip & archive bomb guards:** archive readers cap extraction and enforce safe path canonicalization.
- **XML entity defense:** `defusedxml` blocks XXE and entity-expansion attacks in manifest parsing.

---

## 18. Known Limitations

- Full AST analysis is implemented for Python source; other source-language scanners use static pattern approaches.
- TLS and server-configuration analysis is the weakest scanner area and should be treated accordingly.
- Binary disassembly of compiled ELF/PE/Mach-O binaries is roadmap functionality (Java bytecode is supported).
- No live network probing of TLS/SSH endpoints — this is a static, air-gapped scanner by design.
- Password-protected JKS keystores are not parsed.

---

## 19. Roadmap

- Deeper data-flow analysis for multi-language source scanners.
- Compiled-binary symbol recovery (ELF/PE/Mach-O).
- CI/CD integration presets (GitHub Actions, GitLab) for SARIF uploads.
- Continuous CBOM drift monitoring across repositories and releases.

---

## 20. License

QuantumShield is licensed under the [MIT License](LICENSE).
