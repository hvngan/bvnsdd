# Review Checklist — <TICKET>

> Define the review viewpoints before implementing. Tick during self-review.

## Spec / AC match
- [ ] Every acceptance criterion is satisfied
- [ ] No requirement added beyond the spec-pack

## General system
- [ ] Numbers, ranges, and units correct
- [ ] Full-width / character-type handling correct
- [ ] No stray magic numbers or hard-coded literals

## FE
- [ ] UI states (loading/empty/error) handled
- [ ] Input validation and messages match spec

## BE / API
- [ ] Contract (request/response/error codes) matches spec
- [ ] Idempotency / concurrency considered

## DB / Migration
- [ ] Schema/migration correct and reversible
- [ ] Query performance and volume considered

## Security / Privacy
- [ ] AuthN/AuthZ enforced; no PII or secret leakage
- [ ] Audit logging where required

## Operation / Maintenance
- [ ] Logging, metrics, and recovery adequate

## Test
- [ ] Each AC mapped to a test; risky cases covered

## Docs / Traceability
- [ ] Artifacts updated; change traceable spec → code → test

## Release / Rollback
- [ ] Rollout and rollback steps clear
