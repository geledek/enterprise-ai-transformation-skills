---
name: people-readiness-conversation
description: Use when assessing an organization's leadership readiness for AI transformation, surfacing where people and leadership gaps will block AI progress, preparing for a leadership team AI conversation, or diagnosing why AI investments aren't creating value despite good technology. Phrases like "is our leadership team ready for AI?", "surface AI readiness gaps in our leadership team", "help me understand where our people gaps are on AI", "prepare me for a leadership team AI conversation", "why aren't we getting value from AI despite our investment?", "assess AI readiness in our organization" all trigger this skill. Runs a four-role gap analysis (CEO / Manager / Employee / HR) with diagnostic questions for each role. Outputs a 4-role gap report with specific actions per gap.
---

# People — AI Leadership Readiness Conversation

Surface the people and leadership gaps that will block AI progress, regardless of how good the technology is. Four roles. Specific diagnostic questions. Actionable gap report.

BCG 2026: 70% of AI value comes from People. The 88/25 manager role-modeling gap is the most actionable single lever. Most organizations that under-perform on AI have a technology that works and people who don't.

---

## Role 1: CEO Readiness — Champion vs. Cheerleader

The gap: a cheerleader endorses AI publicly; a champion personally owns AI outcomes.
McKinsey: firms where the CEO personally owns AI show a 3× performance differential. (Consult `mckinsey-3x-senior-ownership.md`)

