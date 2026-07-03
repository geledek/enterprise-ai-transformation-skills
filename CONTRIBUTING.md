# Contributing

## How to fork and extend

This repo is designed to be forked. Three extension points:

### 1. Add references

Copy a research extract into `references/`, following the file shape in `references/_index.md`. Update `_index.md` with a one-line entry. Skill descriptions reference files by name — your skill can point to any file in `references/` by name.

### 2. Add diagnostic cases

Drop a diagnosed case file into `skills/general-idea-diagnostic/cases/`. Use the existing case format (frontmatter + outcome summary + Q1–Q4 assessment + verdict). The `general-idea-diagnostic` skill will reference the closest case at synthesis time.

### 3. Fork a skill

Start from `templates/SKILL.md.tmpl` (it carries the frontmatter shape, role
structure, and a pre-PR checklist), or copy any `SKILL.md`, rename it, and adjust:
- `name` and `description` frontmatter
- Role instructions (add sector-specific context, internal process names, role titles)
- Reference pointers (point to your own reference files or internal docs)

Example forks: sector-specific (`general-idea-diagnostic-healthtech`), internal process-aware (`roi-gate-[company]`), role-specific (`people-readiness-conversation-board`).

### 4. Distill a new skill from a book or your own practice

The skills here are distilled decision processes. To add one, answer five
questions before writing any role (the full version lives in
`templates/SKILL.md.tmpl`):

1. What decision does the skill gate, and who stands behind the verdict?
2. What are the sequential questions? Each "because" in the original reasoning becomes a role.
3. Which criteria are hard filters (eliminate) vs. ranking criteria (compare)? Keep them in separate roles.
4. Which failure modes deserve their own role?
5. What verdict vocabulary fits — without colliding with another skill's?

Then define 2–3 **negative triggers** — adjacent prompts that must route to a
*different* skill — and add them to the routing table in
`tests/golden-prompts.md`. Before merging, confirm the skill reproduces the
case that inspired it, and that one counterfactual (a changed input) flips the
verdict. `skills/people-tool-selection/` with its `cases/` file is the worked
example of this process.

## What not to change in a fork

- The structural role sequence — it's the methodology, not a style choice
- The output shape (Fund/Kill/etc.) — downstream tooling may depend on this
- Attribution in frontmatter — add your own, don't remove the original

## Pull requests to this repo

PRs welcome for:
- Reference file additions (new flagship research, 2024+)
- Case studies (anonymized, following Stanford 2026 convention: pattern over personality)
- Bug fixes in skill logic or reference pointers
- New skills that fill lifecycle gaps

PRs not accepted for:
- Removing the MIT license or attribution
- Breaking changes to existing skill output shapes
- Vendor-specific promotions

## Before opening a PR

Run the consistency validator — CI runs the same script and will reject drift:

```bash
python3 scripts/validate.py
```

It checks that every reference pointer resolves, `references/_index.md`
matches actual citations, the plugin manifests match the `skills/`
directories, and frontmatter is well-formed. If you changed a skill's
behavior, re-run its row from `tests/golden-prompts.md` and confirm the
verdict vocabulary is unchanged — or run it live:

```bash
python3 scripts/run_golden_prompts.py --only <your-skill>          # activation
python3 scripts/run_golden_prompts.py --routing --only <your-skill> # routing
```

(This calls the API through headless `claude -p`, so it costs tokens and is
not run by CI. If you changed a frontmatter `description`, run the routing
mode — descriptions are what Claude routes on.)

## Commit style

`<skill-or-ref>: <what changed>`

Examples:
- `references: add stanford-51-deployments extract`
- `general-roi-gate: tighten Q3 measurement prompt`
- `general-idea-diagnostic: add healthtech case`
