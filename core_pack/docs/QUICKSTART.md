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

Sau đó **mở dự án trong Claude Code**.

## 2. Phase theo SDD-Installation Pack V04.2

| Phase (V04.2) | Lệnh Claude Code | Tạo ra gì | Bạn làm gì |
|---|---|---|---|
| **Phase 0-B** Common Base / Source Intelligence | `/sdd-map` | `docs/architecture/` — bản đồ source, route, API, DB | **1 lần/dự án.** Chạy trước ticket đầu tiên |
| **Bootstrap** (trước Phase 1) | `/sdd-new T-001` | `docs/changes/T-001/` + tất cả file trống | Đặt mã ticket |
| **Phase 1** Investigation / Spec Pack | `/sdd-spec T-001` | `spec-pack.md`, `source-availability.md`, `open-issues.md` | Kiểm tra AC đúng chưa; trả lời Open Issues |
| **Phase 1** Right-sizing | `/sdd-rightsize T-001` | `mode-decision.md` — chế độ M1–M5/MX + workflow được điều chỉnh | **Quan trọng:** xác nhận chế độ trước khi tiếp tục |
| **Phase 2** Ticket Context / Rules | `/sdd-context T-001` | `context.md`, `source-map.md` | Xác nhận pattern, method thực tồn tại, điều cấm _(bỏ qua nếu M1)_ |
| **Phase 3** Impact Analysis / Impl Plan | `/sdd-plan T-001` | `impact-analysis.md`, `impl-plan.md` | Duyệt phạm vi ảnh hưởng FE/BE/DB và kế hoạch _(bỏ qua nếu M1)_ |
| **Phase 4+5** Review Checklist + Implementation / AI Review / Human Review | `/sdd-implement T-001` | code + `review-checklist.md`, `self-review.md` | Đọc code AI viết; kiểm tra self-review; duyệt |
| **Phase 6** Test Plan / Test Code | `/sdd-test T-001` | `test-plan.md`, `test-results.md` | Xem test có PASS thật không; đọc kết quả |
| **Phase 7** Black-box Test / Test Data | `/sdd-blackbox T-001` | `blackbox-testcases.md` | Xác minh hành vi từ góc nhìn user/QA _(bỏ qua nếu M1)_ |
| **Phase 8** Test Results / Final Report | `/sdd-report T-001` | `report.md` | Đọc báo cáo cuối; xác nhận accepted risk và follow-up |

**Lệnh tiện ích** (Spec 32 — Long Context / Strategic Compact):
- `/sdd-compact T-001` → `strategic-compact.md` — snapshot trạng thái session. Dán vào đầu session mới để tiếp tục mà không cần đọc lại tất cả.

## 3. Chế độ (do `/sdd-rightsize` quyết định)

| Chế độ | Tên | Khi nào dùng | Lệnh bỏ qua |
|---|---|---|---|
| **M1** | Light | Sửa text, config, bug nhỏ < 3 file | context, plan, blackbox |
| **M2** | Standard | Feature thông thường, 1 service | Không bỏ |
| **M3** | Plus | Đụng FE+BE contract, 10–30 file | Không bỏ |
| **M4** | Heavy | Thay đổi kiến trúc, DB migration | Không bỏ + security review |
| **M5** | Critical | Vá lỗi bảo mật, sự cố production | Escalate ngay cho người phụ trách |
| **MX** | Stop | Yêu cầu chưa rõ hoặc rủi ro quá cao | Dừng, giải quyết open issues trước |

## 4. 5 nguyên tắc bắt buộc

1. **Plan trước, code sau.** AI luôn trình kế hoạch trước; bạn duyệt rồi mới cho làm.
2. **`spec-pack.md` là nguồn đúng duy nhất.** Điều chưa rõ → `open-issues.md`. Đừng đoán.
3. **Code thật thắng tài liệu.** Khi Excel/PDF mâu thuẫn với source code, tin source code.
4. **Không đụng secret.** Không đọc/in `.env`, key, token, PII.
5. **Người phán định cuối cùng là bạn.** AI self-review xong, bạn vẫn phải đọc và approve.

## 5. Khi nào DỪNG và báo người phụ trách

- Source thiếu hoặc không đọc được để implement đúng
- Lộ secret hoặc dữ liệu cá nhân
- Thay đổi đụng: thanh toán, đăng nhập/phân quyền, migration DB production
- Source và specification mâu thuẫn nhau
- AI định dùng method hoặc file không tồn tại

## 6. Mẹo

- Mọi kết quả trong `docs/changes/<MÃ-TICKET>/` — mở xem bất cứ lúc nào.
- Cuối mỗi lệnh AI nhắc bạn lệnh tiếp theo cần chạy.
- Quy tắc chi tiết: `.claude/rules/`. Chuẩn dự án: `docs/standards/`.
