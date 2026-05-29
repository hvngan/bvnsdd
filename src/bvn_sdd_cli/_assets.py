"""Locate and copy the bundled `core_pack` assets into a target project.

`core_pack/` ships inside the wheel (see pyproject `force-include`). For an
editable install or a source checkout it lives at the repository root. We
resolve whichever exists, then copy its three top-level trees into the target:

    core_pack/claude   -> <project>/.claude
    core_pack/bvn-sdd  -> <project>/.bvn-sdd
    core_pack/docs     -> <project>/docs

`claude` is stored unhidden in source (a leading dot confuses packaging) and
renamed to `.claude` on copy.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path

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
