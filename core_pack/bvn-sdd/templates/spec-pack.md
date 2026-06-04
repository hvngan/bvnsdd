# Spec Pack — <TICKET>

> Single source of truth for this ticket. Acceptance Criteria must be testable.
> Inferences go in Assumptions; items needing a human go in Open Issues.

## 1. Overview
_What this change is, in one paragraph._

## 2. Context / Purpose
_Why it is being done; the problem or need it addresses._

## 3. Scope
_What is included._

## 4. Out of scope
_What is explicitly excluded._

## 5. Business glossary / preconditions
_Domain terms and assumptions a reader needs._

## 6. Acceptance Criteria
_Testable conditions. Use a checklist; reference IDs (AC-1, AC-2, ...)._
- [ ] AC-1:

## 7. Input / Output
_Inputs, outputs, and their shapes._

## 8. Surface impact (per platform)
_What surfaces this change touches. Name the functional surface, not the widget
(stay neutral on the HOW). For a single platform, keep only its row._
| Platform | Screens / surfaces touched | Backend / API touched | Data / events |
|---|---|---|---|
| Shared (contract) |  |  |  |
| Android |  |  |  |
| iOS |  |  |  |

## 9. Client/Service contract (platform-neutral)
_Request/response shape, field names, types, error codes (if applicable). This
contract is identical for every client (Android and iOS consume it the same
way). Mark platform-only fields `[android-only]` / `[ios-only]`, but still
define their type here._

## 10. Validation / Error / Messages
_Validation rules, error handling, user-facing messages._

## 11. Security / Privacy / Permission / Audit
_Auth, authorization, PII handling, audit logging considerations._

## 12. Operation / Logging / Monitoring / Recovery
_Operational concerns: logging, metrics, alerts, recovery._

## 13. Test Strategy Summary
_How this will be tested at a high level._

## 14. Source Availability Summary
_What source was available; see source-availability.md for detail._

## 15. Complexity Classification
_Recommended mode: M1 Light / M2 Standard / M3 Plus / M4 Heavy / M5 Critical.
Briefly justify. Note: delivering two native trees (e.g. Android + iOS) from one
spec raises baseline scope — consider M3+._

## 16. Assumptions
_Anything inferred rather than confirmed._

## 17. Open Issues
_Pointer to open-issues.md; list the blocking ones here._

## 18. Human Decisions Required
_Decisions only a human can make before/at implementation._
