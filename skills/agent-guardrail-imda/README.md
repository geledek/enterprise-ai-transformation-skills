# Agent Guardrail (IMDA)

IMDA's four-dimension agentic AI governance check, adapted for enterprise deployment decisions.

## What it does

Assesses any AI agent deployment across four dimensions:
1. Assess and bound the risks upfront (suitability, blast radius, structural bounds)
2. Make humans meaningfully accountable (responsibility allocation, human-in-loop design)
3. Implement technical controls (pre-deployment testing, structural controls, logging)
4. Enable end-user responsibility (transparency, training, tradecraft protection)

Outputs a Governance Readiness Assessment: Deploy / Deploy-with-conditions / Do-not-deploy, with named gaps and required actions.

## When to use it

Before any AI agent goes live. Also use it at any scale boundary (10 users → 10,000 users requires re-assessment). Re-run if anomalies appear post-deployment.

## What it outputs

A structured governance readiness assessment with:
- Readiness verdict (Deploy / Deploy-with-conditions / Do-not-deploy)
- Gap list with required actions and named owners
- Critical gaps (any one = Do-not-deploy)
- Regulatory obligations triggered (EU AI Act, NIST RMF)

## Sources used

- `imda-4-dimensions-agentic.md` — IMDA four-dimension governance framework
- `eu-ai-act-essentials.md` — EU AI Act obligations
- `nist-rmf-functions.md` — NIST RMF GOVERN and MANAGE functions

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
