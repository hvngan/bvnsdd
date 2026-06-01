# Black-box Review Checklist — <TICKET>

> QA / user-perspective review checklist. Filled during Phase 7 (`/sdd-blackbox`).
> Written from the outside — no knowledge of implementation details.

## AC coverage

- [ ] Every AC in spec-pack.md has at least one test case
- [ ] Happy path covered for each AC
- [ ] Error path covered (invalid input, missing fields, out-of-range)
- [ ] Boundary values covered
- [ ] Permission boundaries covered (allowed AND denied roles)

## User experience

- [ ] Error messages match the exact wording in spec
- [ ] UI states (loading, empty, error) verified where applicable
- [ ] Behaviour is predictable from a non-technical user's perspective

## Data / state

- [ ] Test data defined and documented in `test-data.md`
- [ ] State / fixtures cleaned up after tests

## API contract

- [ ] Response shape matches the spec contract (field names, types)
- [ ] HTTP status codes match spec
- [ ] Error response shape matches spec

## Test execution summary

| TC-# | Description | Status | Note |
|------|-------------|--------|------|
| | | Pass / Fail / Manual | |

## Sign-off

- [ ] All P0 cases pass
- [ ] P1 failures have open issues filed

