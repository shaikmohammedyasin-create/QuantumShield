# MG Solutions Build Spark Hackathon — Verified Requirements

> Derived from the live hackathon platform at `hackathon.mgsolutions.sbs` (accessed 2026-10-29).
> No requirement below is invented; each is sourced from the platform UI or rules page.

---

## 1. Event Window (from `/hackathons`)

| Requirement | Source | Value |
|---|---|---|
| Event name | Hackathon catalogue | **Build Spark Hackathon** — "Ignite Ideas. Build the Future." |
| Event window | Hackathon catalogue | **11/2/2026 — 11/15/2026** |
| Team size | Hackathon catalogue | **2–3 members** |
| Team roster (as of last check) | Submission page | "Team Diet Claude" — **2 members** (Lead: You) |

> Note: The event window listed is 11/2–11/15/2026. The teammate count is 2 (minimum allowed is 2 — you are compliant, but at the bottom edge; consider adding a 3rd member if the rubric rewards complete teams).

---

## 2. Round Structure & Deadlines (from `/rules` + submission page)

| Requirement | Source | Value |
|---|---|---|
| Sequential gated rounds | Rules §2 | Round 1: Idea → Round 2: Prototype → Final: Evaluation |
| Round 1 name | Submission page | **Round 1 — Idea Submission** |
| Round 1 cutoff | Submission page | **11/1/2026, 11:59:59 PM IST** |
| Timezone standard | Rules §2 | Asia/Kolkata (IST, UTC+05:30) |
| Hard deadline enforcement | Rules §2 | At cutoff, endpoints reject new/updated payloads with HTTP 403 |

> ⚠️ **Deadline risk:** The Round 1 cutoff (11/1/2026 23:59 IST) falls **before** the listed event start (11/2/2026). Submit early — do not rely on the event window dates.

---

## 3. Submission Form Fields (from `/submit` page — Round 1)

These are the exact labeled fields on the submission form:

| # | Field Label | Type | Required |
|---|---|---|---|
| 1 | PROJECT TITLE | text | ⭐ yes |
| 2 | PROBLEM STATEMENT | textarea | no star shown |
| 3 | PROPOSED SOLUTION & ARCHITECTURE | textarea | no star shown |
| 4 | TECHNOLOGY STACK (COMMA SEPARATED) | text | no star shown |
| 5 | PROJECT DELIVERABLE FILES & ATTACHMENTS | file upload | ⭐ yes |
| 6 | PRESENTATION DECK URL (GOOGLE SLIDES / CANVA / PITCH) | url | no star shown |
| 7 | VIDEO PITCH / WALKTHROUGH URL (YOUTUBE / LOOM / DRIVE) | url | no star shown |
| 8 | WORKING PROTOTYPE DEPLOYMENT URL | url | no star shown |
| 9 | PUBLIC GITHUB REPOSITORY URL | url | no star shown |
| 10 | SETUP INSTRUCTIONS & TEST CREDENTIALS | textarea | no star shown |

### File upload constraints (from upload UI)

| Requirement | Source | Value |
|---|---|---|
| Allowed types | Upload widget | **PPT, PPTX, PDF, DOC, DOCX, ZIP** |
| Max size per file | Upload widget | **25MB** |
| Accepted content | Upload widget | "Upload presentation slides (PPT/PPTX), proposal/report (PDF), source archives (ZIP), or design assets" |

### Field placeholders (from form HTML — used to infer expected content)

| Field | Placeholder text |
|---|---|
| Problem statement | "Clearly describe the problem your team is addressing..." |
| Solution & architecture | "Describe technical implementation, innovation, and design..." |
| Tech stack | "e.g. React, TypeScript, Rust, WebAssembly, Firebase" |
| Deck URL | "https://docs.google.com/presentation/..." |
| Video URL | "https://youtu.be/..." |
| Prototype URL | "https://my-app.vercel.app" |
| GitHub URL | "https://github.com/org/repo" |
| Setup/credentials | "Include demo account credentials or instructions to run locally..." |

---

## 4. Platform Rules (from `/rules`) — Design Implications

