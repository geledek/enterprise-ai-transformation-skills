# Enterprise AI Transformation Skills

Fifteen installable skills that help executives, operators, and consultants run enterprise AI transformation — from "where do we start?" to "is our agent governed correctly?" — distilled from 21 flagship research sources (Stanford, MIT, McKinsey, BCG, Deloitte, PwC, Accenture, NIST, EU AI Act, IMDA, WEF) published 2024–2026.

> **TL;DR.** 95% of enterprise GenAI pilots return zero P&L impact. The 5% that win don't have better models — they operate differently across **people, process, technology**, and a layer of **general** strategy/diagnostics. This skill library encodes those operating patterns. Each skill is a structured prompt the AI runs for you; you ask the question, the skill produces a board-ready output.

---

## The four buckets (30 seconds)

Skills are grouped by what they fix. Pick the bucket that matches your problem; pick the skill inside it that matches the question.

| Prefix | What it covers | Use when… |
|---|---|---|
| `general-` | Cross-cutting strategy, selection, diagnosis | You don't yet know *which* layer is broken |
| `people-` | Leadership, workforce, frontline change | Tech works, value isn't landing |
| `process-` | Pilot design, productionization, observability | You have a candidate / a prototype / a portfolio |
| `tech-` | Stack, sourcing, data deployment, agent guardrails | You're choosing a vendor, a tier, a model, or governing an agent |

**The default order is general → process → tech → people**, but most real engagements jump around. The "Which skill when?" decision tree below does the picking for you.

---

## Which skill when? — Decision tree

**Start here.** Read top to bottom; stop at the first row that matches.

| Your situation | Skill to invoke | Bucket |
|---|---|---|
| "We don't know where to point AI first." | `general-use-case-discovery` | general |
| "We have an idea — should we pursue it?" | `general-idea-diagnostic` | general |
| "Where are we on the AI maturity curve, and what's next?" | `general-maturity-assessment` | general |
| "Has anyone else done this before?" | `general-peer-cases` | general |
| "Should we approve this AI investment / fund this program?" | `general-roi-gate` | general |
| "How should we structure the 90-day pilot?" | `process-pilot-design` | process |
| "Demo works — how do we move it to production?" | `process-productionization` | process |
| "We've shipped 10 agents — what's the net ROI?" | `process-portfolio-observability` | process |
| "Diagnose our AI tech stack — where's the weakest link?" | `tech-stack-diagnostic` | tech |
| "Should we build, buy, or partner for this AI capability?" | `tech-buy-vs-build` | tech |
| "Where can this data legally run? ChatGPT? Enterprise SaaS? VPC?" | `tech-data-deployment` | tech |
| "We're about to launch an AI agent — is it safely governed?" | `tech-agent-guardrail` | tech |
| "Why isn't our AI investment moving the needle? (people gaps)" | `people-readiness-conversation` | people |
| "We need an AI literacy / EU AI Act Art. 4 training program." | `people-literacy-curriculum` | people |
| "Frontline experts (clinicians, lawyers, agents) are blocking the pilot." | `people-frontline-engagement` | people |

If your question hits multiple rows, run the **higher one first** — it sets context for the rest.

---

## Get started in 5 minutes

### Install once

**Claude Desktop (easiest)** — Customize → Plugins → Upload custom plugin → paste:
```
https://github.com/geledek/enterprise-ai-transformation-skills
```
Restart. All 15 skills activate from their trigger phrases.

**Claude Code** — `claude plugin install https://github.com/geledek/enterprise-ai-transformation-skills`

