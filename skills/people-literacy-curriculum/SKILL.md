---
name: people-literacy-curriculum
description: Use when designing AI literacy training, addressing workforce that "uses AI as a chatbot only", responding to EU AI Act Art. 4 mandatory literacy duty, building role-based AI upskilling, or fixing low-awareness symptoms across executives/managers/frontline. Phrases like "our employees only use AI as a chatbot", "we need an AI literacy program", "what does EU AI Act Art. 4 require us to train", "build a role-based AI curriculum", "how do we get older workers up to speed on AI", "design an AI training rollout" all trigger this skill. Builds a four-pattern mental-model taxonomy (chatbot / RAG / workflow / agent) crossed with role segments, then outputs a curriculum spec, EU AI Act Art. 4 compliance footprint, and 30-day rollout plan.
---

# People — Workforce AI Literacy Curriculum

Design a role-anchored AI literacy program that satisfies EU AI Act Art. 4 (mandatory literacy duty, in force since 2 Feb 2025) AND fixes the "chatbot-only" usage pattern that strands organizations on the wrong side of the MIT 95% GenAI divide.

Anchor: BCG 88/25 manager role-modeling — 88% of managers say role-modeling AI matters, only 25% do it visibly; weekly-AI-use rates jumped 55%→72% YoY in cohorts where managers used the tools themselves. Training without manager role-modeling is theatre.

---

## Step 1: Mental-Model Taxonomy

Core question: Do learners know which of the four AI patterns fits their problem — or are they defaulting to chatbot for everything?

The four canonical patterns. Every learner must distinguish them by capability, failure mode, and one example in their own job:

1. **Chatbot (single-turn / multi-turn LLM).** Capability: open-ended generation, summarization, brainstorming. Limit: no memory across sessions, no access to your data, hallucinates facts. Canonical example: "Draft a customer email from these bullets."
2. **RAG (retrieval-augmented).** Capability: grounded answers over your documents/policies/tickets. Limit: only as good as the corpus; cannot act. Canonical example: "Answer HR policy questions over the employee handbook."
3. **Workflow AI (deterministic chain / function-calling).** Capability: scripted multi-step automation with AI in specific nodes; predictable. Limit: brittle to off-path inputs. Canonical example: "Extract invoice fields → validate → post to ERP."
4. **Agent (autonomous, tool-using, planning).** Capability: decomposes goals, calls tools, iterates. Limit: blast radius; needs guardrails (*see `imda-4-dimensions-agentic.md`*). Canonical example: "Resolve this Tier-1 support ticket end-to-end."

Diagnostic for the cohort:
1. **Can each learner name which pattern they should use for a given task?** (Test with 5 job-anchored scenarios.)
2. **Do they know what each pattern cannot do?** (Hallucination, no-memory, no-grounding, no-tool — name the failure mode per pattern.)
3. **Is there a sanctioned example of each pattern already deployed internally?** (If not, training has nothing to anchor to — fix this before content design.)

Output:
PATTERN COVERAGE | FAILURE-MODE FLUENCY | INTERNAL ANCHOR EXAMPLES | TAXONOMY GAPS

---

## Step 2: Role Segmentation

Core question: Which segments need which depth — and where are the highest-leverage cohorts?

Five segments, each with distinct competency needs. Do not collapse into "all employees."

- **Executive (C-suite, BU heads).** Pain: capital allocation decisions, narrative-setting, vendor selection. Depth: pattern-recognition + ROI gates + governance posture; not prompt craft. *Consult `deloitte-cheerleader-to-champion.md`: 30% of orgs have champion-level execs; the rest under-invest.*
- **Manager (people leaders).** Pain: BCG 88/25 bottleneck — adoption stalls without manager modeling. Depth: must use AI weekly themselves AND coach team usage. Highest-leverage segment.
- **Knowledge Worker (analysts, engineers, marketers, ops).** Pain: chatbot-only usage; no awareness of RAG/workflow/agent. Depth: full taxonomy + hands-on + role-anchored exercises.
- **Frontline (sales, service, field).** Pain: in-flow tools matter more than classroom. Depth: pattern recognition for sanctioned tools only + escalation rules.
- **Risk-Compliance (legal, audit, infosec, HR).** Pain: must evaluate AI without using it. Depth: EU AI Act + NIST RMF literacy + redress mechanisms. *Consult `eu-ai-act-essentials.md` and `nist-rmf-functions.md`.*

