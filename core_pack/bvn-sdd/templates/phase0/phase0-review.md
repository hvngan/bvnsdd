# Phase 0-A Review — <PROJECT>

> Human sign-off on the Safety Gate phase. AI pre-ticks items it confirmed
> during `/sdd-phase0a`. A human must tick the final sign-off line.

## Deliverables

| Artifact | Created | Content reviewed by AI | Content reviewed by human |
|---|---|---|---|
| `.claude/CLAUDE.md` | | | |
| `.claude/settings.json` | | | |
| `.claude/rules/00-safety.md` | | | |
| `.claude/rules/30-security.md` | | | |
| `docs/maintenance/phase0/phase0-plan.md` | | | |
| `docs/maintenance/phase0/phase0-decisions.md` | | | |
| `docs/maintenance/phase0/phase0-execution-log.md` | | | |
| `docs/maintenance/phase0/phase0-risk-register.md` | | | |
| `docs/standards/automation/context-loading-policy.md` | | | |
| `docs/standards/automation/external-content-intake.md` | | | |
| `docs/standards/automation/repo-intake-checklist.md` | | | |

## Safety checklist

- [ ] No real secrets are committed to the repository
- [ ] `.env` and credential files are in `.gitignore`
- [ ] Permission policy (deny/ask/allow) is appropriate for this project
- [ ] All hooks have been inspected and are safe
- [ ] All MCP servers have been reviewed; none have unvetted write/delete/send access
- [ ] External document handling policy is understood by the team
- [ ] Context loading order is agreed upon
- [ ] Large auto-generated directories are excluded from AI context
- [ ] Language setting matches team preference
- [ ] Risk register has been reviewed and High/Medium risks have mitigations

## Open items before sign-off

_List anything that must be resolved before Phase 0-A is considered complete._

| Item | Owner | Due |
|---|---|---|
| | | |

## Human sign-off

> **This line must be completed by a human, not AI.**

- [ ] I have read the phase0 artifacts and confirm Phase 0-A is complete.

Signed: __________________ Date: __________________
