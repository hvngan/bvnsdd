**Mục lục**
- [34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Vietnamese](#34_sdd_project-knowledge-and-pattern-library_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Kết luận](#1-kết-luận)
  - [2. Quan hệ với 29](#2-quan-hệ-với-29)
  - [3. Phân loại Knowledge](#3-phân-loại-knowledge)
  - [4. Cấu trúc thư mục khuyến nghị](#4-cấu-trúc-thư-mục-khuyến-nghị)
  - [5. Knowledge Card](#5-knowledge-card)
  - [6. Pattern Card](#6-pattern-card)
  - [7. Anti-pattern Card](#7-anti-pattern-card)
  - [8. AI Context Pack](#8-ai-context-pack)
  - [9. Tiêu chí nâng cấp lên CLAUDE.md / rules / prompts / checklist](#9-tiêu-chí-nâng-cấp-lên-claudemd--rules--prompts--checklist)
  - [10. Knowledge Lifecycle](#10-knowledge-lifecycle)
  - [11. Tiêu chí đăng ký](#11-tiêu-chí-đăng-ký)
  - [12. Chuẩn Known Good Example](#12-chuẩn-known-good-example)
  - [13. Chuẩn Known Bad Example](#13-chuẩn-known-bad-example)
  - [14. Framework Constraints](#14-framework-constraints)
  - [15. Method Allowlist / Denylist](#15-method-allowlist--denylist)
  - [16. Domain Glossary](#16-domain-glossary)
  - [17. Project Knowledge về số, loại ký tự và ngày tháng](#17-project-knowledge-về-số-loại-ký-tự-và-ngày-tháng)
  - [18. Review Pattern Library](#18-review-pattern-library)
  - [19. Test Pattern Library](#19-test-pattern-library)
  - [20. Cách chuyển Project Knowledge cho 31](#20-cách-chuyển-project-knowledge-cho-31)
  - [21. Quản lý độ tươi mới của Knowledge](#21-quản-lý-độ-tươi-mới-của-knowledge)
  - [22. Lưu ý về Security / Privacy](#22-lưu-ý-về-security--privacy)
  - [23. Prompt chuyên dụng cho 34](#23-prompt-chuyên-dụng-cho-34)
  - [24. Metrics](#24-metrics)
  - [25. Failure Mode tiêu biểu](#25-failure-mode-tiêu-biểu)
  - [26. Definition of Done](#26-definition-of-done)
  - [27. Quy trình xây dựng ban đầu cho tri thức dự án](#27-quy-trình-xây-dựng-ban-đầu-cho-tri-thức-dự-án)
  - [28. Cách trích xuất Knowledge từ dự án hiện có](#28-cách-trích-xuất-knowledge-từ-dự-án-hiện-có)
  - [29. Độ chi tiết của Knowledge](#29-độ-chi-tiết-của-knowledge)
  - [30. Vận hành trong nhóm](#30-vận-hành-trong-nhóm)
  - [31. Lưu ý khi yêu cầu AI sử dụng Project Knowledge](#31-lưu-ý-khi-yêu-cầu-ai-sử-dụng-project-knowledge)
  - [32. Knowledge Usage Record](#32-knowledge-usage-record)
  - [33. Knowledge và đào tạo](#33-knowledge-và-đào-tạo)
  - [34. Tách biệt với Knowledge xuyên tổ chức](#34-tách-biệt-với-knowledge-xuyên-tổ-chức)
  - [34-A. Những nội dung cần đưa lại từ Advanced Options nhóm 40 vào Knowledge](#34-a-những-nội-dung-cần-đưa-lại-từ-advanced-options-nhóm-40-vào-knowledge)
  - [35. Knowledge Debt](#35-knowledge-debt)
  - [Tài liệu chuẩn và tài liệu công khai đã tham khảo](#tài-liệu-chuẩn-và-tài-liệu-công-khai-đã-tham-khảo)
- [Appendix. Dành cho người mới: Quy trình thực thi và prompt copy-paste của pack này](#appendix-dành-cho-người-mới-quy-trình-thực-thi-và-prompt-copy-paste-của-pack-này)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Đầu vào đầu tiên cần cho AI đọc](#a-3-đầu-vào-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Sản phẩm cần tạo/cập nhật](#a-4-sản-phẩm-cần-tạocập-nhật)
  - [A-5. Quy trình thực thi dành cho người mới](#a-5-quy-trình-thực-thi-dành-cho-người-mới)
  - [A-6. Prompt dùng để copy-paste: Prompt bắt đầu chỉ lập Plan](#a-6-prompt-dùng-để-copy-paste-prompt-bắt-đầu-chỉ-lập-plan)
  - [A-7. Checklist xác nhận Plan](#a-7-checklist-xác-nhận-plan)
  - [A-8. Prompt dùng để copy-paste: Prompt phê duyệt Plan](#a-8-prompt-dùng-để-copy-paste-prompt-phê-duyệt-plan)
  - [A-9. Prompt dùng để copy-paste: Prompt review sản phẩm và đánh giá hoàn tất](#a-9-prompt-dùng-để-copy-paste-prompt-review-sản-phẩm-và-đánh-giá-hoàn-tất)
  - [A-10. Prompt dùng để copy-paste: Prompt trả lại để sửa](#a-10-prompt-dùng-để-copy-paste-prompt-trả-lại-để-sửa)
  - [A-11. Điều kiện Stop/Ask](#a-11-điều-kiện-stopask)
  - [A-12. Cổng hoàn tất](#a-12-cổng-hoàn-tất)
  - [A-13. Điểm cần đi tiếp](#a-13-điểm-cần-đi-tiếp)
  - [A-14. Lỗi người mới thường mắc và cách phòng tránh](#a-14-lỗi-người-mới-thường-mắc-và-cách-phòng-tránh)
  - [A-15. Lộ trình ngắn nhất](#a-15-lộ-trình-ngắn-nhất)

# 34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Vietnamese

Ngày tạo: 2026-05-16  
Đối tượng: Quy tắc riêng của dự án, mẫu thành công, mẫu bị cấm, tri thức nghiệp vụ, cải thiện độ chính xác của AI  
Kết nối tới: 21〜33,40〜49

---

## 0. Vai trò của tài liệu này

Tài liệu này là tiêu chuẩn để tích lũy và duy trì tri thức riêng của dự án dưới dạng AI có thể tái sử dụng.

Trong SDD, chỉ các best practice chung là chưa đủ.  
Thứ quyết định độ chính xác của AI tại hiện trường thường là **tri thức đặc thù của từng dự án** như sau.

```text
- Thuật ngữ nghiệp vụ
- Tên màn hình, tên báo cáo, tên API
- Quy tắc đặt tên DB
- Ràng buộc của framework hiện có
- Method được phép dùng
- Method không được phép dùng
- Ví dụ triển khai đúng hiện có
- Ví dụ triển khai đã từng thất bại
- Chuẩn xử lý ngoại lệ
- Chuẩn log
- Chuẩn kiểm tra quyền
- Chuẩn dữ liệu test
- Cách xử lý số, số full-width, loại ký tự và ngày tháng
- Các góc nhìn review thường xuyên bị nhắc lại
```

29 là “cơ chế học từ thất bại”.  
34 là cơ chế chỉnh lý các bài học và mẫu thành công đó thành **tri thức mà AI thực sự có thể dùng trong lần sau**.

---

## 1. Kết luận

Trong Project Knowledge and Pattern Library, các điểm sau là bắt buộc.

```text
1. Không nhốt tri thức riêng của dự án trong chat.
2. Lưu lại cả mẫu thành công và mẫu bị cấm.
3. Tạo Context Pack ngắn để AI đọc trước khi làm việc.
4. Không nhồi tất cả vào CLAUDE.md, mà tách theo mục đích sử dụng.
5. Có luồng nâng cấp từ Failure Mode lên Knowledge.
6. Knowledge phải có owner, evidence, status và expiry.
7. Knowledge cũ phải được deprecate hoặc cập nhật.
8. Ví dụ triển khai đúng được lưu làm Known Good Example.
9. Ví dụ triển khai sai được lưu làm Known Bad Example.
10. Knowledge của 34 chỉ được đưa vào AI context thông qua 31 ở mức tối thiểu cần thiết.
```

---

## 2. Quan hệ với 29

| 29 Failure Mode | 34 Project Knowledge |
|---|---|
| Ghi lại thất bại, sự cố, near miss | Chuyển thất bại thành tri thức tái sử dụng được để phòng tránh |
| Tổ chức Root Cause và Prevention | Nâng cấp thành pattern / rule / prompt / checklist cụ thể |
| Ghi chép sự kiện riêng lẻ | Hành vi chuẩn cho tương lai |
| postmortem / failure entry | knowledge card / pattern card / anti-pattern card |

Ví dụ:

```text
29:
AI đã gọi DBStatement#setDouble() không tồn tại

34:
Đăng ký “danh sách method có thể dùng trong DBStatement” vào framework-constraints.md
Đăng ký setDouble vào method-denylist.md
Đăng ký ví dụ đúng về xử lý BigDecimal vào known-good-examples.md
Thêm kiểm tra method không tồn tại vào review-patterns.md
```

---

## 3. Phân loại Knowledge

| Category | Nội dung | Ví dụ |
|---|---|---|
| Glossary | Thuật ngữ nghiệp vụ | Đơn hàng, xuất kho, phân bổ, SEQNO |
| Domain Rules | Quy tắc nghiệp vụ | Điều kiện có thể hủy, xử lý chốt kỳ |
| Architecture Patterns | Cấu trúc và trách nhiệm | Controller-Service-Repository |
| Coding Patterns | Chuẩn triển khai | Xử lý ngoại lệ, null handling |
| FE Patterns | Màn hình và quản lý state | loading/error/empty |
| BE Patterns | API/Service | validation, transaction |
| DB Patterns | table, index, migration | precision/scale |
| Security Patterns | Ủy quyền, audit, secret | permission check |
| Test Patterns | Dữ liệu test, giá trị biên | số full-width, số chữ số |
| Operation Patterns | Log, giám sát, khôi phục | correlation id |
| Anti-patterns | Ví dụ bị cấm | magic number, method không tồn tại |
| Known Good Examples | Ví dụ đúng | Triển khai tốt hiện có |
| Known Bad Examples | Ví dụ xấu | Bug trong quá khứ |
| Tooling Rules | Claude/Codex/CI | hạn chế hooks/MCP |
| Review Patterns | Góc nhìn thường thấy | xu hướng false positive |

---

## 4. Cấu trúc thư mục khuyến nghị

```text
docs/project-knowledge/
  README.md
  00_ai-context-pack.md
  01_glossary.md
  02_domain-rules.md
  03_architecture-patterns.md
  04_coding-patterns.md
  05_fe-patterns.md
  06_be-patterns.md
  07_db-patterns.md
  08_api-patterns.md
  09_security-patterns.md
  10_testing-patterns.md
  11_operation-patterns.md
  12_review-patterns.md
  13_framework-constraints.md
  14_method-allowlist.md
  15_method-denylist.md
  16_known-good-examples.md
  17_known-bad-examples.md
  18_migration-notes.md
  19_prompt-patterns.md
  20_ci-and-tooling.md
  archive/
```

---

## 5. Knowledge Card

```md
# Knowledge Card

## ID
KN-

## Title

## Category
- glossary / domain / architecture / coding / fe / be / db / api / security / testing / operation / review / tooling

## Status
- Draft / Active / Deprecated / Superseded

## Summary

## When to Apply

## Do

## Do Not

## Evidence
- source:
- review:
- failure mode:
- human decision:

## Example

## Counterexample

## Related Files

## Related Failure Modes

## Owner

## Last Reviewed

## Expiry / Re-review Trigger
```

---

## 6. Pattern Card

```md
# Pattern Card

## Pattern ID
PAT-

## Name

## Problem

## Context

## Recommended Solution

## Implementation Steps
1.
2.
3.

## Known Good Example

## Review Checklist

## Test Checklist

## Security / Operation Notes

## Anti-patterns to Avoid

## Related Knowledge

## Adoption Criteria
```

---

## 7. Anti-pattern Card

```md
# Anti-pattern Card

## Anti-pattern ID
AP-

## Name

## What It Looks Like

## Why It Is Bad

## How to Detect

## Correct Pattern

## Known Bad Example

## Known Good Example

## Review Prompt Snippet

## Test / CI Detection

## Related Failure Modes

## Status
```

---

## 8. AI Context Pack

Không cho AI đọc toàn bộ Project Knowledge mỗi lần.  
Trước khi làm việc, hãy tạo Context Pack ở mức tối thiểu cần thiết.

```md
# AI Context Pack

## Task

## Must Read Knowledge
-

## Must Follow Rules
-

## Allowed Methods / Components
-

## Forbidden Methods / Components
-

## Known Good Examples
-

## Known Bad Examples
-

## Domain Terms
-

## Validation / Error / Message Rules
-

## Security / Permission Rules
-

## Test Rules
-

## Operation / Logging Rules
-

## Related Failure Modes
-

## Do Not Read / Do Not Use
-
```

---

## 9. Tiêu chí nâng cấp lên CLAUDE.md / rules / prompts / checklist

### 9.1 Những nội dung viết vào CLAUDE.md

```text
- Nguyên tắc ngắn mà mọi người luôn phải tuân thủ
- Điều cấm quan trọng
- Điều bắt buộc về an toàn
- Kiểm tra cơ bản trước khi bắt đầu công việc
```

### 9.2 Những nội dung viết vào rules

```text
- Quy ước luôn áp dụng xuyên suốt dự án
- Quy tắc triển khai theo từng ngôn ngữ/framework
- Quy tắc định hình về security, test và review
```

### 9.3 Những nội dung viết vào prompts

```text
- Câu hỏi và định dạng output dùng trong một Phase cụ thể
- Gọi ra các góc nhìn review
- Trích xuất Failure Mode
- Trích xuất ứng viên pattern
```

### 9.4 Những nội dung viết vào checklist

```text
- Hạng mục mà reviewer người cần kiểm tra mỗi lần
- Góc nhìn từng bị bỏ sót lặp lại trong quá khứ
- Góc nhìn AI dễ tạo false negative
```

### 9.5 Những nội dung nâng cấp lên CI/Test

```text
- Có thể phát hiện bằng máy
- Hiệu quả phòng tái phát cao
- Có thể kiểm soát false positive
- Giá trị phát hiện lớn hơn chi phí sửa
```

---

## 10. Knowledge Lifecycle

```text
Candidate
  ↓
Draft
  ↓
Reviewed
  ↓
Active
  ↓
Promoted
  ↓
Deprecated / Superseded
```

| Status | Ý nghĩa |
|---|---|
| Candidate | Được đề xuất từ Failure Mode hoặc review |
| Draft | Đang tổng quát hóa |
| Reviewed | Đã được Tech Lead hoặc người tương đương xác nhận |
| Active | Có thể đưa vào AI context |
| Promoted | Đã nâng cấp lên rules/prompts/checklist/CI |
| Deprecated | Đã cũ, cấm dùng |
| Superseded | Được thay thế bằng card mới |

---

## 11. Tiêu chí đăng ký

Những nội dung nên Knowledge hóa:

```text
- Cùng một lỗi xảy ra từ 2 lần trở lên
- Chỉ 1 lần nhưng đã dẫn đến sự cố nghiêm trọng
- AI có xác suất sai cao
- Người mới có xác suất vướng cao
- Thường xuyên xuất hiện trong review
- Xem ví dụ triển khai hiện có dễ hiểu hơn so với đọc spec
- Đặc thù framework, kiến thức chung không đủ
- Đặc thù khách hàng/nghiệp vụ, không có trong tri thức bên ngoài
```

Những nội dung không nên Knowledge hóa:

```text
- Sự kiện ngẫu nhiên chỉ xảy ra một lần
- Biện pháp tạm thời đã hết hạn
- Bản thân thông tin mật
- Dữ liệu thật có chứa thông tin cá nhân
- Chi tiết đã triển khai xong và không còn giá trị tham chiếu trong tương lai
- Nội dung chỉ cần kiến thức chung là đủ
```

---

## 12. Chuẩn Known Good Example

```md
# Known Good Example

## ID
KGE-

## Title

## Applies To
- language:
- framework:
- layer:
- feature:

## Why This Is Good

## Code Location

## Key Points

## Use When

## Do Not Use When

## Related Pattern

## Related Tests

## Review Notes
```

---

## 13. Chuẩn Known Bad Example

```md
# Known Bad Example

## ID
KBE-

## Title

## What Went Wrong

## Code / Diff / Incident Reference

## Why AI Might Repeat It

## Detection Method

## Correct Pattern

## Related Failure Mode

## Preventive Rule

## Test / CI Candidate
```

---

## 14. Framework Constraints

```md
# Framework Constraints

## Framework / Library

## Version

## Allowed APIs

| API | Use case | Example | Notes |
|---|---|---|---|

## Disallowed APIs

| API | Reason | Correct alternative |
|---|---|---|

## Common Pitfalls

## Compile / Runtime Checks

## Related Known Good Examples

## Related Failure Modes
```

---

## 15. Method Allowlist / Denylist

```md
# Method Allowlist

| Class / Module | Method | Use Case | Example | Notes |
|---|---|---|---|---|

# Method Denylist

| Class / Module | Forbidden Method | Why Forbidden | Correct Alternative | Detection |
|---|---|---|---|---|
```

---

## 16. Domain Glossary

```md
# Domain Glossary

| Term | Meaning | Related Screen/API/Table | Notes | Source |
|---|---|---|---|---|
```

Thuật ngữ cần có quan hệ tương ứng giữa đa ngôn ngữ, full-width/half-width, viết tắt và tên DB.

```text
- Tên nghiệp vụ
- Tên hiển thị màn hình
- Tên vật lý DB
- API field
- enum value
- master code
- Tiếng Nhật / tiếng Anh / tiếng Việt, v.v.
```

---

## 17. Project Knowledge về số, loại ký tự và ngày tháng

Cụ thể hóa các góc nhìn review của 24 thành quy tắc riêng của dự án.

```md
# Input Normalization Rules

## Numeric Fields
| Field | Allow full-width | Allow comma | Allow negative | Scale | Rounding | DB type | FE rule | BE rule |
|---|---|---|---|---|---|---|---|---|

## Character Rules
| Field | Unicode normalization | Trim | Max length | Encoding risk | Notes |
|---|---|---|---|---|---|

## Date / Time Rules
| Field | Timezone | Format | Boundary | Storage | Display |
|---|---|---|---|---|---|
```

---

## 18. Review Pattern Library

```md
# Review Pattern

## ID
REV-

## Name

## Applies To

## Detection Question

## Why It Matters

## Examples of Real Findings

## False Positive Notes

## Automation Candidate

## Related Tests

## Related Failure Modes
```

---

## 19. Test Pattern Library

```md
# Test Pattern

## ID
TESTPAT-

## Name

## Applies To

## Test Data

## Boundary Cases

## Expected Behavior

## Automation Level
- unit / integration / contract / e2e / manual

## Related Requirement

## Known Pitfalls
```

---

## 20. Cách chuyển Project Knowledge cho 31

Không đưa toàn bộ Project Knowledge vào context.  
Trong Context Manifest của 31, chỉ chọn những phần cần thiết cho task.

```text
1. Xác định loại ticket
2. Xác định layer liên quan
3. Xác định domain term liên quan
4. Tìm kiếm Failure Mode trong quá khứ
5. Chọn relevant pattern
6. Tạo AI Context Pack
7. Đăng ký vào Context Manifest của 31
8. Bàn giao tiếp sang Strategic Compact của 32
```

---

## 21. Quản lý độ tươi mới của Knowledge

```md
# Knowledge Freshness Review

## Target Knowledge

## Last Reviewed

## Trigger
- source changed
- framework version changed
- architecture changed
- failure mode added
- false positive increased
- team rule changed

## Verdict
- Keep / Update / Deprecate / Supersede

## Required Action
```

---

## 22. Lưu ý về Security / Privacy

Không đưa các nội dung sau vào Project Knowledge.

```text
- real secret
- real credential
- production token
- dữ liệu thật có chứa thông tin cá nhân
- tài liệu chứa nguyên văn bí mật khách hàng khi không cần thiết
- chi tiết quá mức về quy trình tấn công
- chi tiết có thể bị lạm dụng của security exception
```

Khi cần thiết, hãy ẩn danh hóa, trừu tượng hóa hoặc tóm tắt.

---

## 23. Prompt chuyên dụng cho 34

### 23.1 Trích xuất ứng viên Knowledge từ Failure Mode

```text
Bạn là Project Knowledge Curator của SDD Ver.04.
Hãy đọc Failure Mode Entry dưới đây và trích xuất các nội dung nên nâng cấp lên Project Knowledge.

# Đầu vào
<Failure Mode Entry>

# Đầu ra
1. Ứng viên Knowledge nên nâng cấp
2. Category
3. Nên nâng cấp thành Pattern / Anti-pattern / Rule / Checklist / Test / CI
4. Evidence
5. Ứng viên Known Good Example
6. Ứng viên Known Bad Example
7. Tóm tắt nên đưa vào AI Context Pack
8. Knowledge hiện có đã cũ
9. Human review required
```

### 23.2 Kiểm kê Project Knowledge

```text
Hãy review Project Knowledge Library dưới đây và tổ chức các tri thức đã cũ, trùng lặp, mâu thuẫn, nội dung nên viết vào CLAUDE.md, nội dung nên nâng cấp lên rules và nội dung nên CI hóa.

# Đầu vào
- knowledge files:
- recent failure modes:
- recent review findings:
- recent source changes:

# Đầu ra
- keep
- update
- deprecate
- merge
- promote to CLAUDE.md
- promote to rules
- promote to prompt
- promote to checklist
- promote to test/CI
- human decisions required
```

### 23.3 Tạo AI Context Pack

```text
Đối với ticket dưới đây, hãy tạo AI Context Pack tối thiểu cần thiết mà AI nên đọc từ Project Knowledge Library.

# Đầu vào
- ticket:
- target files:
- layer:
- source inventory:
- failure mode index:
- project knowledge library:

# Đầu ra
Hãy xuất theo định dạng AI Context Pack.
Không chép toàn bộ; chỉ chọn knowledge cần thiết và chỉ rõ file căn cứ.
```

### 23.4 Tạo Pattern Card

```text
Từ ví dụ thành công hoặc chỉ ra review dưới đây, hãy tạo Pattern Card hoặc Anti-pattern Card.

# Đầu vào
- source / diff:
- review finding:
- test result:
- human decision:
- failure mode:

# Đầu ra
Hãy xuất theo định dạng Pattern Card hoặc Anti-pattern Card.
Bao gồm Do / Do Not, Known Good, Known Bad, Review Checklist và Test Checklist.
```

---

## 24. Metrics

| Metric | Ý nghĩa |
|---|---|
| Knowledge Reuse Rate | Tỷ lệ tri thức được tái sử dụng trong AI Context Pack |
| Repeat Failure Rate | Tỷ lệ tái phát cùng Failure Mode |
| Pattern Promotion Lead Time | Thời gian từ Failure Mode đến khi pattern hóa |
| Knowledge Freshness Pass Rate | Tỷ lệ tri thức được đánh giá còn hiệu lực khi kiểm kê |
| False Positive Reduction | Tỷ lệ giảm false positive sau khi rule hóa |
| Review Finding Recurrence | Tỷ lệ tái phát cùng một chỉ ra review |
| New Member Onboarding Impact | Cải thiện onboarding cho thành viên mới |
| AI Compile Error Reduction | Giảm lỗi compile sau khi phản ánh framework constraints |
| Test Coverage Improvement | Cải thiện độ bao phủ nhờ áp dụng Test Pattern |

---

## 25. Failure Mode tiêu biểu

```text
PKL-001 AI không biết ràng buộc method riêng của dự án và gọi method không tồn tại
PKL-002 Hiểu sai ý nghĩa thuật ngữ nghiệp vụ
PKL-003 Không cung cấp ví dụ triển khai đúng hiện có, dẫn đến triển khai theo lý thuyết chung
PKL-004 Nhồi quá nhiều vào CLAUDE.md khiến rule quan trọng bị chôn vùi
PKL-005 Knowledge cũ còn tồn tại và dẫn dắt sai
PKL-006 Failure Mode không được nâng cấp lên Knowledge nên tái phát
PKL-007 Không có Known Bad Example, khiến AI bắt chước triển khai sai trong quá khứ
PKL-008 Thiếu Test Pattern nên bỏ sót giá trị biên
PKL-009 Quy tắc số, loại ký tự không nhất quán giữa FE/BE/DB
PKL-010 Đưa secret/PII vào Knowledge
```

---

## 26. Definition of Done

Trạng thái vận hành hoàn tất của 34 là như sau.

```text
- docs/project-knowledge/ tồn tại.
- Có thể tạo AI Context Pack.
- Có Glossary.
- Có Framework Constraints.
- Có Method Allowlist / Denylist.
- Có Known Good / Known Bad Examples.
- Có Review Pattern / Test Pattern.
- Có vận hành nâng cấp từ Failure Mode lên Knowledge.
- Có thể deprecate Knowledge cũ.
- Có tiêu chí nâng cấp lên CLAUDE.md / rules / prompts / checklist / CI.
- Có thể đưa vào AI context thông qua 31 chỉ những Knowledge tối thiểu cần thiết.
- Có thể quản lý status và độ tươi mới của Knowledge bằng 33.
```

---

---

## 27. Quy trình xây dựng ban đầu cho tri thức dự án

Khi đưa 34 vào dự án mới, không tạo Library hoàn hảo ngay từ đầu.  
Hãy tạo theo thứ tự dưới đây, ưu tiên những thứ có hiệu quả cao đối với độ chính xác của AI.

```text
1. glossary
2. architecture overview
3. allowed / forbidden methods
4. known good examples
5. input validation rules
6. error / message rules
7. security / permission rules
8. test data rules
9. review patterns
10. operation / logging rules
```

---

## 28. Cách trích xuất Knowledge từ dự án hiện có

```text
- Đọc PR review gần đây
- Đọc sự cố trong quá khứ
- Đọc lịch sử compile error
- Đọc lịch sử test failure
- Tập hợp các nội dung Tech Lead luôn nhắc
- Tập hợp các điểm người mới thường vướng
- Tập hợp những điểm AI lặp lại lỗi
- Chọn 3〜5 triển khai đúng hiện có
```

Prompt trích xuất:

```text
Hãy trích xuất tri thức cần đăng ký vào Project Knowledge Library từ PR review / ghi chép sự cố / test failure / ví dụ triển khai dưới đây.
Không dừng ở cảm tưởng đơn thuần; hãy chuyển thành Pattern / Anti-pattern / Rule / Test Pattern mà AI lần sau có thể dùng.
```

---

## 29. Độ chi tiết của Knowledge

Độ chi tiết xấu:

```text
- Viết chung chung “hãy chú ý chất lượng”
- Dán toàn bộ code
- Biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn
- Chứa secret hoặc dữ liệu thật
- Giữ lại biện pháp tạm thời cũ
```

Độ chi tiết tốt:

```text
- Nói rõ khi nào dùng
- Có Do / Do Not
- Có ví dụ đúng và ví dụ xấu
- Có phương pháp phát hiện
- Có thể kết nối tới test/review/CI
- Có owner và điều kiện cập nhật
```

---

## 30. Vận hành trong nhóm

### 30.1 Weekly Knowledge Triage

```text
Đầu vào:
- Failure Mode mới
- review findings
- test failures
- incidents
- AI mistakes

Đầu ra:
- Ứng viên Knowledge
- card cần cập nhật
- card cần deprecate
- Ứng viên CI hóa
- examples dùng cho đào tạo
```

### 30.2 Monthly Pattern Review

```text
- Failure Mode đang tái phát
- Knowledge không được đọc
- Rule có nhiều false positive
- Framework Constraints đã cũ
- Known Good mới cần chuẩn hóa
```

---

## 31. Lưu ý khi yêu cầu AI sử dụng Project Knowledge

```text
- Knowledge là hỗ trợ, không thay thế latest source
- Knowledge cũ sẽ dẫn dắt sai
- Không copy Known Good Example một cách thiếu phê phán
- Chỉ đưa mức tối thiểu cần thiết vào Context Pack
- Khi AI tham chiếu Knowledge, hãy ghi lại AI đã dùng Knowledge nào
```

---

## 32. Knowledge Usage Record

```md
# Knowledge Usage Record

## Ticket

## AI Context Pack

## Knowledge Used
| ID | Title | Why used | Impact |
|---|---|---|---|

## Knowledge Not Used
| ID | Reason |
|---|---|

## New Knowledge Candidate

## Problems
- stale:
- missing:
- conflicting:
```

---

## 33. Knowledge và đào tạo

Project Knowledge được dùng không chỉ cho AI mà còn cho đào tạo con người.

```text
- Onboarding thành viên mới
- Đào tạo góc nhìn review
- Đào tạo thiết kế test
- Đào tạo security
- Chia sẻ sự cố quá khứ
- Hiểu coding convention
```

Khi chuyển đổi sang tài liệu đào tạo:

```text
- Tóm tắt 1 trang
- So sánh ví dụ đúng / ví dụ sai
- Bài tập 5 phút
- Checklist
- FAQ
```

---

## 34. Tách biệt với Knowledge xuyên tổ chức

Không trộn Project Knowledge với Company-wide Knowledge.

```text
Project Knowledge:
- Đặc thù dự án
- Đặc thù framework
- Đặc thù khách hàng
- Đặc thù DB/màn hình/API

Company-wide Knowledge:
- Chuẩn toàn công ty
- Nguyên tắc security chung
- Góc nhìn review chung
- Vận hành SDD chung
```

Đánh giá nâng cấp:

```text
- Có hiệu quả ở 3 dự án trở lên
- Không chứa thông tin đặc thù khách hàng
- Có thể tổng quát hóa
- false positive thấp
- Xứng đáng với tải vận hành khi rule hóa toàn công ty
```

---

## 34-A. Những nội dung cần đưa lại từ Advanced Options nhóm 40 vào Knowledge

Tri thức thu được ở nhóm 40 không được dùng một lần rồi bỏ. Để nâng độ chính xác, an toàn và hiệu quả chi phí của AI trong lần sau, hãy đưa lại về 34 dưới dạng ứng viên nâng cấp.

| Advanced Option | Ứng viên Knowledge đưa lại về 34 |
|---|---|
| 41 | Cấu trúc repo, hotspot nguy hiểm, ràng buộc framework, Source Map đúng |
| 42 | Thiết kế vai trò Agent, prompt có hiệu quả, agent không cần thiết |
| 43 | Quy tắc ưu tiên tool evidence, quy tắc giảm false positive, Veto Rule |
| 44 | Context Pack hiệu quả trong giảm token, thiết kế Prompt Cache, pattern cấm nén |
| 45 | Quy tắc quyền MCP/hooks, tool bị cấm, điều kiện Human Approval |
| 46 | Code Map, RAG Query, Chunking, Compression rule đã hiệu quả |
| 47 | Quy tắc phán định PR Gate, quy tắc chất lượng review comment, Noise Control |
| 48 | Pattern migration phân tách an toàn, pattern song song hóa đã thất bại |
| 49 | KPI nên tiếp tục, chỉ số AI nên loại bỏ, Evaluation Dataset |

Tiêu chí nâng cấp về 34 không chỉ là “lần này hữu ích”.  
Chỉ nâng cấp những thứ có thể tái sử dụng trong lần sau, có thể phát hiện khi đã cũ, và con người có thể chịu trách nhiệm bảo trì.

## 35. Knowledge Debt

Knowledge cũ, trùng lặp hoặc mâu thuẫn là nợ.

```md
# Knowledge Debt Register

| ID | Debt Type | Description | Risk | Owner | Due |
|---|---|---|---|---|---|
```

Debt Type:

```text
stale
duplicate
conflicting
too_large
too_vague
unsafe
not_used
missing_example
missing_owner
```

## Tài liệu chuẩn và tài liệu công khai đã tham khảo

Pack này tái cấu trúc các tư tưởng của các tiêu chuẩn và tài liệu công khai dưới đây theo ngữ cảnh SDD.  
Các tiêu chuẩn bên ngoài không phải là đối tượng để copy-paste nguyên văn; cần điều chỉnh độ sâu áp dụng theo quy định nội bộ, đặc thù dự án, yêu cầu khách hàng và pháp quy.

| Lĩnh vực | Nguồn tham khảo | Cách dùng trong SDD |
|---|---|---|
| Vận hành AI Agent | Everything Claude Code | Đưa có chọn lọc các tư tưởng về skills / rules / hooks / MCP / memory optimization / continuous learning / security scanning / research-first development theo cách an toàn. |
| Secure SDLC | NIST SP 800-218 SSDF | Làm nền tảng cho Phase 0-A, thiết kế an toàn, phòng tái phát lỗ hổng, evidence và CI security. |
| AI Risk | NIST AI RMF | Xử lý rủi ro phát triển có AI hỗ trợ theo vòng lặp Govern / Map / Measure / Manage. |
| LLM Security | OWASP Top 10 for LLM Applications 2025 | Dùng để phòng Prompt Injection, Sensitive Information Disclosure, Excessive Agency, v.v. khi đọc tài liệu ngoài, log, Issue, Web page. |
| Application Security | OWASP ASVS | Làm đường dẫn phụ trợ cho yêu cầu security, góc nhìn review và góc nhìn test của Web/API. |
| Supply Chain | SLSA / OpenSSF | Làm đường dẫn phụ trợ khi xem xét build, dependency, artifact sinh ra, CI/CD, evidence, signature, chống giả mạo. |
| SBOM | CycloneDX / SPDX | Dùng để biểu diễn dependency, component, AI/ML BOM, vulnerability, license và supply-chain risk. |
| Provenance | W3C PROV | Dùng như tư tưởng để xử lý nguồn gốc, người/tác nhân tạo, căn cứ, quan hệ phái sinh và đánh giá độ tin cậy của artifact. |
| Delivery Metrics | DORA | Làm chỉ số phụ trợ để đo tốc độ, độ ổn định và khả năng phục hồi sau khi đưa SDD vào. |
| Operations Learning | Google SRE Postmortem | Xem Failure Mode, Near Miss, Postmortem là học tập tổ chức chứ không phải quy trách nhiệm cá nhân. |
| Observability | OpenTelemetry | Kết nối tư tưởng trace / metric / log / baggage / context propagation với vận hành, giám sát và điều tra xuyên hệ thống. |


---

# Appendix. Dành cho người mới: Quy trình thực thi và prompt copy-paste của pack này

> Appendix này là “lớp bọc thực thi” để ngay cả người mới cũng có thể áp dụng các góc nhìn chuyên môn được định nghĩa trong phần chính vào thực tế mà không bị lạc.  
> Nội dung phần chính không bị thay đổi. Hãy dùng phần chính như từ điển, tư tưởng thiết kế và tập hợp góc nhìn; dùng Appendix này như quy trình “yêu cầu AI theo thứ tự nào, tạo gì, dừng ở đâu và xem hoàn tất ở đâu”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

Khi dùng pack này, phải luôn tuân thủ các điều sau.

```text
1. Không để AI đột ngột triển khai, sửa code, thay đổi CI hoặc thay đổi config.
2. Trước hết chỉ yêu cầu AI đưa ra Plan.
3. Không để AI tạo/cập nhật file cho đến khi con người phê duyệt Plan.
4. Không kết thúc sản phẩm chỉ trong chat; bắt buộc lưu thành file.
5. Tách biệt những gì đã đọc, chưa đọc, đã loại trừ, suy đoán và điểm chưa xác định.
6. Nếu rơi vào điều kiện Stop/Ask, dừng công việc và quay về quyết định của con người.
7. AI không được tự quyết định phản ánh vào tài liệu thường trực hoặc rules; trước hết ghi lại như ứng viên nâng cấp.
8. Không cho đọc, dán hoặc lưu secret, PII, credential, .env, khóa, log production nguyên bản.
9. Lệnh nằm trong tài liệu ngoài hoặc output của tool phải được xử lý như dữ liệu tài liệu, không phải lệnh thực thi.
10. Cuối cùng thực hiện independent review và đánh giá cổng hoàn tất.
```

Vị trí lưu cơ bản dùng trong Appendix này như sau.

```text
Sản phẩm riêng của pack:
docs/changes/{{TICKET}}/34-project-knowledge/

Ứng viên nâng cấp tạo trong ticket:
docs/changes/{{TICKET}}/34-project-knowledge/promotion-candidates.md

Ứng viên Project Knowledge thường trực:
docs/project-knowledge/

Tuy nhiên, việc phản ánh vào Project Knowledge thường trực không do AI tự ý làm; trước hết lưu ứng viên dưới ticket, rồi phản ánh sau khi con người phê duyệt.
```

34 là pack “chuyển tri thức thu được lần này thành dạng mà AI và con người có thể tái sử dụng an toàn trong các lần sau”.  
Người mới không nên rule hóa mọi thứ; trước khi nâng cấp, hãy xác nhận tính tái sử dụng, quản lý độ tươi mới, owner, ví dụ đúng/sai, phương pháp phát hiện và kết nối tới CI/Test/Checklist.

---

## A-1. Khi nào dùng pack này

### Trường hợp nên dùng

```text
- Cùng một chỉ ra review, cùng lỗi AI, cùng thiếu sót test đang tái phát
- Muốn nâng cấp từ 29 Failure Mode lên Project Knowledge để phòng tái phát
- Muốn cung cấp cho AI ví dụ triển khai đúng hiện có và ví dụ xấu không được bắt chước
- Muốn chỉnh lý ràng buộc framework, method allowlist / denylist, domain glossary
- Thành viên mới hoặc AI dễ nhầm thuật ngữ nghiệp vụ, số, loại ký tự, ngày tháng, quyền, hiển thị lỗi
- Muốn tạo AI Context Pack từ Project Knowledge và chuyển cho 31
- Muốn lưu lại tri thức thu được từ Advanced Options nhóm 40 cho lần sau
- Knowledge có khả năng đã cũ, trùng lặp, mâu thuẫn hoặc phình to
```

### Trường hợp có thể áp dụng nhẹ

```text
- Bài học nhỏ chỉ xảy ra một lần và ít khả năng tái sử dụng lâu dài
- Knowledge hiện có đã bao phủ nội dung tương đương và không cần cập nhật
- Ghi lại dưới dạng 29 Failure Mode, nhưng căn cứ để Knowledge hóa vẫn còn yếu
- Thay đổi nhỏ M1, không ảnh hưởng đến Project Knowledge
```

Dù áp dụng nhẹ, tối thiểu vẫn cần lưu các điểm sau.

```text
- Có đưa vào ứng viên Knowledge hay không
- Lý do không nâng cấp
- Có trùng với Knowledge hiện có hay không
- Có cần đưa vào 31 AI Context Pack hay không
```

### Trường hợp không dùng, hoặc cần quay về pack khác trước

```text
- Chưa phân tích thất bại/tái phát, trước hết cần 29 Failure Mode
- Chưa chỉnh lý ranh giới Context cho AI đọc, trước hết cần 31
- Status hoặc độ tươi mới của artifact chưa rõ, trước hết cần 33
- Spec hoặc ví dụ triển khai có secret/PII và chưa trừu tượng hóa an toàn
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 34
{{PACK_NAME}}: Project Knowledge and Pattern Library Pack
{{PACK_SLUG}}: project-knowledge
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{KNOWLEDGE_SOURCE}}:
{{KNOWLEDGE_PURPOSE}}:
{{TARGET_CONTEXT_USE}}:
```

Ví dụ điền:

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{RISK_LEVEL}}: Medium
{{SDD_MODE}}: M3
{{TIMEBOX}}: Tới khi trích xuất ứng viên Knowledge và draft AI Context Pack
{{KNOWLEDGE_SOURCE}}: Chỉ ra Codex review, test failure, triển khai đúng hiện có, Failure Mode Entry
{{KNOWLEDGE_PURPOSE}}: Giúp AI lần sau không sai về quyền và input validation của email mời
{{TARGET_CONTEXT_USE}}: Chuyển qua 31 trước Phase 3 impl plan và Phase 5 review
```

---

## A-3. Đầu vào đầu tiên cần cho AI đọc

### Đầu vào chung cần đọc

```text
@docs/changes/{{TICKET}}/sources.md
@docs/changes/{{TICKET}}/spec-pack.md
@docs/changes/{{TICKET}}/impact-analysis.md
@docs/changes/{{TICKET}}/impl-plan.md
@docs/changes/{{TICKET}}/review-checklist.md
@docs/changes/{{TICKET}}/self-review.md
@docs/changes/{{TICKET}}/test-plan.md
@docs/changes/{{TICKET}}/test-results.md
@docs/changes/{{TICKET}}/report.md
@docs/architecture/
@docs/standards/
@.claude/CLAUDE.md
@.claude/rules/
```

### Đầu vào đặc biệt cần đọc trong pack này

```text
@docs/changes/{{TICKET}}/29-failure-mode-learning/failure-mode-candidates.md
@docs/changes/{{TICKET}}/29-failure-mode-learning/failure-mode-index.md
@docs/changes/{{TICKET}}/24-review-testcode/independent-review.md
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-inventory.md
@docs/changes/{{TICKET}}/33-artifact-governance/traceability-matrix.md
@docs/changes/{{TICKET}}/31-context-loading/context-manifest.md
@docs/changes/{{TICKET}}/32-strategic-compact/decision-ledger.md
docs/project-knowledge/ hiện có
Chỉ ra PR review gần đây
Sự cố / near miss / postmortem gần đây
Ví dụ triển khai đúng hiện có
Ví dụ triển khai sai hoặc ví dụ bị trả lại
Lịch sử test failure
Lịch sử compile error
```

### Những thứ không cho đọc hoặc chỉ chuyển sau khi trừu tượng hóa

```text
- Ví dụ thật có secret, PII hoặc thông tin cá nhân của khách hàng
- Log production nguyên bản
- Nâng cấp nguyên văn thông tin đặc thù khách hàng thành Company-wide Knowledge
- Xem biện pháp tạm thời chỉ xảy ra một lần là rule vĩnh viễn
- Xem ràng buộc framework cũ là đúng mới nhất
- Dán toàn bộ code dài làm Known Good
```

---

## A-4. Sản phẩm cần tạo/cập nhật

### Thư mục riêng của pack

```text
docs/changes/{{TICKET}}/34-project-knowledge/
```

### Sản phẩm tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/34-project-knowledge/knowledge-candidates.md
docs/changes/{{TICKET}}/34-project-knowledge/ai-context-pack.md
docs/changes/{{TICKET}}/34-project-knowledge/knowledge-usage-record.md
docs/changes/{{TICKET}}/34-project-knowledge/knowledge-review.md
docs/changes/{{TICKET}}/34-project-knowledge/promotion-candidates.md
```

### Sản phẩm tạo khi cần

```text
docs/changes/{{TICKET}}/34-project-knowledge/knowledge-card-drafts.md
docs/changes/{{TICKET}}/34-project-knowledge/pattern-card-drafts.md
docs/changes/{{TICKET}}/34-project-knowledge/anti-pattern-card-drafts.md
docs/changes/{{TICKET}}/34-project-knowledge/known-good-examples.md
docs/changes/{{TICKET}}/34-project-knowledge/known-bad-examples.md
docs/changes/{{TICKET}}/34-project-knowledge/framework-constraints.md
docs/changes/{{TICKET}}/34-project-knowledge/method-allowlist-denylist.md
docs/changes/{{TICKET}}/34-project-knowledge/domain-glossary-update.md
docs/changes/{{TICKET}}/34-project-knowledge/review-pattern-candidates.md
docs/changes/{{TICKET}}/34-project-knowledge/test-pattern-candidates.md
docs/changes/{{TICKET}}/34-project-knowledge/knowledge-freshness-review.md
docs/changes/{{TICKET}}/34-project-knowledge/knowledge-debt-register.md
```

### Điểm ứng viên phản ánh thường trực

```text
docs/project-knowledge/glossary.md
docs/project-knowledge/framework-constraints.md
docs/project-knowledge/method-allowlist.md
docs/project-knowledge/method-denylist.md
docs/project-knowledge/known-good/
docs/project-knowledge/known-bad/
docs/project-knowledge/patterns/
docs/project-knowledge/anti-patterns/
docs/project-knowledge/review-patterns/
docs/project-knowledge/test-patterns/
```

Tuy nhiên, việc thường trực hóa chỉ được thực hiện sau khi con người phê duyệt.

---

## A-5. Quy trình thực thi dành cho người mới

### Step 1. Trích xuất ứng viên Knowledge

Từ đầu vào, phân loại và đưa ra ứng viên theo các nhóm sau.

```text
- Glossary
- Framework Constraint
- Method Allowlist / Denylist
- Known Good Example
- Known Bad Example
- Pattern
- Anti-pattern
- Review Pattern
- Test Pattern
- Security / Permission Rule
- Operation / Logging Rule
- AI Prompt Snippet
- CI/Test Candidate
```

### Step 2. Đánh giá có nên đăng ký hay không

Chỉ đưa vào ứng viên Knowledge những nội dung thỏa các điều sau.

```text
- Có thể tái sử dụng trong lần sau
- Rõ khi nào dùng
- Có Do / Do Not
- Có ví dụ đúng hoặc ví dụ sai
- Có phương pháp phát hiện
- Có thể đặt owner và điều kiện tái xác nhận
- Có thể phát hiện khi đã cũ
- Không chứa secret/PII
```

### Step 3. Tạo draft Card

Chuyển thành Knowledge Card, Pattern Card hoặc Anti-pattern Card. Không dừng ở ghi chú đơn thuần; tạo thành dạng AI có thể dùng lần sau.

### Step 4. Tạo AI Context Pack

Không cho AI đọc toàn bộ Knowledge; chỉ tóm tắt mức tối thiểu cần thiết cho task hiện tại vào `ai-context-pack.md`.  
Pack này sẽ được chuyển cho 31.

### Step 5. Lưu Knowledge Usage Record

Ghi lại AI đã dùng Knowledge nào, không dùng cái nào, có ứng viên mới nào phát sinh.

### Step 6. Xác nhận Freshness và Debt

Ghi lại Knowledge cũ, trùng lặp, mâu thuẫn, quá lớn, mơ hồ, unsafe, not used vào `knowledge-debt-register.md`.

### Step 7. Chỉ thường trực hóa sau khi con người phê duyệt

AI chỉ tạo tới `promotion-candidates.md`. Việc phản ánh vào `docs/project-knowledge/` được thực hiện sau khi con người phê duyệt.

---

## A-6. Prompt dùng để copy-paste: Prompt bắt đầu chỉ lập Plan

```text
Bạn là Project Knowledge Curator của SDD Ver.04.
Từ bây giờ sẽ áp dụng 34_Project Knowledge and Pattern Library Pack cho {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không được đột ngột cập nhật Knowledge thường trực, CLAUDE.md, rules, CI, checklist.
- Trước hết chỉ đưa ra Plan.
- Không được tạo/cập nhật file cho đến khi tôi phê duyệt Plan.
- Không đưa secret, PII, thông tin cá nhân khách hàng, log production nguyên bản vào Knowledge.
- Không biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn.
- Knowledge không phải là thứ thay thế latest source. Luôn tách điều kiện áp dụng, Do / Do Not, Evidence, Owner, Re-review Trigger.
- Không giả định sẽ copy Known Good Example một cách thiếu phê phán.
- Đề xuất lưu sản phẩm trong docs/changes/{{TICKET}}/34-project-knowledge/.
- Thường trực hóa được ghi vào promotion-candidates.md làm ứng viên, sau đó thực hiện sau khi con người phê duyệt.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Knowledge Source: {{KNOWLEDGE_SOURCE}}
- Knowledge Purpose: {{KNOWLEDGE_PURPOSE}}
- Target Context Use: {{TARGET_CONTEXT_USE}}

【Plan bắt buộc phải bao gồm】
1. Có cần áp dụng 34 hay không
2. Knowledge source sẽ đọc
3. Source không đọc / loại trừ
4. Cách phân loại ứng viên Knowledge
5. Cách đánh giá ứng viên không nên nâng cấp
6. Sản phẩm sẽ tạo/cập nhật và nơi lưu
7. Cách tạo AI Context Pack
8. Cách tạo Knowledge Usage Record
9. Nội dung chuyển cho 31 Context Loading
10. Nội dung đăng ký vào 33 Artifact Inventory
11. Ứng viên thường trực hóa và điểm cần con người phê duyệt
12. Điều kiện Stop/Ask

Trước hết chỉ đưa ra Plan. Chưa chỉnh sửa file.
```

---

## A-7. Checklist xác nhận Plan

```text
- [ ] Không định cập nhật Knowledge thường trực ngay lập tức
- [ ] Có kế hoạch tách ứng viên Knowledge và ứng viên không nâng cấp
- [ ] Loại trừ secret, PII, thông tin khách hàng, log production nguyên bản
- [ ] Có tiền đề không biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn
- [ ] Có kế hoạch đưa Evidence, Owner, Re-review Trigger
- [ ] Có tiền đề không copy Known Good / Known Bad một cách thiếu phê phán
- [ ] Có kế hoạch tối thiểu hóa AI Context Pack
- [ ] Có đường dẫn chuyển sang 31
- [ ] Có đường dẫn quản lý status và độ tươi mới bằng 33
- [ ] Điều kiện Stop/Ask được nêu rõ
```

---

## A-8. Prompt dùng để copy-paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật sản phẩm của 34_Project Knowledge and Pattern Library Pack theo đúng quy trình đã đề xuất.

【Quy tắc thực thi】
- Trước hết hãy tạo knowledge-candidates.md.
- Với từng ứng viên, ghi Category, Evidence, điều kiện tái sử dụng, có nâng cấp hay không, ứng viên đích nâng cấp.
- Với ứng viên không nâng cấp, ghi lý do không nâng cấp.
- Khi cần, tạo draft Knowledge Card / Pattern Card / Anti-pattern Card.
- Known Good / Known Bad không được biểu diễn bằng toàn bộ code, mà bằng ý chính, path tham chiếu, điều kiện áp dụng và lưu ý.
- Nội dung cho AI đọc hãy tóm tắt ở mức tối thiểu cần thiết trong ai-context-pack.md.
- AI đã dùng gì thì ghi vào knowledge-usage-record.md.
- Ứng viên thường trực hóa hãy tổng hợp trong promotion-candidates.md; không cập nhật trực tiếp docs/project-knowledge/.
- Nếu có Knowledge cũ, trùng lặp, mâu thuẫn, quá lớn hoặc unsafe, hãy ghi vào knowledge-debt-register.md.
- Sau khi làm xong, tự đánh giá cổng hoàn tất.
```

---

## A-9. Prompt dùng để copy-paste: Prompt review sản phẩm và đánh giá hoàn tất

```text
Bạn là independent reviewer của SDD Ver.04.
Hãy review các sản phẩm 34_Project Knowledge and Pattern Library Pack dưới đây và đánh giá pack này có thể hoàn tất hay chưa.

【Đối tượng review】
@docs/changes/{{TICKET}}/34-project-knowledge/knowledge-candidates.md
@docs/changes/{{TICKET}}/34-project-knowledge/knowledge-card-drafts.md
@docs/changes/{{TICKET}}/34-project-knowledge/pattern-card-drafts.md
@docs/changes/{{TICKET}}/34-project-knowledge/anti-pattern-card-drafts.md
@docs/changes/{{TICKET}}/34-project-knowledge/known-good-examples.md
@docs/changes/{{TICKET}}/34-project-knowledge/known-bad-examples.md
@docs/changes/{{TICKET}}/34-project-knowledge/ai-context-pack.md
@docs/changes/{{TICKET}}/34-project-knowledge/knowledge-usage-record.md
@docs/changes/{{TICKET}}/34-project-knowledge/promotion-candidates.md
@docs/changes/{{TICKET}}/34-project-knowledge/knowledge-debt-register.md
@docs/changes/{{TICKET}}/34-project-knowledge/knowledge-review.md

Nếu file không tồn tại, hãy xử lý là “không tồn tại” và đánh giá có cần thiết hay không.

【Góc nhìn review】
1. Ứng viên Knowledge có ở độ chi tiết tái sử dụng được không
2. Có biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn không
3. Có chứa secret, PII, thông tin đặc thù khách hàng, log production nguyên bản không
4. Có Evidence, Owner, Last Reviewed, Re-review Trigger không
5. Có Do / Do Not, Known Good, Known Bad, phương pháp phát hiện không
6. AI Context Pack có tối thiểu cần thiết không
7. Knowledge có bị xem như thay thế latest source không
8. Knowledge cũ, trùng lặp, mâu thuẫn, quá lớn có được xử lý như Debt không
9. Có đường dẫn chuyển cho 31 không
10. Có thể quản lý status và độ tươi mới bằng 33 không
11. Việc thường trực hóa có điểm phê duyệt của con người không

【Định dạng output】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Unsafe knowledge risks
- Stale / duplicate / conflicting knowledge
- Over-generalization risks
- Missing evidence / owner / review trigger
- Required human decisions
- Promotion candidates review
- Final completion gate checklist
- Next action
```

---

## A-10. Prompt dùng để copy-paste: Prompt trả lại để sửa

```text
Dựa trên các chỉ ra review dưới đây, hãy sửa các sản phẩm của 34_Project Knowledge and Pattern Library Pack.

【Quy tắc sửa】
- Trước khi bắt tay, hãy diễn giải ý định của chỉ ra trong 1 dòng.
- Liệt kê trước các sản phẩm bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Cấm sửa theo hướng đưa secret, PII, thông tin cá nhân khách hàng, log production nguyên bản vào Knowledge.
- Không biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn; nếu cần, hãy đưa lại về Failure Mode hoặc memo tạm thời.
- Ứng viên thường trực hóa chỉ dừng ở promotion-candidates.md.
- Hãy giảm AI Context Pack xuống mức tối thiểu cần thiết.
- Sau khi sửa, ghi kết quả xử lý vào knowledge-review.md.

【Chỉ ra review】
Dán chỉ ra vào đây
```

---

## A-11. Điều kiện Stop/Ask

```text
- Ứng viên Knowledge chứa secret, PII, thông tin cá nhân khách hàng, log production nguyên bản
- Đang cố biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn
- Đang cố nâng cấp thông tin đặc thù khách hàng thành Company-wide Knowledge
- Không thể đặt owner hoặc điều kiện tái xác nhận
- Không có Evidence, gần giống cảm tưởng cá nhân
- Có khả năng mâu thuẫn với latest source
- Đang xem framework constraint cũ là mới nhất
- Đang cố cho AI copy Known Good Example thiếu phê phán
- Knowledge quá dài khiến AI Context Pack phình to
- Đang cố đưa thông tin mà 31 phải loại trừ vào AI Context Pack
- Đang dùng Knowledge có trạng thái Deprecated / Superseded trong 33
- Đang cố phản ánh trực tiếp vào CLAUDE.md hoặc rules mà chưa có con người phê duyệt
```

---

## A-12. Cổng hoàn tất

```text
- [ ] knowledge-candidates.md đã được tạo
- [ ] Mỗi ứng viên có Category, Evidence, điều kiện tái sử dụng, quyết định có nâng cấp hay không
- [ ] Lý do không nâng cấp được ghi lại
- [ ] Có draft Knowledge Card / Pattern Card / Anti-pattern Card cần thiết
- [ ] Đã đánh giá có cần cập nhật Glossary / Framework Constraints / Method Allowlist / Denylist hay không
- [ ] Ứng viên Known Good / Known Bad được trừu tượng hóa an toàn
- [ ] ai-context-pack.md được tạo ở mức tối thiểu cần thiết
- [ ] knowledge-usage-record.md tồn tại
- [ ] Ứng viên thường trực hóa được tách vào promotion-candidates.md
- [ ] Không chứa secret, PII, log production nguyên bản
- [ ] Đã cân nhắc owner, Last Reviewed, Re-review Trigger
- [ ] Knowledge cũ, trùng lặp, mâu thuẫn, quá lớn được xử lý như Debt
- [ ] Có đường dẫn chuyển cho 31
- [ ] Có thể quản lý status và độ tươi mới bằng 33
- [ ] Đã review và không còn Blocker
```

---

## A-13. Điểm cần đi tiếp

```text
- Chuyển Knowledge tối thiểu cho AI đọc → quay về 31 Context Loading
- Quản lý status và độ tươi mới của Knowledge → đăng ký vào 33 Artifact Governance
- Cần phân tích gốc của rule phòng tái phát → quay về 29 Failure Mode
- Dùng cho impl plan từ Phase 3 trở đi → phản ánh vào impl-plan / review-checklist / test-plan
- Thường trực hóa → sau khi con người phê duyệt, phản ánh vào docs/project-knowledge/
- Đo đánh giá, tỷ lệ sử dụng, tỷ lệ tái phát → chuyển cho 49 Evaluation / Observability
- Có tri thức từ Advanced Option → liên kết với sản phẩm của pack tương ứng trong nhóm 40
```

---

## A-14. Lỗi người mới thường mắc và cách phòng tránh

| Lỗi | Nguy hiểm ở đâu | Cách phòng tránh |
|---|---|---|
| Knowledge hóa mọi thứ | Rule phình to và không ai tuân thủ | Xác nhận điều kiện tái sử dụng và owner |
| Biến tình huống chỉ xảy ra một lần thành rule vĩnh viễn | Dẫn dắt sai AI lần sau | Ghi lý do không nâng cấp |
| Cho copy Known Good nguyên xi | Dẫn đến copy implementation sai ngữ cảnh | Thêm điều kiện áp dụng và Do Not |
| Giữ Knowledge cũ | Gây triển khai sai | Đặt Re-review Trigger và quản lý Debt |
| Đưa secret/PII vào ví dụ | Gây rò rỉ thông tin | Dùng trừu tượng hóa, mask, ví dụ tổng hợp |
| Đưa toàn bộ vào AI Context Pack | Context quá tải, làm chìm điểm quan trọng | Chỉ chuyển tối thiểu cần thiết cho 31 |
| AI cập nhật trực tiếp rule thường trực | Rule chưa được phê duyệt bị lan rộng | Dừng ở promotion-candidates.md |

---

## A-15. Lộ trình ngắn nhất

```text
1. Dán prompt bắt đầu
2. Trích xuất ứng viên từ Failure Mode / review / test failure / good example
3. Tách nội dung Knowledge hóa và không Knowledge hóa
4. Tạo draft Knowledge Card / Pattern Card / Anti-pattern Card
5. Tạo ai-context-pack.md ở mức tối thiểu cần thiết
6. Lưu knowledge-usage-record.md
7. Tách ứng viên thường trực hóa vào promotion-candidates.md
8. Đánh giá hoàn tất bằng knowledge-review.md
```
