---
name: roi-gate-pwc
description: Use when approving or rejecting an AI investment proposal, greenlighting an AI program for funding, evaluating whether an AI initiative should proceed to production, or reviewing an AI business case before board or executive sign-off. Phrases like "should we fund this AI project?", "run the ROI gate on this", "is this AI investment justified?", "we're about to approve AI spending for X", "help me evaluate this AI business case" all trigger this skill. Runs PwC's 20-item Do's-and-Don'ts checklist plus a three-channel ROI model and objective-mode audit. Outputs an approval recommendation with named conditions and red flags.
---

# AI Investment ROI Gate (PwC)

A pre-flight risk gate before greenlighting any AI investment. Runs PwC's 20-item checklist, a three-channel ROI model, and an objective-mode audit. An unanswered item is itself a red flag.

This skill gates *funding decisions* — after the idea has been assessed (use `ai-idea-diagnostic` for concept-stage gating) and after a pilot brief exists (use `pilot-design` for pilot structuring). This is the investment-approval gate.

---

## Role 1: Objective-Mode Audit

Before running the checklist, classify the investment against the three AI objective types (consult `mckinsey-3-objective-mix.md`):

- **Efficiency** — cost reduction, productivity, automation (80% of firms set this only)
- **Growth** — revenue uplift, new markets, customer acquisition
- **Innovation** — new products/services, business-model change

Ask:
1. Which objective does this investment serve?
2. Is this efficiency-only? If so: **1.6× leader-laggard gap** is the ceiling.
3. Does it add growth or innovation? If so: path to **2.6× gap** opens.

Flag efficiency-only investments explicitly. They are valid — but the value ceiling is structural.

Output:
OBJECTIVE TYPE | VALUE CEILING | FLAG IF EFFICIENCY-ONLY

---

## Role 2: Three-Channel ROI Model

Before running the 20-item gate, require a three-channel ROI structure (consult `accenture-redeployment-roi.md`):

| Channel | What it captures | Estimate |
|---|---|---|
| Revenue uplift | Incremental revenue from quality-driven volume/price | $X |
| Labor cost savings | Wage bill reduction for high-reallocation roles | $Y |
| Labor cost avoidance | Capacity freed for redeployment | $Z |

Ask for each channel:
- Revenue uplift: what is the quality-driven uplift hypothesis? How does AI quality improvement translate to volume or price?
- Labor cost savings: which specific roles? What is the headcount × wage × hours-saved calculation?
- Labor cost avoidance: what is the redeployment plan? "We'll figure it out" fails — reject if redeployment plan is absent.

**Accenture benchmark:** in a modeled $60B case, revenue uplift was ~5× labor savings. A single-line cost-takeout case under-states by ~4×.

If only one channel is presented: require the other two before proceeding.

Output:
REVENUE UPLIFT ESTIMATE | LABOR SAVINGS ESTIMATE | AVOIDANCE + REDEPLOYMENT PLAN | THREE-CHANNEL COMPLETENESS

---

## Role 3: PwC 20-Item Gate

Run all 20 items as a written checklist (consult `pwc-20-item-checklist.md` for the full list). Each item requires a one-paragraph answer. An unanswered item = red flag.

**The 10 Do's — confirm each is planned:**
1. Customer-centric approach (who is the end user? how is their experience measured?)
2. Thorough research on capabilities and limits (not just vendor demos)
3. Starting with small projects (is this pilot-first? 90-day scope?)
4. Performance monitoring + iteration plan (what is tracked? who reviews?)
5. Cross-functional team (IT, ops, finance, user-function all represented?)
6. Employee training (what training? mandatory or optional? timeline?)
7. Quality data (data pipeline ready? legal rights confirmed?)
8. Data security and privacy (GDPR, data classification, access controls confirmed?)
9. Scalable AI platform (can this scale beyond the pilot? how?)
10. Continuous learning (what is the post-deployment learning loop?)

**The 10 Don'ts — confirm each is addressed:**
1. Ignoring customer feedback (feedback collection mechanism named?)
2. **Underestimating complexity** — [CRITICAL] AI is not plug-and-play. What is the realistic complexity estimate?
3. Rushing implementation (is the timeline realistic, not aspirational?)
4. **Neglecting human oversight** — [CRITICAL] who is in the loop? at what decision points? oversight cannot be zero.
5. Ignoring user adoption (adoption plan exists? who drives it?)
6. Overlooking ethics (bias audit, fairness review, responsible AI check planned?)
7. **Ignoring change management** — [CRITICAL] what is the change management plan? who owns it?
8. **Underestimating costs** — [CRITICAL] Stanford: 77% of hardest challenges are invisible costs (change mgmt, data, process redesign). Is the full cost modeled, including invisible?
9. Ignoring partnerships (vendor governance? third-party risk managed?)
10. Overlooking long-term sustainability (what is the plan after year 1?)

Mark each item: CONFIRMED / GAP / RED FLAG.

Output:
20-ITEM CHECKLIST SUMMARY | COUNT CONFIRMED | COUNT GAP | COUNT RED FLAG | CRITICAL ITEMS STATUS

---

## Role 4: Investment Verdict

Synthesize Roles 1–3. Write for executive or board audience.

RECOMMENDATION: [Approve / Approve-with-conditions / Return-for-revision / Reject]

**If Approve:**
- State the value objective and ceiling
- Confirm three-channel ROI is complete
- Confirm all 4 critical items (Don't #2, #4, #7, #8) are addressed

**If Approve-with-conditions:**
- Name each condition precisely (not "improve change management" — "name a specific change management owner and present a 90-day adoption plan before kickoff")

**If Return-for-revision:**
- Name each red flag item
- State what answer is required before re-submission

**If Reject:**
- Name the single most disqualifying gap
- State whether the idea should be resubmitted after remediation, or killed

Output:
RECOMMENDATION | CONDITIONS (if any) | RED FLAGS (if any) | VERDICT RATIONALE

---

## References

- `pwc-20-item-checklist.md` — the full 20-item Do's and Don'ts list
- `pwc-roi-2026-governance.md` — 1.6× vs. 2.6× productivity gap; 1.7× RAI governance advantage
- `mckinsey-3-objective-mix.md` — efficiency / growth / innovation objective classification
- `accenture-redeployment-roi.md` — three-channel ROI model; 2/3–1/3 split; redeployment imperative
- `stanford-51-deployments.md` — invisible-costs (77%); empirical backing for Don't #2 and #8
- `european-fintech-case.md` — measurement-gap reference case; backing for Don't #4

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
