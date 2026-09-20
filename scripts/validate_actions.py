#!/usr/bin/env python3
"""
Name: validate_actions.py
Purpose: Structural validation for this repo's composite actions. Catches the
         breakage class that otherwise surfaces only when a consuming repo's
         E2E run goes red: a renamed input, a moved script, a malformed
         action.yml.
Created: 2026-09-19
Author: Michael K. Steinberg

Usage: python scripts/validate_actions.py [actions-dir]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

# `inputs.foo`, `inputs['foo']` and `inputs["foo"]` inside a ${{ }} expression.
_INPUT_REF = re.compile(r"inputs\s*(?:\.\s*([A-Za-z_][\w-]*)|\[\s*['\"]([^'\"]+)['\"]\s*\])")
_EXPRESSION = re.compile(r"\$\{\{(.*?)\}\}", re.DOTALL)

# Steps may legitimately reference a local path, a published action, or a
# docker image. Only the first is checkable from inside this repo.
_LOCAL_USES = re.compile(r"^\./")

REQUIRED_METADATA = ("name", "description", "runs")


def _walk_strings(node: Any) -> list[str]:
    """Every string anywhere in the parsed YAML tree."""
    if isinstance(node, str):
        return [node]
    if isinstance(node, dict):
        return [s for value in node.values() for s in _walk_strings(value)]
    if isinstance(node, list):
        return [s for item in node for s in _walk_strings(item)]
    return []


def _referenced_inputs(action: dict) -> set[str]:
    names: set[str] = set()
    for text in _walk_strings(action):
        for expression in _EXPRESSION.findall(text):
            for dotted, bracketed in _INPUT_REF.findall(expression):
                names.add(dotted or bracketed)
    return names


def _referenced_scripts(action: dict, action_dir: Path) -> list[tuple[str, Path]]:
    """Script paths a `run:` block invokes relative to the action directory."""
    found: list[tuple[str, Path]] = []
    steps = (action.get("runs") or {}).get("steps") or []
    for step in steps:
        run = step.get("run") if isinstance(step, dict) else None
        if not isinstance(run, str):
            continue
        for match in re.finditer(r"(?:bash|sh)\s+(\S+\.sh)", run):
            raw = match.group(1)
            if "${{" in raw or "$" in raw:
                continue  # templated path; not statically resolvable
            if raw.startswith("/"):
                # Absolute paths run inside a container, not from this repo --
                # e.g. `docker compose exec database sh /update.sh`. Nothing
                # here can confirm they exist, and they are not our files.
                continue
            found.append((raw, (action_dir / raw).resolve()))
    return found


def validate_action(action_yml: Path, repo_root: Path) -> list[str]:
    """Returns a list of human-readable problems; empty means valid."""
    problems: list[str] = []
    rel = action_yml.relative_to(repo_root)

    try:
        action = yaml.safe_load(action_yml.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        return [f"{rel}: does not parse as YAML: {error}"]

    if not isinstance(action, dict):
        return [f"{rel}: top level is not a mapping"]

    for field in REQUIRED_METADATA:
        if field not in action:
            problems.append(f"{rel}: missing required metadata field '{field}'")

    runs = action.get("runs")
    if isinstance(runs, dict):
        if runs.get("using") != "composite":
            problems.append(f"{rel}: runs.using is {runs.get('using')!r}, expected 'composite'")
        steps = runs.get("steps")
        if not isinstance(steps, list) or not steps:
            problems.append(f"{rel}: runs.steps is missing or empty")
        else:
            for index, step in enumerate(steps):
                if not isinstance(step, dict):
                    problems.append(f"{rel}: runs.steps[{index}] is not a mapping")
                    continue
                if "run" in step and step.get("shell") is None:
                    # A composite `run:` step without `shell:` fails at
                    # runtime, in the consuming repo, not here.
                    problems.append(f"{rel}: runs.steps[{index}] has 'run' but no 'shell'")
                uses = step.get("uses")
                if isinstance(uses, str) and _LOCAL_USES.match(uses):
                    target = (repo_root / uses[2:]).resolve()
                    if (
                        not (target / "action.yml").exists()
                        and not (target / "action.yaml").exists()
                    ):
                        problems.append(
                            f"{rel}: runs.steps[{index}] uses '{uses}', which has no action.yml"
                        )

    declared = set((action.get("inputs") or {}).keys())
    for name in sorted(_referenced_inputs(action)):
        if name not in declared:
            problems.append(
                f"{rel}: references undeclared input '{name}' "
                f"(declared: {', '.join(sorted(declared)) or 'none'})"
            )

    for raw, resolved in _referenced_scripts(action, action_yml.parent):
        if not resolved.exists():
            problems.append(f"{rel}: runs a script that does not exist: {raw}")

    for name, spec in (action.get("inputs") or {}).items():
        if not isinstance(spec, dict):
            problems.append(f"{rel}: input '{name}' is not a mapping")
            continue
        if "description" not in spec:
            problems.append(f"{rel}: input '{name}' has no description")
        if spec.get("required") is False and "default" not in spec:
            # Optional with no default reads as "" at runtime; making that
            # explicit is the difference between a documented default and a
            # silent empty string.
            problems.append(f"{rel}: input '{name}' is optional but declares no default")

    return problems


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    actions_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else repo_root / "actions"

    action_files = sorted(actions_dir.glob("*/action.yml")) + sorted(
        actions_dir.glob("*/action.yaml")
    )
    if not action_files:
        print(f"No composite actions found under {actions_dir}", file=sys.stderr)
        return 1

    problems: list[str] = []
    for action_yml in action_files:
        found = validate_action(action_yml, repo_root)
        status = "FAIL" if found else "ok"
        print(f"{status}: {action_yml.relative_to(repo_root)}")
        problems.extend(found)

    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    print(f"\nAll {len(action_files)} composite actions validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
