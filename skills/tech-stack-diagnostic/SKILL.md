---
name: tech-stack-diagnostic
description: Use when assessing an organization's AI technology infrastructure, diagnosing why AI pilots aren't scaling, evaluating technical readiness before a major AI investment, or identifying the weakest layer in the AI stack. Phrases like "diagnose our AI tech stack", "why isn't our AI scaling?", "assess our AI infrastructure", "where are we technically on AI?", "what are our biggest tech gaps for AI?", "review our AI architecture" all trigger this skill. Walks the full six-layer stack — data, model, orchestration, tools, oversight, operations — surfaces the weakest link, and outputs a prioritized remediation plan.
---

# Tech — AI Stack Diagnostic

Diagnose the full enterprise AI technology stack across six layers. The model is the smallest part of the problem. Data and orchestration are where most organizations are blocked.

Walk each layer. Score it. Surface the weakest link. A chain breaks where the weakest link breaks — and most chains break at data or orchestration, not at the model.

---

## Layer 1: Data Foundation

Core question: Is data AI-ready, or does it "should exist"?

Stanford AI Index 2026: data engineers and software engineers are tied as the most in-demand AI role. The limiting factor in enterprise AI is data pipeline readiness — not model access. For every $1 of visible tech investment, up to $10 is invisible — mostly data and change management.

Assess:
- **Existence:** Does the required data exist in a usable format? (Not "does it exist somewhere in the enterprise?")
- **Access:** Is there a data pipeline that delivers this data to AI systems in production? (Not just in a notebook)
- **Quality:** What are the null rates, duplicate rates, freshness, and provenance characteristics?
- **Rights:** Does the organization have confirmed legal rights to use this data for AI? (GDPR, training data rights, contractual restrictions)
- **Unity:** Is data unified across functions, or siloed in 50+ databases controlled by 50+ VPs? (The Ng Unified Data Warehouse prerequisite — consult `isg-data-foundation.md`)

Score: STRONG / ADEQUATE / GAP / BLOCKING
Note: if BLOCKING, nothing in layers 2–6 will compound. Fix this first.

Output:
DATA EXISTENCE | DATA ACCESS | DATA QUALITY | DATA RIGHTS | DATA UNITY | LAYER 1 SCORE

---

## Layer 2: Model Selection and Lifecycle

Core question: Is the model decision appropriate, and is there a management process?

Key framing: foundation models commoditize. The strategic question is orchestration, not which model to buy or train. Over-optimization of the model layer at the expense of layers 3–6 is the most common misallocation.

Assess:
- **Selection rationale:** Is the model selection based on empirical task evaluation, or vendor marketing?
- **Buy vs. build:** Is the organization buying foundation model capability or trying to train its own? (NANDA 2:1 buy advantage — consult `nanda-tech-buy-vs-build.md`)
- **Model lifecycle:** Is there a process for model updates, version control, and performance tracking?
- **Abstraction:** Is there a model abstraction layer, so the application layer can switch models without rearchitecting?

Score: STRONG / ADEQUATE / GAP / BLOCKING

Output:
MODEL SELECTION | BUILD-VS-BUY POSTURE | MODEL LIFECYCLE | ABSTRACTION LAYER | LAYER 2 SCORE

---

## Layer 3: Orchestration

Core question: Does an orchestration layer exist, and is it the moat-building investment?

This is the most strategically important layer for GenAI. The orchestration layer — model routing, agent coordination, model abstraction, tool integration, self-service consumption — is where the moat lives. It compounds as the organization operates.

Reference: European energy company with Accenture AI core: 5 months to ship AI apps vs. 18 months before. The orchestration layer was the difference. (Consult `accenture-redeployment-roi.md`)

Assess:
- **Routing:** Can the system route tasks to the appropriate model or agent based on task type?
- **Agent coordination:** If multiple agents are used — is there a coordination mechanism?
- **Self-service consumption:** Can business users consume AI capabilities without engineering support for each new use case?
- **Tool integration:** Is the orchestration layer connected to the tools and systems where work actually happens?
- **Reuse:** Are AI capabilities built for reuse (MIT CISR Stage 3 requirement) or rebuilt for each new project?

Score: STRONG / ADEQUATE / GAP / BLOCKING

Output:
ROUTING | AGENT COORDINATION | SELF-SERVICE | TOOL INTEGRATION | REUSE ARCHITECTURE | LAYER 3 SCORE

---

## Layer 4: Tools and Applications

