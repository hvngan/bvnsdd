# 50 — Review

Review happens in layers. Define the viewpoints *before* implementing
(`review-checklist.md`), then check against them.

- **Self-review (you).** After implementing, fill `self-review.md`: what changed,
  how it maps to spec/AC, checklist results, commands run, known issues,
  accepted-risk candidates, and points a second reviewer should focus on.
- **Be specific.** Findings must include file path, evidence, reproduction
  condition, impact, and a suggested fix. No vague comments.
- **Classify findings:** Blocker / Major / Minor / Question / False-positive /
  Accepted-risk. Address Blocker and Major first.
- **Lower confidence honestly.** If unsure a finding is real, mark it Question
  and state how to confirm it.
- **Human has the final say.** A human approves or rejects, with a recorded
  reason. Do not self-approve and merge.
- **Checklist viewpoints:** spec/AC match, general system (numbers, full-width
  characters, magic numbers), FE, BE/API, DB/migration, security/privacy,
  operation/maintenance, test, docs/traceability, release/rollback.
