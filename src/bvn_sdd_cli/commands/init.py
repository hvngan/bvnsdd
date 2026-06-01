"""`bvn-sdd init` — scaffold the BVN-SDD structure into a project."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Optional

import typer

from .. import _assets
from .._console import console, error, info, ok, panel, rule, skip, warn
from .._version import __version__

# ---------------------------------------------------------------------------
# Next-steps panel content per language
# ---------------------------------------------------------------------------

_NEXT_STEPS: dict[str, str] = {
    "vi": """\
[bold cyan]Bước 1[/bold cyan]  Mở thư mục dự án trong [bold]Claude Code[/bold].

[bold cyan]Bước 2[/bold cyan]  Chạy 1 lần để AI hiểu codebase:
          [cyan]/sdd-map[/cyan]

[bold cyan]Bước 3[/bold cyan]  Tạo ticket đầu tiên:
          [cyan]/sdd-new T-001[/cyan]

[bold cyan]Bước 4[/bold cyan]  Chạy từng phase theo thứ tự:
          [cyan]/sdd-spec T-001[/cyan]       →  spec-pack.md
          [cyan]/sdd-rightsize T-001[/cyan]  →  mode-decision.md  (M1–M5)
          [cyan]/sdd-context T-001[/cyan]    →  context.md  [dim](bỏ qua nếu M1)[/dim]
          [cyan]/sdd-plan T-001[/cyan]       →  impl-plan.md  [dim](bỏ qua nếu M1)[/dim]
          [cyan]/sdd-implement T-001[/cyan]  →  code + self-review.md
          [cyan]/sdd-test T-001[/cyan]       →  test-plan.md, test-results.md
          [cyan]/sdd-blackbox T-001[/cyan]   →  blackbox-testcases.md  [dim](bỏ qua nếu M1)[/dim]
          [cyan]/sdd-report T-001[/cyan]     →  report.md

[dim]Mẹo: dùng /sdd-compact T-001 bất cứ lúc nào để lưu trạng thái session[/dim]\
""",
    "en": """\
[bold cyan]Step 1[/bold cyan]  Open the project folder in [bold]Claude Code[/bold].

[bold cyan]Step 2[/bold cyan]  Run once to map the codebase:
          [cyan]/sdd-map[/cyan]

[bold cyan]Step 3[/bold cyan]  Create your first ticket:
          [cyan]/sdd-new T-001[/cyan]

[bold cyan]Step 4[/bold cyan]  Drive each phase in order:
          [cyan]/sdd-spec T-001[/cyan]       →  spec-pack.md
          [cyan]/sdd-rightsize T-001[/cyan]  →  mode-decision.md  (M1–M5)
          [cyan]/sdd-context T-001[/cyan]    →  context.md  [dim](skip for M1)[/dim]
          [cyan]/sdd-plan T-001[/cyan]       →  impl-plan.md  [dim](skip for M1)[/dim]
          [cyan]/sdd-implement T-001[/cyan]  →  code + self-review.md
          [cyan]/sdd-test T-001[/cyan]       →  test-plan.md, test-results.md
          [cyan]/sdd-blackbox T-001[/cyan]   →  blackbox-testcases.md  [dim](skip for M1)[/dim]
          [cyan]/sdd-report T-001[/cyan]     →  report.md

[dim]Tip: run /sdd-compact T-001 at any point to snapshot the session state[/dim]\
""",
    "ja": """\
[bold cyan]ステップ 1[/bold cyan]  プロジェクトフォルダを [bold]Claude Code[/bold] で開きます。

[bold cyan]ステップ 2[/bold cyan]  コードベースをマップするため1回実行:
              [cyan]/sdd-map[/cyan]

[bold cyan]ステップ 3[/bold cyan]  最初のチケットを作成:
              [cyan]/sdd-new T-001[/cyan]

[bold cyan]ステップ 4[/bold cyan]  各フェーズを順番に実行:
              [cyan]/sdd-spec T-001[/cyan]       →  spec-pack.md
              [cyan]/sdd-rightsize T-001[/cyan]  →  mode-decision.md  (M1–M5)
              [cyan]/sdd-context T-001[/cyan]    →  context.md  [dim](M1はスキップ)[/dim]
              [cyan]/sdd-plan T-001[/cyan]       →  impl-plan.md  [dim](M1はスキップ)[/dim]
              [cyan]/sdd-implement T-001[/cyan]  →  コード + self-review.md
              [cyan]/sdd-test T-001[/cyan]       →  test-plan.md, test-results.md
              [cyan]/sdd-blackbox T-001[/cyan]   →  blackbox-testcases.md  [dim](M1はスキップ)[/dim]
              [cyan]/sdd-report T-001[/cyan]     →  report.md

