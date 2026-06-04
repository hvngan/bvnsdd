# Walkthrough: Adding a field to an EXISTING API with BVN-SDD (Survey mode, M3)

**Scenario**: You join an existing e-commerce backend (Spring Boot) + web frontend
(React). Ticket **T-042** asks for a small but contract-touching change: the Order
detail API should also return a human-readable `statusLabel` so the frontend stops
hard-coding status text. There IS source code — so Phase 0-B runs in **Survey mode**
(reads real source), and because it changes the FE/BE contract the mode is **M3**.

> This is a **documentation example** — it shows what the artifacts look like for an
> existing codebase, not real code you must run. Compare with
> `EXAMPLE-ios-weather-en.md` (greenfield) to see what Survey mode adds.
>
> **Every phase runs.** M3 sets depth (standard + contract focus); it does not skip
> any phase. Only MX halts.

**Project overview**

| | |
|---|---|
| Backend | Java 17, Spring Boot 3, JPA/Hibernate, PostgreSQL |
| Frontend | React 18, TypeScript, React Query |
| State | **Existing** codebase, brownfield |
| Ticket | **T-042** — add `statusLabel` to `GET /api/orders/{id}` response |
| Mode | **M3** (FE/BE contract change) |

---

## 0. Setup (in the existing repo)

```bash
cd ecommerce-platform          # your existing monorepo
bvn-sdd init --here --lang en
# ✓ .claude/ .bvn-sdd/ docs/ created (existing files are never overwritten)
```

Open in **Claude Code**, then run `/sdd-phase0a`.

---

## Phase 0-A — Safety Gate (existing project)

```
/sdd-phase0a

Project: ecommerce-platform — existing Spring Boot API + React web.
Stack: Java 17 / Spring Boot 3 / JPA / PostgreSQL; React 18 / TS / React Query.
Constraints: production DB exists — never run destructive migrations from here.
Secrets: application-prod.yml holds DB creds — do NOT read it.
```

**What AI does**: Globs for source → finds `src/main/java/...`, `web/src/...` →
records `project_type = existing`.

**Generated** (excerpt) `docs/maintenance/phase0/phase0-plan.md`:
```markdown
## Project Type
existing — source detected (Spring Boot backend + React frontend)

## Safety Constraints Recorded
- DENY read: application-prod.yml, .env, *.pem
- ASK before: any Flyway/Liquibase migration, git push
- Source-of-truth priority: source code > docs > AI inference
```

`/sdd-phase0a` also writes `phase0-decisions.md`, `phase0-execution-log.md`,
`phase0-risk-register.md`, `phase0-review.md`, and the three
`docs/standards/automation/*` policies. **You** review `phase0-review.md` and sign off.

---

## Phase 0-B — Source Intelligence (SURVEY mode)

**Command**: `/sdd-map`

**What AI does**: `project_type = existing` → **Survey mode**. It does a *shallow*
read of the real source (not every file) and produces maps with **real paths** — no
`[PLANNED]` markers (contrast: the greenfield iOS example marks everything `[PLANNED]`).

**Generated** `docs/architecture/system-map.md` (excerpt):
```markdown
# System Map — ecommerce-platform   (Survey mode — observed from source)

## Components
| Component | Responsibility | Key locations |
|---|---|---|
| Order API | order CRUD + status | src/main/java/com/shop/order/ |
| Order domain | Order, OrderStatus enum | src/main/java/com/shop/order/domain/ |
| Web order page | order detail UI | web/src/features/orders/ |

## How they connect
React Query → GET /api/orders/{id} → OrderController → OrderService → OrderRepository → PostgreSQL
```

**Generated** (also real, not planned):
- `source-inventory.md` — key files & purpose
- `route-api-map.md` — `GET /api/orders/{id}`, `OrderController#getOrder`
- `repository-db-map.md` — `orders` table, `OrderStatus` enum values `1/2/3/4`
- `fe-be-contract-map.md` — current `OrderResponse` DTO shape consumed by the web app
- `test-map.md` — existing `OrderControllerTest`, `OrderServiceTest`, web `orderApi.test.ts`

