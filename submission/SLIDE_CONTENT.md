# QuantumShield — Slide Content

## Slide 1: Title
- **Title:** QuantumShield
- **Subtitle:** Cryptographic Risk Intelligence & Post-Quantum Readiness Platform
- **Tagline:** Discover. Quantify. Prioritize. Migrate.
- **Team:** Team Diet Claude
- **Hackathon:** MG Solutions Build Spark Hackathon
- **Production URL:** https://quantumshield-seven.vercel.app
- **GitHub:** https://github.com/shaikmohammedyasin-create/QuantumShield

## Slide 2: The Problem
- **Headline:** Your organization cannot migrate cryptography it cannot see.
- **Invisible Assets:** Source Code, Dependencies, X.509 Certificates, Keystores, Server Configurations, JVM Bytecode.
- **Quantum Threat Vectors:**
  - *Shor:* Breaks RSA, DSA, ECDSA, ECDH, DH.
  - *Grover:* Halves symmetric cipher and hash security.
  - *HNDL (Harvest Now, Decrypt Later):* Data captured today can be decrypted once a CRQC arrives.
  - *TNFL (Trust Now, Forge Later):* Historical signatures become forgeable.
- **Conclusion:** The first step toward quantum readiness is complete cryptographic visibility.

## Slide 3: Our Solution
- **Headline:** QuantumShield turns invisible cryptography into actionable risk intelligence.
- **Workflow:** DISCOVER → INVENTORY → ANALYZE → PRIORITIZE → REMEDIATE → MONITOR
- **Core Principles:** Offline-first, evidence-backed, standards-native, migration-oriented.
- **Platform:** FastAPI backend + 11-screen React & TypeScript security workstation.

## Slide 4: How It Works
- **Headline:** A six-stage cryptographic intelligence pipeline
- **Stages:**
  1. *Discovery:* Source, dependencies, certificates, keystores, configs, JVM bytecode.
  2. *Evidence Normalization:* File + line + snippet + confidence.
  3. *Deduplication:* Normalized path + line + algorithm + usage.
  4. *Quantum Classification:* Shor-broken / Grover-weakened / classically-broken / quantum-safe.
  5. *Risk Modeling:* Mosca inequality + 5-factor risk score.
  6. *Remediation:* PQC recommendations + CBOM + reports.

## Slide 5: Quantum Risk Engine
- **Headline:** From algorithm detection to measurable business risk
- **Mosca's Inequality:** X + Y > Z (Data Lifetime + Migration Time > CRQC Horizon).
- **5-Factor Deterministic Risk Model (0–100 Score):**
  - Quantum Exposure (35%)
  - Business Criticality (25%)
  - Exposure Surface (15%)
  - Data Sensitivity (15%)
  - Inversed Agility (10%)
- **Bands:** Critical / High / Medium / Low.

## Slide 6: Post-Quantum Migration
- **Headline:** From finding → recommendation → migration plan
- **Standards Mapping:** NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA), SP 800-208 (LMS/XMSS).
- **Migration Lifecycle:** Detect → Prioritize → Recommend → Track.
- **Focus:** Practical transition from classical primitives to hybrid and pure lattice cryptography.

## Slide 7: CBOM + Reporting
- **Headline:** Turn cryptographic findings into portable security evidence
- **Generated Formats:** CycloneDX 1.6 CBOM (`cbom.json`), SARIF 2.1.0 (`findings.sarif`), JSON, CSV, HTML (`report.html`), PDF (`report.pdf`), Markdown (`summary.md`).
- **Verified Corpus Metrics:** 25 cryptographic assets in sample project, schema-validated CycloneDX 1.6 with zero errors.
- **Value:** Security teams get machine-readable, schema-valid evidence for compliance and supply-chain governance.

## Slide 8: Validation / Proof
- **Headline:** Built and validated as a real working system
- **Verified Metrics:**
  - **71 / 71** automated tests passing
  - **1.000** Precision on controlled corpus
  - **0.974** Recall on controlled corpus
  - **0 errors** on CycloneDX 1.6 schema validation
  - **3 external repos scanned** (OpenSSL 3.3.0, CPython 3.12.3, OpenSSH 9.7)
- **Deployment:** Vercel (Frontend) + Render (FastAPI Backend).

## Slide 9: Why QuantumShield
- **Headline:** Built for the gap between vulnerability scanning and quantum readiness
- **Comparison:**
  - *Generic SAST/SCA:* Focuses on software vulnerabilities (CVEs) and dependencies; lacks cryptographic parameter awareness, quantum classification, HNDL/TNFL modeling, and CBOM generation.
  - *QuantumShield:* Purpose-built around cryptographic visibility, quantum attack surface analysis, Mosca simulation, explainable risk scoring, NIST PQC recommendations, and offline-first execution.
- **Core Takeaway:** Not another scanner — a cryptographic decision system.

## Slide 10: Impact + Roadmap
- **Headline:** Make post-quantum readiness measurable
- **Impact Areas:** Security (visibility), Risk (prioritization), Migration (evidence-backed action).
- **Roadmap:**
  - *Now:* Cryptographic discovery, risk intelligence, PQC recommendations, CBOM + reporting.
  - *Next (Planned):* Continuous repository monitoring, migration tracking, expanded language coverage, enterprise workflow integrations.
- **Call to Action:**
  - Production URL: https://quantumshield-seven.vercel.app
  - GitHub: https://github.com/shaikmohammedyasin-create/QuantumShield
