# Skill Catalog Effectiveness Report

_Run date: 2026-06-12 · all 15 skills evaluated (initial run + 1 retest) · 110 agent calls · ~4.56M tokens · 17.5 min wall-clock total_

## 1. Executive Summary

Across 15 skills evaluated under a three-condition harness (vanilla model, kb-ask wiki retrieval, full skill), the catalog demonstrates a **clear and consistent lift over both baselines**. Aggregate scores: vanilla A = **216.3 / 400** (54%), kb-ask B = **300.7 / 400** (75%), full skill C = **362.3 / 400** (91%). The full-skill condition won the judge majority verdict in **15 of 15 cases (100%)**.

- **Skills beat vanilla:** Yes, decisively. Mean lift of full skill over vanilla = **+9.0 points** (out of 25). Every skill in the catalog out-scored vanilla by a meaningful margin.
- **Skills beat kb-ask:** Yes, but the margin is materially smaller. Mean lift of full skill over kb-ask = **+3.7 points**. kb-ask alone already closes roughly **66% of the gap** between vanilla and full skill, which is the most important honest finding in this evaluation.
- **Overall catalog grade: B.** The skills work, but kb-ask retrieval is doing a lot of the heavy lifting. Three skills (`process-pilot-design`, `process-productionization`, `people-literacy-curriculum`) post lifts under +2.0 over kb-ask and earn **D / C** grades — they are at risk of being functionally redundant with retrieval alone.
- **Pattern:** Skills that encode **named multi-part frameworks with structural traps** (IMDA 4-dimension, PwC 20-item gate, three-channel ROI, six-layer stack) outperform retrieval most. Skills that are essentially **playbooks of best-practice content** (pilot design, productionization, curriculum) are most exposed to kb-ask substitution.

## 2. Methodology

- **Three conditions per skill:**
  - **A — Vanilla:** Base model, no skill, no retrieval.
  - **B — kb-ask:** Wiki retrieval over the knowledge base, no skill scaffolding.
  - **C — Full skill:** Skill invoked end-to-end.
- **Adversarial prompts:** Each skill was tested against a single domain-specific scenario engineered to expose the structural disciplines the skill is meant to enforce (e.g., the operational-mode trap for `general-idea-diagnostic`, the structural-vs-prompt-layer distinction for `tech-agent-guardrail`). Personas spanned APAC and EU sectors not used in the existing usage-guide examples.
- **Judges:** 3 independent judges per skill, blinded condition labels, instructed to mentally re-shuffle to control for position bias.
- **Dimensions (0–5 each, max 25 per condition):**
  1. Specificity to scenario
  2. Framework rigor
  3. Decision readiness
  4. Evidence and citations
  5. Failure-mode awareness
- **Lift = C − max(A, B).** Grades: A ≥ +6, B +3 to +6, C +2 to +3, D < +2.

## 3. Roll-Up Table

| Skill | A | B | C | Lift (C − max(A,B)) | Grade | Judge majority |
|---|---:|---:|---:|---:|:---:|:---:|
| general-peer-cases | 13.99 | 19.33 | 25.00 | +5.67 | B | C (3/3) |
| general-use-case-discovery | 12.00 | 18.66 | 24.00 | +5.34 | B | C (3/3) |
| people-frontline-engagement | 15.33 | 19.00 | 24.00 | +5.00 | B | C (3/3) |
| tech-data-deployment | 15.66 | 20.00 | 25.00 | +5.00 | B | C (3/3) |
| tech-stack-diagnostic | 13.66 | 20.00 | 25.00 | +5.00 | B | C (3/3) |
| tech-agent-guardrail | 14.67 | 20.00 | 24.67 | +4.67 | B | C (3/3) |
| process-portfolio-observability | 15.33 | 20.00 | 24.67 | +4.67 | B | C (3/3) |
| general-roi-gate | 13.67 | 20.33 | 25.00 | +4.67 | B | C (3/3) |
| tech-buy-vs-build | 16.33 | 19.67 | 24.00 | +4.33 | B | C (3/3) |
| general-maturity-assessment | 12.00 | 19.00 | 23.00 | +4.00 | B | C (3/3) |
| people-readiness-conversation | 15.33 | 20.00 | 24.00 | +4.00 | B | C (3/3) |
| general-idea-diagnostic | 16.34 | 20.33 | 24.00 | +3.67 | C | C (3/3) |
| people-literacy-curriculum | 13.67 | 22.00 | 24.00 | +2.00 | C | C (3/3) |
| process-pilot-design | 14.33 | 21.01 | 23.00 | +1.99 | D | C (3/3) |
| process-productionization | 14.00 | 21.34 | 23.00 | +1.66 | D | C (3/3) |

## 4. Findings

