# QuantumShield — Roadmap

## Shipping Now (Validated Capabilities)

- Multi-language and multi-artifact cryptographic discovery across source code, dependency manifests, X.509 certificates, keystores, configs, and Java bytecode.
- Shor/Grover classification and HNDL/TNFL threat-surface tagging.
- Mosca's Inequality simulation with scenario presets.
- Five-factor (35/25/15/15/10) explainable risk scoring.
- PQC recommendations mapped to FIPS 203, FIPS 204, FIPS 205, and SP 800-208.
- CycloneDX 1.6 CBOM generation and schema validation.
- SARIF 2.1.0, CSV, HTML, PDF, and Markdown reporting.
- FastAPI + React + TypeScript security workstation.
- Air-gapped and local scanning mode.
- Production deployment over Vercel + Render.

## Near-Term

- Expand product UI support for multi-repository portfolio views.
- Add richer export summaries and CBOM diff views for progress tracking.
- Add migration workflow status updates per finding (partially represented in migration page).
- Add corpus and external target reproducibility controls for evaluator workflows.
- Expand scanner test corpus coverage for false-positive rejection.
- Expand production telemetry-free diagnostics and scan log export.

## Mid-Term

- Deeper data-flow analysis for multi-language source scanners (currently Python has full AST; other languages use static-pattern engines).
- Binary/ELF symbol recovery and direct analysis of compiled native binaries.
- Java bytecode hardening and malformed-archive test expansion.
- CI/CD integration presets for automated CBOM drift monitoring.
- Continuous portfolio-level cryptographic migration tracking dashboards.
- Additional certificate and key lifecycle analysis.
- Adapter for existing dependency/security governance toolchains via SARIF import.

## Long-Term

- Organization-wide cryptographic posture benchmarking (internal baseline).
- Policy controls for risk-weight calibration and compliance thresholds.
- Scalable ingestion across enterprise repository estates behind air-gap boundaries.
- Cryptographic agility metrics and timeline comparison.
- Integration with software composition analysis pipelines where permitted by air-gap policy.
- Ecosystem mappings beyond NIST PQC standards when required by sector requirements.

## Explicitly Roadmap (from current README)

- Compiled-binary symbol recovery (ELF/PE/Mach-O).
- CI/CD integration presets (GitHub Actions, GitLab) for SARIF uploads.
- Continuous CBOM drift monitoring across repositories and releases.
- Deeper data-flow analysis for multi-language source scanners.
- TLS / server-config scanner strengthening (currently documented as weakest area).

## Roadmap Principle

Roadmap items are limited to capabilities that are either already evidenced by code, planned in project documentation, or directly implied by the existing architecture. No fabricated enterprise features, partnerships, customers, or compliance certifications are claimed.
