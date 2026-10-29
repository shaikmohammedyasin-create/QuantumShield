# QuantumShield — Ready-to-Paste Submission Form Answers

> For MG Solutions Build Spark Hackathon → `https://hackathon.mgsolutions.sbs/hackathons/build-spark-hackathon/submit` (Round 1 — Idea Submission).
> Cutoff: **11/1/2026, 11:59:59 PM IST**. Submit early; endpoints return 403 after cutoff.

---

## FIELD: PROJECT TITLE

**ANSWER:**
QuantumShield: Cryptographic Risk Intelligence & Post-Quantum Readiness Platform

**LIMIT:** Not specified on form.
**NOTES:** Use this exact title consistently across all artifacts.

---

## FIELD: PROBLEM STATEMENT

**ANSWER:**
Security teams cannot see their own cryptography. Cryptographic primitives are embedded invisibly across source code, dependency manifests, X.509 certificates, keystores, server configurations, and Java bytecode — and no mainstream tool produces a complete, standards-based cryptographic inventory in one pass. Quantum computing turns that invisibility into a time-boxed risk: Shor's algorithm will break RSA, DSA, ECDSA, ECDH, and Diffie-Hellman once a cryptographically relevant quantum computer (CRQC) exists, and Grover's algorithm halves the effective security of symmetric ciphers. Harvest-Now-Decrypt-Later (HNDL) means ciphertext captured today will be decryptable within its lifetime, and Trust-Now-Forge-Later (TNFL) means signatures captured today can be forged retroactively. Without an inventory, an organization cannot answer the four questions a quantum-readiness program starts with: which systems use Shor-vulnerable algorithms, which protect data that outlives the CRQC horizon, which signatures can be forged retroactively, and what to migrate first. Generic SAST/SCA tools look for vulnerable library versions, not for the cryptographic properties of the code itself. Organizations additionally cannot use cloud SCA tools at all if their code cannot leave the perimeter (defense, finance, critical infrastructure). QuantumShield addresses this gap as an offline-first, standards-native cryptographic risk intelligence platform.

**LIMIT:** No explicit char limit shown on form; aim for ≤1200 chars. This answer ≈ 1160 chars.
**NOTES:** If a stricter limit applies, trim the final sentence first.

---

## FIELD: PROPOSED SOLUTION & ARCHITECTURE

**ANSWER:**
QuantumShield is a Cryptographic Risk Intelligence & Post-Quantum Readiness Platform delivered as a FastAPI backend plus an 11-screen React + TypeScript security workstation. It runs a 6-stage pipeline: (1) Offline discovery across source code (.py, .java, .js, .ts, .c, .h), dependency manifests (requirements.txt, pom.xml, package.json, go.mod, Cargo.toml), X.509 certificates and keystores (.pem, .der, .p12, .pub), server configs (nginx, sshd, openssl), and JVM bytecode (.class, .jar); (2) Evidence normalization with provenance (file, line, snippet, confidence); (3) Cross-scanner deduplication by [NormPath, Line, Algorithm, Usage]; (4) Post-quantum classification (Shor-broken, Grover-weakened, classically-broken, quantum-safe) with HNDL/TNFL threat-surface tagging; (5) Mosca's Inequality simulation (X + Y > Z) over data lifetime, migration time, and CRQC horizon; (6) Deterministic 5-factor risk scoring (0–100, banded Critical/High/Medium/Low) with weights 35/25/15/15/10 (Quantum Exposure, Business Criticality, Exposure Surface, Data Sensitivity, Inversed Agility). Every finding maps to a NIST FIPS 203/204/205 recommendation (ML-KEM, ML-DSA, SLH-DSA, SLH-DSA) and exports as a schema-validated CycloneDX 1.6 CBOM, SARIF 2.1.0, CSV, HTML, PDF, and Markdown. Security: 100% offline, zero private-key persistence, path-traversal defense, Zip Slip and archive-bomb guards, defusedxml XML hardening, zero shell=True. Validation: 71 automated tests pass; controlled corpus precision 1.000 / recall 0.974; OpenSSL 3.3.0, CPython 3.12.3, OpenSSH 9.7 scanned with zero CBOM validation errors. Production: https://quantumshield-seven.vercel.app (frontend), https://quantumshield-b5j2.onrender.com (backend). GitHub: https://github.com/shaikmohammedyasin-create/QuantumShield.

