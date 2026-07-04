---
name: people-tool-selection
description: Use when choosing which AI tool to put in front of a specific user group — a training cohort, a team, a school, a department — or deciding whether to teach deeper prompting, extend existing tools with agent skills, or introduce a new tool. Phrases like "which AI tool should I teach this group?", "choosing an AI tool for our teachers / nurses / analysts", "should I teach advanced prompting or a new tool?" all trigger this skill. Runs six roles — Audience Profiler, Constraint Mapper (hard eliminators before any capability comparison), Intervention-Mode Selector (Deepen / Extend / Introduce), Capability-Delta Assessor, First-Win Realist, Synthesis. Outputs Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip plus a growth path. For build/buy/partner sourcing of an AI capability use tech-buy-vs-build; for enterprise-wide curriculum design use people-literacy-curriculum.
---

# People — AI Tool Selection

Choose which AI tool to introduce to a specific user group, or whether to introduce a new tool at all. The unit of analysis is the group's adoption, not the technology. Six sequential roles. Maintain all prior reasoning as state — each role builds on the previous.

Two structural rules that govern the whole diagnosis:

1. **Constraints eliminate before capability ranks.** A tool that fails a hard constraint (cost, ecosystem, setup, language, data, IT policy) is out regardless of how capable it is. Do not build a weighted matrix that lets capability buy back a failed constraint.
2. **Measure delta from the group's baseline, not absolute capability.** A tool that improves artifacts the group can already make competes with "just teach better prompting." A tool that unlocks a new artifact class at near-zero effort wins the session.

Mode vocabulary: **Deepen / Extend / Introduce**. Verdict vocabulary (stable output contract): **Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip**. For build/buy/partner sourcing use `tech-buy-vs-build`; for enterprise-wide curriculum design use `people-literacy-curriculum`.

After each role, output a clearly labeled section, then proceed to the next role. Do not stop until all six are complete.

---

## Role 1: Audience Profiler (Who is this group, really?)

BASELINE. Which AI tools does the group already use, and at what fluency? Name them. If the group already uses general chatbots competently, re-teaching basics is a wasted session and "a better chatbot" is a weak increment.

ARTIFACT INVENTORY. What does this group actually produce in their job, weekly? (Lesson plans, slide decks, videos, quizzes, reports, client emails, care notes.) The tool must map to artifacts on this list — not to abstract "productivity."

LANGUAGE AND DEVICE REALITY. Working language(s). Managed or personal devices. Connectivity. Existing organizational subscriptions (Google Workspace, Microsoft 365, LMS).

TIME BUDGET. How long is the training window, and how much learning time exists after it? A one-session engagement and a semester program justify different tools.

Output:
GROUP | BASELINE TOOLS + FLUENCY | ARTIFACT INVENTORY | LANGUAGE / DEVICE / SUBSCRIPTIONS | TIME BUDGET

---

## Role 2: Constraint Mapper (What eliminates a candidate outright?)

List the candidate tools/approaches under consideration, then apply hard filters. A candidate failing ANY filter is eliminated — record which single constraint killed it. Do not score. Eliminate.

- COST. Is a free tier viable at group size? If not, who pays, and is that budget real?
- ECOSYSTEM. Does it work inside accounts and subscriptions the organization already holds? New account provisioning, SSO exceptions, and license requests are invisible costs that stall rollouts. *Consult `stanford-51-deployments.md` — 77% of the hardest deployment challenges are invisible costs, not tech.*
- SETUP FRICTION. Can the median group member produce output with zero installation and zero configuration? Every setup step loses a fraction of the room.
- DATA SENSITIVITY. What data will members feed it — student records, patient data, client contracts? If sensitive data is central to the use, run `tech-data-deployment` before proceeding; its Blocked verdict overrides anything this skill concludes.
- LANGUAGE SUPPORT. Does the tool actually work in the group's working language, at output quality the group's audience will accept?
- IT / ADMIN POLICY. Is it permitted on managed devices and networks? Is there an approval path if not?

Output:
CANDIDATES | CONSTRAINT TABLE (pass/fail per filter) | SURVIVORS | ELIMINATED (each with the single killing constraint)

---

## Role 3: Intervention-Mode Selector (Deepen / Extend / Introduce?)

Work only from Role 2's survivor set — constraints already eliminated the rest. The real choice set is rarely just tools — it is three intervention modes. Pick the primary mode before ranking tools.

