# BVN-SDD — Hướng dẫn nhanh (1 trang)
# Brycen Viet Nam — Spec-Driven Development

> Bạn **chạy lệnh**, không cần đọc hết tài liệu. Mỗi lệnh tương ứng một phase
> trong SDD-Installation Pack V04.2 và tạo ra file artifact cụ thể trong
> `docs/changes/<MÃ-TICKET>/`.

## 1. Cài đặt (làm 1 lần)

```bash
bvn-sdd check            # kiểm tra đã có git + Claude Code chưa
bvn-sdd init du-an       # tạo khung dự án (hoặc: bvn-sdd init --here)
```

Chọn ngôn ngữ khi được hỏi: 1=Tiếng Việt / 2=English / 3=日本語

Sau đó **mở dự án trong Claude Code** và chạy `/sdd-phase0a` ngay lập tức.

## 2. Bạn đang ở kịch bản nào?

| Bước | Codebase có sẵn | Repo trống / dự án mới |
|---|---|---|
| Cài đặt | `bvn-sdd init --here` vào repo hiện có | `git clone <empty-repo>`, rồi `bvn-sdd init --here` |
| Phase 0-A | Audit config + nhận diện tech stack; ghi `project_type = existing` | Audit config; phát hiện không có source; ghi `project_type = new` |
| Phase 0-B | **Survey mode** — đọc source, tạo `system-map.md`, `source-inventory.md`, route/DB map | **Green-field mode** — tạo `system-map.md` là tài liệu quyết định kiến trúc; tất cả đánh dấu `[PLANNED]`; chưa có source-inventory hay test-map |
| Phase 2 (`/sdd-context`) | Xác minh API/pattern tồn tại trong source | Thiết kế API/pattern dự kiến; đánh dấu `[PLANNED]`; `source-map.md` liệt kê file cần **tạo** |
| Phase 3–9 | Lên kế hoạch và implement dựa trên code hiện có | Lên kế hoạch và implement code mới từ đầu |
| Sau các ticket đầu | Chạy lại `/sdd-map` nếu cần cập nhật | **Chạy lại `/sdd-map`** để thay `[PLANNED]` bằng source map thực tế |

Cả hai kịch bản dùng cùng tập lệnh — command tự phát hiện chế độ từ `phase0-plan.md`
(được thiết lập bởi `/sdd-phase0a`).

## 3. Phase theo SDD-Installation Pack V04.2

| Phase (V04.2) | Lệnh Claude Code | Tạo ra gì | Bạn làm gì |
|---|---|---|---|
| **Phase 0-A** Safety Gate | `/sdd-phase0a` | `docs/maintenance/phase0/` + `docs/standards/automation/` — bằng chứng an toàn, chính sách context | **1 lần/dự án.** Chạy ngay sau `bvn-sdd init`, trước `/sdd-map` |
| **Phase 0-B** Common Base / Source Intelligence | `/sdd-map` | `docs/architecture/` — bản đồ source, route, API, DB, FE/BE contract, test coverage | **1 lần/dự án.** Chạy trước ticket đầu tiên |
| **Bootstrap** (trước Phase 1) | `/sdd-new T-001` | `docs/changes/T-001/` + tất cả file trống | Đặt mã ticket |
| **Phase 1** Investigation / Spec Pack | `/sdd-spec T-001` | `spec-pack.md`, `source-availability.md`, `open-issues.md` | Kiểm tra AC đúng chưa; trả lời Open Issues |
| **Phase 1** Right-sizing | `/sdd-rightsize T-001` | `mode-decision.md` — chế độ M1–M5/MX + workflow được điều chỉnh | **Quan trọng:** xác nhận chế độ trước khi tiếp tục |
| **Phase 2** Ticket Context / Rules | `/sdd-context T-001` | `context.md`, `source-map.md`, `ticket-rules.md` | Xác nhận pattern, method thực tồn tại, điều cấm _(M1: làm gọn, không bỏ)_ |
| **Phase 3** Impact Analysis / Impl Plan | `/sdd-plan T-001` | `impact-analysis.md`, `impl-plan.md` | Duyệt phạm vi ảnh hưởng FE/BE/DB và kế hoạch _(M1: làm gọn, không bỏ)_ |
| **Phase 4+5** Review Checklist + Implementation / AI Review / Human Review | `/sdd-implement T-001` | code + `review-checklist.md`, `self-review.md` | Đọc code AI viết; kiểm tra self-review; **điền `human-review.md`** rồi duyệt |
| **Phase 6** Test Plan / Test Code | `/sdd-test T-001` | `test-plan.md`, `test-results.md` | Xem test có PASS thật không; đọc kết quả |
| **Phase 7** Black-box Test / Test Data | `/sdd-blackbox T-001` | `blackbox-testcases.md`, `test-data.md`, `blackbox-review-checklist.md` | Xác minh hành vi từ góc nhìn user/QA _(M1: vài case chính, không bỏ)_ |
| **Phase 8** Test Results / Final Report | `/sdd-report T-001` | `report.md` | Đọc báo cáo cuối; xác nhận accepted risk và follow-up |
| **Phase 9** Living Docs / Failure Mode Update | `/sdd-learnings T-001` | `promotion-candidates.md` + cập nhật `docs/maintenance/failure-mode-index.md` | Duyệt promotion candidates; xác nhận những gì được đưa vào chuẩn dự án |

