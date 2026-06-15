# Restaurant Director r02 — From "AI for Menus and Chatbots" to a Prep-Demand Pilot

**One-line summary:** A 12-store casual dining director walks in convinced AI means menu optimization and a booking chatbot; the general-use-case-discovery skill reframes the portfolio around food-cost waste and labor scheduling, and picks demand-forecast-for-prep as the first pilot.

## Persona / Setup

**Who:** Director of Operations, mid-market casual dining group. 12 stores across Singapore and Klang Valley (Malaysia). ~600 staff (mostly part-time and FT crew, ~30 store managers and ASMs, 4 head office). Average ticket SGD 28. Mix of dine-in (65%), delivery aggregators (25%), takeaway (10%).

**Tech estate:** Cloud POS from a regional vendor (outsourced support contract). One IT manager at HQ. No data warehouse. Inventory tracked in a spreadsheet-plus-vendor-portal hybrid. Reservations split across Chope, Google, and a few Excel-on-WhatsApp store-level books. Aggregator dashboards (Grab, foodpanda, ShopeeFood) are siloed per platform.

**Data reality:** Two years of POS transactions exist but have never been pulled into one place. Recipe-level cost data lives in the chef's laptop. Labor scheduling is done by store managers in WhatsApp threads.

**The participant's words (survey r02):**
> "How to focus on areas where AI can be utilized... retail/restaurants leverage AI."

**The opening pitch in the room:**
> "I think AI is for menu optimization and chatbots. Everyone's talking about chatbots for booking. We should probably also look at AI to redesign our menu — drop the bottom sellers, push the high-margin items."

**Why this needs the skill:** The director has compressed all of "AI" into the two use cases that are most visible in trade press. He has not yet looked at where the actual dollar-and-hour pain is in his P&L. Food cost is running 34% (target 30%); labor is 28% (target 25%); both numbers come from his own opening remarks. Neither menu optimization nor a booking chatbot directly attacks those lines.

## Applying general-use-case-discovery

We run the four roles in sequence. The director is in the room with his IT manager and the group head chef. Total session time: 2.5 hours.

### Role 1 — Value-Pool Mapper

We ignore "AI" entirely for the first 40 minutes. The question is McKinsey-style: where is the dollar-or-hour pain by sub-function?

We walk the operating P&L of a single representative store (monthly revenue SGD 380K) and tag pain pools:

| Sub-function | Dollar / hour pain | Root cause named by participant |
|---|---|---|
| Food prep & inventory | ~SGD 22K/month/store food waste (over-prep + spoilage on slow days). 12 stores → ~SGD 264K/month group-wide. | "Managers over-prep on Mondays because they got burned once on a sudden lunch rush." |
| Labor scheduling | ~3% labor over-spend = ~SGD 11K/month/store. Manager spends 6–8 hrs/week building rosters in WhatsApp. | "Every store manager schedules from gut feel. No one looks at last year's same-week pattern." |
| Customer complaints | ~80–120 complaints/month group-wide across Grab, foodpanda, Google reviews, in-store cards. ~1.5 FTE at HQ triaging. Slow response cited by 3 store managers as reputation risk. | "By the time we see a Google 1-star, the customer is already gone and the post is up." |
| Menu engineering | Bottom-quartile SKUs contribute <8% revenue, but waste analysis was last done 18 months ago. Pain real but not bleeding. | "We know the bottom sellers, we just haven't acted." |
| Reservations / booking | ~3% of dine-in covers = no-shows or walk-aways. Pain real but small in absolute SGD. | "It's annoying but it's not what's killing the P&L." |
| Drive-thru / counter ordering | N/A — no drive-thru in this format. | — |

**Output of Role 1 — ranked value pools (annualized group-wide):**

1. Food prep / inventory waste: ~SGD 3.2M/year
2. Labor scheduling over-spend + manager time: ~SGD 1.6M/year
3. Complaint triage delay (reputation + ~1.5 FTE): ~SGD 150K/year direct, undefined reputational
4. Menu engineering: ~SGD 400K/year (estimated)
5. No-shows on reservations: ~SGD 90K/year

The booking-chatbot pitch is now in 5th place by value. The director's face changes.

### Role 2 — Capability Archetype Classifier

For each top value pool, we ask: what is the friction shape, and which capability archetype matches? We use Andrew Ng's "one-second rule" (does this task involve a judgment a human could make in roughly a second, repeated at high volume?) and the Stanford 51-deployments archetype set (chatbot, RAG, workflow automation, agent, prediction model).

