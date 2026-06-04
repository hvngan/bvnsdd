# Hướng dẫn: DB migration nặng với BVN-SDD (M4, hệ thống có sẵn)

**Bối cảnh**: Cùng backend thương mại điện tử cần **tách cột `orders.customer_name`
thành `orders.customer_id` + bảng `customers` mới** — thay đổi schema thiên hướng
phá huỷ, có backfill, trên hệ thống có dữ liệu production. Đây là **M4 (Heavy)**: độ
sâu đầy đủ, artifact sâu theo nhu cầu (heavy source analysis, security review,
independent review), kế hoạch rollback expand-contract rõ ràng — và **không bỏ phase nào**.

> Đây là **ví dụ tài liệu**. Nó cố ý cho thấy chu trình **test FAIL → fix** và các
> artifact M4 **tạo theo nhu cầu** (không nằm trong bộ 20 file scaffold mặc định),
> minh hoạ "Core nhẹ, option sâu".
>
> Mode nâng **độ sâu**, không bỏ phase. Chỉ MX mới dừng.

**Tổng quan ticket**

| | |
|---|---|
| Ticket | **T-077** — chuẩn hoá dữ liệu khách: `customer_name` → `customer_id` + `customers` |
| Stack | Spring Boot 3, JPA, **Flyway** migration, PostgreSQL (dữ liệu prod) |
| Mode | **M4 (Heavy)** — migration schema, backfill, ảnh hưởng nhiều tầng |
| Artifact sâu (theo nhu cầu) | `heavy-source-analysis.md`, `security-review.md`, `codex-review.md` |

---

## Phase 0-A / 0-B (đã làm cho repo này)

`project_type = existing` đã được ghi; bản đồ survey từ `/sdd-map` đã có (xem ví dụ
survey). Với ticket M4 bạn **chạy lại `/sdd-map` cho vùng bị ảnh hưởng** để làm mới
`repository-db-map.md` và `route-api-map.md` trước khi lập kế hoạch.

---

## T-077 Bootstrap — `/sdd-new T-077 Normalise customer data`

---

### Phase 1 — Spec Pack (`/sdd-spec T-077`)

```markdown
## 6. Acceptance Criteria
- [ ] AC-1: Bảng `customers` mới (id, name, created_at); unique trên name trong giai đoạn chuyển tiếp.
- [ ] AC-2: `orders.customer_id` FK → customers.id, nullable trong giai đoạn expand.
- [ ] AC-3: Mọi order hiện có được backfill sang một customer row (không mất dữ liệu).
- [ ] AC-4: Hành vi API/response không đổi với client (vẫn trả customer_name).
- [ ] AC-5: Migration đảo ngược được đến giai đoạn contract; rollback có tài liệu.
- [ ] AC-6: Không ghi PII (customer_name) vào log khi backfill.

## 11. Security / Privacy
customer_name là PII. Backfill không được log tên; quyền truy cập giữ trong scope hiện có.
```

`source-availability.md` → GREEN. `open-issues.md` OI-1: "Tên trùng — gộp hay giữ
khách riêng biệt?" (blocking — cần người quyết).

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-077`)

```markdown
# Mode Decision — T-077
## Scoring: Reversibility 3 | Uncertainty 2 | Risk 3 | Scope 3  → M4
## Quyết định: M4 (Heavy) — đổi schema thiên phá huỷ + backfill trên dữ liệu prod.
## Độ sâu mỗi phase: mọi phase chạy ở độ sâu ĐẦY ĐỦ (không bỏ).
## Artifact sâu cần cho ticket này:
##   - heavy-source-analysis.md  (các nơi dùng customer_name)
##   - security-review.md        (PII trong backfill/log)
##   - codex-review.md           (independent review trước merge)
## Cổng người: OI-1 phải giải quyết trước Phase 3; rollback xác minh trước merge.
```

**Stop/Ask**: OI-1 blocking → AI dừng và hỏi. **Bạn** quyết: "Giữ khách riêng theo
mỗi tên unique; trùng tạm chấp nhận."

---

### Phase 2 — Context (`/sdd-context T-077`)

Độ sâu đầy đủ, cộng **heavy source analysis** theo nhu cầu:
```markdown
# heavy-source-analysis.md — T-077  (artifact M4, tạo theo nhu cầu)
## Nơi đọc/ghi customer_name (xác minh qua Grep)
- OrderEntity.customerName            (field JPA)        — đường ghi
- OrderMapper.toResponse              (đọc name)         — AC-4 giữ trả về
- OrderSearchRepository.byCustomer    (LIKE trên name)   — phải chuyển sang join
- ReportJob.exportCustomers           (batch, hằng đêm)  — rủi ro: đọc name hàng loạt
## Vùng rủi ro
- ReportJob chạy hằng đêm → migration không được làm hỏng giữa lúc deploy (expand-contract).
- Tìm theo name dùng index → lên kế hoạch index thay thế trên customers(name).
```
`context.md` ghi pattern cấm: **không bao giờ log `customerName`** (AC-6).

---

### Phase 3 — Plan (`/sdd-plan T-077`)

```markdown
# Impl Plan — T-077  (expand → migrate → contract)
## Phase A (expand, đảo ngược được):
  V12__create_customers.sql        — bảng mới, orders.customer_id nullable
  Deploy app GHI-KÉP name + customer_id
## Phase B (backfill):
  V13__backfill_customers.sql      — chèn name distinct → customers; set orders.customer_id
  Backfill theo lô; KHÔNG log name (AC-6)
