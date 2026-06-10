# 06 — Universal Stop / Ask Conditions

Stop immediately and ask a human when any of the following apply. These
conditions override mode and convenience — they apply in every phase.

- **Blocking open issue.** An entry in `open-issues.md` is marked blocking and
  unresolved.
- **Missing required source.** Source code, DB schema, or spec needed to proceed
  safely is absent and cannot be inferred.
- **Secret or PII exposed.** A secret, credential, key, token, or PII file would
  need to be read or produced.
- **High-risk domain without clearance.** The change touches payments,
  authentication, PII handling, or a production migration beyond the chosen mode.
- **Destructive operation only path.** Force-push, history rewrite, bulk delete,
  DB drop, or production deploy is the only way forward.
- **Shared rule amendment.** A promotion candidate would modify `.claude/rules/*`
  or `docs/standards/*` — propose the change and wait for confirmation; do not
  apply it unilaterally.
- **Contradictory artifacts.** Facts are irreconcilably contradictory between
  artifacts and cannot be resolved from source code alone.
- **Mode M5 or MX triggered.** Escalate to human lead; do not auto-proceed.
