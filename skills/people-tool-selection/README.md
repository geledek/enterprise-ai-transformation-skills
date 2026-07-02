# People — AI Tool Selection

A six-role selector for choosing which AI tool to put in front of a specific user group — or whether to introduce a new tool at all.

## What it does

Decides between three intervention modes and, within them, ranks candidate tools:
- **Role 1 (Audience Profiler):** baseline fluency, weekly artifact inventory, language/device/subscription reality, time budget
- **Role 2 (Constraint Mapper):** hard eliminators — cost, ecosystem, setup friction, data sensitivity, language support, IT policy. Constraints eliminate *before* capability ranks.
- **Role 3 (Intervention-Mode Selector):** Deepen (better use of current tools) / Extend (agent skills, templates) / Introduce (a new tool)
- **Role 4 (Capability-Delta Assessor):** new artifact classes vs. improved-same, ranked by delta-per-unit-of-friction
- **Role 5 (First-Win & Day-2 Realist):** the in-session win, who role-models next week, blast radius review
- **Synthesis:** Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip, plus a growth path

## When to use it

Planning a training, a team rollout, or a "which tool should we standardize on for this group?" decision. The unit of analysis is a human group's adoption, not architecture.

Boundaries: for build/buy/partner sourcing of a *capability*, use `tech-buy-vs-build`. For an org-wide literacy *curriculum*, use `people-literacy-curriculum` (this skill picks the tool; that one designs the program). If sensitive data is central, `tech-data-deployment` gates first.

## What it outputs

- Verdict: Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip
- Primary tool + mode (Deepen / Extend / Introduce)
- A concrete first-win exercise and a growth path
- Weakest link and closest reference case

## Cases

See `cases/` — starting with the Mongolian-teachers decision (NotebookLM chosen over advanced prompting, agent skills, and Manus).
