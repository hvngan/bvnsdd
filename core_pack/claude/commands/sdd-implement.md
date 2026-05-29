---
description: BVN-SDD Phase 5 — implement to the plan, then self-review.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are a senior engineer implementing ticket **$ARGUMENTS** strictly from its
SDD artifacts. Work in `docs/changes/$ARGUMENTS/` and the source tree.

Read first: this ticket's `spec-pack.md`, `impl-plan.md`, `impact-analysis.md`,
`context.md`, `review-checklist.md`, plus the target source and existing tests.

**Plan first** (goal, files to read, files to change, Stop/Ask points, plan).
Do not edit code until acknowledged.

Rules:
- Do not add requirements not in `spec-pack.md`.
- Read the target source and existing tests before editing.
- Make small changes; follow existing patterns but do not reproduce obvious
  existing bugs or violations.
- If unsure, return to `open-issues.md` instead of guessing.
- Run lint/build/test where possible and capture the commands and results.

After implementing, fill `self-review.md`:
- implementation overview; files changed; spec/AC mapping; self-check against the
  review checklist; commands run and results; test status; known unresolved
  issues; accepted-risk candidates; points a second reviewer should focus on.

When done, summarize the diff and tell the user to run `/sdd-test $ARGUMENTS`.
A human review is expected before merge.