| Value pool | Friction shape | Andrew Ng one-second test | Archetype | Notes |
|---|---|---|---|---|
| Prep / inventory waste | Predict tomorrow's covers and item-mix per store, per daypart. Tabular, repeatable, decision happens once per day. | No — humans cannot do this in a second; this is a forecasting task, not a perception task. | **Prediction model / workflow** (classic ML, not LLM) | Closest to demand forecasting in retail. Boring, well-trodden. |
| Labor scheduling | Optimization given forecasted covers + labor rules + staff preferences. | No — combinatorial, not perception. | **Optimization + workflow**, optionally LLM as the manager-facing UI | Depends on Role 1 forecast as input. |
| Complaint triage | Classify, route, draft response. Sentiment + topic + urgency on free text. | Yes — a human reads a complaint in seconds and decides "refund / apologize / escalate." | **LLM workflow (classify + draft)**, possibly RAG over past resolutions | Good archetype-friction fit. |
| Menu engineering | Analytical task done quarterly. Already partly solved with off-the-shelf POS analytics. | No — this is BI, not AI. | **BI / analytics** (no AI needed) | Mis-pitched as AI. |
| Reservation booking chatbot | Conversational front-end over a calendar. | Yes one-second test, but volume is low and Chope/Google already do this. | **Chatbot over an existing API** | Capability fit OK, value pool small, vendor competition heavy. |

**Insight surfaced for the director:** The two biggest pools (prep, scheduling) are not LLM problems at all — they are forecasting and optimization. The LLM-shaped problem is complaint triage, which is mid-sized. The chatbot pitch is a real archetype but pointed at a tiny pool. Menu engineering is not even an AI problem.

### Role 3 — Feasibility & Moat Scorer

