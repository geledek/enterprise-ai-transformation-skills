---
title: NIST AI RMF — Govern / Map / Measure / Manage
source-id: nist-ai-rmf
wiki-page: (02_References/enterprise-ai/wiki/frameworks/nist-ai-rmf-core.md)
last-synced: 2026-06-07
---

# NIST AI RMF — Four Functions

## What this reference contains

NIST AI Risk Management Framework (AI 100-1). The U.S. consensus standard for enterprise AI risk governance. Four functions — GOVERN, MAP, MEASURE, MANAGE — 19 categories, 72 subcategories. Referenced by the EU AI Act conformity-assessment community, the OECD, and most enterprise risk frameworks.

## The four functions

| Function | One-line outcome | When it applies |
|---|---|---|
| **GOVERN** | "A culture of risk management is cultivated and present." | Cross-cutting — infused throughout the other three |
| **MAP** | "Context is recognized and risks related to context are identified." | Entry point — contextual understanding before measurement |
| **MEASURE** | "Identified risks are assessed, analyzed, or tracked." | After MAP — produces the evidence base |
| **MANAGE** | "Risks are prioritized and acted upon based on a projected impact." | Ongoing — allocates response resources |

Source: NIST AI 100-1, p.20.

## Key subcategories for enterprise deployers

- **GOVERN 1.1** — policies, processes, and practices for AI risk are documented, transparent, and effective
- **GOVERN 1.6** — AI system inventory (most enterprise sources omit this as a first-class artifact)
- **GOVERN 2.3** — executive responsibility for AI deployment decisions (not delegable to data science or legal alone)
- **MAP 3.5** — human oversight processes defined pre-deployment
- **MANAGE 1.1** — explicit go/no-go decision on whether deployment should proceed
- **MANAGE 2.4** — supersede/disengage/deactivate capability — every AI system needs a documented "off" path
- **MANAGE 4.1** — post-deployment monitoring including override, decommissioning, incident response

## How it applies iteratively

MAP outputs feed MEASURE, MEASURE outputs feed MANAGE, MANAGE outcomes loop back to MAP. The RMF is not a waterfall — it is a governance operating cycle.

## When to consult

- For skill `agent-guardrail-imda`: NIST RMF GOVERN and MANAGE functions map against IMDA Dimensions 2 and 3 — use both together.
- For skill `stack-diagnostic`: the MEASURE and MANAGE functions define what ongoing stack oversight looks like post-deployment.

## Source

NIST AI Risk Management Framework 1.0 (AI 100-1) + AI RMF Playbook. U.S. standard for managing AI risk; 19 categories, 72 subcategories.
