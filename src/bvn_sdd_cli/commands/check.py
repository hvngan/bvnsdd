"""`bvn-sdd check` — verify the tools the workflow relies on are present."""

from __future__ import annotations

import shutil

from rich.table import Table

from .._console import console

# Tools the BVN-SDD workflow expects on PATH. `claude` is required to run the
# slash commands; `git` is recommended so artifacts are version-controlled.
TOOLS = [
    ("git", "Version control for SDD artifacts", True),
    ("claude", "Claude Code CLI - runs the /sdd-* slash commands", True),
]


def check() -> None:
    """Report which prerequisite tools are installed."""
    table = Table(title="BVN-SDD prerequisites", title_style="bold cyan")
    table.add_column("Tool")
    table.add_column("Status")
    table.add_column("Purpose")

    all_ok = True
    for name, purpose, _recommended in TOOLS:
        path = shutil.which(name)
        if path:
            status = "[green]found[/green]"
        else:
            status = "[yellow]missing[/yellow]"
            all_ok = False
        table.add_row(name, status, purpose)

    console.print(table)
    if all_ok:
        console.print("[green]+[/green] All prerequisites are available.")
    else:
        console.print(
            "[yellow]![/yellow] Some tools are missing. "
            "Install them to use the full BVN-SDD workflow."
        )