| Rule | Text (paraphrased) | What QuantumShield must provide |
|---|---|---|
| **Identity integrity** | One account per participant; no duplicate accounts | — |
| **Team constraint** | Member cannot be in multiple teams in the same hackathon | — |
| **Originality / plagiarism** | "All projects must represent authentic intellectual work. Pre-existing commercial applications cannot be resubmitted." | QuantumShield is the team's own work (origin: validated ECDAT prototype). Must show original architecture + code written during the hackathon window. Frame the ECDAT lineage as the validated foundation, not a prior commercial product. |
| **Open source allowed** | Libraries/frameworks permitted; core business logic and system architecture must be developed during the hackathon | README must show the original custom scanners, risk engine, Mosca model, CBOM generator as internals — not just wrappers around frameworks. |
| **Blinded evaluation** | "Judges evaluate submissions blindly. Competitor names and affiliations are concealed." | Public-facing docs should be generic (no personal names in README). Judging is on the weighted rubric. |
| **Certificate revocation** | Plagiarized code / deceptive demos → disqualification + revoked certificates | Zero fabricated claims in all submission assets; screenshots must be real. |

---

## 5. Judging & Evaluation (from `/rules` §4)

| Requirement | Source | Value |
|---|---|---|
| Evaluation mode | Rules §4 | **Blinded** — names/affiliations concealed |
| Scoring basis | Rules §4 | "Predefined weighted rubrics" (round-specific, not published in full) |
| Leaderboard | Rules §4 | Finalized by admins, public upon official publication |

> The exact rubric weights are not published on the platform. This package therefore maps QuantumShield against the **standard hackathon rubric dimensions implied by the submission form** (problem validity, solution quality, technical depth, innovation, completeness, presentation), and the strongest evidence is assembled for each. See `13_JUDGING_ALIGNMENT.md`.

---

## 6. FAQ Signal (from `/faq`)

| FAQ | Signal |
|---|---|
| "How are round deadlines calculated and enforced?" | Cutoffs are server-clock enforced; no grace. Submit before 11/1/2026 23:59:59 IST. |
| "How does blinded evaluation work?" | Judges see only the submission, not the team. Make the artifacts self-explanatory. |
| "How can employers or universities verify my certificate?" | Post-event verification ledger. Irrelevant to submission content. |

---

## 7. What QuantumShield Must Provide (mapped)

| Requirement | What QuantumShield provides | Status |
|---|---|---|
| Project title | "QuantumShield: Cryptographic Risk Intelligence & Post-Quantum Readiness Platform" | ✅ Ready |
| Problem statement | Text drafted in `03_PROBLEM_STATEMENT.md` | ✅ Ready |
| Solution & architecture | FastAPI + React pipeline described in `04_SOLUTION.md` + architecture diagram | ✅ Ready |
| Technology stack | Comma-separated list in `12_SUBMISSION_FORM.md` | ✅ Ready |
| Deliverable attachments | ZIP (source + README + reports) and/or PPTX deck; PDF proposal | ✅ Build in progress |
| Presentation deck URL | Requires a Google Slides / Canva / Pitch link — **team action item** | ⏳ Manual |
| Video pitch URL | Requires YouTube / Loom / Drive link — **team action item** | ⏳ Manual |
| Working prototype URL | https://quantumshield-seven.vercel.app (production) | ✅ Live |
| Public GitHub URL | https://github.com/shaikmohammedyasin-create/QuantumShield | ✅ Live |
| Setup instructions | Paste from `12_SUBMISSION_FORM.md` | ✅ Ready |
| Blinded-eval friendly | No personal/affiliation names in README body | ✅ Checked |
| No fabricated claims | All metrics traceable to `tests/results/*` | ✅ Checked |

---

## 8. Manual Actions Required (not automatable from here)

1. **Presentation deck URL** — upload a deck (PPTX or Google Slides/Canva) to a shareable link. A `submission/BuildSpark_QuantumShield.pptx` is generated; upload it to Google Drive/Slides and paste the share link.
2. **Video pitch URL** — record/narrate the demo (the demo script in `10_DEMO_SCRIPT.md` is the 5-minute narration) and host on YouTube/Loom/Drive.
3. **File upload** — attach the generated `.zip` (and optionally the `.pptx` and the PDF proposal) to the "PROJECT DELIVERABLE FILES & ATTACHMENTS" field.
4. **Final form fill** — paste answers from `12_SUBMISSION_FORM.md` into the live form and click **Confirm Final Submission** before 11/1/2026 23:59 IST.

---

**Status legend:** ✅ verified/ready · ⏳ manual/team action · ⚠️ risk.
