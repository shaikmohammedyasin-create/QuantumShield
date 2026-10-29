# QuantumShield — Project Description

## Project Title

**QuantumShield: Cryptographic Risk Intelligence & Post-Quantum Readiness Platform**

## One-Line Tagline

**Find every piece of cryptography in your codebase, see how quantum-broken it is, and know exactly what to migrate first.**

## Short Description (elevator)

QuantumShield scans source code, dependency manifests, X.509 certificates, server configurations, and Java bytecode to build a complete cryptographic bill of materials (CycloneDX 1.6 CBOM), classifies each asset's post-quantum vulnerability using Shor and Grover analysis, models migration urgency with Mosca's Inequality, and produces explainable risk scores plus standards-based remediation mapped to NIST FIPS 203/204/205 — all 100% offline.

## Executive Summary

Organizations today have no systematic way to answer a deceptively simple question: *where is our cryptography, and how much of it will a quantum computer break?* Cryptography is embedded invisibly across source code, dependencies, certificates, and server configuration — and the arrival of cryptographically relevant quantum computers (CRQC) turns that invisibility into a direct, time-boxed risk: data encrypted today with RSA or ECC can be harvested now and decrypted later.

QuantumShield is a cryptographic risk intelligence and post-quantum readiness platform that answers that question end-to-end. It discovers cryptographic assets across six artifact categories using static, air-gapped scanners; normalizes the evidence into a CycloneDX 1.6 Cryptographic Bill of Materials; classifies each asset as Shor-broken, Grover-weakened, classically broken, or quantum-safe; tags each finding with its real-world threat surface (Harvest-Now-Decrypt-Later vs Trust-Now-Forge-Later); models exposure timelines using Mosca's Inequality (X + Y > Z); and prioritizes remediation through a transparent, five-factor weighted risk engine. Every finding carries a deterministic, standards-mapped migration recommendation (ML-KEM, ML-DSA, SLH-DSA) and exports as CBOM JSON, SARIF 2.1.0, CSV, HTML, PDF, and Markdown.

The platform ships as a production deployment (React + TypeScript frontend on Vercel, FastAPI backend on Render) and as a single-command local launcher for air-gapped environments. It is validated end-to-end: 71 automated tests pass, the controlled corpus achieves 100% precision and 97.4% recall with zero false positives, and the scanner has been executed against three real-world open-source codebases (OpenSSL 3.3.0, CPython 3.12.3, OpenSSH 9.7) producing schema-valid CBOMs with zero validation errors.

QuantumShield productizes and extends a previously validated cryptographic analysis capability into a standalone, productized platform — the codebase and its verification artifacts are the track record.

---

## 2. Why This Problem Matters

1. **The quantum threat is a deadline, not a theory.** Adversarial "harvest now, decrypt later" (HNDL) campaigns mean data with long confidentiality lifetimes is already at risk the moment it is encrypted with Shor-vulnerable algorithms, regardless of when a CRQC actually arrives.
2. **Cryptography is invisible sprawl.** A modern application touches cryptography in source code, transitive dependencies, TLS certificates, SSH keys, keystores, and reverse-proxy configs. Most organizations cannot produce a complete list of their own cryptographic assets — the first step of any migration.
3. **Migration is a multi-year program, not a patch.** NIST finalized ML-KEM (FIPS 203), ML-DSA (FIPS 204), and SLH-DSA (FIPS 205) in 2024, but migrating key exchange, signatures, certificates, and protocols takes years. Without a prioritized inventory, organizations cannot even scope the effort.
4. **Trust-now-forge-later (TNFL)** extends the risk to signatures and identity: code-signing keys and document signatures made today can be forged once a CRQC exists, breaking software supply-chain integrity retroactively.
5. **Generic SCA tools do not solve this.** Existing SAST/SCA tools look for vulnerable *libraries*, not for the cryptographic *properties* of the code itself (which algorithm, which key size, which protocol version, used for what). Cryptographic BOM tooling is an emerging gap that has no mainstream offline-first answer.

## 3. Existing Gap

| Gap | Current state |
|---|---|
| Cryptographic visibility | No mainstream tool produces a standards-based cryptographic inventory across source, manifests, certificates, configs, and bytecode in one pass. |
| Quantum-aware prioritization | Generic vulnerability scanners flag CVEs, not "is this algorithm breakable by Shor's algorithm, and does the data outlive the CRQC horizon?" |
| Migration guidance | Existing scanners stop at detection. None map findings to specific NIST PQC replacements with a deterministic, explainable rationale. |
| Evidence for auditors | Compliance and supply-chain workflows need machine-readable evidence (CycloneDX CBOM, SARIF), not just human-readable reports. |
| Offline / air-gapped operation | Defense, finance, and critical-infrastructure environments cannot send code to a cloud SCA. Existing cloud scanners are unusable there. |

QuantumShield is built specifically to close this gap as an offline-first, standards-native cryptographic risk intelligence platform.

---

## 4. Proposed Solution (short form for submission)

**Discover → Inventory → Analyze → Prioritize → Remediate → Monitor.**

QuantumShield is a full-stack cryptographic risk intelligence platform. A FastAPI backend runs offline scanners (Python AST, Java source, JavaScript/TypeScript, C/C++, dependency manifests, X.509 certificates, keystores, server configs, JVM bytecode) that produce raw forensic evidence; this is normalized, deduplicated, and classified into quantum-status categories (Shor-broken / Grover-weakened / classically-broken / quantum-safe) with HNDL/TNFL threat-surface tags. A Mosca's-Inequality engine (X + Y > Z) models whether data encrypted today will be decryptable within its lifetime. A deterministic five-factor risk engine produces explainable, banded (Critical/High/Medium/Low) priorities, and a rules engine maps every finding to a specific NIST FIPS 203/204/205 post-quantum replacement. Output is a schema-validated CycloneDX 1.6 CBOM plus SARIF 2.1.0, CSV, HTML, PDF, and Markdown reports, delivered through an 11-screen React + TypeScript security workstation.

---

*Continue to `04_SOLUTION.md` for the full architecture, workflow, and risk-model explanation.*
