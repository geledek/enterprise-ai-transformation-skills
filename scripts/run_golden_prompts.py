#!/usr/bin/env python3
"""Golden-prompt runner. Executes tests/golden-prompts.md against a live model.

Runs each prompt through `claude -p` with this repo loaded via --plugin-dir,
then asserts:
  - activation rows (the per-bucket tables): the named skill activates, and in
    --full mode the output uses the contracted verdict vocabulary;
  - routing rows ("must NOT misfire" table): the intended skill activates and
    the adjacent skill does not; the dormancy row activates nothing.

This costs API tokens and takes minutes — it is NOT run by CI on push.
Run it before cutting a release, or after editing any frontmatter description
(routing) or role structure (contracts).

Usage:
  python3 scripts/run_golden_prompts.py --list          # parse and show cases, no API calls
  python3 scripts/run_golden_prompts.py --routing       # routing table only (cheap: capped turns)
  python3 scripts/run_golden_prompts.py --full          # everything, uncapped, checks verdict vocab
  python3 scripts/run_golden_prompts.py --only people-tool-selection,general-roi-gate
  python3 scripts/run_golden_prompts.py --model sonnet  # cross-model run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOLDEN = os.path.join(ROOT, "tests", "golden-prompts.md")

# Read-only tools only: skills may consult references/, but must not mutate.
ALLOWED_TOOLS = "Skill Read Glob Grep"


def parse_cases():
    """Return (activation_cases, routing_cases) from golden-prompts.md."""
    activation, routing = [], []
    in_routing = False
    for line in open(GOLDEN):
        if line.startswith("## Routing prompts"):
            in_routing = True
            continue
        if not line.startswith("|") or line.startswith("|-") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if in_routing:
            if len(cells) < 3 or cells[0] in ("Prompt", "---"):
                continue
            prompt = cells[0].strip('"')
            must = m.group(1) if (m := re.search(r"`([a-z0-9-]+)`", cells[1])) else None
            must_not = m.group(1) if (m := re.search(r"`([a-z0-9-]+)`", cells[2])) else "ANY"
            routing.append({"prompt": prompt, "must": must, "must_not": must_not})
        else:
            m = re.match(r"`([a-z0-9-]+)`", cells[0])
            if not m or len(cells) < 3:
                continue
            prompt = cells[1].strip('"')
            vocab_groups = [
                [opt.strip() for opt in grp.split(" / ")]
                for grp in re.findall(r"\*\*(.+?)\*\*", cells[2])
            ]
            activation.append({"skill": m.group(1), "prompt": prompt, "vocab": vocab_groups})
    return activation, routing


def run_claude(prompt: str, model: str | None, max_turns: int | None, timeout: int):
    """Run one headless prompt. Returns (activated_skills, result_text, error)."""
    cmd = [
        "claude", "-p", prompt,
        "--plugin-dir", ROOT,
        "--output-format", "stream-json", "--verbose",
        "--allowedTools", ALLOWED_TOOLS,
    ]
    if model:
        cmd += ["--model", model]
    if max_turns:
        cmd += ["--max-turns", str(max_turns)]
    # Neutral cwd: don't let this repo's CLAUDE.md leak into the routing test.
    with tempfile.TemporaryDirectory() as neutral:
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=timeout, cwd=neutral
            )
        except subprocess.TimeoutExpired:
            return set(), "", "timeout"
    if proc.returncode != 0 and not proc.stdout:
        return set(), "", (proc.stderr or "claude exited non-zero").strip()[:300]

    activated, result_text, result_error = set(), "", None
    for raw in proc.stdout.splitlines():
        try:
            event = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "assistant":
            for block in event.get("message", {}).get("content", []):
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    activated.add(block.get("input", {}).get("skill", "").split(":")[-1])
        elif event.get("type") == "result":
            result_text = event.get("result") or ""
            if event.get("is_error") or event.get("subtype") != "success":
                # A failed run must not masquerade as "skill stayed dormant".
                result_error = f"{event.get('subtype')}: {result_text[:200]}"
    return activated, result_text, result_error


def vocab_hit(options: list[str], text: str) -> bool:
    """True if any option appears in text (hyphen/space interchangeable)."""
    for opt in options:
        pattern = re.escape(opt).replace(r"\-", "[-\\s]").replace(r"\ ", "[-\\s]")
        if re.search(rf"\b{pattern}\b", text):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true", help="show parsed cases, no API calls")
    ap.add_argument("--routing", action="store_true", help="routing table only")
    ap.add_argument("--full", action="store_true", help="activation + verdict vocabulary, uncapped")
    ap.add_argument("--only", help="comma-separated skill slugs to test")
    ap.add_argument("--model", help="model alias to run against (default: your configured model)")
    ap.add_argument("--sleep", type=int, default=15, help="seconds between runs (rate-limit headroom)")
    args = ap.parse_args()

    activation, routing = parse_cases()
    if args.only:
        keep = set(args.only.split(","))
        activation = [c for c in activation if c["skill"] in keep]
        routing = [c for c in routing if c["must"] in keep or c["must_not"] in keep]

    if args.list:
        for c in activation:
            print(f"activate  {c['skill']:35s} vocab groups: {len(c['vocab'])}")
        for c in routing:
            print(f"route     {str(c['must']):35s} not: {c['must_not']}")
        print(f"\n{len(activation)} activation + {len(routing)} routing cases")
        return 0

    failures = []
    run_activation = not args.routing

    if run_activation:
        for c in activation:
            max_turns = None if args.full else 3
            timeout = 600 if args.full else 180
            activated, text, error = run_claude(c["prompt"], args.model, max_turns, timeout)
            time.sleep(args.sleep)
            if error:
                failures.append(f"{c['skill']}: run failed ({error})")
                print(f"ERROR {c['skill']}: {error}")
                continue
            ok = c["skill"] in activated
            if not ok:
                failures.append(f"{c['skill']}: did not activate (activated: {sorted(activated) or 'none'})")
            if args.full and ok:
                for group in c["vocab"]:
                    if not vocab_hit(group, text):
                        ok = False
                        failures.append(f"{c['skill']}: output missing vocabulary {group}")
            print(f"{'PASS' if ok else 'FAIL'}  activate {c['skill']}")

    for c in routing:
        activated, _, error = run_claude(c["prompt"], args.model, 3, 180)
        time.sleep(args.sleep)
        if error:
            failures.append(f"routing '{c['prompt'][:40]}…': run failed ({error})")
            print(f"ERROR routing '{c['prompt'][:40]}…': {error}")
            continue
        ok = True
        if c["must"] and c["must"] not in activated:
            ok = False
            failures.append(f"routing '{c['prompt'][:40]}…': {c['must']} did not activate ({sorted(activated) or 'none'})")
        if c["must_not"] == "ANY":
            if activated:
                ok = False
                failures.append(f"dormancy '{c['prompt'][:40]}…': activated {sorted(activated)}")
        elif c["must_not"] in activated:
            ok = False
            failures.append(f"routing '{c['prompt'][:40]}…': misfired {c['must_not']}")
        print(f"{'PASS' if ok else 'FAIL'}  route    {c['must'] or '(dormancy)'}")

    print()
    if failures:
        print(f"FAIL — {len(failures)} issue(s):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("OK — all golden prompts passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
