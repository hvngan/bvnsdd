# 10 — Development

- **Minimal change.** Implement the smallest change that satisfies the
  acceptance criteria in `spec-pack.md`. Do not add unrequested features.
- **Follow existing patterns.** Read neighbouring code and tests before writing.
  Match naming, structure, error handling, and logging conventions already in use.
- **Do not call APIs that do not exist.** Confirm a method/class exists in the
  source before using it. List confirmed-existing vs. forbidden patterns in the
  ticket's `context.md`.
- **Do not reproduce known bugs or violations** present in surrounding code, even
  to "stay consistent". Note them instead.
- **Run what you can.** Execute lint, build, and tests within reach and record
  the commands and results in `self-review.md` / `test-results.md`.
- **When in doubt, stop.** Unresolved questions go to `open-issues.md`; do not
  guess your way through business rules.
