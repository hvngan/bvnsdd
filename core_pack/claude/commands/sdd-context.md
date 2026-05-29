---
description: BVN-SDD Phase 2 — pin down the ticket's context and rules.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are preparing the working context for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read first: `.claude/CLAUDE.md`, `.claude/rules/*`, this ticket's `spec-pack.md`
and `open-issues.md`, `docs/architecture/*`, `docs/standards/*`.

**Plan first** (goal, files to read, files to update, Stop/Ask points, plan).
Do not edit until acknowledged.

Goal: make sure the implementation phase does not use non-existent APIs or
forbidden patterns.

Update:
- `context.md` — concrete correct examples already in the codebase; allowed vs.
  forbidden patterns; methods/classes that actually exist vs. must not be used;
  DTO/Entity/Table mappings; master-data / code-value mappings; encoding and
  multi-language notes.
- `source-map.md` — the specific files this ticket will read and touch, with a
  one-line purpose each.

Verify claims against the real source (use Grep/Glob/Read). Mark anything
uncertain in `open-issues.md`. When done, tell the user to run `/sdd-plan
$ARGUMENTS` next.
