# Coverage Matrix — Participant Challenges → Skills

Battle-test of the skill library against the 22 GSB pre-workshop respondents (16 June 2026, Stanford GSB Singapore alumni event). Each participant pain was clustered, scored against all 15 skills, and adversarially verified.

Methodology: parallel agent extract → cluster → score every cluster against every skill (0–3) → adversarial-verify COVERED / PARTIAL claims with refute-by-default skeptics → synthesize. Workflow run: 24 agents, 1.16M tokens, 582s.

---

## Cluster → Skill mapping

| # | Participant cluster | Representative quote | Owning skill | Status |
|---|---|---|---|---|
| 1 | Use-case selection | r02 "How to focus on areas where AI can be utilized"; r05 "decide among the myriad of choices"; r21 "Finding a useful productive case use"; r22 "Knowing what to adopt and how to use agentic" | `use-case-discovery` | NEW |
| 2 | Workforce AI literacy | r03 "AI literacy level is still low... using AI as a chatbot"; r17 "Awareness. Employees don't understand"; r23 older workers; r25 basics of AI | `workforce-literacy-curriculum` | NEW |
| 3 | Data confidentiality / deployment pattern | r01 "proprietary data... retaining confidentiality"; r19 "data privacy"; r20 "tools people use at home vs enterprise grade" | `data-trust-deployment-pattern` | NEW |
| 4 | Pilot-to-production reliability | r15 "Moving past prototypes to production-grade reliability"; r10 "AI still make mistakes" | `productionization-playbook` | NEW |
| 5 | Frontline fear / clinical augmentation | r07 nurse "Integrating AI into the clinical setting"; r09 "fear of replacement among clinicians" | `augmentation-frontline-engagement` | NEW |
| 6 | Peer-learning / vertical benchmarks | r05, r13, r17, r21, r22 — "hearing from others", "exchange best practices", "learn from other experiences" | `peer-case-library` | NEW |
| 7 | Portfolio observability + per-agent ROI | r17 "Organization don't have a view how the agent perform and ROI of each agent... unpredictable token consumption" | `ai-portfolio-observability` | NEW |
| 8 | Data readiness foundations | r14 "Data readiness"; r17 unstructured corpus | `stack-diagnostic` | EXISTING |
| 9 | Leadership conservatism / change | r06 "Management's being too conservative and bureaucratic"; r12 "Well establishment disrupted" | `readiness-conversation` | EXISTING |
| 10 | AI idea evaluation | r11 SME founder use cases; r16 govt "what to adopt" | `ai-idea-diagnostic` | EXISTING |
| 11 | Agent governance | r19 "Governance and risk-management frameworks that work in practice" | `agent-guardrail-imda` | EXISTING |
| 12 | Build vs. buy / SME tooling | r11 SME founder; r18 "high quality SMB specific vendors" | `buy-vs-build` | EXISTING |
| 13 | Pilot structure | (cross-cluster) | `pilot-design` | EXISTING |
| 14 | ROI gating | (cross-cluster) | `roi-gate-pwc` | EXISTING |
| 15 | Maturity baselining | (cross-cluster) | `maturity-assessment` | EXISTING |

---

## Audit summary

Pre-audit coverage of the 8 original skills against the 13 participant clusters: **1 covered, 4 partial, 8 gap**. Post-audit, the 7 new skills close all 8 gaps, with one near-cluster (#9 leadership conservatism) reinforced via the existing `readiness-conversation` four-role gap analysis.

| Gap heat | Cluster | Closing skill |
|---|---|---|
| HOT | use-case-selection | `use-case-discovery` |
| HOT | tool-overload-sme | `use-case-discovery` + `buy-vs-build` |
| HOT | peer-learning-benchmarks | `peer-case-library` |
| WARM | data-confidentiality-privacy | `data-trust-deployment-pattern` |
| WARM | fear-of-replacement | `augmentation-frontline-engagement` |
| WARM | education-academic-integrity | `data-trust-deployment-pattern` (FERPA tier) + `workforce-literacy-curriculum` |
| WARM | prototype-to-production | `productionization-playbook` |
| WARM | internal-ai-operating-model | `ai-portfolio-observability` |

---

## Test cases

Each new skill ships with at least one participant-grounded end-to-end test case under `skills/<skill>/cases/`:

| Skill | Case | Persona |
|---|---|---|
| `use-case-discovery` | `restaurant-director-r02.md` | 12-store restaurant chain director |
| `workforce-literacy-curriculum` | `cfo-tech-r03.md` | CFO, 1,200-person mid-cap tech, EU subsidiary |
| `data-trust-deployment-pattern` | `risk-analyst-finance-r01.md` | MAS-regulated finance company, credit-memo drafter |
| `productionization-playbook` | `proptech-founder-r15.md` | Solo founder, Zeno AI PropTech |
| `augmentation-frontline-engagement` | `nurse-clinician-r07.md` | Asst Nurse Clinician, psychiatric inpatient ward |
| `peer-case-library` | `healthcare-md-r05.md` | MD, 4-hospital Singapore healthcare group |
| `ai-portfolio-observability` | `enterprise-it-consulting-r16.md` | EAE running 20-agent portfolio at regional bank |
