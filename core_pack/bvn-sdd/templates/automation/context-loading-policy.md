# Context Loading Policy — <PROJECT>

> Defines the order and rules for loading context into an AI session.
> Filled by `/sdd-phase0a`. Prevents context pollution and token waste.

## Reading priority order

1. `.claude/CLAUDE.md` — core principles and workflow (always read first)
2. `.claude/rules/*` — safety, security, development, review rules
3. `docs/architecture/*` — system map, source inventory (read once per project)
4. `docs/standards/*` — coding, testing, security, review standards
5. `docs/changes/<TICKET>/*` — current ticket artifacts
6. Source files and tests within the change's scope (read on demand)

## Directories AI may read

| Directory | Condition |
|---|---|
| `.claude/` | Always |
| `docs/` | Always |
| `src/` or equivalent source root | Within ticket scope |
| `tests/` or equivalent test root | Within ticket scope |
| Config files at root (`*.json`, `*.yml`, `*.toml`) | Always (no secrets) |

## Directories AI must NOT read

| Directory | Reason |
|---|---|
| `.env`, `*.key`, `*.pem` | Secrets |
| `node_modules/`, `vendor/` | Auto-generated; not source of truth |
| `dist/`, `build/`, `.next/`, `out/` | Generated output |
| `*.log`, `logs/` | Runtime data; may contain PII |
| `secrets/`, `credentials/` | Credentials |

## External content rules

- Office / PDF files: extract key points to `reference-extracts.md` first.
  Do not use original files as source of truth. See `external-content-intake.md`.
- Web pages: summarise into `reference-extracts.md`; link to original URL.
- External repos: follow `repo-intake-checklist.md` before reading.

## Context budget guidance

| Session type | Suggested context limit |
|---|---|
| Single-file fix (M1) | Load only the target file and its direct imports |
| Standard feature (M2) | Load spec-pack + architecture map + files in scope |
| Cross-service change (M3+) | Load spec-pack + full architecture + all impacted files |

## Project-specific notes

_Any project-specific context loading decisions made during Phase 0-A._
