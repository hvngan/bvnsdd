"""BVN-SDD CLI — entry point and Typer application.

Turns the BVN-SDD V04.2 methodology pack into a runnable workflow:
`bvn-sdd init` scaffolds a project, then Claude Code slash commands
(`/sdd-spec`, `/sdd-plan`, ...) drive each phase.
"""

from __future__ import annotations

import typer

from ._console import print_banner
from ._version import __version__
from .commands import check as check_cmd
from .commands import init as init_cmd

app = typer.Typer(
    name="bvn-sdd",
    help="BVN-SDD CLI — Spec-Driven Development for Claude Code.",
    no_args_is_help=True,
    add_completion=False,
)


def _version_callback(value: bool) -> None:
    if value:
        print_banner(__version__)
        raise typer.Exit()


@app.callback()
def _main(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show the BVN-SDD CLI version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    """BVN-SDD CLI — scaffold and drive the BVN SDD workflow."""


app.command("init", help="Scaffold the BVN-SDD structure into a project.")(init_cmd.init)
app.command("check", help="Check that git and Claude Code are available.")(
    check_cmd.check
)


@app.command("version", help="Show the BVN-SDD CLI version.")
def version() -> None:
    print_banner(__version__)


def main() -> None:
    """Console-script entry point."""
    app()


if __name__ == "__main__":
    main()
