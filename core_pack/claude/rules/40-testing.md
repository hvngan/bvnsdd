# 40 — Testing

- **Tests are evidence, not decoration.** Their purpose is to catch regressions,
  boundary bugs, and contract violations — not to inflate coverage numbers.
- **Trace every AC.** Each acceptance criterion in `spec-pack.md` must map to at
  least one test in `test-plan.md`.
- **Cover the risky cases:** boundary values, permission differences, state
  transitions, async/idempotency/double-submit, error and timeout paths.
- **Reuse existing tests** before writing new ones; note which existing tests
  already cover the change.
- **Record real runs.** Put the exact commands and PASS/FAIL results in
  `test-results.md`. Never claim a test passed without running it.
- **Black-box view (optional in v1).** Where useful, describe test cases in
  user/QA-observable terms so non-developers can verify them.
