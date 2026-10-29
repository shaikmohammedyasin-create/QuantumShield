# QuantumShield — Technology Stack

## Core Technologies

| Layer | Technologies & Libraries | Purpose |
|---|---|---|
| **Language & Runtime** | Python 3.10+ (tested on 3.11 / 3.12) | Core scanning engine, AST parsers, quantum classification, risk model, CBOM generator, report generation |
| **Backend Framework** | FastAPI, Uvicorn (ASGI) | High-performance asynchronous REST API serving frontend requests and orchestrating scans |
| **Frontend Workstation** | React 18, TypeScript, Vite | 11-screen security workstation UI (Dashboard, New Scan, Inventory, Finding Inspector, Mosca, Risk, Migration, CBOM, Terminal, Settings, Reports) |
| **Styling & Icons** | Tailwind CSS, Lucide React | Modern, responsive enterprise security workstation UI design |
| **Data Visualization** | Chart.js, Recharts | Interactive risk charts, quantum exposure distributions, and Mosca simulation curves |
| **Standards & Schemas** | CycloneDX 1.6 (`bom-1.6.schema.json`), SARIF 2.1.0 | Machine-readable cryptographic bill of materials and static analysis interchange format |
| **Document Generation** | ReportLab, Python-Markdown | Executive security PDF reports, HTML reports, and structured CSV/Markdown exports |
| **XML & Parsing Security** | `defusedxml`, Python Standard Library (`ast`, `zipfile`, `hashlib`) | Secure XML entity parsing (XXE defense), AST traversal, and archive containment |
| **Testing & Quality** | Pytest (`61` passing unit/integration tests) | Rigorous test coverage across scanners, API routes, risk engine, and CBOM generation |
| **Production Deployment** | Vercel (Frontend), Render (Backend Python Web Service) | Live cloud production architecture with global CDN and CORS security |

---

## Comma-Separated Stack (for submission forms)

> `Python, FastAPI, React, TypeScript, Vite, Tailwind CSS, CycloneDX, ReportLab, pytest, Docker`
