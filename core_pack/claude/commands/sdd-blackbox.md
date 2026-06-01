---
description: BVN-SDD Phase 7 — design and run black-box tests from the user/AC perspective, without reading implementation.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are the black-box tester for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read first — ONLY these files:
- `spec-pack.md` (Acceptance Criteria, Input/Output, FE/BE contract,
  Validation/Error/Messages, Security/Permission sections)
- `mode-decision.md` (to know which test types are required)
- `test-plan.md` (to avoid duplicating unit/integration tests already planned)

**Do NOT read implementation source code.** Black-box tests verify behavior from
the outside, as a user or API caller would experience it. Reading implementation
biases the tests toward what was built, not what was specified.

**Plan first** (goal, files to read, files to update, Stop/Ask points, plan).
Do not edit until acknowledged.

Goal: produce `blackbox-testcases.md` — a concrete, runnable set of test
scenarios derived entirely from the spec, covering the cases most likely to
reveal spec-vs-implementation divergence.

## What to produce

For each Acceptance Criterion (AC-N) in `spec-pack.md`:

1. **Happy path** — nominal input, expected output, exact assertion.
2. **Boundary / edge cases** — values at the boundary of valid input, empty
   input, maximum input, special characters.
3. **Permission / role boundary** — who is allowed, who is denied; verify both.
4. **Error path** — invalid input, missing required fields, out-of-range values;
   verify the error message and code, not just that an error occurred.

Additionally, for any API contract defined in `spec-pack.md` section 9:

5. **Contract test** — call the endpoint with the exact request shape; assert the
   response matches the defined contract (field names, types, status codes).
6. **Error contract** — call with invalid data; assert error response matches the
   defined error shape.

## Format of each test case

```
### TC-<N>: <short title>
AC: AC-N
Type: happy-path | boundary | permission | error | contract
Precondition: <setup state>
Input: <exact input>
Expected output: <exact assertion>
Run command: <exact command or curl or UI steps>
```

## Instructions

1. List every AC from `spec-pack.md`. Do not skip any.
2. Write at least one test case per AC (more for complex ACs).
3. For ACs with permission rules, write both the allowed and denied case.
4. After writing the cases, run as many as are automatically runnable (API calls,
   CLI commands, automated tests). Record results in `test-results.md` under a
   section headed `## Black-box results`.
5. For cases that require a running environment unavailable here, mark them
   `Status: Manual — not run` and explain what environment is needed.
6. Never claim a test passed without running it.

## Stop / Ask conditions

- If the spec does not define the expected output for a scenario, do not invent
  it. Add an open issue to `open-issues.md` and skip that test case.
- If running a test would require destructive side effects (deleting production
  data, sending real emails, charging real money), stop and ask before running.

When done: report how many test cases were written, how many were run, how many
passed, and how many are manual. Tell the user to run `/sdd-report $ARGUMENTS`
next.
