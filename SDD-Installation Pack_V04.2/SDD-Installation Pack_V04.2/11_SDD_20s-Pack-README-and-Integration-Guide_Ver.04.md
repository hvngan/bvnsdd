**Mục lục**
- [11_SDD_20s-Pack-README-and-Integration-Guide_Ver.04_Japanese](#11_sdd_20s-pack-readme-and-integration-guide_ver04_japanese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Tổng quan về nhóm tài liệu số 20](#1-tổng-quan-về-nhóm-tài-liệu-số-20)
  - [2. Thứ tự nên đọc đầu tiên](#2-thứ-tự-nên-đọc-đầu-tiên)
  - [3. Bộ tài liệu đọc tối thiểu theo loại dự án](#3-bộ-tài-liệu-đọc-tối-thiểu-theo-loại-dự-án)
  - [4. Cách sử dụng theo Mode](#4-cách-sử-dụng-theo-mode)
  - [5. Bảng tương ứng giữa Phase và Pack](#5-bảng-tương-ứng-giữa-phase-và-pack)
  - [6. Bảng tương ứng theo artifact](#6-bảng-tương-ứng-theo-artifact)
  - [7. Quy trình đưa vào sử dụng trong ngày 1, tuần 1, tháng 1](#7-quy-trình-đưa-vào-sử-dụng-trong-ngày-1-tuần-1-tháng-1)
  - [8. Nguyên tắc không làm SDD trở nên quá nặng](#8-nguyên-tắc-không-làm-sdd-trở-nên-quá-nặng)
  - [9. Vai trò của 31〜34 nhìn từ tài liệu 11](#9-vai-trò-của-3134-nhìn-từ-tài-liệu-11)
  - [10. Anti-pattern khi đưa vào sử dụng](#10-anti-pattern-khi-đưa-vào-sử-dụng)
  - [11. Definition of Done cho vận hành nhóm tài liệu số 20](#11-definition-of-done-cho-vận-hành-nhóm-tài-liệu-số-20)
  - [12. Prompt Pack Selector](#12-prompt-pack-selector)
  - [13. Quy tắc bảo trì nhóm tài liệu số 20](#13-quy-tắc-bảo-trì-nhóm-tài-liệu-số-20)
  - [14. Ví dụ sử dụng chi tiết theo kịch bản](#14-ví-dụ-sử-dụng-chi-tiết-theo-kịch-bản)
  - [15. Cách đọc theo vai trò](#15-cách-đọc-theo-vai-trò)
  - [16. Kết nối với Advanced Options nhóm tài liệu số 40](#16-kết-nối-với-advanced-options-nhóm-tài-liệu-số-40)
  - [17. Chương trình đào tạo khi đưa nhóm tài liệu số 20 vào sử dụng](#17-chương-trình-đào-tạo-khi-đưa-nhóm-tài-liệu-số-20-vào-sử-dụng)
  - [18. Mô hình trưởng thành khi triển khai](#18-mô-hình-trưởng-thành-khi-triển-khai)
  - [19. KPI triển khai](#19-kpi-triển-khai)
  - [Các tiêu chuẩn bên ngoài và tài liệu công khai đã tham khảo](#các-tiêu-chuẩn-bên-ngoài-và-tài-liệu-công-khai-đã-tham-khảo)

# 11_SDD_20s-Pack-README-and-Integration-Guide_Ver.04_Japanese

Ngày tạo: 2026-05-16  
Đối tượng: người sử dụng nhóm tài liệu SDD Ver.04 số 20, Tech Lead, PM, QA, Security, người thúc đẩy phát triển dựa trên AI  
Tiền đề: `21`〜`29` đã được tạo. `31`〜`34` được sử dụng như phần tiếp nối sau README này. Khi sử dụng Advanced Options nhóm tài liệu số 40, bắt buộc phải lựa chọn thông qua `40_SDD_Advanced-Options-Overview-and-Selection-Guide_Ver.04_Japanese.md`.

---

## 0. Vai trò của tài liệu này

Tài liệu này là **README tổng hợp / hướng dẫn thứ tự triển khai / hướng dẫn lựa chọn pack** để sử dụng nhóm tài liệu số 20 của SDD Ver.04 tại hiện trường mà không bị lúng túng.

Nếu đây là lần đầu xem toàn bộ SDD Ver.04, hãy đọc `10_BVN-SDD_GuideLine.md` trước.  
Tài liệu 11 này chủ yếu là hướng dẫn để sử dụng không nhầm lẫn các pack vận hành thông thường gồm 21〜29 và 31〜34. Advanced Options 40〜49 cần bắt đầu từ hướng dẫn lựa chọn số 40.

Nhóm tài liệu số 20 có nội dung lớn; nếu vận hành theo kiểu lần nào cũng đọc toàn bộ thì sẽ trở nên nặng nề.  
Ngược lại, nếu giao cho AI triển khai hoặc review mà chưa đọc các pack cần thiết, các vấn đề sau sẽ xảy ra.

- AI triển khai bằng suy đoán mà không đọc source mới nhất.
- Bỏ sót contract FE/BE, ràng buộc DB, khả năng tương thích API.
- Bỏ sót rủi ro của cấu hình bảo mật, MCP, hooks, tài liệu bên ngoài.
- Áp dụng quy trình Heavy cho cả dự án nhỏ, khiến SDD trở nên quá nặng.
- Lỗi và nhận xét review không được tận dụng ở lần sau.
- Artifact tăng lên nhưng không biết đâu là bản chuẩn.

Vì vậy README này làm rõ 3 điểm sau.

```text
1. File nào phụ trách việc gì
2. Dự án nào cần dùng file nào
3. Nên triển khai, vận hành và cải tiến SDD theo thứ tự nào
```

---

## 1. Tổng quan về nhóm tài liệu số 20

```text
21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md
22_SDD_1st-Step-Pack_03_プロンプト集_Core_Ver.04_Japanese.md

23_SDD_Source-Intelligence-Pack_Ver.04_Japanese.md
24_SDD_Review-TestCode-Enhancement_Ver.04_Japanese.md
25_SDD_Security-Gate-and-CI-Security_Ver.04_Japanese.md
26_SDD_FE-BE-Contract-and-Impact-Analysis_Ver.04_Japanese.md
27_SDD_Microservice-and-MultiRepo-Analysis_Ver.04_Japanese.md
28_SDD_Applicability-and-RightSizing_Ver.04_Japanese.md
29_SDD_Failure-Mode-and-Continuous-Learning_Ver.04_Japanese.md

11_SDD_20s-Pack-README-and-Integration-Guide_Ver.04_Japanese.md
31_SDD_Context-Loading-and-Exclusion_Ver.04_Japanese.md
32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Japanese.md
33_SDD_Artifact-Governance-and-Traceability_Ver.04_Japanese.md
34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Japanese.md
```

### 1.1 Vị trí của 21〜29

| No | File | Vai trò nói ngắn gọn | Mức độ bắt buộc |
|---|---|---|---|
| 21 | Quy trình cụ thể Core | Quy trình chuẩn Phase 0-A〜9 | Core cho mọi dự án |
| 22 | Bộ prompt Core | Prompt để thực hiện 21 | Core cho mọi dự án |
| 23 | Source Intelligence | Nâng cao độ chính xác phân tích source, xử lý source phức tạp | Standard trở lên |
| 24 | Review/TestCode | Tăng cường review, test, số full-width, khả năng bảo trì | Standard trở lên |
| 25 | Security Gate / CI | Bảo mật, môi trường phát triển AI, CI/CD | Bắt buộc khi có ảnh hưởng Security |
| 26 | FE/BE Contract | FE/BE tách rời, contract API, Contract Test | Bắt buộc khi FE/BE tách rời |
| 27 | Microservice/MultiRepo | Nhiều repo, microservice, quy mô lớn | Bắt buộc với dự án phức tạp |
| 28 | RightSizing | Phán định độ sâu áp dụng, tinh gọn, Stop decision | Core cho mọi dự án |
| 29 | Failure Mode | Biến lỗi, nhận xét, sự cố thành tài sản | Standard trở lên |

### 1.2 Vị trí của 11・31〜34

| No | File | Vai trò nói ngắn gọn | Vì sao cần |
|---|---|---|---|
| 11 | README / Integration Guide | Cổng vào cho 21〜29・31〜34 | Giúp không bị lạc khi số file tăng |
| 31 | Context Loading / Exclusion | Quy định AI được đọc gì và không được đọc gì | Quyết định độ chính xác, an toàn và chi phí |
| 32 | Long Context / Strategic Compact | Ghi nhớ và bàn giao trong công việc dài | Ngăn sự cố compact, quên tiền đề, mất phương hướng |
| 33 | Artifact Governance / Traceability | Quản lý bản chuẩn, bằng chứng, tính nhất quán của artifact | Tránh lệch giữa spec/report/test/review |
| 34 | Project Knowledge / Pattern Library | Tích lũy tri thức đặc thù dự án và pattern thành công | Tăng tính tái lập và phù hợp thực tế của AI |

---

## 2. Thứ tự nên đọc đầu tiên

### 2.1 Thứ tự khuyến nghị khi triển khai mới

```text
Step 1: Đọc 11
Step 2: Dùng 28 để phán định mode áp dụng cho dự án
Step 3: Dùng 21 để xác nhận quy trình tổng thể
Step 4: Dùng prompt của Phase tương ứng từ 22
Step 5: Chọn pack chuyên môn cần thiết từ 23〜27
Step 6: Dùng 31 để xác định tài liệu sẽ cho AI đọc
Step 7: Dùng 33 để quyết định nơi lưu artifact, bản chuẩn và bằng chứng
Step 8: Dùng 32 để quyết định quy tắc bàn giao cho công việc dài
Step 9: Bắt đầu vận hành học tập và tri thức hóa bằng 29 và 34
```

### 2.2 Khi đưa vào dự án hiện hữu giữa chừng

Khi đưa SDD vào một dự án hiện hữu giữa chừng, không cần làm lại hoàn hảo tất cả Phase ngay từ đầu.  
Hãy chỉnh trước những điểm dễ đổ vỡ theo thứ tự sau.

```text
1. Phán định Right-sizing bằng 28
2. Quyết định tài liệu được/không được cho AI đọc bằng 31
3. Tạo Source Availability và Source Inventory bằng 23
4. Quyết định bản chuẩn của artifact bằng 33
5. Tạo Review Checklist bằng 24
6. Biến lỗi đã biết và nhận xét review thành Failure Mode bằng 29
7. Biến quy tắc đặc thù dự án thành Pattern Library bằng 34
```

---

## 3. Bộ tài liệu đọc tối thiểu theo loại dự án

| Loại dự án | Bắt buộc đọc | Đọc khi cần | Thường có thể không đọc |
|---|---|---|---|
| Sửa text nhỏ | 21,22,28,11 | 31 | 23,25,26,27,29 |
| Sửa bug nhẹ | 21,22,28,11,31 | 23,24,33 | 26,27 |
| Sửa API thông thường | 21,22,23,24,28,11,31,33 | 25,29,34 | 26,27 |
| Chỉ sửa FE | 21,22,24,28,11,31 | 23,26,33,34 | 27 |
| Chỉ sửa BE | 21,22,23,24,28,11,31 | 25,33,34 | 26,27 |
| Chức năng FE/BE tách rời | 21,22,23,24,26,28,11,31,33 | 25,29,34 | 27 |
| Có thay đổi DB | 21,22,23,24,25,28,11,31,33 | 29,34 | 26,27 |
| Microservice | 21,22,23,24,25,27,28,11,31,32,33 | 29,34 | 26 chỉ khi FE/BE tách rời |
| Nhiều repo / nhiều tech stack | 21,22,23,24,27,28,11,31,32,33 | 25,29,34 | 26 chỉ khi FE/BE tách rời |
| Có ảnh hưởng bảo mật | 21,22,23,24,25,28,11,31,33 | 29,34 | 26,27 tùy cấu trúc đối tượng |
| Sau sự cố / lỗi production | 21,24,28,29,11,31,33,34 | 23,25,26,27,32 | Không có |
| Cải tạo dài hạn / quy mô lớn | 11 và 21〜29・31〜34 | Advanced Options nhóm 40 | Không có |

---

## 4. Cách sử dụng theo Mode

Dựa trên Mode được định nghĩa trong 28, thay đổi độ sâu áp dụng của nhóm tài liệu số 20.

| Mode | Tổng quan | File chính sử dụng | Phương châm |
|---|---|---|---|
| M0 | Ngoài phạm vi SDD hoặc siêu nhẹ | 11,28 | Chỉ ghi nhận. AI triển khai ở mức tối thiểu. |
| M1 Light | Sửa nhẹ | 21,22,28,11,31 | Tiến hành với artifact tối thiểu. |
| M2 Core Standard | Dự án thông thường | 21,22,23,24,28,11,31,33 | SDD chuẩn. |
| M3 Standard Plus | Có phạm vi ảnh hưởng | 21〜26,28,11〜33 | Bổ sung FE/BE/DB/Security, v.v. |
| M4 Heavy | Phức tạp / quy mô lớn | 11 và 21〜29・31〜34 | Bắt buộc Source Intelligence, Strategic Compact, Traceability. |
| M5 Critical | Rủi ro cao | 11 và 21〜29・31〜34 + nhóm 40 | Bắt buộc phê duyệt của con người, bằng chứng audit, CI Security. |
| MX Stop | Thiếu thông tin / nguy hiểm | 28,31,33 | Dừng triển khai. Bổ sung thông tin cần thiết. |

---

## 5. Bảng tương ứng giữa Phase và Pack

| Phase | Phụ trách chính | Pack bổ trợ | Artifact chính |
|---|---|---|---|
| Phase 0-A Safety Gate | 21,25 | 28,31,33 | repo intake, security gate, settings review |
| Phase 0-B Source Intelligence | 21,23 | 31,33 | source availability, source inventory |
| Phase 1 Spec Pack | 21,22 | 23,26,27,31,33 | spec-pack, source availability summary |
| Phase 2 Context / Rules | 21,22 | 31,34 | context.md, project rules, pattern refs |
| Phase 3 Impl Plan | 21,22 | 23,26,27,33 | impl-plan, impact analysis |
| Phase 4 Review Checklist | 21,22,24 | 25,26,27,33 | review-checklist |
| Phase 5 Implementation | 21,22 | 31,32,33,34 | code change, implementation log |
| Phase 6 Self Review | 21,22,24 | 25,26,27,33 | self-review |
| Phase 7 Test Plan | 21,22,24 | 26,27,33 | test-plan |
| Phase 8 Test Results | 21,22,24 | 33 | test-results |
| Phase 9 Report / Learning | 21,22,29 | 33,34 | final-report, failure mode, knowledge updates |

---

## 6. Bảng tương ứng theo artifact

| Artifact | Nguồn tạo | Quản lý bản chuẩn | Thời điểm cập nhật |
|---|---|---|---|
| `source-availability.md` | 23,31 | 33 | Phase 0-B / Phase 1 |
| `source-inventory.md` | 23 | 33 | Lần đầu / khi thay đổi lớn |
| `context-loading-policy.md` | 31 | 33 | Khi bắt đầu dự án |
| `spec-pack.md` | 21,22 | 33 | Khi thay đổi yêu cầu / phản ánh kết quả điều tra |
| `impact-analysis.md` | 23,26,27 | 33 | Phase 1〜3 |
| `impl-plan.md` | 21,22 | 33 | Trước triển khai / khi thay đổi phương châm |
| `review-checklist.md` | 24 | 33 | Trước triển khai / trước review |
| `security-review.md` | 25 | 33 | Khi có ảnh hưởng Security |
| `test-plan.md` | 24,26,27 | 33 | Sau triển khai / trước test |
| `test-results.md` | 24 | 33 | Sau khi thực thi test |
| `strategic-compact.md` | 32 | 33 | Khi làm việc dài / trước handoff |
| `final-report.md` | 21,22 | 33 | Khi hoàn tất |
| `failure-mode-entry.md` | 29 | 33,34 | Khi có lỗi / near miss / tái phát |
| `pattern-card.md` | 34 | 33 | Khi tri thức hóa |

---

## 7. Quy trình đưa vào sử dụng trong ngày 1, tuần 1, tháng 1

### 7.1 Ngày 1

```text
- Phân phối 11
- Đưa Right-sizing bằng 28 vào sử dụng
- Dùng 21/22 làm quy trình Core
- Chỉ đưa quy tắc tối thiểu của 31 vào sử dụng
  - Không cho đọc secrets
  - Không cho đọc .env
  - Không xem tài liệu cũ là bản chuẩn
  - Lưu danh sách file đã đọc
```

### 7.2 Tuần 1

```text
- Đưa 23 Source Intelligence vào các dự án chuẩn
- Biến 24 Review/TestCode thành chuẩn review
- Đưa 25 Phase 0-A Security Gate vào sử dụng
- Đưa quy tắc đặt tên artifact và quản lý bản chuẩn của 33 vào sử dụng
- Bắt đầu vận hành bộ Failure Mode ban đầu của 29
```

### 7.3 Tháng 1

```text
- Áp dụng 26 FE/BE Contract cho dự án FE/BE tách rời
- Áp dụng 27 Microservice/MultiRepo cho dự án phức tạp
- Đưa 32 Strategic Compact vào công việc dài hạn
- Xây dựng 34 Project Knowledge Library
- Bắt đầu Monthly Continuous Learning Review
```

---

## 8. Nguyên tắc không làm SDD trở nên quá nặng

SDD Ver.04 mạnh mẽ, nhưng nếu luôn áp dụng toàn bộ thì tải vận hành tại hiện trường sẽ cao.  
Vì vậy cần tuân thủ các nguyên tắc sau.

```text
1. Thực hiện Right-sizing bằng 28 trước cho mọi dự án.
2. Không bắt buộc artifact Heavy đối với M1/M2.
3. Tuy nhiên không xem nhẹ Security/DB/FE-BE/Microservice/External IF.
4. Nếu lược bỏ, ghi lại đã lược bỏ gì và vì sao vẫn an toàn.
5. Trước khi tăng khối lượng công việc cho AI, hãy nâng chất lượng Context đưa cho AI.
6. Khi tăng artifact, dùng 33 để quản lý bản chuẩn và độ tươi mới.
7. Nếu thất bại, biến thành Failure Mode bằng 29 và nâng cấp tri thức cần thiết sang 34.
```

---

## 9. Vai trò của 31〜34 nhìn từ tài liệu 11

### 9.1 31 Context Loading / Exclusion

Không phải cứ tăng thông tin cho AI đọc là độ chính xác sẽ tăng.  
Cần kiểm soát “những gì nên đọc” và “những gì không được cho đọc” dựa trên tính mới, tính bản chuẩn, tính bảo mật, noise, Prompt Injection và token cost.

### 9.2 32 Long Context / Strategic Compact

Trong dự án quy mô lớn, session AI, review, triển khai và quyết định sẽ kéo dài.  
32 giúp không làm mất tiền đề trong compact, handoff, resume và phối hợp multi-agent.

### 9.3 33 Artifact Governance / Traceability

Artifact SDD càng nhiều, việc xác định đâu là bản chuẩn và requirement nào được kiểm chứng bởi test nào càng quan trọng.  
33 giữ cho đường dây Requirement → Spec → Plan → Code → Test → Review → Report không bị đứt.

### 9.4 34 Project Knowledge / Pattern Library

AI mạnh về kiến thức tổng quát nhưng không biết framework, method, thuật ngữ nghiệp vụ, pattern cấm đặc thù của dự án.  
34 biến “cách làm đúng” của dự án thành tri thức có thể tái sử dụng.

---

## 10. Anti-pattern khi đưa vào sử dụng

| Anti-pattern | Điều gì xảy ra | Đối sách |
|---|---|---|
| Lần nào cũng đọc toàn bộ file | SDD quá nặng và không được dùng | Right-sizing bằng 28 |
| Ưu tiên tài liệu cũ hơn source | Triển khai/review sai | Định nghĩa Source Priority bằng 31 |
| Chỉ cập nhật Report | Spec Pack hoặc Test Plan bị cũ | Freshness Check bằng 33 |
| Quy trách nhiệm cá nhân khi thất bại | Lỗi bị che giấu | Vận hành blameless bằng 29 |
| Viết mọi thứ vào CLAUDE.md | Không được đọc, mâu thuẫn | Chia Knowledge bằng 34 |
| Bật toàn bộ hooks/MCP ngay từ đầu | Tăng rủi ro quyền hạn/thực thi | Review bằng 25, giới hạn Context bằng 31 |
| Cái gì cũng Heavy hóa | Tăng gánh nặng cho dự án nhỏ | Phán định Mode bằng 28 |
| Cho AI đọc nguyên trạng tài liệu bên ngoài | Prompt injection, noise, nhận định sai | Tạo bản trích xuất bằng 31 |
| Phụ thuộc vào chat cho công việc dài | Mất tiền đề sau compact | Strategic Compact bằng 32 |
| Vị trí artifact tự do | Không rõ bản chuẩn, không audit được | Artifact Governance bằng 33 |

---

## 11. Definition of Done cho vận hành nhóm tài liệu số 20

Trạng thái có thể xem là hoàn tất việc đưa nhóm tài liệu số 20 vào vận hành như sau.

```text
- 21/22 đang được dùng làm quy trình và prompt Core.
- Mode áp dụng cho từng dự án được quyết định bằng 28.
- Tài liệu được/không được cho AI đọc được kiểm soát bằng 31.
- Source Availability và Source Inventory được tạo bằng 23.
- Quan điểm review/test được chuẩn hóa bằng 24.
- Security Gate được đưa vào sử dụng bằng 25.
- 26 được dùng trong dự án FE/BE tách rời.
- 27 được dùng trong dự án Microservice/MultiRepo.
- Có thể bàn giao công việc dài bằng 32.
- Bản chuẩn, bằng chứng, độ tươi mới của artifact được quản lý bằng 33.
- Lỗi được biến thành Failure Mode bằng 29.
- Lỗi và pattern thành công được nâng cấp lên Project Knowledge bằng 34.
```

---

## 12. Prompt Pack Selector

```text
Bạn là kiến trúc sư triển khai SDD Ver.04.
Hãy đọc thông tin dự án dưới đây và phán định nên sử dụng file nào của nhóm tài liệu số 20, theo thứ tự nào.

# Thông tin dự án
- Mục tiêu:
- Đối tượng thay đổi:
- FE/BE tách rời:
- Thay đổi DB:
- External IF:
- Microservice / MultiRepo:
- Ảnh hưởng Security / Privacy:
- Ảnh hưởng vận hành:
- Deadline:
- Điều chưa chắc chắn đã biết:
- Tài liệu có thể sử dụng:
- Tài liệu không thể sử dụng:

# Định dạng đầu ra
1. Mode khuyến nghị
2. File bắt buộc sử dụng
3. File sử dụng khi cần
4. File không cần đọc
5. Artifact cần tạo đầu tiên
6. Điều kiện Stop / Ask
7. Điểm cần con người phê duyệt
8. Quy trình có thể lược bỏ và lý do
9. Có cần áp dụng 31〜34 hay không
10. Đề xuất cuối cùng
```

---

## 13. Quy tắc bảo trì nhóm tài liệu số 20

```text
- 21/22 là Core nên không làm phình to thường xuyên.
- Nội dung có tính chuyên môn cao đưa sang 23〜27.
- Phán định áp dụng tập trung vào 28.
- Học từ thất bại tập trung vào 29.
- Cổng vào giữa các file tập trung vào 11.
- Kiểm soát Context tập trung vào 31.
- Công việc dài/handoff tập trung vào 32.
- Quản lý artifact tập trung vào 33.
- Tri thức đặc thù dự án tập trung vào 34.
- Trước khi thêm quan điểm mới, kiểm tra nó thuộc file hiện hữu nào.
```

---

---

## 14. Ví dụ sử dụng chi tiết theo kịch bản

### 14.1 Sửa text UI nhỏ

```text
Mục tiêu:
- Xác nhận spec và giảm thiểu side effect

Đọc:
- 11
- 28
- Phase tương ứng của 21
- Prompt tương ứng của 22
- Quy tắc Context tối thiểu của 31

Tạo:
- mini spec
- diff summary
- test skip reason hoặc test result đơn giản
- final note

Thường có thể không cần đọc:
- 26
- 27
- 32
- toàn bộ 34
```

### 14.2 Sửa bug nhập số

```text
Đọc:
- 21,22
- 23 Source Availability
- 24 General System Review / Test Pattern
- 28 Mode phán định
- 31 Context Loading
- 33 Traceability
- 34 Input Normalization Rules

Bắt buộc xác nhận:
- số full-width
- trộn half-width/full-width
- comma
- số thập phân
- số âm
- null/empty
- precision/scale
- FE validation
- BE validation
- ràng buộc DB
```

### 14.3 Thêm chức năng FE/BE tách rời

```text
Đọc:
- 21,22,23,24,26,28,11,31,33
- Nếu có ảnh hưởng Security thì đọc 25
- Nếu kéo dài thì đọc 32
- Nếu có quy tắc đặc thù dự án thì đọc 34

Tạo:
- Source Availability
- FE/BE Contract Map
- Impact Analysis
- Validation Parity Map
- Error Message Map
- Permission Map
- Contract Test Plan
- Traceability Matrix
```

### 14.4 Cải tạo xuyên microservice

```text
Đọc:
- 21〜25
- 27〜34

Tạo:
- Service Catalog
- Repo Catalog
- Cross-Repo Version Matrix
- Dependency Map
- API/Event Contract Map
- Data Ownership Map
- Retry/Idempotency Map
- Deployment Order
- Rollback Plan
- Observability Map
- Strategic Compact
- Audit Package
```

### 14.5 Dự án rủi ro bảo mật cao

```text
Đọc:
- 21,22,23,24,25,28,11,31,33
- Nếu dùng AI harness hoặc MCP/hooks thì bắt buộc đọc 25 và 31
- Nếu review dài thì đọc 32
- Nếu phòng ngừa tái phát thì đọc 29/34

Tạo:
- Security Gate
- Threat Model
- Security Review Findings
- Accepted Risk Record
- SBOM / dependency evidence
- CI security evidence
- Human Approval Record
```

---

## 15. Cách đọc theo vai trò

| Vai trò | Đọc đầu tiên | Đọc sâu | Trách nhiệm chính |
|---|---|---|---|
| Developer | 11,21,22,28 | 23,24,31,34 | Triển khai với context đúng và để lại bằng chứng |
| Tech Lead | 11,21,23,24,28,33 | 26,27,31,32,34 | Quyết định độ sâu áp dụng, quyết định thiết kế, chấp nhận/từ chối review |
| QA | 24,28,33 | 26,27,29,34 | Xem AC, test plan, test result, traceability |
| Security | 25,31,33 | 23,24,27,29 | Xem Security Gate, AI harness, CI security |
| PM/PL | 11,28,33 | 29,32 | Quản lý mức độ nặng, schedule, approval, risk |
| Người thúc đẩy AI | 11,28,29,34 | 31,32,33 | Vận hành continuous improvement, knowledge hóa, đào tạo |

---

## 16. Kết nối với Advanced Options nhóm tài liệu số 40

Nhóm tài liệu số 20 là vận hành chuẩn.  
Nhóm tài liệu số 40 chỉ được bổ sung khi vận hành chuẩn không đủ.

```text
40_Advanced-Options-Overview-and-Selection-Guide
41_Heavy-Source-Analysis-and-Repository-Intelligence
42_Multi-Model-Multi-Agent-Orchestrator
43_Tool-Grounded-Verification-and-Consensus
44_Token-Optimization-and-Cost-Control
45_Full-Security-and-Agentic-AI-Governance
46_RAG-CodeMap-and-Context-Compression
47_Automated-PR-Review-and-AI-QA-Gate
48_Parallel-Worktree-and-Large-Refactoring
49_Evaluation-Observability-and-Continuous-Optimization
```

Khi dùng nhóm tài liệu số 40, trước tiên tạo Option Selection Record bằng 40.  
Tạo nền tảng vận hành thông thường bằng 11 và 21〜29・31〜34, sau đó dùng 40 để quyết định “chỉ dùng Advanced Option nào”.

Điều kiện để chuyển sang nhóm 40:

```text
- Phán định M4/M5
- Ảnh hưởng lớn xuyên nhiều repo
- Yêu cầu bảo mật/audit cao
- Lượng code và quan hệ phụ thuộc nhiều, review thông thường không đủ
- Cần tách AI review thành nhiều hệ thống/quan điểm
- Muốn chia việc an toàn bằng parallel worktree
```

Điều kiện bắt buộc trước khi chuyển sang nhóm 40:

```text
- Có 31 Context Manifest
- Có 32 Handoff / Compact
- Có 33 Artifact Inventory
- Mode phán định bằng 28 là M4/M5
- Đã qua 25 Security Gate
```

---

## 17. Chương trình đào tạo khi đưa nhóm tài liệu số 20 vào sử dụng

### Day 1: Cổng vào SDD

```text
- Tổng quan của 11
- Quy trình Core của 21/22
- Right-sizing của 28
- Bài tập nhỏ
```

### Day 2: Nâng độ chính xác

```text
- 23 Source Intelligence
- 31 Context Loading
- 24 Review/TestCode
- Bài tập số, số full-width, Magic Number
```

### Day 3: Làm an toàn

```text
- 25 Security Gate
- Đối sách secret/PII/prompt injection
- CI security
- Bài tập external content intake
```

### Day 4: Dự án phức tạp

```text
- 26 FE/BE Contract
- 27 Microservice/MultiRepo
- 32 Strategic Compact
- 33 Traceability
```

### Day 5: Cải tiến liên tục

```text
- 29 Failure Mode
- 34 Project Knowledge
- Monthly Learning Review
- Vận hành Pattern Library
```

---

## 18. Mô hình trưởng thành khi triển khai

| Level | Trạng thái | Cải tiến tiếp theo |
|---|---|---|
| L0 | Đang yêu cầu AI tùy lúc | Đưa 21/22 vào sử dụng |
| L1 | Có quy trình Core | Right-sizing bằng 28 |
| L2 | Source/Review/Test đã chuẩn hóa | Quản lý context và artifact bằng 31/33 |
| L3 | Security/FE-BE/Microservice cũng đã chuẩn hóa | Vận hành dài hạn và học tập bằng 32/29/34 |
| L4 | Continuous improvement đang chạy | Lựa chọn đưa Advanced nhóm 40 vào sử dụng |
| L5 | Có thể audit như chuẩn tổ chức | Cải tiến chỉ số, đào tạo, tự động hóa |

---

## 19. KPI triển khai

```text
- Số dự án áp dụng SDD
- Tỷ lệ thực hiện phán định Right-sizing
- Tỷ lệ tạo Source Availability
- Tỷ lệ tạo Context Manifest
- Tỷ lệ tạo Review Checklist
- Tỷ lệ kết nối Test Plan / Test Results
- Tỷ lệ tạo Traceability Matrix
- Tỷ lệ đăng ký Failure Mode
- Tỷ lệ nâng cấp sang Pattern Library
- Tỷ lệ giảm rework do AI gây ra
- Tỷ lệ giảm thời gian review của con người
- Tỷ lệ False Positive
- Tỷ lệ tái phát của sự cố production, rework, review miss
```

## Các tiêu chuẩn bên ngoài và tài liệu công khai đã tham khảo

Pack này tái cấu trúc tư tưởng của các tiêu chuẩn bên ngoài và tài liệu công khai dưới đây theo ngữ cảnh SDD.  
Các tiêu chuẩn bên ngoài không phải là đối tượng để copy nguyên trạng, mà cần điều chỉnh độ sâu áp dụng theo quy định nội bộ, đặc tính dự án, yêu cầu khách hàng và pháp quy.

| Lĩnh vực | Nguồn tham khảo | Cách dùng trong SDD |
|---|---|---|
| Vận hành AI Agent | Everything Claude Code | Đưa có chọn lọc và an toàn các tư tưởng về skills / rules / hooks / MCP / memory optimization / continuous learning / security scanning / research-first development vào sử dụng. |
| Secure SDLC | NIST SP 800-218 SSDF | Làm nền tảng cho Phase 0-A, thiết kế an toàn, phòng ngừa tái phát lỗ hổng, bằng chứng, CI security. |
| AI Risk | NIST AI RMF | Xử lý rủi ro của phát triển có AI hỗ trợ theo vòng Govern / Map / Measure / Manage. |
| LLM Security | OWASP Top 10 for LLM Applications 2025 | Dùng cho đối sách Prompt Injection, Sensitive Information Disclosure, Excessive Agency, v.v. khi đọc tài liệu bên ngoài, log, Issue, Web page. |
| Application Security | OWASP ASVS | Làm đường dẫn bổ trợ cho yêu cầu bảo mật, quan điểm review và quan điểm test của Web/API. |
| Supply Chain | SLSA / OpenSSF | Làm đường dẫn bổ trợ để xem xét build, dependency, artifact tạo ra, CI/CD, bằng chứng, chữ ký, khả năng chống sửa đổi. |
| SBOM | CycloneDX / SPDX | Dùng để biểu diễn dependency, component, AI/ML BOM, lỗ hổng, license, rủi ro supply chain. |
| Provenance | W3C PROV | Dùng như tư tưởng xử lý nguồn gốc, người tạo, căn cứ, quan hệ phái sinh, đánh giá độ tin cậy của artifact. |
| Delivery Metrics | DORA | Dùng làm chỉ số bổ trợ để đo tốc độ, tính ổn định và khả năng phục hồi sau khi triển khai SDD. |
| Operations Learning | Google SRE Postmortem | Xử lý Failure Mode, Near Miss, Postmortem như học tập của tổ chức thay vì trách nhiệm cá nhân. |
| Observability | OpenTelemetry | Kết nối tư tưởng trace / metric / log / baggage / context propagation với vận hành, giám sát, điều tra xuyên hệ thống. |
