# Walkthrough: A Heavy DB migration with BVN-SDD (M4, existing system)

**Scenario**: The same e-commerce backend must **split the `orders.customer_name`
column into `orders.customer_id` + a new `customers` table** — a destructive-leaning
schema change with backfill, on a system with production data. This is **M4 (Heavy)**:
full depth, on-demand deep artifacts (heavy source analysis, security review,
independent review), an explicit expand-contract rollback plan — and **no phase is
skipped**.

> This is a **documentation example**. It deliberately shows a **test FAIL → fix**
> cycle and the M4-only deep artifacts that are **created on demand** (not part of the
> default 20-file scaffold), illustrating "Core light, options deep".
>
> The mode raises **depth**, never skipping phases. Only MX halts.

**Ticket overview**

| | |
|---|---|
| Ticket | **T-077** — normalise customer data: `customer_name` → `customer_id` + `customers` |
| Stack | Spring Boot 3, JPA, **Flyway** migrations, PostgreSQL (prod data) |
| Mode | **M4 (Heavy)** — schema migration, backfill, multi-layer impact |
| Deep artifacts (on demand) | `heavy-source-analysis.md`, `security-review.md`, `codex-review.md` |

---

## Phase 0-A / 0-B (already done for this repo)

`project_type = existing` is already recorded; the survey maps from `/sdd-map` exist
(see the survey example). For an M4 ticket you **re-run `/sdd-map` for the affected
area** to refresh `repository-db-map.md` and `route-api-map.md` before planning.

---

## T-077 Bootstrap — `/sdd-new T-077 Normalise customer data`

---

### Phase 1 — Spec Pack (`/sdd-spec T-077`)

```markdown
## 6. Acceptance Criteria
- [ ] AC-1: New `customers` table (id, name, created_at); unique on name during transition.
- [ ] AC-2: `orders.customer_id` FK → customers.id, nullable during expand phase.
- [ ] AC-3: Every existing order is backfilled to a customer row (no data loss).
- [ ] AC-4: API/response behaviour unchanged for clients (customer_name still returned).
- [ ] AC-5: Migration is reversible up to the contract phase; rollback documented.
- [ ] AC-6: No PII (customer_name) written to logs during backfill.

## 11. Security / Privacy
customer_name is PII. Backfill must not log names; access stays within existing scope.
```

`source-availability.md` → GREEN. `open-issues.md` OI-1: "Duplicate names — merge or
keep distinct customers?" (blocking — needs human decision).

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-077`)

```markdown
# Mode Decision — T-077
## Scoring: Reversibility 3 | Uncertainty 2 | Risk 3 | Scope 3  → M4
## Decision: M4 (Heavy) — destructive-leaning schema change + backfill on prod data.
## Per-phase depth: every phase runs at FULL depth (no skipping).
## On-demand deep artifacts required this ticket:
##   - heavy-source-analysis.md  (call sites of customer_name)
##   - security-review.md        (PII in backfill/logs)
##   - codex-review.md           (independent review before merge)
## Human gate: OI-1 must be resolved before Phase 3; rollback verified before merge.
```

**Stop/Ask**: OI-1 is blocking → AI stops and asks. **You** decide: "Keep distinct
customers per unique name; duplicates are acceptable for now."

---

### Phase 2 — Context (`/sdd-context T-077`)

Full-depth, plus the on-demand **heavy source analysis**:
```markdown
# heavy-source-analysis.md — T-077  (M4 deep artifact, created on demand)
## customer_name read/write sites (verified via Grep)
- OrderEntity.customerName            (JPA field)        — write path
- OrderMapper.toResponse              (reads name)       — AC-4 keep returning
- OrderSearchRepository.byCustomer    (LIKE on name)     — must switch to join
- ReportJob.exportCustomers           (batch, nightly)   — risk: reads name in bulk
## Risk areas
- ReportJob runs nightly → migration must not break it mid-deploy (expand-contract).
- Search by name uses an index → plan a replacement index on customers(name).
```
`context.md` records the forbidden pattern: **never log `customerName`** (AC-6).

---

### Phase 3 — Plan (`/sdd-plan T-077`)

```markdown
# Impl Plan — T-077  (expand → migrate → contract)
## Phase A (expand, reversible):
  V12__create_customers.sql        — new table, nullable orders.customer_id
  Deploy app that DUAL-WRITES name + customer_id
## Phase B (backfill):
  V13__backfill_customers.sql      — insert distinct names → customers; set orders.customer_id
  Backfill in batches; NO name logging (AC-6)
