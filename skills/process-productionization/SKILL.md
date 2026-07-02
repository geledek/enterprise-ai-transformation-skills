---
name: process-productionization
description: Use when moving an AI prototype past demo-ware into production with reliability, fallbacks, and on-call. Phrases like "demo works but production breaks", "need SLOs and evals", "AI still makes mistakes so benefit unclear", "fallback and human-in-loop design", "staged rollout plan", "go-live readiness gate" all trigger this skill. Runs the 5-stage pilot-to-production playbook anchored in Stanford's 51-deployments postmortem and NIST RMF MANAGE controls. Outputs a go-live verdict, remediation list, and week-by-week rollout schedule.
---

# Process — Pilot-to-Production Playbook

Take a working prototype to production-grade. Stanford's 51-deployment study found most failures happen *after* the demo: missing SLOs, no fallback path, no on-call, project team disbands before product team forms. NIST RMF MANAGE 2.4 mandates off-path handling. This playbook closes the gap with 5 stages and a 15-item go-live gate.

## Stage 1: SLO & Eval Definition

Demos optimize for the happy path. Production needs measured floors and ceilings. *Consult `pilot-discipline-ng.md`: every pilot needs pre-declared success metrics or it cannot graduate.*

1. **What is the p50 and p95 latency budget?** (User-perceived; include retrieval, reasoning, tool calls, render.)
2. **What is the minimum acceptable accuracy on the golden set?** (Floor below which you roll back; size the golden set ≥200 labeled cases.)
3. **What is the maximum tolerable hallucination / fabrication rate?** (Ceiling per 100 calls; measured on adversarial-set ≥100 cases.)
4. **What is the regression eval cadence?** (Run on every prompt change, model version bump, retrieval-index refresh.)
5. **Who owns the eval suite as code?** (Named individual; suite lives in CI, not a notebook.)

Output:
P50_LATENCY | P95_LATENCY | ACCURACY_FLOOR | HALLUCINATION_CEILING | EVAL_OWNER

## Stage 2: Fallback & Failure Design

The r10 complaint — "AI still makes mistakes, benefit unclear" — is a fallback-design failure, not a model failure. *Consult `imda-4-dimensions-agentic.md`: structural controls (kill-switch, human-confirm, scope-fence) belong here.* *Consult `nist-rmf-functions.md`: MANAGE 2.4 requires off-path procedures for incidents.*

1. **What is the silent-failure mode?** (When the model is confidently wrong — who catches it, what signal triggers? Confidence score alone is insufficient.)
2. **What is the human-in-loop trigger?** (Defined thresholds: confidence < X, novel input class, regulated decision, monetary value > Y.)
3. **What is the kill-switch latency?** (Time from incident detection to system disable; target <5 minutes for high-stakes.)
4. **What is the deterministic fallback path?** (Rule-based or human queue when AI declines; never a blank screen.)
5. **How are incidents logged for post-mortem?** (Trace ID, input, output, ground truth, decision; retained per regulatory requirement.)

Output:
SILENT_FAIL_DETECTOR | HIL_TRIGGER | KILL_SWITCH_SLA | FALLBACK_PATH | INCIDENT_LOG

## Stage 3: Staged-Rollout Plan

Big-bang launches caused 7 of Stanford's 51 documented failures. Staged rollout with named pause criteria per stage is the discipline. Observability dashboards must be live *before* stage 1, not after the first incident.

1. **Shadow stage — what runs in parallel?** (Model produces output; human/legacy system decides; outputs compared offline. Duration ≥2 weeks.)
2. **1% canary — what's the pause criterion?** (Named metric thresholds: latency, error rate, user complaints, cost-per-call. Auto-rollback if breached.)
3. **10% rollout — what new failure modes appear?** (Long-tail inputs, concurrency issues, downstream system load. Held ≥1 week.)
4. **50% rollout — is the operating model holding?** (On-call paged appropriately, runbooks used, evals catching regressions.)
5. **100% — what is the deprecation plan for the legacy path?** (Or is it kept as the deterministic fallback per Stage 2.)

Output:
SHADOW_DURATION | CANARY_PAUSE_RULE | OBSERVABILITY_DASHBOARD | ROLLBACK_TRIGGER | LEGACY_DEPRECATION

## Stage 4: Operating Model Shift

