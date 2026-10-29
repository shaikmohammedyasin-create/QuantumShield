# QuantumShield — Business Impact

## Who Benefits

**Security engineering teams** get an asset-level inventory of cryptography embedded across applications, infrastructure, certificates, and dependencies — with code-location evidence instead of a vague posture score.

**CISOs and risk leaders** get an explainable prioritization model and an interactive Mosca horizon to allocate migration budget based on confidentiality lifetime, criticality, exposure surface, and cryptographic agility.

**Compliance and audit teams** get evidence they can ingest: a schema-validated CycloneDX 1.6 CBOM, SARIF 2.1.0 findings, CSV inventory, and executive HTML/PDF reports.

**Defense, finance, and critical-infrastructure environments** get a genuinely offline scanning path. Source code and key metadata stay inside the controlled environment; no telemetry or external API is required.

**Platform and DevSecOps teams** get SARIF output for CI/CD code scanning plus deterministic recommendations that can become migration tickets.

## Operational Outcomes

QuantumShield turns an open-ended transformation program into a sequence of operational decisions:

1. **Discover hidden crypto:** Replace assumptions with file, line, algorithm, and usage evidence.
2. **Prioritize before migration:** Use a transparent score and HNDL/TNFL tags to identify what matters first.
3. **Sequence replacements:** Move from classical algorithms to hybrid, then PQC, using NIST standards mapping.
4. **Prove progress:** Re-run scans and compare CBOMs; export machine-readable evidence and reports.
5. **Reduce long-term exposure:** Start migration while data remains confidential, rather than waiting for a CRQC announcement.

## Verified Demonstration Evidence

The repository includes executed validation artifacts, not hypothetical business claims:

- A controlled corpus reached **100% precision, 97.4% recall, and 98.67% F1** in the final validation report, with zero false positives.
- Three real-world open-source repositories were scanned without modification: OpenSSL 3.3.0, CPython 3.12.3, and OpenSSH 9.7.
- Every external target generated a CycloneDX 1.6 CBOM with **zero schema validation errors**.
- Production deployment is available at the Vercel frontend and Render backend URLs listed in the README.

These are validation results, not claims of customer adoption, savings, revenue, or compliance certification.

## Why Impact Is Immediate

Quantum migration is an inventory problem before it is a cryptography problem. An organization cannot replace what it cannot find. QuantumShield lowers the cost of the first critical step: converting a codebase into a defensible, reviewable, standards-based map of where cryptographic risk lives.