For each candidate, we score 0–3 on four dimensions: data readiness, technical feasibility, organizational readiness, and moat (per Andrew Ng's three-moat framing: proprietary data, distribution / workflow lock-in, or a regulatory / domain-trust position). We then weight using BCG's 10/20/70 (10% algorithm, 20% tech / data plumbing, 70% people-and-process).

Scoring (0 = blocker, 3 = strong):

| Candidate | Data readiness | Tech feasibility | Org readiness | Moat | 10/20/70-weighted notes |
|---|---|---|---|---|---|
| **Demand-forecast for prep** | 2 — 2 yrs POS exists, needs ETL and weather/holiday joins, doable in weeks | 3 — classical forecasting, mature toolkit (Prophet, lightGBM, even POS-vendor add-ons) | 2 — chefs and store managers must trust and act on the number; change-management heavy (the 70%) | 2 — proprietary item-mix data per store is genuinely yours over time | The 70% (manager adoption) is the real risk, not the model. |
| **Schedule optimization** | 1 — labor data is in WhatsApp; needs to be digitized first | 2 — solver tech is mature, but depends on forecast as input | 1 — managers will resist losing scheduling autonomy; union / MOM rules in SG add complexity | 1 — workflow lock-in possible once adopted | Blocked by Role-1 forecast and by data plumbing. Sequence after, not first. |
| **Complaint triage (LLM)** | 2 — text data exists across Grab/foodpanda/Google but scattered; aggregator API access varies | 3 — off-the-shelf LLM classify+draft is a solved pattern | 2 — HQ team of 1.5 FTE wants the help; low political resistance | 1 — generic LLM behind it; data moat is thin (volumes too low to fine-tune meaningfully) | Good archetype fit, modest moat, fast to ship. |
| **Menu engineering** | 3 — POS data sufficient | 3 — a BI dashboard would do it; "AI" is a misnomer | 2 — chef has opinions, will need to be a co-author | 0 — no moat; everyone with a POS can do this | Should be done; should not be called AI; do not eat budget that should go to forecasting. |
| **Booking chatbot** | 2 — Chope/Google data accessible | 3 — vendors will sell this turnkey | 2 — low resistance | 0 — Chope/Google/OpenTable already own the distribution; you cannot build a moat here | Buy, do not build. Not a strategic AI pilot. |

### Role 4 — Portfolio Sequencer

We plot value (Role 1) against feasibility-adjusted-for-moat (Role 3). Heatmap, then apply pilot-discipline (Andrew Ng): the first pilot must be **narrow, reversible, and measurable** within ~6 months.

| | Low feasibility | Mid feasibility | High feasibility |
|---|---|---|---|
| **High value (>SGD 1M/yr)** | Schedule-opt (blocked on data + change-mgmt) | **Prep demand-forecast** | — |
| **Mid value (SGD 100K–1M/yr)** | — | Complaint triage | Menu engineering (but not AI) |
| **Low value (<SGD 100K/yr)** | — | — | Booking chatbot (buy, do not build) |

**First-pilot screen against pilot-discipline-ng:**

- **Narrow?** Yes if scoped to *one daypart × one item category × 2 stores*. (E.g. lunch service, rice-bowl SKUs, two flagship stores.)
- **Reversible?** Yes — prep decisions are made daily; if the forecast is bad, managers fall back to gut feel the next day. No customer-facing risk.
- **Measurable?** Yes — primary metric: food waste SGD per cover, measured weekly vs same-store same-week last year. Secondary: stockout rate.

**Pilot pick:** Demand-forecast-for-prep, 2 stores, lunch daypart, rice-bowl + noodle SKUs, 12 weeks. Target: 20% waste reduction on the in-scope SKUs.

## Synthesis

```
TOP-3 RANKED USE CASES
1. Prep demand-forecast (per-store, per-daypart, per-SKU). Value pool ~SGD 3.2M/yr group-wide.
   Verdict: Greenlight as first pilot.
2. Complaint triage (LLM classify + draft + route over Grab / foodpanda / Google reviews / in-store cards).
   Value pool ~SGD 150K/yr direct + reputational.
   Verdict: Stage-and-watch — start in parallel as a thin slice (one channel: Google reviews) once forecast pilot is in flight.
3. Schedule optimization (uses forecast output as input).
   Value pool ~SGD 1.6M/yr.
   Verdict: Park until forecast pilot proves out and labor data is digitized. Sequence Q3.

FIRST PILOT
Demand-forecast-for-prep. Scope: 2 flagship stores × lunch daypart × rice-bowl + noodle SKUs.
Duration: 12 weeks. Primary KPI: SGD waste per cover vs same-store same-week prior year.
Target: -20% on in-scope SKUs. Reversibility: daily; managers retain override.
Owner: Group Head Chef + IT Manager. External help: 1 contracted ML engineer for 8 weeks.

WHY-NOT-OTHERS
- Menu engineering: not an AI problem, it is a BI problem. Fix with a dashboard and a quarterly chef review. Do not let it eat the AI budget or the AI narrative.
- Booking chatbot: small value pool (~SGD 90K/yr), no moat, Chope and Google already own this distribution. Buy a vendor feature if needed; do not build, do not call it your AI pilot.
- Schedule optimization: blocked by missing labor data (WhatsApp rosters) and high change-management cost. Cannot be narrow, reversible, and measurable in 6 months without forecast already live.

KILL LIST
- Booking chatbot as a strategic AI initiative. Reclassify as a vendor-buy decision under IT.
- "AI menu optimization" as a pitched workstream. Reclassify as quarterly BI + chef review.
- Any drive-thru ASR conversation in this format (no drive-thru exists). Park entirely.

VERDICT: Greenlight (prep demand-forecast). Stage-and-watch (complaint triage). Park (schedule-opt). Reject (booking chatbot as AI pilot, menu-AI as AI pilot).
```

## Why This Matters

The director arrived with the two use cases that dominate restaurant-tech press: menu optimization and chatbots. Both are real things that real chains do. Neither is where his P&L is bleeding. Within 90 minutes of value-pool mapping, the conversation moved from "what is AI good at?" to "where is my dollar pain, and which of those pains is AI-shaped?" That is the entire point of leading with Role 1 instead of Role 2.

The second lesson is archetype-fit. Two of his three real pains — prep forecasting and labor scheduling — are not LLM problems. They are classical ML and operations-research problems with twenty-year-old toolkits. If he had hired an "AI consultant" who only talked LLMs, he would have shipped a chatbot and missed the SGD 3.2M/yr waste pool entirely. Andrew Ng's one-second rule was the cleanest disqualifier for the chatbot framing: forecasting tomorrow's covers is not a thing a human does in one second, and so it is not a thing a one-second-rule LLM should be solving on its own.

The third lesson is sequencing discipline. Schedule-optimization is the most strategically interesting pool and the one a tech-first leader would jump to first. It is also the one that fails the narrow-reversible-measurable test today: labor data is in WhatsApp, manager adoption risk is high, and it depends on a forecast that does not yet exist. Putting it first would have produced a 12-month project with a high probability of stalling. Putting it third — gated on the forecast pilot succeeding — turns it into an earned next move.

## Sources

- McKinsey value-pool framing — [The state of AI: How organizations are rewiring to capture value, McKinsey Global Survey, 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- Andrew Ng "one-second rule" — [AI Transformation Playbook, Landing AI](https://landing.ai/wp-content/uploads/2020/05/LandingAI_Transformation_Playbook_11-19.pdf)
- Andrew Ng on the three moats and pilot discipline — [Stanford CS229 / DeepLearning.AI talks; "AI is the new electricity"](https://www.deeplearning.ai/the-batch/)
- Stanford 51-deployments archetype set — [Stanford HAI AI Index 2024, enterprise deployment patterns](https://aiindex.stanford.edu/report/)
- BCG 10/20/70 effort weighting — [BCG, "AI doesn't transform organizations. People do," 2024](https://www.bcg.com/publications/2024/the-ai-only-strategy-wont-work)
- Pilot discipline (narrow / reversible / measurable) — internal skill `pilot-discipline-ng` in this kit; primary source: Andrew Ng, "Concrete steps to get started with AI," 2018.
- Restaurant food-waste benchmarks (~30% target food cost, ~5–10% recoverable through better prep) — [Toast Restaurant Industry Report, 2024](https://pos.toasttab.com/resources/restaurant-industry-report)
- Aggregator review-volume realities (Grab, foodpanda, Google) — participant survey r02, June 2026.