**You**: skim the maps; they become the navigation guide for every ticket.

---

## T-042: add `statusLabel` to the Order response

### Bootstrap — `/sdd-new T-042 Order statusLabel`

Creates `docs/changes/T-042/` with the 20 blank artifacts.

---

### Phase 1 — Spec Pack (`/sdd-spec T-042`)

```
/sdd-spec T-042

Requirement: GET /api/orders/{id} must also return `statusLabel` — a human-readable
label for the existing numeric `status` (1=Pending, 2=Paid, 3=Shipped, 4=Cancelled).
The web order page should display statusLabel instead of mapping the number itself.
Labels are English for now; i18n is out of scope.
```

**AI reads first**: `docs/architecture/*` (the survey maps), then the real
`OrderController`, `OrderResponse`, `OrderStatus`. **Generated** `spec-pack.md` (excerpt):
```markdown
## 6. Acceptance Criteria
- [ ] AC-1: GET /api/orders/{id} response includes a new string field `statusLabel`.
- [ ] AC-2: statusLabel maps status 1→"Pending", 2→"Paid", 3→"Shipped", 4→"Cancelled".
- [ ] AC-3: Existing `status` (numeric) is unchanged — additive only, backward compatible.
- [ ] AC-4: Web order page shows statusLabel; removes its local number→text map.
- [ ] AC-5: Unknown status value → statusLabel = "Unknown" (no 500).

## 9. Client/Service contract (platform-neutral)
OrderResponse adds: statusLabel: string (non-null). `status` field unchanged.
Backward compatible: existing consumers ignoring the new field keep working.
```

`source-availability.md` → GREEN (all relevant source readable). `open-issues.md`
records OI-1: "Confirm label wording with product (Paid vs Completed?)".

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-042`)

```markdown
# Mode Decision — T-042
## Scoring: Reversibility 1 | Uncertainty 1 | Risk 2 | Scope 2  → M3
## Decision: M3 (Plus) — touches the FE/BE contract, so contract parity matters.
## Per-phase depth: all phases run at standard depth; extra focus on §9 contract.
## On-demand deep artifact: fe-be-contract-map.md (ticket-level).
```

> Even though the change is small, it crosses the FE/BE boundary → M3, not M1. All
> phases still run.

---

### Phase 2 — Context (`/sdd-context T-042`)

EXISTING PROJECT MODE — AI verifies against real source with Grep/Read.

```markdown
# Context — T-042
## Correct examples in the codebase
- src/main/java/com/shop/order/OrderResponse.java — DTO is a Java record; add field here.
- web/src/features/orders/orderApi.ts — React Query hook; types mirror the DTO.

## Methods / classes that actually exist (verified)
- OrderStatus enum: PENDING(1), PAID(2), SHIPPED(3), CANCELLED(4)  ← confirmed via Grep
- OrderMapper.toResponse(Order) — the single place DTOs are built; change here.

## Forbidden
- Do NOT add label logic in the React component (AC-4 removes the FE map).
- Do NOT change the numeric `status` serialization (AC-3).
```

`source-map.md` lists the real files to touch: `OrderResponse.java`,
`OrderMapper.java`, `orderApi.ts`, `OrderStatusBadge.tsx` + their tests.

---

### Phase 3 — Plan (`/sdd-plan T-042`)

```markdown
# Impact Analysis — T-042
| Area | Affected? | Detail |
| Shared contract | Yes | OrderResponse +statusLabel (additive, backward compatible) |
| BE / API | Yes | OrderMapper maps enum→label |
| Web FE | Yes | consume statusLabel; delete local map in OrderStatusBadge.tsx |
| DB | No | no schema change — derived from existing status |
| Test | Yes | BE mapper test, contract test, web component test |

