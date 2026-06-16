# People — Workforce AI Literacy Curriculum

Designs a role-anchored AI literacy program that satisfies EU AI Act Art. 4 and breaks the chatbot-only usage pattern.

## What it does

1. Builds a four-pattern mental-model taxonomy (Chatbot / RAG / Workflow / Agent) and tests cohort fluency in each pattern's failure modes
2. Segments the workforce into five cohorts (Executive / Manager / Knowledge Worker / Frontline / Risk-Compliance) with distinct depth requirements
3. Produces a 5x4 competency matrix labelled MUST / SHOULD / COULD per cell with a named proof artifact per cell
4. Assigns delivery channels (sandbox, cohort workshop, in-flow tutorial) with manager-first sequencing and a 70-20-10 budget split
5. Outputs an EU AI Act Art. 4 evidence checklist, effectiveness metrics beyond completion, and a 30-day rollout calendar with verdict frame

## When to use it

When designing AI literacy training, addressing a workforce that uses AI as a chatbot only, or responding to the EU AI Act Art. 4 mandatory literacy duty (in force 2 Feb 2025). Triggers include: "our employees only use AI as a chatbot", "we need an AI literacy program", "what does Art. 4 require us to train", "build a role-based AI curriculum", or "design an AI training rollout". Use when stakes include regulator inquiry, works-council scrutiny, or a multi-million reskilling envelope.

## What it outputs

- Four-pattern taxonomy diagnostic with PATTERN COVERAGE, FAILURE-MODE FLUENCY, INTERNAL ANCHOR EXAMPLES, TAXONOMY GAPS
- Segment map with highest-leverage cohort, older-worker posture, and Risk-Compliance depth call
- 5x4 competency matrix with MUST/SHOULD/COULD labels and named proof artifact per cell
- Channel mix with manager-first sequencing, sandbox readiness check, 70-20-10 budget split
- EU AI Act Art. 4 evidence checklist with status per item and named remediation owner
- 30-day rollout calendar (Day 1-7, 8-21, 22-30) and verdict frame (Compliant-and-effective / Compliant-not-effective / Non-compliant)

## Example

**Scenario:** Aiko Tanaka is CPO at Marusan Logistics, a 14,000-employee third-party logistics and cold-chain group based in Osaka with operations in Japan, Korea, and a newly acquired 1,200-person Hamburg fulfilment arm that pulls the group under EU jurisdiction. The board approved a EUR 6.2M reskilling envelope for FY26 after a pulse showed 81% of self-described "AI users" only paste into ChatGPT to fix emails. Warehouse supervisors, dispatchers, safety auditors, and the C-suite have very different needs. The German works council is asking what Art. 4 now legally requires. Average workforce age is 47.

**User prompt:**

> I'm the CPO at Marusan Logistics — 14,000 staff across Japan, Korea, and a Hamburg unit we just acquired (1,200 people, brings us under EU rules). Board signed off EUR 6.2M for AI reskilling next fiscal year. The problem: our recent pulse showed 81% of "AI users" basically just paste stuff into ChatGPT to fix their emails. Dispatchers, warehouse supervisors, safety auditors, the C-suite — totally different needs but HR keeps proposing one generic "AI for everyone" e-learning. Hamburg works council is also asking what the EU now legally requires us to train. Can you help me design what this program should actually look like, who gets what depth of training, what we owe regulators in Hamburg, and how to roll it out without it becoming compliance theatre? Average workforce age is 47 and rising — that's a sensitivity too.

**Skill output (excerpt):**

