"""Locate and copy the bundled `core_pack` assets into a target project.

`core_pack/` ships inside the wheel (see pyproject `force-include`). For an
editable install or a source checkout it lives at the repository root. We
resolve whichever exists, then copy its three top-level trees into the target:

    core_pack/claude   -> <project>/.claude
    core_pack/bvn-sdd  -> <project>/.bvn-sdd
    core_pack/docs     -> <project>/docs

`claude` is stored unhidden in source (a leading dot confuses packaging) and
renamed to `.claude` on copy.

Template layout under `core_pack/bvn-sdd/templates/`:
  ├── *.md                    ticket-level artifacts (copied by /sdd-new)
  │   includes: spec-pack, source-availability, open-issues, mode-decision,
  │             context, source-map, ticket-rules,
  │             impact-analysis, impl-plan,
  │             review-checklist, self-review, human-review,
  │             test-plan, test-results,
  │             blackbox-testcases, blackbox-review-checklist, test-data,
  │             strategic-compact, report, promotion-candidates
  ├── phase0/                 project-level Phase 0-A artifacts (used by /sdd-phase0a)
  │   ├── phase0-plan.md
  │   ├── phase0-decisions.md
  │   ├── phase0-execution-log.md
  │   ├── phase0-risk-register.md
  │   └── phase0-review.md
  └── automation/             context and external-content policies (used by /sdd-phase0a)
      ├── context-loading-policy.md
      ├── external-content-intake.md
      └── repo-intake-checklist.md

All subtrees are copied recursively by `scaffold()`. The phase0/ and automation/
subdirectories are project-level (one per project, created by /sdd-phase0a) and
must NOT be copied into per-ticket folders by /sdd-new.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path

# Language directive injected into .claude/rules/00-language.md
_LANGUAGE_RULES: dict[str, str] = {
    "en": """\
# Language Policy

**Active language: English**

All AI responses, artifact content, plan outputs, document fills, generated code
comments, and any text you produce in this project must be written in **English**.
This rule applies to every phase command, open-issues entry, and spec section.
Do not mix languages; if the user writes in another language, still respond in English.
""",
    "vi": """\
# Chính sách Ngôn ngữ

**Ngôn ngữ đang dùng: Tiếng Việt**

Mọi phản hồi AI, nội dung artifact, kết quả plan, điền vào tài liệu, bình luận code
sinh ra, và bất kỳ văn bản nào bạn tạo trong dự án này đều phải viết bằng **Tiếng Việt**.
Quy tắc này áp dụng cho mọi lệnh phase, mục open-issues, và phần spec.
Không trộn ngôn ngữ; nếu người dùng viết bằng ngôn ngữ khác, vẫn phản hồi bằng Tiếng Việt.
""",
    "ja": """\
# 言語ポリシー

**使用言語: 日本語**

このプロジェクトで作成するすべてのAI応答、アーティファクトの内容、プランの出力、
ドキュメントの記入、生成されたコードのコメント、およびすべてのテキストは
**日本語**で記述してください。このルールはすべてのフェーズコマンド、
open-issuesのエントリ、およびspecのセクションに適用されます。
言語を混在させないでください。ユーザーが別の言語で書いた場合でも、日本語で応答してください。
""",
}

SUPPORTED_LANGUAGES: dict[str, str] = {
    "vi": "Tiếng Việt",
    "en": "English",
    "ja": "日本語",
}

# Maps a directory inside core_pack to its destination name in the project.
PACK_DIRS = {
    "claude": ".claude",
    "bvn-sdd": ".bvn-sdd",
    "docs": "docs",
}


def find_core_pack() -> Path:
    """Return the path to the bundled `core_pack` directory.

    Checks the packaged location first (installed wheel), then the repo root
    (editable install / source checkout). Raises if neither is found.
    """
    candidates = [
        Path(__file__).parent / "core_pack",  # packaged (wheel) location
        Path(__file__).parent.parent.parent / "core_pack",  # repo root (src layout)
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(
        "Could not locate the bundled core_pack assets. "
        "Reinstall bvn-sdd-cli or run from the project source root."
    )


@dataclass
class CopyResult:
    """Outcome of scaffolding: which files were written vs. skipped."""

    created: list[Path] = field(default_factory=list)
    skipped: list[Path] = field(default_factory=list)


def _copy_tree(src: Path, dst: Path, *, force: bool, result: CopyResult) -> None:
    """Recursively copy `src` into `dst`, never clobbering unless `force`.

    Records each file relative to `dst.parent` (the project root) so callers
    can report clean project-relative paths.
    """
    project_root = dst.parent
    for item in sorted(src.rglob("*")):
        relative = item.relative_to(src)
        target = dst / relative
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        rel_to_project = target.relative_to(project_root)
        if target.exists() and not force:
            result.skipped.append(rel_to_project)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
        result.created.append(rel_to_project)


def scaffold(target: Path, *, force: bool = False) -> CopyResult:
    """Copy every core_pack tree into `target`, returning what changed."""
    core_pack = find_core_pack()
    result = CopyResult()
    for pack_name, dest_name in PACK_DIRS.items():
        src = core_pack / pack_name
        if not src.is_dir():
            continue
        _copy_tree(src, target / dest_name, force=force, result=result)
    return result


def set_language(target: Path, lang: str) -> None:
    """Write the language directive rule and copy the localized QUICKSTART.

    Called after scaffold(). Writes:
      <target>/.claude/rules/00-language.md  — Claude language directive
      <target>/docs/QUICKSTART.md            — localized quick-start guide
      <target>/.bvn-sdd/config.yml           — patches language: <lang>
    """
    if lang not in _LANGUAGE_RULES:
        raise ValueError(f"Unsupported language: {lang!r}. Choose from {list(_LANGUAGE_RULES)}")

    # 1. Write the Claude language rule.
    rules_dir = target / ".claude" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    (rules_dir / "00-language.md").write_text(_LANGUAGE_RULES[lang], encoding="utf-8")

    # 2. Copy the localized QUICKSTART.
    core_pack = find_core_pack()
    qs_src = core_pack / "bvn-sdd" / "i18n" / f"QUICKSTART-{lang}.md"
    qs_dst = target / "docs" / "QUICKSTART.md"
    if qs_src.exists():
        qs_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(qs_src, qs_dst)

    # 3. Patch language into config.yml.
    config_path = target / ".bvn-sdd" / "config.yml"
    if config_path.exists():
        content = config_path.read_text(encoding="utf-8")
        if "language:" in content:
            import re
            content = re.sub(r"^language:.*$", f"language: {lang}", content, flags=re.MULTILINE)
        else:
            content = f"language: {lang}\n" + content
        config_path.write_text(content, encoding="utf-8")
