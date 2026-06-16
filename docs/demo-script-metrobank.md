# Demo Script — MetroBank Singapore

A live-demo script for the Enterprise AI Transformation Skills library. Six prompts across the four buckets (general / process / tech / people), all running the same MetroBank Singapore narrative so the audience sees how the skills compose into one coherent advisory engagement.

**Total runtime:** ~12 minutes (6 prompts × 90s + 2 min for setup/closer).
**5-minute version:** run prompts 1, 3, 5 only — one per bucket.

---

## Setup line for the audience (10 seconds)

> *"You are advising the CDO of MetroBank Singapore — 2,400 staff, MAS-regulated retail/SME bank. CEO declared 'AI-first' 14 months ago, S$50M committed. Results are patchy. Board meeting in 90 minutes. Let's see what the skill library does in real time."*

---

## 1. `general-maturity-assessment` *(GENERAL — diagnose where we are)*

**Prompt:**
> Where is MetroBank Singapore on the AI maturity curve? We're a mid-size SG retail/SME bank, ~2,400 staff, MAS-regulated. CEO declared "AI-first" 14 months ago, S$50M committed. We've shipped Microsoft Copilot to all knowledge workers, a customer-service chatbot, and three RAG pilots in compliance. Adoption is patchy. CHRO hasn't been asked to do anything specific. Where are we, why are we stuck, and what's the next stage?

**Verdict to expect:** MIT CISR Stage 2, Accenture archetype = AI Experimenter, **binding constraint = Foundation gap** (no platform, no MLOps, governance-on-paper). Stage 3 needs shared platform + data product layer + a growth-objective use case.

**Speaker beat:** *"Two frameworks doing two jobs — MIT CISR tells us where, Accenture tells us why we're stuck."*

---

## 2. `general-use-case-discovery` *(GENERAL — what to pilot first)*

**Prompt:**
> We have 23 candidate AI ideas from our innovation challenge — RM call-prep summarizer, AI-powered SME loan underwriting, customer churn prediction, KYC document classification, claims-style branch chatbot, etc. We need to pick the first pilot for the next quarter. Which use case should we point AI at first, and why not the others?

**Verdict to expect:** Top-3 ranked, **first-pilot pick = RM call-prep summarizer** (narrow, internal blast radius, distribution moat from existing CRM seats), kill list with one-line reason each.

**Speaker beat:** *"Watch how it Stage-and-watches customer-facing candidates — that's an alignment fix from yesterday so this skill doesn't recommend something the pilot-design skill would immediately downrate. Stanford 51 deployments shows ~60% of failed pilots launched customer-facing without tighter stop conditions."*

---

## 3. `process-pilot-design` *(PROCESS — design the test)*

**Prompt:**
> Design a 90-day pilot for the RM call-prep summarizer at MetroBank. RAG over CRM + product docs + recent emails, drafts a 1-page brief 30 minutes before each meeting. Premier Banking team, ~40 RMs, S$5M+ AUM clients. Need a one-page brief for the COO sponsor by Friday.

**Verdict to expect:** 7-role walk: scope → pre-deployment metrics → blast radius → stop conditions → workflow redesign → ownership → one-page brief. Will flag a measurement gap (downstream RM-meeting outcome metric needs new instrumentation), Day 30/60/90 stop conditions, named owner = Head of Premier Banking Digital.

**Speaker beat:** *"Pre-deployment metrics — the metric that matters vs. the metric that's easy. This is the discipline most pilots miss."*

---

## 4. `tech-data-deployment` *(TECH — where can the data legally run)*

**Prompt:**
> RMs want to summarize client meeting transcripts. Transcripts contain client name + portfolio holdings + occasional MNPI ("client mentioned planned IPO of their company"). Today they're pasting into ChatGPT free. Cross-border component — Swiss back-office team needs to read outputs. What's the deployment pattern, and what controls do we need?

**Verdict to expect:** **Data class = REGULATED** (MNPI dominant), **Tier = T4 minimum** (private VNet or self-host), **Verdict = BLOCKED at current state, Conditional approval on T4** with named control products (Purview DLP, Entra conditional access, ABAC on RAG corpus, PDPA Transfer Impact Assessment).

**Speaker beat:** *"Names the regulators (MAS, PDPC, FINMA), names the tier, names the products. Decision-grade output, not generic GDPR hand-waving."*

---

## 5. `people-frontline-engagement` *(PEOPLE — when experts block the rollout)*

**Prompt:**
> Six months ago we deployed an AI tool that auto-scores SME loan applications. The credit-risk team has 12 senior credit analysts, all 15+ years tenure. Two have resigned. The remaining ten are openly hostile in team meetings. One said in writing: "If this thing approves a bad loan and we get an MAS audit finding, who's on the hook? Me. So no, I'm not using it." Pilot is stalled. How do I get them to engage before I lose more?

**Verdict to expect:** Five-role walk: empathic listen (named fear = accountability shift + status loss) → jagged-frontier task split → co-design workshop → six-clause psychological-safety contract (incl. no-headcount-cut, opt-in piloting, named accountable senior) → tradecraft-protection mechanisms. **Verdict = Imposed-with-resistance, achievable as Co-designed if Roles 3–5 run within 30 days.**

**Speaker beat:** *"Edmondson's psychological safety + Dell'Acqua's jagged frontier + Accenture redeployment. The output is a signed contract, not a town hall."*

---

## 6. `process-portfolio-observability` *(PROCESS — what's the net ROI)*

**Prompt:**
> MetroBank has shipped 11 AI agents over 18 months. Token spend grew from S$8K to S$140K/month. CFO is asking what we earned. We have no portfolio dashboard, no net-of-oversight ROI, and the CEO is in front of the board next month. What's the state of our AI portfolio?

**Verdict to expect:** KPI tree connectivity (only 4 of 11 agents traceable to P&L), **gross-vs-net delta** (typical pattern: claimed S$3.2M productivity, real net S$1.81M = −44%), three-state verdict = **Black-box**, freeze new deployments until Dim 1 + Dim 3 stand up, sunset rule (net ROI negative 2 months → archive).

**Speaker beat:** *"PwC 2026 was explicit — net of oversight is the only honest number. This skill produces it."*

---

## Optional 7th — `general-roi-gate` (closer for advanced rooms)

**Prompt:**
> The board has a S$8M ask on the table to fund a "GenAI-powered KYC remediation platform" — pitched as 40% reduction in periodic-review backlog. Run the ROI gate before the credit committee meets next week.

**Verdict to expect:** Three-channel ROI = 1/3 complete (only labor savings present), 20-item PwC checklist (12 confirmed, 5 gap, 3 red flag), **Verdict = Return-for-revision** with named conditions.

**Closer line:** *"Each skill is one file — `SKILL.md` — that an AI agent loads on demand. The model commoditizes. The skill library compounds."*

---

## Live-demo hygiene

- **Run them in order** — each builds the same MetroBank narrative.
- **Don't read outputs verbatim.** Let the skill produce, summarize the verdict in one sentence, move on. Audience attention dies on long output.
- **Highlight the verdict vocabulary differences** — Fund/Reframe/Kill (concept), Greenlight/Stage/Park/Reject (selection), Approve/Conditional/Return/Reject (funding). Each gate uses different language by design — they sit at different points in the lifecycle.
- **Time check:** 6 prompts × ~90 seconds each = ~9 minutes. Add 60 seconds at the start (setup) and 60 seconds at the end (closer). Comfortable inside a 12-minute slot.
- **If you only have 5 minutes:** run prompts 1, 3, 5 (one per bucket — general, process, people) and skip the rest.
