---
case: enterprise-it-consulting-r16
persona: Enterprise Account Executive, global IT services & consulting firm
client: 25,000-person regional bank (APAC)
skill: process-portfolio-observability
date: 2026-06-11
---

> One-line summary: An EAE at a global IT services firm runs the process-portfolio-observability skill on a regional bank's 20-initiative AI portfolio (14 in prod, 6 in pilot) where token spend is $180k/month with zero per-agent attribution and the audit team is escalating. End-state: KPI tree across 3 layers, net-of-oversight ROI, per-agent / per-BU / per-portfolio dashboard, weekly/monthly/quarterly cadence, 3 sunset triggers.

# Portfolio Observability for a Regional Bank's 20-Agent Estate

## Persona / Setup

**Practitioner.** Karthik Subramanian, Enterprise Account Executive at a global IT services & consulting firm. He owns the bank account across advisory, build, and run. Survey response (r17) verbatim:

> "Observability and governance. Organization don't have a view how the agent perform and ROI of each agent. They could limit some Agent to prevent unpredictable token consumption."

**Client.** A 25,000-person regional bank, APAC-headquartered, MAS-regulated (Singapore subsidiary), with branches across SG / MY / ID / VN. Tier-1 capital ratio 14.8%. Cost-to-income 43%. Mid-tier on AI maturity — past the hype phase, deep in production scaling pain.

**The portfolio.**
- 14 AI initiatives in production
- 6 in active pilot
- Spread across 5 business units: Retail Banking, SME Lending, Wealth, Operations (back-office), Risk & Compliance
- Models: GPT-4o (Azure), Claude 3.5 Sonnet (AWS Bedrock), in-house fine-tuned BERT for KYC, plus 3 Copilot-style integrations
- Token spend: ~$180k/month, billed to a single shared cost centre. No per-initiative attribution. No tagging discipline.
- Build teams: 4 internal squads + Karthik's firm (~22 consultants on-site)

**Trigger event.** Internal Audit issued a yellow-flag finding two weeks ago: "Cannot demonstrate proportionate oversight of generative AI workloads in scope of MAS FEAT principles. No portfolio-level KPI reporting exists." The CRO is now asking the CIO for a portfolio dashboard before the September board meeting. Karthik has 90 days.

**What's already broken.**
- The credit-memo drafter (SME Lending) is "loved by RMs" anecdotally — no measured productivity number
- The customer-service triage agent (Retail Banking) had a CSAT regression in March that nobody caught for 6 weeks
- Two pilots are still running with no kill criteria after 11 months
- One agent's token bill spiked 4x in April after a prompt change; finance noticed before the build team did

## Applying process-portfolio-observability

Karthik runs the skill across two workshop days with the bank's Head of Enterprise Architecture (Mei Lin), the AI CoE lead (Arjun), and the CFO's BP (Sandra). Everything below comes out of those two days.

### Dimension 1 — KPI Tree Construction

The skill demands three connected layers per initiative: **input KPIs → output KPIs → outcome KPIs**. Karthik insists on the connection: outcome KPIs without traceable inputs are vanity metrics; input KPIs without outcome linkage are infrastructure telemetry, not business performance.

**Portfolio-wide KPI tree shape (applied to all 20 initiatives):**

| Layer | KPI category | Examples | Owner |
|---|---|---|---|
| Input | Usage | DAU, sessions/day, prompts/user/day | Product owner |
| Input | Latency | p50, p95, p99 response time | Platform engineering |
| Input | Token cost | $/session, $/user/month, total $/month | FinOps + product owner |
| Output | Task completion | % tasks completed without human takeover | Product owner |
| Output | Override rate | % AI outputs edited/rejected by human | Business unit lead |
| Output | Error rate | hallucination flags, factual errors caught in QA | Risk + QA |
| Output | CSAT | NPS, thumbs-up rate, complaint volume | Business unit lead |
| Outcome | Hours saved | FTE equivalent, cycle-time delta | BU + Finance |
| Outcome | Revenue lift | conversion delta, deal-size delta, retention | BU + Finance |
| Outcome | Defect drop | rework rate, audit findings, error cost | Risk + Operations |

**Worked example A — Credit-Memo Drafter (SME Lending).**

