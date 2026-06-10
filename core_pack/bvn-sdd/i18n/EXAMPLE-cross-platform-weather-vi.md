# Ví dụ: Thêm màn hình dự báo vào WeatherNow (Android + iOS có sẵn)

**Kịch bản**: *WeatherNow* đã có trên cả Android và iOS với màn hình thời tiết hiện tại đang hoạt động.
Bạn thêm **màn hình dự báo 5 ngày** (T-001) theo BVN-SDD.

| | |
|---|---|
| Nền tảng | Android (Kotlin, Compose, Hilt) **+** iOS (Swift, SwiftUI, async/await) |
| Trạng thái | Codebase có sẵn — màn hình thời tiết hiện tại đã hoạt động |
| Repo | monorepo: `android/` + `ios/` + `docs/` |

So sánh với `EXAMPLE-ios-weather-vi.md` để thấy sự khác biệt khi chưa có codebase.

---

## 0. Thiết lập

```bash
bvn-sdd init --here --lang vi
```

Sửa `.bvn-sdd/config.yml` để khai báo hai nền tảng:

```yaml
platforms:
  - android
  - ios
platform_stack:
  android: "Kotlin, Jetpack Compose, Hilt, StateFlow"
  ios: "Swift, SwiftUI, @Observable, async/await"
```

Mở project trong **Claude Code**.

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**Chạy:**
```
/sdd-phase0a
```
Không cần argument — command tự đọc cấu trúc project và `config.yml`.

**Bạn cần làm:**
- Đọc `docs/maintenance/phase0/phase0-review.md`
- Ký nhận (tick) các mục còn chờ xác nhận

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

**Chạy:**
```
/sdd-map
```

**Bạn cần làm:**
- Đọc `docs/architecture/system-map.md` — kiểm tra §Parity Status (cả hai nền tảng có baseline ngang nhau không?)
- Đọc `docs/architecture/platform-android-map.md` và `platform-ios-map.md`
- Điều chỉnh nếu AI hiểu sai cấu trúc, rồi tiến hành tạo ticket

---

## Bootstrap (`/sdd-new T-001`)

**Chạy:**
```
/sdd-new T-001 Màn hình dự báo 5 ngày
```

---

## Phase 1 — Spec Pack (`/sdd-spec T-001`)

**Chạy** — dán yêu cầu gốc ngay bên dưới lệnh:
```
/sdd-spec T-001

[Dán yêu cầu từ Jira / email / brief vào đây]
```
Đây là phase duy nhất bạn cần cung cấp input thủ công.

**Bạn cần làm:**
- Kiểm tra AC đúng và đủ chưa
- Đảm bảo spec trung lập nền tảng (WHAT, không phải HOW)
- Trả lời tất cả mục trong `open-issues.md` trước khi chạy bước tiếp

---

## Phase 1 — Right-sizing (`/sdd-rightsize T-001`)

**Chạy:**
```
/sdd-rightsize T-001
```

**Bạn cần làm:**
- Đọc `mode-decision.md`, xác nhận mode (M1–M5)
- Lưu ý: mode đặt **độ sâu** của mỗi phase, không bỏ phase nào

---

## Phase 2 — Context (`/sdd-context T-001`)

**Chạy:**
```
/sdd-context T-001
```

**Bạn cần làm:**
- Xác nhận pattern và method thực sự tồn tại trong codebase
- Kiểm tra parity gap — nếu một nền tảng chưa có feature cần thiết, giải quyết trước khi tiếp tục

---

## Phase 3 — Impact & Plan (`/sdd-plan T-001`)

**Chạy:**
```
/sdd-plan T-001
```

**Bạn cần làm:**
- Đọc `impact-analysis.md` và `impl-plan.md`
- Kiểm tra bảng parity cross-platform (Android vs iOS có cùng hành vi không?)
- **Duyệt rõ ràng** — AI không viết code trước khi bạn xác nhận

---

## Phase 4+5 — Implement (`/sdd-implement T-001`)

**Chạy:**
```
/sdd-implement T-001
```

**Bạn cần làm:**
- Duyệt review checklist trước khi AI bắt đầu code (AI sẽ dừng chờ)
- Đọc toàn bộ code AI đã viết (diff)
- Điền `human-review.md` — AI không điền file này

---

## Phase 6 — Test (`/sdd-test T-001`)

**Chạy:**
```
/sdd-test T-001
```

**Bạn cần làm:**
- Chạy test thực tế trên cả hai nền tảng và xác nhận PASS
- Android: `./gradlew :app:testDebugUnitTest`
- iOS: `xcodebuild test -scheme WeatherNow -destination '...'`

---

## Phase 7 — Black-box Test (`/sdd-blackbox T-001`)

**Chạy:**
```
/sdd-blackbox T-001
```

**Bạn cần làm:**
- Test thủ công từng case trong `blackbox-testcases.md` trên **cả hai nền tảng**
- Đánh dấu Pass / Fail từng case
- Điền fixture cần thiết vào `test-data.md`

---

## Phase 8 — Final Report (`/sdd-report T-001`)

**Chạy:**
```
/sdd-report T-001
```

**Bạn cần làm:**
- Đọc `report.md`, xác nhận accepted risks và ticket follow-up

---

## Phase 9 — Learnings (`/sdd-learnings T-001`)

**Chạy:**
```
/sdd-learnings T-001
```

**Bạn cần làm:**
- Đọc `promotion-candidates.md`
- Xác nhận pattern nào vào `docs/standards/`, failure mode nào vào `failure-mode-index.md`

---

## Điểm khác biệt so với greenfield

| Codebase có sẵn (ví dụ này) | Greenfield |
|---|---|
| Phase 0-A: không cần mô tả project — AI tự đọc | Phase 0-A: phải mô tả project trong message |
| Phase 0-B: Survey mode — đọc source thực | Phase 0-B: Green-field mode — tất cả `[PLANNED]` |
| context.md: xác minh pattern đã tồn tại | context.md: thiết kế pattern mới, đánh dấu `[PLANNED]` |
| source-map.md: file cần sửa + file mới | source-map.md: file cần tạo mới |
| Parity check: verify baseline cả hai nền tảng | Không có parity debt ngay từ đầu |
| Sau ticket đầu: không cần chạy lại `/sdd-map` | Sau ticket đầu: **chạy lại `/sdd-map`** để thay `[PLANNED]` |
