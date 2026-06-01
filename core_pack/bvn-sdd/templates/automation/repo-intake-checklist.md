# Repository Intake Checklist — <PROJECT>

> Complete this checklist before reading or integrating any external repository,
> submodule, or third-party codebase. Prevents unvetted code from being treated
> as trusted source.

## Intake metadata

| Field | Value |
|---|---|
| External repo name / URL | |
| Reason for intake | |
| Date | |
| Reviewer | |

## Pre-read checks

- [ ] Repository source is known and trusted (not an anonymous or unknown author)
- [ ] Repository does not contain secrets or credentials
- [ ] Repository license is compatible with this project
- [ ] Repository is the correct version / branch / tag (not a fork or outdated copy)
- [ ] Repository does not contain executable scripts that run on import

## Context safety checks

- [ ] Auto-generated directories (`node_modules/`, `vendor/`, `dist/`) will be
  excluded from AI context
- [ ] Log files, `.env`, and credential files will be excluded
- [ ] Large binary files will not be read by AI
- [ ] External repo will be treated as **reference only** — not source of truth

## Integration scope

- [ ] Only the specific files needed for this ticket will be read
- [ ] AI will not modify files in the external repo
- [ ] Any conflicts between external repo patterns and this project's patterns
  will be raised as open issues, not resolved silently

## Sign-off

- [ ] All checks above are complete. This repo is safe to reference.

Reviewer: __________________ Date: __________________
