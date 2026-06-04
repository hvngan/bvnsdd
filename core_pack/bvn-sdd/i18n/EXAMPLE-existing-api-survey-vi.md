# Hướng dẫn: Thêm field vào API CÓ SẴN với BVN-SDD (Survey mode, M3)

**Bối cảnh**: Bạn tham gia một backend thương mại điện tử có sẵn (Spring Boot) +
frontend web (React). Ticket **T-042** yêu cầu một thay đổi nhỏ nhưng đụng contract:
API chi tiết Order phải trả thêm `statusLabel` (nhãn đọc được) để frontend ngừng
hard-code text trạng thái. Đã CÓ source — nên Phase 0-B chạy ở **Survey mode** (đọc
source thật), và vì đổi FE/BE contract nên mode là **M3**.

> Đây là **ví dụ tài liệu** — minh hoạ artifact cho codebase có sẵn, không phải code
> thật cần chạy. So sánh với `EXAMPLE-ios-weather-vi.md` (greenfield) để thấy Survey
> mode thêm gì.
>
> **Mọi phase đều chạy.** M3 đặt độ sâu (chuẩn + chú trọng contract); không bỏ phase
> nào. Chỉ MX mới dừng.

**Tổng quan dự án**

| | |
|---|---|
| Backend | Java 17, Spring Boot 3, JPA/Hibernate, PostgreSQL |
| Frontend | React 18, TypeScript, React Query |
| Trạng thái | Codebase **có sẵn** (brownfield) |
| Ticket | **T-042** — thêm `statusLabel` vào response `GET /api/orders/{id}` |
| Mode | **M3** (đổi FE/BE contract) |

---

## 0. Thiết lập (trong repo có sẵn)

```bash
cd ecommerce-platform          # monorepo có sẵn của bạn
bvn-sdd init --here --lang vi
# ✓ .claude/ .bvn-sdd/ docs/ đã tạo (file có sẵn không bao giờ bị ghi đè)
```

Mở trong **Claude Code**, rồi chạy `/sdd-phase0a`.

---

## Phase 0-A — Safety Gate (dự án có sẵn)

```
/sdd-phase0a

Project: ecommerce-platform — API Spring Boot + web React có sẵn.
Stack: Java 17 / Spring Boot 3 / JPA / PostgreSQL; React 18 / TS / React Query.
Constraints: có DB production — không chạy migration phá huỷ từ đây.
Secrets: application-prod.yml chứa creds DB — KHÔNG đọc.
```

**AI làm gì**: Glob tìm source → thấy `src/main/java/...`, `web/src/...` → ghi
`project_type = existing`.

**Tạo ra** (trích) `docs/maintenance/phase0/phase0-plan.md`:
```markdown
## Project Type
existing — phát hiện source (backend Spring Boot + frontend React)

## Safety Constraints Recorded
- DENY đọc: application-prod.yml, .env, *.pem
- ASK trước khi: chạy migration Flyway/Liquibase, git push
- Ưu tiên nguồn đúng: source code > docs > suy luận AI
```

`/sdd-phase0a` cũng viết `phase0-decisions.md`, `phase0-execution-log.md`,
`phase0-risk-register.md`, `phase0-review.md`, và 3 policy
`docs/standards/automation/*`. **Bạn** đọc `phase0-review.md` và ký duyệt.

---

## Phase 0-B — Source Intelligence (SURVEY mode)

**Lệnh**: `/sdd-map`

**AI làm gì**: `project_type = existing` → **Survey mode**. Đọc *nông* source thật
(không phải mọi file) và tạo bản đồ với **đường dẫn thật** — không đánh dấu
`[PLANNED]` (ngược với ví dụ iOS greenfield đánh dấu mọi thứ `[PLANNED]`).

**Tạo ra** `docs/architecture/system-map.md` (trích):
```markdown
# System Map — ecommerce-platform   (Survey mode — quan sát từ source)

## Components
| Component | Trách nhiệm | Vị trí chính |
|---|---|---|
| Order API | order CRUD + status | src/main/java/com/shop/order/ |
| Order domain | Order, OrderStatus enum | src/main/java/com/shop/order/domain/ |
| Web order page | UI chi tiết order | web/src/features/orders/ |

## Cách kết nối
React Query → GET /api/orders/{id} → OrderController → OrderService → OrderRepository → PostgreSQL
```

