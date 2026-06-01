# BVN-SDD CLI

Turn the **BVN-SDD V04.2** methodology into something you *run*, not something
you *read*. Like [spec-kit](https://github.com/github/spec-kit) does for
spec-driven development: one command scaffolds your project, then Claude Code
slash commands walk you through each phase and produce real artifacts.

## Why

BVN-SDD ships as ~28 long Markdown files. Nobody reads all of them, so the method
doesn't get applied. This CLI bundles the essentials and makes them executable:
`bvn-sdd init` drops a ready-to-use `.claude/` + `docs/` structure into your
project, and the `/sdd-*` commands guide the rest.

## Install

Requires **Python 3.11+**. Pick one:

```bash
# from a local checkout (works today)
pip install -e .

# one-off from the git repo, no install (needs uv)
uvx --from git+https://github.com/hvngan/bvnsdd.git bvn-sdd init my-project

# install as a tool from the git repo
uv tool install git+https://github.com/hvngan/bvnsdd.git
# or:
pipx install git+https://github.com/hvngan/bvnsdd.git
```

> Not yet published to a package index, so install from the git repo or a local
> checkout. If the `bvn-sdd` command isn't on your PATH after install, run it via
> `python -m bvn_sdd_cli` instead.

## Quickstart

```bash
bvn-sdd check                 # confirm git + Claude Code are available
bvn-sdd init my-project       # scaffold a new project (or: bvn-sdd init --here)
cd my-project
```

Then open the project in **Claude Code** and run, in order:

1. `/sdd-map` — map the codebase (once per project)
2. `/sdd-new T-001` — create a ticket workspace
3. `/sdd-spec T-001` → `/sdd-context T-001` → `/sdd-plan T-001`
4. `/sdd-implement T-001` → `/sdd-test T-001` → `/sdd-report T-001`

Each command fills a concrete artifact under `docs/changes/T-001/`.

> **For employees:** a one-page field guide in Vietnamese ships with every
> scaffolded project at [`docs/QUICKSTART.md`](core_pack/docs/QUICKSTART.md).

## Commands

### CLI

| Command | Description |
|---|---|
| `bvn-sdd init [NAME]` | Scaffold `.claude/`, `.bvn-sdd/`, `docs/` into a project. Flags: `--here`, `--force`, `--no-git`, `--lang vi\|en\|ja` (prompted interactively if omitted). |
| `bvn-sdd check` | Verify `git` and `claude` are on PATH. |
| `bvn-sdd version` | Show the CLI version. |

### Claude Code slash commands (added by `init`)

| Command | Phase | Produces |
|---|---|---|
| `/sdd-map` | 0-B Source Intelligence | `docs/architecture/*` |
| `/sdd-new <T>` | bootstrap | ticket folder + blank artifacts |
| `/sdd-spec <T>` | 1 Investigation | `spec-pack.md`, `source-availability.md`, `open-issues.md` |
| `/sdd-rightsize <T>` | 1-B Mode Decision | `mode-decision.md` — adapted workflow (M1–M5/MX) |
| `/sdd-context <T>` | 2 Context/Rules | `context.md`, `source-map.md` |
| `/sdd-plan <T>` | 3 Impact/Plan | `impact-analysis.md`, `impl-plan.md` |
| `/sdd-implement <T>` | 5 Implement | code + `self-review.md` |
| `/sdd-test <T>` | 6 Test | `test-plan.md`, `test-results.md` |
| `/sdd-blackbox <T>` | 7 Black-box Test | `blackbox-testcases.md` (skipped for M1) |
| `/sdd-report <T>` | 8 Report | `report.md` |
| `/sdd-compact <T>` | any — utility | `strategic-compact.md` — session snapshot for handoff/resume |

## What `init` creates

```
my-project/
├── .claude/
│   ├── CLAUDE.md            # short AI constitution
│   ├── settings.json        # permission deny/ask/allow
│   ├── rules/               # safety, dev, architecture, security, testing, review
│   └── commands/            # the /sdd-* slash commands
├── .bvn-sdd/
│   ├── config.yml           # version, default mode (M2), ticket conventions
│   ├── templates/           # one template per artifact
│   └── scripts/             # create-ticket (PowerShell + bash)
└── docs/
    ├── QUICKSTART.md        # one-page employee field guide (Vietnamese)
    ├── architecture/        # system-map.md (filled by /sdd-map)
    ├── standards/           # coding, review, testing, security (stubs)
    ├── maintenance/         # failure-mode-index.md, pattern-library.md
    └── changes/             # per-ticket artifacts live here
```

## Scope (v1)

Covers the **Core workflow at Mode M2 (Standard)**: Phase 0 → 8 for Claude Code.
Not yet included (planned): automatic M0–M5 right-sizing, Codex independent
review, black-box test generation, FE/BE-contract & microservice packs, and
multi-agent support. The structure leaves room to add these later.

## Development

```bash
pip install -e ".[dev]"
pytest
```
