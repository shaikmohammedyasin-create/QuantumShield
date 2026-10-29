# QuantumShield — Solution & Architecture

## 1. Solution Overview

QuantumShield is a **Cryptographic Risk Intelligence & Post-Quantum Readiness Platform**. It transforms raw codebases, configurations, and artifacts into actionable, standards-based migration programs through a 6-stage operational pipeline:

$$\text{Discover} \longrightarrow \text{Inventory} \longrightarrow \text{Analyze} \longrightarrow \text{Prioritize} \longrightarrow \text{Remediate} \longrightarrow \text{Monitor}$$

It is delivered as a full-stack system: a **FastAPI backend** running offline analysis engines and an **11-screen React + TypeScript security workstation** providing deep forensic inspection, interactive Mosca simulation, and standards-based evidence exports.

---

## 2. End-to-End Processing Pipeline

```text
[1] RAW INPUT LAYER
    Source Code (.py, .java, .js, .ts, .c, .h)
    Dependency Manifests (requirements.txt, pom.xml, package.json, go.mod, Cargo.toml)
    Certificates & Keystores (.pem, .der, .crt, .p12, .pub)
    Server Configurations (nginx.conf, sshd_config, openssl.cnf)
    Java Bytecode (.class, .jar, .war)
         │
         ▼
[2] OFFLINE DISCOVERY & AST EXTRACTION
    • Python AST visitor: detects call-sites, key generation, hash algorithms
    • Java static pattern engine: detects Cipher, KeyPairGenerator, Signature instances
    • JS/TS visitor: detects WebCrypto and Node.js crypto API usages
    • C/C++ regex/lexical visitor: detects EVP_*, OpenSSL, and OpenSSH primitive usage
    • Manifest parsers (defusedxml for XML, safe JSON/text parsers)
    • X.509 ASN.1 metadata extractor (algorithm, key size, validity, subject, issuer)
    • Server config parser (TLS protocols, cipher suites, DH parameters)
    • JVM constant pool reader (offline binary inspection with Zip Slip protection)
         │
         ▼
[3] EVIDENCE NORMALIZATION & CROSS-SCANNER DEDUPLICATION
    Extracts provenance (file path, line range, caller context, confidence).
    Deduplicates findings using composite key: [NormPath, Line, Algorithm, Usage].
         │
         ▼
[4] POST-QUANTUM CLASSIFICATION & THREAT MODELING
    • Shor-Broken: RSA, DSA, ECDSA, ECDH, X25519, Ed25519 (asymmetric break)
    • Grover-Weakened: AES-128, ChaCha20, unknown-keysize AES (quadratic speedup)
    • Classically Broken: MD5, SHA-1, DES, 3DES, RC4, TLS 1.0/1.1
    • Quantum-Safe: AES-256, SHA-256/384/512, SHA-3, ML-KEM, ML-DSA, SLH-DSA
    Threat Surface Tagging:
    • HNDL (Harvest-Now-Decrypt-Later): Key Exchange & Encryption findings
    • TNFL (Trust-Now-Forge-Later): Digital Signatures & Certificate findings
         │
         ▼
[5] MOSCA'S INEQUALITY SIMULATION (X + Y > Z)
    Evaluates:
      X = Data Secrecy Lifetime (years)
      Y = Migration / Deployment Time (years)
      Z = CRQC Arrival Horizon (years)
    If X + Y > Z: Flagged as active vulnerability (data compromised in transit/storage).
         │
         ▼
[6] 5-FACTOR EXPLAINABLE RISK ENGINE
    Calculates deterministic risk score (0–100) per finding:
      Score = 100 × (0.35·Q + 0.25·B + 0.15·E + 0.15·S + 0.10·(1 - A))
    Categorizes into Critical, High, Medium, Low risk bands.
         │
         ▼
[7] DETERMINISTIC PQC MIGRATION RECOMMENDATIONS
    Maps each finding to NIST FIPS 203/204/205 standards:
    • Key Exchange → Hybrid X25519 + ML-KEM-768 or pure ML-KEM
    • Signatures → ML-DSA-65 (NIST Level 3)
    • High-Assurance / Firmware Signatures → SLH-DSA or LMS/XMSS (SP 800-208)
    • Symmetric Ciphers → Upgrade to AES-256-GCM
         │
         ▼
[8] STANDARDS-BASED DELIVERABLE GENERATION
    • CycloneDX 1.6 Cryptographic BOM (cbom.json) — validated against official schema
    • SARIF 2.1.0 (findings.sarif) — for GitHub Code Scanning and CI/CD integration
    • Tabular Asset Inventory (inventory.csv) — for spreadsheet analysis
    • Executive Security Report (report.html & report.pdf) — for leadership and auditors
    • Markdown Summary (summary.md) — for PR comments and documentation
```

---

## 3. The 5-Factor Explainable Risk Model

QuantumShield avoids opaque, black-box AI risk scores. Every finding is ranked using a transparent, weighted formula designed for cryptographic risk triage:

