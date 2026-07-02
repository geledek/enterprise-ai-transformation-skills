---
name: general-peer-cases
description: Use when a leader asks for named peer cases, comparable deployments, or analog stories before making a selection or build decision. Phrases like "how have others done this?", "show me cases from similar orgs", "what peer examples exist for this use case?", "I want to learn from others' experiences", "exchange best practices on AI deployment", "any Stanford / named case studies on this?" all trigger this skill. Retrieves 3-5 named peer cases matched on vertical / org-size / use-case archetype, extracts cross-case patterns against the 95/5 base rate, and outputs a curated case bundle plus a closest-match action recommendation.
---

# General — Peer Case Library

Surface relevant named peer cases for the asker's situation. Output what worked, what failed, what they would do differently — and which single case is the closest analog.

Anchor base rate: 95% of GenAI pilots produce zero measurable P&L impact (MIT 2025). Only 5% break through. Every retrieved case must be situated against this floor — a "success story" pulled in isolation is misleading.

The library is bundled in `references/`. Pull cases by archetype match — not by name recall.

---

## Step 1: Asker Profile

Filter the library before retrieving. Without a profile, every case looks equally relevant — and nothing is actionable.

PROFILE QUESTIONS — answer each in one line:

1. **Vertical?** (Healthcare / FinServ / Public sector / Manufacturing / Retail / Tech / Professional services / Other — name the sub-vertical if it matters, e.g. "tertiary hospital" not just "healthcare".)
2. **Org size and operating model?** (Headcount band; centralized vs federated; regulated vs unregulated; geography.)
3. **Use-case archetype?** (Customer service automation / knowledge-worker copilot / document extraction / agentic workflow / vertical AI product / internal search — pick one. If unclear, force it.)
4. **Maturity stage?** (Experimenting / Piloting / Scaling / Operating — map against MIT-CISR's four stages. *Consult `mit-cisr-4-stages.md`.*)
5. **Decision being made?** (Selection / build-vs-buy / scale-vs-kill / vendor swap / governance gate — the case bundle should be tuned to this decision.)

If the asker can answer fewer than 4 of these, stop. Surface the gap. Cases retrieved without profile are noise.

Output:
VERTICAL | ORG SIZE | ARCHETYPE | MATURITY STAGE | DECISION TYPE

---

## Step 2: Case Retrieval

Pull 3-5 named cases from the bundled library. Match on archetype first, vertical second, org-size third. Never pad with weak matches — 3 strong analogs beat 5 mixed ones.

For each case, return the same six fields. No prose.

CASE SCHEMA:
- **YEAR** — when the deployment ran (or peak-public reporting year).
- **MODE** — Replace / Augment / Create (operational, not marketing).
- **OUTCOME** — measured result. Quantified where possible. Flag if only vanity metrics exist.
- **STORY** — three sentences max: what they did, what they tried, what happened.
- **LESSON** — the one thing the operator said in retrospect they would do differently.
- **SOURCE** — named report / paper / executive interview. No anonymized cases.

Stanford studied 51 enterprise GenAI deployments and found 77% of difficulty was invisible cost — change management, data, process redesign — not the model. *Consult `stanford-51-deployments.md`* for the canonical retrieved-case set; supplement with `european-fintech-case.md` for the canonical Replace-mode failure mode (700 agents replaced; CSAT -22%; hiring resumed in months).

If fewer than 3 cases match the archetype, state "No-analog-found" and skip to Step 4 with that verdict — do not fabricate adjacency.

Output:
CASE_1 (year/mode/outcome/story/lesson/source) | CASE_2 (...) | CASE_3 (...) | CASE_4 (optional) | CASE_5 (optional)

---

## Step 3: Cross-Case Pattern Extraction

Aggregate. Find the signal across the bundle — not the headline of any single case.

CONVERGENCE — what is the same across all retrieved cases?
- Common precondition (e.g. "all five had a named accountable executive before scaling").
- Common failure mode (e.g. "all five tracked volume; none tracked quality at week 12").
- Common time-to-value (state the median; state the spread).

DIVERGENCE — where do the cases split?
- Buy-vs-build split: name the count. *Consult `nanda-tech-buy-vs-build.md` if relevant — buy deploys 2x faster; build wins only with deep moat.*
- Replace-vs-Augment-vs-Create split: name the count.
- Centralized vs federated ownership split.

EMPIRICAL FLOOR / CEILING.
- Floor: the worst-case outcome among the retrieved cases. Quantified.
- Ceiling: the best-case outcome among the retrieved cases. Quantified.
- 95/5 anchor: state explicitly which retrieved cases sit on the 5% breakthrough side and which are in the 95% no-impact zone. *Consult `95-5-genai-divide.md`* — most "case studies" in circulation are dressed-up 95% cases.

OBJECTIVE-MIX CHECK. Map each case to efficiency / growth / innovation per `mckinsey-3-objective-mix.md`. Note the dominant objective in the bundle — and whether the asker's stated objective matches the bundle's center of gravity.

FUTURE-BUILT SIGNAL. *Consult `bcg-future-built.md`*: leaders pursue 10/20/70 split — 10% algorithm, 20% tech/data, 70% people/process. State for each case whether the operator credited the win (or blamed the failure) on the 70% layer.

Output:
CONVERGENCE | DIVERGENCE | FLOOR/CEILING | 95/5 PLACEMENT | OBJECTIVE MIX | 70% SIGNAL

---

## Step 4: Closest-Match Recommendation

From the bundle of 3-5, pick exactly one. The closest analog. State the parallel explicitly. State the divergence explicitly. State what the asker should do differently because of the divergence.

CLOSEST CASE: Name the case in one line.

PARALLEL — three concrete points where the asker's situation matches:
1. (e.g. same vertical, same archetype, same regulatory regime)
2. (e.g. comparable org-size and operating model)
3. (e.g. same maturity stage at decision time)

DIVERGENCE — three concrete points where the asker's situation differs:
1. (e.g. asker is federated; case was centralized — implication?)
2. (e.g. asker has weaker data foundation — implication?)
3. (e.g. asker is in regulated EU context; case was US — Art. 26 EU AI Act applies, case did not face it.)

ACTION INHERITANCE — for each parallel, what the asker should copy:
- (e.g. "Adopt their named-executive-owner pattern before scaling — saved 6 months in case.")

ACTION DIVERGENCE — for each divergence, what the asker must do differently:
- (e.g. "Case did big-bang rollout. Asker is federated — must phase by BU; expect 9-month not 4-month time-to-value.")

CONFIDENCE STATE: state one — High-confidence-analog / Partial-analog / No-analog-found.
- High-confidence-analog: 3+ parallels, 0-1 material divergences.
- Partial-analog: 2 parallels OR 2+ material divergences — case is directional, not prescriptive.
- No-analog-found: stop here. Tell the asker the library does not contain a sufficient match — and what they would need to source.

Output:
CLOSEST CASE | PARALLELS | DIVERGENCES | ACTION INHERITANCE | ACTION DIVERGENCE | CONFIDENCE STATE

---

## Synthesis: Case Bundle + Cross-Case Lessons + Closest-Match Action

Consolidate Steps 1-4 into a peer-learning brief. Write it the way the asker would want to hear it from a peer over coffee — terse, specific, named.

PROFILE: one line. (Vertical | Size | Archetype | Stage | Decision.)

CASE BUNDLE: the 3-5 cases as a numbered list, six fields each, no narrative connective tissue.

CROSS-CASE LESSONS: three bullets max.
1. The convergence finding the asker should treat as a precondition.
2. The divergence finding the asker should treat as a fork-in-the-road.
3. The 95/5 placement — how many of these cases actually broke through, and what separated them.

CLOSEST-MATCH ACTION:
- Named case: [case name].
- Inherit: [the one specific pattern to copy].
- Adjust: [the one specific divergence-driven adjustment].
- Avoid: [the one mistake the case made that the asker is still upstream of].

CONFIDENCE: High-confidence-analog / Partial-analog / No-analog-found.

NETWORK PROMPT: name 1-2 specific people / forums / events the asker should approach to deepen the case (e.g. "Stanford GSB Digital Business Academy alumni in same vertical"; "the named operator from the closest-match case if reachable; LinkedIn intro path"). Peer learning is incomplete without a route to a live conversation.

Output:
PROFILE | CASE BUNDLE | CROSS-CASE LESSONS | CLOSEST-MATCH ACTION | CONFIDENCE | NETWORK PROMPT

---

## References

*All files below live in `references/` at the plugin root (`${CLAUDE_PLUGIN_ROOT}/references/` when installed as a plugin).*

- `stanford-51-deployments.md` — 51-deployment study; 77% invisible-cost finding; canonical retrieved-case set.
- `95-5-genai-divide.md` — base-rate anchor: 95% of pilots produce zero measurable P&L impact; 5% breakthrough criteria.
- `european-fintech-case.md` — canonical Replace-mode case: 700 agents replaced, CSAT -22%, hiring resumed; the measurement-gap failure mode.
- `mckinsey-3-objective-mix.md` — objective-mix classification (efficiency / growth / innovation) for cross-case mapping.
- `bcg-future-built.md` — 10/20/70 split; the 70% people/process layer signal in retrieved cases.
- `mit-cisr-4-stages.md` — Experimenting / Piloting / Scaling / Operating maturity-stage filter for case match.

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
