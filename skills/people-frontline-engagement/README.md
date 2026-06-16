# People — Frontline Augmentation Engagement

A five-role engagement protocol that turns fearful frontline experts into co-authors of an augmentation workflow.

## What it does

1. Names and classifies the frontline fear (replacement / deskilling / accountability shift / autonomy / status) in the expert's own quoted language
2. Maps the role into a four-column jagged-frontier task split (AI-leads / Human-leads / Hybrid / Off-limits) with evidence checks
3. Runs a 2-hour co-design workshop where the experts redraw the split and author their own success metrics
4. Drafts a six-clause Psychological Safety Contract (error-without-blame, opt-in, sunset, no-retaliation-on-override, no-headcount-cut, named accountable individual)
5. Designs tradecraft-protection mechanisms (no-AI rotation, AI-off recertification, trainee unaided period) and issues a Co-designed / Imposed-with-resistance / Stalled verdict

## When to use it

When frontline experts — clinicians, examiners, investigators, lawyers, engineers, customer agents — are blocking or quietly route-arounding an AI rollout. Trigger phrases: "clinicians are afraid AI will replace them", "the team thinks this is automation in disguise", "senior staff are blocking the pilot", "two town halls ended in walkouts". Use when the rollout is stalling on resistance, not on technology, and especially when there has been a recent restructure or headcount cut.

## What it outputs

- Fear classification table with verbatim expert quotes and trust baseline
- Four-column AI-leads / Human-leads / Hybrid / Off-limits task split with evidence gaps
- Workshop-as-is workflow map, pain heat-map, and expert-authored success metrics
- Six-clause signed Safety Contract with named sunset thresholds and accountable individual
- Tradecraft-protection mechanisms and erosion-signal monitoring plan
- Verdict: Co-designed / Imposed-with-resistance / Stalled, with critical-failure stop conditions

## Example

**Scenario:** Ji-won Park is Director of Examination Reform at KIPO (Korea Intellectual Property Office, Daejeon), overseeing 1,180 patent examiners. A vendor-built AI prior-art and claim-similarity tool is ready for an electrical-division pilot (240 examiners), but the senior examiners' union (avg tenure 17 years) has formally objected after a recent 6% headcount cut. Two town halls ended in walkouts. The Commissioner wants Q3 launch; Ji-won has six weeks to the next steering committee.

**User prompt:**

> I run examination reform at KIPO in Daejeon. We've got an AI prior-art and claim-similarity tool ready to pilot in our electrical patent division — about 240 examiners — and the senior examiners' union has dug in. Two town halls ended in walkouts. The grievances I'm hearing: "this is automation in disguise after last year's 6% cut", "if I grant a patent the AI flagged as novel and it gets invalidated at IPTAB, I'm the one whose name is on the file", and from the 20-year veterans, "junior examiners with this tool will look more productive than me on the dashboard." The Commissioner wants electrical division live by end of Q3. How do I actually get the senior examiners on board so this doesn't blow up at the steering committee in six weeks? I need a concrete plan, not platitudes.

**Skill output (excerpt):**

```
VERDICT: Stalled — do NOT launch Q3 as scoped. Re-run Role 1 with Commissioner before
returning to the union. Two clauses below are non-negotiable for restart.

ROLE 1 — NAMED FEARS (verbatim)
  F1 Replacement      "automation in disguise after last year's 6% cut"   trust = depleted
  F2 Accountability   "I'm the one whose name is on the IPTAB file"       fear = rational
  F3 Status / dashboard inversion  "juniors will look more productive than me"

ROLE 2 — JAGGED-FRONTIER SPLIT (electrical division, 14 sub-tasks)
  AI-leads (3)    KR/EN/JP/CN prior-art retrieval ranking; duplicate-claim clustering;
                  citation-graph expansion
  Human-leads (5) means-plus-function claim parsing; non-text disclosure (drawings,
                  circuit diagrams); §57 KPA novelty judgement; IPTAB-defensible
                  reasoning; examiner interview with applicant
  Hybrid (4)      foreign-language art triage; claim-chart drafting; 102/103 mapping;
                  Office Action drafting
  Off-limits (2)  final grant decision; IPTAB liaison correspondence
  Evidence gap:   vendor demo only — no benchmark on KIPO's own 2023–24 electrical corpus

ROLE 4 — SAFETY CONTRACT (six clauses, signed by Commissioner + union chair + Ji-won)
  1. Error-without-blame: AI-flagged novelty later invalidated at IPTAB → system-learning
     log, not examiner performance review. Log owner: Examination Quality Bureau.
  2. Opt-in pilot cohort: 24 volunteer examiners. Coercion via KPI voids the pilot.
  3. Sunset: invalidation rate, examiner-hours-per-grant, or appeal rate regress for
     two consecutive quarters → tool withdrawn. Thresholds named in Annex A.
  4. No-retaliation override: override rate visible to union rep + EQB only,
     never to line supervisors or the dashboard.
  5. NO-HEADCOUNT-CUT for pilot duration (24 months). Refusal to sign = Stalled.
  6. Named accountable individual: Deputy Commissioner (Examination), not the examiner.

ROLE 5 — TRADECRAFT PROTECTION
  - Trainee unaided period: 24 months full examination without AI before AI-assist granted
  - No-AI rotation: one examination day per fortnight, AI off, full claim parse unaided
  - AI-off recertification: annual, failure routes to retraining not discipline
  - Erosion signals monitored: override rate trending to zero; juniors unable to articulate
    why the AI was wrong; senior examiners stop teaching means-plus-function parsing

CRITICAL FAILURES IF DEPLOYED AS-IS
  [X] Clause 5 (no-headcount-cut) not yet offered → F1 unaddressed
  [X] Dashboard productivity ranking not redesigned → F3 structurally amplified by tool
  [X] IPTAB liability default lands on examiner → F2 unaddressed; recategorize to Hybrid
```

**How to read this output:**

- The **Verdict** is load-bearing — Stalled means do not deploy regardless of Commissioner pressure. The two named gates (clause 5 and dashboard redesign) are the unblock conditions.
- The **four-column split** must be authored or revised by examiners in the workshop. If it arrives pre-baked from the deployer, the contract is theatre.
- The **six contract clauses** are non-negotiable as a set. Refusal to sign clause 5 (no-headcount-cut) is the diagnostic for whether leadership actually means augmentation or means displacement.
- The **trainee unaided period** is the structural inversion of F3 (status / dashboard inversion) — without it, the dashboard rewards the AI-augmented junior and punishes the senior expert.
- Push back if AI-leads contains any sub-task whose error consequence lands personally on the examiner — that recategorizes to Hybrid or Off-limits.

## Sources used

- `stanford-51-deployments.md` — 77% of deployment costs are invisible (change, trust, redesign); tradecraft preservation as first-class deliverable
- `imda-4-dimensions-agentic.md` — named human accountability (Dimension 2); structural over prompt-layer controls
- `bcg-manager-modeling.md` — leader-speaks-last norm; manager modeling as the unlock for frontline adoption
- `accenture-redeployment-roi.md` — redeployment-over-displacement contract correlates with higher retention and downstream ROI
- `mckinsey-workflow-redesign.md` — 21% of orgs actually redesign workflows around AI; the rest bolt-on and stall
- `deloitte-cheerleader-to-champion.md` — surface enthusiasm without behavior change reads as threat to the frontline

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).

## Effectiveness

Effectiveness test (2026-06-12): scored 24/25 (Grade B, +5 lift over the strongest baseline of vanilla LLM and kb-ask retrieval). 3-judge unanimous verdict.

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
