---
name: general-use-case-discovery
description: Use when a leader cannot decide where to point AI first across a function or business unit. Phrases like "how to focus on areas where AI can be utilized", "finding a useful productive case use", "knowing what to adopt and how to use agentic", "decide among the myriad of choices", "which use case should we pilot first", all trigger this skill. Generates, scores and ranks candidate AI use cases through four sequential roles — Value-Pool Mapper, Capability Archetype Classifier, Feasibility & Moat Scorer, Portfolio Sequencer — and outputs a TOP-3 ranked portfolio with first-pilot pick, why-not-others, and kill list.
---

# General — Use-Case Discovery

Most enterprises drown in candidate ideas and pilot the wrong one. MIT's 95/5 finding shows 95% of GenAI pilots return zero P&L impact — the failure is upstream, in selection. Stanford's 51-deployment study shows winners cluster around narrow, repetitive, measurable workflows. Run the four roles below before committing budget.

Anchor: McKinsey's three-objective mix (productivity / growth / transformation), Andrew Ng's three moats, BCG 10/20/70 effort split.

## Role 1: Value-Pool Mapper

Where is the dollar-or-hour pain, by sub-function? Do not start from "what can AI do" — start from where the bleeding is.

1. **Where do FTE-hours concentrate?** (Pull headcount × time-on-task by sub-process. Top 3 buckets only.)
2. **Where is the rework / error / SLA-miss tax?** (Quality cost, not just labor cost.)
3. **Where is revenue leaking?** (Conversion drop-offs, abandoned carts, slow quoting, missed renewals.)
4. **What is the customer-experience pain that shows up in NPS verbatims?** (External, not internal.)
5. **Map each pool to McKinsey's 3-objective mix.** (Productivity = cost-out, Growth = topline, Transformation = new model. Aim ~50/30/20 across the portfolio — *consult `mckinsey-3-objective-mix.md`.*)

Refuse to advance any candidate without a quantified pool (≥$500K/yr or ≥2 FTE-equivalents or ≥5pt NPS).

Output:
SUB_FUNCTION | PAIN_TYPE | ANNUAL_VALUE_POOL | OBJECTIVE_BUCKET | EVIDENCE_SOURCE

## Role 2: Capability Archetype Classifier

Match the friction shape to a capability archetype. Do not let vendors pick the archetype for you.

Five archetypes (Stanford 51-deployments taxonomy — *consult `stanford-51-deployments.md`*):
- **Chatbot / Q&A** — single-turn, low-stakes, deflection plays.
- **RAG / Knowledge-surfacing** — retrieval over owned corpus, expert assist.
- **Workflow co-pilot** — embedded in a system of record, draft-and-approve.
- **Multi-step agent** — tool-use across systems, long-horizon tasks.
- **Decision-support / forecasting** — analytical, model-driven, advisory.

1. **Apply Andrew Ng's one-second rule.** (Is the human task something a competent human does in <1 second of cognition? If yes → automatable now. If it requires judgment under ambiguity → co-pilot, not agent.)
2. **Is the workflow well-defined or open-ended?** (Well-defined → workflow co-pilot. Open-ended → agent only if reversible — see `pilot-discipline-ng.md`.)
3. **Does the value require integration into a system of record?** (If yes, kill standalone chatbot framings — MIT 95/5 shows chatbots-on-the-side underperform 2x vs. embedded co-pilots.)
4. **Is the user a power-user or once-a-month-user?** (Once-a-month users do not adopt anything. Move it to backend automation.)

Output:
USE_CASE | ARCHETYPE | ONE_SECOND_TEST | INTEGRATION_DEPTH | USER_FREQUENCY

## Role 3: Feasibility & Moat Scorer

Score each candidate 0-3 on six dimensions. Anything scoring <12/18 goes to the kill list.

Data readiness (ISG four pillars — *consult `isg-data-foundation.md`*):
1. **Data availability.** (0 = does not exist, 3 = clean and accessible via API.)
2. **Data rights.** (0 = legal blocker, 3 = owned + permissioned for AI use.)

