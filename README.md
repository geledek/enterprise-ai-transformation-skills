# Enterprise AI Transformation Skills

Eight installable skills for diagnosing, designing, governing, and scaling enterprise AI transformation — distilled from 21 flagship research sources published 2024–2026.

---

## Why these skills exist

95% of enterprise GenAI pilots return zero measurable P&L impact. The 5% that capture nearly all the value don't have better models — they operate differently across five layers: Governance, Technology, Process, People, and Strategy.

These skills encode the structural patterns that separate that 5%: decision frameworks, diagnostic tools, and gate criteria drawn from Stanford, MIT, McKinsey, BCG, Deloitte, PwC, Accenture, NIST, EU AI Act, IMDA, and WEF — compressed into formats an AI agent can load and execute.

A skill is a documented, versioned, forkable unit of how the work gets done. The model commoditizes. The skill library compounds.

---

## Who should use these skills

- **Investors** evaluating AI-first companies and AI initiative funding proposals
- **Operators** running AI transformation programs, CoEs, or portfolio pilots
- **Founders** assessing build vs. buy, structuring AI product strategy
- **Boards and executives** needing structured frameworks for AI governance and investment decisions
- **Consultants and advisors** delivering enterprise AI strategy engagements

These skills produce board-ready outputs — not engineering artifacts. No coding background required to use them.

---

## When to use which skill

### By lifecycle stage

| Stage | Skills to use |
|---|---|
| **Concept** — "Should we pursue this AI idea?" | `ai-idea-diagnostic` |
| **Pilot design** — "How do we structure the 90-day test?" | `pilot-design` |
| **Funding gate** — "Should we approve this investment?" | `roi-gate-pwc` |
| **Build vs. buy** — "Should we build this, buy it, or partner?" | `buy-vs-build` |
| **Deployment** — "Are our agents governed correctly?" | `agent-guardrail-imda` |
| **Scaling** — "Is our tech stack ready to scale?" | `stack-diagnostic` |

### Cross-cutting diagnostics

| Diagnostic | When |
|---|---|
| `readiness-conversation` | Any time you need to surface where leadership gaps will block progress |
| `maturity-assessment` | Quarterly or before setting AI strategy — where are we on the maturity curve? |

### Typical executive flow

1. `maturity-assessment` — baseline where the org sits
2. `ai-idea-diagnostic` — gate each new AI concept
3. `pilot-design` — structure the pilot with pre-deployment metrics
4. `roi-gate-pwc` — approve or kill at the funding gate
5. `buy-vs-build` — decide the sourcing model
6. `agent-guardrail-imda` — govern deployed agents
7. `readiness-conversation` — run quarterly to surface people/leadership gaps
8. `stack-diagnostic` — run before any major scaling decision

---

## How to install

### Claude Code (primary)

```bash
# Via Claude Code plugin manager
claude plugin install https://github.com/geledek/enterprise-ai-transformation-skills

# Or manual clone
git clone https://github.com/geledek/enterprise-ai-transformation-skills.git ~/.claude/plugins/enterprise-ai-transformation-skills
```

Then restart Claude Code. Skills activate automatically from their trigger descriptions.

See `INSTALL.md` for full setup, verification steps, and ChatGPT custom GPT adaptation.

---

## How to add your own knowledge

Three forks:

1. **Add references** — copy a wiki extract into `references/`, follow the file shape in `references/_index.md`, update `_index.md`. Skill descriptions reference files by name, not path.

2. **Add cases** — drop a diagnosed case into `skills/ai-idea-diagnostic/cases/` (Markdown, following the existing case format). The diagnostic skill will reference the closest case automatically.

3. **Fork a skill** — copy any `SKILL.md`, rename it, adjust the role instructions and reference pointers for your sector, internal processes, or role-specific context.

---

## Sources

21 flagship sources, 2024–2026:

| ID | Source |
|---|---|
| `stanford-ai-index-2026` | Stanford AI Index 2026 |
| `mit-nanda-2025` | MIT NANDA GenAI Deployment Study 2025 |
| `mckinsey-state-ai-2025` | McKinsey State of AI 2025 |
| `bcg-bffxai-2026` | BCG Build for the Future x AI 2026 |
| `deloitte-ai-leaders-2026` | Deloitte AI Leaders Survey 2026 |
| `pwc-roi-2026` | PwC ROI Report 2026 |
| `pwc-agentic-playbook-2026` | PwC Agentic AI Playbook 2026 |
| `accenture-co-intelligence-2026` | Accenture Co-Intelligence 2026 |
| `accenture-maturity-global` | Accenture AI Maturity Global 2024 |
| `mit-cisr-2024` | MIT CISR AI Maturity Stages 2024 |
| `nist-ai-rmf` | NIST AI Risk Management Framework 1.0 |
| `eu-ai-act-2024` | EU AI Act 2024 |
| `imda-agentic-2026` | IMDA Agentic AI Framework 2026 |
| `wef-rai-2024` | WEF Responsible AI Playbook 2024 |
| `landing-ai-playbook` | Landing AI Enterprise Transformation Playbook |
| `andrew-ng-moats` | Andrew Ng — Three AI Moats |
| `isg-genai-2025` | ISG GenAI Enterprise Research 2025 |
| `bcg-manager-modeling` | BCG Role-Modeling Research 2026 |
| `hiten-shah-skill-library` | Hiten Shah — "Every Company's First AI Strategy Should Be a Skill Library", June 2026 |
| `accenture-five-success` | Accenture Five Success Factors 2025 |
| `wharton-skills-index` | Wharton-Accenture Skills Index 2025 |

See `references/` for curated extracts from each source.

---

## License

MIT — see `LICENSE`.

## Author

Ray Han · June 2026
