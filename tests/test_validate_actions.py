"""
Name: test_validate_actions.py
Purpose: Proves the composite-action validator actually catches the breakage
         classes it exists for -- a validator that never fails is worse than
         no validator.
Created: 2026-09-19
Author: Michael K. Steinberg
"""

import importlib.util
import textwrap
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "validate_actions", _REPO_ROOT / "scripts" / "validate_actions.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = _load()

VALID = """\
name: Demo
description: A demo action.
inputs:
  token:
    description: A token.
    required: false
    default: ""
runs:
  using: composite
  steps:
    - name: Use it
      shell: bash
      run: echo "${{ inputs.token }}"
"""


def _write(tmp_path: Path, body: str) -> Path:
    action_dir = tmp_path / "actions" / "demo"
    action_dir.mkdir(parents=True)
    action_yml = action_dir / "action.yml"
    action_yml.write_text(textwrap.dedent(body))
    return action_yml


def _problems(tmp_path: Path, body: str) -> list[str]:
    return validator.validate_action(_write(tmp_path, body), tmp_path)


def test_a_well_formed_action_has_no_problems(tmp_path: Path) -> None:
    assert _problems(tmp_path, VALID) == []


def test_catches_an_undeclared_input_reference(tmp_path: Path) -> None:
    # The headline breakage class: an input is renamed in one place and not
    # the other, and every consuming repo's E2E discovers it at runtime.
    problems = _problems(tmp_path, VALID.replace("inputs.token", "inputs.tokne"))

    assert any("undeclared input 'tokne'" in p for p in problems)


def test_accepts_bracket_style_input_references(tmp_path: Path) -> None:
    problems = _problems(tmp_path, VALID.replace("inputs.token", "inputs['token']"))

    assert problems == []


def test_catches_an_undeclared_bracket_reference(tmp_path: Path) -> None:
    problems = _problems(tmp_path, VALID.replace("inputs.token", "inputs['nope']"))

    assert any("undeclared input 'nope'" in p for p in problems)


def test_ignores_non_input_expressions(tmp_path: Path) -> None:
    # runner.environment, github.*, env.* and friends are not our business.
    problems = _problems(
        tmp_path, VALID.replace("${{ inputs.token }}", "${{ runner.environment }}")
    )

    assert problems == []


def test_catches_malformed_yaml(tmp_path: Path) -> None:
    problems = _problems(tmp_path, "name: [unclosed\n")

    assert any("does not parse as YAML" in p for p in problems)


@pytest.mark.parametrize("field", ["name", "description", "runs"])
def test_catches_missing_metadata(tmp_path: Path, field: str) -> None:
    body = "\n".join(line for line in VALID.splitlines() if not line.startswith(f"{field}:"))
    problems = _problems(tmp_path, body + "\n")

    assert any(f"missing required metadata field '{field}'" in p for p in problems)


def test_catches_a_non_composite_action(tmp_path: Path) -> None:
    problems = _problems(tmp_path, VALID.replace("using: composite", "using: node20"))

    assert any("expected 'composite'" in p for p in problems)


def test_catches_a_run_step_without_a_shell(tmp_path: Path) -> None:
    # A composite run step with no `shell:` fails at runtime, in the consuming
    # repo -- exactly the class this validator exists to move left.
    problems = _problems(tmp_path, VALID.replace("      shell: bash\n", ""))

    assert any("has 'run' but no 'shell'" in p for p in problems)


def test_catches_empty_steps(tmp_path: Path) -> None:
    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps: []
        """,
    )

    assert any("runs.steps is missing or empty" in p for p in problems)


def test_catches_a_missing_local_action_reference(tmp_path: Path) -> None:
    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - uses: ./actions/does-not-exist
        """,
    )

    assert any("has no action.yml" in p for p in problems)


def test_accepts_a_local_action_that_exists(tmp_path: Path) -> None:
    other = tmp_path / "actions" / "other"
    other.mkdir(parents=True)
    (other / "action.yml").write_text(VALID)

    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - uses: ./actions/other
        """,
    )

    assert problems == []


def test_ignores_published_action_references(tmp_path: Path) -> None:
    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - uses: actions/checkout@v7
        """,
    )

    assert problems == []


def test_catches_a_missing_script(tmp_path: Path) -> None:
    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - shell: bash
              run: bash wait-for-db.sh
        """,
    )

    assert any("script that does not exist: wait-for-db.sh" in p for p in problems)


def test_accepts_a_script_that_exists(tmp_path: Path) -> None:
    action_yml = _write(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - shell: bash
              run: bash wait-for-db.sh
        """,
    )
    (action_yml.parent / "wait-for-db.sh").write_text("#!/usr/bin/env bash\n")

    assert validator.validate_action(action_yml, tmp_path) == []


def test_ignores_absolute_script_paths(tmp_path: Path) -> None:
    # `docker compose exec database sh /update.sh` runs inside the container;
    # the path is not this repo's to resolve. setup-hive really does this.
    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - shell: bash
              run: docker compose exec -T database sh /update.sh
        """,
    )

    assert problems == []


def test_ignores_templated_script_paths(tmp_path: Path) -> None:
    problems = _problems(
        tmp_path,
        """\
        name: Demo
        description: A demo action.
        runs:
          using: composite
          steps:
            - shell: bash
              run: bash $SCRIPT_DIR/run.sh
        """,
    )

    assert problems == []


def test_catches_an_input_without_a_description(tmp_path: Path) -> None:
    problems = _problems(tmp_path, VALID.replace("    description: A token.\n", ""))

    assert any("input 'token' has no description" in p for p in problems)


def test_catches_an_optional_input_without_a_default(tmp_path: Path) -> None:
    # Optional-with-no-default silently reads as "" at runtime; the difference
    # between a documented default and an empty string is a real bug source.
    problems = _problems(tmp_path, VALID.replace('    default: ""\n', ""))

    assert any("optional but declares no default" in p for p in problems)


def test_every_real_action_in_this_repo_validates() -> None:
    """The actual regression gate -- runs against actions/ as committed."""
    action_files = sorted((_REPO_ROOT / "actions").glob("*/action.yml"))
    assert action_files, "no composite actions found"

    problems: list[str] = []
    for action_yml in action_files:
        problems.extend(validator.validate_action(action_yml, _REPO_ROOT))

    assert problems == [], "\n".join(problems)
