---
description: BVN-SDD Phase 7 — design and run black-box tests from the user/AC perspective, without reading implementation.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are the black-box tester for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read ONLY: `spec-pack.md` (AC, Input/Output, contract, Validation/Error, Security/Permission), `mode-decision.md`, `test-plan.md`.
**Do NOT read implementation source code** — black-box tests must reflect the spec, not what was built.

**Plan first.** State goal, reads, writes, Stop/Ask points, steps. Do not edit until acknowledged.

Goal: produce two files in the ticket folder:
- `blackbox-testcases.md` — a concrete, runnable set of test scenarios derived
  entirely from the spec, covering the cases most likely to reveal
  spec-vs-implementation divergence.
- `test-data.md` — fixtures, seed data, environment variables, and cleanup
  steps required to run the test cases.
- `blackbox-review-checklist.md` — QA-perspective checklist: AC coverage,
  UX, data/state, API contract, and sign-off. Fill each item as you run
  or review the test cases.

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
3a. **Multi-platform** (when `.bvn-sdd/config.yml` `platforms:` lists more than
   one): derive cases from the shared spec only, and tag each with `Platform:`.
   When the observable behavior is identical across platforms, write one case
   marked `Both`; when the surface differs (e.g. a Compose permission dialog vs.
   an iOS Settings deep-link), write one case per platform. Cover every AC on
   every in-scope platform.
4. After writing the cases, run as many as are automatically runnable (API calls,
   CLI commands, automated tests). Record results in `test-results.md` under a
   section headed `## Black-box results`.
5. For cases that require a running environment unavailable here, mark them
   `Status: Manual — not run` and explain what environment is needed.
6. Never claim a test passed without running it.

## Stop / Ask condition

Spec doesn't define expected output → add open issue, skip that test case. Do not invent assertions.

When done: report how many test cases were written, how many were run, how many
passed, and how many are manual. Confirm that `test-data.md` is populated with
all fixtures and environment requirements, and that `blackbox-review-checklist.md`
sign-off items are ticked. Tell the user to run `/sdd-report $ARGUMENTS` next.
