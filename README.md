# BVN-SDD CLI

`bvn-sdd` installs the **BVN-SDD V04.2** methodology pack into any project.
`bvn-sdd init` copies a set of Claude Code slash commands, artifact templates, and
AI rules into your project folder. After that, Claude Code guides each development
phase and writes real files — spec, impact analysis, implementation plan, tests,
report — into `docs/changes/<TICKET>/`.

## Install

Requires **Python 3.11+**.

```bash
# From a local checkout
pip install -e .

# One-off without installing (requires uv)
uvx --from git+https://github.com/hvngan/bvnsdd.git bvn-sdd init my-project

# Install as a global tool
uv tool install git+https://github.com/hvngan/bvnsdd.git
# or
pipx install git+https://github.com/hvngan/bvnsdd.git
```

> Not yet published to PyPI. Install from the git repo or a local checkout.
> If `bvn-sdd` is not on PATH after install, run via `python -m bvn_sdd_cli`.

## Quickstart

### 1. Check prerequisites

```bash
bvn-sdd check
```

Verifies that `git` and `claude` (Claude Code CLI) are on PATH.

### 2. Scaffold a project

```bash
bvn-sdd init my-project    # creates ./my-project/ with full BVN-SDD structure
bvn-sdd init --here        # scaffold into the current directory instead
```

During init you will be asked to choose the language for all AI responses and documents:

```
Select language / 言語を選択 / Chọn ngôn ngữ:
  1  Tiếng Việt
  2  English
  3  日本語
Choice [1/2/3]:
```

Or skip the prompt with `--lang vi`, `--lang en`, or `--lang ja`.

The chosen language is written to `.claude/rules/00-language.md`. Claude reads
this file at the start of every session and produces all responses and artifact
content in that language.

### 3. Open the project in Claude Code

All `/sdd-*` slash commands become available immediately.

### 4. Map the codebase — once per project

```
/sdd-map
```

Reads the source tree and writes architecture maps to `docs/architecture/`
(system map, entry points, routes, APIs, DB schema, external interfaces).
Run this before the first ticket; re-run only after large structural changes.

### 5. Work a ticket

```
/sdd-new T-001          → creates docs/changes/T-001/ with all blank artifact files
/sdd-spec T-001         → fills spec-pack.md (AC, scope, FE/BE/DB impact, assumptions)
/sdd-rightsize T-001    → scores the ticket and writes mode-decision.md (M1–M5/MX)
```

After `/sdd-rightsize`, the command prints the exact list of remaining commands
to run for the chosen mode. You do not need to decide what to skip yourself.

For an **M2 Standard** ticket the full sequence is:

```
/sdd-context T-001      → context.md, source-map.md
/sdd-plan T-001         → impact-analysis.md, impl-plan.md
/sdd-implement T-001    → source code + self-review.md
/sdd-test T-001         → test-plan.md, test-results.md
/sdd-blackbox T-001     → blackbox-testcases.md
/sdd-report T-001       → report.md
```

Use `/sdd-compact T-001` at any point to snapshot the session state into
`strategic-compact.md`. Paste that file's content at the start of a new Claude
session to resume without re-reading all artifacts from scratch.

## Operating modes

`/sdd-rightsize` scores four criteria — Reversibility, Uncertainty, Risk, Scope —
and maps the total to a mode. The mode determines which subsequent commands are
required, which are optional, and which to skip entirely.

| Mode | Name | Typical trigger | Commands skipped vs M2 |
|---|---|---|---|
| M1 | Light | Bug fix, text change, config update | `/sdd-context`, `/sdd-plan`, `/sdd-blackbox` |
| M2 | Standard | Normal single-service feature | — (full flow) |
| M3 | Plus | FE+BE contract change, 10–30 files | — (extra attention on spec section 9) |
| M4 | Heavy | Architecture change, DB migration, large refactor | — (+ security review before merge, re-run `/sdd-map`) |
| M5 | Critical | Security patch, production incident | Escalate to human lead; minimal automation |
| MX | Stop | Requirements unclear or risk too high | Halt all commands until open issues are resolved |

