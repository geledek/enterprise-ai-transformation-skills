# Use-Case Discovery

Generates, scores, and ranks AI use-case candidates through four sequential roles into a TOP-3 portfolio.

## What it does

1. Maps value pools by sub-function — quantifies FTE-hours, rework tax, revenue leak, and NPS pain; refuses any candidate without a $500K/yr or 2-FTE or 5-pt NPS pool
2. Classifies each candidate against five Stanford archetypes (chatbot, RAG, co-pilot, multi-step agent, decision-support) using Andrew Ng's one-second test, integration depth, and user-frequency filters
3. Scores 0-3 across six dimensions (data availability, data rights, three Ng moats, tech-vs-change ratio); kills anything under 12/18
4. Plots survivors on a value × feasibility 2x2 and applies pilot-discipline filters (narrow / reversible / measurable / owned) to issue Greenlight, Stage-and-watch, Park, or Reject
5. Outputs TOP-3 ranked portfolio, first-pilot pick with kill date and named owner, why-not-others, and a kill list

## When to use it

When a leader cannot decide where to point AI first across a function or business unit. Triggered by phrases like "how to focus on areas where AI can be utilized," "which use case should we pilot first," "decide among the myriad of choices," or "knowing what to adopt." Use it before committing pilot budget, when a vendor short-list is overwhelming, or when the CEO has demanded a fixed number of pilots without selection criteria.

## What it outputs

- Value-pool table — sub-function, pain type, annual value, McKinsey objective bucket, evidence source
- Archetype classification — one-second test, integration depth, user frequency per candidate
- Feasibility scorecard — data score, moat score, effort score, total /18, kill-or-keep
- 2x2 placement and verdict frame (Greenlight / Stage-and-watch / Park / Reject)
- TOP-3 ranked use cases with first-pilot pick (named owner, success metric, kill date)
- Why-not-others rationale and kill list with one-line reason each

## Example

**Scenario:** Hiroshi Nakamura is COO of Sankai Logistics, an Osaka-based 3PL with ¥38B revenue, 1,400 staff across 6 distribution centers serving Western Japan e-commerce and FMCG clients. The board allocated ¥600M for AI after a McKinsey-style review flagged the company as "AI-laggard." His IT director has forwarded 23 vendor decks. The CEO wants three pilots launched by Q4. Hiroshi has 10 weeks to the next board meeting and faces a vendor short-list where every pitch sounds equally compelling, with a CFO skeptical after past failed digital projects.

**User prompt:**

> I need help. I'm COO of Sankai Logistics — Osaka-based 3PL, ¥38B revenue, 1,400 staff, six DCs in Western Japan. The board has approved ¥600M for AI and the CEO wants three pilots running by Q4. My inbox has 23 vendor pitches: warehouse picking co-pilots, a chatbot for shipper inquiries, route optimization, IDP for customs paperwork, predictive maintenance for our forklifts, demand forecasting, an HR resume screener, contract review for our shipping agreements, and more. Every vendor swears theirs is the highest ROI. I have 10 weeks until the next board review. How do I figure out which two or three to actually pilot first, and how do I defend that choice to a skeptical CFO who's seen too many failed digital projects?

**Skill output (excerpt):**

