# Golden prompts

One trigger prompt per skill plus the output contract it must honor. Use this
to regression-check skill edits: run the prompt against the edited skill and
confirm (a) the skill triggers, (b) all roles/steps execute in order, and
(c) the final verdict uses exactly the vocabulary listed here. The verdict
vocabularies are stable output contracts — see CLAUDE.md.

The effectiveness reports in `docs/effectiveness/` are point-in-time runs of
prompts like these; re-running this table after a skill change makes results
comparable across versions.

## General

| Skill | Golden prompt | Expected output contract |
|---|---|---|
| `general-idea-diagnostic` | "Should we pursue an AI agent that auto-approves expense reports under S$200?" | 5 roles (Investigator, Devil's Advocate, Long-term Strategist, Realist, Senior Advisor); verdict **Fund / Fund-with-condition / Reframe / Kill** + mode **Replace / Augment / Create**; names closest case from `cases/` |
| `general-use-case-discovery` | "Where should we point AI first across our claims operation?" | Ranked candidate list; per-candidate verdict **Greenlight / Stage-and-watch / Park / Reject**; customer-facing candidates default to Stage-and-watch without sponsor-signed risk acceptance |
| `general-maturity-assessment` | "Where are we on the AI maturity curve, and what's next?" | MIT CISR stage placement (Stage 1–4) + Accenture archetype; named next-stage actions |
| `general-peer-cases` | "Has anyone else deployed AI for member services at a financial cooperative?" | Asker profile, case bundle, cross-case patterns; confidence state incl. **No-analog-found** when <3 archetype matches (must not fabricate cases) |
| `general-roi-gate` | "Run the ROI gate on this AI investment proposal" | PwC 20-item checklist + three-channel ROI; recommendation **Approve / Approve-with-conditions / Return-for-revision / Reject** |

## Process

| Skill | Golden prompt | Expected output contract |
|---|---|---|
| `process-pilot-design` | "Design a 90-day pilot for an RM call-prep summarizer at our private bank." | 90-day plan with Day 30 / Day 60 / Day 90 gates, pre-deployment metrics, stop conditions, pass/fail verdict criterion |
| `process-productionization` | "Demo works — how do we move it to production?" | 5-stage playbook + 15-item gate; verdict **GO / CONDITIONAL GO / NO-GO** with remediation list and rollout schedule |
| `process-portfolio-observability` | "We deployed 11 agents but can't see what they're earning. Help." | Three-layer KPI tree + dashboard spec, net-of-oversight ROI; verdict **Observable-and-governed / Partial-observability / Black-box** |

## Tech

| Skill | Golden prompt | Expected output contract |
|---|---|---|
| `tech-stack-diagnostic` | "Diagnose our AI tech stack — where's the weakest link?" | Six-layer stack assessment naming the single weakest layer + remediation priority |
| `tech-buy-vs-build` | "Should we build, buy, or partner for this AI capability?" | Per-component **Buy / Build** verdicts + investment verdict; applies "buy the model, build the orchestration" |
| `tech-data-deployment` | "Where can this data legally run? ChatGPT? Enterprise SaaS? VPC?" | Deployment-tier mapping per data class; verdict **Approved / Conditional / Blocked** |
| `tech-agent-guardrail` | "We're about to launch an AI agent — is it safely governed?" | IMDA four-dimension + NIST RMF assessment; verdict **Deploy / Deploy-with-conditions / Do-not-deploy-until-gaps-addressed** |

## People

| Skill | Golden prompt | Expected output contract |
|---|---|---|
| `people-readiness-conversation` | "Why isn't our AI investment moving the needle? Surface the people gaps." | 4-role gap report (CEO / Manager / Employee / HR); per-layer rating **STRONG / DEVELOPING / CRITICAL-GAP** with actions per gap |
| `people-literacy-curriculum` | "We need an AI literacy program that satisfies EU AI Act Article 4." | Role-based curriculum + Art. 4 evidence plan; verdict **Compliant-and-effective / Compliant-not-effective / Non-compliant** |
| `people-frontline-engagement` | "Our senior lawyers are openly hostile to the contract-review AI. What now?" | Co-design engagement plan incl. pilot-window no-headcount-cut clause; verdict **Co-designed / Imposed-with-resistance / Stalled** |
| `people-tool-selection` | "I'm training school teachers who already use ChatGPT — should I teach advanced prompting, agent skills, or a new tool?" | 6 roles; constraints eliminate before capability ranks; mode **Deepen / Extend / Introduce**; verdict **Adopt-now / Adopt-with-scaffolding / Pilot-with-subgroup / Skip** + first-win exercise + growth path |

## Routing prompts — must NOT misfire

With 16 skills, the failure mode isn't just "skill doesn't trigger" — it's the
*adjacent* skill triggering instead. Each prompt below must route to the skill
in column 2 and must NOT activate the skill in column 3. Run these after
editing any frontmatter `description` (that's what Claude routes on).

| Prompt | Must route to | Must NOT trigger | Boundary being tested |
|---|---|---|---|
| "Which AI tool should I teach this group of nurses?" | `people-tool-selection` | `people-literacy-curriculum` | Single tool for one group vs. enterprise-wide program design |
| "Build a role-based AI literacy curriculum for the whole company" | `people-literacy-curriculum` | `people-tool-selection` | Same boundary, opposite direction |
| "Should we build or buy this AI capability?" | `tech-buy-vs-build` | `people-tool-selection` | Sourcing decision vs. group-adoption decision |
| "Should we pursue this AI idea at all?" | `general-idea-diagnostic` | `general-roi-gate` | Concept-stage gating vs. investment approval |
| "The idea is validated — run the funding gate on the proposal" | `general-roi-gate` | `general-idea-diagnostic` | Same boundary, opposite direction |
| "Where can this customer data legally run — ChatGPT or VPC?" | `tech-data-deployment` | `tech-agent-guardrail` | Where data runs vs. how an agent is governed |
| "We're launching an autonomous agent next month — is it safely governed?" | `tech-agent-guardrail` | `tech-data-deployment` | Same boundary, opposite direction |
| "Design a 90-day pilot for the claims summarizer" | `process-pilot-design` | `process-productionization` | Pilot structuring vs. post-demo production hardening |
| "Refactor this Python function to use a dict lookup" | *(none)* | any of the 16 | Dormancy check — unrelated engineering work must not activate the plugin |
