#!/usr/bin/env python3
"""Repo consistency validator. Run from the repo root: python3 scripts/validate.py

Checks:
  1. Every backticked `*.md` pointer in a SKILL.md resolves to a file in
     references/ or in the skill's own directory (e.g. cases/).
  2. references/_index.md main-table consumer columns (Primary for skill +
     Also consulted by) match the actual citations in SKILL.md files.
  3. Every .md file in references/ (except _index.md, queries/) appears in
     _index.md, and _index.md lists no phantom files.
  4. Skill lists in .claude-plugin/plugin.json and marketplace.json match the
     skills/ directories on disk, and each other.
  5. plugin.json version == marketplace.json metadata.version.
  6. Every skill has SKILL.md + README.md; frontmatter `name` matches the
     directory name; `description` present and <= 1024 chars.
  7. WARN (non-fatal) when a SKILL.md body exceeds ~4K tokens — skills should
     stay loadable in one gulp; density over completeness.

Exits non-zero with a list of failures if anything is inconsistent.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_SIZE_BUDGET = 16_000  # chars, ~4K tokens
errors = []
warnings = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def frontmatter(text: str) -> dict:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    fields = {}
    if m:
        for line in m.group(1).splitlines():
            fm = re.match(r"([a-z-]+):\s*(.*)", line)
            if fm:
                fields[fm.group(1)] = fm.group(2).strip()
    return fields


# ---- collect skills and their reference citations ----------------------
skills_dir = os.path.join(ROOT, "skills")
skill_names = sorted(
    d for d in os.listdir(skills_dir)
    if os.path.isdir(os.path.join(skills_dir, d))
)

cites: dict[str, set[str]] = {}  # reference filename -> set of skill slugs
for skill in skill_names:
    sdir = os.path.join(skills_dir, skill)
    skill_md = os.path.join(sdir, "SKILL.md")
    readme = os.path.join(sdir, "README.md")

    # check 6: required files + frontmatter
    if not os.path.isfile(readme):
        err(f"skills/{skill}: missing README.md")
    if not os.path.isfile(skill_md):
        err(f"skills/{skill}: missing SKILL.md")
        continue
    body = open(skill_md).read()
    fm = frontmatter(body)
    if fm.get("name") != skill:
        err(f"skills/{skill}/SKILL.md: frontmatter name {fm.get('name')!r} != directory name")
    desc = fm.get("description", "")
    if not desc:
        err(f"skills/{skill}/SKILL.md: missing frontmatter description")
    elif len(desc) > 1024:
        err(f"skills/{skill}/SKILL.md: description is {len(desc)} chars (limit 1024)")

    # check 7: size budget (warning only)
    if len(body) > SKILL_SIZE_BUDGET:
        warn(
            f"skills/{skill}/SKILL.md is {len(body):,} chars "
            f"(budget {SKILL_SIZE_BUDGET:,} ≈ 4K tokens) — consider moving detail to references/ or cases/"
        )

    # check 1: every backticked .md pointer resolves
    for ref in set(re.findall(r"`([a-z0-9-]+\.md)`", body)):
        in_references = os.path.isfile(os.path.join(ROOT, "references", ref))
        in_skill_dir = any(
            ref in files for _, _, files in os.walk(sdir)
        )
        if in_references:
            cites.setdefault(ref, set()).add(skill)
        elif not in_skill_dir:
            err(f"skills/{skill}/SKILL.md: cites `{ref}` — not found in references/ or the skill directory")

# ---- check 2 + 3: _index.md accuracy ------------------------------------
index_path = os.path.join(ROOT, "references", "_index.md")
indexed_files: set[str] = set()
for line in open(index_path):
    m = re.match(r"\| `([a-z0-9-]+\.md)` \|", line)
    if not m:
        continue
    fname = m.group(1)
    indexed_files.add(fname)
    cells = [c.strip() for c in line.rstrip().split("|")]
    if len(cells) != 6:  # additional-references table has no consumer columns
        continue
    primary, also = cells[3], cells[4]
    claimed = set() if primary == "—" else {primary}
    if not also.startswith("—"):
        claimed |= {s.strip() for s in also.split(",") if s.strip()}
    unknown = claimed - set(skill_names)
    if unknown:
        err(f"_index.md: `{fname}` row names unknown skills: {sorted(unknown)}")
    actual = cites.get(fname, set())
    if claimed != actual:
        err(
            f"_index.md: `{fname}` consumer drift — "
            f"index says {sorted(claimed) or '—'}, SKILL.md files cite {sorted(actual) or '—'}"
        )

disk_files = {
    f for f in os.listdir(os.path.join(ROOT, "references"))
    if f.endswith(".md") and f != "_index.md"
}
for f in sorted(disk_files - indexed_files):
    err(f"_index.md: references/{f} exists on disk but is not listed in the index")
for f in sorted(indexed_files - disk_files):
    err(f"_index.md: lists `{f}` but no such file exists in references/")

# ---- check 4 + 5: plugin manifests ---------------------------------------
plugin = json.load(open(os.path.join(ROOT, ".claude-plugin", "plugin.json")))
market = json.load(open(os.path.join(ROOT, ".claude-plugin", "marketplace.json")))

plugin_skills = {os.path.basename(p.rstrip("/")) for p in plugin.get("skills", [])}
market_skills = {
    os.path.basename(p.rstrip("/"))
    for entry in market.get("plugins", [])
    for p in entry.get("skills", [])
}
if plugin_skills != set(skill_names):
    err(
        f"plugin.json skill list drift — missing {sorted(set(skill_names) - plugin_skills) or 'none'}, "
        f"phantom {sorted(plugin_skills - set(skill_names)) or 'none'}"
    )
if market_skills != set(skill_names):
    err(
        f"marketplace.json skill list drift — missing {sorted(set(skill_names) - market_skills) or 'none'}, "
        f"phantom {sorted(market_skills - set(skill_names)) or 'none'}"
    )

pv = plugin.get("version")
mv = market.get("metadata", {}).get("version")
if pv != mv:
    err(f"version drift — plugin.json has {pv!r}, marketplace.json has {mv!r}")

# ---- report ---------------------------------------------------------------
for w in warnings:
    print(f"  WARN - {w}")
if errors:
    print(f"FAIL — {len(errors)} issue(s):\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK — {len(skill_names)} skills, {len(disk_files)} references, all pointers and manifests consistent")
