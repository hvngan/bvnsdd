"""`bvn-sdd check` — verify the tools the workflow relies on are present."""

from __future__ import annotations

import shutil

from rich.table import Table

from .._console import console, panel, rule

TOOLS = [
    (
        "git",
        "Version control — tracks all SDD artifacts per ticket",
        "https://git-scm.com/downloads",
    ),
    (
        "claude",
        "Claude Code CLI — executes /sdd-* slash commands",
        "https://claude.ai/code",
    ),
]


def check() -> None:
    """Report which prerequisite tools are installed and how to get missing ones."""
    rule("Brycen Viet Nam SDD — Prerequisites")
    console.print()

    table = Table(
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
        show_lines=False,
        expand=False,
        padding=(0, 1),
    )
    table.add_column("Tool", style="bold", min_width=8)
    table.add_column("Status", min_width=14)
    table.add_column("Purpose")

    missing: list[tuple[str, str]] = []

    for name, purpose, install_url in TOOLS:
        path = shutil.which(name)
        if path:
            status = f"[green]✓  found[/green]"
        else:
            status = "[red]✗  missing[/red]"
            missing.append((name, install_url))
        table.add_row(name, status, purpose)

    console.print(table)
    console.print()

    if not missing:
        console.print(
            "  [green]✓[/green]  All prerequisites are installed."
            " Run [cyan]bvn-sdd init[/cyan] to scaffold a project.\n"
        )
    else:
        console.print("  [red]✗[/red]  The following tools are missing:\n")
        for name, url in missing:
            console.print(f"      [bold]{name}[/bold]  →  {url}")
        console.print()
        console.print(
            "  Install the missing tools above, then re-run [cyan]bvn-sdd check[/cyan].\n"
        )