# Impl Plan — T-042
## BE: add statusLabel to OrderResponse; OrderMapper switch on OrderStatus → label; default "Unknown".
## FE: orderApi.ts type +statusLabel; OrderStatusBadge.tsx renders statusLabel, remove numberToText().
## fe-be-contract-map.md: record field, type, nullability, the 4 enum→label rows + Unknown.
```

---

### Phase 4+5 — Implement (`/sdd-implement T-042`)

```java
// OrderResponse.java — additive field (status unchanged → AC-3)
public record OrderResponse(Long id, int status, String statusLabel, /* ... */) {}

// OrderMapper.java
static String label(OrderStatus s) {
    return switch (s) {
        case PENDING -> "Pending";
        case PAID -> "Paid";
        case SHIPPED -> "Shipped";
        case CANCELLED -> "Cancelled";
    }; // enum is exhaustive; defensive "Unknown" handled where status is parsed (AC-5)
}
```
```tsx
// OrderStatusBadge.tsx — now trusts the server label (AC-4)
export function OrderStatusBadge({ statusLabel }: { statusLabel: string }) {
  return <span className="badge">{statusLabel}</span>;
}
```

`self-review.md` checks: status unchanged (AC-3 ✓), FE map removed (AC-4 ✓), Unknown
path (AC-5 ✓). **You** fill `human-review.md`.

---

### Phase 6 — Test (`/sdd-test T-042`)

```markdown
# Test Plan — T-042
| AC | Test type | Test name | Priority |
| AC-2 | BE unit | OrderMapperTest.labelsEachStatus | H |
| AC-3 | contract | OrderResponseContractTest.statusStillNumeric | H |
| AC-5 | BE unit | OrderMapperTest.unknownStatusLabel | M |
| AC-4 | web unit | OrderStatusBadge.test.tsx.rendersServerLabel | H |

## Run commands
./gradlew test
cd web && npm test
```
`test-results.md`: 4 PASS. Backward-compat contract test confirms existing consumers
are unaffected.

---

### Phase 7 — Black-box (`/sdd-blackbox T-042`)

```markdown
### TC-1: Paid order shows label
Input: GET /api/orders/1001  (status=2 in DB)
Expected: response.statusLabel == "Paid"; response.status == 2 still present.

### TC-2: Backward compatibility
Input: an old client that ignores unknown fields calls GET /api/orders/1001
Expected: still parses; `status` numeric unchanged.

### TC-3: Web page
Input: open /orders/1001
Expected: badge shows "Paid" sourced from the API (no client-side mapping).
```

---

### Phase 8 — Report (`/sdd-report T-042`)

```markdown
# Final Report — T-042   Status: COMPLETE
Additive `statusLabel` shipped; numeric `status` unchanged (backward compatible).
BE 3 files, FE 2 files. Tests 4/4 PASS incl. contract backward-compat.
Accepted risk: none. Open issue OI-1 (wording) resolved with product: keep "Paid".
```

---

### Phase 9 — Learnings (`/sdd-learnings T-042`)

```markdown
# Promotion Candidates — T-042
## PC-1 → docs/standards/api-contract.md
Server owns human-readable labels; clients must not re-map enum→text locally.
## PC-2 → docs/maintenance/pattern-library.md
Additive-field pattern: extend DTO + keep old field → backward compatible by default.
```

After T-042, re-run `/sdd-map` if the contract maps need refreshing.

---

## Summary — what Survey mode adds vs greenfield

| | Greenfield (iOS example) | Survey mode (this example) |
|---|---|---|
| Phase 0-B source maps | `[PLANNED]` decisions | **Real paths**, observed from source |
| Phase 2 context | designs planned APIs | **verifies** real methods/enums via Grep |
| Risk focus | establishing architecture | **backward compatibility** of an existing contract |
| Phases run | all | all (M3 — depth, not skipping) |
