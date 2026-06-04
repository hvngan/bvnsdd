# Mode Decision — <TICKET>

> This document is the authoritative record of the operating mode chosen for this
> ticket. The mode sets the DEPTH of each phase — it does not skip phases. Every
> ticket runs the full sequence (context → plan → implement → test → blackbox →
> report → learnings); a light mode just keeps each artifact brief. Only MX halts.

## Scoring

| Criterion | Score (1–3) | Justification |
|---|---|---|
| Reversibility | | |
| Uncertainty | | |
| Risk | | |
| Scope | | |
| **Total** | | |

## Chosen mode

**M? — Name**

_One-paragraph rationale referencing the score and any override conditions._

## Blocking issues checked

- [ ] No unresolved blocking issues in `open-issues.md`
- [ ] Scope is clear enough to score Uncertainty with confidence

## Per-phase depth

_Every phase runs. Record how deep each goes for this mode (brief / standard /
full), not whether it is skipped._

| Phase | Depth (brief / standard / full) | Notes |
|---|---|---|
| Context (`/sdd-context`) | | |
| Plan (`/sdd-plan`) | | |
| Implement + review (`/sdd-implement`) | | |
| Test (`/sdd-test`) | | |
| Black-box (`/sdd-blackbox`) | | |
| Report (`/sdd-report`) | | |
| Learnings (`/sdd-learnings`) | | |

## On-demand deep artifacts (M3+)

_Deep artifacts to add for this ticket if the mode/scope needs them — created on
demand, not part of the default scaffold. Leave empty for M1/M2._

| Artifact | Needed? | Reason |
|---|---|---|
| `fe-be-contract-map.md` | | |
| `security-review.md` | | |
| `codex-review.md` | | |
| `heavy-source-analysis.md` | | |

## Human decisions required before proceeding

_Any decisions that must be made by a human before the next phase can start._