**Tạo ra** (đều thật, không phải planned):
- `source-inventory.md` — file chính & mục đích
- `route-api-map.md` — `GET /api/orders/{id}`, `OrderController#getOrder`
- `repository-db-map.md` — bảng `orders`, enum `OrderStatus` giá trị `1/2/3/4`
- `fe-be-contract-map.md` — shape `OrderResponse` hiện tại mà web đang dùng
- `test-map.md` — `OrderControllerTest`, `OrderServiceTest`, web `orderApi.test.ts`

**Bạn**: lướt các bản đồ; chúng thành kim chỉ nam điều hướng cho mọi ticket.

---

## T-042: thêm `statusLabel` vào response Order

### Bootstrap — `/sdd-new T-042 Order statusLabel`

Tạo `docs/changes/T-042/` với 20 artifact trống.

---

### Phase 1 — Spec Pack (`/sdd-spec T-042`)

```
/sdd-spec T-042

Yêu cầu: GET /api/orders/{id} phải trả thêm `statusLabel` — nhãn đọc được cho
`status` dạng số đang có (1=Pending, 2=Paid, 3=Shipped, 4=Cancelled). Trang order web
hiển thị statusLabel thay vì tự map số. Nhãn tiếng Anh tạm thời; i18n ngoài phạm vi.
```

**AI đọc trước**: `docs/architecture/*` (bản đồ survey), rồi `OrderController`,
`OrderResponse`, `OrderStatus` thật. **Tạo ra** `spec-pack.md` (trích):
```markdown
## 6. Acceptance Criteria
- [ ] AC-1: Response GET /api/orders/{id} có thêm field string `statusLabel`.
- [ ] AC-2: statusLabel map status 1→"Pending", 2→"Paid", 3→"Shipped", 4→"Cancelled".
- [ ] AC-3: `status` (số) giữ nguyên — chỉ thêm, tương thích ngược.
- [ ] AC-4: Trang order web hiện statusLabel; bỏ map số→text cục bộ.
- [ ] AC-5: Giá trị status lạ → statusLabel = "Unknown" (không 500).

## 9. Client/Service contract (trung lập nền tảng)
OrderResponse thêm: statusLabel: string (non-null). Field `status` giữ nguyên.
Tương thích ngược: consumer cũ bỏ qua field mới vẫn chạy.
```

`source-availability.md` → GREEN (đọc được mọi source liên quan). `open-issues.md`
ghi OI-1: "Xác nhận từ ngữ nhãn với product (Paid hay Completed?)".

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-042`)

```markdown
# Mode Decision — T-042
## Scoring: Reversibility 1 | Uncertainty 1 | Risk 2 | Scope 2  → M3
## Quyết định: M3 (Plus) — đụng FE/BE contract, nên parity contract quan trọng.
## Độ sâu mỗi phase: mọi phase chạy ở độ sâu chuẩn; chú trọng thêm §9 contract.
## Artifact sâu theo nhu cầu: fe-be-contract-map.md (cấp ticket).
```

> Dù thay đổi nhỏ, nó vượt ranh giới FE/BE → M3, không phải M1. Mọi phase vẫn chạy.

---

### Phase 2 — Context (`/sdd-context T-042`)

EXISTING PROJECT MODE — AI xác minh với source thật bằng Grep/Read.

```markdown
# Context — T-042
## Ví dụ đúng trong codebase
- src/main/java/com/shop/order/OrderResponse.java — DTO là Java record; thêm field ở đây.
- web/src/features/orders/orderApi.ts — hook React Query; type phản chiếu DTO.

## Method / class thực sự tồn tại (đã xác minh)
- enum OrderStatus: PENDING(1), PAID(2), SHIPPED(3), CANCELLED(4)  ← xác nhận qua Grep
- OrderMapper.toResponse(Order) — nơi DUY NHẤT dựng DTO; sửa ở đây.

## Cấm
- KHÔNG thêm logic nhãn trong component React (AC-4 bỏ map FE).
- KHÔNG đổi serialization của `status` dạng số (AC-3).
```

`source-map.md` liệt kê file thật cần đụng: `OrderResponse.java`, `OrderMapper.java`,
`orderApi.ts`, `OrderStatusBadge.tsx` + test của chúng.

---

### Phase 3 — Plan (`/sdd-plan T-042`)

```markdown
# Impact Analysis — T-042
| Area | Affected? | Chi tiết |
| Shared contract | Yes | OrderResponse +statusLabel (chỉ thêm, tương thích ngược) |
| BE / API | Yes | OrderMapper map enum→nhãn |
| Web FE | Yes | dùng statusLabel; xoá map cục bộ trong OrderStatusBadge.tsx |
| DB | No | không đổi schema — suy ra từ status có sẵn |
| Test | Yes | test mapper BE, contract test, test component web |

