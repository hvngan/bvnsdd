**Mục lục**
- [32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Vietnamese](#32_sdd_long-context-and-strategic-compact_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Kết luận](#1-kết-luận)
  - [2. Khác biệt so với 31](#2-khác-biệt-so-với-31)
  - [3. Tư tưởng cơ bản của Strategic Compact](#3-tư-tưởng-cơ-bản-của-strategic-compact)
  - [4. Thời điểm cần Compact](#4-thời-điểm-cần-compact)
  - [5. Strategic Compact Snapshot](#5-strategic-compact-snapshot)
  - [6. Session Handoff Pack](#6-session-handoff-pack)
  - [7. Resume Pack](#7-resume-pack)
  - [8. Decision Ledger](#8-decision-ledger)
  - [9. Work State Board](#9-work-state-board)
  - [10. Changed Files Summary](#10-changed-files-summary)
  - [11. Handoff giữa nhiều AI](#11-handoff-giữa-nhiều-ai)
  - [12. Chia nhỏ Source Analysis dài hạn](#12-chia-nhỏ-source-analysis-dài-hạn)
  - [13. Strategic Compact cho dự án tách FE/BE](#13-strategic-compact-cho-dự-án-tách-febe)
  - [14. Strategic Compact cho dự án Microservice / MultiRepo](#14-strategic-compact-cho-dự-án-microservice--multirepo)
  - [15. Quy trình tiếp tục sau Compact](#15-quy-trình-tiếp-tục-sau-compact)
  - [16. Long Context Safety Checklist](#16-long-context-safety-checklist)
  - [17. Prompt chuyên dụng cho 32](#17-prompt-chuyên-dụng-cho-32)
  - [18. Metrics](#18-metrics)
  - [19. Failure Mode tiêu biểu](#19-failure-mode-tiêu-biểu)
  - [20. Definition of Done](#20-definition-of-done)
  - [21. Độ chi tiết của Strategic Compact](#21-độ-chi-tiết-của-strategic-compact)
  - [22. Kỹ thuật nén Context](#22-kỹ-thuật-nén-context)
  - [23. Tích hợp nhiều review](#23-tích-hợp-nhiều-review)
  - [24. Ứng phó Long Context Incident](#24-ứng-phó-long-context-incident)
  - [25. Emergency Snapshot khi công việc bị gián đoạn](#25-emergency-snapshot-khi-công-việc-bị-gián-đoạn)
  - [25-A. Kết nối với Advanced Options nhóm 40](#25-a-kết-nối-với-advanced-options-nhóm-40)
  - [26. Multi-Agent Orchestration Board](#26-multi-agent-orchestration-board)
  - [Tài liệu tham khảo / chuẩn công khai đã tham chiếu](#tài-liệu-tham-khảo--chuẩn-công-khai-đã-tham-chiếu)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt có thể copy-paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-có-thể-copy-paste)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input cần cho AI đọc đầu tiên](#a-3-input-cần-cho-ai-đọc-đầu-tiên)
  - [A-4. Thành quả cần tạo / cập nhật](#a-4-thành-quả-cần-tạo--cập-nhật)
  - [A-5. Quy trình thực hiện dành cho người mới](#a-5-quy-trình-thực-hiện-dành-cho-người-mới)
  - [A-6. Dùng để copy-paste: Prompt bắt đầu chỉ lập Plan](#a-6-dùng-để-copy-paste-prompt-bắt-đầu-chỉ-lập-plan)
  - [A-7. Checklist xác nhận Plan](#a-7-checklist-xác-nhận-plan)
  - [A-8. Dùng để copy-paste: Prompt phê duyệt Plan](#a-8-dùng-để-copy-paste-prompt-phê-duyệt-plan)
  - [A-9. Dùng để copy-paste: Prompt review thành quả và phán định hoàn tất](#a-9-dùng-để-copy-paste-prompt-review-thành-quả-và-phán-định-hoàn-tất)
  - [A-10. Dùng để copy-paste: Prompt trả về sửa](#a-10-dùng-để-copy-paste-prompt-trả-về-sửa)
  - [A-11. Điều kiện Stop/Ask](#a-11-điều-kiện-stopask)
  - [A-12. Cổng hoàn tất](#a-12-cổng-hoàn-tất)
  - [A-13. Bước tiếp theo](#a-13-bước-tiếp-theo)
  - [A-14. Lỗi người mới hay gặp và cách phòng tránh](#a-14-lỗi-người-mới-hay-gặp-và-cách-phòng-tránh)
  - [A-15. Lộ trình ngắn nhất](#a-15-lộ-trình-ngắn-nhất)

# 32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Vietnamese

Ngày tạo: 2026-05-16  
Đối tượng: Các dự án SDD thực hiện trong thời gian dài, quy mô lớn, nhiều ngày, nhiều AI hoặc nhiều người phụ trách  
Kết nối tới: 21,22,23,27,28,29,31,33,34,42,44,48,49

---

## 0. Vai trò của tài liệu này

Tài liệu này là tiêu chuẩn để khi vận hành SDD trong thời gian dài hoặc ở quy mô lớn, AI và con người **không đánh mất tiền đề, quyết định, tiến độ và các vấn đề chưa giải quyết**.

Trong phát triển do AI hỗ trợ, nếu chỉ là một task ngắn thì có thể tiến hành chỉ bằng chat.  
Tuy nhiên, với các dự án như dưới đây, chỉ dựa vào chat sẽ dễ đổ vỡ.

```text
- Triển khai kéo dài nhiều ngày
- Phân tích source quy mô lớn
- FE/BE tách biệt và có nhiều người phụ trách
- Microservice / MultiRepo / nhiều Tech Stack
- Review bởi nhiều AI
- Review nhiều tầng Claude → Codex → Human
- Lặp đi lặp lại triển khai, test, review, sửa
- Phát sinh context compact
- Người thực hiện thay đổi
- Tiếp tục lại vào ngày khác
```

Tài liệu này không để “trí nhớ” của AI phụ thuộc vào chat, mà quản lý nó như **trí nhớ đã được artifact hóa**.

---

## 1. Kết luận

Trong SDD dài hạn, bắt buộc thực hiện các việc sau.

```text
1. Tiền đề quan trọng phải lưu trong artifact, không chỉ lưu trong chat.
2. Trước khi compact, tạo Strategic Compact Snapshot.
3. Sau khi compact, đối chiếu Snapshot và artifact rồi mới tiếp tục.
4. Quyết định phải lưu vào Decision Ledger.
5. Vấn đề chưa xác định phải lưu vào Open Questions.
6. Source đã đọc phải được kế thừa từ Context Manifest.
7. File đã thay đổi và việc chưa hoàn tất phải được quản lý bằng Work State Board.
8. Khi review bằng nhiều AI, phải tạo Handoff Pack.
9. Quản lý bản chuẩn và độ mới của artifact bằng 33.
10. Lỗi, mất trí nhớ, thiếu sót khi handoff phải đăng ký vào 29 và tri thức hóa vào 34.
```

---

## 2. Khác biệt so với 31

| File | Mối quan tâm chính |
|---|---|
| 31 | Đưa gì vào context, không đưa gì vào context |
| 32 | Làm thế nào để không đánh mất context và phán đoán đó sau thời gian dài, handoff hoặc compact |

31 là “kiểm soát input”.  
32 là “kiểm soát trí nhớ, bàn giao và tái khởi động”.

---

## 3. Tư tưởng cơ bản của Strategic Compact

Strategic Compact là hành động nén các thông tin quan trọng một cách ngắn gọn, chính xác và có thể tiếp tục lại được khi phiên AI hoặc công việc đã kéo dài.

Compact xấu chỉ là một bản tóm tắt sơ sài.  
Compact tốt là **trạng thái công việc mà người tiếp theo có thể tiếp tục an toàn**.

### 3.1 Compact xấu

```text
- Chỉ viết “đang triển khai đại khái”
- Quyết định và phỏng đoán bị trộn lẫn
- Không rõ đã đọc gì
- Không rõ còn gì chưa xác nhận
- Bỏ sót quyết định của con người
- Không rõ file đã thay đổi
- Chưa test nhưng coi như đã hoàn tất
```

### 3.2 Compact tốt

```text
- Mục tiêu hiện tại rõ ràng
- Phase hiện tại rõ ràng
- Quyết định cuối cùng của con người rõ ràng
- File đã đọc và file chưa đọc rõ ràng
- File đã thay đổi rõ ràng
- Task chưa hoàn tất rõ ràng
- Điều kiện Stop rõ ràng
- Việc tiếp theo cần làm rõ ràng
- Trạng thái cập nhật artifact rõ ràng
```

---

## 4. Thời điểm cần Compact

```text
- Session đã kéo dài
- AI bắt đầu quên tiền đề
- Đã phát sinh nhiều quyết định quan trọng
- Chuyển qua Phase khác
- Chuyển từ triển khai sang review
- Bàn giao từ Claude sang Codex
- Bàn giao từ AI sang con người review
- Tiếp tục công việc vào ngày hôm sau
- Công việc lan sang nhiều Repo / nhiều service
- Đã đọc nhiều source và căn cứ quan trọng bị phân tán
- Có dấu hiệu compact tự động sắp xảy ra
```

---

## 5. Strategic Compact Snapshot

Với Standard trở lên, hoặc công việc kéo dài, hãy tạo nội dung sau.

```md
# Strategic Compact Snapshot

## 1. Snapshot Metadata
- Ticket:
- Mode:
- Current Phase:
- Created at:
- Created by:
- Target next user / AI:
- Related artifacts:

## 2. Current Objective
-

## 3. Must Not Forget
- Chỉ thị quan trọng con người đã nêu rõ:
- Những việc tuyệt đối không được làm:
- Phạm vi không được thay đổi:
- Spec cần ưu tiên:
- Phán đoán đã được phê duyệt:

## 4. Current State
- Completed:
- In progress:
- Not started:
- Blocked:

## 5. Source Files Read
| Path | Why read | Key finding | Confidence |
|---|---|---|---|

## 6. Source Files Not Yet Read
| Path / area | Why needed | Risk if not read |
|---|---|---|

## 7. Decisions
| Decision | Who decided | Evidence | Impact | Reversible? |
|---|---|---|---|---|

## 8. Assumptions
| Assumption | Why assumed | Risk | Verification plan |
|---|---|---|---|

## 9. Changed Files
| File | Change summary | Status | Needs review |
|---|---|---|---|

## 10. Tests
- Tests planned:
- Tests run:
- Tests failed:
- Tests deferred:
- Reason for deferral:

## 11. Risks / Accepted Risks
-

## 12. Open Questions
-

## 13. Artifacts Updated
| Artifact | Status | Notes |
|---|---|---|

## 14. Artifacts Not Yet Updated
| Artifact | Required update | Risk |
|---|---|---|

## 15. Next Recommended Step
1.
2.
3.

## 16. Stop Conditions
-
```

---

## 6. Session Handoff Pack

Khi có nhiều AI, nhiều người phụ trách, hoặc tiếp tục vào ngày hôm sau, ngoài Snapshot hãy tạo Handoff Pack.

```md
# Session Handoff Pack

## 1. Recipient
- Human / AI / Role:
- Expected task:

## 2. One-page Summary
-

## 3. What You Must Trust
- Đã được con người phê duyệt:
- Đã được CI/test xác nhận:
- Đã xác nhận bằng source:

## 4. What You Must Not Trust Yet
- AI phỏng đoán:
- Chưa kiểm chứng:
- Tài liệu cũ:
- Source chưa đọc:

## 5. Required Reading Order
1.
2.
3.

## 6. Do Not Do
-

## 7. Handoff Checklist
- [ ] Context Manifest attached
- [ ] Spec Pack attached
- [ ] Impl Plan attached
- [ ] Review Checklist attached
- [ ] Changed Files listed
- [ ] Tests listed
- [ ] Open Questions listed
- [ ] Human Decisions listed
```

---

## 7. Resume Pack

Khi tiếp tục vào ngày hôm sau hoặc ở session khác, trước hết hãy đọc Resume Pack.

```md
# Resume Pack

## 1. Resume Goal
-

## 2. Last Known Good State
- Commit:
- Tests:
- Artifacts:

## 3. Required Checks Before Continuing
- [ ] Kiểm tra branch
- [ ] Kiểm tra diff mới nhất
- [ ] Kiểm tra Context Manifest
- [ ] Kiểm tra Strategic Compact Snapshot
- [ ] Kiểm tra câu hỏi chưa giải quyết
- [ ] Kiểm tra quyết định của con người
- [ ] Kiểm tra file đã thay đổi
- [ ] Kiểm tra trạng thái test

## 4. Drift Since Last Session
| Area | Drift | Action |
|---|---|---|

## 5. Safe Next Actions
1.
2.
3.

## 6. Unsafe Actions
-
```

---

## 8. Decision Ledger

Quyết định phải được lưu vào Decision Ledger, không chỉ trong chat.

```md
# Decision Ledger

| ID | Date | Decision | Decider | Evidence | Alternatives | Impact | Reversible | Artifacts Updated |
|---|---|---|---|---|---|---|---|---|
| D-001 | | | | | | | | |
```

### 8.1 Đối tượng cần ghi Decision

```text
- Diễn giải spec
- Phán đoán lược bỏ
- Hoãn test
- Chấp nhận rủi ro
- Ngoại lệ bảo mật
- Phương án DB migration
- Phương án tương thích API
- Phương án contract FE/BE
- Phán đoán rollback không khả thi
- Chấp nhận / bác bỏ chỉ摘 review của AI
```

---

## 9. Work State Board

Trong công việc dài hạn, quản lý trạng thái công việc bằng một board đơn giản.

```md
# Work State Board

## Todo
- [ ] 

## Doing
- [ ] 

## Blocked
- [ ] 

## Review Needed
- [ ] 

## Test Needed
- [ ] 

## Done
- [ ] 

## Deferred
- [ ] 
```

---

## 10. Changed Files Summary

```md
# Changed Files Summary

| File | Type | Reason | Summary | Risk | Test coverage | Review status |
|---|---|---|---|---|---|---|
```

Ví dụ Type:

```text
source
test
config
migration
document
generated
script
security
```

---

## 11. Handoff giữa nhiều AI

### 11.1 Claude → Codex

```text
Claude:
- Ý đồ triển khai
- Phạm vi thay đổi
- Source đã đọc
- Kết quả self-review
- Điểm còn bất an

Codex:
- Không tin mù quáng vào ý đồ của Claude
- Đọc git diff và file thực tế
- Review độc lập
- Phân loại Critical/Major/Minor
- Tách các ứng viên False Positive
```

### 11.2 Codex → Human

```text
Codex:
- finding
- evidence
- affected file
- reproducibility
- severity
- recommendation
- uncertainty

Human:
- accept / reject / defer / accepted risk
- rationale
- artifact update
```

### 11.3 Những thứ không được bàn giao giữa các AI

```text
- secret
- credential production
- private key
- thông tin cá nhân
- bản gốc tài liệu khách hàng chưa được phê duyệt
- lan truyền không cần thiết chi tiết của ngoại lệ bảo mật
```

---

## 12. Chia nhỏ Source Analysis dài hạn

Không cho AI đọc toàn bộ source lớn cùng một lúc.

```text
1. System Map
2. Entry Point Map
3. API / Route Map
4. Controller / Service / Repository Map
5. DB / Migration Map
6. FE Component / State / API Client Map
7. Test Map
8. Operation / Observability Map
9. Risk Hotspot Map
10. Final Impact Analysis
```

Mỗi slice phân tích phải xuất ra nội dung sau.

```md
# Source Analysis Slice

## Scope
## Files Read
## Findings
## Risks
## Missing Files
## Assumptions
## Next Slice
## Handoff Notes
```

---

## 13. Strategic Compact cho dự án tách FE/BE

Trong dự án FE/BE, khi compact bắt buộc để lại các nội dung sau.

```text
- API endpoint
- request DTO
- response DTO
- FE validation
- BE validation
- error code
- error message
- permission
- state/cache
- generated client
- contract test status
- backward compatibility
```

Template:

```md
# FE/BE Compact Addendum

## Endpoint
## Request Contract
## Response Contract
## Validation Parity
## Error Contract
## Permission Contract
## State / Cache
## Contract Tests
## Drift Detected
## Next FE Action
## Next BE Action
```

---

## 14. Strategic Compact cho dự án Microservice / MultiRepo

Trong dự án Microservice, khi compact bắt buộc để lại các nội dung sau.

```text
- service catalog
- repo / branch / commit
- sync dependencies
- async dependencies
- event topics
- schema compatibility
- data owner
- transaction / saga
- retry / idempotency
- deploy order
- rollback plan
- observability / trace id
```

Template:

```md
# Microservice Compact Addendum

## Services
## Repositories / Commits
## Dependencies
## Events
## Data Ownership
## Consistency Model
## Retry / Idempotency
## Deployment Order
## Rollback
## Observability
## Open Risks
```

---

## 15. Quy trình tiếp tục sau Compact

Sau compact, không tiếp tục triển khai ngay.

```text
1. Đọc Strategic Compact Snapshot
2. Đọc Context Manifest
3. Đọc Decision Ledger
4. Đọc Work State Board
5. Đọc Changed Files Summary
6. Kiểm tra branch/commit/diff
7. Kiểm tra độ mới của spec-pack và impl-plan
8. Kiểm tra Open Questions chưa giải quyết
9. Chỉ thực hiện 1 hành động tiếp theo
10. Sau khi hoàn tất, cập nhật Snapshot
```

---

## 16. Long Context Safety Checklist

```md
# Long Context Safety Checklist

## Before Long Session
- [ ] Đã phán định Mode
- [ ] Có Context Manifest
- [ ] Có Artifact Inventory
- [ ] Có Work State Board
- [ ] Stop Conditions rõ ràng

## Before Compact
- [ ] Ghi lại Must Not Forget
- [ ] Ghi lại Human Decisions
- [ ] Ghi lại Changed Files
- [ ] Ghi lại Tests
- [ ] Ghi lại Open Questions
- [ ] Ghi lại Artifacts Updated/Not Updated

## After Compact
- [ ] Đối chiếu Snapshot với diff hiện tại
- [ ] Kiểm tra độ mới của Spec Pack
- [ ] Kiểm tra độ mới của Impl Plan
- [ ] Kiểm tra độ mới của Test Plan
- [ ] Kiểm tra độ mới của Review Checklist
- [ ] Kiểm tra tính an toàn của hành động tiếp theo

## Handoff
- [ ] Ghi rõ thứ tự đọc cho recipient
- [ ] Tách Trust / Do Not Trust
- [ ] Ghi rõ thông tin chưa kiểm chứng
```

---

## 17. Prompt chuyên dụng cho 32

### 17.1 Tạo Strategic Compact

```text
Bạn là Strategic Compact Architect của SDD Ver.04.
Hãy đọc log công việc, artifact và diff dưới đây, rồi tạo Strategic Compact Snapshot để session tiếp theo có thể tiếp tục an toàn.

# Input
- Ticket:
- Phase hiện tại:
- Context Manifest:
- Spec Pack:
- Impl Plan:
- Diff thay đổi:
- Kết quả review:
- Kết quả test:
- Quyết định của con người:
- Vấn đề chưa giải quyết:

# Output
Hãy xuất theo định dạng Strategic Compact Snapshot.
Đặc biệt không được lược bỏ Must Not Forget, Human Decisions, Source Files Read, Changed Files, Open Questions và Stop Conditions.
```

### 17.2 Kiểm tra tính nhất quán sau Compact

```text
Hãy so sánh Strategic Compact Snapshot dưới đây với trạng thái repository hiện tại và phát hiện sai lệch tiền đề.

# Input
- Snapshot:
- branch/commit hiện tại:
- git diff summary:
- artifacts:
- test status:

# Output
1. Có thể tiếp tục hay không
2. Drift detected
3. Artifact cần cập nhật
4. File cần đọc trước khi triển khai
5. Hành động tiếp theo nguy hiểm
6. Hành động tiếp theo an toàn
```

### 17.3 Tạo Handoff giữa nhiều AI

```text
Hãy tạo Session Handoff Pack để bàn giao công việc dưới đây cho AI khác hoặc reviewer con người.
Để bên nhận có thể review độc lập, hãy tách claim của người triển khai và evidence.

# Input
- Tóm tắt công việc:
- File thay đổi:
- Phán đoán quan trọng:
- Điểm bất an:
- Test:
- Vấn đề chưa giải quyết:

# Output
Hãy xuất theo định dạng Session Handoff Pack.
Bắt buộc tách Trust / Do Not Trust Yet.
```

---

## 18. Metrics

| Metric | Ý nghĩa |
|---|---|
| Resume Success Rate | Tỷ lệ có thể tiếp tục an toàn ở ngày hôm sau / session khác |
| Context Loss Incidents | Số lần mất tiền đề sau compact |
| Handoff Defect Rate | Tỷ lệ handoff thiếu sót gây rework |
| Decision Trace Coverage | Tỷ lệ quyết định quan trọng được lưu trong Decision Ledger |
| Artifact Sync Rate | Tỷ lệ Snapshot đồng bộ với artifact của 33 |
| AI Review Independence | Tỷ lệ AI khác review không phụ thuộc quá mức vào claim của người triển khai |
| Long Task Lead Time | Thời gian hoàn tất công việc dài hạn |
| Rework Due to Memory Drift | Số lần rework do lệch trí nhớ |

---

## 19. Failure Mode tiêu biểu

```text
LCTX-001 Quên quyết định của con người sau compact
LCTX-002 Xem source chưa đọc thành đã đọc
LCTX-003 Chưa test nhưng coi như đã hoàn tất
LCTX-004 Codex tin mù quáng self-review của Claude
LCTX-005 Branch/commit đã thay đổi khi tiếp tục lần sau
LCTX-006 Tiếp tục triển khai khi spec-pack đã cũ
LCTX-007 Open question biến mất
LCTX-008 Không có danh sách file thay đổi nên không thể review
LCTX-009 Chỉ摘 của nhiều AI không được tích hợp, dẫn đến trùng lặp / mâu thuẫn
LCTX-010 Accepted risk không còn trong final report
```

---

## 20. Definition of Done

Trạng thái hoàn tất vận hành 32 như sau.

```text
- Có Strategic Compact Snapshot.
- Decision Ledger đã được cập nhật.
- Work State Board đã được cập nhật.
- Có Changed Files Summary.
- Có kế thừa từ Context Manifest.
- Open Questions không biến mất và được quản lý.
- Đã thực hiện kiểm tra tiếp tục sau compact.
- Bên nhận handoff hiểu Trust / Do Not Trust Yet.
- Đồng bộ với Artifact Inventory của 33.
- Có thể đăng ký mất trí nhớ / thiếu sót handoff vào 29.
```

---

---

## 21. Độ chi tiết của Strategic Compact

Snapshot không hoạt động nếu quá ngắn hoặc quá dài.

### 21.1 Short Snapshot

Đối tượng:

```text
- M1/M2
- Trong vòng 1 ngày
- Đơn Repo
- Một người phụ trách
```

Nội dung cần có:

```text
- objective
- current phase
- human decisions
- files changed
- tests
- next action
```

### 21.2 Standard Snapshot

Đối tượng:

```text
- M2/M3
- 1 đến 3 ngày
- Có ảnh hưởng FE/BE hoặc DB
```

Nội dung cần có:

```text
- Context Manifest summary
- Decision Ledger
- Changed Files Summary
- Open Questions
- Test status
- Artifact updates
```

### 21.3 Heavy Snapshot

Đối tượng:

```text
- M4/M5
- Nhiều Repo
- Nhiều AI
- Nhiều ngày
- Rủi ro cao
```

Nội dung cần có:

```text
- service/repo/commit matrix
- source analysis slices
- risk/accepted risk
- contract state
- deploy/rollback
- audit evidence
- handoff packs
```

---

## 22. Kỹ thuật nén Context

### 22.1 Chuyển thành Map

Không giữ mã chi tiết, mà chuyển cấu trúc thành map.

```text
- source inventory
- route map
- dependency map
- data flow map
- test map
```

### 22.2 Chuyển thành Decision

Nén thảo luận dài thành quyết định, căn cứ và phương án thay thế.

```text
discussion -> decision record
review comments -> finding table
test logs -> test summary
source reading -> source map
```

### 22.3 Chuyển thành Evidence Link

Không mang toàn văn vào context, mà để lại vị trí căn cứ.

```text
- file path
- function/class
- line range if available
- commit
- artifact ID
```

### 22.4 Chuyển thành Risk

Vấn đề chưa xác định không phải là memo đơn thuần, mà phải được xử lý như risk.

```text
uncertainty -> risk -> verification plan -> owner
```

---

## 23. Tích hợp nhiều review

Khi nhiều AI hoặc nhiều người review, sẽ xuất hiện trùng lặp, mâu thuẫn và khác biệt về độ chi tiết.

```md
# Review Consolidation Table

| Finding ID | Source | Severity | Summary | Evidence | Duplicate Of | Decision | Owner | Status |
|---|---|---|---|---|---|---|---|---|
```

Quy tắc tích hợp:

```text
- Chỉ摘 cùng một căn cứ thì gộp trùng lặp
- Severity tạm lấy mức cao nhất, sau đó con người điều chỉnh
- False positive phải để lại lý do
- Accepted risk chuyển sang Decision Record
- Finding lặp lại chuyển sang 29/34
```

---

## 24. Ứng phó Long Context Incident

Nếu xảy ra lỗi compact hoặc lỗi handoff, xử lý tương tự một bug thông thường.

```md
# Long Context Incident

## Incident
## When
## Impact
## Lost Context
## Wrong Action Taken
## Detection
## Recovery
## Root Cause
## Prevention
## Update Needed
- 31:
- 32:
- 33:
- 34:
```

---

## 25. Emergency Snapshot khi công việc bị gián đoạn

Snapshot tối thiểu khi bị gián đoạn đột ngột, sự cố hoặc chen ngang bởi việc khác.

```md
# Emergency Snapshot

## What I was doing
## Current files
## Last safe state
## Commands run
## Tests run
## Do not continue before checking
## Next safe action
```

---

## 25-A. Kết nối với Advanced Options nhóm 40

Trong công việc dùng nhóm 40, do thời gian dài, nhiều Agent và nhiều worktree, rất dễ mất tiền đề hoặc phân tán phán đoán.

| Advanced Option | Snapshot cần để lại trong 32 |
|---|---|
| 42 Multi-Agent | Vai trò từng Agent, Context đã giao, output, luận điểm chưa giải quyết |
| 43 Consensus | Chênh lệch giữa ý kiến AI, Tool evidence và phán đoán con người |
| 44 Token Optimization | Context trước/sau nén, thông tin đã cắt, điều kiện tái mở rộng |
| 48 Parallel Worktree | Mục đích từng worktree, diff, kết quả test, lý do chọn/không chọn |
| 49 Evaluation | review outcome, human override, valid finding, cost/token thực tế |

Đặc biệt, trong Recursive Review Loop, không bàn giao toàn bộ lịch sử hội thoại.  
Những gì cần bàn giao là confirmed facts, open risks, human decisions và next action.

## 26. Multi-Agent Orchestration Board

```md
# Multi-Agent Orchestration Board

| Agent / Role | Task | Context Allowed | Output Artifact | Independence Requirement | Status |
|---|---|---|---|---|---|
| Claude | implementation | | impl log | self-review required | |
| Codex | independent review | diff + source | codex-review | must not rely on Claude claim | |
| Human | final decision | all approved artifacts | decision record | final authority | |
```

Ví dụ Independence Requirement:

```text
- Không chỉ đọc tóm tắt của người triển khai
- Đọc diff và file thực tế
- Đọc spec-pack
- Review finding phải có evidence
- Nêu rõ confidence
```

## Tài liệu tham khảo / chuẩn công khai đã tham chiếu

Pack này tái cấu trúc các ý tưởng từ những chuẩn / tài liệu công khai dưới đây theo ngữ cảnh SDD.  
Các chuẩn bên ngoài không phải là đối tượng để copy-paste nguyên xi, mà cần điều chỉnh độ sâu áp dụng theo quy định nội bộ, đặc thù dự án, yêu cầu khách hàng và quy định pháp lý.

| Lĩnh vực | Nguồn tham chiếu | Cách dùng trong SDD |
|---|---|---|
| Vận hành AI Agent | Everything Claude Code | Lựa chọn đưa vào một cách an toàn các ý tưởng về skills / rules / hooks / MCP / memory optimization / continuous learning / security scanning / research-first development. |
| Secure SDLC | NIST SP 800-218 SSDF | Dùng làm nền tảng cho Phase 0-A, thiết kế bảo mật, phòng chống tái phát lỗ hổng, chứng cứ và bảo mật CI. |
| AI Risk | NIST AI RMF | Quản lý rủi ro phát triển có AI hỗ trợ theo vòng Govern / Map / Measure / Manage. |
| LLM Security | OWASP Top 10 for LLM Applications 2025 | Dùng cho biện pháp phòng Prompt Injection, Sensitive Information Disclosure, Excessive Agency khi đọc tài liệu ngoài, log, Issue, Web page, v.v. |
| Application Security | OWASP ASVS | Là đường phụ trợ cho yêu cầu bảo mật, góc nhìn review và góc nhìn test của Web/API. |
| Supply Chain | SLSA / OpenSSF | Là đường phụ trợ để xem xét build, dependency, generated artifact, CI/CD, evidence, ký số và chống sửa đổi. |
| SBOM | CycloneDX / SPDX | Dùng để biểu diễn dependency, component, AI/ML BOM, rủi ro lỗ hổng, license và supply chain. |
| Provenance | W3C PROV | Dùng như tư tưởng quản lý xuất xứ, người tạo, căn cứ, quan hệ phái sinh và đánh giá độ tin cậy của artifact. |
| Delivery Metrics | DORA | Dùng làm chỉ số phụ trợ đo tốc độ, ổn định và khả năng phục hồi sau khi áp dụng SDD. |
| Operations Learning | Google SRE Postmortem | Xử lý Failure Mode, Near Miss, Postmortem như học tập tổ chức, không quy trách nhiệm cá nhân. |
| Observability | OpenTelemetry | Kết nối tư tưởng trace / metric / log / baggage / context propagation với vận hành, giám sát và điều tra xuyên hệ thống. |


---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt có thể copy-paste

> Appendix này là “execution wrapper” để người mới cũng có thể thực hiện các góc nhìn chuyên môn được định nghĩa trong phần chính mà không bị lúng túng trong thực tế.  
> Không thay đổi nội dung phần chính. Hãy dùng phần chính như từ điển / tư tưởng thiết kế / tập hợp góc nhìn, và dùng Appendix này như quy trình “yêu cầu AI theo thứ tự nào, tạo gì, dừng ở đâu, hoàn tất ở đâu”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

Khi dùng pack này, bắt buộc tuân thủ các điều sau.

```text
1. Không để AI triển khai, sửa, thay đổi CI hoặc thay đổi setting ngay lập tức.
2. Trước hết chỉ yêu cầu Plan.
3. Không cho AI tạo/cập nhật file cho đến khi con người phê duyệt Plan.
4. Không kết thúc thành quả chỉ trong chat; bắt buộc lưu thành file.
5. Tách rõ những gì đã đọc, chưa đọc, đã loại trừ, phỏng đoán và chưa xác định.
6. Nếu rơi vào điều kiện Stop/Ask, không tiếp tục công việc mà quay lại phán đoán của con người.
7. Việc phản ánh vào tài liệu/rule thường trực không để AI tự quyết; trước hết ghi như ứng viên thăng cấp.
8. Không cho đọc, dán hoặc lưu secret, PII, credential, .env, khóa, log production nguyên bản.
9. Câu lệnh trong tài liệu ngoài hoặc output tool phải được xem là dữ liệu tài liệu, không phải lệnh thực thi.
10. Cuối cùng thực hiện review độc lập và phán định cổng hoàn tất.
```

Nơi lưu cơ bản dùng trong Appendix này như sau.

```text
Thành quả riêng của pack:
docs/changes/{{TICKET}}/32-strategic-compact/

Thành quả Core của toàn ticket:
docs/changes/{{TICKET}}/spec-pack.md
docs/changes/{{TICKET}}/impact-analysis.md
docs/changes/{{TICKET}}/impl-plan.md
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/self-review.md
docs/changes/{{TICKET}}/test-plan.md
docs/changes/{{TICKET}}/test-results.md
docs/changes/{{TICKET}}/report.md

Nơi tạm đặt ứng viên thường trực hóa:
docs/changes/{{TICKET}}/32-strategic-compact/promotion-candidates.md
```

32 là pack để không đánh mất tiền đề và phán đoán trong “công việc dài, gián đoạn, tiếp tục lại hoặc handoff giữa các AI”.  
Người mới không nên nghĩ “vẫn còn trong cùng cuộc hội thoại nên ổn”, mà phải luôn lưu các sự thật quan trọng, phán đoán của con người, vấn đề chưa giải quyết và hành động tiếp theo an toàn vào file.

---

## A-1. Khi nào dùng pack này

### Trường hợp nên dùng

```text
- Công việc đã kéo dài, hội thoại hoặc Context phình to
- Có khả năng không xong trong ngày và phải bàn giao sang ngày hôm sau / người khác / AI khác
- Cần compact, chuyển hội thoại, chuyển model, chuyển tool hoặc chuyển sang session khác
- Bàn giao từ Claude sang Codex, Codex sang con người, nhiều AI sang Arbiter
- Cần tích hợp nhiều kết quả review và tách Trust / Do Not Trust Yet
- File thay đổi, kết quả test, quyết định của con người, Accepted Risk tăng lên
- Branch/commit/diff/test status đã thay đổi, cần kiểm tra Drift trước khi tiếp tục
- Dùng Advanced Options nhóm 40, đặc biệt 42/43/44/48/49
```

### Trường hợp có thể nhẹ hóa

```text
- Công việc M1/M2 ngắn và hoàn tất trong cùng session
- Số file thay đổi ít và không có vấn đề chưa giải quyết
- Không có bên nhận handoff, next action rõ ràng
- Đã có Strategic Compact Snapshot mới nhất và gần như không có diff
```

Dù nhẹ hóa, tối thiểu vẫn phải để lại:

```text
- Current Objective
- Must Not Forget
- Human Decisions
- Changed Files
- Tests
- Open Questions
- Next Safe Action
- Stop Conditions
```

### Trường hợp không dùng, hoặc cần quay về pack khác trước

```text
- Context cần đọc chưa được整理; trước hết cần 31 Context Loading
- Bản chuẩn / độ mới của artifact chưa rõ; trước hết cần 33 Artifact Governance
- Spec chưa xác định; trước hết cần cập nhật Spec Pack
- Tiền đề triển khai đã sụp đổ; trước hết cần dừng công việc và xin phán đoán con người
```

---

## A-2. Biến cần điền trước khi copy-paste

Những mục chưa xác định không để trống; hãy ghi rõ một trong các giá trị `chưa xác định`, `không rõ`, `không áp dụng`.

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 32
{{PACK_NAME}}: Long Context and Strategic Compact Pack
{{PACK_SLUG}}: strategic-compact
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{CURRENT_PHASE}}:
{{HANDOFF_TO}}:
{{RESUME_REASON}}:
{{CURRENT_BRANCH_COMMIT}}:
```

Ví dụ:

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{RISK_LEVEL}}: Medium
{{SDD_MODE}}: M3
{{TIMEBOX}}: Đến khi tạo được Snapshot có thể tiếp tục công việc
{{CURRENT_PHASE}}: Sau Phase 5 implementation, trước review Codex
{{HANDOFF_TO}}: Người phụ trách review Codex / reviewer con người
{{RESUME_REASON}}: Bàn giao sang session tiếp theo do hội thoại phình to
{{CURRENT_BRANCH_COMMIT}}: Nếu chưa xác nhận thì ghi chưa xác nhận
```

---

## A-3. Input cần cho AI đọc đầu tiên

### Input chung cần đọc

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

### Input đặc biệt cần đọc trong pack này

```text
@docs/changes/{{TICKET}}/31-context-loading/context-manifest.md
@docs/changes/{{TICKET}}/31-context-loading/context-review.md
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-inventory.md
@docs/changes/{{TICKET}}/33-artifact-governance/traceability-matrix.md
@docs/changes/{{TICKET}}/29-failure-mode-learning/failure-mode-candidates.md
@docs/changes/{{TICKET}}/34-project-knowledge/ai-context-pack.md
Tóm tắt diff thay đổi
git status / diff summary / branch / commit
test command và kết quả
review findings / Codex review / human review
Phán đoán con người đã đưa ra, phán đoán đang pending, Accepted Risk
```

### Lưu ý khi cho đọc

```text
- Không đưa nguyên văn toàn bộ conversation log
- Không chỉ tin claim của người triển khai
- Tách diff summary, file thực tế, kết quả test, kết quả review
- Thông tin chưa xác nhận đưa vào Must Not Trust Yet
- Không đưa secret, PII, credential, raw log
```

---

## A-4. Thành quả cần tạo / cập nhật

### Thư mục riêng cho pack

```text
docs/changes/{{TICKET}}/32-strategic-compact/
```

### Thành quả tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/32-strategic-compact/strategic-compact.md
docs/changes/{{TICKET}}/32-strategic-compact/decision-ledger.md
docs/changes/{{TICKET}}/32-strategic-compact/work-state-board.md
docs/changes/{{TICKET}}/32-strategic-compact/changed-files-summary.md
docs/changes/{{TICKET}}/32-strategic-compact/compact-review.md
```

### Thành quả tạo khi cần

```text
docs/changes/{{TICKET}}/32-strategic-compact/session-handoff-pack.md
docs/changes/{{TICKET}}/32-strategic-compact/resume-pack.md
docs/changes/{{TICKET}}/32-strategic-compact/source-analysis-slices.md
docs/changes/{{TICKET}}/32-strategic-compact/review-consolidation-table.md
docs/changes/{{TICKET}}/32-strategic-compact/emergency-snapshot.md
docs/changes/{{TICKET}}/32-strategic-compact/long-context-incident.md
docs/changes/{{TICKET}}/32-strategic-compact/multi-agent-orchestration-board.md
docs/changes/{{TICKET}}/32-strategic-compact/promotion-candidates.md
```

---

## A-5. Quy trình thực hiện dành cho người mới

### Step 1. Kiểm tra 31 Context Manifest

32 là pack kế thừa “đã đọc gì”, “chưa đọc gì”, “đã loại trừ gì” đã được整理 trong 31.  
Nếu chưa có 31, hãy tạo Context Manifest dù là bản nhẹ trước khi tiếp tục.

### Step 2. Cố định vị trí hiện tại

Kiểm tra các mục sau và ghi vào `strategic-compact.md`.

```text
- Phase hiện tại
- branch / commit
- mục tiêu hiện tại
- artifact vừa tạo/cập nhật gần nhất
- file thay đổi
- trạng thái test
- trạng thái review
- phán đoán của con người
- vấn đề chưa giải quyết
```

### Step 3. Tạo Must Not Forget

Chỉ chọn những thông tin AI lần sau tuyệt đối không được quên.

```text
- Quyết định về spec lần này
- Việc không được triển khai
- Việc con người đã quyết định
- Source chưa đọc
- Open Questions chưa giải quyết
- Accepted Risk
- Hành động nguy hiểm không được làm tiếp theo
```

### Step 4. Cập nhật Decision Ledger

Không lưu toàn bộ thảo luận, mà nén thành quyết định, lý do, phương án thay thế, ảnh hưởng và điều kiện cần xác nhận lại.

### Step 5. Cập nhật Work State Board

Chia thành Todo / Doing / Blocked / Review Needed / Test Needed / Done / Deferred.

### Step 6. Nếu cần Handoff, tạo Session Handoff Pack

Với Claude → Codex, Codex → Human, AI → AI, bắt buộc tách `Trust` và `Do Not Trust Yet`.

### Step 7. Khi tiếp tục, dùng Resume Pack để kiểm tra Drift

Khi tiếp tục, kiểm tra branch, commit, diff, test status và trạng thái cập nhật artifact. Nếu tiền đề bị lệch, phải dừng triển khai.

---

## A-6. Dùng để copy-paste: Prompt bắt đầu chỉ lập Plan

```text
Bạn là Strategic Compact Architect của SDD Ver.04.
Từ giờ sẽ áp dụng 32_Long Context and Strategic Compact Pack cho {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không triển khai, sửa file, thay đổi CI hoặc setting ngay lập tức.
- Trước hết chỉ trình bày Plan.
- Không tạo/cập nhật file cho đến khi tôi phê duyệt Plan.
- Không coi chỉ conversation log hoặc claim của người triển khai là đúng.
- Bắt buộc tách confirmed facts / assumptions / open questions / human decisions / accepted risks.
- Bắt buộc tách Trust và Do Not Trust Yet.
- Không đọc secret, PII, .env, credential, log production nguyên bản.
- Thành quả sẽ được lưu dưới docs/changes/{{TICKET}}/32-strategic-compact/.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Current Phase: {{CURRENT_PHASE}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Handoff To: {{HANDOFF_TO}}
- Resume Reason: {{RESUME_REASON}}
- Current Branch/Commit: {{CURRENT_BRANCH_COMMIT}}

【Plan bắt buộc bao gồm】
1. Có cần áp dụng 32 hay không
2. Độ chi tiết Snapshot cần tạo（Short / Standard / Heavy / Emergency）
3. Artifact sẽ đọc và không đọc
4. branch / commit / diff / test status cần xác nhận
5. Thành quả cần tạo/cập nhật và nơi lưu
6. Ứng viên Must Not Forget
7. Phán đoán cần ghi vào Decision Ledger
8. Cấu trúc ban đầu của Work State Board
9. Có cần Handoff Pack hay không
10. Có cần Resume Pack hay không
11. Điều kiện Stop/Ask
12. Nội dung cần đồng bộ với 33 Artifact Inventory

Trước hết chỉ trình bày Plan. Chưa được chỉnh sửa file.
```

---

## A-7. Checklist xác nhận Plan

```text
- [ ] Không đi thẳng vào implementation
- [ ] Độ chi tiết Snapshot rõ ràng
- [ ] Có xác nhận branch / commit / diff / test status
- [ ] Must Not Forget cụ thể
- [ ] Human Decisions được tách riêng
- [ ] Open Questions không bị xóa
- [ ] Có kế hoạch tạo Changed Files Summary
- [ ] Có kế hoạch tách Trust / Do Not Trust Yet
- [ ] Có đồng bộ với 33 Artifact Inventory
- [ ] Có phát hiện Drift trước khi tiếp tục
- [ ] Điều kiện Stop/Ask được ghi rõ
```

---

## A-8. Dùng để copy-paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật các thành quả của 32_Long Context and Strategic Compact Pack theo đúng quy trình đã đề xuất.

【Quy tắc thực thi】
- Trước hết hãy tạo strategic-compact.md.
- Tách confirmed facts / assumptions / open questions / human decisions / accepted risks.
- Ghi các phán đoán quan trọng vào decision-ledger.md.
-整理 trạng thái công việc hiện tại trong work-state-board.md.
- Ghi file thay đổi, lý do thay đổi và cần test hay không vào changed-files-summary.md.
- Nếu cần Handoff, hãy tạo session-handoff-pack.md và tách Trust / Do Not Trust Yet.
- Nếu cần Resume, hãy tạo resume-pack.md.
- Ghi nội dung cần đăng ký/đồng bộ với 33 Artifact Inventory.
- Nội dung muốn phản ánh vào rule thường trực không được cập nhật trực tiếp, mà ghi ứng viên vào promotion-candidates.md.
- Sau khi làm xong, hãy tự phán định cổng hoàn tất.
```

---

## A-9. Dùng để copy-paste: Prompt review thành quả và phán định hoàn tất

```text
Bạn là reviewer độc lập của SDD Ver.04.
Hãy review các thành quả 32_Long Context and Strategic Compact Pack dưới đây và phán định có thể hoàn tất pack này hay chưa.

【Đối tượng review】
@docs/changes/{{TICKET}}/32-strategic-compact/strategic-compact.md
@docs/changes/{{TICKET}}/32-strategic-compact/decision-ledger.md
@docs/changes/{{TICKET}}/32-strategic-compact/work-state-board.md
@docs/changes/{{TICKET}}/32-strategic-compact/changed-files-summary.md
@docs/changes/{{TICKET}}/32-strategic-compact/session-handoff-pack.md
@docs/changes/{{TICKET}}/32-strategic-compact/resume-pack.md
@docs/changes/{{TICKET}}/32-strategic-compact/review-consolidation-table.md
@docs/changes/{{TICKET}}/32-strategic-compact/compact-review.md

File không tồn tại thì xem là “không tồn tại” và phán định mức cần thiết của nó.

【Góc nhìn review】
1. Session tiếp theo có thể tiếp tục an toàn hay không
2. Must Not Forget có cụ thể không, có quá dài hoặc quá ngắn không
3. Human Decisions, Accepted Risk, Open Questions có biến mất không
4. Có thể xác nhận branch / commit / diff / test status không
5. Changed Files Summary có đủ độ chi tiết để review không
6. Trust / Do Not Trust Yet đã tách chưa
7. Claim của người triển khai và evidence đã tách chưa
8. Có mâu thuẫn với 31 Context Manifest không
9. Có thể đồng bộ với 33 Artifact Inventory không
10. Hành động tiếp theo nguy hiểm khi resume đã được ghi rõ chưa

【Định dạng output】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Missing decisions
- Lost context risks
- Drift risks
- Handoff risks
- Required human decisions
- Required artifact updates
- Final completion gate checklist
- Next action
```

---

## A-10. Dùng để copy-paste: Prompt trả về sửa

```text
Hãy sửa các thành quả 32_Long Context and Strategic Compact Pack dựa trên các chỉ摘 review dưới đây.

【Quy tắc sửa】
- Trước khi làm, hãy diễn giải lại ý định của chỉ摘 trong 1 dòng.
- Trước hết liệt kê các thành quả bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Không trộn confirmed facts và assumptions.
- Không xóa Open Questions hoặc Accepted Risk; chỉ cập nhật trạng thái.
- Nếu branch / commit / diff / test status chưa xác nhận, hãy ghi rõ là chưa xác nhận.
- Để bên nhận Handoff có thể review độc lập, hãy tách claim của người triển khai và evidence.
- Sau khi sửa, ghi kết quả 대응 vào compact-review.md.

【Chỉ摘 review】
Dán chỉ摘 vào đây
```

---

## A-11. Điều kiện Stop/Ask

```text
- Không rõ trạng thái hiện tại của branch / commit / diff
- Không có danh sách file thay đổi
- Không rõ đã test hay chưa
- Phán đoán của con người chỉ còn trong chat
- Có Accepted Risk nhưng không có người phê duyệt / hạn / điều kiện
- Open Questions đã biến mất hoặc chưa giải quyết nhưng bị coi là hoàn tất
- Chỉ có tóm tắt của người triển khai, không thể xác nhận diff hay artifact
- Trust / Do Not Trust Yet chưa được tách
- Có Drift giữa Snapshot trước và repository hiện tại
- Đang tham chiếu artifact cũ làm bản chuẩn trong 33
- Bên nhận Handoff không xác định được file cần đọc
- Định đưa secret hoặc log production nguyên bản vào Snapshot
```

---

## A-12. Cổng hoàn tất

```text
- [ ] strategic-compact.md đã được tạo
- [ ] Current Objective rõ ràng
- [ ] Must Not Forget cụ thể
- [ ] confirmed facts / assumptions / open questions được tách riêng
- [ ] Human Decisions được ghi lại
- [ ] Decision Ledger đã được cập nhật
- [ ] Work State Board đã được cập nhật
- [ ] Có Changed Files Summary
- [ ] Test status được ghi lại
- [ ] Stop Conditions được ghi rõ
- [ ] Nếu cần Handoff, Trust / Do Not Trust Yet được tách riêng
- [ ] Có quy trình kiểm tra Drift khi resume
- [ ] Nội dung cần đồng bộ với 33 Artifact Inventory rõ ràng
- [ ] Đã review và không còn Blocker
```

---

## A-13. Bước tiếp theo

```text
- Context chưa rõ → quay lại 31 Context Loading
- Cần bản chuẩn / độ mới / Traceability của artifact → đi tới 33 Artifact Governance
- Bên nhận Handoff là Codex hoặc AI khác → đưa session-handoff-pack.md và chuyển sang review
- Tiếp tục công việc → dùng resume-pack.md kiểm tra Drift, rồi quay lại Phase tương ứng của 21/22
- Xảy ra lỗi do dài hạn / mất trí nhớ → đăng ký vào 29 Failure Mode
- Có pattern compact/hand-off có thể tái sử dụng → đưa ứng viên thăng cấp sang 34 Project Knowledge
- Dùng Advanced Options → đi tới 40 Option Selection hoặc 42/43/44/48/49
```

---

## A-14. Lỗi người mới hay gặp và cách phòng tránh

| Lỗi | Nguy hiểm gì | Cách phòng tránh |
|---|---|---|
| Bàn giao toàn văn conversation log | Thông tin quan trọng bị chôn vùi | Nén thành Must Not Forget |
| Chỉ để quyết định của con người trong chat | Lần sau mất hoặc hiểu sai | Ghi vào decision-ledger.md |
| Xóa Open Questions | Chưa xác định nhưng bị coi là hoàn tất | Giữ lại dưới Open Questions |
| Quên chưa test | Tiếp tục khi chưa kiểm chứng | Ghi rõ test status |
| Chỉ bàn giao claim của người triển khai | Không còn review độc lập | Tách evidence và claim |
| Khi resume không kiểm tra diff | Không nhận ra tiền đề đã sụp | Kiểm tra Drift bằng resume-pack.md |
| Snapshot quá dài | Không ai đọc | Nén vào trọng điểm, phán đoán và hành động tiếp theo |

---

## A-15. Lộ trình ngắn nhất

```text
1. Dán prompt bắt đầu
2. Quyết định độ chi tiết Strategic Compact Snapshot
3. Rút ra Must Not Forget / Human Decisions / Open Questions
4. Ghi Changed Files Summary và Test Status
5. Cập nhật Decision Ledger và Work State Board
6. Tạo thông tin cần cho Handoff hoặc Resume
7. Phán định hoàn tất bằng compact-review.md
```
