# CLAUDE.md

This repo is a Claude Code plugin: 15 prompt-only skills for enterprise AI
transformation. No build step, no runtime dependencies — everything is
markdown plus two JSON manifests.

## Layout

- `skills/<bucket>-<name>/` — one directory per skill: `SKILL.md` (the skill),
  `README.md` (human-facing summary), optional `cases/` (worked examples).
  Buckets: `general-` (strategy/diagnosis), `process-` (pilot/ship/observe),
  `tech-` (stack/sourcing/data/agents), `people-` (leadership/workforce/frontline).
- `references/` — 200–500-word research extracts skills cite by bare filename.
  `references/_index.md` is the catalog; its consumer columns are validated
  against actual citations.
- `.claude-plugin/plugin.json` + `marketplace.json` — both list all 15 skills
  and carry the version; they must stay in sync (CI checks this).
- `templates/SKILL.md.tmpl` — starting point for new skills.
- `docs/` — usage guide, demo scripts, effectiveness reports.

## Conventions

- Skills cite reference files by bare filename in backticks, e.g.
  ``consult `95-5-genai-divide.md` `` — resolved against `references/` at the
  plugin root. Every citation must resolve to a real file.
- Adding/renaming a skill requires updating BOTH `.claude-plugin/plugin.json`
  and `.claude-plugin/marketplace.json`, plus `README.md` tables and
  `INSTALL.md` trigger-phrase tables.
- Each skill's verdict vocabulary (e.g. Fund / Reframe / Kill) is a stable
  output contract — do not rename verdicts; downstream users depend on them.
- Skill H1 titles read `<Bucket> — <Title>` (e.g. `# General — AI Idea Diagnostic`).
- Frontmatter: `name` must match the directory name; `description` ≤ 1024 chars
  and must include the trigger phrases.
- Commit style: `<skill-or-ref>: <what changed>`
  (e.g. `general-roi-gate: tighten Q3 measurement prompt`).
- Notable changes go under `## [Unreleased]` in `CHANGELOG.md`.

## Before committing

Run the consistency validator — CI runs the same script on every push/PR:

```bash
python3 scripts/validate.py
```

## Releasing

```bash
python3 scripts/bump_version.py 0.4.0
```

Updates both manifests and stamps the `[Unreleased]` changelog section with
the version and date.
