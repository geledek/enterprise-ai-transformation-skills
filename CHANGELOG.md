# Changelog

All notable changes to this plugin are documented here.

## [Unreleased]

### Added
- **New skill: `people-tool-selection`** — six-role selector for choosing which AI tool to put in front of a specific user group (training cohort, team, department). Constraint-first method: hard eliminators (cost, ecosystem, setup friction, data, language, IT policy) filter candidates before capability comparison; then picks an intervention mode (Deepen / Extend / Introduce) and ranks survivors by new-artifact delta per unit of friction. Outputs Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip plus a first-win exercise and growth path. Ships with the Mongolian-teachers reference case (NotebookLM chosen over advanced prompting, agent skills, and Manus). Skill count is now 16.

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
