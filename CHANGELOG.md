# Changelog

All notable changes to this plugin are documented here.

## [Unreleased]

### Added
- `scripts/run_golden_prompts.py` — live golden-prompt runner. Executes every activation and routing prompt from `tests/golden-prompts.md` through headless `claude -p --plugin-dir`, asserting the right skill activates, adjacent skills stay dormant, and (in `--full` mode) the output uses the contracted verdict vocabulary. Costs API tokens — run before releases, not in CI. Supports `--model` for cross-model checks.
- "Wrong verdict report" issue template (`.github/ISSUE_TEMPLATE/wrong-verdict.yml`) — structured field-report intake; every confirmed report becomes a regression case.

### Fixed
- **`plugin.json` rejected by current Claude Code.** The manifest failed schema validation (`author` must be an object, not a string; `skills` paths must be `./`-prefixed), so `--plugin-dir` loads — and potentially fresh plugin-manager installs — silently dropped all 16 skills. Found by the first live run of the golden-prompt runner.

### Changed
- Applied a "missing manual" checklist pass (trigger design, structure, steering, pruning) across the skill suite:
  - Removed a generic "write for [audience]. Be direct." sentence from 7 Synthesis/consolidation roles that added nothing beyond the output template already below it (kept concrete stakeholder specs where present, e.g. `tech-data-deployment`'s CISO/business-owner/DPO sign-off).
  - Reinforced two under-used "leading words" so they survive past the intro: `people-tool-selection`'s "constraints eliminate before capability ranks" now echoes at Role 3; `general-idea-diagnostic`'s "Friction-first vs. Tech-first" now echoes at Roles 2 and 4.
  - Shortened the two long "not to be confused with" disambiguation footnotes (70/20/10 in `process-portfolio-observability`, 88/25 in `tech-data-deployment`) — each colliding number is now self-disambiguating at first use, so the footnote no longer has to carry the whole burden.
  - Trimmed one redundant example trigger phrase each from the three longest skill descriptions (`people-tool-selection`, `tech-data-deployment`, `people-frontline-engagement`), keeping every distinct phrasing.
  - `CLAUDE.md` documents the deliberate model-invoked trigger choice for this plugin (and the context-load tradeoff), so it isn't "fixed" by a future contributor; `templates/SKILL.md.tmpl` and `CONTRIBUTING.md` gain a noop-deletion-test and leading-words habit for new skills.

## [0.5.0] — 2026-07-02

### Added
- Routing (negative-trigger) tests in `tests/golden-prompts.md` — nine prompts that must route to one skill and must NOT activate its adjacent sibling (tool-selection vs. literacy-curriculum, idea-diagnostic vs. roi-gate, data-deployment vs. agent-guardrail, …), plus a dormancy check. Inspired by the book-to-skill ecosystem's activation/dormancy testing.
- Size-budget warning in `scripts/validate.py` — non-fatal WARN when a SKILL.md exceeds ~4K tokens (16K chars), keeping skills one-gulp loadable.
- Distillation guide — the five extraction questions for turning a book, framework, or real decision into a skill, in `templates/SKILL.md.tmpl` and `CONTRIBUTING.md`, with negative-trigger and counterfactual-reproduction requirements in the pre-PR checklist.
- **New skill: `people-tool-selection`** — six-role selector for choosing which AI tool to put in front of a specific user group (training cohort, team, department). Constraint-first method: hard eliminators (cost, ecosystem, setup friction, data, language, IT policy) filter candidates before capability comparison; then picks an intervention mode (Deepen / Extend / Introduce) and ranks survivors by new-artifact delta per unit of friction. Outputs Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip plus a first-win exercise and growth path. Ships with the Mongolian-teachers reference case (NotebookLM chosen over advanced prompting, agent skills, and Manus). Skill count is now 16.

### Changed
- All 16 SKILL.md files now front-load their output contract — verdict vocabulary (and boundary pointers to adjacent skills) stated before Role 1, so the contract survives context compaction.

## [0.4.0] — 2026-07-02

### Added
- `scripts/validate.py` + GitHub Action (`.github/workflows/validate.yml`) — CI consistency check on every push/PR: every reference pointer in a SKILL.md resolves, `_index.md` consumer columns match actual citations, plugin manifests match the `skills/` directories, versions agree across manifests, and skill frontmatter is well-formed.
- `CLAUDE.md` — repo conventions for Claude Code sessions (bucket prefixes, reference-pointer rule, verdict-vocabulary stability, validator, release flow).
- `templates/SKILL.md.tmpl` — starting point for new skills, with frontmatter shape, role structure, and a pre-PR checklist.
- `scripts/bump_version.py` — single-command version bump across `plugin.json`, `marketplace.json`, and the changelog.
- `tests/golden-prompts.md` — one trigger prompt per skill plus its output contract, for regression-checking skill edits.
- Each SKILL.md References section now states where reference files live (`${CLAUDE_PLUGIN_ROOT}/references/`), making retrieval deterministic when installed as a plugin.
- Plugin manifest metadata: `repository` + `keywords` in `plugin.json`, owner email in `marketplace.json`.

### Fixed
- **Broken reference pointer.** Three skills (`tech-buy-vs-build`, `tech-stack-diagnostic`, `general-peer-cases`) and `references/_index.md` cited `nanda-tech-buy-vs-build.md`, but the file on disk was named `nanda-buy-vs-build.md`. The file has been renamed to match the citations.
- **Stale consumer columns in `references/_index.md`.** The "Also consulted by" column predated the 0.3.0 skill renames and cross-linking; regenerated from actual SKILL.md citations. `pwc-six-step-roadmap.md` and `wef-strategic-positions.md` are flagged as not currently cited by any skill.

## [0.3.0] — 2026-06-16

### Added
- Bucket prefix in human-readable skill titles. Every SKILL.md and README.md H1 now reads `<Bucket> — <Title>` (e.g. `# General — AI Idea Diagnostic`).
- `docs/demo-script-metrobank.md` — six-prompt MetroBank Singapore live-demo script covering all four buckets.
- `docs/effectiveness/` — skill effectiveness reports.
- `references/queries/` — research query archive.

### Changed (BREAKING)
- All 15 skills renamed with bucket prefixes. **Reinstall required** for anyone on 0.2.x — the slugs in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` now point at the new directories.

  | Old slug | New slug |
  |---|---|
  | `ai-idea-diagnostic` | `general-idea-diagnostic` |
  | `use-case-discovery` | `general-use-case-discovery` |
  | `maturity-assessment` | `general-maturity-assessment` |
  | `peer-case-library` | `general-peer-cases` |
  | `roi-gate-pwc` | `general-roi-gate` |
  | `pilot-design` | `process-pilot-design` |
  | `productionization-playbook` | `process-productionization` |
  | `ai-portfolio-observability` | `process-portfolio-observability` |
  | `stack-diagnostic` | `tech-stack-diagnostic` |
  | `buy-vs-build` | `tech-buy-vs-build` |
  | `data-trust-deployment-pattern` | `tech-data-deployment` |
  | `agent-guardrail-imda` | `tech-agent-guardrail` |
  | `readiness-conversation` | `people-readiness-conversation` |
  | `workforce-literacy-curriculum` | `people-literacy-curriculum` |
  | `augmentation-frontline-engagement` | `people-frontline-engagement` |

- README rewritten as a decision-tree-first beginner guide, organized by the four buckets (general / process / tech / people) with a "Which skill when?" lookup table.
- INSTALL.md verification table regrouped by bucket.
- INSTALL.md — Claude Desktop install path corrected: Customization → Add plugin (`+`) → Create Plugin → Add Marketplace → Add from a repository.

### Fixed
- **Customer-facing pilot conflict.** `general-use-case-discovery` Role 4 now defaults customer-facing first-pilot candidates to *Stage-and-watch* unless the sponsor signs a tighter reliability bar. Previously the discovery skill's value-pool prompts pushed toward customer-pain pools that `process-pilot-design` would then downrate at the blast-radius check.
- **BCG 88/25 citation drift.** `tech-data-deployment` previously co-opted "BCG 88/25" to refer to the broad-use-vs-value-capture gap; now uses explicit wording and flags that the 88/25 *manager role-modeling* finding lives in the people bucket.
- **70/20/10 vs 10/20/70 confusion.** Three skills used the same digits for different things. `process-portfolio-observability` now explicitly labels its anchor as the *portfolio mix* prior (70% core / 20% adjacent / 10% transformational), distinct from BCG's 10/20/70 *effort split* and `people-literacy-curriculum`'s 70-20-10 *training-budget* split.
- `people-literacy-curriculum` BCG 88/25 attribution corrected to the manager-modeling source.

## [0.2.0] — 2026-06-14

Initial public release. Fifteen skills covering enterprise AI transformation, distilled from 21 flagship research sources (Stanford, MIT, McKinsey, BCG, Deloitte, PwC, Accenture, NIST, EU AI Act, IMDA, WEF).