Older-worker overlay: Stanford shows 16% headcount drop in 22-25yo with high AI exposure — older workers' job security depends on demonstrating AI fluency. Provide segment-blind extra office hours; do not create an "older worker track" (stigmatizing).

Output:
SEGMENT MAP | HIGHEST-LEVERAGE COHORT | OLDER-WORKER POSTURE | RISK-COMPLIANCE DEPTH

---

## Step 3: Competency Matrix

Core question: For each role × each pattern, what is must-know vs should-know vs could-know?

Build the 5×4 matrix. Per cell, label MUST / SHOULD / COULD and name the artifact that proves competency (a deliverable, not a quiz score).

| | Chatbot | RAG | Workflow | Agent |
|---|---|---|---|---|
| Executive | SHOULD | MUST | SHOULD | MUST |
| Manager | MUST | MUST | SHOULD | SHOULD |
| Knowledge Worker | MUST | MUST | SHOULD | COULD |
| Frontline | MUST (sanctioned tool only) | SHOULD | COULD | COULD |
| Risk-Compliance | MUST | MUST | MUST | MUST |

MUST = blocks role performance without it. SHOULD = needed within 6 months. COULD = enriching but not required.

Proof artifacts (not quizzes):
1. **Knowledge Worker MUST-Chatbot:** ship one sanctioned-tool output to a real stakeholder.
2. **Manager MUST-RAG:** demonstrate one team query answered against internal corpus.
3. **Risk-Compliance MUST-Agent:** complete one IMDA 4-dimension review (*see `imda-4-dimensions-agentic.md`*).
4. **Executive MUST-Agent:** sign one tech-buy-vs-build decision with explicit governance rationale.

*Consult `hiten-skill-library.md`: capture proof artifacts into a reusable skill library so each completion compounds organizational capability rather than evaporating.*

Output:
COMPETENCY MATRIX | PROOF ARTIFACTS | SKILL-LIBRARY HOOK | UNCOVERED CELLS

---

## Step 4: Delivery Architecture

Core question: What gets delivered as workshop, e-learning, sandbox, or in-flow tutorial — and how does manager modeling get hard-wired in?

Three delivery channels, each with a specific job:

- **Sanctioned sandbox (always-on).** A safe environment with sanctioned models + sample data + the four pattern templates pre-built. Suppresses shadow-AI by giving a better path. Track usage as the primary leading indicator.
- **Role-anchored exercises (workshop / cohort).** 90-minute live sessions per role × pattern, using the learner's actual job artifacts. Not generic prompt-engineering decks. Cohort size ≤15 for managers; ≤25 for knowledge workers.
- **In-flow tutorial (frontline + knowledge worker).** Embedded coaching in the sanctioned tool itself — "why this prompt failed", "try RAG instead", surfaced at the moment of use. Highest retention channel.

Manager role-modeling tie-in (BCG 88/25): managers are the multiplier. Hard-wire by:
1. **Manager-first sequencing.** Manager cohort completes 30 days before their team's rollout starts.
2. **Weekly visible-use ritual.** Each manager shares one AI-assisted artifact in team standup; absence is noticed.
3. **Manager metric.** Team's sanctioned-sandbox weekly active rate is on the manager's scorecard, not the learner's.

*Consult `bcg-manager-modeling.md`: without this, adoption ceiling is ~25%; with it, 72%+.*

Allocate budget by 70-20-10 (*see `70-20-10-value-split.md`*): 10% on the deck/e-learning content, 20% on cohort delivery + manager enablement, 70% on the sandbox + in-flow tutorials + integration with real workflows.

Output:
CHANNEL MIX | MANAGER-FIRST SEQUENCING | SANDBOX READINESS | 70-20-10 BUDGET SPLIT

---

## Step 5: Compliance & Measurement

