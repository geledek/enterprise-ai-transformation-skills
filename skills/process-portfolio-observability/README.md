# Process — AI Portfolio Observability

Builds the KPI tree, dashboard spec, review cadence, and sunset rule that expose net-of-oversight ROI.

## What it does

1. Constructs a three-layer KPI tree per agent — Input KPIs (usage, tokens, latency, HITL minutes) → Output KPIs (completion, override, hallucination, CSAT delta) → Outcome KPIs (hours, revenue, cycle time) tied to a P&L line
2. Subtracts oversight cost from gross gains — review hours, rework hours, escalation hours, and incident hours, producing a Net ROI = (efficiency + growth + revenue) − (review + rework + escalation + incident)
3. Specifies a three-view dashboard architecture (per-agent, per-portfolio with 70/20/10 overlay, per-BU with charged-back P&L) and named alert thresholds with kill-switch
4. Defines weekly / monthly / quarterly review cadence with named owners and a written sunset rule (net ROI negative for 2 months OR override > 30% sustained → archive)
5. Issues an Observable-and-governed / Partial-observability / Black-box verdict and a remediation sequence

## When to use it

When agents are in production but ROI is invisible. Trigger phrases: "we deployed agents but can't see them", "unclear ROI on our AI", "token spend is exploding", "governance dashboard for AI", "what's the net ROI after oversight". Use before a board AI briefing, after a CFO ROI challenge, or when token spend has materially outpaced the original business case.

## What it outputs

- Three-layer KPI tree per agent with TREE_CONNECTIVITY check and named P&L_LINE_OWNER
- Net ROI table: GROSS_VALUE | OVERSIGHT_COST | REWORK_COST | ESCALATION_COST | NET_ROI | DELTA_VS_CLAIMED
- Dashboard spec with per-agent, per-portfolio, per-BU views; alert thresholds; kill-switch placement
- Review-cadence pack: weekly/monthly/quarterly agendas, owners, escalation triggers, written sunset rule
- Verdict: Observable-and-governed | Partial-observability | Black-box, with a sequenced remediation plan
- 70/20/10 portfolio mix overlay flagging core/adjacent/transformational drift

## Example

**Scenario:** Henrik Bjornsson, CDO of Nordfrakt Logistics — a Nordic 3PL (EUR 620M revenue, ~2,800 staff, 14 DCs across Sweden/Norway/Denmark/Finland). Over 14 months his AI Centre has shipped 11 production agents (customs drafter, load planner, three multilingual support copilots, freight pricer, invoice reconciliation, shift roster, three internal knowledge bots), each green-lit by individual BU heads. Azure OpenAI spend has tripled to EUR 95K/month. The CFO wants a Net ROI answer 11 weeks before the September board.

**User prompt:**

> I'm in a bit of a corner. We're a Nordic logistics group, ~EUR 620M revenue, and over the last 14 months my team has put 11 AI agents into production — customs paperwork, load planning, three multilingual support copilots, freight pricing, invoice reconciliation, shift rostering, and three internal knowledge bots. Each was green-lit individually by different BU heads with their own business cases. My CFO is asking before the September board: what are these things actually earning us? Our Azure OpenAI bill went from ~EUR 30K to EUR 95K a month in two quarters. Each team swears their agent is "saving hours" but I cannot reconcile that to anything in the P&L, and our support team has quietly added two QA reviewers to babysit the copilots. How do I get my arms around this before the board meeting in 11 weeks?

**Skill output (excerpt):**