```
ROLE 1 — VALUE POOLS (≥¥50M threshold)
SUB-FUNCTION              | PAIN          | ANNUAL POOL | OBJECTIVE
Customs paperwork (IDP)   | rework + SLA  | ¥420-500M   | Productivity
Route planning (W-Japan)  | fuel + OT     | ¥350-450M   | Productivity
Forklift maintenance      | downtime      | ¥120-180M   | Productivity
Shipper-inquiry chatbot   | deflection    | ¥40-60M     | (below threshold)
HR resume screener        | unquantified  | —           | KILL — no pool

ROLE 2 — ARCHETYPE
USE CASE          | ARCHETYPE          | 1-SEC | INTEGRATION  | FREQ
Customs IDP       | Workflow co-pilot  | YES   | WMS embedded | Daily power-user
Route opt         | Decision-support   | NO    | TMS embedded | Daily planner
Forklift PdM      | Decision-support   | NO    | Sensor-dep.  | Once-a-month
Shipper chatbot   | Chatbot (bolt-on)  | YES   | Standalone   | Once-a-month
                  → 95/5 anti-pattern; JP B2B deflection ceiling ~18%

ROLE 3 — FEASIBILITY (0-3 x 6, kill <12)
USE CASE       | DATA | MOAT | EFFORT | /18  | VERDICT
Customs IDP    |  5   |  6   |   5    | 16/18| KEEP
Route opt      |  4   |  5   |   3    | 12/18| KEEP (sponsor risk)
Forklift PdM   |  1   |  3   |   2    |  6/18| KILL (sensor retrofit)
Shipper chat   |  3   |  2   |   3    |  8/18| KILL (bolt-on)

ROLE 4 — PORTFOLIO
TOP-3 RANKED
#1 Customs IDP co-pilot   — Greenlight, ¥420M pool, 16/18
#2 Route optimization     — Stage-and-watch, sponsor TBD
#3 (none clears bar)      — return what we have; do NOT pad

FIRST PILOT — Customs IDP co-pilot
  Owner: COO (Hiroshi). Embedded in WMS at Osaka DC.
  Metric: ¥-per-declaration ↓35% on 8K decs/mo by week 10.
  Kill date: 60 days. Reversible (manual fallback intact).

WHY NOT #2: route opt needs named TMS owner + driver buy-in;
            revisit Q1 once IDP verdict lands.
WHY NOT 3rd: do not parallelize. Sequencing rule: one pilot, one verdict.

KILL LIST
- Shipper chatbot — 95/5 bolt-on; sub-threshold pool.
- Forklift PdM    — sensor data does not exist.
- HR screener     — no quantified pool; EU AI Act high-risk.
- Contract review — no power-user; once-a-month frequency.
```

**How to read this output:**

- Start with the value-pool table — anything below the ¥50M / 2-FTE / 5-pt-NPS threshold should not have advanced. If it did, the skill failed upstream.
- The feasibility /18 column is load-bearing: anything <12 is a kill, not a "monitor." Push back if a candidate scoring 11/18 appears in the TOP-3.
- The sequencing rule (one Greenlight pilot per quarter, no parallelization) is the single most-violated discipline. If the output recommends three parallel pilots, the skill did not run — that is the kb-ask failure mode this skill exists to prevent.
- Kill-list reasons should each map to a named structural test (one-second test, 95/5 bolt-on, missing pool). Vague reasons mean the discipline broke.
- The first-pilot pick must name a senior owner, a pre-declared metric tied to the value pool, and a kill date. Anonymous owners or "TBD" metrics are reject conditions.

## Sources used

- `mckinsey-3-objective-mix.md` — productivity / growth / transformation portfolio balance, ~50/30/20 default
- `andrew-ng-three-moats.md` — proprietary data, workflow embedding, distribution as the only durable applied-AI moats
- `pilot-discipline-ng.md` — narrow + reversible + measurable + owned filter for first-pilot selection
- `stanford-51-deployments.md` — empirical archetype taxonomy from 51 enterprise deployments
- `95-5-genai-divide.md` — MIT finding that 95% of GenAI pilots show zero P&L; the 5% are embedded co-pilots not standalone chatbots
- `bcg-future-built.md` — 10/20/70 effort split (algorithm / tech / people-and-process)
- `isg-data-foundation.md` — four-pillar data readiness check (availability, rights, quality, lineage)

## Effectiveness

Effectiveness test (2026-06-12): scored 24/25 (Grade B, +5.34 lift over the strongest baseline of vanilla LLM and kb-ask retrieval). 3-judge unanimous verdict.

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