**Lệnh tiện ích** (Spec 32 — Long Context / Strategic Compact):
- `/sdd-compact T-001` → `strategic-compact.md` — snapshot trạng thái session. Dán vào đầu session mới để tiếp tục mà không cần đọc lại tất cả.

## 4. Chế độ (do `/sdd-rightsize` quyết định)

> **Chế độ đặt ĐỘ SÂU của mỗi phase, KHÔNG bỏ phase.** Mọi ticket — đơn hay đa nền
> tảng — chạy đủ toàn bộ chuỗi phase; M1 chỉ viết gọn artifact. Chỉ **MX** mới dừng.

| Chế độ | Tên | Khi nào dùng | Độ sâu ở chế độ này |
|---|---|---|---|
| **M1** | Light | Sửa text, config, bug nhỏ < 3 file | Đủ phase nhưng artifact gọn (nếu không có gì riêng, ghi 1 dòng); chỉ self-review |
| **M2** | Standard | Feature thông thường, 1 service | Độ sâu chuẩn cho mọi artifact |
| **M3** | Plus | Đụng FE+BE contract, 10–30 file | Chuẩn + chú trọng FE/BE contract; thêm artifact sâu theo nhu cầu (contract-map, codex-review) |
| **M4** | Heavy | Thay đổi kiến trúc, DB migration | Đầy đủ + heavy-source-analysis, security-review, rollback/migration plan, independent review |
| **M5** | Critical | Vá lỗi bảo mật, sự cố production | Sâu nhất + cổng người bắt buộc (threat model, bằng chứng test, audit); escalate cho người phụ trách |
| **MX** | Stop | Yêu cầu chưa rõ hoặc rủi ro quá cao | Dừng — giải quyết open issues trước. Chế độ duy nhất dừng việc |

## 5. 5 nguyên tắc bắt buộc

1. **Plan trước, code sau.** AI luôn trình kế hoạch trước; bạn duyệt rồi mới cho làm.
2. **`spec-pack.md` là nguồn đúng duy nhất.** Điều chưa rõ → `open-issues.md`. Đừng đoán.
3. **Code thật thắng tài liệu.** Khi Excel/PDF mâu thuẫn với source code, tin source code.
4. **Không đụng secret.** Không đọc/in `.env`, key, token, PII.
5. **Người phán định cuối cùng là bạn.** AI self-review xong, bạn vẫn phải đọc và approve.

## 6. Khi nào DỪNG và báo người phụ trách

- Source thiếu hoặc không đọc được để implement đúng
- Lộ secret hoặc dữ liệu cá nhân
- Thay đổi đụng: thanh toán, đăng nhập/phân quyền, migration DB production
- Source và specification mâu thuẫn nhau
- AI định dùng method hoặc file không tồn tại

## 7. Mẹo

- Mọi kết quả trong `docs/changes/<MÃ-TICKET>/` — mở xem bất cứ lúc nào.
- Cuối mỗi lệnh AI nhắc bạn lệnh tiếp theo cần chạy.
- Quy tắc chi tiết: `.claude/rules/`. Chuẩn dự án: `docs/standards/`.

## 8. Ví dụ Walkthrough

Xem **[EXAMPLE-cross-platform-weather-vi.md](EXAMPLE-cross-platform-weather-vi.md)** để có walkthrough đầy đủ về việc thêm tính năng vào app WeatherNow đang chạy trên **cả Android và iOS có sẵn** theo BVN-SDD.

Mỗi phase đều hiển thị:
- Lệnh chính xác bạn chạy
- Nội dung artifact quan trọng AI tạo ra (trích đoạn thực tế)
- Quyết định hoặc xác nhận bạn cần đưa ra trước khi sang phase tiếp theo

Bao gồm toàn bộ luồng codebase có sẵn: Phase 0-A → Phase 0-B (Survey Mode, `platform-android-map.md` + `platform-ios-map.md`) → Bootstrap T-001 → Spec → Rightsize → Context (xác minh thực tế, không có [PLANNED]) → Plan → Implement → Test → Black-box → Report → Learnings.

Walkthrough đơn nền tảng (greenfield, để so sánh):
- **[EXAMPLE-ios-weather-vi.md](EXAMPLE-ios-weather-vi.md)** — iOS duy nhất, xây dựng từ đầu (M2). So sánh khi không có codebase sẵn.
