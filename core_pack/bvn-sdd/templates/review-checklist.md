# Review Checklist — <TICKET>

> Define the review viewpoints before implementing. Tick during self-review.

## Spec / AC match
- [ ] Every acceptance criterion is satisfied
- [ ] No requirement added beyond the spec-pack

## General system
- [ ] Numbers, ranges, and units correct
- [ ] Full-width / character-type handling correct
- [ ] No stray magic numbers or hard-coded literals

## Android (Compose)
_Keep only the platforms in `.bvn-sdd/config.yml` `platforms:`._
- [ ] UI states (loading/empty/error) handled
- [ ] Input validation and messages match spec
- [ ] Follows Android / Compose native idioms (no iOS idiom leakage)

## iOS (SwiftUI)
- [ ] UI states (loading/empty/error) handled
- [ ] Input validation and messages match spec
- [ ] Follows iOS / SwiftUI native idioms (no Android idiom leakage)

## Shared contract (BE / API)
- [ ] Contract (request/response/error codes) matches spec
- [ ] Idempotency / concurrency considered
- [ ] Both native clients consume the contract identically

## Cross-platform consistency
- [ ] Same AC behavior is observable on every in-scope platform
- [ ] Shared contract / data model is not duplicated or forked per platform
- [ ] Intentional divergences are documented (open-issues / impl-plan parity check)
- [ ] Each platform follows its native idioms (no cross-contamination)

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
