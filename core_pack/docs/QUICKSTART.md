# BVN-SDD — Hướng dẫn nhanh (1 trang)

> Bạn **chạy lệnh**, không cần đọc hết tài liệu. Mỗi lệnh tạo ra 1 file kết quả
> trong `docs/changes/<MÃ-TICKET>/`.

## 1. Cài đặt (làm 1 lần)

```bash
bvn-sdd check            # kiểm tra đã có git + Claude Code chưa
bvn-sdd init du-an-cua-toi   # tạo khung dự án mới (hoặc: bvn-sdd init --here)
```

Sau đó **mở dự án trong Claude Code**.

## 2. Quy trình 7 bước cho mỗi công việc

| Bước | Gõ lệnh trong Claude Code | Tạo ra gì | Bạn làm gì |
|---|---|---|---|
| 0 | `/sdd-map` | bản đồ source (`docs/architecture/`) | **Chỉ 1 lần/dự án.** Để AI hiểu code |
| 1 | `/sdd-new T-001` | thư mục ticket + các file trống | Đặt mã ticket (vd `T-001`) |
| 2 | `/sdd-spec T-001` | `spec-pack.md` (đặc tả) | Kiểm tra AC đúng chưa, trả lời Open Issues |
| 3 | `/sdd-context T-001` | `context.md`, `source-map.md` | Xác nhận pattern/API đúng |
| 4 | `/sdd-plan T-001` | `impact-analysis.md`, `impl-plan.md` | Duyệt phạm vi ảnh hưởng & kế hoạch |
| 5 | `/sdd-implement T-001` | code + `self-review.md` | Đọc code AI viết, duyệt |
| 6 | `/sdd-test T-001` | `test-plan.md`, `test-results.md` | Xem test có PASS thật không |
| 7 | `/sdd-report T-001` | `report.md` | Đọc báo cáo cuối, chốt |

> Việc nhỏ (sửa text, thêm log)? Có thể bỏ qua bước 3 và làm gọn. Việc đụng tới
> DB / thanh toán / quyền / PII? Làm đủ các bước và **báo người phụ trách**.

## 3. 5 nguyên tắc bắt buộc

1. **Plan trước, code sau.** AI luôn trình kế hoạch trước; bạn duyệt rồi mới cho làm.
2. **`spec-pack.md` là chuẩn duy nhất.** Không tự thêm yêu cầu ngoài nó. Điều chưa
   rõ → ghi vào `open-issues.md`, **đừng đoán**.
3. **Code thật thắng tài liệu.** Khi tài liệu (Excel/PDF) mâu thuẫn với source, tin source.
4. **Không đụng secret.** Không đọc/in `.env`, key, token, mật khẩu, dữ liệu cá nhân (PII).
5. **Người duyệt cuối là bạn.** AI tự review xong, bạn vẫn phải đọc và phê duyệt.

## 4. Khi nào DỪNG và hỏi người phụ trách

- Thiếu source / thiếu định nghĩa DB để làm đúng
- Lộ secret hoặc dữ liệu cá nhân
- Thay đổi đụng: thanh toán, đăng nhập/phân quyền, migration DB production

## 5. Mẹo

- Mọi kết quả nằm trong `docs/changes/<MÃ-TICKET>/` — mở ra xem bất cứ lúc nào.
- Quên bước tiếp theo? Cuối mỗi lệnh AI luôn nhắc bạn gõ lệnh kế tiếp.
- Quy tắc chi tiết: `.claude/rules/`. Chuẩn dự án: `docs/standards/`.
