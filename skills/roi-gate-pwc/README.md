# ROI Gate (PwC)

A three-role investment approval gate: objective-mode audit, three-channel ROI model, PwC 20-item checklist. Outputs a formal Approve / Approve-with-conditions / Return-for-revision / Reject recommendation.

## What it does

Gates AI funding decisions before board or executive sign-off by running:
1. Objective-mode audit (efficiency / growth / innovation) — sets the value ceiling
2. Three-channel ROI model (revenue uplift / labor savings / labor avoidance) — requires a complete business case
3. PwC 20-item Do's-and-Don'ts checklist — surfaces gaps across 10 strategic dimensions

## When to use it

After a pilot has run and produced evidence, before committing to production investment or board approval. If you're still at concept stage, use `ai-idea-diagnostic` first. If you're designing the pilot, use `pilot-design` first.

## What it outputs

A structured investment recommendation with:
- Objective classification and value ceiling
- Three-channel ROI completeness assessment
- 20-item checklist summary (confirmed / gap / red flag)
- Formal recommendation with named conditions or red flags

## Sources used

- `pwc-20-item-checklist.md` — the 20-item gate
- `pwc-roi-2026-governance.md` — 1.6× vs. 2.6× productivity gap
- `mckinsey-3-objective-mix.md` — objective classification
- `accenture-redeployment-roi.md` — three-channel ROI model
- `stanford-51-deployments.md` — invisible-costs empirical backing

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
