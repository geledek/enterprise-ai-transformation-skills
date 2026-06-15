# Peer Case Library

Retrieves named peer cases matched on archetype/vertical/size, then names the closest analog and what to copy or change.

## What it does

1. Forces a 5-question asker profile (vertical, size, archetype, maturity stage, decision type) — stops if fewer than 4 are answered.
2. Pulls 3-5 named cases from the bundled library under a strict schema: year / mode / outcome / story / lesson / source. Refuses anonymized cases and refuses to fabricate adjacency.
3. Runs cross-case pattern extraction — convergence, divergence, floor/ceiling, 95/5 placement, objective-mix, and 70% (people/process) signal.
4. Picks one closest-match case, names parallels and divergences, and converts each into action inheritance vs. action divergence.
5. Closes with a confidence verdict (High / Partial / No-analog-found) and a network prompt — specific people, forums, or alumni routes to source live conversations.

## When to use it

When a leader asks "how have others done this?", "show me cases from similar orgs", "what peer examples exist for this use case?", or "exchange best practices on AI deployment" — before a selection, build-vs-buy, or scale-vs-kill decision. Especially when the asker name-drops plausible cases from memory and needs them disciplined into a verified bundle. Trigger phrases include "Stanford / named case studies on this?" and "I want to learn from others' experiences."

## What it outputs

- Asker profile line (vertical | size | archetype | stage | decision)
- 3-5 named cases under fixed schema with sources — or an explicit No-analog-found verdict
- Cross-case convergence / divergence table with median time-to-value and 95/5 placement per case
- Closest-match recommendation with parallels, divergences, action inheritance, action divergence
- Confidence state and a named network prompt (operators, forums, alumni paths) to extend the bundle

## Example

**Scenario:** Brazilian agribusiness cooperative — CDO evaluating an agentic AI deployment for cooperative member services (claims processing, agronomic advisory, credit pre-screening) across 80,000 smallholder coffee and soy farmer-members in Minas Gerais and Mato Grosso. Board has earmarked R$45M for a two-year program; the CDO is being pressured to commit at the next quarterly meeting and wants to anchor the decision in what comparable cooperatives or member-services organizations have actually done.

**User prompt:**

> Hey — I'm the CDO at a Brazilian agribusiness cooperative (about 80k smallholder farmer-members across coffee and soy, Minas Gerais and Mato Grosso, R$12bn annual GMV). My board wants me to commit R$45M over two years to an agentic AI rollout — member services, agronomic advisory chatbots, claims triage, credit pre-screening — at our next quarterly meeting.
>
> Before I sign anything, I want to ground this in reality: have you seen what other cooperatives or large member-services orgs have actually rolled out in this space? I'm not looking for vendor decks — I want real deployments with names, numbers, and what blew up. Off the top of your head, what comes to mind? Anything from Rabobank's ag side, Cooxupé, Indian dairy co-ops like Amul, FrieslandCampina, John Deere's operations centre, or even credit unions doing similar member-AI plays? Just walk me through 3 or 4 you'd point me at.

**Skill output (excerpt):**

```
PROFILE: Brazilian ag-co-op (80k members, R$12bn GMV) | Federated/regulated/LGPD
       | Agentic workflow + member CS | Stage 1-2 | R$45M-2yr scale-commit gate

CASE BUNDLE (library-supported only — Rabobank/Cooxupé/Amul/Deere/CU NOT in bundle)
1. European Fintech Replace-mode CS — 2024 — Replace — CSAT -22%, hiring resumed
   in months — tracked volume/cost; missed quality — Stanford AI Index 2026.
2. Stanford-51 CS-Triage Aggregate — 2024-26 — Augment — wins concentrate when
   narrow + expert-in-loop; 95% of pilots produce zero P&L — Stanford AI Index 2026.
3. Stanford-51 Financial-Analysis Aggregate — 2024-26 — Augment — gains when expert
   retains sign-off; collapse under autonomous authority — Stanford AI Index 2026.
4. DBS Bank Stage-4 Exemplar — 2022-25 — Augment+Create — S$150M -> S$1B+ AI impact
   via shared platform + CEO-owned 1,000 experiments/yr — MIT CISR 2024.

CROSS-CASE PATTERN
- Convergence: pre-deployment quality metrics + invisible cost ~$10:$1 visible.
- Divergence: 4/4 centralized — NO library analog for federated cooperative ownership.
- 95/5 placement: 1 of 4 (DBS) on the 5% side; asker's plan resembles 95% pattern.
- Objective mix: bundle is efficiency-dominant (1.6x ceiling); asker's mix is too.
- 70% signal: 4/4 cases credit/blame the people-process layer, not the model.

CLOSEST MATCH: European Fintech Replace-mode CS (directional, NOT prescriptive)
  Inherit  — pre-defined quality metrics; treat 4 use cases as 4 pilots, not 1 program
  Adjust   — Augment-only for credit + claims; phase by region; 10/20/70 budget split;
             build shared platform in Year 2, not Year 1
  Avoid    — single big-bang Replace rollout (cost the case 22 CSAT points)

CONFIDENCE: NO-ANALOG-FOUND. Library lacks ag-cooperative / smallholder / Brazilian
/ federated-mutual cases. Treat brief as failure-mode floor, not a template.

NETWORK PROMPT (sourcing sprint before the board meeting):
- Cooxupé via OCB / ABAG / Embrapa digital-ag program
- Rabobank ag-AI via Rabo Foundation + São Paulo office
- Amul/NDDB via ICA ag-co-op working group
- John Deere Brazil via AgTech Garage Piracicaba
- Stanford GSB Latin America network — request peer convening
```

**How to read this output:**

- Read the CONFIDENCE line first. No-analog-found means the bundle is directional only — do not let it stand in for actual peer comparison.
- Check the CASE BUNDLE for sources. Every case has a named report; if a case lacks a source line, push back.
- The 95/5 placement count is load-bearing. 1-of-4 on the breakthrough side means the asker's plan is structurally closer to the failure pattern.
- The Inherit / Adjust / Avoid triad is the decision-relevant artifact. Each item should be traceable to a named parallel or divergence.
- The NETWORK PROMPT converts the asker's name-dropped orgs into a concrete sourcing route — that is the sprint that closes the gap the library cannot.

## Sources used

- `stanford-51-deployments.md` — 51-deployment study; 77% invisible-cost finding; canonical retrieved-case set
- `95-5-genai-divide.md` — base-rate anchor: 95% of pilots produce zero measurable P&L; 5% breakthrough criteria
- `european-fintech-case.md` — canonical Replace-mode failure: 700 agents, CSAT -22%, hiring resumed
- `mckinsey-3-objective-mix.md` — efficiency / growth / innovation classification for cross-case mapping
- `bcg-future-built.md` — 10/20/70 split; 70% people/process layer signal in retrieved cases
- `mit-cisr-4-stages.md` — Experimenting / Piloting / Scaling / Operating maturity-stage filter
- `nanda-tech-buy-vs-build.md` — buy deploys 2x faster; build wins only with deep moat

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).

## Effectiveness

Effectiveness test (2026-06-12): scored 25/25 (Grade B, +5.67 lift over the strongest baseline of vanilla LLM and kb-ask retrieval). 3-judge unanimous verdict.

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
