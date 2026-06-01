"""`bvn-sdd init` — scaffold the BVN-SDD structure into a project."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Optional

import typer

from .. import _assets
from .._console import console, error, ok, panel, skip, warn

_NEXT_STEPS: dict[str, str] = {
    "vi": (
        "Bước tiếp theo:\n\n"
        "  1. Mở dự án trong [bold]Claude Code[/bold].\n"
        "  2. (1 lần/dự án) Chạy [cyan]/sdd-map[/cyan] để AI hiểu codebase.\n"
        "  3. Tạo ticket: [cyan]/sdd-new T-001[/cyan]\n"
        "  4. Chạy từng phase:\n"
        "     [cyan]/sdd-spec[/cyan] → [cyan]/sdd-rightsize[/cyan] → [cyan]/sdd-context[/cyan]\n"
        "     → [cyan]/sdd-plan[/cyan] → [cyan]/sdd-implement[/cyan]\n"
        "     → [cyan]/sdd-test[/cyan] → [cyan]/sdd-blackbox[/cyan] → [cyan]/sdd-report[/cyan]\n\n"
        "Kết quả mỗi lệnh nằm trong docs/changes/<TICKET>/\n"
        "Xem docs/QUICKSTART.md để bắt đầu nhanh."
    ),
    "en": (
        "Next steps:\n\n"
        "  1. Open this project in [bold]Claude Code[/bold].\n"
        "  2. (Once per project) run [cyan]/sdd-map[/cyan] to map the codebase.\n"
        "  3. Start a ticket: [cyan]/sdd-new T-001[/cyan]\n"
        "  4. Drive each phase:\n"
        "     [cyan]/sdd-spec[/cyan] → [cyan]/sdd-rightsize[/cyan] → [cyan]/sdd-context[/cyan]\n"
        "     → [cyan]/sdd-plan[/cyan] → [cyan]/sdd-implement[/cyan]\n"
        "     → [cyan]/sdd-test[/cyan] → [cyan]/sdd-blackbox[/cyan] → [cyan]/sdd-report[/cyan]\n\n"
        "Each command fills a real artifact under docs/changes/<TICKET>/\n"
        "See docs/QUICKSTART.md to get started quickly."
    ),
    "ja": (
        "次のステップ:\n\n"
        "  1. このプロジェクトを [bold]Claude Code[/bold] で開きます。\n"
        "  2. (プロジェクトごとに1回) [cyan]/sdd-map[/cyan] でコードベースをマップします。\n"
        "  3. チケットを開始: [cyan]/sdd-new T-001[/cyan]\n"
        "  4. 各フェーズを実行:\n"
        "     [cyan]/sdd-spec[/cyan] → [cyan]/sdd-rightsize[/cyan] → [cyan]/sdd-context[/cyan]\n"
        "     → [cyan]/sdd-plan[/cyan] → [cyan]/sdd-implement[/cyan]\n"
        "     → [cyan]/sdd-test[/cyan] → [cyan]/sdd-blackbox[/cyan] → [cyan]/sdd-report[/cyan]\n\n"
        "各コマンドの結果は docs/changes/<TICKET>/ に保存されます。\n"
        "docs/QUICKSTART.md をご覧ください。"
    ),
}


def _prompt_language() -> str:
    """Interactive language selector. Returns 'vi', 'en', or 'ja'."""
    console.print("\n[bold]Select language / 言語を選択 / Chọn ngôn ngữ:[/bold]")
    console.print("  [cyan]1[/cyan]  Tiếng Việt")
    console.print("  [cyan]2[/cyan]  English")
    console.print("  [cyan]3[/cyan]  日本語")
    choices = {"1": "vi", "vi": "vi", "2": "en", "en": "en", "3": "ja", "ja": "ja"}
    while True:
        raw = typer.prompt("Choice [1/2/3]", default="1")
        lang = choices.get(raw.strip().lower())
        if lang:
            return lang
        console.print("[red]Please enter 1, 2, or 3.[/red]")


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
    lang: Optional[str] = typer.Option(
        None,
        "--lang",
        help="Language for AI responses and documents: vi | en | ja. "
        "Prompted interactively if omitted.",
    ),
) -> None:
    """Scaffold .claude/, .bvn-sdd/ and docs/ into a project."""
    if here and project_name:
        error("Pass either a project name or --here, not both.")
        raise typer.Exit(code=1)
    if not here and not project_name:
        error("Provide a project name, or use --here for the current directory.")
        raise typer.Exit(code=1)

    # Resolve language before any file I/O.
    if lang is not None:
        lang = lang.strip().lower()
        if lang not in _assets.SUPPORTED_LANGUAGES:
            error(f"Unsupported language {lang!r}. Choose: vi | en | ja")
            raise typer.Exit(code=1)
    else:
        lang = _prompt_language()

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

    _assets.set_language(target, lang)
    lang_label = _assets.SUPPORTED_LANGUAGES[lang]
    ok(f"language set to {lang_label} ({lang})")

    if not no_git:
        if _git_init(target):
            ok("initialized git repository")

    where = "current directory" if here else target.name
    panel(
        _NEXT_STEPS[lang],
        title=f"BVN-SDD ready in {where} [{lang_label}]",
    )
