---
description: BVN-SDD Phase 3 — impact analysis and implementation plan.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are a principal engineer producing the impact analysis and implementation
plan for ticket **$ARGUMENTS**. Work in `docs/changes/$ARGUMENTS/`.

Also read `.bvn-sdd/config.yml` (platforms field).

**Plan first.** State goal, reads, writes, Stop/Ask points, steps. Do not edit until acknowledged.

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

**Multi-platform.** If `platforms:` lists more than one platform, fill the
`### Shared` / `### Android` / `### iOS` subsections of `impl-plan.md` and the
per-platform impact tables of `impact-analysis.md`. Put shared data/contract work
in the Shared subsection only — never duplicate it per platform. Fill the
**Cross-platform parity check** table (shared AC → Android impl → iOS impl →
identical?). Confirm the mode is M3+ when two native trees are in scope.

**Depth by mode (this phase always runs).** In M1, keep `impact-analysis.md` and
`impl-plan.md` brief — a short impact table and a skeleton are enough; if an area is
not affected, one line stating why suffices. Never skip the artifact. M3+ adds the
on-demand deep artifacts noted in `mode-decision.md` (e.g. `fe-be-contract-map.md`,
`heavy-source-analysis.md`).

If the change involves DB changes or contract changes, recommend escalating to a
Heavy mode and note it. Verify against the real source. When done, tell the user
the next step is `/sdd-implement $ARGUMENTS`.
