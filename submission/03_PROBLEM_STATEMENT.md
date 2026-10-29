# QuantumShield — Problem Statement

## The Problem

Security teams cannot see their own cryptography.

Modern software touches cryptography everywhere — RSA key generation buried in a Python helper, an ECDSA signing routine in a Java service, a self-signed X.509 certificate in a config directory, a legacy TLS 1.0 cipher suite in an nginx configuration, a hard-coded MD5 call in a dependency. None of this appears in a vulnerability scanner, because none of it is a "CVE." It is simply the cryptographic substrate of the application, and today it is effectively invisible.

Quantum computing converts that invisibility into a concrete, time-boxed risk:

1. **Shor's algorithm** will break RSA, DSA, ECDSA, ECDH, and Diffie-Hellman — the entire public-key foundation of today's key exchange and digital signatures — once a cryptographically relevant quantum computer (CRQC) exists.
2. **Grover's algorithm** halves the effective security of symmetric ciphers and hashes, weakening AES-128-class deployments.
3. **Harvest-Now-Decrypt-Later (HNDL)** means the attacker does not need to wait: ciphertext captured today over classical key exchange will be decrypted within its lifetime if the CRQC arrives before that lifetime ends.
4. **Trust-Now-Forge-Later (TNFL)** means signatures captured today — code signing, certificates, document signing — can be forged retroactively, attacking the integrity of the software supply chain itself.

## The Consequence

Without a cryptographic inventory, an organization cannot answer any of the questions a quantum-readiness program starts with:

- Which of our systems use Shor-vulnerable algorithms today?
- Which of those protect data that must stay secret past the CRQC horizon?
- Which certificates and signatures can be forged retroactively?
- What do we migrate first, to what, and how do we prove it to an auditor?

Mosca's inequality captures the trap formally: if **X** (the time the data must remain secret) plus **Y** (the time the migration will take) exceeds **Z** (time until a CRQC exists), then the data is *already exposed* — the migration should have started before today. Organizations that cannot inventory their cryptography cannot even compute X, Y, or Z for their own estate.

## Who Feels It

- **Security engineering teams** asked for a "quantum readiness posture" and having no tool to produce one.
- **Compliance and audit functions** who need machine-readable, standards-based evidence (CycloneDX CBOM, SARIF) rather than ad-hoc spreadsheets.
- **Defense, finance, and critical infrastructure operators** — precisely the sectors with the longest data lifetimes — who additionally cannot use cloud SCA tools at all, because their code cannot leave the perimeter.
- **Software supply chain owners** whose code-signing and release infrastructure is exposed to retroactive forgery.

## Why Existing Tools Do Not Solve It

Generic SAST/SCA tooling looks for vulnerable *library versions*, not for the cryptographic *properties* of the code itself. There is no mainstream offline-first tool that, in one pass, discovers cryptographic assets across source code, dependency manifests, X.509 certificates, keystores, server configuration, and JVM bytecode; classifies each by its quantum attack surface; models the HNDL/TNFL timeline; and emits standards-based evidence. The CycloneDX community added cryptographic bill-of-materials (CBOM) support to the 1.6 specification specifically because this discovery layer was missing — but generating and validating a CBOM is still a manual, expert task today.

## Our Problem Statement (one line for the submission form)

> Organizations have no offline, standards-based way to discover their cryptographic assets, quantify their exposure to cryptographically relevant quantum computers, and prioritize the post-quantum migration — so data harvested today will be decryptable within its lifetime before anyone knows it was at risk.
