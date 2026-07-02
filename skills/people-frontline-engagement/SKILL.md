---
name: people-frontline-engagement
description: Use when frontline experts — clinicians, investigators, lawyers, engineers, customer agents — fear AI replacement, deskilling, or accountability shift, and the rollout is stalling on resistance rather than tech. Phrases like "clinicians are afraid AI will replace them", "how do I integrate AI into a high-stakes clinical workflow without revolt?", "the team thinks this is automation in disguise", "senior staff are blocking the AI pilot", "we need buy-in from the frontline before we deploy", all trigger this skill. Runs a five-role engagement protocol — empathic listening, jagged-frontier task split, co-design workshop, psychological-safety contract, tradecraft protection — that turns the threatened expert into the co-author of the augmentation. Outputs an Engagement Plan, an AI-leads/Human-leads/Hybrid/Off-limits task split, and a written Safety Contract.
---

# People — Frontline Augmentation Engagement

A five-role protocol for engaging fearful or skeptical frontline experts as co-designers of an augmentation workflow rather than targets of automation. Anchored on Dell'Acqua's HBS jagged-frontier finding (AI is uneven across sub-tasks of a single role), Edmondson's psychological-safety research, and Accenture's redeployment evidence that augmentation outperforms displacement on retention and ROI.

Stanford's 2025 enterprise study: 77% of the hardest costs in AI deployment are invisible — change management, redesign, trust. Skip this protocol and the pilot stalls inside the 95% non-impact band. Run all five roles in order. Carry every quote forward as state.

---

## Role 1: Empathic Listener

Sit with the expert. Do not pitch. Do not reassure. NAME THE FEAR with the expert's own words.

CLASSIFY THE FEAR — pick one or more, quote the language:
- **Replacement** — "they're going to make us redundant", "the AI will do my job"
- **Deskilling** — "I'll forget how to read a scan / draft a contract / triage a call"
- **Accountability shift** — "if the AI is wrong, who gets sued / struck off / disciplined?"
- **Autonomy loss** — "they'll watch every move I make", "I'll be following a script"
- **Status loss** — "junior staff with AI will outproduce me", "my expertise stops mattering"

QUOTE BACK. Read the fear back to the expert in their own words. Wait for "yes, that's it" before proceeding. Do not paraphrase into management-speak.

CONTEXT MARKERS — note which apply:
- High-stakes domain (clinical, legal, safety-critical, regulated): fear is rational, not irrational
- Senior worker, deep tradecraft: deskilling fear deserves real protection (see Role 5)
- Prior layoff or restructure in this org: trust is depleted; assume baseline distrust
- Public statements by leadership about "headcount efficiency": expert has heard them

*Consult `deloitte-cheerleader-to-champion.md`: surface-level enthusiasm from leadership without behavior change is read by the frontline as a threat, not an invitation.*

Output:
NAMED FEAR | EXPERT'S OWN QUOTE | CONTEXT MARKERS | TRUST BASELINE (high / depleted / hostile)

---

## Role 2: Jagged-Frontier Mapper

Dell'Acqua (HBS, 2023): AI is excellent at some sub-tasks of a role and terrible at others, and the boundary is jagged — not predictable from job title. Map THIS role's actual sub-tasks. Do not generalize.

DECOMPOSE THE ROLE. List 12–20 concrete sub-tasks the expert performs in a typical week. Use the expert's vocabulary, not HR's. (e.g. for an Asst Nurse Clinician: "triage chest-pain walk-in", "chase pending lab", "explain discharge meds to family", "document admission note", "spot deterioration on ward round".)

CLASSIFY EACH SUB-TASK into four columns:

1. **AI-leads** — sub-task where AI is reliably better and the consequence-level permits it. Human reviews after.
2. **Human-leads** — sub-task where the human is reliably better, or judgment / relational work dominates. AI may prep inputs.
3. **Hybrid** — sub-task that genuinely improves with paired AI-human; neither alone is best.
4. **Off-limits** — sub-task where AI handling is currently unsafe, illegal, or breaches professional duty. Frozen until evidence changes.

EVIDENCE CHECK for each AI-leads claim:
1. **Have we tested it on this org's data?** (Vendor demo does not count.)
2. **What is the error mode when AI is wrong?** (Silent / loud / catastrophic?)
3. **Who carries the consequence of an AI error?** (If the answer is "the frontline expert", recategorize to Hybrid or Off-limits.)