# Impl Plan — T-042
## BE: thêm statusLabel vào OrderResponse; OrderMapper switch OrderStatus → nhãn; mặc định "Unknown".
## FE: orderApi.ts type +statusLabel; OrderStatusBadge.tsx render statusLabel, bỏ numberToText().
## fe-be-contract-map.md: ghi field, type, nullability, 4 dòng enum→nhãn + Unknown.
```

---

### Phase 4+5 — Implement (`/sdd-implement T-042`)

```java
// OrderResponse.java — field thêm vào (status giữ nguyên → AC-3)
public record OrderResponse(Long id, int status, String statusLabel, /* ... */) {}

// OrderMapper.java
static String label(OrderStatus s) {
    return switch (s) {
        case PENDING -> "Pending";
        case PAID -> "Paid";
        case SHIPPED -> "Shipped";
        case CANCELLED -> "Cancelled";
    }; // enum đầy đủ; "Unknown" phòng vệ xử lý nơi parse status (AC-5)
}
```
```tsx
// OrderStatusBadge.tsx — giờ tin nhãn từ server (AC-4)
export function OrderStatusBadge({ statusLabel }: { statusLabel: string }) {
  return <span className="badge">{statusLabel}</span>;
}
```

`self-review.md` kiểm: status giữ nguyên (AC-3 ✓), bỏ map FE (AC-4 ✓), nhánh Unknown
(AC-5 ✓). **Bạn** điền `human-review.md`.

---

### Phase 6 — Test (`/sdd-test T-042`)

```markdown
# Test Plan — T-042
| AC | Loại test | Tên test | Ưu tiên |
| AC-2 | BE unit | OrderMapperTest.labelsEachStatus | H |
| AC-3 | contract | OrderResponseContractTest.statusStillNumeric | H |
| AC-5 | BE unit | OrderMapperTest.unknownStatusLabel | M |
| AC-4 | web unit | OrderStatusBadge.test.tsx.rendersServerLabel | H |

## Run commands
./gradlew test
cd web && npm test
```
`test-results.md`: 4 PASS. Contract test tương thích ngược xác nhận consumer cũ không
bị ảnh hưởng.

---

### Phase 7 — Black-box (`/sdd-blackbox T-042`)

```markdown
### TC-1: Order Paid hiện nhãn
Input: GET /api/orders/1001  (status=2 trong DB)
Expected: response.statusLabel == "Paid"; response.status == 2 vẫn còn.

### TC-2: Tương thích ngược
Input: client cũ bỏ qua field lạ gọi GET /api/orders/1001
Expected: vẫn parse được; `status` số giữ nguyên.

### TC-3: Trang web
Input: mở /orders/1001
Expected: badge hiện "Paid" lấy từ API (không map phía client).
```

---

### Phase 8 — Report (`/sdd-report T-042`)

```markdown
# Final Report — T-042   Status: COMPLETE
Đã ship `statusLabel` (chỉ thêm); `status` số giữ nguyên (tương thích ngược).
BE 3 file, FE 2 file. Test 4/4 PASS gồm cả contract tương thích ngược.
Accepted risk: không. Open issue OI-1 (từ ngữ) đã chốt với product: giữ "Paid".
```

---

### Phase 9 — Learnings (`/sdd-learnings T-042`)

```markdown
# Promotion Candidates — T-042
## PC-1 → docs/standards/api-contract.md
Server sở hữu nhãn đọc được; client không được tự map enum→text cục bộ.
## PC-2 → docs/maintenance/pattern-library.md
Pattern thêm-field: mở rộng DTO + giữ field cũ → mặc định tương thích ngược.
```

Sau T-042, chạy lại `/sdd-map` nếu các bản đồ contract cần làm mới.

---

## Tóm tắt — Survey mode thêm gì so với greenfield

| | Greenfield (ví dụ iOS) | Survey mode (ví dụ này) |
|---|---|---|
| Bản đồ source Phase 0-B | quyết định `[PLANNED]` | **Đường dẫn thật**, quan sát từ source |
| Context Phase 2 | thiết kế API dự kiến | **xác minh** method/enum thật qua Grep |
| Trọng tâm rủi ro | thiết lập kiến trúc | **tương thích ngược** của contract có sẵn |
| Phase chạy | tất cả | tất cả (M3 — độ sâu, không bỏ) |
