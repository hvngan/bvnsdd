# Ví dụ: Xây dựng WeatherNow (iOS) từ đầu

**Kịch bản**: Bạn xây dựng ứng dụng thời tiết iOS *WeatherNow* hoàn toàn mới — chưa có codebase.

| | |
|---|---|
| Nền tảng | iOS 17+, Swift 5.9, SwiftUI |
| Trạng thái | Greenfield — chưa có code nào |
| Ticket | **T-001** — Màn hình thời tiết hiện tại |

So sánh với `EXAMPLE-cross-platform-weather-vi.md` để thấy sự khác biệt khi codebase đã có sẵn.

---

## 0. Thiết lập

```bash
bvn-sdd check
git clone git@github.com:my-org/weathernow-ios.git
cd weathernow-ios
bvn-sdd init --here --lang vi
```

Mở project trong **Claude Code**.

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**Chạy** — mô tả project ngay bên dưới lệnh (bắt buộc vì chưa có source):
```
/sdd-phase0a

Dự án: WeatherNow — ứng dụng xem thời tiết iOS mới hoàn toàn, chưa có code.
Nền tảng: iOS 17+, SwiftUI, MVVM + Clean Architecture, Swift Package Manager.
API bên ngoài: OpenWeatherMap (REST, xác thực bằng API key).
Offline: cache dữ liệu cuối, hiện banner "Cập nhật lần cuối X phút trước".
```

**Bạn cần làm:**
- Đọc `docs/maintenance/phase0/phase0-plan.md`
- Trả lời câu hỏi mở AI đặt ra (cấu trúc module, thời gian cache stale, v.v.)

---

## Phase 0-B — Source Intelligence — Green-field mode (`/sdd-map`)

**Chạy:**
```
/sdd-map
```

**Bạn cần làm:**
- Đọc `docs/architecture/system-map.md` — đây là **quyết định kiến trúc**, tất cả đánh dấu `[PLANNED]`
- Điều chỉnh cấu trúc module nếu cần — file này là bản thiết kế cho mọi ticket tiếp theo
- Duyệt xong mới bắt đầu ticket đầu tiên

---

## Bootstrap (`/sdd-new T-001`)

**Chạy:**
```
/sdd-new T-001 Màn hình thời tiết hiện tại
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
- Trả lời tất cả mục trong `open-issues.md` trước khi chạy bước tiếp

---

## Phase 1 — Right-sizing (`/sdd-rightsize T-001`)

**Chạy:**
```
/sdd-rightsize T-001
```

**Bạn cần làm:**
- Đọc `mode-decision.md`, xác nhận mode (M1–M5)
- Ticket đầu của dự án greenfield thường là M2–M3 vì nhiều tầng được tạo cùng lúc

---

## Phase 2 — Context (`/sdd-context T-001`)

**Chạy:**
```
/sdd-context T-001
```

**Bạn cần làm:**
- Xác nhận convention và pattern được thiết kế (đánh dấu `[PLANNED]` — chưa có code thực)
- Kiểm tra `source-map.md` liệt kê file cần **tạo mới**, không phải file cần sửa

---

## Phase 3 — Impact & Plan (`/sdd-plan T-001`)

**Chạy:**
```
/sdd-plan T-001
```

**Bạn cần làm:**
- Đọc thứ tự implement trong `impl-plan.md` (phụ thuộc đúng chưa?)
- Ghi nhận bước thủ công AI không làm được (ví dụ: thêm key vào Info.plist trong Xcode)
- **Duyệt rõ ràng** — AI không viết code trước khi bạn xác nhận

---

## Phase 4+5 — Implement (`/sdd-implement T-001`)

**Chạy:**
```
/sdd-implement T-001
```

**Bạn cần làm:**
- Duyệt review checklist trước khi AI bắt đầu code (AI sẽ dừng chờ)
- Thực hiện các bước thủ công song song (ví dụ: thêm chuỗi Info.plist trong Xcode)
- Đọc toàn bộ code AI đã viết (diff)
- Điền `human-review.md` — AI không điền file này

---

## Phase 6 — Test (`/sdd-test T-001`)

**Chạy:**
```
/sdd-test T-001
```

**Bạn cần làm:**
- Chạy test: `xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,...'`
- Xác nhận tất cả PASS trước khi tiếp tục

---

## Phase 7 — Black-box Test (`/sdd-blackbox T-001`)

**Chạy:**
```
/sdd-blackbox T-001
```

**Bạn cần làm:**
- Test thủ công từng case trong `blackbox-testcases.md` trên iOS Simulator hoặc thiết bị thật
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

## Sau T-001: cập nhật kiến trúc

**Chạy lại `/sdd-map`** để thay thế `[PLANNED]` bằng đường dẫn source thực tế:
```
/sdd-map
```

Từ T-002 trở đi, Phase 2 sẽ tìm thấy pattern thực trong source để tham chiếu thay vì phải thiết kế từ đầu.