```
TAXONOMY DIAGNOSTIC
  Pattern coverage:        chatbot 81% / RAG ~5% / workflow ~2% / agent 0%
  Failure-mode fluency:    LOW across all four
  Internal anchor examples: NONE in dispatch, safety, or warehouse ops
  Taxonomy gap:            no sanctioned RAG over SOPs / KPIs; fix BEFORE content design

COMPETENCY MATRIX (MUST / SHOULD / COULD)
                       Chatbot  RAG     Workflow  Agent
  Executive            SHOULD   MUST    SHOULD    MUST
  Manager (sup./disp.) MUST     MUST    SHOULD    SHOULD   <- highest-leverage cohort
  Knowledge Worker     MUST     MUST    SHOULD    COULD
  Frontline (warehouse) MUST*   SHOULD  COULD     COULD    *sanctioned tool only
  Risk-Compliance      MUST     MUST    MUST      MUST

  Proof artifacts (not quizzes):
    Manager MUST-RAG:        one team query answered against SOP corpus
    Risk-Compliance MUST-Agent: one IMDA 4-dimension review on file
    Executive MUST-Agent:    one signed tech-buy-vs-build with governance rationale

DELIVERY ARCHITECTURE  -- 70-20-10 budget on EUR 6.2M
  10% (EUR 0.62M)  content / e-learning shell
  20% (EUR 1.24M)  cohort delivery + manager enablement
  70% (EUR 4.34M)  sandbox + in-flow tutorials + integration
  Manager-first:   manager cohort completes Day 1-30 BEFORE team rollout
  Older-worker:    segment-blind extra office hours; no "older worker track"

ART. 4 EVIDENCE CHECKLIST (deployer scope, Hamburg)
  [ ] Training tied to role x AI-system-exposure -- owner: HR-DE, due Day 14
  [ ] Per-individual completion records -- owner: L&D ops, due Day 21
  [ ] Risks/harms content per role -- owner: Legal-DE, due Day 21
  [ ] Refresh cadence (annual + on material change) -- owner: HR-DE, due Day 30
  [ ] Evidence retention location -- owner: Compliance, due Day 30

30-DAY ROLLOUT
  Day 1-7    Manager cohort kickoff; sandbox stood up with sanctioned models
  Day 8-21   Manager cohort completion; weekly visible-use ritual launched
  Day 22-30  Knowledge-worker wave 1; in-flow tutorials live; first metrics pulse

VERDICT (Day 90 gate)
  Compliant-and-effective:   Art. 4 complete AND sandbox WAR >=60% AND pattern-fit >=70%
  Compliant-not-effective:   evidence done, usage lagging -> fix manager modeling first
  Non-compliant:             Art. 4 gaps -> halt new pattern rollout until closed
```

**How to read this output:**

- Start with the taxonomy diagnostic — if internal anchor examples are missing, content design is premature
- The matrix cell labels (MUST/SHOULD/COULD) plus named proof artifacts are the load-bearing output; quiz scores are not acceptable substitutes
- The 70-20-10 split is the budget integrity check — if HR is proposing 80% e-learning content, the program will fail the BCG 88/25 manager-modeling test
- Push back if the Day 90 verdict frame is dropped or if "completion %" is the only metric proposed — that produces compliant-not-effective at best
- The Art. 4 checklist must name an owner and date per row; otherwise evidence will not be producible within the 5-day regulator window

## Sources used

- `eu-ai-act-essentials.md` — Art. 4 mandatory literacy duty, scope, refresh, evidence requirements
- `bcg-manager-modeling.md` — 88/25 finding; manager weekly use as the adoption multiplier
- `deloitte-cheerleader-to-champion.md` — 30% champion-level executive sponsorship as adoption ceiling
- `70-20-10-value-split.md` — budget allocation across content, delivery, integration/sandbox
- `hiten-skill-library.md` — capturing proof artifacts as reusable skills compounds capability
- `accenture-redeployment-roi.md` — redeployment outcome as the true business case for literacy spend
- `imda-4-dimensions-agentic.md` — agent-pattern competency anchor for Risk-Compliance and Executive segments

## Effectiveness

Effectiveness test (2026-06-12): scored 24/25 (Grade C, +2 lift over the strongest baseline). kb-ask retrieval scored 22/25 — the skill adds organizational artifact output and named structural traps that retrieval alone misses.

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
