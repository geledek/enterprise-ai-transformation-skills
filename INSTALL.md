# Installation Guide

## Claude Code (Primary)

### Option A — Plugin Manager (recommended)

```bash
claude plugin install https://github.com/geledek/enterprise-ai-transformation-skills
```

Restart Claude Code. All 15 skills activate automatically.

### Option B — Manual Clone

```bash
git clone https://github.com/geledek/enterprise-ai-transformation-skills.git \
  ~/.claude/plugins/enterprise-ai-transformation-skills
```

Restart Claude Code — it auto-discovers plugins in `~/.claude/plugins/`.

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
| `use-case-discovery` | "Where do we start with AI?" |
| `data-trust-deployment-pattern` | "Where can this data legally run?" |
| `productionization-playbook` | "How do we move this prototype to production?" |
| `ai-portfolio-observability` | "What is each AI initiative actually returning?" |
| `augmentation-frontline-engagement` | "How do we engage skeptical frontline experts?" |
| `peer-case-library` | "Has anyone else done this before?" |
| `workforce-literacy-curriculum` | "Build a role-based AI literacy curriculum" |

---

## Claude Desktop

1. Open Claude Desktop → **Customize** (left sidebar) → **Plugins** tab
2. Click **Browse plugins** or **Upload custom plugin**
3. Paste this URL when prompted:
   `https://github.com/geledek/enterprise-ai-transformation-skills`
4. Restart Claude Desktop. All 15 skills activate automatically.

Requires a paid plan (Pro, Max, Team, or Enterprise). See [Claude plugin docs](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

---

## ChatGPT

### Option A — Native Skills (if available on your plan)

1. Go to **chatgpt.com → Explore skills** or open Settings → **Skills**
2. Click **Add skill from URL** (if shown) and paste:
   `https://github.com/geledek/enterprise-ai-transformation-skills`

See [OpenAI skills docs](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for current plan availability.

### Option B — Custom GPT (no code required, always available)

1. Create a new GPT at `chat.openai.com/gpts`
2. In **Instructions**, paste the full content of any skill's `SKILL.md`
3. In **Knowledge**, upload the relevant files from `references/`
4. Set the **Conversation Starter** to the skill's trigger phrase
5. Repeat per skill, or combine up to 4 skills into one GPT

Limitation: Custom GPTs don't auto-trigger on phrase matching — you'll need to explicitly invoke the skill in conversation.

---

## Grok CLI

### Option A — Marketplace install

Add this repo as a marketplace source in `~/.grok/config.toml`:

```toml
[[marketplace.sources]]
url = "https://github.com/geledek/enterprise-ai-transformation-skills"
```

Then browse and install from the **Marketplace** tab in the Grok TUI, or run:

```bash
grok plugin install enterprise-ai-transformation-skills
```

### Option B — Manual clone

```bash
git clone https://github.com/geledek/enterprise-ai-transformation-skills.git \
  ~/.grok/plugins/enterprise-ai-transformation-skills
```

Grok auto-discovers plugins in `~/.grok/plugins/`. Skills appear as `/skill-name` slash commands.

See [Grok skills & plugins docs](https://docs.x.ai/build/features/skills-plugins-marketplaces).

---

## Claude.ai Projects (no install required)

For users without a paid Claude Code or Desktop plan:

1. Create a new **Project** at [claude.ai](https://claude.ai)
2. Open **Project Instructions**
3. Paste the contents of any skill's `README.md` from this repo
4. Upload relevant files from `references/` as Project Knowledge

This loads one skill per Project. Skills activate on their trigger phrases.

---

## Updating / Syncing References

Reference files in `references/` are snapshots. To update:

```bash
git pull origin main
```

If you've forked the repo and added your own references, merge upstream changes selectively — don't overwrite your local additions.
