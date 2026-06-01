---
description: BVN-SDD Phase 0-A — Safety Gate. Establish the minimum safe environment for AI to work in this project.
argument-hint: (no arguments)
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are performing **Safety Gate** (BVN-SDD Phase 0-A) for this project.
Run this **once per project**, immediately after `bvn-sdd init`, before `/sdd-map`.

Read `.claude/CLAUDE.md` and `.claude/rules/*` first.

Goal: document the safety environment that `bvn-sdd init` pre-configured, record
project-specific decisions, and produce an audit trail so every future session
can verify safety without re-checking from scratch.

**Plan first.** Output only: (1) goal of this phase, (2) directories/files you
will inspect, (3) files you will create, (4) Stop/Ask points. Do not create files
until the plan is acknowledged.

---

## Step 1 — Inspect existing configuration

Read and summarise what `bvn-sdd init` already installed:
- `.claude/CLAUDE.md` — note the 6 core principles and workflow
- `.claude/settings.json` — note every permission entry (deny/ask/allow)
- `.claude/rules/` — list each file and its scope
- `.bvn-sdd/config.yml` — note language, default_mode, tickets_dir

Then inspect the project itself (shallow scan — do NOT read every file):
- Root directory listing: identify tech stacks, package managers, CI config
- Check for `.env`, `*.key`, `*.pem`, `secrets/` — note their existence only,
  do NOT open or read them
- Check `.claude/settings.json` for any hooks or MCP server entries
- Check for external documents: `*.xlsx`, `*.docx`, `*.pdf` in root and `docs/`

**Detect project type** (record in `phase0-plan.md` under "Project Type"):
- Use Glob to check for source files outside BVN-SDD scaffolding:
  common patterns include `src/**`, `lib/**`, `app/**`, `*.py`, `*.ts`, `*.js`,
  `*.go`, `*.java`, `*.cs`, `*.rb` — exclude `.bvn-sdd/`, `.claude/`, `docs/`,
  `node_modules/`, `.git/`
- **existing** — source files found; this is an established codebase
- **new** — no source files found; this is a green-field project
- If `project_type = new`, add a note: "`/sdd-map` will run in green-field mode
  (architecture decisions, not source survey)"

---

## Step 2 — Identify project-specific risks

Based on your inspection, flag any of the following that apply to this project:

| Risk area | Check |
|---|---|
| Secrets / keys present in repo | .env, *.key, *.pem found? |
| External docs present | Office/PDF files that could be injected? |
| Hooks configured | Pre-commit, pre-push hooks that run code? |
| MCP servers configured | External integrations with write/delete permissions? |
| Large auto-generated dirs | node_modules, dist, .next, build — should stay out of context |
| Multi-repo / submodules | External code that AI should not treat as local source? |
| Production DB access possible | env vars pointing to prod? |

For each risk that applies, note the severity (Low / Medium / High) and the
mitigation already in place or needed.

---

## Step 3 — Create output files

Create all directories and files below. **Populate them with project-specific
content** based on your inspection — do not copy blank templates.

### `docs/maintenance/phase0/README.md`
One paragraph: what Phase 0-A is, what was done, when, and where the evidence
lives. Reference the five other phase0 files.

### `docs/maintenance/phase0/phase0-plan.md`
Copy template from `.bvn-sdd/templates/phase0/phase0-plan.md`, then fill in:
- Project name (from package.json, pyproject.toml, or root directory name)
- Date (write the date the user ran this command — ask if unknown)
- Tech stack identified
- Scope of this Phase 0-A run

### `docs/maintenance/phase0/phase0-decisions.md`
Copy template from `.bvn-sdd/templates/phase0/phase0-decisions.md`, then fill in:
- Each permission decision in `.claude/settings.json` with its rationale
- Language setting and why
- External content handling policy chosen
- Context loading order confirmed

### `docs/maintenance/phase0/phase0-execution-log.md`
Copy template from `.bvn-sdd/templates/phase0/phase0-execution-log.md`, then
record each inspection step you performed: what you checked, what you found.

### `docs/maintenance/phase0/phase0-risk-register.md`
Copy template from `.bvn-sdd/templates/phase0/phase0-risk-register.md`, then
enter one row per risk identified in Step 2 (even Low risks). Leave empty rows
if no risks found — do not omit the table.

### `docs/maintenance/phase0/phase0-review.md`
Copy template from `.bvn-sdd/templates/phase0/phase0-review.md`. Pre-tick every
item that was confirmed during this run. Leave unticked any item that requires
human verification. Do NOT mark the "Human sign-off" line as complete.

### `docs/standards/automation/context-loading-policy.md`
Copy template from `.bvn-sdd/templates/automation/context-loading-policy.md`,
then fill in: the reading order for this project, which directories AI may and
may not read, and the maximum context budget guidance if known.

### `docs/standards/automation/external-content-intake.md`
Copy template from `.bvn-sdd/templates/automation/external-content-intake.md`,
then fill in: list all external document types found in this project and the
handling policy for each (extract → review → promote to spec-pack only).

### `docs/standards/automation/repo-intake-checklist.md`
Copy template from `.bvn-sdd/templates/automation/repo-intake-checklist.md`.
This file is used before bringing in any external repository or submodule.
Pre-fill the project name and tech stack; leave checklist items unticked.

---

## Step 4 — Stop/Ask conditions

Immediately stop and ask a human if:
- Any `.env`, `*.key`, or credential file contains real secrets that are
  committed to the repository (not just `.env.example`)
- An MCP server is configured with `write`, `delete`, or `send` permissions
  and has not been reviewed by the team
- Production DB connection strings are present in any readable config file
- A hook runs external code that cannot be inspected

---

## Done

When all files are created, report:
1. A summary table: file created → status (created / skipped-already-exists)
2. List of risks found (severity and mitigation)
3. Items in `phase0-review.md` that still need human sign-off
4. Next step: tell the user to review `docs/maintenance/phase0/phase0-review.md`,
   sign off the remaining items, then run `/sdd-map` to continue.
