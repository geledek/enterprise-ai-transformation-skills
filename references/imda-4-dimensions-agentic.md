---
title: IMDA — Four Dimensions of Agentic AI Governance
source-id: imda-agentic-ai-2026
wiki-page: (02_References/enterprise-ai/wiki/frameworks/four-dimensions-of-agentic-ai-governance.md)
last-synced: 2026-06-07
---

# IMDA — Four Dimensions of Agentic AI Governance

## What this reference contains

IMDA's Model AI Governance Framework (Agentic AI extension), 2026. The central governance model for responsible agentic AI deployment: four dimensions applied iteratively across the agent lifecycle.

## The four dimensions

| # | Dimension | Core question |
|---|---|---|
| 1 | **Assess and bound the risks upfront** | Is this use case suitable for an agent, and how do we limit its blast radius by design? |
| 2 | **Make humans meaningfully accountable** | Who is responsible for what, and how do we ensure human oversight remains effective at scale? |
| 3 | **Implement technical controls and processes** | How do we operationalize safety across the lifecycle? |
| 4 | **Enable end-user responsibility** | How do we equip the people who use or oversee agents to do so safely? |

Source: IMDA Agentic AI Framework 2026, p.13.

## Dimension details

**Dimension 1 — Assess and bound:**
- Score use case on risk factors (impact × likelihood)
- Set structural limits on tools, data, autonomy, and area of impact
- Issue agent identities and authorizations before deployment
- Avoid single all-powerful agents; restrict device installation in mission-critical contexts

**Dimension 2 — Human accountability:**
- Allocate responsibility across the agentic value chain (model devs, platform, deployer, users)
- Design human-approval checkpoints
- Audit override rates and response times (automation bias is a measurable risk)

**Dimension 3 — Technical controls:**
- Pre-deployment: structural controls (not prompt-layer only); agent-specific testing (task execution, policy adherence, tool calling, robustness)
- Post-deployment: gradual rollout, continuous monitoring, change management
- Tighten permissive defaults; dedicated agent credentials; log all actions

**Dimension 4 — End-user responsibility:**
- Transparency to users (capabilities, actions, escalation paths, data handling)
- Training on autonomous-agent risks
- Protect foundational skills and tradecraft from agent erosion

## Iterative principle

> "These four dimensions should be viewed as an iterative process. If an anomaly is detected during monitoring, organisations should re-evaluate the earlier dimensions." — IMDA 2026, p.13

## When to consult

- For skill `tech-agent-guardrail`: this IS the core content — the skill operationalizes all four dimensions as a structured assessment.
- For skill `tech-stack-diagnostic`: Dimension 3 (technical controls) maps to the oversight and ops layers of the stack.
- For skill `people-readiness-conversation`: Dimension 2 (human accountability) surfaces the governance-ownership gap in leadership teams.

## Source

IMDA Model AI Governance Framework (Agentic AI), 2026, pp.13–47. The four-dimension model, iterative principle, and worked examples including the OpenClaw case.
