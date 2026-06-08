# AI Idea Diagnostic

A five-role concept gate for AI ideas — before any pilot design or investment decision.

## What it does

Diagnoses an AI idea at concept stage using four questions and five sequential roles:
- **Q1 (Investigator):** Is there real friction — or is this tech-first?
- **Q2 (Devil's Advocate):** Is Replace / Augment / Create the right mode, and is the critical condition met?
- **Q3 (Long-term Strategist):** Does value accumulate? What's the moat? Are the right metrics named?
- **Q4 (Realist):** Is data ready? Is change management capacity present?
- **Synthesis (Senior Advisor):** Fund / Fund-with-condition / Reframe / Kill

## When to use it

Before you design a pilot. Before you ask for investment approval. Any time someone says "we're thinking about building AI for X."

If you want a funding-gate assessment (after the idea has become an investment proposal), use `roi-gate-pwc` instead.

## What it outputs

A structured five-section report, ending with:
- Verdict: Fund / Fund-with-condition / Reframe / Kill
- Mode: Replace / Augment / Create
- Strongest link, weakest link, one specific change
- Closest reference case from `cases/`

## Cases

See `cases/` for six diagnosed examples: Air Canada, JPMorgan COIN, Klarna (anonymized), McDonald's, Moderna, NYC MyCity.

## Sources used

- `95-5-genai-divide.md` — empirical basis for gating
- `european-fintech-case.md` — measurement-gap reference case
- `mckinsey-3-objective-mix.md` — objective classification
- `andrew-ng-three-moats.md` — moat classification
- `stanford-51-deployments.md` — invisible-costs reality check
- `isg-data-foundation.md` — data readiness criteria

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
