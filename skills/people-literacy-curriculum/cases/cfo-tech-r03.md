---
case: cfo-tech-r03
participant: r03 (CFO, mid-cap tech, ~1,200 FTE, DE + SG entities)
skill: people-literacy-curriculum
verdict: Compliant-not-effective (current state) -> Compliant-and-effective (post-rollout)
---

# CFO at a 1,200-Person Tech Mid-Cap: Turning a Chatbot Workforce into a Pattern-Literate One

> "AI literacy level is still low... many people are still using AI as a chatbot. Lack of understanding of various AI tools." — r03, CFO

One-line summary: The CFO has bought the tools (M365 Copilot enterprise + three function-specific SaaS) but the workforce only knows one mental model — "chatbot." EU AI Act Art. 4 is in force at the German subsidiary. Engineering is on consumer ChatGPT. The curriculum below replaces "AI training" (single generic e-learning) with a pattern-literacy + role-anchored architecture.

## Persona / Setup

- **Company**: Listed mid-cap tech firm, HQ Singapore, regulated EU subsidiary in Munich (~340 FTE), commercial entities in UK, US, AU.
- **Workforce**: 1,200 FTE. ~280 engineers, ~190 sales, ~140 G&A (incl. 22 finance, 14 legal/compliance), ~210 customer success/support, ~180 product/design/marketing, ~200 operations/frontline ops.
- **Existing AI estate**:
  - M365 Copilot enterprise (847 licences activated, ~31% weekly active)
  - Gong (revenue intelligence, sales)
  - Harvey-style legal copilot pilot (8 seats, legal)
  - GitHub Copilot (engineering, 240 seats)
  - Sanctioned ChatGPT Enterprise — *purchased but not yet rolled out*
- **Shadow AI**: Internal survey from r03's CISO peer flagged ~38% of engineers admit to pasting code into consumer ChatGPT/Claude.ai accounts. Three confirmed instances of customer data in prompts (Q1).
- **Compliance trigger**: EU AI Act Art. 4 ("AI literacy") obligation in force since 2 Feb 2025. Munich entity in scope. Internal audit flagged "no documented literacy program" as an open finding for FY26 audit.
- **CFO's stated frustration** (paraphrased from r03 survey response): the company has spent ~€2.1M on AI tooling and licences in 18 months but "decision quality hasn't moved, and I can't tell if Copilot is doing anything other than writing nicer emails."

The brief to the curriculum team: design something Art. 4-defensible, role-differentiated, and capable of moving the workforce off "AI = chatbot" within one quarter.

---

## Applying people-literacy-curriculum

### Step 1 — Mental-Model Taxonomy