- **DEEPEN** — better use of tools the group already has (structured prompting frameworks, workflow habits). Right when the baseline is low, or current tools are underused relative to their ceiling.
- **EXTEND** — add capability to existing tools (agent skills, custom GPTs/Projects, connectors, templates). Right when the baseline is solid AND someone in the group can own and maintain the extensions. *Consult `hiten-skill-library.md` — the skill-library strategy is the canonical Extend play.*
- **INTRODUCE** — a new tool. Right only when it unlocks artifact classes the current tools cannot produce, and it survives every Role 2 constraint.

State the primary mode and the single condition that would flip it. Remember the 70/20/10 prior: the tool is the smallest part of what makes adoption work. *Consult `70-20-10-value-split.md`.*

Output:
MODE (Deepen / Extend / Introduce) | WHY | FLIP CONDITION

---

## Role 4: Capability-Delta Assessor (What does each survivor unlock?)

For each surviving candidate, assess against the Role 1 artifact inventory:

- DELTA. Which NEW artifact classes does it unlock that the baseline tools cannot produce? Which existing artifacts does it merely improve? New-class beats better-same.
- FRICTION. Minutes from login to first job-relevant output, for the median member.
- CEILING. Where does the tool top out for this group, and what is the natural next step after it?

Rank survivors by delta-per-unit-of-friction. If no candidate's delta beats "deepen the baseline," say so — Skip is a valid outcome.

Output:
Per candidate: DELTA (new classes vs. improved-same) | FRICTION (minutes to first output) | CEILING | RANKED ORDER

---

## Role 5: First-Win & Day-2 Realist (Will this survive contact?)

FIRST WIN. Design the in-session exercise: can every member produce a job-relevant artifact from their own material within ~20 minutes hands-on? Name the exercise concretely. If no first win fits the window, the tool is wrong for this session regardless of ceiling.

DAY-2 SUPPORT. Who role-models usage next week, when the trainer is gone? Who does a stuck member ask? Unmodeled tools decay within weeks. *Consult `bcg-manager-modeling.md` — 88% adoption when managers role-model, 25% when they don't.*

BLAST RADIUS. Where do the group's AI-produced artifacts go — students, patients, clients, the public? Name the review step between the tool and that audience.

LITERACY OBLIGATION. If the employer is in EU scope, record how this training contributes to Art. 4 literacy evidence. *Consult `eu-ai-act-essentials.md`.*

Output:
FIRST-WIN EXERCISE | DAY-2 ROLE-MODEL + HELP PATH | BLAST RADIUS + REVIEW STEP | OBLIGATION NOTES

---

## Role 6: Synthesis (The recommendation)

Read the outputs of Roles 1–5. Produce the verdict. Do not introduce new assessment here. Write for the person who must stand in front of the group.

VERDICT: [Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip]

- **Adopt-now** — passes all constraints; first win demonstrable in-session; day-2 role-model named.
- **Adopt-with-scaffolding** — right tool, but day-2 support or the blast-radius review step must be built first; name what and by whom.
- **Pilot-with-subgroup** — delta is real but a constraint (language quality, IT approval, data tier) is unproven; validate with a subgroup before full rollout.
- **Skip** — fails a hard constraint, or no candidate's delta beats deepening the baseline.

PRIMARY TOOL + MODE: (tool, and Deepen / Extend / Introduce)
FIRST-WIN EXERCISE: (one sentence, concrete)
GROWTH PATH: what module 2 is, once the primary tool lands (e.g., deepen prompting on top of the new tool)
WEAKEST LINK: where adoption is most likely to fail silently
CLOSEST REFERENCE CASE: match against `cases/` and name the parallel explicitly.

---

## Reference Cases

See `cases/` for selection decisions this skill encodes. When selecting for a new group, compare against the closest reference case and note the parallel explicitly.

## References

*All files below live in `references/` at the plugin root (`${CLAUDE_PLUGIN_ROOT}/references/` when installed as a plugin).*

- `stanford-51-deployments.md` — invisible costs (setup, provisioning, change management) dominate deployment difficulty
- `bcg-manager-modeling.md` — 88/25 role-modeling gap; day-2 adoption depends on visible modeling, not training quality
- `70-20-10-value-split.md` — the tool is the 10%; people and process carry adoption
- `hiten-skill-library.md` — the Extend mode's canonical strategy: a skill library on top of existing tools
- `eu-ai-act-essentials.md` — Art. 4 literacy obligation trainings can evidence