Core question: Is the tool landscape coherent and integrated, or fragmented and shadow-IT-heavy?

Assess:
- **Fragmentation:** How many separate AI tools/point solutions exist? Is there a shared consumption layer?
- **Shadow AI:** Are employees using unauthorized AI tools? Is there a sanctioned alternative?
- **Integration:** Are AI tools connected to the systems of record where decisions are made?
- **User experience:** Do end users adopt the tools voluntarily, or is adoption forced?

Score: STRONG / ADEQUATE / GAP / BLOCKING

Output:
TOOL FRAGMENTATION | SHADOW AI RISK | INTEGRATION STATUS | ADOPTION STATUS | LAYER 4 SCORE

---

## Layer 5: Oversight and Governance

Core question: Is AI behavior visible post-deployment, and are accountability mechanisms active?

NIST RMF MANAGE: every AI system needs a documented path for monitoring, override, and decommissioning. An AI system with no post-deployment visibility is unmanaged, not managed. (Consult `nist-rmf-functions.md`)

Assess:
- **Visibility:** Are AI system behaviors observable via dashboards or monitoring? (MIT CISR Stage 3 requirement)
- **Alert thresholds:** Are there defined thresholds that trigger human review?
- **Accountability:** Is there a named human accountable for each AI system in production?
- **Override:** Can humans override AI outputs at every consequential decision point?
- **Audit trail:** Are AI decisions logged with enough context for post-hoc review?

Score: STRONG / ADEQUATE / GAP / BLOCKING

Output:
VISIBILITY | ALERT THRESHOLDS | ACCOUNTABILITY | OVERRIDE CAPABILITY | AUDIT TRAIL | LAYER 5 SCORE

---

## Layer 6: Operations and Lifecycle

Core question: Is the AI system treated as a living system with a managed lifecycle, or as a shipped artifact?

Assess:
- **Model drift:** Is there a monitoring process for when model performance degrades?
- **Retraining triggers:** Are retraining triggers defined (data drift, performance decline, distribution shift)?
- **Version management:** Are model versions tracked and rollback possible?
- **Incident response:** Is there an AI-specific incident response process?
- **Decommissioning:** Is there a documented path for decommissioning AI systems when they're no longer appropriate? (NIST MANAGE 2.4 — every AI system needs an "off" path)

Score: STRONG / ADEQUATE / GAP / BLOCKING

Output:
DRIFT MONITORING | RETRAINING TRIGGERS | VERSION MANAGEMENT | INCIDENT RESPONSE | DECOMMISSIONING PLAN | LAYER 6 SCORE

---

## Stack Synthesis

Aggregate the six-layer assessment. Surface the weakest link.

STACK SCORECARD:
- Layer 1 (Data): [Score]
- Layer 2 (Model): [Score]
- Layer 3 (Orchestration): [Score]
- Layer 4 (Tools): [Score]
- Layer 5 (Oversight): [Score]
- Layer 6 (Operations): [Score]

WEAKEST LINK: [Name the layer; explain why it is blocking]

MATURITY STAGE IMPLICATION (consult `mit-cisr-4-stages.md`):
- Layers 1–2 adequate, 3–6 absent → Stage 2 (pilots working, not scaling)
- Layers 1–3 strong → Stage 3 (platform exists, architectural reuse present)
- All six layers strong → Stage 3–4 (industrialized AI, approaching continuous innovation)

REMEDIATION PRIORITIES:
For each GAP or BLOCKING layer, state:
1. The specific gap (one sentence)
2. The required action (specific)
3. The estimated effort (weeks / months)
4. The dependency (does fixing this unblock another layer?)

Output:
STACK SCORECARD | WEAKEST LINK | MATURITY STAGE IMPLICATION | REMEDIATION PRIORITIES (ordered)

---

## References

*All files below live in `references/` at the plugin root (`${CLAUDE_PLUGIN_ROOT}/references/` when installed as a plugin).*

- `ai-stack-layers.md` — the six-layer framework reference
- `nanda-tech-buy-vs-build.md` — 2:1 buy advantage; orchestration-as-moat
- `accenture-redeployment-roi.md` — AI core case study (5 vs. 18 months)
- `mit-cisr-4-stages.md` — Stage 3 platform requirements
- `nist-rmf-functions.md` — GOVERN, MEASURE, MANAGE lifecycle functions
- `isg-data-foundation.md` — data foundation requirements; data as binding constraint

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
