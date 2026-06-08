---
name: agent-guardrail-imda
description: Use when deploying an AI agent, reviewing agentic AI governance, checking whether an AI agent deployment is safe and well-governed, or assessing whether an organization's oversight of autonomous AI systems is adequate. Phrases like "check the governance on this agent deployment", "is our agentic AI safe to deploy?", "review guardrails for this AI agent", "we're about to launch an AI agent — what do we need to have in place?", "help me assess our agentic AI oversight" all trigger this skill. Runs IMDA's four-dimension agentic governance check across risk bounding, human accountability, technical controls, and end-user responsibility. Outputs a governance readiness assessment with gaps and required actions.
---

# Agentic AI Governance Check (IMDA)

A four-dimension governance assessment for any AI agent deployment. Runs IMDA's Model AI Governance Framework (Agentic AI, 2026) iteratively across the agent lifecycle.

The framework is iterative — not a one-time gate. If anomalies appear in monitoring (Dimension 3), re-run Dimensions 1 and 2.

---

## Dimension 1: Assess and Bound the Risks Upfront

Core question: Is this use case suitable for an agent, and how do we limit its blast radius by design?

SUITABILITY CHECK:
- What is the intended scope of the agent's actions? (Tasks it can take, data it can access, systems it can touch)
- What is the blast radius if the agent takes an unintended action? (Internal-only / operational / customer-facing / regulatory)
- Is this use case suitable for autonomous operation, or does it require a human decision-maker in the loop?

RISK SCORING:
For each of the following risk dimensions, rate LOW / MEDIUM / HIGH:
- **Impact** — what is the worst-case consequence of an agent error?
- **Likelihood** — how often could errors occur given current controls?
- **Recovery** — how quickly and completely can an error be reversed?

STRUCTURAL BOUNDS:
Agents must be bounded by design, not by prompt. Identify:
- Which tools does this agent have access to? (Should it have access to all of them, or should access be scoped narrower?)
- What data can it read? What data can it modify?
- Does it operate with a single all-powerful agent pattern? (Red flag — avoid; use scoped agents instead)
- What authorizations and identity credentials are issued for this agent?

Output:
SUITABILITY | RISK SCORES (impact/likelihood/recovery) | STRUCTURAL BOUNDS | AGENT IDENTITY STATUS

---

## Dimension 2: Make Humans Meaningfully Accountable

Core question: Who is responsible for what, and how do we ensure human oversight remains effective at scale?

RESPONSIBILITY ALLOCATION across the agentic value chain:
- **Model developer:** has this foundation model been assessed for the intended use case?
- **Platform/tooling provider:** what guarantees does the platform provide on safety and performance?
- **Deployer (this organization):** who specifically owns the deployment decision? Who is the named accountable individual?
- **Users:** what is expected of users who interact with or oversee the agent?

WITHIN-ORGANIZATION ACCOUNTABILITY:
- Who made the deployment decision? (Named person — not a team)
- Who monitors agent behavior post-deployment?
- Who has authority to pause or shut down the agent?
- Who reviews override rates and escalation patterns?

HUMAN-IN-LOOP DESIGN:
For each consequential action type the agent can take, state whether:
- Human approval is required before the action (pre-approval)
- Human review is required after the action (post-review)
- The action is fully autonomous with monitoring only (name the monitoring mechanism)

AUTOMATION BIAS CHECK:
If humans are in the loop, are they actually reviewing — or rubber-stamping? Name the mechanism for auditing override rates and response times.

Output:
RESPONSIBILITY MAP | NAMED ACCOUNTABLE INDIVIDUAL | HUMAN-IN-LOOP DESIGN | AUTOMATION BIAS RISK

---

## Dimension 3: Technical Controls and Processes

Core question: How do we operationalize safety across the lifecycle?

PRE-DEPLOYMENT TESTING — confirm each is complete:
- [ ] Task execution testing (does the agent do what it's supposed to?)
- [ ] Policy adherence testing (does it stay within its authorized scope?)
- [ ] Tool-calling correctness (are external tool calls accurate and bounded?)
- [ ] Robustness testing (does it handle edge cases, adversarial inputs, unexpected states?)
- [ ] Multi-agent interaction testing (if it operates within a multi-agent system: what are the interaction failure modes?)

STRUCTURAL CONTROLS (not prompt-layer only):
- Are guardrails structural (architecture, authorization, API scope) or prompt-based only?
- Prompt-layer controls alone are insufficient — flag if structural controls are absent.
- Are permissive defaults tightened? (Default should be minimum-necessary access, not maximum access)

POST-DEPLOYMENT OPERATIONS:
- Gradual rollout plan (start narrow, monitor, expand — not big-bang deployment)
- Continuous monitoring: what anomaly detection exists?
- All agent actions logged? (Yes/No — No is a red flag)
- Change management process for agent updates

Output:
PRE-DEPLOYMENT TEST STATUS | STRUCTURAL CONTROLS ASSESSMENT | POST-DEPLOYMENT OPERATIONS PLAN | LOGGING STATUS

---

## Dimension 4: End-User Responsibility

Core question: How do we equip the people who use or oversee agents to do so safely?

USER TRANSPARENCY:
Does the end user know:
- What capabilities this agent has?
- What range of actions it can take?
- How to escalate to a human?
- How their data is handled?

TRAINING AND EDUCATION:
- Have users and oversight personnel been trained on autonomous-agent risks?
- Is the training specific to THIS agent's capabilities and failure modes, or generic?

TRADECRAFT PROTECTION:
- Does this agent automate tasks that require foundational skills to be maintained by human operators?
- If yes: what is the plan to protect those skills from erosion?
  (Example: if an agent automates document review, do human reviewers still maintain the ability to review without the agent?)

Output:
USER TRANSPARENCY STATUS | TRAINING COMPLETENESS | TRADECRAFT RISK

---

## Synthesis: Governance Readiness Assessment

Consolidate Dimensions 1–4. Write for deployment decision-maker.

READINESS VERDICT: [Deploy / Deploy-with-conditions / Do-not-deploy-until-gaps-addressed]

For each gap found:
- State the gap in one sentence
- State the required action (specific, not general)
- State the accountable owner for the action

CRITICAL GAPS (any one of these = Do-not-deploy):
- No named accountable individual (Dimension 2)
- No structural controls — prompt-layer only (Dimension 3)
- No agent action logging (Dimension 3)
- Agent operates in customer-facing or regulatory-consequence context without human-in-loop (Dimension 2)
- Pre-deployment testing incomplete for consequential action types (Dimension 3)

REGULATORY CONTEXT:
- EU AI Act (Art. 4): if deploying in EU context, AI literacy obligation applies to all users
- EU AI Act (Art. 26): if this is a high-risk system, named human oversight is legally required
- NIST RMF MANAGE: every AI system needs a documented "off" path (MANAGE 2.4)
(Consult `eu-ai-act-essentials.md` and `nist-rmf-functions.md` for detailed obligations.)

Output:
READINESS VERDICT | GAPS LIST | CRITICAL GAPS | REGULATORY OBLIGATIONS TRIGGERED

---

## References

- `imda-4-dimensions-agentic.md` — the four-dimension governance framework (IMDA 2026)
- `eu-ai-act-essentials.md` — Art. 4 literacy obligation; Art. 26 deployer obligations; risk tiers
- `nist-rmf-functions.md` — GOVERN, MANAGE functions; MANAGE 2.4 (off-path requirement)
- `pwc-roi-2026-governance.md` — 1.7× AI leadership advantage for documented RAI strategy

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