## Phase C (contract, ticket sau): drop orders.customer_name khi mọi reader đã chuyển

## Migration / rollback
- Phase A/B đảo ngược được: drop customer_id + customers (dữ liệu còn ở customer_name).
- Script rollback: V13_rollback.sql có tài liệu và test ở staging.
- Điểm không quay lại: Phase C (ticket riêng, duyệt riêng).
```

---

### Phase 4+5 — Implement + review (`/sdd-implement T-077`)

Hiện thực ghi-kép + script Flyway. Rồi **hai review** (độ sâu M4):

```markdown
# self-review.md (Claude)
- [x] Ghi-kép giữ customer_name (AC-4 tương thích ngược)
- [x] Backfill theo lô; không log name (AC-6)
- [ ] WARN: ràng buộc unique(name) sẽ fail trên tên trùng có sẵn → xem test

# codex-review.md (độc lập, M4 theo nhu cầu)
Verdict: NEEDS_FIX
- [Major] V12 thêm UNIQUE(name) nhưng prod có tên trùng → migration sẽ abort.
  Fix: dùng unique chuyển tiếp dạng partial/deferred, hoặc dedupe theo id chứ không theo name.
```

Review độc lập đã bắt được lỗi thật trước khi merge.

---

### Phase 6 — Test (`/sdd-test T-077`) — FAIL → fix

```markdown
# test-results.md — Run 1
FAIL  MigrationTest.backfillPreservesAllOrders
  → V12 UNIQUE(name) vi phạm: 2 row có sẵn tên "John Smith".
  Nguyên nhân: dữ liệu giống prod có tên trùng (khớp Major của codex-review).

# Fix đã áp
- V12: thay UNIQUE(name) bằng UNIQUE(id); cho phép tên trùng trong chuyển tiếp
  (khớp quyết định OI-1: giữ khách riêng theo mỗi row).
- Chạy lại backfill: mỗi order → một customer row riêng.

# test-results.md — Run 2
PASS  MigrationTest.backfillPreservesAllOrders   (0 order mất; map 1:1)
PASS  MigrationTest.rollbackRestoresState
PASS  OrderApiContractTest.customerNameStillReturned   (AC-4)
PASS  BackfillLoggingTest.noPiiInLogs                  (AC-6)
```

> Chu trình FAIL→fix này chính là điểm mấu chốt: độ sâu M4 (review độc lập + test
> migration thật) bắt được hiểm hoạ dữ liệu prod mà happy path sẽ bỏ sót.

---

### Phase 7 — Black-box (`/sdd-blackbox T-077`)

```markdown
### TC-1: Order cũ vẫn đọc được
Input: GET /api/orders/9001 (tạo trước migration)
Expected: customer_name trả như cũ (AC-4); nay cũng liên kết một customer_id.

### TC-2: Diễn tập rollback (staging)
Steps: áp V12+V13, rồi chạy rollback có tài liệu.
Expected: schema + dữ liệu về trạng thái trước migration; không mất order (AC-5).

### TC-3: Soi log backfill
Steps: chạy backfill với debug log bật.
Expected: không dòng log nào chứa chuỗi tên khách (AC-6).
```

---

### Phase 8 — Report (`/sdd-report T-077`)

```markdown
# Final Report — T-077   Status: COMPLETE (giai đoạn expand + backfill)
Đã chuẩn hoá dữ liệu khách qua expand-contract. Ghi-kép giữ API ổn định (AC-4).
Review độc lập + test migration bắt được abort do tên trùng trước khi merge.
Test: Run 1 FAIL (tên trùng) → fix → Run 2 all PASS.

## Accepted risks
- AR-1: giữ orders.customer_name đến ticket contract (T-09x) — có chủ đích.
## Security
- security-review.md: PASS — không PII trong log; scope truy cập không đổi.
## Follow-up
- T-09x: giai đoạn contract (drop customer_name) — ticket + duyệt riêng (điểm không quay lại).
```

---

### Phase 9 — Learnings (`/sdd-learnings T-077`)

```markdown
# Promotion Candidates — T-077
## PC-1 → docs/maintenance/failure-mode-index.md
Failure: giả định một cột là unique khi migration. Dữ liệu prod có tên trùng.
Prevention: không thêm UNIQUE trên dữ liệu text tự do khi chưa có kế hoạch dedupe/chuyển tiếp.
## PC-2 → docs/standards/database.md
Luôn expand → backfill → contract qua các lần deploy riêng; mỗi bước đảo ngược được.
```

---

## Tóm tắt — M4 (Heavy) thêm gì, không bỏ phase nào

| Khía cạnh | M2/M3 | **M4 (ví dụ này)** |
|---|---|---|
| Phase chạy | tất cả | tất cả (độ sâu đầy đủ) |
| Phân tích source | bản đồ chuẩn | + `heavy-source-analysis.md` (call site, rủi ro batch) |
| Review | self (+ codex tuỳ chọn) | self **+ `codex-review.md` độc lập** (bắt được lỗi) |
| Security | inline | + `security-review.md` riêng (PII trong backfill) |
| Migration | thường không | expand→backfill→contract + rollback đã test |
| Test | PASS | **FAIL→fix** trên dữ liệu giống prod, rồi PASS |

Các artifact sâu trên được tạo **theo nhu cầu cho M4** — không scaffold vào mọi
ticket, giữ core nhẹ cho công việc M1/M2.
