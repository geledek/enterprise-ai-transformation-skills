---
name: ai-idea-diagnostic
description: Use when evaluating an AI idea, AI concept, or early-stage AI proposal — before any pilot design or investment decision. Phrases like "should we pursue this AI idea?", "is this AI concept worth exploring?", "does this AI use case make sense?", "we're thinking about building AI for X — is it a good idea?" all trigger this skill. Diagnoses using a five-role framework — Investigator (real friction), Devil's Advocate (right solution mode), Long-term Strategist (value accumulates), Realist (right capability), Senior Advisor (synthesis verdict). Outputs Fund / Fund-with-condition / Reframe / Kill.
---

# AI Idea Diagnostic

Diagnose an AI idea at concept stage — before pilot design, before investment, before any build decision. Five sequential roles. Maintain all prior reasoning as state — each role builds on the previous.

After each role, output a clearly labeled section, then proceed to the next role. Do not stop until all five are complete.

---

## Role 1: Investigator (Q1 — Real Friction?)

NAME WHO FEELS THE PAIN. Who specifically experiences the problem? What does it cost them — in time, money, quality, or risk?

CLASSIFY THE STARTING POINT.
- Friction-first: "Our customers / teams struggle with [specific thing]"
- Tech-first: "We should use AI for [task]"

State which — and quote the language that signals it.

FRICTION STATEMENT. If friction-first: state the pain in one sentence. If tech-first: flag this as a warning sign and identify the real friction before proceeding.

Output:
WHO FEELS THE PAIN | WHAT IT COSTS | FRICTION-FIRST OR TECH-FIRST | PAIN STATEMENT

---

## Role 2: Devil's Advocate (Q2 — Right Solution Mode?)

Your job is to find where this breaks, not where it succeeds.

RELIABILITY TEST. "Would I be comfortable if this output reached the end consequence — the customer, the regulator, the judge — without human review?" Yes or no. Name the consequence of an error.

OPERATIONAL-MODE CHECK. Strip out the human-in-loop language from the pitch. In the moment the output reaches the end party, is a human actually between the AI and them? If no, the initiative is operationally Replace regardless of how it is described.

CONSEQUENCE LEVEL CHECK. Does this application handle tasks or queries of different consequence levels? If yes, the most consequential type sets the mode for the whole application.

ERROR LOOP.
- No one catches errors → Replace mode. Name the risk.
- Human in loop by design → Augment mode. Name their role.
- AI enables what structurally couldn't exist before → Create mode.

MODE VERDICT. State: Replace / Augment / Create. State the single condition that must hold. Flag if it is not yet met.

Output:
RELIABILITY TEST | OPERATIONAL MODE | CONSEQUENCE LEVEL | ERROR LOOP | MODE | CRITICAL CONDITION | FAILURE RISK

---

## Role 3: Long-term Strategist (Q3 — Value Accumulates?)

WHAT ACCUMULATES? Assess all three dimensions. A gap on any one produces Fund-with-condition, not Fund.

(a) Gets better — does the solution improve as it is used, through data accumulation, model learning, or network effects? A solution that plateaus on day one is a productivity tool.
(b) Switching costs — how costly is it for a user or organisation to leave? High accumulation with low switching costs is still vulnerable.
(c) Competitive preference — do users actively choose this over alternatives, or do they tolerate it because leaving is expensive?

Name which dimensions pass and which do not.

MEASUREMENT CHECK — THE MEASUREMENT GAP.
Name three metrics that prove this is working. Are these the metrics that would naturally get tracked? Flag any gap between what matters and what is easy to measure.

*Consult `european-fintech-case.md` in the `references/` folder: a leading European fintech replaced 700 agents with one AI system — tracked volume, speed, cost; did NOT track resolution quality, repeat-contact rate, CSAT. CSAT dropped 22%. Hiring resumed within months.*

OBJECTIVE-MODE CHECK.
Map this idea to one of three objectives (consult `mckinsey-3-objective-mix.md`):
- Efficiency (cost reduction, productivity): 80% of firms; narrowest path
- Growth (revenue uplift, new markets): high-performer objective
- Innovation (new products, business-model change): high-performer objective

MOAT CHECK.
Does this idea build toward one of three moat types (consult `andrew-ng-three-moats.md`)?
- Asset portfolio: multiple difficult, mutually-reinforcing AI assets?
- Industry-specific advantage: becomes the AI leader in a vertical?
- Virtuous cycle: product produces data; data improves product?

BLAST-RADIUS CHECK. If this fails on day one, who sees it — internal users, paying customers, regulators, or the public?

Output:
WHAT ACCUMULATES | THREE METRICS | MEASUREMENT GAP | OBJECTIVE MODE | MOAT TYPE | BLAST RADIUS

---

## Role 4: Realist (Q4 — Right Capability?)

Your job is to identify the execution gaps that would prevent this idea from working in practice, regardless of how sound the concept is.

DATA. Is the data AI-ready? Does the organisation have confirmed legal rights to use it? Is it in a usable format and accessible via pipeline? (Consult `isg-data-foundation.md` in `references/` — the binding-constraint finding.)

INTEGRATION. Is there a plan to connect the AI output to real operational workflows — including what happens when the AI is wrong?

CHANGE MANAGEMENT. Stanford: 77% of the hardest challenges in enterprise AI are invisible costs — change management, data quality, process redesign. Not tech. Does the org have the muscle to absorb this deployment? (Consult `stanford-51-deployments.md` in `references/`.)

Output:
DATA | INTEGRATION | CHANGE MANAGEMENT | Q4 VERDICT (Pass / Gaps / Fail)

---

## Role 5: Senior Advisor (Synthesis)

Read the outputs of Roles 1–4. Produce the verdict. Do not introduce new assessment here.

Write for a board audience. Be direct.

VERDICT: [Fund / Fund-with-condition / Reframe / Kill]
MODE: [Replace / Augment / Create]

Q1 — REAL FRICTION? (2 sentences)
Q2 — RIGHT SOLUTION MODE? (2 sentences)
Q3 — VALUE ACCUMULATES? (2 sentences)
Q4 — RIGHT CAPABILITY? (2 sentences)

STRONGEST LINK: Where this idea is most solid.
WEAKEST LINK: Where this idea is most at risk of failing silently.
ONE CHANGE: Specific action — not a general recommendation.

CLOSEST REFERENCE CASE: Match against the cases in `cases/` and name the parallel explicitly.

---

## Reference Cases

See `cases/` for diagnosed examples. When diagnosing a new idea, compare against the closest reference case and note the parallel explicitly.

## References

- `95-5-genai-divide.md` — empirical basis for why rigorous gating matters: 95% of pilots produce zero measurable P&L impact
- `european-fintech-case.md` — canonical measurement-gap failure case
- `mckinsey-3-objective-mix.md` — objective-mode classification (efficiency / growth / innovation)
- `andrew-ng-three-moats.md` — moat-type classification
- `stanford-51-deployments.md` — invisible-costs reality check
- `isg-data-foundation.md` — data readiness criteria
