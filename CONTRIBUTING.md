# Contributing

## How to fork and extend

This repo is designed to be forked. Three extension points:

### 1. Add references

Copy a research extract into `references/`, following the file shape in `references/_index.md`. Update `_index.md` with a one-line entry. Skill descriptions reference files by name — your skill can point to any file in `references/` by name.

### 2. Add diagnostic cases

Drop a diagnosed case file into `skills/ai-idea-diagnostic/cases/`. Use the existing case format (frontmatter + outcome summary + Q1–Q4 assessment + verdict). The `ai-idea-diagnostic` skill will reference the closest case at synthesis time.

### 3. Fork a skill

Copy any `SKILL.md`, rename it, and adjust:
- `name` and `description` frontmatter
- Role instructions (add sector-specific context, internal process names, role titles)
- Reference pointers (point to your own reference files or internal docs)

Example forks: sector-specific (`ai-idea-diagnostic-healthtech`), internal process-aware (`roi-gate-[company]`), role-specific (`readiness-conversation-board`).

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

## Commit style

`<skill-or-ref>: <what changed>`

Examples:
- `references: add stanford-51-deployments extract`
- `roi-gate-pwc: tighten Q3 measurement prompt`
- `ai-idea-diagnostic: add healthtech case`
