# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

`bvn-sdd-cli` is a Python CLI tool that scaffolds the **BVN-SDD V04.2 methodology** into software projects. Running `bvn-sdd init` copies `core_pack/` into a target project as three hidden directories (`.claude/`, `.bvn-sdd/`, `docs/`), giving that project AI governance rules, 14 Claude Code slash commands, and 20+ markdown artifact templates for a spec-driven development workflow.

The `core_pack/` directory is **the product** — the CLI exists only to deliver it correctly.

## Commands

```bash
# Development install
pip install -e ".[dev]"

# Run all tests
pytest

# Run a single test
pytest tests/test_init.py::test_scaffold_creates_expected_tree

# Run the CLI locally
bvn-sdd check
bvn-sdd init my-project
bvn-sdd init --here --lang en
bvn-sdd init my-project --no-git --lang en   # skip git init
bvn-sdd init my-project --force --lang en    # overwrite existing files

# Build the wheel (bundles core_pack inside)
python -m hatchling build
```

## Architecture

### CLI Layer (`src/bvn_sdd_cli/`)

| File | Role |
|---|---|
| `__init__.py` | Typer app; registers `init`, `check`, `version` commands |
| `_assets.py` | Locates `core_pack/`, scaffolds trees, writes language config |
| `_console.py` | Rich UI helpers (`ok`, `warn`, `error`, `panel`, `rule`, banner) |
| `commands/init.py` | `bvn-sdd init`: validates args, prompts language, calls `_assets`, runs `git init` |
| `commands/check.py` | `bvn-sdd check`: verifies `git` and `claude` are on PATH |

### Core Pack (`core_pack/`) — Bundled Assets

Three directories that become the scaffolded output:

- **`claude/`** → `.claude/` in target project
  - `CLAUDE.md` — AI constitution (6 core principles)
  - `settings.json` — Claude Code permissions (deny secrets, ask before destructive ops)
  - `commands/` — 14 slash command templates driving the 9-phase workflow
  - `rules/` — 7 AI behavior rule files (safety, stop-conditions, development, architecture, security, testing, review)

- **`bvn-sdd/`** → `.bvn-sdd/` in target project
  - `config.yml` — language, default mode (M2), tickets_dir, artifact list
  - `templates/` — 20 blank artifact `.md` files per ticket + `phase0/` + `automation/`
  - `i18n/` — `QUICKSTART-<lang>.md` (vi/en/ja) + `EXAMPLE-*.md` green-field walkthroughs
  - `scripts/powershell/create-ticket.ps1` and `scripts/bash/create-ticket.sh`

- **`docs/`** → `docs/` in target project
  - `architecture/` — stubs for `/sdd-map` to populate (system, routes, APIs, DB, contracts)
  - `standards/` — coding, testing, review, security, cross-platform convention stubs
  - `maintenance/` — `failure-mode-index.md`, `pattern-library.md` (living docs)
  - `changes/` — per-ticket folders created by `/sdd-new T-001`

### Language Support

At `bvn-sdd init`, the user picks vi/en/ja. `_assets.set_language()` then:
1. Writes `.claude/rules/00-language.md` with the language directive
2. Patches `.bvn-sdd/config.yml` `language:` field
3. Copies `i18n/QUICKSTART-<lang>.md` to `docs/QUICKSTART.md`

### Packaging

`pyproject.toml` uses `hatchling` with a `force-include` directive that bundles `core_pack/` inside the wheel at `bvn_sdd_cli/core_pack/`. `_assets.py` locates the pack by first checking the installed package path, then falling back to the repo root for editable installs.

## BVN-SDD Workflow Phases (for context when editing commands/)

The 14 slash commands implement a sequential 9-phase workflow per ticket:

| Command | Phase | Output Artifacts |
|---|---|---|
| `/sdd-phase0a` | 0-A Safety Gate | `phase0/` audit trail, `automation/` policies |
| `/sdd-map` | 0-B Source Intelligence | `docs/architecture/*` maps |
| `/sdd-new T-001` | Bootstrap | `docs/changes/T-001/` with blank artifacts |
| `/sdd-spec T-001` | 1 Spec Pack | `spec-pack.md`, `source-availability.md`, `open-issues.md` |
| `/sdd-rightsize T-001` | 1 Mode Decision | `mode-decision.md` (M1–M5 or MX stop) |
| `/sdd-context T-001` | 2 Context | `context.md`, `source-map.md`, `ticket-rules.md` |
| `/sdd-plan T-001` | 3 Impact & Plan | `impact-analysis.md`, `impl-plan.md` |
| `/sdd-implement T-001` | 4–5 Implement & Self-Review | source code + `self-review.md`, `human-review.md` |
| `/sdd-test T-001` | 6 Test | `test-plan.md`, `test-results.md` |
| `/sdd-blackbox T-001` | 7 Black-box Test | `blackbox-testcases.md`, `blackbox-review-checklist.md`, `test-data.md` |
| `/sdd-report T-001` | 8 Final Report | `report.md` |
| `/sdd-learnings T-001` | 9 Learnings | `promotion-candidates.md`; updates `failure-mode-index.md`, `pattern-library.md` |
| `/sdd-compact T-001` | Utility | `strategic-compact.md` (session snapshot) |
| `/sdd-translate T-001` | Utility | `vi-review.md` (Vietnamese review of key JA artifacts — internal only) |

The mode sets the **depth** of each phase — it does not skip phases. Every ticket
(single- or multi-platform) runs the full sequence above; M1 (Light) just keeps each
artifact brief, while M4/M5 add depth and extra review. Only Mode MX stops work
entirely.

## Important Constraints

- **`core_pack/` is the deliverable.** Changes to templates, commands, or rules directly affect every project scaffolded from this CLI. Edit carefully.
- **The `core_pack/claude/CLAUDE.md`** is the AI constitution deployed to user projects — it is *not* the CLAUDE.md for developing this CLI (that is this file).
- **Wheel bundling:** If you add new files under `core_pack/`, verify they are included in the `hatchling` `force-include` config in `pyproject.toml`.
- **Language directive files** (`00-language.md`) are generated at runtime and must never be committed to `core_pack/`.
- **`phase0/` and `automation/` are project-level** (one copy per project, created by `/sdd-phase0a`). They live under `templates/` only as source; `/sdd-new` must NOT copy them into per-ticket folders — only the root-level `*.md` templates belong there.
