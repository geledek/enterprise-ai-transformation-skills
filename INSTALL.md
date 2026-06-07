# Installation Guide

## Claude Code (Primary)

### Option A — Plugin Manager

```bash
claude plugin install https://github.com/geledek/enterprise-ai-transformation-skills
```

Restart Claude Code. All 8 skills activate automatically.

### Option B — Manual Clone

```bash
git clone https://github.com/geledek/enterprise-ai-transformation-skills.git \
  ~/.claude/plugins/enterprise-ai-transformation-skills
```

Then in Claude Code settings, add the plugin path, or restart — Claude Code auto-discovers plugins in `~/.claude/plugins/`.

### Verify Installation

After restart, test each skill with its trigger phrase:

| Skill | Trigger phrase |
|---|---|
| `ai-idea-diagnostic` | "Should we pursue this AI idea?" |
| `pilot-design` | "Design a 90-day AI pilot for [X]" |
| `roi-gate-pwc` | "Run the ROI gate on this AI investment" |
| `agent-guardrail-imda` | "Check governance on this AI agent deployment" |
| `stack-diagnostic` | "Diagnose our AI tech stack" |
| `buy-vs-build` | "Should we build or buy this AI capability?" |
| `readiness-conversation` | "Surface AI readiness gaps in our leadership team" |
| `maturity-assessment` | "Where are we on the AI maturity curve?" |

---

## ChatGPT Custom GPT Adaptation

These skills can be adapted as a ChatGPT Custom GPT (no code required).

1. Create a new GPT at `chat.openai.com/gpts`
2. In **Instructions**, paste the full content of the `SKILL.md` you want to adapt
3. In **Knowledge**, upload the relevant reference files from `references/`
4. Set the **Conversation Starter** to the skill's primary trigger phrase
5. Repeat per skill, or combine up to 4 skills into one GPT using role-selection prompt logic

Limitation: Custom GPTs don't auto-trigger on phrase pattern-matching the way Claude Code plugins do — you'll need to explicitly invoke the skill in conversation.

---

## Updating / Syncing References

Reference files in `references/` are snapshots. To update:

```bash
git pull origin main
```

If you've forked the repo and added your own references, merge upstream changes selectively — don't overwrite your local additions.
