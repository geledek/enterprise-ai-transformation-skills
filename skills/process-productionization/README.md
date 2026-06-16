# Process — Pilot-to-Production Playbook

A 5-stage playbook for moving a working AI prototype past demo-ware into SLO-bound production with named owners and a go-live verdict.

## What it does

1. Defines Stage 1 SLOs and eval discipline (p50/p95 latency, accuracy floor, hallucination ceiling, golden + adversarial sets, named eval owner)
2. Designs Stage 2 fallback and failure handling (silent-failure detector, HIL trigger, kill-switch SLA, deterministic fallback, incident logging)
3. Builds a Stage 3 staged-rollout plan (shadow / 1% canary / 10% / 50% / 100%) with named pause and rollback rules
4. Forces a Stage 4 operating-model shift from project team to product team (PM, eval engineer, on-call rota, change process, feedback loop)
5. Scores the Stage 5 15-item production-readiness gate and emits a GO / CONDITIONAL GO / NO-GO verdict, remediation list, and week-by-week rollout calendar

## When to use it

Triggered when a prototype works in demo but breaks in production, when SLOs and evals need to be defined, when a fallback / human-in-loop design is missing, or when a go-live readiness gate is needed. Anchored in Stanford's 51-deployments postmortem and NIST RMF MANAGE 2.4. Use after `process-pilot-design` and before scaling traffic.

## What it outputs

- Stage 1 SLO line: P50_LATENCY | P95_LATENCY | ACCURACY_FLOOR | HALLUCINATION_CEILING | EVAL_OWNER
- Stage 2 fallback line: SILENT_FAIL_DETECTOR | HIL_TRIGGER | KILL_SWITCH_SLA | FALLBACK_PATH | INCIDENT_LOG
- Stage 3 rollout line with shadow duration, canary pause rules, observability prerequisites, rollback triggers
- Stage 4 operating model: named PM, eval engineer, on-call rota, change process, feedback loop
- Stage 5 15-item gate scored GREEN / YELLOW / RED with named accountable individual per item
- One-page go-live memo: GO-LIVE VERDICT, remediation list (item, owner, due date), week-by-week rollout calendar

## Example

**Scenario:** Wei Lin, solo technical founder of Zeno AI (agentic AI for property maintenance — drafts work orders from tenant WhatsApp messages, dispatches contractors). The product is a Streamlit demo on her MacBook with hardcoded creds and a Google Sheet of contractors. Her first paying customer Astoria Estates (Singapore, 200 units across 4 condos) signed a S$48k/year contract and wants the system live across all 200 units in 8 weeks. Closing this contract decides whether Zeno raises pre-seed or shuts down.

**User prompt:**

> We have a working demo for Zeno (agentic AI for property maintenance — classifies tenant tickets, drafts work orders, dispatches contractors). First paying customer Astoria Estates wants 200 units live in 8 weeks. I am one person. Demo works but production breaks every other test. Need SLOs, fallbacks, a staged rollout plan, and an honest go-live readiness gate. Walk me through it.

**Skill output (excerpt):**

```
Stage 1 — SLO & Evals
  P50: 8s | P95: 25s | ACCURACY_FLOOR: 92% golden / 85% adversarial / 0.5% false-dispatch
  HALLUCINATION_CEILING: 1% on adversarial-20 | EVAL_OWNER: Wei (CI in GH Actions)

Stage 2 — Fallback
  SILENT_FAIL: 24h post-dispatch contractor reconciliation; mismatch → incident
  HIL: confidence < 0.70 OR cross-LLM disagreement OR landlord-only flag (2-min SLA)
  KILL_SWITCH: 5 min via LaunchDarkly toggle (tested W7)
  FALLBACK: manual workflow stays live as deterministic path (NOT deprecated)

Stage 3 — Staged rollout
  W8-9 shadow (200 units, log-only) → W10 1% canary (5 units) →
  W11-12 10% (1 condo) → W13 50% (2 condos) → W14 100%
  Pause rules per stage; auto-rollback wired

Stage 4 — Operating model (n=1 adaptation)
  PM: Wei (Mondays) + Marcus Tan (Astoria ops) as product partner; hire post-raise
  ON-CALL: solo, 8am-8pm SGT only, after-hours queue, repriced S$48k → S$42k
  CHANGE: 2-person CAB (Wei+Marcus), pre-merge eval gate

Stage 5 — Gate (15-item, week 7 review)
  13 GREEN | 2 YELLOW | 0 RED
   #6 Rollback path  YELLOW — full reversion-to-manual not yet timed end-to-end
  #15 Cost-per-task YELLOW — 50-ticket sample only, need shadow-stage data

VERDICT: CONDITIONAL GO at W8 — shadow + 1% canary only.
         Full 100% deferred to W14, NOT W8.
REMEDIATION (6 items, all dated, all owned)
  1. Renegotiate Astoria timeline → phased launch (W7, Wei)
  2. Time full reversion-to-manual end-to-end ≤30min (W7, Wei+Marcus)
  3. After-hours queue test on shadow data (W8-9, Wei)
  ...
```

**How to read this output:**

- The verdict line is load-bearing: CONDITIONAL GO with a deferred 100% date is the skill saying "your stated launch date is wrong"
- Look at YELLOW items first — they name exactly the gaps that would have killed the launch
- Every remediation item has a dated owner; if any owner is "the team" reject it
- The Stage 4 operating-model section adapts to constraints (here n=1 → business-hours SLA, repricing) rather than skipping the stage
- Push back if the Stage 5 gate has fewer than 15 items, or if shadow stage is shorter than 2 weeks

## Sources used

- `stanford-51-deployments.md` — postmortem of 51 enterprise AI deployments; root causes of post-launch failure
- `imda-4-dimensions-agentic.md` — structural-controls dimension (kill-switch, human-confirm, scope-fence)
- `nist-rmf-functions.md` — NIST AI RMF; MANAGE 2.4 mandates off-path procedures and incident response
- `pilot-discipline-ng.md` — Andrew Ng on pre-declared success metrics and pilot graduation
- `pwc-20-item-checklist.md` — production-readiness checklist; accountable-owner pattern
- `european-fintech-case.md` — fintech case delaying launch 6 weeks to close 4 gate items, then 18 months incident-free
- `mit-cisr-4-stages.md` — experiment → industrialize stage transition demanding operating-model change

## Effectiveness

Effectiveness test (2026-06-12): scored 23/25 (Grade D, +1.66 lift over the strongest baseline). kb-ask retrieval alone scored 21.34/25 — much of this skill's value is reproducible from the references/ folder. Strongest contribution is decision-ready artifact output (named owners, dated stop conditions).

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