## Commands

### CLI

| Command | What it does |
|---|---|
| `bvn-sdd init [NAME]` | Scaffold `.claude/`, `.bvn-sdd/`, `docs/` into a project. Options: `--here`, `--force`, `--no-git`, `--lang vi\|en\|ja` (prompted interactively if omitted). |
| `bvn-sdd check` | Verify `git` and `claude` are on PATH. |
| `bvn-sdd version` | Print the CLI version. |

### Claude Code slash commands

All phase commands take a ticket ID (e.g. `T-001`) as their argument.

| Command | Phase | Artifact written |
|---|---|---|
| `/sdd-map` | 0-B Source Intelligence | `docs/architecture/system-map.md`, `route-api-map.md`, `service-layer-map.md`, `repository-db-map.md`, `external-interface-map.md` |
| `/sdd-new <T>` | 0 Bootstrap | `docs/changes/<T>/` — all blank artifact files copied from templates |
| `/sdd-spec <T>` | 1 Investigation | `spec-pack.md`, `source-availability.md`, `open-issues.md` |
| `/sdd-rightsize <T>` | 1-B Mode Decision | `mode-decision.md` — chosen mode, score, adapted workflow |
| `/sdd-context <T>` | 2 Context | `context.md`, `source-map.md` |
| `/sdd-plan <T>` | 3 Impact & Plan | `impact-analysis.md`, `impl-plan.md` |
| `/sdd-implement <T>` | 5 Implement | source code changes + `self-review.md` |
| `/sdd-test <T>` | 6 Test | `test-plan.md`, `test-results.md` |
| `/sdd-blackbox <T>` | 7 Black-box Test | `blackbox-testcases.md` — test cases derived from spec only, not from code (M2+ only) |
| `/sdd-report <T>` | 8 Report | `report.md` — summary, AC traceability, accepted risks, follow-up items |
| `/sdd-compact <T>` | utility (any time) | `strategic-compact.md` — session snapshot: current phase, decisions made, files read, next steps |

## What `init` creates

```
my-project/
├── .claude/
│   ├── CLAUDE.md                  # AI constitution — read at the start of every session
│   ├── settings.json              # tool permission deny / ask / allow lists
│   ├── rules/
│   │   ├── 00-language.md         # generated at init — instructs Claude to use chosen language
│   │   ├── 00-safety.md           # stop conditions, destructive-operation guardrails
│   │   ├── 10-development.md      # plan-first rule, coding standards
│   │   ├── 20-architecture.md     # 10-level source priority, context include/exclude rules
│   │   ├── 30-security.md         # secrets, PII, external input policy
│   │   ├── 40-testing.md          # AC-tracing, test evidence requirements
│   │   └── 50-review.md           # severity model (Blocker/Major/Minor), review viewpoints
│   └── commands/                  # one .md file per /sdd-* slash command
├── .bvn-sdd/
│   ├── config.yml                 # language, default mode, ticket artifact list
│   ├── templates/                 # blank artifact files copied per ticket by /sdd-new
│   ├── i18n/                      # QUICKSTART-vi.md, QUICKSTART-en.md, QUICKSTART-ja.md
│   └── scripts/                   # create-ticket helper scripts (PowerShell + bash)
└── docs/
    ├── QUICKSTART.md              # one-page field guide in the language chosen at init
    ├── architecture/              # filled by /sdd-map; one file per map type
    ├── standards/                 # coding.md, review.md, testing.md, security.md (stubs)
    ├── maintenance/               # failure-mode-index.md, pattern-library.md
    └── changes/                   # docs/changes/T-001/, T-002/, … — one folder per ticket
```

## Development

```bash
pip install -e ".[dev]"
pytest
```
