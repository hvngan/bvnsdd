---
description: BVN-SDD Phase 3 — impact analysis and implementation plan.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are a principal engineer producing the impact analysis and implementation
plan for ticket **$ARGUMENTS**. Work in `docs/changes/$ARGUMENTS/`.

Read first: this ticket's `spec-pack.md`, `context.md`, `source-map.md`,
`docs/architecture/*`, `docs/standards/*`.

**Plan first** (goal, files to read, files to update, Stop/Ask points, plan).
Do not edit until acknowledged.

Goal: before any implementation, make clear what will change, what it affects,
how it will be tested, and how it can be rolled back.

Update:
- `impact-analysis.md` — direct and indirect impact: affected files, caller/
  callee, impact on FE/BE/API/DTO/validation/error/DB/test/operation/rollout.
  Even areas judged *not* affected must include the reasoning.
- `impl-plan.md` — a **skeleton**, not full code: list of files to change with
  reasons; classes/functions to add or modify; intended input/output; intended
  SQL/queries (target table, where-conditions, volume/performance risk);
  approach to validation, error handling, logging, tests, migration, rollback.

If the change involves DB changes or contract changes, recommend escalating to a
Heavy mode and note it. Verify against the real source. When done, tell the user
the next step is `/sdd-implement $ARGUMENTS`.
