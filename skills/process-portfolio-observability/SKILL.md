---
name: process-portfolio-observability
description: Use when an enterprise has shipped AI agents but cannot see usage, cost, or ROI at the portfolio level. Phrases like "we deployed agents but can't see them", "unclear ROI on our AI", "token spend is exploding", "governance dashboard for AI", "how do we track agent performance", "what's the net ROI after oversight" all trigger this skill. Builds a three-layer KPI tree, dashboard spec, and review cadence that subtracts human-oversight cost from gross gains — outputs a portfolio observability blueprint with sunset criteria and an Observable-and-governed / Partial-observability / Black-box verdict.
---

# Process — AI Portfolio Observability

Most enterprises run AI like a black box: they ship agents, they pay tokens, they cannot answer "what did this earn us net of oversight?" PwC's 2026 ROI guidance is explicit — *gross* productivity is not the number; **net-of-oversight ROI** is. The european fintech case shows the trap: 40% deflection headline, 22% CSAT drop, net value negative. This skill builds the instrumentation that exposes that math before the board does.

Anchor: PwC three-channel ROI (efficiency + growth + revenue) minus oversight cost; IMDA Dimension 4 structural controls; NIST RMF MANAGE function on continuous monitoring; 70/20/10 *portfolio mix* prior (70% core / 20% adjacent / 10% transformational — not to be confused with BCG's 10/20/70 *effort split* used in `general-use-case-discovery` and `general-peer-cases`, or `people-literacy-curriculum`'s 70-20-10 *training-budget* split).

## Dimension 1: KPI Tree Construction

Every initiative gets three connected layers. If any layer is missing, the agent is unobservable by definition.

1. **Input KPIs — what is consumed?** (Usage volume, p50/p95 latency, tokens per call, token cost per call, infra spend, human-in-the-loop minutes per call.)
2. **Output KPIs — what does the agent produce?** (Task-completion rate, override/correction rate, hard-error rate, hallucination rate on golden set, CSAT or NPS delta, escalation rate to human.)
3. **Outcome KPIs — what does the business get?** (Hours saved per week, revenue lift, cycle-time drop, defect rate drop, headcount reallocated — tied to a P&L line.)

The tree must *connect*: input dollars → output behavior → outcome dollars. If "hours saved" cannot be traced to a specific output KPI driving it, the number is fiction. *Consult `pwc-20-item-checklist.md`: items 11–16 cover the input/output/outcome wiring expected by audit.*

Output:
INPUT_KPIS | OUTPUT_KPIS | OUTCOME_KPIS | TREE_CONNECTIVITY | P&L_LINE_OWNER

## Dimension 2: Oversight-Cost Subtraction

Gross ROI is marketing. Net-of-oversight ROI is the only honest number. PwC's 2026 framing breaks value into three channels — efficiency, growth, revenue — and demands explicit subtraction of:

1. **Human review hours.** (Every output a human checks before it ships costs the loaded hourly rate.)
2. **Rework hours.** (Override rate × time-to-correct × volume. A 15% override rate on 10k calls/week at 6 minutes each is 150 person-hours/week — one full FTE.)
3. **Escalation hours.** (Tier-2 specialist time triggered by agent confusion. Track minutes per escalation, not just count.)
4. **Incident & remediation hours.** (Post-mortem time when the agent ships something wrong — the european fintech CSAT-22% miss is the canonical case: 40% deflection looked like a win until churn signals surfaced three months later.)

Net ROI = (efficiency $ + growth $ + revenue $) − (review + rework + escalation + incident $). *Consult `pwc-roi-2026-governance.md`: net-of-oversight is now the disclosure-grade number; gross is no longer defensible.* *Consult `european-fintech-case.md`: how a "winning" deployment posted negative net value once oversight cost was included.*

Output:
GROSS_VALUE | OVERSIGHT_COST | REWORK_COST | ESCALATION_COST | NET_ROI | DELTA_VS_CLAIMED

## Dimension 3: Dashboard Architecture

Three views, one source of truth. If your stack cannot produce all three, you have partial observability — treat it as Critical-Gap.