Diagnostic questions (answer with evidence, not aspiration):
1. **Does the CEO personally own named AI initiatives?** (Not "sponsor" them — own them. Is the CEO's name on the initiative, reviewing metrics, accountable for outcomes?)
2. **Does the CEO review AI initiative metrics at the same cadence as P&L?**
3. **Has the CEO made a public commitment (internally) to a specific, measurable AI goal?** (Not "we're all in on AI" — a number, a timeline, a business outcome)
4. **Has the CEO personally used AI tools in the past 30 days?** (Not in a demo — in real work)
5. **Does the org have an AI strategy ratified by the C-suite?** Or is it an IT/data team document?

GAP CLASSIFICATION:
- Cheerleader (endorses without ownership): PRIMARY GAP — nothing else will reach the 3× differential without this
- Aware but not active: SECONDARY GAP — developing
- Champion (personally owns, publicly accountable): PASS

Output:
CEO STATUS | EVIDENCE | GAP CLASSIFICATION | SPECIFIC ACTION REQUIRED

---

## Role 2: Manager Readiness — Role-Modeling Gap

The gap: 88% of managers believe AI role-modeling matters. Only 25% do it visibly. (BCG BFFxAI 2026 — consult `bcg-manager-modeling.md`)

Diagnostic questions:
1. **In the past month, how many managers have used AI outputs in a team meeting?** (Not prepared privately — used publicly)
2. **In the past month, how many managers have run an AI prompt in front of their direct reports?**
3. **Do managers assign AI-augmented tasks to their teams, and review the AI output together?**
4. **Is AI use part of any manager's performance objective or review?**
5. **What is the manager's stated belief about AI?** ("AI will replace jobs" = adoption barrier; "AI is a tool I should model" = alignment)

GAP CLASSIFICATION:
- Below 25% visible adoption: CRITICAL GAP — the 88/25 gap is exactly this
- 25–50% visible adoption: DEVELOPING
- Above 50%: STRONG

Output:
MANAGER VISIBLE ADOPTION RATE | EVIDENCE | GAP CLASSIFICATION | SPECIFIC ACTION REQUIRED

---

## Role 3: Employee Readiness — Literacy and Duty

The gap: employees are the 70% that creates AI value. EU AI Act Art. 4 (in force February 2025) makes AI literacy a mandatory duty for any org deploying AI in the EU. (Consult `eu-ai-act-essentials.md`)

Diagnostic questions:
1. **Is AI literacy training in place?** (Mandatory or optional? Coverage rate? Completion rate?)
2. **Do employees understand the difference between what they should trust AI to do vs. what requires human judgment?**
3. **Is there a sanctioned AI toolkit employees can use?** Or are they using shadow AI?
4. **Are employees bringing AI to their work voluntarily?** Or waiting for permission?
5. **Is there a feedback mechanism for employees to report AI tool issues or suggest improvements?**

GAP CLASSIFICATION:
- No training or optional-only: GAP (also potential regulatory exposure under EU AI Act Art. 4)
- Mandatory training with <50% completion: DEVELOPING
- Mandatory training with >80% completion + sanctioned toolkit + voluntary adoption: STRONG

Output:
AI LITERACY STATUS | SHADOW AI RISK | VOLUNTARY ADOPTION SIGNAL | REGULATORY EXPOSURE | GAP CLASSIFICATION

---

## Role 4: HR Readiness — Five Jobs

The gap: HR has five distinct jobs in the AI workforce transition. Most organizations are executing 0–2 of them. (Deloitte 2026 — consult `deloitte-cheerleader-to-champion.md`)

For each of HR's five jobs, assess status (ACTIVE / PLANNED / ABSENT):

1. **Talent acquisition — AI literacy as a hiring criterion**
   - Is AI literacy in job descriptions? Is it assessed in interviews? Or is it a nice-to-have?
   
2. **Career-path redesign — rebuilding the pipeline for AI-era entry-level roles**
   - Stanford AI Index 2026: 22–25 year-olds in high-AI-exposure occupations down 16% in headcount. Entry-level erosion is empirically real.
   - Is HR actively redesigning entry-level career paths for the AI-era? Or hoping existing ladders still work?
   
3. **Performance and incentive redesign — incorporating AI usage into performance frameworks**
   - Only 30% of organizations do this (Deloitte 2026).
   - Is AI proficiency part of any performance review? Is manager role-modeling a performance expectation?
   
4. **Workforce planning and redeployment — assessing skill demand under AI transition**
   - Only 30% do this (Deloitte 2026).
   - Does HR have a forward-looking workforce plan that accounts for AI-driven role changes?
   - Is there a redeployment plan for roles that AI automates? Or just silence?
   
5. **Employment-mix rebalance — FT/contract/gig strategy**
   - Only 19% do this (Deloitte 2026).
   - Is the org's employment mix proactively managed for AI era, or inherited from pre-AI defaults?

Output:
JOB 1–5 STATUS (ACTIVE/PLANNED/ABSENT) | CRITICAL GAPS | SPECIFIC ACTIONS PER GAP

---

## Synthesis: 4-Role Gap Report

Consolidate Roles 1–4. Write for CEO or CHRO audience.

**OVERALL READINESS ASSESSMENT:**
- People layer is: STRONG / DEVELOPING / CRITICAL-GAP
- BCG 70% value layer is at risk from: [named gaps]

**PRIORITY ORDER:**
1. [First priority gap — with specific action and named owner]
2. [Second priority gap — with specific action and named owner]
3. [Third priority gap — with specific action and named owner]

**QUICK WINS (addressable within 30 days):**
- [Action 1 — specific, not generic]
- [Action 2]

**STRUCTURAL ACTIONS (require 60–90 day commitment):**
- [Action 1 — specific, not generic]
- [Action 2]

**THE MULTIPLIER ACTION** (the one change that unlocks the others):
- [Single most important action — usually CEO champion posture or manager visible role-modeling program]

---

## References

- `70-20-10-value-split.md` — BCG 70% people value; context for why these gaps matter
- `bcg-manager-modeling.md` — 88/25 role-modeling gap; specific manager behaviors
- `mckinsey-3x-senior-ownership.md` — 3× CEO ownership differential
- `deloitte-cheerleader-to-champion.md` — HR's five jobs; 74/21 governance gap
- `eu-ai-act-essentials.md` — Art. 4 AI literacy mandatory duty
- `mckinsey-3-objective-mix.md` — objective-mode audit for CEO strategy gap
- `accenture-maturity-archetypes.md` — Differentation axis includes sponsorship + training; Innovator vs. Builder gap

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