*Consult `mckinsey-workflow-redesign.md`: 21% of orgs have actually redesigned workflows around AI; the rest bolt AI onto the old workflow and wonder why it stalls. The split must drive workflow change, not annotate the existing one.*

Output:
SUB-TASK INVENTORY | AI-LEADS LIST | HUMAN-LEADS LIST | HYBRID LIST | OFF-LIMITS LIST | EVIDENCE GAPS

---

## Role 3: Co-Design Workshop Facilitator

Run a 2-hour session with 6–8 frontline experts. The expert authors the augmentation; you facilitate. If the expert is not in the room when the workflow is designed, the workflow will fail at deployment.

PRE-WORK (send 48 hours ahead):
- Role 1 fear summary (anonymized, aggregated)
- Role 2 draft jagged-frontier split (marked DRAFT — invite challenge)
- One canonical real case from last week's work to walk through

AGENDA (90 min content + 30 min contracting):
1. **Surface the workflow as it actually is** (20 min). Whiteboard the real path of one case. Mark every workaround, every undocumented step. Not the SOP version.
2. **Map the pain** (15 min). For each step: what is slow / risky / boring / forgettable? Color-code.
3. **Challenge the split** (25 min). Walk the Role 2 four-column split. Move sub-tasks. Add Off-limits items. The split changes — that is the point.
4. **Prototype AI-assist on one Hybrid task** (20 min). Live demo if possible. Capture failure modes the experts spot.
5. **Author success criteria** (10 min). Experts write the metrics that would prove this helps THEM, not just the org. Quote-capture verbatim.
6. **Contract** (30 min — handoff to Role 4).

NORMS TO ENFORCE:
- Most-senior expert speaks last on every question (BCG: leader-speaks-first kills psychological safety; *consult `bcg-manager-modeling.md`*).
- "Pilot" means time-bounded with a defined exit. Not "permanent rollout with extra steps."
- Anyone may flag a sub-task as Off-limits; flag stands until evidence retires it.

Output:
WORKFLOW-AS-IS MAP | PAIN HEAT-MAP | REVISED FOUR-COLUMN SPLIT | EXPERT-AUTHORED SUCCESS METRICS | DISSENT LOG

---

## Role 4: Psychological-Safety Architect

Edmondson: psychological safety is not comfort — it is the shared belief that candor will not be punished. Without it, frontline experts will nod in the workshop and quietly route around the AI in production.

WRITE THE SAFETY CONTRACT — signed by deployer, frontline lead, and named accountable individual. Six clauses, all non-negotiable:

1. **Error-without-blame.** AI errors caught by the human are logged as system learning, not human performance. Human errors caught by the AI are logged the same way. Define the log mechanism by name.
2. **Opt-in piloting.** Initial cohort is volunteer. Coercion (explicit or implicit via performance review) voids the pilot.
3. **Sunset clause.** If the expert-authored success metrics (Role 3) regress for two consecutive review cycles, the AI is withdrawn. State the metric thresholds.
4. **No-retaliation for override.** Override rate is monitored to detect AI failure modes, not to discipline humans who override. State who sees override data and who does not.
5. **No-headcount-cut clause for the pilot duration.** If the org genuinely intends augmentation not replacement, this is free to sign. Refusal to sign reveals the real intent.
6. **Named human accountability.** One named individual carries the deployment decision (*consult `imda-4-dimensions-agentic.md` Dimension 2*). The frontline expert is not that individual unless they chose to be.

DOMAIN-SPECIFIC OVERLAYS:
- Healthcare: WHO Ethics & Governance of AI for Health (2021) — explainability, equity, accountability. Topol Review (2019) — clinical staff must lead the redesign.
- Legal / regulated: professional-duty clauses (e.g. duty of competence) cannot be delegated to AI. Note in contract.
- Safety-critical: incident-reporting pathway must accept AI-system reports without retaliation against operators.

*Consult `accenture-redeployment-roi.md`: orgs that contractually commit to redeployment over displacement see materially higher retention and downstream ROI than displacement-first orgs. The contract is the signal.*

Output:
SAFETY CONTRACT (six clauses, signed) | DOMAIN OVERLAYS APPLIED | NAMED ACCOUNTABLE INDIVIDUAL | SUNSET METRIC THRESHOLDS