$$\text{Risk Score} = 100 \times \left(0.35 \cdot Q + 0.25 \cdot B + 0.15 \cdot E + 0.15 \cdot S + 0.10 \cdot (1 - A)\right)$$

| Factor | Weight | Parameter | Meaning & Scoring Basis |
|---|---|---|---|
| **$Q$** | **35%** | **Quantum Exposure** | Classification severity: Shor-Broken = 1.0, Classically Broken = 0.9, Grover-Weakened = 0.6, Quantum-Safe = 0.0. |
| **$B$** | **25%** | **Business Criticality** | Asset criticality in the application: Authentication/Core = 1.0, Production Service = 0.75, Internal = 0.5, Test = 0.2. |
| **$E$** | **15%** | **Exposure Surface** | Threat vector: Public Internet / External API = 1.0, Service-to-Service = 0.7, Internal Storage = 0.4. |
| **$S$** | **15%** | **Data Sensitivity** | Lifetime and classification: Classified/Regulated/PVI = 1.0, Confidential = 0.75, Operational = 0.4, Public = 0.1. |
| **$A$** | **10%** | **Cryptographic Agility** | How easily the asset can be swapped: Hard-coded in code/schema = 0.1 (low agility, high risk), Config-driven = 0.8 (high agility, low risk). |

*Note: This formula represents QuantumShield's explainable prioritization model, calibrated for cryptographic triage; weights can be adjusted in the Workstation Settings.*

---

## 4. Post-Quantum Migration Strategy (NIST Standards Mapping)

QuantumShield provides actionable, deterministic migration guidance mapped directly to the final NIST Post-Quantum Cryptography standards:

```text
Current Vulnerable               Recommended Hybrid State                 Target PQC State
    Classical                              (Stage 2)                          (Stage 3)
┌────────────────┐                     ┌──────────────────┐               ┌────────────────┐
│   RSA-2048 /   │  ────────────────►  │  X25519 +        │  ──────────►  │   ML-KEM-768   │
│   ECDH P-256   │                     │  ML-KEM-768      │               │  (FIPS 203)    │
└────────────────┘                     └──────────────────┘               └────────────────┘
┌────────────────┐                     ┌──────────────────┐               ┌────────────────┐
│   RSA-2048 /   │  ────────────────►  │  ECDSA P-256 +   │  ──────────►  │   ML-DSA-65    │
│   ECDSA P-256  │                     │  ML-DSA-65       │               │  (FIPS 204)    │
└────────────────┘                     └──────────────────┘               └────────────────┘
┌────────────────┐                                                        ┌────────────────┐
│  AES-128-CBC   │  ───────────────────────────────────────────────────►  │  AES-256-GCM   │
│  (Grover-weak) │                                                        │ (Quantum-Safe) │
└────────────────┘                                                        └────────────────┘
```

1. **NIST FIPS 203 (ML-KEM):** Module-Lattice-Based Key-Encapsulation Mechanism. Recommended for general key exchange and envelope encryption.
2. **NIST FIPS 204 (ML-DSA):** Module-Lattice-Based Digital Signature Algorithm. Recommended for application-level signatures, API authentication, and certificates.
3. **NIST FIPS 205 (SLH-DSA):** Stateless Hash-Based Digital Signature Algorithm. Recommended for long-term document signing, firmware integrity, and root CAs.
4. **SP 800-208 (LMS / XMSS):** Stateful Hash-Based Signatures for bounded-use signing environments.

---

## 5. CycloneDX 1.6 Cryptographic BOM (CBOM)

QuantumShield natively emits and validates against the official CycloneDX 1.6 specification (`bom-1.6.schema.json`):
- Every detected asset is modeled as a component with `cryptoProperties`.
- Includes `assetType` (algorithm, certificate, protocol, key), `algorithmProperties` (primitive, curve, modeOfOperation, padding), `nistQuantumSecurityLevel` (0–5), and complete forensic `evidence` (file path, line numbers, snippet).
- Schema validation runs via `jsonschema.Draft7Validator` on every output generation, ensuring strict compliance and zero errors.

---

## 6. Security Architecture & Air-Gap Defenses

QuantumShield is engineered for high-security, defense, and air-gapped environments:
- **100% Offline Execution:** Scanners perform local AST and regex parsing. Zero network calls, zero external telemetry, zero phoning home.
- **Zero Private Key Persistence:** Scanner strictly extracts metadata (algorithm, key length, public exponents, validity dates). Private keys are explicitly filtered and never stored in memory, state, or reports.
- **Path Traversal Protection:** API endpoints strictly validate target scan paths against directory escape attacks and prohibit root-level scanning.
- **Zip Slip & Archive Bomb Containment:** Bytecode and archive analyzers enforce safe canonical path validation and maximum extraction thresholds.
- **DefusedXML Enforcement:** Manifest and pom.xml parsing utilizes `defusedxml` to neutralize XML External Entity (XXE) and entity expansion attacks.