Core question: What is the minimum-viable evidence to satisfy EU AI Act Art. 4, and what real metrics prove the program works?

EU AI Act Art. 4 minimum-viable evidence (*from `eu-ai-act-essentials.md`*):
- [ ] Documented training program tied to role × AI-system-exposure
- [ ] Completion records per individual interacting with AI systems
- [ ] Content covers: technical knowledge appropriate to role, awareness of opportunities and risks, possible harms
- [ ] Refresh cadence defined (annual minimum; on material system change)
- [ ] Provider-vs-deployer scope: as deployer, train staff who operate or are affected by the AI system
- [ ] Evidence retained for regulator inquiry

Note: Art. 4 has been in force since 2 Feb 2025; enforcement via national authorities from 2 Aug 2026. Non-compliance is not penalty-listed in Art. 99, but documented absence undermines defense in any incident.

Effectiveness metrics (lagging completion is not enough):

1. **Sandbox weekly active rate by role.** Target: 60%+ knowledge worker, 80%+ manager within 90 days.
2. **Pattern-fit accuracy.** When learners select a pattern for a new task, do they pick correctly? Measure via 5-scenario pulse quarterly.
3. **Applied-use artifacts.** Count of proof artifacts shipped per learner per quarter.
4. **Shadow-AI suppression.** Network/DLP signal of unsanctioned tool usage trending down — if not, the sanctioned path is worse than the shadow path; fix the sandbox.
5. **Redeployment outcome.** *Per `accenture-redeployment-roi.md`*: track learners who moved into AI-augmented roles vs attrition. Redeployment ROI is the program's true business case.

Diagnostic:
1. **Is completion >90% but sandbox usage <30%?** (Compliant-not-effective. Fix manager modeling and in-flow tutorials.)
2. **Is shadow-AI usage flat or rising?** (Sandbox is failing — content/access problem, not training problem.)
3. **Can you produce per-individual training evidence within 5 working days?** (If no, you fail Art. 4 on procedure regardless of content quality.)

Output:
ART. 4 EVIDENCE STATUS | SANDBOX ACTIVE RATE | PATTERN-FIT ACCURACY | SHADOW-AI TREND | REDEPLOYMENT COUNT

---

## Synthesis

Produce three artifacts:

**CURRICULUM SPEC.** The 5×4 competency matrix with MUST/SHOULD/COULD per cell, proof artifacts named, delivery channel assigned per cell, owner named per segment.

**COMPLIANCE FOOTPRINT.** Art. 4 evidence checklist with current status per item; gap list with named remediation owner and date; refresh cadence calendar; retention location.

**30-DAY ROLLOUT.** Day 1-7: manager cohort kickoff + sandbox stood up. Day 8-21: manager cohort completion + role-modeling ritual launched. Day 22-30: knowledge-worker wave 1 begins; in-flow tutorials live; first metrics pulse.

Verdict states:
- **Compliant-and-effective.** Art. 4 evidence complete AND sandbox active rate ≥60% AND pattern-fit accuracy ≥70% AND shadow-AI trending down. Continue; widen waves.
- **Compliant-not-effective.** Art. 4 evidence complete but usage/accuracy lagging. Fix manager modeling, sandbox UX, and in-flow tutorials before adding content.
- **Non-compliant.** Art. 4 evidence gaps remain. Halt new pattern rollout; close evidence gaps within 30 days; do not allow Risk-Compliance segment to start coverage assessments until their own training is documented.

---

## References

- eu-ai-act-essentials.md — Art. 4 mandatory literacy duty, scope, refresh, evidence requirements.
- bcg-manager-modeling.md — 88/25 finding; manager weekly use as the adoption multiplier.
- deloitte-cheerleader-to-champion.md — 30% champion-level executive sponsorship as ceiling on adoption.
- 70-20-10-value-split.md — budget allocation across content, delivery, and integration/sandbox.
- hiten-skill-library.md — capturing proof artifacts as reusable skills compounds capability.
- accenture-redeployment-roi.md — redeployment outcome is the true business case for literacy spend.
- imda-4-dimensions-agentic.md — agent-pattern competency anchor for Risk-Compliance and Executive segments.

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