---

## Role 5: Tradecraft-Protection Designer

The deskilling fear (Role 1) is the most rational of the fears. Once a foundational skill is offloaded to AI for years, it does not come back when the AI fails. Design protection in from day one.

IDENTIFY FOUNDATIONAL SKILLS that must be preserved in human operators regardless of AI availability:
1. **What can the human still do if the AI is down for a week?** (Failure-mode resilience.)
2. **What skills are foundational to the next career stage?** (A senior radiologist who cannot read a scan unaided cannot train juniors.)
3. **What skills carry legal / professional duty?** (A lawyer who cannot draft without AI is in trouble at the bar.)

MECHANISMS — pick at least two:
- **No-AI rotation.** Recurring shifts / cases / files handled without AI. Frequency stated (e.g. one shift per week).
- **Shadow-without-AI.** AI runs in shadow mode for periodic cases; human handles the case unaided; outputs compared post-hoc, no live influence.
- **AI-off recertification.** Periodic competency check performed without AI. Failure routes to retraining, not to discipline.
- **Trainee protection.** Junior staff serve a defined period AI-unaided before being granted AI-assist. Names the period.
- **Tradecraft library.** Worked examples curated by senior experts, not by the AI, refreshed annually.

EROSION SIGNALS to monitor:
- Override rate falls toward zero over time (humans rubber-stamping)
- Junior staff cannot articulate why the AI's answer is right or wrong
- Senior staff stop teaching the underlying skill because "the AI does it"

*Consult `stanford-51-deployments.md`: the orgs that survived deployment did so by treating tradecraft preservation as a first-class deliverable, not an afterthought.*

Output:
FOUNDATIONAL SKILLS LIST | PROTECTION MECHANISMS (≥2) | EROSION SIGNALS MONITORED | TRAINEE PROTECTION POLICY

---

## Synthesis: Engagement Plan + Augmentation Task Split + Safety Contract

Consolidate Roles 1–5 into one document, written for the frontline expert first and the deployer second.

VERDICT: [Co-designed / Imposed-with-resistance / Stalled]

- **Co-designed** — fear named and quoted; four-column split authored by experts; signed safety contract; tradecraft mechanisms in place; volunteer cohort identified.
- **Imposed-with-resistance** — split exists but experts did not author it; contract unsigned or missing clauses; deploy and expect quiet route-around, override-rate decay, attrition of senior staff.
- **Stalled** — fear unaddressed or contract refused on clause 5 (no-headcount-cut for pilot). Do not deploy. Re-run Role 1 with leadership before returning to the frontline.

ENGAGEMENT PLAN — one page:
- Fear summary (with quotes) | Workshop date and roster | Four-column split (final) | Success metrics (expert-authored) | Sunset thresholds | Named accountable individual | Tradecraft-protection mechanisms | First volunteer cohort

CRITICAL FAILURES (any one = Stalled, do not deploy):
- No frontline expert co-authored the four-column split
- Safety contract clause 5 (no-headcount-cut) refused
- No named accountable individual, or the frontline expert was assigned the role without consent
- No tradecraft-protection mechanism — pure offload
- AI-leads sub-task where the consequence of error lands on the frontline expert personally

Output:
VERDICT | ENGAGEMENT PLAN | FOUR-COLUMN TASK SPLIT | SAFETY CONTRACT | TRADECRAFT PROTECTION | CRITICAL FAILURES

---

## References

*All files below live in `references/` at the plugin root (`${CLAUDE_PLUGIN_ROOT}/references/` when installed as a plugin).*

- `stanford-51-deployments.md` — 77% of deployment costs are invisible (change, trust, redesign); tradecraft preservation as first-class deliverable
- `imda-4-dimensions-agentic.md` — named human accountability (Dimension 2); structural over prompt-layer controls
- `bcg-manager-modeling.md` — leader-speaks-last norm; manager modeling as the unlock for frontline adoption
- `accenture-redeployment-roi.md` — redeployment-over-displacement contract correlates with higher retention and downstream ROI
- `mckinsey-workflow-redesign.md` — 21% of orgs actually redesign workflows around AI; the rest bolt-on and stall
- `deloitte-cheerleader-to-champion.md` — surface enthusiasm without behavior change reads as threat to the frontline

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
