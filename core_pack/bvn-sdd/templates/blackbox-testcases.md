# Black-box Test Cases — <TICKET>

> Tests are derived from spec-pack.md only. Implementation code is not read.
> Each AC must have at least one test case.

## AC coverage map
_Cover every AC on every in-scope platform. The Platform column records which
platform each case targets (`Both` when behavior is identical)._

| AC | Platform | Happy path | Boundary | Permission | Error | Contract | Status |
|---|---|---|---|---|---|---|---|
| AC-1 | Both / Android / iOS | TC-? | TC-? | TC-? | TC-? | — | Pending |

---

## Test cases

### TC-1: <short title>
**AC:** AC-1
**Type:** happy-path
**Platform:** Shared / Android / iOS / Both _(identical behavior → one `Both`
case; differing surface → one case per platform)_
**Precondition:** _Setup state required before running._
**Input:** _Exact input values._
**Expected output:** _Exact assertion — field values, status code, message._
**Run command:**
```
# exact command
```
**Status:** Pending / Pass / Fail / Manual — not run
**Notes:** _If fail: what was different from expected._

---

<!-- Repeat TC-N block for each test case -->