[dim]ヒント: /sdd-compact T-001 でいつでもセッション状態をスナップショット保存できます[/dim]\
""",
}

_PANEL_TITLES: dict[str, str] = {
    "vi": "BVN-SDD — Dự án đã sẵn sàng",
    "en": "BVN-SDD — Project ready",
    "ja": "BVN-SDD — プロジェクト準備完了",
}

_LANG_PROMPT_LABELS: dict[str, str] = {
    "vi": "Ngôn ngữ / Language / 言語",
    "en": "Language / Ngôn ngữ / 言語",
    "ja": "言語 / Language / Ngôn ngữ",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _prompt_language() -> str:
    """Interactive language selector printed in a styled panel. Returns 'vi', 'en', or 'ja'."""
    console.print()
    console.print(
        "[bold]Select language[/bold]  [dim]/ 言語を選択 / Chọn ngôn ngữ[/dim]"
    )
    console.print()
    console.print("    [cyan bold]1[/cyan bold]   Tiếng Việt  [dim](mặc định)[/dim]")
    console.print("    [cyan bold]2[/cyan bold]   English")
    console.print("    [cyan bold]3[/cyan bold]   日本語")
    console.print()

    choices = {"1": "vi", "vi": "vi", "2": "en", "en": "en", "3": "ja", "ja": "ja"}
    while True:
        raw = typer.prompt("  Choice [1/2/3]", default="1")
        lang = choices.get(raw.strip().lower())
        if lang:
            console.print()
            return lang
        error("Please enter 1, 2, or 3.")


def _git_init(target: Path) -> bool:
    """Run `git init` in `target` if it is not already a repo. Returns True if initialized."""
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


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------


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

    from .._console import FULL_NAME, BANNER
    from rich.text import Text

    # Header
    console.print()
    console.print(Text(BANNER, style="bold cyan"))
    console.print(Text(f"  {FULL_NAME}", style="dim"))
    console.print(Text(f"  v{__version__}", style="bold"))
    console.print()

    # Validate arguments
    if here and project_name:
        error("Pass either a project name or --here, not both.")
        raise typer.Exit(code=1)
    if not here and not project_name:
        error("Provide a project name, or use --here for the current directory.")
        raise typer.Exit(code=1)

    # Resolve language
    if lang is not None:
        lang = lang.strip().lower()
        if lang not in _assets.SUPPORTED_LANGUAGES:
            error(
                f"Unsupported language [bold]{lang!r}[/bold]. "
                "Choose: [cyan]vi[/cyan] | [cyan]en[/cyan] | [cyan]ja[/cyan]"
            )
            raise typer.Exit(code=1)
    else:
        lang = _prompt_language()

    lang_label = _assets.SUPPORTED_LANGUAGES[lang]

    # Resolve target directory
    if here:
        target = Path.cwd()
        where = target.name
    else:
        target = Path.cwd() / project_name  # type: ignore[arg-type]
        target.mkdir(parents=True, exist_ok=True)
        where = project_name

    # Guard against re-scaffolding
    if (target / ".bvn-sdd").exists() and not force:
        error(
            f"[bold]{target / '.bvn-sdd'}[/bold] already exists. "
            "Use [cyan]--force[/cyan] to overwrite."
        )
        raise typer.Exit(code=1)

    # Scaffold files
    rule(f"Scaffolding → {where}  [{lang_label}]")
    console.print()

    try:
        result = _assets.scaffold(target, force=force)
    except FileNotFoundError as exc:
        error(str(exc))
        raise typer.Exit(code=1) from exc

    created_count = len(result.created)
    skipped_count = len(result.skipped)

    for path in result.created:
        ok(path.as_posix())
    for path in result.skipped:
        skip(f"already exists — skipped  {path.as_posix()}")

    console.print()
    info(
        f"[green]{created_count}[/green] file(s) created"
        + (f",  [yellow]{skipped_count}[/yellow] skipped" if skipped_count else "")
    )

    # Apply language
    _assets.set_language(target, lang)
    ok(f"Language set to [bold]{lang_label}[/bold]  →  .claude/rules/00-language.md")

    # Git
    if not no_git:
        if _git_init(target):
            ok("Git repository initialized")
        else:
            info("Git repository already exists — skipped")

    # Summary + next steps
    console.print()
    rule()
    console.print()
    panel(
        _NEXT_STEPS[lang],
        title=f"{_PANEL_TITLES[lang]}  ·  {where}  ·  {lang_label}",
    )
    console.print()
