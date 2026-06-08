---
name: maturity-assessment
description: Use when plotting an organization's AI maturity stage, assessing where an org sits on the AI capability curve, benchmarking AI progress against industry peers, setting AI strategy ambition level, or preparing a board-level AI readiness briefing. Phrases like "where are we on the AI maturity curve?", "assess our AI maturity", "benchmark our AI progress", "what stage are we at for AI?", "help me understand how mature our AI capabilities are", "prepare a board briefing on our AI readiness" all trigger this skill. Runs MIT CISR's four-stage model alongside Accenture's Foundation × Differentiation 2×2, surfaces the binding constraint (platform gap vs. strategy gap), and outputs a maturity placement with a prioritized roadmap to the next stage.
---

# AI Maturity Assessment

Plot the organization on the AI maturity curve. Identify the binding constraint. Build the roadmap to the next stage.

Two complementary frameworks: MIT CISR's four-stage sequential model (where are we, and what is next?) + Accenture's Foundation × Differentiation 2×2 (what is the binding constraint that's keeping us here?). Use both — they answer different questions.

---

## Part 1: MIT CISR Stage Placement

Four stages, empirically associated with financial performance. Stages 1–2 = below-industry performance. Stages 3–4 = above-industry performance. The Stage 2 → Stage 3 transition is the most important threshold. (Consult `mit-cisr-4-stages.md`)

**Stage diagnostics — answer each with evidence:**

**Stage 1 signals (Experiment and Prepare, 28% of firms):**
- [ ] AI literacy program in place for board and senior leadership
- [ ] Acceptable-use policy for AI exists and is enforced
- [ ] Data accessibility initiative underway
- [ ] Individual AI experiments happening but no tracked, value-attributed pilots
- NOT yet: systematic pilots, APIs sharing data cross-silo, shared platform

**Stage 2 signals (Build Pilots and Capabilities, 34% of firms):**
- [ ] Tracked pilots with named business cases and measured value
- [ ] Data APIs connecting some silos
- [ ] LLMs in use to augment work in at least one function
- [ ] Internal storytelling about pilot learnings happening
- NOT yet: enterprise-wide platform; reusable models; test-and-learn as default; cross-function value

**Stage 3 signals (Develop AI Ways of Working, 31% of firms):**
- [ ] Shared AI platform with reusable services
- [ ] Business dashboards showing AI performance and value
- [ ] Test-and-learn is the default operating mode across functions
- [ ] Foundation models and SLMs in systematic use
- [ ] AI value visible and attributed across the organization

**Stage 4 signals (Become AI Future Ready, 7% of firms):**
- [ ] AI embedded in all default decision-making
- [ ] Selling AI capability as a service externally
- [ ] Combining analytical + generative + agentic + robotic AI
- [ ] CEO-level KPI on AI outcomes (e.g., DBS: 1,000 experiments/year)

STAGE PLACEMENT: [Stage 1 / Stage 2 / Stage 3 / Stage 4]
Note: firms self-flatter. Use the NOT-YET criteria to triangulate. If the Stage 3 signals require "shared AI platform" and the org doesn't have one — it's not Stage 3, regardless of pilot count.

Output:
STAGE PLACEMENT | KEY EVIDENCE | NOT-YET GAPS | NEXT-STAGE PREREQUISITES

---

## Part 2: Accenture Foundation × Differentiation Assessment

The Accenture 2×2 identifies the binding constraint — not just where you are, but WHY you're there. (Consult `accenture-maturity-archetypes.md`)

**Foundation capabilities (x-axis):** Score each LOW / MEDIUM / HIGH
- Cloud platform and AI infrastructure
- Data platform (unified, accessible, AI-ready)
- Model lifecycle management (MLOps)
- AI governance documentation and operation
- Technical documentation and reproducibility

**Differentiation capabilities (y-axis):** Score each LOW / MEDIUM / HIGH
- C-suite AI strategy (ratified, not just endorsed)
- CEO + senior sponsorship (champion posture, not cheerleader)
- AI talent strategy (hiring, training, retention)
- Innovation culture (test-and-learn as default, not exception)
- Responsible AI by design (embedded in process, not bolt-on)

ARCHETYPE PLACEMENT:
- Foundation HIGH + Differentiation HIGH → **AI Achiever (12%)** — 50% greater revenue growth vs. peers
- Foundation LOW + Differentiation HIGH → **AI Innovator (13%)** — vision-without-execution; binding constraint: platform
- Foundation HIGH + Differentiation LOW → **AI Builder (12%)** — substrate-without-strategy; binding constraint: strategy/culture
- Foundation LOW + Differentiation LOW → **AI Experimenter (63%)** — no anchor; binding constraint: Foundation first

BINDING CONSTRAINT: [Foundation / Differentiation / Both]

Output:
FOUNDATION SCORE | DIFFERENTIATION SCORE | ARCHETYPE | BINDING CONSTRAINT

---

## Part 3: Performance Context

Frame the maturity placement against the performance data.

FINANCIAL PERFORMANCE IMPLICATION (from MIT CISR):
- Stage 1: −12.6 pp vs. industry average on revenue; −9.6 pp on profit
- Stage 2: −3.5 pp vs. industry average on revenue; −2.2 pp on profit
- Stage 3: +11.3 pp vs. industry average; +8.7 pp on profit
- Stage 4: +17.1 pp vs. industry average; +10.4 pp on profit

The gap between Stage 2 and Stage 3 is +14.8 pp on revenue. This is not a technology decision — it is a platform and culture investment decision.

AI PORTFOLIO OBJECTIVE MIX (consult `mckinsey-3-objective-mix.md`):
- What percentage of the current AI portfolio is efficiency vs. growth vs. innovation?
- 100% efficiency = structural cap on value; not a technology issue
- High performers add growth/innovation objectives

PwC REINFORCEMENT:
- Efficiency-only = 1.6× leader-laggard productivity gap
- Reinvention = 2.6× leader-laggard gap
- Documented Responsible AI strategy = 1.7× more likely to be an AI leader

Output:
FINANCIAL PERFORMANCE IMPLICATION | OBJECTIVE MIX | VALUE CEILING

---

## Part 4: Roadmap to the Next Stage

Produce a stage-advancement roadmap based on Parts 1–3.

CURRENT STATE SUMMARY:
- MIT CISR Stage: [X]
- Accenture Archetype: [Y]
- Binding constraint: [Foundation / Differentiation / Both]

TARGET STATE (next stage):
- What does the target stage look like for this org specifically?
- What is the time horizon? (CISR recommends defining this explicitly)

CAPABILITY GAPS (ordered by priority):
1. [Gap 1 — specific; binding constraint first]
   - Required action: [specific]
   - Owner: [function or role]
   - Timeline: [weeks/months]
2. [Gap 2]
3. [Gap 3]

BOLD GOAL (required for Stage 4 aspiration):
- DBS Bank example: 1,000 experiments/year; S$370M AI economic impact
- What is the equivalent bold, tangible goal for this organization?
- Without a named goal, the Stage 4 conversation is aspirational, not operational

NEXT REVIEW CADENCE: [Quarterly / Bi-annual — stage does not change in 30 days]

Output:
CURRENT STATE SUMMARY | TARGET STATE | CAPABILITY GAPS (ordered) | BOLD GOAL | REVIEW CADENCE

---

## References

- `mit-cisr-4-stages.md` — four-stage model; performance data; Stage 3 inflection; DBS/Ping An exemplars
- `accenture-maturity-archetypes.md` — Foundation × Differentiation 2×2; archetype definitions; Achiever performance premium
- `mckinsey-3-objective-mix.md` — efficiency/growth/innovation objective mix
- `pwc-roi-2026-governance.md` — 1.6× vs. 2.6× productivity gap; 1.7× RAI advantage
- `bcg-future-built.md` — Future-Built archetype; multi-dimensional investment
- `deloitte-cheerleader-to-champion.md` — 74/21 governance gap; HR five jobs
- `hiten-skill-library.md` — skill library as the Stage 3–4 knowledge architecture

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