Stanford's 51 deployments converged on one root cause: project teams ship demos, product teams keep them alive. Most orgs never make the transition. *Consult `stanford-51-deployments.md`: deployments without a named PM and on-call rota fail within 90 days.* *Consult `mit-cisr-4-stages.md`: the move from "experiment" to "industrialize" is the stage that demands operating-model change.*

1. **Who is the product manager post-launch?** (Named individual, not a committee; owns roadmap, evals, user feedback.)
2. **Who is the eval engineer?** (Owns golden set, adversarial set, CI integration; distinct from data scientist.)
3. **What is the on-call rota?** (Minimum 3 engineers, weekly rotation, paged on SLO breach; runbook within 24 hours of go-live.)
4. **What is the change-management process for prompts and models?** (Two-person review, eval gate, staged rollout — same rigor as code.)
5. **What is the user-feedback loop?** (Thumbs-up/down captured, sampled and reviewed weekly, fed into adversarial set.)

Output:
PRODUCT_PM | EVAL_ENGINEER | ON_CALL_ROTA | CHANGE_PROCESS | FEEDBACK_LOOP

## Stage 5: Go/No-Go Gate

15-item production-readiness checklist. Each item has a named accountable individual; no item is owned by a team. *Consult `pwc-20-item-checklist.md`: missing accountable owners is the single largest predictor of post-launch incidents.* *Consult `european-fintech-case.md`: the fintech case study shows the gate working — they delayed launch 6 weeks to close 4 items, then ran for 18 months without major incident.*

Production-Readiness Checklist:
1. P95 latency measured on production-equivalent load — owner: SRE lead
2. Golden-set accuracy ≥ floor for 3 consecutive runs — owner: eval engineer
3. Adversarial-set hallucination ≤ ceiling — owner: eval engineer
4. Kill-switch tested in staging within 5-minute SLA — owner: SRE lead
5. Human-in-loop trigger documented and exercised — owner: product PM
6. Deterministic fallback path live and tested — owner: engineering lead
7. Incident-logging schema deployed and queryable — owner: data lead
8. Observability dashboard live with named alerts — owner: SRE lead
9. Shadow stage run ≥2 weeks with comparison report — owner: product PM
10. On-call rota published, paged in dry-run — owner: engineering manager
11. Runbook reviewed by full on-call rota — owner: engineering manager
12. Change-management process documented in repo — owner: engineering lead
13. User-feedback capture deployed in UI — owner: product PM
14. Regulatory sign-off obtained where required (EU AI Act, sector rules) — owner: compliance/legal
15. Cost-per-successful-task measured and within budget — owner: finance/PM

## Synthesis

Score the 15-item gate. Verdict states:

GO — all 15 items green; named owners confirmed; staged rollout begins.
CONDITIONAL GO — 1-3 items yellow; remediation owner and date pre-committed; rollout begins at shadow only until cleared.
NO-GO — any red item, or 4+ yellow; return to Stage 1 of the playbook for the affected dimension.

Output:
GO-LIVE VERDICT | REMEDIATION LIST (item, owner, due-date) | WEEK-BY-WEEK ROLLOUT (W1 shadow, W3 canary 1%, W4 10%, W6 50%, W8 100%)

The deliverable is a one-page go-live memo with the verdict, the remediation list, and the rollout calendar. No item without an accountable name. No stage without a pause rule.

## References

*All files below live in `references/` at the plugin root (`${CLAUDE_PLUGIN_ROOT}/references/` when installed as a plugin).*

- stanford-51-deployments.md — Stanford's postmortem of 51 enterprise AI deployments; root causes of post-launch failure.
- imda-4-dimensions-agentic.md — IMDA's structural-controls dimension covering kill-switch, human-confirm, scope-fence.
- nist-rmf-functions.md — NIST AI RMF; MANAGE 2.4 mandates off-path procedures and incident response.
- pilot-discipline-ng.md — Andrew Ng on pre-declared success metrics and pilot graduation criteria.
- pwc-20-item-checklist.md — PwC production-readiness checklist; accountable-owner pattern.
- european-fintech-case.md — Fintech case study delaying launch 6 weeks to close gate items, then 18 months incident-free.
- mit-cisr-4-stages.md — MIT CISR's experiment→industrialize stage transition demanding operating-model change.

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
