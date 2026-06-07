---
title: ISG + Stanford — AI Data Foundation Requirements
source-id: (multi-source: isg-genai-2025, stanford-playbook-2026)
wiki-page: (02_References/enterprise-ai/wiki/skills/technology/build-data-foundation-for-ai.md)
last-synced: 2026-06-07
---

# AI Data Foundation Requirements

## What this reference contains

Cross-source synthesis on what "data readiness" actually means for enterprise AI deployment. ISG GenAI Enterprise Research 2025 and Stanford AI Index 2026 converge on the same finding: data infrastructure is the binding constraint in most enterprise AI deployments — not model capability.

## Key claims (with citations)

- **Data engineers are the most in-demand AI role** — tied with software engineers. The limiting factor in enterprise AI is not model access; it is data pipeline readiness. Source: Stanford AI Index 2026.
- **"Should exist" data is not pipeline-ready data.** Most pilots fail at scale not because the data doesn't exist in the enterprise, but because it isn't accessible, clean, or correctly structured for AI consumption. Source: ISG + Stanford synthesis.
- **Three data readiness questions for any AI initiative:**
  1. Does the required data exist in a usable format? (Not "does it exist?")
  2. Does the organization have confirmed legal rights to use it for AI? (Training data, GDPR, contractual restrictions)
  3. Is there a data pipeline that can deliver this data to the AI system in production? (Not just in a notebook)
- **50 siloed databases = AI paralysis.** "If you have 50 different databases siloed under the control of 50 different VPs, it will be nearly impossible for an engineer or AI software to get access to this data." Source: Landing AI Playbook (Andrew Ng).
- **Data quality investment returns more than model investment for most organizations.** Improving data quality and access has higher marginal returns than switching foundation models. Source: ISG GenAI 2025.
- **ISG three foundations for AI value:** (1) data foundation, (2) governance foundation, (3) talent foundation. Data is listed first because it blocks the other two. Source: ISG GenAI Enterprise Research 2025.

## Data readiness checklist

For any AI initiative, assess:
- [ ] Data exists in a usable format (structured, accessible, not locked in PDFs or proprietary formats)
- [ ] Legal rights confirmed (data usage agreements, privacy compliance, training data rights)
- [ ] Pipeline exists or can be built within pilot scope
- [ ] Data quality baseline measured (null rates, duplicate rates, freshness)
- [ ] Single source of truth identified (or explicitly noted as a gap)

## When to consult

- For skill `stack-diagnostic`: Layer 1 (Data) assessment — the checklist above is the starting point for the data layer.
- For skill `ai-idea-diagnostic`: Q4 (Right Capability?) includes data readiness as a first-class capability question.
- For skill `pilot-design`: data readiness must be confirmed before pilot design — a pilot on unpipeline-ready data is not a pilot, it's a data engineering project.

## Source

ISG GenAI Enterprise Research 2025 (three foundations; data as binding constraint). Stanford AI Index 2026 (data engineer demand; invisible costs). Landing AI Playbook (data unification prerequisite).
