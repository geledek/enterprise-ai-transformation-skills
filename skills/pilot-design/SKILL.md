---
name: pilot-design
description: Use when designing an AI pilot, structuring a proof-of-concept, or preparing to test an AI idea before full investment. Phrases like "how should we structure this pilot?", "what does a 90-day AI pilot look like?", "help me design the test for this AI initiative?", "we want to pilot AI for X — what do we need?", "what metrics should we track?" all trigger this skill. Runs a structured 7-question pilot design protocol: scope, problem, pre-deployment metrics, blast radius, stop conditions, workflow redesign, ownership. Outputs a one-page pilot brief ready for sponsor approval.
---

# AI Pilot Design

Design a 90-day AI pilot with pre-deployment metrics, stop conditions, and workflow redesign baked in. Seven questions. One-page output ready for sponsor approval.

The discipline: narrow scope, pre-deployment metrics, workflow redesign before technology. AI bolted onto a legacy workflow is the #1 process failure mode (Stanford AI Index 2026 — consult `stanford-51-deployments.md`).

---

## Role 1: Scope and Problem Framing

Answer the two foundational questions before any technology decisions.

**SCOPE CHECK — Scope × Execution Grid** (consult `95-5-genai-divide.md`):
- Narrow scope + simple execution = fast wins (target this quadrant)
- Narrow scope + complex execution = early pilots (proceed with caution)
- Broad scope = partial pilots or failure (justify explicitly if broad scope is proposed)

Classify the proposed pilot:
- What is the scope? (One function, one workflow, one user group)
- What is the execution complexity? (Simple / Complex)
- Is this upper-left on the grid?

**PROBLEM STATEMENT:**
State the friction this pilot addresses in one sentence. This should be friction-first ("users struggle with X because of Y"), not tech-first ("we want to test AI for Z").

Output:
SCOPE | COMPLEXITY | GRID POSITION | FRICTION STATEMENT

---

## Role 2: Pre-Deployment Metrics

Name the metrics BEFORE the pilot launches. If you can't name them now, the pilot isn't ready.

THE MEASUREMENT-GAP WARNING (consult `european-fintech-case.md`):
A leading European fintech replaced 700 agents with one AI system. Tracked volume, response time, cost. Did NOT track resolution quality, repeat-contact rate, CSAT. CSAT dropped 22%. Hiring resumed within months.

Name three metrics that prove this pilot is working:
1. [Metric 1 — what it measures, how it will be tracked]
2. [Metric 2 — what it measures, how it will be tracked]
3. [Metric 3 — what it measures, how it will be tracked]

For each metric, answer:
- Would this naturally get tracked, or does it require additional instrumentation?
- Is this the metric that matters, or the metric that's easy?

Flag any gap between what matters and what will actually be measured.

Output:
METRIC 1 | METRIC 2 | METRIC 3 | MEASUREMENT GAP FLAG

---

## Role 3: Blast Radius Assessment

If this pilot fails on day one, who sees it?

BLAST RADIUS OPTIONS (from most to least contained):
1. Internal team only — developer and data team see the failure
2. Internal users — employees using the tool see the failure
3. Paying customers — customer experience degrades
4. Regulators — compliance failure triggers regulatory attention
5. Public — reputational damage

State the worst plausible blast radius. Set the reliability bar accordingly:
- Internal only → higher tolerance for failure, faster iteration acceptable
- Customers or regulators → human-in-loop required; stop conditions must be tighter

Output:
BLAST RADIUS | RELIABILITY BAR | HUMAN-IN-LOOP REQUIREMENT

---

## Role 4: Stop Conditions

Define what causes the pilot to pause for diagnosis at day 30, 60, and 90.

A pilot without stop conditions drifts to perpetual "almost ready." Stop conditions are forcing functions for metric discipline.

For each milestone:
- **Day 30:** What signal must be present to continue? (Example: adoption rate ≥X%, no critical error events)
- **Day 60:** What signal must be present to continue to production evaluation? (Example: Metric 1 ≥Y, Metric 3 not deteriorating)
- **Day 90:** What is the pass/fail verdict criterion? (Example: Metric 2 ≥Z AND no customer-facing errors)

State: if Day 30 stop condition is not met, what happens? (Pause + diagnose / scope reduction / kill)

Output:
DAY 30 CONDITION | DAY 60 CONDITION | DAY 90 VERDICT CRITERION | FAILURE RESPONSE

---

## Role 5: Workflow Redesign

AI bolted onto a legacy workflow produces marginal benefit at best. Redesign the workflow before deploying (consult `mckinsey-workflow-redesign.md`).

Answer the five redesign questions:
1. What is this workflow trying to accomplish?
2. Which steps exist only because of constraints that AI removes?
3. Which steps add value and must be kept?
4. Which steps can be eliminated entirely?
5. What does the redesigned workflow look like?

Sketch the redesigned workflow (before AI touches the legacy version). This is the target state. AI deployment is the path to this state — not an addition to the current state.

Output:
ELIMINATED STEPS | PRESERVED STEPS | REDESIGNED WORKFLOW DESCRIPTION

---

## Role 6: Ownership and Sponsorship

A pilot without a named individual owner is a committee experiment. Committees don't make the decisions that matter when the pilot hits friction.

Name:
- **Pilot owner:** one person accountable for outcomes (not a team)
- **Sponsor:** the executive who has committed resources and will review Day 30/60/90 checkpoints
- **User champion:** the functional lead who will drive adoption within the affected team

Output:
PILOT OWNER | SPONSOR | USER CHAMPION

---

## Role 7: Pilot Brief (Synthesis)

Produce a one-page pilot brief from Roles 1–6. Write for sponsor approval. Be direct.

**PILOT BRIEF**

**Problem:** [One-sentence friction statement from Role 1]
**Scope:** [Narrow scope + grid position from Role 1]
**Workflow:** [Redesigned workflow from Role 5]
**Metrics:**
- [Metric 1]
- [Metric 2]
- [Metric 3]
**Blast radius:** [From Role 3]
**Stop conditions:**
- Day 30: [Condition]
- Day 60: [Condition]
- Day 90: [Verdict criterion]
**Ownership:** [Owner / Sponsor / User champion from Role 6]
**Duration:** 90 days
**Budget ask:** [If known; else "TBD pending sponsor meeting"]

**Recommendation:** [Proceed / Proceed with modification / Do not proceed — one sentence]

---

## References

- `95-5-genai-divide.md` — Scope × Execution Grid; 90-day timeline; narrow-scope success patterns
- `stanford-51-deployments.md` — invisible-costs; workflow-redesign-first; pre-deployment metrics discipline
- `european-fintech-case.md` — measurement-gap reference case
- `pilot-discipline-ng.md` — cross-source pilot discipline synthesis
- `mckinsey-workflow-redesign.md` — 3× workflow redesign; AI-bolted-onto-legacy failure mode

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