- *Input.* 47 RMs use it daily. ~12 memos/RM/week. p95 latency 8.2s. Token cost: $14,200/month (~$0.89 per memo at average 16k input + 4k output tokens).
- *Output.* Task completion 71% (RM accepts draft with <20% edits). Override rate 29%. Error rate 4.1% (factual errors caught in 4-eye review — 2 of these would have hit the credit committee uncorrected). CSAT from RMs: 4.2/5.
- *Outcome.* Cycle time per memo 4.5h → 1.8h. Hours saved: 47 RMs × 12 memos × 2.7h × 4 weeks = ~6,090 hours/month gross. Revenue lift: deal velocity up 18%, attributable revenue lift ~$2.1M/quarter (econometric estimate, Sandra's team). Defect drop: not yet measured — credit-committee rejection rate flat.

The connection holds: inputs (usage × token cost) → outputs (completion rate × override rate) → outcomes (hours saved × cycle time). When override spiked in week 9, outcome dropped within 2 weeks. Causal chain visible.

**Worked example B — Customer-Service Triage Agent (Retail Banking).**

- *Input.* 11,000 customer chats/day routed through the agent. p95 latency 3.1s. Token cost: $38,400/month (highest of any agent — driven by long context windows on customer history).
- *Output.* Task completion 64% (resolved without human handoff). Override/handoff rate 36%. Error rate 2.8% (compliance-flagged responses). **CSAT 71%, down from 82% pre-launch — the regression nobody caught for 6 weeks.**
- *Outcome.* Hours saved: ~340 agent-FTE-equivalent hours/day. Revenue impact: -$420k Q1 attributable to CSAT-driven churn (Sandra's churn model). **Net outcome NEGATIVE for Q1 once the CSAT miss was monetised.**

This is exactly the european-fintech-case pattern referenced in the skill: cost saved, CSAT lost, net value destroyed. The skill flags this and Karthik makes it the centrepiece of the CRO presentation.

**Across the other 18 initiatives.** Karthik's team builds the same 3-layer table for each. 5 of 14 prod initiatives have NO outcome-layer measurement at all — pure activity reporting. 3 of 6 pilots have no output-layer measurement either. These get tagged "Black-box" in the synthesis.

### Dimension 2 — Oversight-Cost Subtraction

The skill is explicit: **net-of-oversight ROI is the only honest number.** It pulls the PwC three-channel frame (efficiency + growth + revenue) and subtracts (a) human oversight hours, (b) rework hours, (c) escalation hours. The skill flags the european-fintech case: a 22-point CSAT miss erased the cost saving.

Karthik runs the calculation across the portfolio. Initial gross-claim numbers from BU leads:

| Channel | Gross claim | Source |
|---|---|---|
| Efficiency (hours saved) | $14.2M annualised | BU productivity reports |
| Growth (deal velocity, conversion) | $8.4M annualised | Sandra's revenue attribution |
| Revenue (new product enabled) | $2.1M annualised | Wealth advisory upsell |
| **Gross total** | **$24.7M** | |

Then the subtractions, line by line, agent by agent. Karthik's team pulls timesheet data from the build squads and the QA team:

| Oversight cost | Detail | Annualised |
|---|---|---|
| Human review hours | 4-eye on credit-memo (mandatory), compliance review on triage outputs, RM sign-off | $3.8M |
| Rework hours | Editing AI drafts, re-running prompts, fixing hallucinations downstream | $2.6M |
| Escalation hours | Risk committee reviews, audit responses, incident handling (incl. April token spike) | $1.4M |
| **CSAT miss monetised** (triage agent regression) | $420k Q1 × 4 (annualised before fix) | $1.7M |
| **Total oversight + miss** | | **$9.5M** |

**Net-of-oversight ROI: $15.2M annualised, not $24.7M.** The gross number was 62% inflated. Sandra's reaction in the workshop: "We've been showing the board the wrong number for two quarters."

The skill flags two further structural issues:
1. The CSAT miss on the triage agent is a structural recurrence of the european-fintech pattern. Without per-agent CSAT instrumentation tied to revenue impact, this WILL happen again on another agent.
2. Oversight cost is currently buried in BU operating budgets. It looks like normal BAU work. The skill insists this be broken out and visible per-agent — otherwise leadership will keep approving agents that destroy net value.

### Dimension 3 — Dashboard Architecture

The skill specifies three view tiers: **per-agent, per-business-unit, per-portfolio.** Plus alert thresholds, token-cost guardrails (IMDA structural controls), and logging discipline (NIST AI RMF MANAGE function).

**Per-agent view.** One page per initiative. Live tiles for each of the 9 KPIs in the tree (3 input + 4 output + 3 outcome where measurable). 30-day trend. Alert threshold per KPI:
- Token cost > 1.3x rolling 4-week average → amber. > 1.7x → red, auto-page FinOps.
- p95 latency > SLA × 1.2 → amber.
- Override rate WoW delta > 5pp → amber. > 10pp → red.
- CSAT WoW delta < -3pp → amber. < -5pp → red, freeze further rollout.
- Error rate above agent-specific threshold (set per risk classification) → red.

**Per-BU view.** Roll-up across all agents in that BU. Net-of-oversight ROI for the BU. Top-3 agents by value, bottom-3 by net-value-destroyed. Oversight cost as % of gross benefit (the "honesty ratio" — Karthik's term). Trend on aggregate token spend.

**Per-portfolio view.** All 20 agents on one screen, scored on a 2x2: net ROI (x) vs. risk classification (y). Quadrants: Scale / Sustain / Fix-or-kill / Sunset. Aggregate token spend vs. budget. Aggregate oversight ratio. Compliance status (MAS FEAT + NIST AI RMF mapping). Pipeline of agents in pilot with kill-by dates.

**Token-cost guardrails (per IMDA structural controls).**
- Hard per-agent monthly cap, set at 1.5x baseline. Breach → automatic throttle, build team paged.
- Per-user daily cap on consumer-facing agents. Breach → graceful degradation to template responses.
- Cost-attribution tagging mandatory at the API call layer. Every prompt tagged with agent_id + bu_id + user_id (hashed). No tag = no service. This is the change that makes the $180k/month spend actually attributable.
- Quarterly token-budget review at portfolio level, signed off by CFO BP.

**Logging requirement (NIST AI RMF MANAGE function — MANAGE-2.3, MANAGE-3.2, MANAGE-4.1).**
- Every prompt + completion logged with full metadata (agent, user-hash, timestamp, model version, token count, latency, override flag, output classification).
- 7-year retention for logs touching credit decisions or KYC, per MAS guidelines.
- Quarterly log-quality audit by Internal Audit (closes the yellow-flag finding).
- Incident logs (every red-threshold breach) reviewed in monthly portfolio cadence.

The dashboard is built in the bank's existing Power BI estate, fed by a new event hub Karthik's firm provisions. 6-week build. 12-week to full instrumentation across all 20 agents.

### Dimension 4 — Review Cadence

The skill demands three cadences with explicit accountability and escalation triggers.

**Weekly ops review.** 30 minutes, Tuesday 9am.
- Attendees: AI CoE lead (Arjun), each agent product owner, platform engineering lead, FinOps analyst.
- Reviews: red/amber alerts from past 7 days, token spend vs. cap per agent, latency SLA breaches, override-rate deltas.
- Decisions: throttle / unfreeze / hotfix dispatch.
- Escalation trigger: any red unresolved 7+ days, or any agent breaching token cap 2 consecutive weeks → goes to monthly.

**Monthly portfolio review.** 90 minutes, first Wednesday.
- Attendees: CIO, CRO delegate, CFO BP (Sandra), AI CoE lead, BU heads (rotating), Karthik.
- Reviews: per-BU rollups, net-of-oversight ROI per agent, oversight-cost ratio trend, pipeline status (pilots), incident log.
- Decisions: agents moved between Scale / Sustain / Fix-or-kill / Sunset quadrants. Pilot extensions approved or denied. Budget reallocations.
- Escalation trigger: any agent in Fix-or-kill for 2 consecutive months OR net ROI negative 2 quarters running → goes to quarterly with sunset recommendation.

**Quarterly board review.** As part of the existing Risk & Tech board sub-committee.
- Attendees: board sub-committee, CEO, CIO, CRO, CFO, AI CoE lead.
- Reviews: portfolio-level net ROI vs. plan, compliance posture (MAS FEAT, NIST RMF), top wins, sunset decisions, capital ask for next quarter.
- Decisions: Sunset (kill) decisions formally ratified. Strategic portfolio rebalancing. Risk appetite adjustments.

**Sunset criteria (the skill insists these be pre-committed, not invented at kill-time).**
A pilot or production agent enters the sunset queue when ANY of:
1. Net-of-oversight ROI is negative for 2 consecutive quarters.
2. Override rate above 40% for 3 consecutive months (signals the human is doing the work anyway).
3. CSAT regression > 5 points sustained for 2 quarters with no recovery path.
4. Token cost exceeds gross benefit by >50% for 2 quarters.
5. Pilot has run >12 months without graduation criteria being met.

Two of the bank's current agents already trip criteria 1 and 5 the day the dashboard goes live. The triage agent trips criterion 3 retroactively. These are the first sunset/fix decisions for the September board.

## Synthesis

**KPI TREE + DASHBOARD SPEC + REVIEW CADENCE + SUNSET CRITERIA**

- **KPI Tree.** Three-layer tree (input → output → outcome) instantiated for all 20 agents. 9 KPIs per agent where fully measurable; 5 of 14 production agents and 3 of 6 pilots currently have no outcome-layer measurement and are tagged Black-box pending instrumentation. Two anchor examples: credit-memo drafter (net positive, $2.1M/qtr lift, 18% velocity gain, 71% completion) and customer-service triage (net negative Q1, -$420k attributable to 11-point CSAT regression — the european-fintech pattern recurring locally).

- **Dashboard Spec.** Three-tier (per-agent / per-BU / per-portfolio) Power BI build over an event-hub instrumentation layer. Token-cost guardrails per IMDA structural controls: hard per-agent monthly cap at 1.5x baseline, mandatory call-level tagging (agent_id + bu_id + user_hash), CFO-signed quarterly budget review. Logging per NIST AI RMF MANAGE-2.3 / 3.2 / 4.1: full prompt+completion capture, 7-year retention for credit/KYC, quarterly log-quality audit. Alert thresholds set on every input/output KPI with red/amber bands. 6-week build, 12-week to full coverage.

- **Review Cadence.** Weekly ops (30min, alerts + token spend + override deltas, throttle/hotfix decisions). Monthly portfolio (90min, CIO+CRO+CFO BP, net-of-oversight ROI per agent, quadrant moves, pilot extensions). Quarterly board (Risk & Tech sub-committee, formal sunset ratification, portfolio rebalancing). Pre-committed escalation triggers between cadences — no agent can hide for more than one cycle.

- **Sunset Criteria.** Five pre-committed kill triggers: negative net ROI (2 quarters), override rate >40% (3 months), CSAT regression >5pts sustained (2 quarters), token cost >150% of benefit (2 quarters), pilot >12 months unbroken. Three current agents already trigger one or more on day one of the dashboard.

- **Net-of-oversight ROI.** Gross claim $24.7M annualised. Oversight + rework + escalation + CSAT-miss subtractions $9.5M. **Honest number $15.2M.** The board has been seeing the gross number; the synthesis replaces it.

**State: Partial-observability** today (instrumentation gap on outcome layer for 8 of 20 agents, no per-agent attribution despite $180k/month spend). **Target state: Observable-and-governed** at week 12, with all four artefacts live and the audit yellow-flag closed.

## Why This Matters

The bank wasn't lying to itself out of malice. It was lying to itself out of structure: cost centre design that lumped $180k of token spend into a single bucket, BU productivity reports that counted hours saved without subtracting hours of oversight, a CSAT instrument that wasn't piped into the same dashboard as the agent KPIs, and a board cadence that received agent updates as one-off slides rather than a portfolio scoreboard. Every individual person was reporting honestly within their lens. The portfolio was opaque because no lens was set wide enough to see the tradeoffs.

Karthik's two-day workshop produced four artefacts that are individually unremarkable — a KPI tree, a dashboard spec, a cadence, a kill list. What's load-bearing is that they're connected: the tree feeds the dashboard, the dashboard surfaces the alerts, the alerts drive the cadence, the cadence ratifies the kills. Removing any one collapses the others. This is why the skill insists on producing all four, not three of four. Most banks Karthik has seen produce three of four and wonder why the discipline doesn't stick — usually the missing one is sunset criteria, because pre-committing kill rules feels career-limiting until the day the portfolio has 40 agents and nobody can name the bottom 10.

The european-fintech pattern (cost saved, CSAT lost, net value destroyed) showed up here as a 6-week-undetected regression on the triage agent. Once is anecdote. The skill argues — and Karthik's portfolio scan agrees — that without per-agent outcome instrumentation tied to a monthly cadence with pre-committed escalation, the same pattern WILL recur on another agent within 4 quarters. The dashboard isn't documentation; it's a forcing function. The cadence isn't ceremony; it's how the org notices what it would otherwise rationalise.

## Sources

- PwC. "AI Jobs Barometer 2025 — Three-channel productivity, growth, revenue framing." https://www.pwc.com/gx/en/issues/artificial-intelligence/ai-jobs-barometer.html
- IMDA / AI Verify Foundation. "Model AI Governance Framework for Generative AI." https://aiverifyfoundation.sg/resources/mgf-gen-ai/
- NIST. "AI Risk Management Framework (AI RMF 1.0) — MANAGE function." https://www.nist.gov/itl/ai-risk-management-framework
- Monetary Authority of Singapore. "FEAT Principles — Fairness, Ethics, Accountability, Transparency in AI use in finance." https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/FEAT
- Internal cross-reference: skills/process-portfolio-observability/cases/european-fintech-case.md (CSAT-22% miss pattern referenced in Dimension 2)
- Internal cross-reference: skills/general-idea-diagnostic/cases/klarna.md (precedent for net-of-oversight ROI pattern)
- Survey raw data, respondent r17, verbatim quote on observability and token consumption.
