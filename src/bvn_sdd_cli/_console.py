"""Shared Rich console helpers for consistent CLI output."""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# BVN-SDD brand accent used across the CLI.
ACCENT = "bold cyan"

BANNER = r"""
 ____  _   _ _   _       ____  ____  ____
| __ )| | | | \ | |     / ___||  _ \|  _ \
|  _ \| | | |  \| |_____\___ \| | | | | | |
| |_) | |_| | |\  |_____|___) | |_| | |_| |
|____/ \___/|_| \_|     |____/|____/|____/
""".strip(
    "\n"
)


def print_banner(version: str) -> None:
    """Print the BVN-SDD banner with the current version."""
    text = Text(BANNER, style=ACCENT)
    subtitle = Text(
        f"Spec-Driven Development CLI for Claude Code - v{version}",
        style="dim",
    )
    console.print(text)
    console.print(subtitle)


# ASCII-only markers so output renders on legacy Windows consoles (cp1252).
def ok(message: str) -> None:
    console.print(f"[green]+[/green] {message}")


def skip(message: str) -> None:
    console.print(f"[yellow]-[/yellow] {message}")


def warn(message: str) -> None:
    console.print(f"[yellow]![/yellow] {message}")


def error(message: str) -> None:
    console.print(f"[red]x[/red] {message}")


def panel(body: str, title: str) -> None:
    console.print(Panel(body, title=title, border_style="cyan", expand=False))
