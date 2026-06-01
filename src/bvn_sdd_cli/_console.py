"""Shared Rich console helpers for consistent CLI output."""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

console = Console()

ACCENT = "bold cyan"

BANNER = r"""
 ____  _   _ _   _       ____  ____  ____
| __ )| | | | \ | |     / ___||  _ \|  _ \
|  _ \| | | |  \| |_____\___ \| | | | | | |
| |_) | |_| | |\  |_____|___) | |_| | |_| |
|____/ \___/|_| \_|     |____/|____/|____/
""".strip("\n")

FULL_NAME = "Brycen Viet Nam — Spec-Driven Development for Claude Code"


def print_banner(version: str) -> None:
    """Print the BVN-SDD banner with version."""
    console.print()
    console.print(Text(BANNER, style=ACCENT))
    console.print(Text(f"  {FULL_NAME}", style="dim"))
    console.print(Text(f"  v{version}", style="bold"))
    console.print()


def rule(title: str = "") -> None:
    """Print a horizontal divider, optionally with a section title."""
    console.print(Rule(title, style="dim cyan"))


def ok(message: str) -> None:
    console.print(f"  [green]✓[/green]  {message}")


def skip(message: str) -> None:
    console.print(f"  [yellow]–[/yellow]  [dim]{message}[/dim]")


def warn(message: str) -> None:
    console.print(f"  [yellow]![/yellow]  {message}")


def error(message: str) -> None:
    console.print(f"  [red]✗[/red]  {message}")


def info(message: str) -> None:
    console.print(f"  [cyan]·[/cyan]  {message}")


def panel(body: str, title: str) -> None:
    console.print(Panel(body, title=title, border_style="cyan", expand=False, padding=(1, 2)))