Moats (Andrew Ng's three — *consult `andrew-ng-three-moats.md`*):
3. **Proprietary data moat.** (Does winning here compound? 0 = commodity, 3 = unique corpus competitors cannot replicate.)
4. **Workflow moat.** (Is this embedded deep enough to create switching cost? 0 = bolt-on, 3 = re-architects the process.)
5. **Distribution moat.** (Do we already own the user surface? 0 = greenfield adoption, 3 = ships to existing seats.)

Effort (BCG 10/20/70 — *consult `bcg-future-built.md`*):
6. **Tech-vs-change ratio.** (0 = >70% change-management lift with no internal sponsor, 3 = sponsor secured + change runway funded. Tech is the easy 10%.)

Output:
USE_CASE | DATA_SCORE | MOAT_SCORE | EFFORT_SCORE | TOTAL_/18 | KILL_OR_KEEP

## Role 4: Portfolio Sequencer

Plot survivors on a 2×2: Value pool (Y) × Feasibility total (X). Pick the first pilot from the upper-right quadrant using pilot-discipline filters.

Pilot-discipline filters (Andrew Ng — *consult `pilot-discipline-ng.md`*):
1. **Narrow.** (One persona, one workflow, one system. If the pitch needs three orgs to align, reject.)
2. **Reversible.** (Can we kill it in 60 days with no contractual or reputational tail? If no, stage-and-watch.)
3. **Measurable.** (Pre-defined success metric tied to the value pool from Role 1. No metric → Park.)
4. **Owned.** (Named accountable senior — McKinsey shows 3x success rate when senior owns vs. delegates. Anonymous = Reject.)

Sequencing rule: ship one Greenlight pilot per quarter, queue 2 Stage-and-watch behind it, Park the long-tail, Reject the rest. Do not parallelize until pilot 1 has a verdict.

**Blast-radius default for first pilot.** When ranking candidates that pass Role 3, prefer internal-only blast radius (employees-as-users) for the first pilot unless the sponsor explicitly accepts customer-facing risk in the brief. Customer-facing pain pools surfaced in Role 1 Q3–Q4 default to Stage-and-watch until an internal-blast-radius variant exists or `process-pilot-design` Role 3 produces a tighter reliability bar. Rationale: Stanford 51-deployments shows ~60% of failed pilots launched on customer-facing surfaces with insufficient stop conditions.

Verdict states:
- **Greenlight** — meets all four pilot-discipline filters, ≥14/18 feasibility, value pool ≥$500K/yr, blast radius internal OR customer-facing with sponsor-signed reliability bar.
- **Stage-and-watch** — value present but data or moat <2, OR customer-facing without explicit sponsor risk acceptance; revisit in 90 days.
- **Park** — interesting, no sponsor or no metric; backlog only.
- **Reject** — fails one-second test, lacks value pool, or 95/5 chatbot-on-the-side pattern.

Output:
USE_CASE | QUADRANT | VERDICT | PILOT_RANK | METRIC | OWNER

## Synthesis

Produce the report:

**TOP-3 RANKED USE CASES** — table: rank, use case, archetype, value pool, total score, verdict.

**FIRST PILOT PICK** — one paragraph: who, what, where it embeds, success metric, kill date, accountable owner.

**WHY-NOT-OTHERS** — two-line rationale per #2 and #3 explaining what would move them to first-pilot status.

**KILL LIST** — every candidate that scored <12/18 or failed the one-second test or violated the 95/5 embedded-vs-bolt-on rule. One-line reason each.

Default stance: if fewer than 3 candidates clear the bar, return what you have and name the gap. Do not pad the portfolio.

## References

*All files below live in `references/` at the plugin root (`${CLAUDE_PLUGIN_ROOT}/references/` when installed as a plugin).*

- mckinsey-3-objective-mix.md — productivity / growth / transformation portfolio balance, ~50/30/20 default.
- andrew-ng-three-moats.md — proprietary data, workflow embedding, distribution as the only durable moats in applied AI.
- pilot-discipline-ng.md — narrow + reversible + measurable + owned filter for first-pilot selection.
- stanford-51-deployments.md — empirical archetype taxonomy from 51 enterprise deployments; pattern-match new candidates here.
- 95-5-genai-divide.md — MIT finding that 95% of GenAI pilots show zero P&L; the 5% are embedded co-pilots not standalone chatbots.
- bcg-future-built.md — 10/20/70 effort split (algorithm / tech / people-and-process); use to calibrate change-management weight.
- isg-data-foundation.md — four-pillar data readiness check (availability, rights, quality, lineage) feeding the feasibility score.

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
