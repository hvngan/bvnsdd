"""Tests for `bvn-sdd init` scaffolding."""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from bvn_sdd_cli import app
from bvn_sdd_cli import _assets

runner = CliRunner()


# Files that must exist after a fresh init, relative to the project root.
EXPECTED_FILES = [
    ".claude/CLAUDE.md",
    ".claude/settings.json",
    ".claude/rules/00-safety.md",
    ".claude/commands/sdd-spec.md",
    ".claude/commands/sdd-new.md",
    ".bvn-sdd/config.yml",
    ".bvn-sdd/templates/spec-pack.md",
    ".bvn-sdd/templates/report.md",
    ".bvn-sdd/scripts/powershell/create-ticket.ps1",
    ".bvn-sdd/scripts/bash/create-ticket.sh",
    "docs/QUICKSTART.md",
    "docs/architecture/system-map.md",
    "docs/standards/coding.md",
    "docs/maintenance/failure-mode-index.md",
    "docs/maintenance/pattern-library.md",
]


def test_scaffold_creates_expected_tree(tmp_path: Path) -> None:
    result = _assets.scaffold(tmp_path)
    assert result.created, "nothing was created"
    for rel in EXPECTED_FILES:
        target = tmp_path / rel
        assert target.is_file(), f"missing {rel}"
        assert target.stat().st_size > 0, f"empty {rel}"


def test_scaffold_renames_claude_dir(tmp_path: Path) -> None:
    _assets.scaffold(tmp_path)
    assert (tmp_path / ".claude").is_dir()
    # The unhidden source name must not leak into the project.
    assert not (tmp_path / "claude").exists()


def test_scaffold_skips_existing_without_force(tmp_path: Path) -> None:
    (tmp_path / ".claude").mkdir()
    sentinel = tmp_path / ".claude" / "CLAUDE.md"
    sentinel.write_text("DO NOT OVERWRITE", encoding="utf-8")

    result = _assets.scaffold(tmp_path)

    assert sentinel.read_text(encoding="utf-8") == "DO NOT OVERWRITE"
    assert Path(".claude/CLAUDE.md") in result.skipped


def test_scaffold_force_overwrites(tmp_path: Path) -> None:
    (tmp_path / ".claude").mkdir()
    sentinel = tmp_path / ".claude" / "CLAUDE.md"
    sentinel.write_text("DO NOT OVERWRITE", encoding="utf-8")

    _assets.scaffold(tmp_path, force=True)

    assert "DO NOT OVERWRITE" not in sentinel.read_text(encoding="utf-8")


def test_init_command_creates_project(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(
        app, ["init", "demo-proj", "--no-git"], catch_exceptions=False
    )
    assert result.exit_code == 0
    assert "BVN-SDD ready" in result.stdout
    assert (tmp_path / "demo-proj" / ".claude" / "CLAUDE.md").is_file()
    assert (tmp_path / "demo-proj" / ".bvn-sdd" / "templates" / "spec-pack.md").is_file()


def test_init_requires_name_or_here() -> None:
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 1