1. **Per-agent view.** (Live tile: usage, token spend run-rate, override rate, CSAT, latency, error rate. Token-cost guardrail per agent — hard cap with auto-throttle, not a slack alert. IMDA structural control: bounded tool access, bounded budget, kill-switch.)
2. **Per-portfolio view.** (All agents on one page, ranked by net ROI. 70/20/10 lens overlay — are core/adjacent/transformational bets in the right ratio? Red/amber/green on net-ROI threshold.)
3. **Per-business-unit view.** (Roll up by BU owner, accountable exec named on the tile. Cost charged back to the BU's P&L line — no ambiguity about who pays for tokens.)

Logging requirement (NIST RMF MANAGE): every prompt, every tool call, every output, every override — retained per data-retention policy, queryable for incident response. *Consult `nist-rmf-functions.md`: MANAGE function specifies continuous monitoring and incident-response logging as non-optional.* *Consult `imda-4-dimensions-agentic.md`: Dimension 4 structural controls map directly to dashboard alert thresholds.*

Alert thresholds (defaults — tune per agent):
- Token spend > 120% of weekly budget → throttle.
- Override rate > 20% week-over-week → freeze new deployment.
- CSAT delta < −5pp vs baseline → mandatory review.
- p95 latency > SLO for 3 consecutive days → escalate.

Output:
PER_AGENT_VIEW | PER_PORTFOLIO_VIEW | PER_BU_VIEW | LOGGING_DEPTH | ALERT_THRESHOLDS | KILL_SWITCH

## Dimension 4: Review Cadence

Dashboards no one reads are theater. Cadence and accountability convert telemetry into decisions.

1. **Weekly ops review (60 min).** (Owner: agent product manager. Reviewed: per-agent KPIs, override rate spikes, token-budget burn, incident log. Trigger: any red threshold → throttle or rollback by Friday.)
2. **Monthly portfolio review (90 min).** (Owner: AI CoE lead + finance partner. Reviewed: net ROI by initiative, 70/20/10 mix drift, redeployment of capacity from sunset agents. Trigger: bottom-quartile agents enter "improve-or-sunset" 30-day clock.)
3. **Quarterly board review (45 min).** (Owner: CIO/CDAO + CFO. Reviewed: portfolio net ROI vs business case, regulatory exposure, MIT-CISR stage progression, capital reallocation. Trigger: portfolio-level net ROI miss > 25% → strategy reset.)
4. **Sunset criteria — written, not negotiated in the room.** (Net ROI negative for 2 consecutive months OR override rate > 30% sustained OR CSAT regression unrecovered after one fix cycle → archive. No agent gets sentimentality budget.)

*Consult `mit-cisr-4-stages.md`: cadence intensity scales with stage — Stage 2 weekly, Stage 4 can move to bi-weekly ops.* *Consult `70-20-10-value-split.md`: monthly review explicitly checks portfolio mix against the 70/20/10 prior, not just individual ROI.*

Output:
WEEKLY_AGENDA | MONTHLY_AGENDA | QUARTERLY_AGENDA | OWNERS | ESCALATION_TRIGGERS | SUNSET_RULE

## Synthesis

Produce the four artifacts. Assign one of three states:

- **Observable-and-governed.** All four dimensions in place, net-ROI tracked, sunset rule written, board sees the same numbers ops sees. Continue to scale.
- **Partial-observability.** KPI tree exists but oversight cost not subtracted, OR dashboard exists but cadence is ad-hoc, OR sunset rule is informal. 30-day remediation plan, named owner, no new agent launches until closed.
- **Black-box.** Two or more dimensions missing. Token spend is unbounded, ROI is gross-only, no portfolio view. Freeze new deployments. Stand up Dim 1 + Dim 3 within 60 days before resuming launches.

Output:
KPI_TREE | DASHBOARD_SPEC | REVIEW_CADENCE | SUNSET_CRITERIA | STATE: Observable-and-governed | Partial-observability | Black-box

## References

- `pwc-roi-2026-governance.md` — net-of-oversight ROI as the disclosure-grade number; gross ROI no longer defensible.
- `pwc-20-item-checklist.md` — 20-item governance audit; items 11–16 cover input/output/outcome KPI wiring.
- `imda-4-dimensions-agentic.md` — Dimension 4 structural controls (bounded tools, bounded budget, kill-switch) maps to dashboard guardrails.
- `nist-rmf-functions.md` — MANAGE function: continuous monitoring and incident logging are non-optional.
- `european-fintech-case.md` — 40% deflection / −22% CSAT case; gross win, net loss, three-month lag to detection.
- `70-20-10-value-split.md` — portfolio mix prior used in the monthly review overlay.
- `mit-cisr-4-stages.md` — cadence intensity calibration by enterprise AI maturity stage.

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
