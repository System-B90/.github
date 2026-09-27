"""
Name: test_plugins.py
Purpose: Keep the Claude Code marketplace consistent: every listed plugin
    exists, its manifest and skill agree on the name, and its SessionStart
    hook script is where plugin.json points.
Created: 2026-09-27
Author: Michael K. Steinberg
"""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
PLUGINS = MARKETPLACE["plugins"]


@pytest.mark.parametrize("entry", PLUGINS, ids=[p["name"] for p in PLUGINS])
def test_plugin_is_complete(entry: dict) -> None:
    plugin_dir = ROOT / entry["source"]
    manifest = json.loads(
        (plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    assert manifest["name"] == entry["name"]

    skill = plugin_dir / "skills" / entry["name"] / "SKILL.md"
    front = re.match(r"^---\n(.*?)\n---\n", skill.read_text(encoding="utf-8"), re.DOTALL)
    assert front, f"{skill} has no frontmatter"
    assert f"name: {entry['name']}" in front.group(1)
    assert "description: " in front.group(1)

    for group in manifest.get("hooks", {}).values():
        for matcher in group:
            for hook in matcher["hooks"]:
                script = re.search(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\"]+)", hook["command"])
                assert script and (plugin_dir / script.group(1)).is_file()


def test_plugin_names_are_unique() -> None:
    names = [p["name"] for p in PLUGINS]
    assert len(names) == len(set(names))