The diagnostic survey (n=420 across r03's company) confirmed r03's hypothesis: 71% of respondents named "ChatGPT" or "Copilot chat" when asked to describe how they use AI at work. Only 9% could distinguish a RAG-grounded assistant from a generic chatbot. 3% could articulate what makes something an "agent." This is the literacy gap the curriculum has to close.

Four patterns, with one canonical in-house example per pattern so the abstraction sticks:

| # | Pattern | What it can do | What it cannot do | Canonical example at r03's company |
|---|---------|----------------|-------------------|------------------------------------|
| 1 | **Chatbot** (parametric LLM, no grounding) | Open-ended generation, brainstorming, rewriting, generic Q&A | Cite internal facts reliably; act on systems; remember beyond a session | M365 Copilot Chat with web grounding off — drafting an email to a customer |
| 2 | **RAG** (retrieval-augmented over a known corpus) | Answer questions grounded in *your* documents with citations; reduce hallucination on factual queries | Reason across many documents; do multi-step planning; act in systems | Copilot for Microsoft 365 grounded in SharePoint — "what was the renewal value of Acme last cycle?" |
| 3 | **Workflow** (deterministic pipeline with LLM as one step) | Reliably execute a known process with LLM-powered judgment at specific nodes; auditable | Handle novel cases outside the designed flow | Gong's deal-risk scoring pipeline → Salesforce field update → Slack alert |
| 4 | **Agent** (autonomous loop with tool use, planning, memory) | Decompose goals, call tools, iterate, recover from errors; high-leverage for novel multi-step work | Be trusted without scoped authority, eval harness, and human checkpoints; predictable cost | A scoped CS-triage agent that reads a ticket, queries Zendesk + product DB, drafts a response, and routes to L2 if confidence < threshold — *not yet deployed at r03's company* |

Design implication: every module in the curriculum opens with "which of the four are we using right now, and why?" — the taxonomy is the spine, not an appendix.

### Step 2 — Role Segmentation

Five segments, each with a different *job-to-be-done* against AI. The CFO's instinct ("just train everyone the same way") is the trap; r03 had been quoted €180k for a generic vendor e-learning that would have produced the same chatbot-shaped workforce, just certified.

| Segment | Headcount | Primary literacy need | What good looks like |
|---|---|---|---|
| **Executive** (ExCo + VPs, ~35) | 35 | Pattern-fluency for capital allocation; risk posture; vendor due diligence | Can read an AI vendor pitch and ask "is this RAG, workflow, or agent? what's your eval set?" |
| **Manager** (people leaders, ~140) | 140 | Role-modeling AI use; coaching ICs; redesigning team rituals around AI | Visibly uses AI in 1:1s, planning, reviews; sets team-level adoption norms (BCG 88/25 lever) |
| **Knowledge Worker / IC** (product, marketing, CS, ops analysts, ~510) | 510 | Tool selection per task; prompt hygiene; verification habit | Picks the right of 4 patterns for the task; cites sources; doesn't paste customer PII |
| **Specialist — Finance** (~22) and **Legal/Compliance** (~14) | 36 | Domain-specific risk: hallucination in numbers; privilege; Art. 4/5 obligations | Knows which finance tasks are RAG-safe vs. chatbot-only; legal knows what *cannot* go to a US-hosted model |
| **Specialist — Engineering** (~280) | 280 | Secure tool use; pattern-level architecture literacy; shadow-AI suppression | Uses sanctioned GitHub Copilot + ChatGPT Enterprise only; understands when to build agent vs. workflow |
| **Frontline / Ops** (support T1, ops, ~200) | 200 | In-flow assistance with tight guardrails | Uses pre-approved RAG assistants in Zendesk/ServiceNow; escalates novel cases |

The CFO himself is in segment 1 (Executive). His role-modeling is a leverage point we explicitly design for in Step 4 — the BCG 2024 *AI at Work* finding that frontline adoption is 88% in firms with leader role-modeling vs. 25% without is the single biggest reason the existing 31% Copilot WAU has not moved in six months.

### Step 3 — Competency Matrix (Role × Pattern)

Each cell: **M** = must-know (assessed), **S** = should-know (taught, not assessed), **C** = could-know (optional deep-dive).

| Role \ Pattern | Chatbot | RAG | Workflow | Agent |
|---|---|---|---|---|
| Executive | M | M | M | M |
| Manager | M | M | S | S |
| Knowledge Worker (IC) | M | M | S | C |
| Finance specialist | M | M | M (own pipelines) | S |
| Legal/Compliance | M | M | M | M (Art. 5 risk) |
| Engineering | M | M | M | M (they build them) |
| Frontline/Ops | M | S (use only) | C | C |

Concrete example of what "must-know RAG" means for a finance IC at r03's company: given a Copilot-grounded query against the SharePoint finance library, can the analyst (a) confirm which document the answer cites, (b) detect when the citation doesn't actually support the claim, and (c) know that *unstructured* commentary in a deck is a worse RAG source than a *structured* tagged data room. That's a 25-minute exercise, not a slide.

### Step 4 — Delivery Architecture

Three mandatory modules, role-anchored exercises, and a single sanctioned sandbox.

**Sanctioned Sandbox**: ChatGPT Enterprise tenant (already procured, not rolled out). Configured with:
- SSO-bound, no consumer fallthrough
- Custom GPTs pre-built per role (Finance-RAG-GPT, Legal-Privilege-Aware-GPT, Eng-Code-GPT)
- DLP scanning on inputs (Microsoft Purview integration)
- Activity logged for Art. 4 evidence
- Explicitly badged in the UI: "this is a *chatbot* — for grounded answers, use Copilot in M365"

This addresses the engineering shadow-AI directly: the consumer ChatGPT block goes in at the firewall *the same week* the sanctioned sandbox opens, with a 14-day amnesty/migration window. Suppression without substitution always fails.

**Three mandatory modules** (every FTE, 90 minutes total, Art. 4 evidence):

1. **M1: The Four Patterns** (30 min, e-learning, all roles)
   - The taxonomy from Step 1, with the four canonical in-house examples
   - Embedded 6-question check (must-pass, 5/6) — this is the Art. 4 minimum-viable evidence anchor
   - Includes the EU AI Act Art. 5 prohibited practices in plain language

2. **M2: Pattern-to-Task Selection** (30 min, role-branched e-learning)
   - Branch per segment; each branch presents 8 real tasks from that role and asks: chatbot, RAG, workflow, or agent?
   - Finance branch built around month-end close tasks; legal around contract review; engineering around code review and incident response
   - Worked examples; no certification theatre

3. **M3: Verification, Privacy, and Escalation** (30 min, all roles)
   - Hallucination detection drills (3 examples where the model confidently lies, including one numerical)
   - PII/IP gates: what cannot leave the tenant; the customer-data-in-prompts incidents from Q1, anonymised, used as cases
   - When to escalate to legal/security
   - "If in doubt, don't paste" — and how to use the sandbox correctly instead

**Role-anchored workshops** (segments 1-2, mandatory; segments 3-6, opt-in by manager assignment):

- **Executive workshop** (half-day, 35 attendees, two cohorts): pattern-fluency for capital allocation. CFO co-facilitates the "is this RAG or agent?" vendor pitch teardown. Output: each exec commits to one AI ritual they will visibly perform in their org for the next 90 days.
- **Manager workshop** (3 hours, 140 managers, six cohorts): the **BCG 88/25 role-modeling tie-in is the central frame**. Managers leave with three concrete role-modeling behaviours: (a) start one weekly 1:1 by sharing a Copilot/sandbox use from that week, (b) require AI-augmented drafts in two specific recurring deliverables, (c) include "AI use" as a standing agenda item in monthly team retros. Adoption telemetry is shared back to managers monthly.

**In-flow tutorials**: for sales (Gong) and engineering (GitHub Copilot), 5-minute task-specific micro-lessons triggered the first time a user touches a feature. Built once, lives in the tool.

**Format split**:
- Workshop (synchronous, instructor-led): Executive, Manager, plus engineering "agent architecture" deep-dive
- E-learning: M1, M2, M3 for everyone
- In-flow tutorial: Gong, GitHub Copilot, Copilot-in-Excel for finance

This is deliberately not a 40-hour curriculum. r03 doesn't need a university; he needs the workforce to stop treating four different patterns as one thing.

### Step 5 — Compliance & Measurement

**EU AI Act Art. 4 minimum-viable evidence** (Munich entity, 340 FTE in scope, but applied group-wide because the cost of differentiating is higher than the cost of including):

1. **Documented curriculum** mapped to roles and AI systems used (this document + the LMS structure)
2. **Completion records** with timestamp, score, and role tag for M1-M3 — held in the LMS for 5 years
3. **Role-tailored content** evidence: the branched M2 satisfies "considering the context in which the AI systems are to be used" (Art. 4 language)
4. **Refresh cadence**: annual recompletion + event-triggered updates when a new AI system is onboarded (the trigger is wired into the AI system inventory governance process)
5. **Provider information ingestion**: M1 and M2 explicitly reference vendor-supplied capability/limitation information (Copilot, Gong, GitHub Copilot, sandbox) — this satisfies the "taking into account... information given by the provider" clause

**Measurement** (three layers, reported monthly to ExCo):

| Layer | Metric | Target (90 days) | Source |
|---|---|---|---|
| Completion | M1-M3 completion rate | ≥95% group, 100% Munich | LMS |
| Pattern literacy | M1 quiz pass rate first attempt | ≥80% | LMS |
| Applied use | Sanctioned sandbox WAU / total | ≥50% | ChatGPT Ent admin + Copilot telemetry |
| Applied use | Copilot WAU | 31% → 55% | M365 admin |
| Applied use | Pattern-appropriate use (manual sample) | ≥70% of audited uses match pattern | Quarterly audit, n=80 |
| Shadow-AI suppression | Consumer ChatGPT/Claude.ai DNS hits | -90% from baseline | Network telemetry |
| Shadow-AI suppression | Self-reported shadow use | 38% → <10% | Repeat survey at d+90 |
| Manager role-modeling | Managers with ≥1 visible AI ritual | ≥75% | Manager self-attestation + skip-level check (n=40) |

**Shadow-AI suppression check** is non-negotiable: if at d+60 the network telemetry doesn't show consumer-AI traffic collapsing, the curriculum has not landed and we re-open the engineering segment.

---

## Synthesis

**CURRICULUM SPEC**
- 4-pattern taxonomy as spine: Chatbot / RAG / Workflow / Agent
- 6 role segments: Executive (35) / Manager (140) / IC (510) / Finance (22) / Legal (14) / Engineering (280) / Frontline (200)
- 3 mandatory modules (M1 Four Patterns, M2 Pattern-to-Task, M3 Verification & Privacy) — 90 min total, all FTE
- 2 mandatory workshops (Executive half-day, Manager 3hr) — segments 1 and 2
- In-flow tutorials in Gong, GitHub Copilot, Copilot-in-Excel
- Sanctioned sandbox: ChatGPT Enterprise with role-specific custom GPTs, DLP, SSO, Art. 4 logging
- Manager role-modeling tie-in: BCG 88/25 — three required visible behaviours per manager, telemetry shared back monthly

**COMPLIANCE FOOTPRINT (EU AI Act Art. 4)**
- Scope applied: group-wide; Munich entity (340 FTE) is the legal trigger
- Evidence package: curriculum doc + LMS completion records (5yr retention) + role-mapping + annual-refresh policy + provider-info ingestion in M1/M2
- Audit-ready: yes; closes FY26 internal audit finding
- Art. 5 prohibited-practices coverage: in M1 for all FTE
- Provider reliance: documented for Microsoft, OpenAI, Gong, GitHub, Harvey-equivalent

**30-DAY ROLLOUT**
- **Day 0-7**: ExCo sign-off on curriculum and metric targets; sandbox tenant configured; M1-M3 content production kickoff (reuse 60% from existing vendor library, custom-author the role branches and the 4-patterns module); LMS branching configured; legal review of Art. 4 evidence schema.
- **Day 8-14**: Executive workshop (two cohorts) — CFO co-facilitates vendor teardown. Sandbox opens to pilot cohort (60 engineers + 30 finance). DLP rules tuned. Consumer-AI block staged at firewall with 14-day amnesty notice.
- **Day 15-21**: Manager workshop (six cohorts). M1 launches group-wide; completion target 60% by d+21. In-flow tutorials enabled in Gong and GitHub Copilot. Consumer-AI block goes live at d+21.
- **Day 22-30**: M2 and M3 launch group-wide. Munich entity prioritised (100% completion target by d+30 for Art. 4 evidence). First monthly metrics pack to ExCo at d+30 — completion, sandbox WAU, Copilot WAU delta, consumer-AI DNS-hit delta, shadow-AI re-survey scoped.

**VERDICT: Compliant-not-effective (current state) → Compliant-and-effective (post-rollout)**

Current state is *non-compliant* on Art. 4 (open audit finding) and *not effective* (workforce is chatbot-only, 38% shadow AI, 31% Copilot WAU stuck). Post-rollout state is compliant (evidence package + role-tailored + refresh) and on track to effective (pattern-literacy assessable, manager role-modeling instrumented, shadow AI suppressed with substitution). Effectiveness is *probationary* until d+90 metrics confirm: if applied-use and shadow-AI suppression targets miss, re-open Step 4 — don't add more training, redesign the delivery.

---

## Why This Matters

r03's frustration ("€2.1M spent, decision quality hasn't moved") is the canonical mid-cap AI literacy failure mode: the company has bought four different *patterns* of AI tool but the workforce was trained — to the extent they were trained at all — on one. Every Copilot interaction is treated like a chatbot turn, every RAG result is read with chatbot-level scepticism (i.e., none), and the agent-shaped opportunity in CS triage sits unbuilt because no one in the building has a working mental model of what an agent is. This is why the 31% Copilot WAU has flatlined: people who think "AI = chatbot" don't reach for Copilot when the task is actually a RAG task, they alt-tab to ChatGPT.

The curriculum's central design choice is that the **taxonomy is the spine**. Most enterprise AI training programs we reviewed are organised around tools (a Copilot module, a ChatGPT module, a Gong module). That structure ratifies the very confusion r03 named. Organising around patterns — and re-explaining each tool as an instance of one or two patterns — gives the workforce a transferable mental model that survives the next vendor refresh. When the company adopts its fifth AI tool in 2026, no new module is needed; the question becomes "which of the four is this?"

The second design choice — the BCG 88/25 manager-role-modeling tie-in — is what differentiates this from a compliance exercise. Art. 4 evidence is necessary but not sufficient; the EU regulator does not care whether r03's Copilot WAU goes from 31% to 55%, but r03 does. The 88/25 evidence makes managers, not the L&D function, the load-bearing intervention, and that is the part of the architecture that has to survive the inevitable pressure to "just send everyone the e-learning." If the CFO and the 35 execs cannot visibly perform AI use in their own work for 90 days, no amount of LMS completion will move applied-use metrics. The shadow-AI suppression check at d+60 is the canary: if engineers are still on consumer ChatGPT, the curriculum is decoration.

---

## Sources

- European Commission, *Regulation (EU) 2024/1689 — Artificial Intelligence Act*, Article 4 (AI Literacy), in force 2 February 2025. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European Commission AI Office, *Living repository on AI literacy practices*, 2025. https://digital-strategy.ec.europa.eu/en/library/living-repository-foster-learning-and-exchange-ai-literacy
- BCG, *AI at Work 2024: Friend and Foe*, October 2024 — leader role-modeling and frontline adoption (88% vs 25%). https://www.bcg.com/publications/2024/ai-at-work-friend-and-foe
- Microsoft, *Work Trend Index 2024 — AI at Work Is Here. Now Comes the Hard Part*, May 2024. https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- McKinsey, *The State of AI: How Organizations Are Rewiring to Capture Value*, March 2025 — re-skilling and capability gaps. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- Anthropic, *Building Effective Agents*, December 2024 — workflow-vs-agent distinction. https://www.anthropic.com/research/building-effective-agents
- Participant survey r03, CFO mid-cap tech, conducted as part of the GSB AI transformation study, 2026.