**LIMIT:** No explicit char limit shown; ≈ 1480 chars.
**NOTES:** If a tighter limit applies, trim the validation section first, then the security section.

---

## FIELD: TECHNOLOGY STACK (COMMA SEPARATED)

**ANSWER:**
Python, FastAPI, React, TypeScript, Vite, Tailwind CSS, CycloneDX, ReportLab, pytest, Docker

**LIMIT:** "comma separated" text input.
**NOTES:** Matches the actual dependency and runtime stack.

---

## FIELD: PROJECT DELIVERABLE FILES & ATTACHMENTS

**ANSWER (action):** Upload the following (each ≤25MB; allowed: PPT, PPTX, PDF, DOC, DOCX, ZIP):
1. `QuantumShield_Submission_Package.zip` — source + README + reports + submission docs.
2. `QuantumShield_Deck.pptx` — the 12-slide deck (upload to Google Slides and paste the share link in the Deck URL field).
3. `QuantumShield_Proposal.pdf` — `submission/02_PROJECT_DESCRIPTION.md` rendered to PDF (optional).

**LIMIT:** 25MB per file.
**NOTES:** Build the ZIP from the QuantumShield repo minus `node_modules`, `venv`, `.git`, `output/external/` (keep final evidence). Generate the PPTX and PDF with the commands in `12_FINAL_SUBMISSION_CHECKLIST.md`.

---

## FIELD: PRESENTATION DECK URL (GOOGLE SLIDES / CANVA / PITCH)

**ANSWER (manual):** `https://docs.google.com/presentation/d/...` — upload `QuantumShield_Deck.pptx` to Google Drive, open in Google Slides, share as "Anyone with the link can view", paste link here.

**LIMIT:** url.
**NOTES:** ⏳ Manual. Cannot be auto-generated; requires a hosted deck.

---

## FIELD: VIDEO PITCH / WALKTHROUGH URL (YOUTUBE / LOOM / DRIVE)

**ANSWER (manual):** `https://youtu.be/...` or `https://www.loom.com/share/...` — 3–5 minute narrated walkthrough following `09_DEMO_SCRIPT.md`.

**LIMIT:** url.
**NOTES:** ⏳ Manual. Cannot be auto-generated; requires a recorded video. Use the production URL for the walkthrough to avoid cold-start issues.

---

## FIELD: WORKING PROTOTYPE DEPLOYMENT URL

**ANSWER:**
https://quantumshield-seven.vercel.app

**LIMIT:** url.
**NOTES:** Live Vercel frontend. Backend API + docs: https://quantumshield-b5j2.onrender.com/docs ; health: https://quantumshield-b5j2.onrender.com/health.

---

## FIELD: PUBLIC GITHUB REPOSITORY URL

**ANSWER:**
https://github.com/shaikmohammedyasin-create/QuantumShield

**LIMIT:** url.
**NOTES:** Verify the repo is public before submission. Do not push secrets, temp files, or the local SIH test corpus.

---

## FIELD: SETUP INSTRUCTIONS & TEST CREDENTIALS

**ANSWER:**
QuantumShield runs locally with no credentials (air-gapped, no auth required for the workstation).

Prerequisites: Python 3.10+ and Node.js 18+.

1. Clone: `git clone https://github.com/shaikmohammedyasin-create/QuantumShield.git && cd QuantumShield`
2. Backend deps: `pip install -r requirements.txt`
3. Frontend deps: `cd frontend && npm install && cd ..`
4. Launch both: `python run.py` (backend on http://127.0.0.1:8000, frontend on http://localhost:5173, opens browser)
5. Optional separate services: `python run.py --backend-only` then `cd frontend && npm run dev`
6. Run tests: `python -m pytest tests/ -v` (71 tests; expected all pass)
7. Docker: `docker build -t quantumshield . && docker run -p 8000:8000 quantumshield`

No test credentials are required. The workstation has no authentication layer in the current build; scans are restricted to paths the operator authorizes.

**LIMIT:** textarea.
**NOTES:** No secrets or API keys are embedded anywhere in the project. Verify `.env` is not committed (it is gitignored).
