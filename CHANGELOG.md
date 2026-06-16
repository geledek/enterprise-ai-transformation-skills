# Changelog

All notable changes to this plugin are documented here.

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
