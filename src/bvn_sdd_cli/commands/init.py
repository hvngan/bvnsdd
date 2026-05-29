"""`bvn-sdd init` — scaffold the BVN-SDD structure into a project."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Optional

import typer

from .. import _assets
from .._console import error, ok, panel, skip, warn


def _git_init(target: Path) -> bool:
    """Run `git init` in `target` if it is not already a repo. Returns success."""
    if (target / ".git").exists():
        return False
    try:
        subprocess.run(
            ["git", "init"],
            cwd=target,
            check=True,
            capture_output=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        warn("git not available — skipped repository initialization.")
        return False


def init(
    project_name: Optional[str] = typer.Argument(
        None,
        help="Name of the project folder to create. Omit when using --here.",
    ),
    here: bool = typer.Option(
        False, "--here", help="Scaffold into the current directory instead."
    ),
    force: bool = typer.Option(
        False, "--force", help="Overwrite existing files that conflict."
    ),
    no_git: bool = typer.Option(
        False, "--no-git", help="Do not initialize a git repository."
    ),
) -> None:
    """Scaffold .claude/, .bvn-sdd/ and docs/ into a project."""
    if here and project_name:
        error("Pass either a project name or --here, not both.")
        raise typer.Exit(code=1)
    if not here and not project_name:
        error("Provide a project name, or use --here for the current directory.")
        raise typer.Exit(code=1)

    if here:
        target = Path.cwd()
    else:
        target = Path.cwd() / project_name  # type: ignore[arg-type]
        target.mkdir(parents=True, exist_ok=True)

    # Refuse to re-scaffold an existing BVN-SDD project unless forced.
    if (target / ".bvn-sdd").exists() and not force:
        error(
            f"{target / '.bvn-sdd'} already exists. "
            "Use --force to overwrite, or pick a fresh directory."
        )
        raise typer.Exit(code=1)

    try:
        result = _assets.scaffold(target, force=force)
    except FileNotFoundError as exc:
        error(str(exc))
        raise typer.Exit(code=1) from exc

    for path in result.created:
        ok(f"created {path.as_posix()}")
    for path in result.skipped:
        skip(f"skipped (exists) {path.as_posix()}")

    if not no_git:
        if _git_init(target):
            ok("initialized git repository")

    where = "current directory" if here else target.name
    panel(
        "Next steps:\n\n"
        "  1. Open this project in [bold]Claude Code[/bold].\n"
        "  2. (Once per project) run [cyan]/sdd-map[/cyan] to map the codebase.\n"
        "  3. Start a ticket: [cyan]/sdd-new T-001[/cyan]\n"
        "  4. Drive each phase: [cyan]/sdd-spec[/cyan] -> [cyan]/sdd-context[/cyan]"
        " -> [cyan]/sdd-plan[/cyan] ->\n"
        "     [cyan]/sdd-implement[/cyan] -> [cyan]/sdd-test[/cyan]"
        " -> [cyan]/sdd-report[/cyan]\n\n"
        "Each command fills a real artifact under docs/changes/<TICKET>/.",
        title=f"BVN-SDD ready in {where}",
    )
