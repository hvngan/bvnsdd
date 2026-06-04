# Test Plan — <TICKET>

> Tests are evidence. Map every AC to a test; cover the risky cases.

## AC ↔ test matrix
_Every AC is covered on every in-scope platform. A shared contract test may
cover the Shared row. For a single platform, only its rows apply._
| AC | Platform | Test type | Test name / location | Priority |
|---|---|---|---|---|
|  | Shared / Android / iOS | unit / integration / contract / e2e / black-box |  | H/M/L |

## Existing tests reused
_Which current tests already cover part of this change._

## New tests this time
_What to add._

## Risky cases to cover
- Boundary values:
- Permission differences:
- State transitions:
- Async / idempotency / double-submit:
- Error / timeout paths:
- Cross-platform parity: same input yields the same observable result on Android and iOS.

## Test data approach
_How test data is created; no real PII._

## Run commands
_One block per in-scope platform. Keep only the platforms that apply._
```
# Android — exact commands to run the tests
```
```
# iOS — exact commands to run the tests
```