```
VERDICT: Black-box (3 of 4 dimensions missing).
Freeze new launches. Stand up Dim 1 + Dim 3 within 60 days.

KPI TREE (sample — customs drafter)
  INPUT   : 14.2K calls/wk · p95 4.1s · 8.2K tokens/call · EUR 0.41/call · 6 HITL min/call
  OUTPUT  : 78% completion · 19% override · 4.1% hard error · CSAT +2pp
  OUTCOME : 410 hrs/wk saved · EUR 38K/mo gross · P&L line: Customs Ops (owner: M. Lind)
  CONNECT : OK — overrides traced to free-text HS-code field

NET ROI TABLE (illustrative, monthly, EUR)
  Agent              | Gross | Review | Rework | Esc | Incident | Net    | Δ claim
  customs drafter    | 38K   |  6K    |  9K    | 2K  |   0      | +21K   | −45%
  load planner       | 22K   |  3K    |  4K    | 1K  |   0      | +14K   | −30%
  support EN         | 41K   | 14K    | 18K    | 6K  |   3K     |   0K   | −100%
  support DE         | 28K   | 11K    | 14K    | 4K  |   2K     |  −3K   | NEG
  support SV         | 31K   | 10K    | 12K    | 4K  |   1K     |  +4K   | −85%
  freight pricing    | 18K   |  2K    |  3K    | 1K  |   0      | +12K   | −22%
  invoice recon      | 24K   |  3K    |  4K    | 1K  |   0      | +16K   | −15%
  shift roster       |  9K   |  1K    |  2K    | 0   |   0      |  +6K   | −33%
  knowledge × 3      | 12K   |  4K    |  3K    | 1K  |   0      |  +4K   | −67%
  PORTFOLIO TOTAL    | 223K  | 54K    | 69K    | 20K |   6K     | +74K   | −67%

DASHBOARD SPEC
  Per-agent  : usage, token-spend run-rate, override %, CSAT, p95, error %
               token-cap auto-throttle (not Slack alert), kill-switch
  Per-portf. : ranked by Net ROI; 70/20/10 mix overlay (current: 91/9/0 — drift)
  Per-BU     : charged back to BU P&L; named accountable exec on tile
  Logging    : every prompt/tool-call/output/override (NIST RMF MANAGE)

ALERTS — token > 120% wk budget → throttle · override > 20% wow → freeze
         CSAT Δ < −5pp → mandatory review · p95 > SLO 3 days → escalate

CADENCE
  Weekly 60' — Agent PM · per-agent KPIs, override spikes, incident log
  Monthly 90' — CoE lead + Finance · Net ROI, 70/20/10 drift, sunset clock
  Quarterly 45' — CIO/CDAO + CFO · portfolio Net ROI vs case, capital realloc

SUNSET RULE (written): Net ROI < 0 for 2 consecutive months
  OR override > 30% sustained
  OR CSAT regression unrecovered after one fix cycle → archive.

11-WEEK PLAN
  Wk 1–2  KPI tree per agent · finance co-owner named per BU
  Wk 3–5  Dashboard v1 (per-agent + per-portfolio) · token caps live
  Wk 6–7  Net ROI run with oversight subtraction · sunset clock starts on 4 agents
  Wk 8–9  Per-BU view + chargeback · cadence calendar published
  Wk 10–11 Board pack: Net ROI table, verdict, sunset list, 70/20/10 reset
```

**How to read this output:**

- Start with the verdict (Black-box / Partial / Observable-and-governed) — it dictates whether new launches are frozen
- The Net ROI table is the load-bearing artifact for the CFO; the Δ vs claim column is what destroys the "saving hours" narrative
- Check that every Outcome KPI is wired to a P&L line with a named owner — if not, the savings are fiction
- 70/20/10 drift (here 91/9/0) is the portfolio signal that explains why innovation pipeline is empty
- Push back if the sunset rule is missing thresholds, if oversight cost is not subtracted, or if the dashboard cannot produce all three views

## Sources used

- `pwc-roi-2026-governance.md` — net-of-oversight ROI as the disclosure-grade number; gross ROI no longer defensible
- `pwc-20-item-checklist.md` — 20-item governance audit; items 11–16 cover input/output/outcome KPI wiring
- `imda-4-dimensions-agentic.md` — Dimension 4 structural controls (bounded tools, bounded budget, kill-switch)
- `nist-rmf-functions.md` — MANAGE function: continuous monitoring and incident logging are non-optional
- `european-fintech-case.md` — 40% deflection / −22% CSAT case; gross win, net loss, three-month detection lag
- `70-20-10-value-split.md` — portfolio mix prior used in the monthly review overlay
- `mit-cisr-4-stages.md` — cadence intensity calibration by enterprise AI maturity stage

## Effectiveness

Effectiveness test (2026-06-12): scored 24.67/25 (Grade B, +4.67 lift over the strongest baseline of vanilla LLM and kb-ask retrieval). 3-judge unanimous verdict.

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
