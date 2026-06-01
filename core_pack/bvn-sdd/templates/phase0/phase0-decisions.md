# Phase 0-A Decisions — <PROJECT>

> Record of every configuration decision made during Phase 0-A, with rationale.
> This is the audit trail for why the safety environment is set up the way it is.

## Permission decisions (`.claude/settings.json`)

### Hard Block (deny)

| Pattern / Command | Rationale |
|---|---|
| `.env`, `*.key`, `*.pem`, `secrets/` | |
| `rm -rf`, destructive shell commands | |
| `git push --force` | |
| MCP with unreviewed write/delete/send | |

### Ask before running

| Pattern / Command | Rationale |
|---|---|
| `git commit`, `git push` | |
| Docker, kubectl, cloud CLI | |
| Original Office/PDF documents | |

### Allow (read-only / safe operations)

| Pattern / Command | Rationale |
|---|---|
| `git status`, `git diff`, `git log` | |
| `rg`, `find`, `ls`, `cat`, `head` | |
| Lint / test runners | |

## Language setting

| Setting | Value | Rationale |
|---|---|---|
| `language` in config.yml | | |
| `.claude/rules/00-language.md` applied | | |

## External content handling

| Content type | Policy | Rationale |
|---|---|---|
| Word / Excel / PowerPoint | Extract → review → promote | |
| PDF | Extract → review → promote | |
| External web pages | Extract summary only | |
| External repositories | Use repo-intake-checklist | |

## Context loading order

_Confirmed reading priority for this project (see context-loading-policy.md)._

1. `.claude/CLAUDE.md` + `.claude/rules/*`
2. `docs/architecture/*` + `docs/standards/*`
3. `docs/changes/<TICKET>/*`
4. Source files in scope

## Single source of truth

| Artifact | Source of truth |
|---|---|
| Requirements / AC | `docs/changes/<TICKET>/spec-pack.md` |
| Architecture | `docs/architecture/system-map.md` |
| Safety rules | `.claude/rules/` |
| Permission policy | `.claude/settings.json` |
