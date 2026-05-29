---
description: BVN-SDD Phase 6 — design tests and record real results.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are designing and running tests for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/` and the test tree.

Read first: this ticket's `spec-pack.md` (Acceptance Criteria), `impl-plan.md`,
`self-review.md`, and existing tests.

**Plan first** (goal, files to read, files to update, Stop/Ask points, plan).

Goal: tests are evidence — catch regressions, boundary bugs, and contract
violations, not pad coverage.

Update:
- `test-plan.md` — a matrix mapping each AC to test types (FE unit, BE unit, API
  integration, contract, DB, E2E, black-box); priority; existing tests reused;
  new tests this time; test-data approach; exact run commands. Cover boundary
  values, permission differences, state transitions, async/idempotency/double-
  submit, error and timeout paths.
- Then write/adjust the test code as planned.
- Run build/lint/test and record into `test-results.md`: environment, exact
  commands, PASS/FAIL list, bugs fixed vs. outstanding, remaining risks.

Never claim a test passed without running it. When done, tell the user to run
`/sdd-report $ARGUMENTS`.