**No paid plan?** — Open a Project at [claude.ai](https://claude.ai), paste any single skill's `SKILL.md` into Project Instructions, upload relevant `references/` files as Project Knowledge. One skill per Project.

Full instructions for ChatGPT / Grok / others: see [`INSTALL.md`](INSTALL.md).

### Try your first skill (2 minutes)

Pick the question from the decision tree closest to your real situation, then ask the AI in plain English. Examples:

- *"Should we pursue an AI agent that auto-approves expense reports under S$200?"* → triggers `general-idea-diagnostic`
- *"Where should we point AI first across our claims operation?"* → triggers `general-use-case-discovery`
- *"Design a 90-day pilot for an RM call-prep summarizer at our private bank."* → triggers `process-pilot-design`
- *"We deployed 11 agents but can't see what they're earning. Help."* → triggers `process-portfolio-observability`
- *"Our senior lawyers are openly hostile to the contract-review AI. What now?"* → triggers `people-frontline-engagement`

Each skill walks the AI through 4–7 structured roles and produces a verdict (Fund / Reframe / Kill, Greenlight / Stage / Park, Approved / Conditional / Blocked, etc.). The output is meant to be sponsor-ready.

---

## A typical executive flow

For a leader running an end-to-end AI transformation, this is the canonical sequence. You can branch off at any point — the buckets are designed to be invoked individually too.

```
┌─ general-maturity-assessment ─── where are we today?
│
├─ general-use-case-discovery ──── what should we pilot first?
│      │
│      └─ general-idea-diagnostic ─ is THIS specific idea worth doing?
│             │
│             └─ tech-data-deployment ─ where can the data legally run?
│                    │
│                    └─ process-pilot-design ─ design the 90-day pilot
│                           │
│                           └─ general-roi-gate ─ approve / fund / reject
│                                  │
│                                  └─ tech-buy-vs-build ─ buy or build?
│                                         │
│                                         └─ process-productionization ─ ship to prod
│                                                │
│                                                └─ tech-agent-guardrail ─ govern at runtime
│                                                       │
│                                                       └─ process-portfolio-observability ─ track net ROI
│
├─ people-readiness-conversation ── (run quarterly — surfaces gaps the tech can't fix)
├─ people-literacy-curriculum ───── (close the literacy gap, satisfy EU AI Act Art. 4)
├─ people-frontline-engagement ──── (when fearful experts are blocking rollout)
│
├─ general-peer-cases ──────────── (pull at any decision point: "what have others done?")
└─ tech-stack-diagnostic ───────── (run before any major scaling decision)
```

For full-transcript worked examples — four single-skill walkthroughs and five chained-flow operating decisions — see [`docs/usage-guide.md`](docs/usage-guide.md).

---

## Cross-skill cautions

These skills were tested together. A few real interactions worth knowing about:

- **Customer-facing pilots.** `general-use-case-discovery` will surface customer-pain pools (NPS, conversion drop). `process-pilot-design` will downrate any first pilot with customer-facing blast radius. The discovery skill now defaults customer-facing candidates to **Stage-and-watch** unless the sponsor explicitly accepts the risk in the brief. Trust the pilot-design skill on first-pilot scope.
- **Three different "70/20/10"s.** Different sources use the same digits for different things. Each skill is now explicit about which one applies:
  - `general-use-case-discovery` / `general-peer-cases` → **BCG 10/20/70 effort split** (10% algorithm / 20% tech / 70% people-process)
  - `process-portfolio-observability` → **70/20/10 portfolio mix** (70% core / 20% adjacent / 10% transformational)
  - `people-literacy-curriculum` → **70-20-10 training-budget split** (70% sandbox / 20% delivery / 10% content)
- **"BCG 88/25" can mean two things.** `people-readiness-conversation` and `people-literacy-curriculum` use it for *manager role-modeling*. `tech-data-deployment` uses the same digits for *broad-use-vs-value gap*. Both anchors are real; the skills now flag which one they mean.
- **Verdict vocabularies differ across gating skills** by design — concept-stage (`general-idea-diagnostic` → Fund / Reframe / Kill), portfolio-selection (`general-use-case-discovery` → Greenlight / Stage / Park / Reject), funding-approval (`general-roi-gate` → Approve / Conditional / Return / Reject). They sit at different points in the lifecycle. Don't run all three on the same question.
- **CEO public commitment vs. no-headcount-cut clause.** `people-readiness-conversation` recommends a CEO-owned measurable productivity number. `people-frontline-engagement` requires a no-headcount-cut clause for pilot duration. These reconcile — public commitment is on outcome, the clause is on pilot-window — but the CEO must say so explicitly to the frontline.

---

## Who is this for

- **Investors** evaluating AI-first companies and AI initiative funding proposals
- **Operators** running AI transformation programs, CoEs, or portfolio pilots
- **Founders** assessing build vs. buy, structuring AI product strategy
- **Boards and executives** needing structured frameworks for AI governance and investment decisions
- **Consultants and advisors** delivering enterprise AI strategy engagements

Skills produce board-ready outputs. No coding required to use them.

---

## How to extend

Three forks:

1. **Add references** — drop an extract into `references/`, follow the file shape in `references/_index.md`, update `_index.md`. Skill descriptions reference files by filename, not path.
2. **Add cases** — drop a diagnosed case into the relevant `skills/<bucket>-<skill>/cases/`. The skill will pull the closest analog automatically.
3. **Fork a skill** — copy any `SKILL.md`, rename it, adjust the role instructions and reference pointers for your sector, internal processes, or role-specific context.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full contribution shape.

---

## Sources

21 flagship sources, 2024–2026:

| ID | Source |
|---|---|
| `stanford-ai-index-2026` | [Stanford AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |
| `mit-nanda-2025` | MIT NANDA GenAI Deployment Study 2025 |
| `mckinsey-state-ai-2025` | [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) |
| `bcg-bffxai-2026` | BCG Build for the Future x AI 2026 |
| `deloitte-ai-leaders-2026` | [Deloitte AI Leaders Survey 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html) |
| `pwc-roi-2026` | [PwC ROI Report 2026](https://www.pwc.com/gx/en/issues/technology/ai-performance.html) |
| `pwc-agentic-playbook-2026` | PwC Agentic AI Playbook 2026 |
| `accenture-co-intelligence-2026` | Accenture Co-Intelligence 2026 |
| `accenture-maturity-global` | Accenture AI Maturity Global 2024 |
| `mit-cisr-2024` | MIT CISR AI Maturity Stages 2024 |
| `nist-ai-rmf` | [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) |
| `eu-ai-act-2024` | [EU AI Act 2024](https://artificialintelligenceact.eu/the-act/) |
| `imda-agentic-2026` | IMDA Agentic AI Framework 2026 |
| `wef-rai-2024` | WEF Responsible AI Playbook 2024 |
| `landing-ai-playbook` | [Landing AI Enterprise Transformation Playbook](https://landing.ai/resources/ai-transformation-playbook/) |
| `andrew-ng-moats` | Andrew Ng — Three AI Moats |
| `isg-genai-2025` | ISG GenAI Enterprise Research 2025 |
| `bcg-manager-modeling` | BCG Role-Modeling Research 2026 |
| `hiten-shah-skill-library` | Hiten Shah — "Every Company's First AI Strategy Should Be a Skill Library", June 2026 |
| `accenture-five-success` | Accenture Five Success Factors 2025 |
| `wharton-skills-index` | Wharton-Accenture Skills Index 2025 |

See [`references/`](references/) for curated extracts from each source.

---

## License

MIT — see [`LICENSE`](LICENSE).

## Author

Ray Han · June 2026
