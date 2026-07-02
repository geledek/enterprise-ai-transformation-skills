#!/usr/bin/env python3
"""Bump the plugin version in every place it lives.

Usage: python3 scripts/bump_version.py 0.4.0

Updates .claude-plugin/plugin.json, .claude-plugin/marketplace.json, and
stamps the CHANGELOG.md `## [Unreleased]` heading with the version and
today's date. Refuses to run if there is no [Unreleased] section or the
version is not newer than the current one.
"""

import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2 or not re.fullmatch(r"\d+\.\d+\.\d+", sys.argv[1]):
        fail(f"usage: {sys.argv[0]} <major.minor.patch>")
    new = sys.argv[1]

    plugin_path = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    market_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    changelog_path = os.path.join(ROOT, "CHANGELOG.md")

    plugin = json.load(open(plugin_path))
    current = plugin["version"]
    if tuple(map(int, new.split("."))) <= tuple(map(int, current.split("."))):
        fail(f"new version {new} is not newer than current {current}")

    changelog = open(changelog_path).read()
    if "## [Unreleased]" not in changelog:
        fail("CHANGELOG.md has no ## [Unreleased] section to release")

    # plugin.json — rewrite via json to keep it canonical
    plugin["version"] = new
    with open(plugin_path, "w") as f:
        json.dump(plugin, f, indent=2, ensure_ascii=False)
        f.write("\n")

    market = json.load(open(market_path))
    market["metadata"]["version"] = new
    with open(market_path, "w") as f:
        json.dump(market, f, indent=2, ensure_ascii=False)
        f.write("\n")

    today = datetime.date.today().isoformat()
    changelog = changelog.replace("## [Unreleased]", f"## [{new}] — {today}", 1)
    open(changelog_path, "w").write(changelog)

    print(f"bumped {current} -> {new} in plugin.json, marketplace.json, CHANGELOG.md")
    print("review the diff, then commit with e.g.:")
    print(f'  git commit -am "release: {new}"')


if __name__ == "__main__":
    main()
