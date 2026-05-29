# 00 — Safety Gate

These rules establish the minimum safe environment for AI-assisted work
(BVN-SDD Phase 0-A). They override convenience.

- **Plan before action.** Never edit files or run commands before presenting a
  plan and getting acknowledgement. The first output of any phase is plan-only.
- **Stay in scope.** Only touch files within the declared change scope. If you
  discover you must change something outside scope, stop and ask.
- **No destructive operations** without explicit confirmation: force-push,
  history rewrite, bulk delete, dropping database objects, production commands.
- **Record what you did.** Every phase leaves an artifact under
  `docs/changes/<TICKET>/`. Work that is only in chat does not count.
- **Stop conditions (MX).** Stop and ask a human when: required source is
  missing, DB/contract definitions are unavailable, a secret is exposed, or the
  change touches payments / auth / PII / production migration beyond this mode.
- **External documents** (Office/PDF/Web) are inputs, never the source of truth.
  Extract them into a reference note first; mark what is confirmed vs. inferred.