## Phase C (contract, later ticket): drop orders.customer_name once all readers migrated

## Migration / rollback approach
- Phase A/B reversible: drop customer_id + customers (data preserved in customer_name).
- Rollback script: V13_rollback.sql documented and tested in staging.
- Point of no return: Phase C (separate ticket, separate approval).
```

---

### Phase 4+5 — Implement + reviews (`/sdd-implement T-077`)

Dual-write implementation + Flyway scripts. Then **two reviews** (M4 depth):

```markdown
# self-review.md (Claude)
- [x] Dual-write keeps customer_name (AC-4 backward compatible)
- [x] Backfill batched; no name in logs (AC-6)
- [ ] WARN: unique(name) constraint will fail on existing duplicate names → see tests

# codex-review.md (independent, M4 on-demand)
Verdict: NEEDS_FIX
- [Major] V12 adds UNIQUE(name) but production has duplicate names → migration will abort.
  Fix: make the transition unique a partial/deferred constraint, or dedupe-by-id not name.
```

The independent review caught a real defect before merge.

---

### Phase 6 — Test (`/sdd-test T-077`) — FAIL → fix

```markdown
# test-results.md — Run 1
FAIL  MigrationTest.backfillPreservesAllOrders
  → V12 UNIQUE(name) violated: 2 existing rows named "John Smith".
  Root cause: real prod-like data has duplicate names (matches codex-review Major).

# Fix applied
- V12: replace UNIQUE(name) with UNIQUE(id); allow duplicate names during transition
  (matches OI-1 decision: keep distinct customers per row).
- Re-run backfill: each order → its own customer row.

# test-results.md — Run 2
PASS  MigrationTest.backfillPreservesAllOrders   (0 orders lost; 1:1 mapping)
PASS  MigrationTest.rollbackRestoresState
PASS  OrderApiContractTest.customerNameStillReturned   (AC-4)
PASS  BackfillLoggingTest.noPiiInLogs                  (AC-6)
```

> This FAIL→fix cycle is the point: M4 depth (independent review + a real migration
> test) caught a production-data hazard the happy path would have missed.

---

### Phase 7 — Black-box (`/sdd-blackbox T-077`)

```markdown
### TC-1: Existing order still readable
Input: GET /api/orders/9001 (created before migration)
Expected: customer_name returned as before (AC-4); now also linked to a customer_id.

### TC-2: Rollback drill (staging)
Steps: apply V12+V13, then run documented rollback.
Expected: schema + data return to pre-migration state; no order lost (AC-5).

### TC-3: Backfill log inspection
Steps: run backfill with debug logging on.
Expected: no customer name string appears in any log line (AC-6).
```

---

### Phase 8 — Report (`/sdd-report T-077`)

```markdown
# Final Report — T-077   Status: COMPLETE (expand + backfill phases)
Normalised customer data via expand-contract. Dual-write keeps the API stable (AC-4).
Independent review + migration test caught a duplicate-name abort before merge.
Tests: Run 1 FAIL (duplicate names) → fixed → Run 2 all PASS.

## Accepted risks
- AR-1: orders.customer_name kept until the contract ticket (T-09x) — intentional.
## Security
- security-review.md: PASS — no PII in logs; access scope unchanged.
## Follow-up
- T-09x: contract phase (drop customer_name) — separate ticket + approval (point of no return).
```

---

### Phase 9 — Learnings (`/sdd-learnings T-077`)

```markdown
# Promotion Candidates — T-077
## PC-1 → docs/maintenance/failure-mode-index.md
Failure: assuming a column is unique during migration. Prod data had duplicate names.
Prevention rule: never add UNIQUE on free-text data without a dedupe/transition plan.
## PC-2 → docs/standards/database.md
Always use expand → backfill → contract across separate deploys; keep each step reversible.
```

---

## Summary — what M4 (Heavy) adds, with no phase skipped

| Aspect | M2/M3 | **M4 (this example)** |
|---|---|---|
| Phases run | all | all (full depth) |
| Source analysis | standard maps | + `heavy-source-analysis.md` (call sites, batch risk) |
| Review | self (+ optional codex) | self **+ independent `codex-review.md`** (caught the defect) |
| Security | inline | + dedicated `security-review.md` (PII in backfill) |
| Migration | usually none | expand→backfill→contract + tested rollback |
| Tests | PASS | **FAIL→fix** on prod-like data, then PASS |

The deep artifacts above are created **on demand for M4** — they are not scaffolded
into every ticket, keeping the core light for M1/M2 work.
