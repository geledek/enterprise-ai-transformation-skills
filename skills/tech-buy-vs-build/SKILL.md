---
name: tech-buy-vs-build
description: Use when deciding whether to build AI capability in-house, buy it from a vendor, or partner for it. Phrases like "should we build or buy this AI?", "should we train our own model or use an API?", "which vendor should we use for AI?", "help me decide on the AI sourcing strategy", "we're choosing between building vs. buying AI — which is right?" all trigger this skill. Applies the NANDA 2:1 evidence and vendor-archetype taxonomy to produce a BUILD / BUY / PARTNER recommendation with investment rationale.
---

# Tech — Buy vs. Build (AI Sourcing)

Decide whether to build AI capability in-house, buy from a vendor, or partner. Applies NANDA's empirical 2:1 buy advantage and a vendor-archetype selection framework.

The principle: **Buy the model. Build the orchestration.** Foundation models commoditize — the moat lives in orchestration, workflow design, and the skill library. (Consult `nanda-tech-buy-vs-build.md` and `andrew-ng-three-moats.md`.)

---

## Role 1: Map the Decision

Not all AI investment is the same decision. First, classify what is being sourced.

COMPONENT CLASSIFICATION — for each component being decided, classify:
- **Foundation model capability** (GPT-level reasoning, multimodal, code generation) → almost always BUY
- **Orchestration / workflow automation** → BUILD for the parts that encode your processes; BUY platforms where commodity works
- **Fine-tuned or domain-specific model** → BUILD (on top of a bought base) only if the domain is genuinely proprietary
- **End-user application / interface** → often BUY (SaaS or API), with customization built in-house
- **Data infrastructure** → BUILD (it is company-specific; no vendor can own your data strategy)
- **Skill library / process knowledge** → BUILD (this is the moat — consult `hiten-skill-library.md`)

Output a component map: for each component, state the type and initial BUY/BUILD instinct before analysis.

Output:
COMPONENT | TYPE | INITIAL INSTINCT

---

## Role 2: The 2:1 Evidence Test

MIT NANDA 2025 finding: firms that buy AI capability vs. build it internally are 2× more likely to capture value. (Consult `95-5-genai-divide.md`)

For each BUY candidate, confirm the buy rationale holds:
1. **Does an existing vendor solution cover ≥80% of the use case?** If no: buying may not solve the problem.
2. **Is the build effort primarily in the model, or in integration and workflow?** If model: buy. If integration/workflow: that's a build regardless.
3. **Is the value in having this model, or in what you do with it?** If value is in the doing: buying the model is the input, not the output.
4. **Is this a commodity capability or a differentiating capability?** Commodity = buy. Differentiating = evaluate carefully.

For each BUILD candidate, confirm the build rationale holds:
1. **Is this component genuinely proprietary?** (Your company's data, your company's processes, your company's domain logic)
2. **Would a vendor solution expose competitive IP?**
3. **Is this the orchestration/workflow/skill layer?** (Yes = valid build candidate)
4. **Is the build timeline realistic for a 90-day pilot?** (If not: buy something that works and build the proprietary layer later)

Output:
COMPONENT | BUY/BUILD VERDICT | RATIONALE

---

## Role 3: Vendor Archetype Selection

For BUY decisions, the wrong vendor archetype is as costly as the wrong build/buy direction. Three archetypes; most organizations need more than one.

**Full-stack platform** (e.g., Azure AI, AWS Bedrock, Google Vertex):
- Best for: organizations wanting a single vendor relationship, infrastructure-level AI platform
- Risk: lock-in; customization is bounded by vendor platform decisions
- Use when: you need infrastructure + model + developer tooling from one place

**Specialist API provider** (e.g., Anthropic, OpenAI, specialized vertical AI APIs):
- Best for: specific capability needs (coding, reasoning, vision, domain-specific)
- Risk: model changes upstream; API versioning; multiple vendors to manage
- Use when: you need best-in-class capability for a specific task type, not a platform

**Systems integrator / implementation partner**:
- Best for: organizations that lack the internal capability to integrate AI into their operational workflows
- Risk: dependency; IP created in the engagement may belong to the vendor
- Use when: the integration challenge is greater than the AI capability challenge

For each component:
- State the vendor archetype that fits
- Name 1–2 candidate vendors
- Name the key evaluation criteria for this component

Output:
COMPONENT | VENDOR ARCHETYPE | CANDIDATE VENDORS | EVALUATION CRITERIA

---

## Role 4: Investment Verdict

Synthesize Roles 1–3 into a sourcing strategy.

**SOURCING STRATEGY SUMMARY:**

For each component:
- BUY (which archetype, which vendors to evaluate)
- BUILD (what specifically, what the build produces, why it is proprietary)
- PARTNER (what the partner provides, what the org retains)

**MOAT ASSESSMENT:**
Which layer of this sourcing strategy builds toward a defensible moat? (Consult `andrew-ng-three-moats.md`)
- The model is not the moat
- The orchestration + workflow + skill library is the moat
- Confirm that the BUILD investments are in moat-building components

**RISK FLAGS:**
- Is any BUILD investment in a component that a vendor can replicate cheaply? (Flag as misallocated)
- Is any BUY creating lock-in in a strategically critical layer? (Flag as risk)
- Is the build timeline and capability present for the BUILD components? (Flag any gaps)

Output:
SOURCING STRATEGY | MOAT ASSESSMENT | RISK FLAGS | RECOMMENDED NEXT ACTION

---

## References

- `nanda-tech-buy-vs-build.md` — 2:1 buy advantage; orchestration as moat; vendor archetypes
- `95-5-genai-divide.md` — empirical basis for buy advantage
- `andrew-ng-three-moats.md` — moat types; "buy the model, build the orchestration" principle
- `hiten-skill-library.md` — skill library as the BUILD layer that compounds
- `ai-stack-layers.md` — which stack layers are buy vs. build candidates

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