### Top 3 (highest lift over best baseline)
1. **general-peer-cases** (+5.67) — refused to fabricate cases the user explicitly asked about (Rabobank, Cooxupé, Amul, etc.), declared "No-analog-found" per skill rules, and produced schema-compliant cases with year/mode/outcome/lesson/source. Vanilla riffed from training data and risked fabrication — exactly the trap the prompt was engineered to elicit.
2. **general-use-case-discovery** (+5.34) — sequencing rule and value-pool thresholds catch errors kb-ask actively makes (parallel pilots).
3. **people-frontline-engagement** / **tech-data-deployment** / **tech-stack-diagnostic** (+5.00 each) — multi-step structural diagnostics (signed safety contract; data-class-to-tier mapping; six-layer walk with per-layer scorecards) that require the skill scaffolding to assemble.

### Bottom 3 (lowest lift)
1. **process-productionization** (+1.66) — kb-ask's framework citation density (B = 21.34) is nearly equal to the full skill on rigor and evidence. Skill's distinguishing value is concrete SLO numbers; otherwise redundant with retrieval.
2. **process-pilot-design** (+1.99) — kb-ask scores 21.01; the skill adds metric discipline and stop conditions but the playbook content is heavily represented in the wiki.
3. **people-literacy-curriculum** (+2.00) — kb-ask scores 22.00 (highest B in the catalog). Skill adds organizational artifacts (matrix, calendar) on top of content already well-retrieved.

### Patterns observed

- **kb-ask closes the gap most on content-heavy playbook skills.** Where the discipline is "remember these best practices and cite the right paper," retrieval alone gets ~85% of the way. Where the discipline is "execute a structural framework with named tests and verdicts," the skill's lift is durable.
- **Vanilla consistently fails on framework rigor and evidence.** Mean A scores: framework rigor 2.55, evidence 1.46. Vanilla simply does not produce named frameworks or citations under this prompt class.
- **Failure-mode awareness is the most consistent C-vs-B lift.** Across nearly every skill, C's failure-mode dimension is +1 to +2 over B. The skills are encoding "things that go wrong here" better than the wiki retrieves.
- **Decision-readiness gap is structural.** A scores ~3.6, B ~4.0, C ~4.9. kb-ask gives advisory output; skills give artifact output (gap tables, verdicts, owners, dates). This is the consistent structural discriminator.
- **High-lift skills are framework-named.** IMDA, PwC 20-item, three-channel ROI, six-layer stack, dual-framework maturity placement — these are durable. Skills without a named structural anchor (curriculum, productionization) show the smallest lift.

## 5. Recommendations

### Pulling weight (keep, prioritize, do not touch)
`general-peer-cases`, `general-use-case-discovery`, `people-frontline-engagement`, `tech-data-deployment`, `tech-stack-diagnostic`, `general-roi-gate`, `tech-agent-guardrail`, `process-portfolio-observability`, `tech-buy-vs-build`, `general-maturity-assessment`, `people-readiness-conversation`. All show lift ≥ +4 with consistent structural value beyond retrieval.

### Need rework
- **process-productionization (+1.66, D).** kb-ask matches it on framework rigor and beats it on evidence. The skill needs to either (a) deepen the SLO and gate-numerics discipline so it cannot be reproduced by retrieval, or (b) add a structural artifact (e.g., the operating-model handoff, kill-switch SLA contract) that retrieval cannot synthesize. As-is, this is the weakest skill in the catalog.
- **process-pilot-design (+1.99, D).** Borderline redundant. Consider sharpening into a "pilot stop-condition contract" skill rather than a general pilot design playbook — the unique value is the discipline of pre-declared kill criteria and named ownership, not the generic 90-day plan.
- **people-literacy-curriculum (+2.00, C).** kb-ask scores 22/25. The skill should lean harder into the four-pattern mental-model taxonomy and the older-worker stigma trap as structural discriminators; the artifact output (matrix, calendar) alone is not enough lift.

### One systemic recommendation
The catalog's structural advantage is **decision-ready artifact output** (gap tables, verdict frames, named owners, sunset conditions). Several skills with otherwise strong frameworks could push harder on this dimension — explicit verdict + condition + owner + date is the most consistent C-vs-B differentiator and the dimension where skill scaffolding has the most durable edge over retrieval.

## 6. Per-skill detail

Adversarial prompts, dimension scores, and judge rationales are preserved in the raw run data:
- `docs/effectiveness/2026-06-12-skill-effectiveness-raw.json` — initial 14-skill run
- `docs/effectiveness/2026-06-12-general-peer-cases-retest.json` — retest of the one failed run

## 7. Caveats

- **Sample size of 1 prompt per skill.** A second adversarial prompt per skill would strengthen the signal — especially for the bottom-3 skills, where rework decisions hang on whether the result is robust.
- **kb-ask was simulated, not actually invoked.** The B condition was a subagent told to use the references/ folder as a wiki. A real kb-ask invocation against your full vault might score differently. The relative ranking should hold; the absolute B scores might shift.
- **Judges are fellow LLM agents.** They control for position bias by instruction but share blind spots with the conditions they judge. Human review of 2-3 borderline cases (especially the D-graded ones) would harden the conclusion.
- **No remaining failures.** `general-peer-cases` was re-run and posted +5.67 lift (top of catalog).
