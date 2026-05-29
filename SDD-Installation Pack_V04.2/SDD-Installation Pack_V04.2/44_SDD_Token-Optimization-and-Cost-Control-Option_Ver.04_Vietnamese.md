**Mục lục**
- [44_SDD_Token-Optimization-and-Cost-Control-Option_Ver.04_Vietnamese](#44_sdd_token-optimization-and-cost-control-option_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Kết luận tổng thể về Token Optimization](#1-kết-luận-tổng-thể-về-token-optimization)
  - [2. Điều kiện áp dụng](#2-điều-kiện-áp-dụng)
  - [3. Kiến trúc cơ bản của 44](#3-kiến-trúc-cơ-bản-của-44)
  - [4. Token Budget Controller](#4-token-budget-controller)
  - [5. Thiết kế Prompt Caching](#5-thiết-kế-prompt-caching)
  - [6. Cache Strategy](#6-cache-strategy)
  - [7. File Summary Cache](#7-file-summary-cache)
  - [8. Repository Map / Code Map](#8-repository-map--code-map)
  - [9. RAG Optimization](#9-rag-optimization)
  - [10. Context Compression](#10-context-compression)
  - [11. Tool Output Compression](#11-tool-output-compression)
  - [12. Agent Output Compression](#12-agent-output-compression)
  - [13. Agent Context Partitioning](#13-agent-context-partitioning)
  - [14. Recursive State Compression](#14-recursive-state-compression)
  - [15. Model Routing / Cascade](#15-model-routing--cascade)
  - [16. Early Exit](#16-early-exit)
  - [17. Batch / Flex Processing](#17-batch--flex-processing)
  - [18. Cost Observability](#18-cost-observability)
  - [19. KPI](#19-kpi)
  - [20. Security and Privacy](#20-security-and-privacy)
  - [21. Prompt tối ưu token](#21-prompt-tối-ưu-token)
  - [22. Failure Mode](#22-failure-mode)
  - [23. Definition of Ready](#23-definition-of-ready)
  - [24. Definition of Done](#24-definition-of-done)
  - [25. Ví dụ chi tiết về Token Budget](#25-ví-dụ-chi-tiết-về-token-budget)
  - [26. Thiết kế Cache Key](#26-thiết-kế-cache-key)
  - [27. Compression Safety Checklist](#27-compression-safety-checklist)
  - [28. Agent-specific Context Budget Policy](#28-agent-specific-context-budget-policy)
  - [29. Ví dụ tối ưu Prompt Template](#29-ví-dụ-tối-ưu-prompt-template)
  - [30. Tool-first, LLM-last](#30-tool-first-llm-last)
  - [31. Token Regression Test](#31-token-regression-test)
  - [32. Trade-off giữa cắt giảm token và suy giảm độ chính xác](#32-trade-off-giữa-cắt-giảm-token-và-suy-giảm-độ-chính-xác)
  - [33. Prompt Cost Review](#33-prompt-cost-review)
  - [34. Kết nối từ 44 sang 46/49](#34-kết-nối-từ-44-sang-4649)
  - [Tài liệu tiêu chuẩn / công khai tham khảo](#tài-liệu-tiêu-chuẩn--công-khai-tham-khảo)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-copy-paste)
  - [A-0. Quy tắc tuyệt đối phải tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-phải-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào sử dụng pack này](#a-1-khi-nào-sử-dụng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Thành quả cần tạo / cập nhật](#a-4-thành-quả-cần-tạo--cập-nhật)
  - [A-5. Quy trình thực hiện](#a-5-quy-trình-thực-hiện)
  - [A-6. Dùng để copy-paste: Prompt bắt đầu](#a-6-dùng-để-copy-paste-prompt-bắt-đầu)
  - [A-7. Dùng để copy-paste: Prompt phê duyệt Plan](#a-7-dùng-để-copy-paste-prompt-phê-duyệt-plan)
  - [A-8. Dùng để copy-paste: Prompt review thành quả / phán định hoàn tất](#a-8-dùng-để-copy-paste-prompt-review-thành-quả--phán-định-hoàn-tất)
  - [A-9. Dùng để copy-paste: Prompt trả về sửa lại](#a-9-dùng-để-copy-paste-prompt-trả-về-sửa-lại)
  - [A-10. Điều kiện Stop/Ask dành cho người mới](#a-10-điều-kiện-stopask-dành-cho-người-mới)
  - [A-11. Cổng hoàn tất](#a-11-cổng-hoàn-tất)
  - [A-12. Đi tiếp sang đâu](#a-12-đi-tiếp-sang-đâu)

# 44_SDD_Token-Optimization-and-Cost-Control-Option_Ver.04_Vietnamese


> Loại: SDD Ver.04 Advanced Option  
> Tiền đề: Đã áp dụng Core / Extension / Operations Pack của 11 và 21〜29・31〜34, hoặc đã có cơ chế quản lý thành quả, quản lý Context và Security Gate tương đương  
> Nguyên tắc: Không làm Core trở nên nặng nề. Advanced Option chỉ được áp dụng có chọn lọc cho những案件 có độ phức tạp cao, rủi ro cao, yêu cầu độ chính xác cao hoặc yêu cầu tối ưu chi phí.  
> Lưu ý: Tài liệu này không khuyến nghị AI tự động thực thi một cách tự trị. Các quyết định rủi ro cao, ghi file, merge, release, deploy bắt buộc phải có phê duyệt của con người.


## 0. Vai trò của tài liệu này

Tài liệu này là tiêu chuẩn để kiểm soát lượng token, latency, chi phí sử dụng AI và ô nhiễm context vốn dễ phát sinh trong các Advanced Options của SDD Ver.04, đặc biệt là 41 Heavy Source Analysis, 42 Multi-Agent, 43 Tool-Grounded Verification.

Tài liệu đưa tư tưởng cốt lõi của tài liệu đính kèm “Chiến lược bổ sung để cắt giảm token AI_20260516.md” vào thực tiễn SDD.

```text
Để nâng cao độ chính xác của AI, ta đa góc nhìn hóa.
Tuy nhiên, không được để nhiều AI đa góc nhìn đó đọc đi đọc lại cùng một lượng lớn thông tin.

Chỉ thông tin cần thiết,
cho đúng Agent cần thiết,
ở đúng độ chi tiết cần thiết,
vào đúng thời điểm cần thiết,
và được cache, nén, phân phối, tái sử dụng.
```

## 1. Kết luận tổng thể về Token Optimization

Trong SDD, cắt giảm token không đơn thuần là “viết prompt ngắn lại”. Cần thiết kế theo 4 nguyên tắc sau.

```text
1. Không gửi
2. Làm ngắn
3. Tái sử dụng
4. Xử lý rẻ hơn
```

Cụ thể, kết hợp các Layer sau.

```text
Token Optimization Layer
  = Token Budget Controller
  + Prompt Caching
  + Context Caching
  + Exact Cache
  + Semantic Cache
  + Embedding Cache
  + Retrieval Cache
  + File Summary Cache
  + Repository Map / Code Map
  + RAG Optimization
  + Context Compression
  + Tool Output Compression
  + Agent Context Partitioning
  + Recursive State Compression
  + Model Routing / Model Cascade
  + Early Exit
  + Batch / Flex Processing
  + Cost Observability
```

## 2. Điều kiện áp dụng

### 2.1 Bắt buộc áp dụng

```text
- Sử dụng 42 Multi-Agent
- Đọc source quy mô lớn bằng 41 Heavy Source Analysis
- tool output / test log / build log lớn
- token/cost trên mỗi PR cao
- Đang để AI đọc lặp lại cùng một context
- context phình to trong session dài
- Số Agent từ 3 trở lên
- Sử dụng Recursive Review Loop
```

### 2.2 Áp dụng nhẹ

```text
- Với PR thông thường, chỉ đưa vào thiết kế static prefix có ý thức tới Prompt Caching
- Chỉ đưa vào Tool Output Compression
- Chỉ thực hiện Token Audit
```

## 3. Kiến trúc cơ bản của 44

```text
Input / PR / Issue
  ↓
Risk Classifier
  ↓
Token Budget Controller
  ↓
Context Planner
  ↓
Cache Lookup
  ├─ Prompt Cache
  ├─ Exact Cache
  ├─ Semantic Cache
  ├─ File Summary Cache
  └─ Retrieval Cache
  ↓
Context Partitioning
  ↓
Compression
  ├─ Source / Code slice
  ├─ Tool output
  ├─ Agent output
  └─ Recursive state
  ↓
Model Router / Cascade
  ↓
Agent Execution
  ↓
Cost Observability
  ↓
Token Audit / Optimization Feedback
```

## 4. Token Budget Controller

Token Budget Controller là cơ chế quyết định ngân sách trước khi gọi AI.

### 4.1 Nhóm ngân sách

| Category | Nội dung |
|---|---|
| Context budget | Toàn bộ context đầu vào |
| Agent budget | Input/output cho từng Agent |
| Tool output budget | summary kết quả tool |
| Recursive budget | Toàn bộ loop |
| Human summary budget | Tóm tắt dành cho con người |
| Emergency reserve | Kiểm tra bổ sung ngoài dự kiến |

### 4.2 Ví dụ ngân sách theo rủi ro

| Mode | Mục đích | Phương châm |
|---|---|---|
| T0 | Không cần AI | Không dùng |
| T1 | Light | 1 Agent, diff tối thiểu, chỉ tool summary |
| T2 | Standard | diff + related files + test summary |
| T3 | Heavy | Bắt buộc có Impact Slice + Agent Partitioning |
| T4 | Critical | Model hiệu năng cao + Tool evidence + human summary |
| T5 | Stop | Dừng do thiếu context hoặc chi phí quá lớn |

### 4.3 Token Budget Record

```md
# Token Budget Record

## 1. Metadata
- Ticket / PR:
- Date:
- Owner:
- Related SDD Mode:

## 2. Budget
| Area | Budget | Actual | Status | Notes |
|---|---:|---:|---|---|
| Static prefix | | | | |
| Dynamic task | | | | |
| Source context | | | | |
| Tool output | | | | |
| Agent outputs | | | | |
| Recursive rounds | | | | |
| Human summary | | | | |

## 3. Compression Strategy
- Context:
- Tool output:
- Agent output:
- State:

## 4. Stop / Degrade Conditions
- Stop if:
- Degrade to:
- Human ask if:

## 5. Final Cost Notes
- Cost estimate:
- Cost actual:
- Cost per valid finding:
```

## 5. Thiết kế Prompt Caching

Cơ bản để Prompt Caching phát huy hiệu quả là **Static First, Dynamic Last**.

### 5.1 Cấu trúc tốt

```text
[Static Prefix]
- SDD policy
- Agent role
- Output schema
- Coding standards
- Security rules
- Review rubric
- Project stable knowledge

[Dynamic Suffix]
- Current ticket
- Current diff
- Current tool results
- Current user instruction
- Current timestamp if necessary
```

### 5.2 Cấu trúc xấu

```text
[Dynamic]
- PR number
- Current time
- diff
- random request id

[Static]
- role
- rules
- schema
```

Nếu thông tin động nằm ở đầu, prefix dễ bị phá vỡ, khiến cache hit khó xảy ra.

### 5.3 Ứng viên Static Prefix

```text
- SDD Ver.04 common policy
- Agent role catalog
- Review severity model
- Output JSON schema
- Security hard rules
- Project glossary stable section
- Method allowlist / denylist stable section
- Tool result schema
```

### 5.4 Ứng viên Dynamic Suffix

```text
- Ticket summary
- Diff summary
- Changed files
- Tool result summary
- Source Confidence Score
- Human-specific instruction
```

## 6. Cache Strategy

### 6.1 Exact Cache

Những thứ có thể tái sử dụng bằng khớp hoàn toàn.

```text
- summary của cùng file hash
- compressed summary của cùng tool output hash
- cùng agent prompt static prefix
- cùng rules bundle
```

### 6.2 Semantic Cache

Tái sử dụng các truy vấn tương tự. Tuy nhiên, trong phán đoán code có rủi ro.

```text
Có thể dùng:
- FAQ
- project glossary
- giải thích known pattern
- documentation lookup

Cần thận trọng:
- phán đoán bug fix
- phán đoán security
- phán đoán DB migration
- phán đoán current diff
```

### 6.3 Embedding Cache

```text
- file/chunk embeddings
- doc embeddings
- project knowledge embeddings
- API contract embeddings
```

Điều kiện vô hiệu hóa.

```text
- file hash thay đổi
- branch thay đổi
- dependency major version thay đổi
- contract cập nhật
- project rule cập nhật
```

### 6.4 Retrieval Cache

```md
# Retrieval Cache Entry

## Query
- normalized query:
- filters:
- branch/commit:

## Results
| Rank | Source | Chunk | Score | Hash |
|---|---|---|---|---|

## Validity
- Valid until:
- Invalidate if:
```

## 7. File Summary Cache

Với repo quy mô lớn, không để AI đọc full file mỗi lần. Tạo summary gắn với file hash.

```md
# File Summary Cache

## File
- Path:
- Hash:
- Language:
- Last updated:

## Purpose
- What this file does:

## Public Interface
- Functions/classes/types:

## Side Effects
- DB:
- External API:
- File:
- Message:
- Cache:

## Security / Permission
- Auth:
- Permission:
- Sensitive data:

## Error Handling
- Exceptions:
- Retry:
- Logging:

## Tests
- Related tests:

## Do Not Omit
- Critical lines / invariants:

## Recompute If
- Hash changes:
- Related contract changes:
```

## 8. Repository Map / Code Map

Trong 44, Code Map cũng được dùng để cắt giảm token. Ở 41, nó phục vụ độ chính xác phân tích; ở 44, nó phục vụ mục tiêu **không để AI đọc toàn văn**.

```text
Repo Map -> Module Map -> File Summary -> Function Slice -> Surrounding Lines -> Full File only if necessary
```

Những gì cần có trong Code Map.

```text
- module responsibility
- entry points
- public functions/classes
- side effects
- DB/API/event interaction
- auth/permission checks
- related tests
- risk hotspots
- file hash
```

## 9. RAG Optimization

RAG tiện lợi, nhưng dùng qua loa sẽ tốn chi phí và tăng lỗi tìm kiếm.

### 9.1 Pipeline khuyến nghị

```text
1. Query rewrite
2. Source filter
3. Retrieve
4. Rerank
5. Deduplicate
6. Compress
7. Gắn cite/evidence ID
8. Expand-on-demand
```

### 9.2 Lưu ý về Code RAG

```text
- Dễ bị kéo theo function có tên giống nhau
- Rất nguy hiểm nếu nhặt kết quả từ branch cũ
- Dễ nhầm lẫn test code với production code
- Cần loại trừ generated code và vendor code
- Nếu nén làm rơi auth check hoặc transaction boundary thì nguy hiểm
```

## 10. Context Compression

### 10.1 Những thứ có thể nén

```text
- Đoạn giải thích dài
- Log lặp
- Danh sách passed test
- Coding standards đã biết
- Old discussion summary
- Large generated docs
```

### 10.2 Những thứ cần cẩn trọng khi nén

```text
- Điều kiện authorization
- Điều kiện validation
- Tính toán tiền/số lượng
- DB write
- Transaction boundary
- Retry/idempotency
- Error handling
- Quy trình migration
- Security setting
```

### 10.3 Code Skeleton

```md
# Code Skeleton

## File
- Path:
- Hash:

## Signatures
- function name(args): return
- class Name

## Important Branches
| Condition | Behavior | Risk |
|---|---|---|

## Side Effects
| Operation | Target | Condition |
|---|---|---|

## Critical Lines Preserved
| Line | Reason |
|---|---|
```

## 11. Tool Output Compression

Tool output là nguyên nhân chính gây bùng nổ token.

### 11.1 Quy tắc nén

```text
- Lưu raw log dưới dạng artifact
- Chỉ đưa compressed summary cho AI
- Chỉ giữ failed tests
- Gộp các repeated stack frames
- Xóa ANSI/progress/download logs
- Giữ top error và root cause candidate
- Giữ file/line/command/exit code
```

### 11.2 Test Output Summary

```md
# Test Output Summary

## Command

## Verdict

## Failed Tests
| Test | File | Failure | Expected | Actual | First stack frame |
|---|---|---|---|---|---|

## Skipped Tests
| Test | Reason | Risk |
|---|---|---|

## Raw Log
- path:
- hash:
```

### 11.3 Build / Lint / SAST Summary

```md
# Tool Summary

## Tool
- name:
- version:
- command:

## Verdict

## Findings
| ID | Severity | Rule | File | Line | Message |
|---|---|---|---|---|---|

## Noise Removed
- repeated lines:
- non-actionable warnings:

## Raw Ref
```

## 12. Agent Output Compression

Không để Agent viết dài dòng.

```text
- Xử lý nội bộ bằng JSON/table
- Summary cho con người chỉ tạo ngắn ở cuối
- finding sắp xếp theo severity
- Cấm cảm tưởng không có evidence
- duplicate do Arbiter hợp nhất
```

### 12.1 Giới hạn output của Agent

```text
Bug Reviewer:
  max findings: 10
  max explanation per finding: tương đương 80 words
  must include file/line/evidence

Security Reviewer:
  no max for critical/high
  low/info tối đa 5件
  evidence bắt buộc

Arbiter:
  consolidated summary only
  cấm raw agent discussion
```

## 13. Agent Context Partitioning

```text
Common context:
- ticket summary
- AC summary
- diff summary
- risk hotspots
- source confidence

Bug Agent:
- changed functions
- callers/callees
- failing tests

Security Agent:
- auth/permission map
- input handling
- secrets/PII context

Test Agent:
- AC-test matrix
- test plan
- test results

Performance Agent:
- loops/query/payload
- benchmark summary

Arbiter:
- agent outputs
- tool evidence IDs
- policy
```

## 14. Recursive State Compression

Trong Recursive Review Loop, không truyền lịch sử hội thoại của round trước. Chỉ truyền state.

```md
# Recursive State Summary

## Round
- current:
- max:

## Stable Facts
| ID | Fact | Evidence |
|---|---|---|

## Open Findings
| ID | Severity | Status | Next action |
|---|---|---|---|

## Resolved Findings
| ID | Resolution | Evidence |
|---|---|---|

## Disagreements
| ID | Topic | Need |
|---|---|---|

## Stop Conditions
- token budget:
- no new finding:
- human review:
```

## 15. Model Routing / Cascade

### 15.1 Cơ bản

```text
- Không ném mọi thứ vào high-performance model
- Low-risk dùng rule/tool/lightweight model
- Chỉ phần high-risk, mơ hồ, phức tạp mới dùng high-performance model
- Chỉ đánh giá lại disagreement
```

### 15.2 Ví dụ Cascade

```text
1. Rule precheck
2. Tool parser
3. Lightweight summarizer
4. Standard reviewer
5. High-reasoning reviewer for critical slice
6. Human review
```

## 16. Early Exit

Những gì có thể kết thúc trước khi gọi AI thì nên kết thúc.

```text
- docs only and no code impact
- formatting only
- generated lockfile only with verified command
- CI already failed at build step, cần sửa trước khi review
- Source Availability Stop
- Required files missing
```

## 17. Batch / Flex Processing

Với xử lý không cần đồng bộ, cân nhắc xử lý chi phí thấp.

Các xử lý phù hợp.

```text
- Đánh giá lại PR cũ
- nightly review calibration
- cập nhật large repository summary
- tái tạo file summary cache
- gom cụm failure mode
- scoring evaluation dataset
```

Các xử lý không phù hợp.

```text
- Phán định ngay trước khi merge PR
- ứng phó incident
- quyết định critical khi human reviewer đang chờ
- interactive debugging
```

## 18. Cost Observability

Không đo thì không thể giảm.

```md
# Token / Cost Audit

## 1. Summary
- Ticket / PR:
- Date:
- Total input tokens:
- Total output tokens:
- Estimated cost:
- Latency:

## 2. By Stage
| Stage | Input | Output | Cost | Latency | Notes |
|---|---:|---:|---:|---:|---|

## 3. By Agent
| Agent | Input | Output | Cost | Valid findings | Cost / valid finding |
|---|---:|---:|---:|---:|---:|

## 4. Cache
| Cache type | Hit | Miss | Hit rate | Notes |
|---|---:|---:|---:|---|

## 5. Compression
| Target | Raw size | Compressed size | Reduction | Risk |
|---|---:|---:|---:|---|

## 6. Optimization Actions
- Remove:
- Cache:
- Compress:
- Route:
- Early exit:
```

## 19. KPI

```text
- token per PR
- cost per PR
- latency per PR
- cost per valid finding
- valid finding rate
- false positive rate
- cache hit rate
- compression ratio
- tool output compression ratio
- high-cost model utilization rate
- early exit rate
- recursive rounds per PR
```

Quan trọng nhất là **cost per valid finding**. Rẻ mà số lượng chỉ摘 hữu ích giảm thì thất bại. Độ chính xác cao nhưng chi phí quá lớn thì không bền vững.

## 20. Security and Privacy

Cache và compression cũng có thể trở thành rủi ro bảo mật.

```text
- Không cache secrets hoặc PII
- Không chia sẻ cache vượt qua ranh giới tenant/user/project
- Kiểm soát nơi lưu raw log
- Không để thông tin bí mật còn lại trong summary sau nén
- Tránh để semantic cache trộn thông tin từ案件 khác
- Thiết lập retention policy
```

## 21. Prompt tối ưu token

```md
Bạn là Token Optimization Architect của SDD Ver.04.
Hãy lập kế hoạch thực thi giúp giảm token/cost/latency cho kế hoạch AI dưới đây, đồng thời không làm rơi thông tin quan trọng.

# Input
- Ticket / PR:
- Selected Advanced Options:
- Agents:
- Impact Slice:
- Tool outputs:
- Risk level:
- Max budget:
- Required evidence:

# Quy tắc
- Không cho mọi Agent đọc toàn bộ
- Static First, Dynamic Last
- Không đưa raw tool output
- Khi nén code, không làm rơi auth/validation/DB write
- Recursive loop chỉ truyền state summary
- High-cost model chỉ dùng cho high-risk slice
- Ghi rõ thông tin không được cache

# Output
1. Token Budget Record
2. Thiết kế Prompt Caching
3. Agent Context Partitioning
4. Đối tượng được nén và đối tượng cấm nén
5. Cache strategy
6. Model Routing
7. Điều kiện Early Exit
8. Thiết kế Cost Observability
9. Lưu ý Security/Privacy
```

## 22. Failure Mode

| ID | Failure Mode | Mitigation |
|---|---|---|
| TOK-001 | Đưa toàn bộ context cho mọi Agent | Context Partitioning |
| TOK-002 | Đặt thông tin dynamic ở đầu prefix | Static First, Dynamic Last |
| TOK-003 | Đưa toàn văn test log | Tool Output Compression |
| TOK-004 | Nén code làm rơi điều kiện quan trọng | Compression Safety |
| TOK-005 | Dùng thường xuyên high-cost model | Model Router |
| TOK-006 | Semantic cache bị tái sử dụng sai | Cache boundary |
| TOK-007 | Lưu secret/PII trong cache | Security policy |
| TOK-008 | Không đo việc token reduction làm giảm độ chính xác | 49 Evaluation |
| TOK-009 | Đưa toàn bộ lịch sử recursive loop | State Compression |
| TOK-010 | Chỉ nhìn cost và làm giảm valid finding | cost per valid finding |

## 23. Definition of Ready

```text
- Có lý do cần giảm token/cost
- selected options / agents rõ ràng
- context source đã được 31整理
- Có nơi lưu raw log
- Đã quyết định thông tin được/không được cache
- Có tiêu chí không nén quá mức high-risk context
```

## 24. Definition of Done

```text
- Có Token Budget Record
- Cấu trúc Prompt Caching là Static First
- Có Agent Context Partition
- Đã thực hiện Tool Output Compression
- Đã ghi cache hit/miss
- Đã đo cost per valid finding
- Đã kiểm tra với 43/49 xem có suy giảm độ chính xác không
- Tri thức cải tiến đã được phản ánh vào 29/34
```



## 25. Ví dụ chi tiết về Token Budget

Số token thực tế khác nhau tùy model và tokenizer, nên ở đây xử lý như ngân sách tương đối.

| Workload | Common context | Source | Tool | Agent output | Notes |
|---|---:|---:|---:|---:|---|
| Light review | 1 | 1 | 1 | 1 | Chỉ 1 Agent |
| Standard PR | 2 | 3 | 2 | 2 | diff + related files |
| Heavy source | 2 | 6 | 2 | 2 | Bắt buộc có Impact Slice ở 41 |
| Multi-Agent | 2 | 4 per relevant agent | 2 | 1 per agent | Bắt buộc partitioning |
| Critical security | 3 | 5 | 4 | 2 | Cấm nén quá mức |
| Large refactor | 3 | 8 | 5 | 3 | Khuyến nghị 46/48/49 |

## 26. Thiết kế Cache Key

Nếu thiết kế key kém, cache sẽ gây sự cố.

```text
Những thứ nên có trong cache key tốt:
- repo
- branch / commit
- file path
- file hash
- tool version
- rule version
- prompt version
- project knowledge version
- model family nếu output phụ thuộc mạnh
```

```text
Những thứ không nên đưa vào:
- secret
- PII
- raw token
- user-specific confidential context not scoped
```

```md
# Cache Key Design

## Cache Type

## Key Components
| Component | Required | Reason |
|---|---|---|

## Invalidation
| Trigger | Action |
|---|---|

## Security Boundary
- Project:
- Tenant:
- Data class:
```

## 27. Compression Safety Checklist

```text
- Có xóa mất điều kiện authorization không
- Có xóa mất điều kiện validation không
- Có xóa mất boundary value như null/empty/zero/full-width numeric không
- Có xóa mất DB write / transaction không
- Có xóa mất external API / event publish không
- Có xóa mất retry/idempotency không
- Có xóa mất error handling / audit log không
- Source confidence đang thấp mà lại nén quá mức không
- Có giữ lại tham chiếu tới raw artifact không
```

## 28. Agent-specific Context Budget Policy

```yaml
agent_budget_policy:
  common:
    include:
      - ticket_summary
      - ac_summary
      - diff_summary
      - risk_hotspots
    exclude:
      - raw_logs
      - unrelated_docs
  security_reviewer:
    must_include:
      - auth_permission_map
      - input_validation
      - sensitive_data_flow
    compression_forbidden:
      - authorization_conditions
      - audit_log_requirements
  test_reviewer:
    must_include:
      - ac_test_matrix
      - test_failures
      - changed_test_files
    compression_forbidden:
      - expected_actual_failures
  arbiter:
    must_include:
      - agent_summaries
      - evidence_ids
      - veto_flags
    exclude:
      - raw_agent_discussions
```

## 29. Ví dụ tối ưu Prompt Template

Ví dụ xấu.

```text
Bạn là một kỹ sư xuất sắc. Hãy đọc toàn bộ tài liệu khổng lồ dưới đây và review thật hoàn hảo.
[toàn văn tài liệu khổng lồ]
```

Ví dụ tốt.

```text
[Static]
Role: Security Reviewer
Policy: SDD Ver.04 Security Review Rules
Schema: JSON Finding Schema
Severity: Critical/High/Medium/Low

[Dynamic]
Task: PR-123 auth change
Context: Auth Map + changed permission checks + test summary
Instruction: Find only authorization, sensitive data, audit issues. Do not comment on style.
```

## 30. Tool-first, LLM-last

Dùng tool để thu hẹp trước khi đưa cho AI đọc.

```text
- Dùng grep/search để thu hẹp candidate
- Dùng typecheck/build để phát hiện method không tồn tại
- Dùng test failure parser để chỉ trích xuất phần fail
- Dùng SAST/SCA để đưa ra vấn đề đã biết
- Dùng DB schema diff để đưa ra điểm thay đổi
- Dùng git diff để chỉ đưa phần chênh lệch
```

LLM được dùng sau khi tool đã thu hẹp, để phán đoán, tích hợp và giải thích.

## 31. Token Regression Test

Khi thay đổi prompt hoặc agent của SDD, cần kiểm tra xem lượng token có xấu đi không.

```md
# Token Regression Test

## Scenario
- Standard PR:
- Heavy source:
- Multi-agent:

## Before / After
| Scenario | Before input | After input | Delta | Accept? |
|---|---:|---:|---:|---|

## Quality Check
| Scenario | Valid findings before | Valid findings after | False positives | Notes |
|---|---:|---:|---:|---|
```

## 32. Trade-off giữa cắt giảm token và suy giảm độ chính xác

Cắt giảm token là phương tiện, không phải mục đích.

| Biện pháp cắt giảm | Rủi ro độ chính xác | Biện pháp bù đắp |
|---|---|---|
| file summary | Thiếu điều kiện quan trọng | mục do-not-omit, expand-on-demand |
| tool output compression | Thiếu root cause | raw log ref, giữ top stack |
| semantic cache | Tái sử dụng sai | ranh giới scope/hash/version |
| model downgrade | Giảm năng lực suy luận | high-risk cascade |
| early exit | Bỏ sót | trigger matrix và audit |
| recursive state compression | Thiếu ngữ cảnh | tách stable facts/open findings |

## 33. Prompt Cost Review

```md
Bạn là Cost Reviewer của SDD Ver.04.
Hãy xem Token / Cost Audit dưới đây và đưa ra đề xuất cải thiện để lần sau giảm cost mà không làm giảm chất lượng.

# Input
- Token / Cost Audit
- Agent outputs
- Valid / false positive findings
- Tool output sizes
- Cache hit rate

# Output
1. Top 5 nguyên nhân gây cost lớn nhất
2. Context có thể cắt
3. Context không được cắt
4. Ứng viên cache hóa
5. Ứng viên compression
6. Cải thiện model routing
7. Ứng viên early exit
8. Rủi ro suy giảm độ chính xác
9. Đề xuất thí nghiệm lần sau
```

## 34. Kết nối từ 44 sang 46/49

```text
Chuyển sang 46:
- Yêu cầu Code Map
- Yêu cầu File Summary Cache
- Yêu cầu RAG optimization
- Yêu cầu Compression Safety

Chuyển sang 49:
- thực tế token/cost
- cache hit rate
- cost per valid finding
- latency
- kết quả token regression
- chỉ số chất lượng liên quan đến precision/recall
```

## Tài liệu tiêu chuẩn / công khai tham khảo

Advanced Options này sử dụng tài liệu SDD nội bộ, các thành quả V04 của 11 và 21〜29・31〜34, tài liệu đính kèm “AI精度向上のための追加戦略_20260516.md” và “AIトークン削減のための追加戦略_20260516.md” làm input chính, đồng thời đưa tư tưởng của các tài liệu / tiêu chuẩn công khai sau vào ngữ cảnh SDD.

- OpenAI Agents SDK: các yếu tố thiết kế Agent như handoffs, guardrails, function tools, MCP server tool calling, sandbox agents.
- OpenAI Prompt Caching / Cost Optimization / Batch API / Flex Processing: exact prefix caching, thiết kế static prefix, xử lý bất đồng bộ / chi phí thấp.
- OpenAI Structured Outputs: nâng cao khả năng xử lý máy và tái lập nhờ structured output theo JSON Schema.
- Model Context Protocol Security Best Practices: vector tấn công đặc thù của MCP implementation, quyền hạn, rủi ro tool execution.
- NIST SSDF SP 800-218: thực hành secure development có thể tích hợp vào Secure SDLC.
- OWASP ASVS / OWASP LLM Top 10 / OWASP GenAI Security: Web/API security và rủi ro đặc thù của LLM/Agent.
- SLSA / OpenSSF Scorecard: supply chain phần mềm, dependency, build evidence, đánh giá sức khỏe OSS.
- OpenTelemetry GenAI semantic conventions: thiết kế quan sát cho AI/Agent call, tool call, latency, token, error.
- Recursive Multi-Agent Systems: nghiên cứu coi Multi-Agent collaboration như recursive computation. Trong thực務, SDD chỉ áp dụng có giới hạn theo hướng RecursiveMAS-inspired.
- LongLLMLingua / Prompt Compression: tư tưởng về mật độ thông tin quan trọng, position bias, compression trong long context.
- RTK / Rust Token Killer: tư tưởng thực tiễn về giảm token bằng cách nén CLI output trước khi đưa vào LLM context.
- SWE-bench / SWE-bench Verified: tham khảo cho thiết kế dataset đánh giá coding Agent / regression evaluation.
- everything-claude-code: tư tưởng vận hành skills, rules, hooks, MCP, security scanning, continuous learning, cross-harness. Tuy nhiên, trong SDD chỉ đưa vào có chọn lọc và an toàn.


---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste

> Appendix này là “execution wrapper” giúp cả người mới cũng có thể thực hiện Token Optimization / Cost Control được định nghĩa trong phần chính mà không làm giảm chất lượng.  
> Nội dung phần chính không thay đổi. Hãy dùng phần chính như “đặc tả thiết kế cho token budget, Prompt Caching, Compression, Cost Audit”, và dùng Appendix này như quy trình “quản lý ngân sách trước, kiểm soát trong lúc thực thi, kiểm toán sau khi thực thi”.

---

## A-0. Quy tắc tuyệt đối phải tuân thủ đầu tiên

44 là Option để duy trì chất lượng SDD trong khi giảm Token/Cost/Latency.  
Người mới không được xem 44 là “công việc cắt ngắn”, mà phải xem là **công việc phân biệt cái được cắt và cái không được cắt, rồi tối ưu trong khi đo suy giảm chất lượng**.

```text
1. Không đột ngột cắt Context.
2. Trước hết yêu cầu AI chỉ đưa ra Token Budget Plan.
3. Không thay đổi thiết kế Prompt, thiết kế Cache, cách chạy Agent cho tới khi con người phê duyệt Plan.
4. Không cắt phần lõi của AC, Security, quyền hạn, DB migration, external IF, failure log.
5. Tách Static Prefix và Dynamic Suffix.
6. Cache không được chia sẻ vượt qua Security boundary.
7. Nếu nén, phải ghi lại đã giữ gì, đã bỏ gì, rủi ro là gì.
8. Nếu token reduction làm giảm chất lượng Finding thì không được xem là thành công.
9. Không chỉ nhìn Cost; phải nhìn cả valid finding, false negative, review latency.
10. Cuối cùng thực hiện Token / Cost Audit và phán định cổng hoàn tất.
```

Nơi lưu cơ bản dùng trong Appendix này như sau.

```text
Thành quả riêng của pack:
docs/changes/{{TICKET}}/44-token-cost-control/

Handoff sang Option sau:
docs/changes/{{TICKET}}/44-token-cost-control/46-handoff.md
docs/changes/{{TICKET}}/44-token-cost-control/49-feedback.md

Nơi đặt tạm ứng viên thường trực hóa:
docs/changes/{{TICKET}}/44-token-cost-control/promotion-candidates.md
```

Tư tưởng quan trọng.

```text
Mục tiêu của 44 không phải là “giảm Token”,
mà là giảm context thừa, output lặp, tính toán lại, Agent quá mức,
trong khi vẫn giữ Evidence cần thiết và chất lượng phán đoán.
```

---

## A-1. Khi nào sử dụng pack này

### Trường hợp nên dùng

```text
- Context trở nên lớn do 41 Heavy Source Analysis
- Số Agent hoặc Round tăng do 42 Multi-Agent
- Kết quả tool hoặc CI log lớn do 43
- Sử dụng 46 RAG / CodeMap / Context Compression
- Review latency hoặc Cost trở thành vấn đề
- Đang để AI đọc lặp lại cùng một Context
- Muốn thiết kế Prompt Caching, File Summary Cache, Tool Output Compression
- Muốn đo ảnh hưởng của việc cắt giảm Token lên chất lượng bằng 49
```

### Trường hợp có thể nhẹ hóa

```text
- Thay đổi nhỏ, Context ngắn
- Review nhẹ một lần, hiệu quả của thiết kế Cache thấp
- Token/Cost trong phạm vi chấp nhận được, rủi ro chất lượng lớn hơn
- Đã được 28 phán định vận hành nhẹ
```

Kể cả khi nhẹ hóa, tối thiểu vẫn để lại những nội dung sau.

```text
- Lý do nhẹ hóa 44
- Context không được cắt
- Trigger tái đánh giá nếu Token/Cost phình to khi thực thi
- Lý do không dùng compression
```

### Trường hợp không dùng, hoặc phải quay lại pack khác trước

```text
- Spec hoặc Source chưa được整理, cần làm 23/31/33/41 trước
- Security boundary chưa xác định, chia sẻ Cache đang nguy hiểm
- Không có quality baseline, không đo được suy giảm do cắt giảm
- Tool raw output có khả năng chứa secret/PII, cần kiểm tra an toàn bằng 43/45 trước
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 44
{{PACK_NAME}}: Token Optimization and Cost Control Option
{{PACK_SLUG}}: token-cost-control
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{OPTIMIZATION_OBJECTIVE}}:
{{TOKEN_BUDGET}}:
{{COST_LIMIT}}:
{{LATENCY_LIMIT}}:
{{QUALITY_GUARDRAILS}}:
{{STATIC_CONTEXT_CANDIDATES}}:
{{DYNAMIC_CONTEXT_CANDIDATES}}:
{{CACHE_SECURITY_BOUNDARY}}:
```

Ví dụ điền.

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{SCOPE_NOTE}}: Kiểm soát Context và Tool output vì sử dụng 41/42/43
{{RISK_LEVEL}}: High
{{SDD_MODE}}: M3
{{TIMEBOX}}: Đến Token Budget và Compression Safety Review
{{OPTIMIZATION_OBJECTIVE}}: Giảm Cost của Multi-Agent review nhưng không làm giảm chất lượng Security/Test finding
{{TOKEN_BUDGET}}: Plan đầu tiên 20k, mỗi Agent tối đa 8k, tóm tắt Tool tối đa 5k
{{COST_LIMIT}}: Xác nhận với con người về giới hạn cho toàn ticket
{{LATENCY_LIMIT}}: Hỗ trợ PR review trong vòng 15 phút
{{QUALITY_GUARDRAILS}}: Cấm lược bỏ AC/Security/quyền hạn/lõi failure log
{{STATIC_CONTEXT_CANDIDATES}}: SDD rules, quan điểm review chung, output Schema cố định
{{DYNAMIC_CONTEXT_CANDIDATES}}: ticket spec, diff, test result, tool failure
{{CACHE_SECURITY_BOUNDARY}}: Theo repo, theo ticket, cấm cache thông tin nhạy cảm
```

---

## A-3. Input đầu tiên cần cho AI đọc

### Input đọc chung

```text
@docs/changes/{{TICKET}}/spec-pack.md
@docs/changes/{{TICKET}}/impact-analysis.md
@docs/changes/{{TICKET}}/impl-plan.md
@docs/changes/{{TICKET}}/review-checklist.md
@docs/changes/{{TICKET}}/test-plan.md
@docs/changes/{{TICKET}}/test-results.md
@docs/architecture/
@docs/standards/
@.claude/CLAUDE.md
@.claude/rules/
```

### Input đặc biệt cần đọc trong pack này

```text
@docs/changes/{{TICKET}}/40-advanced-options-selection/advanced-option-selection-record.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/impact-slice.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/orchestrator-plan.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-context-partition.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/tool-result-record.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/compressed-tool-output.md
@docs/changes/{{TICKET}}/31-context-loading/context-manifest.md
```

### Input không được cắt

```text
- Acceptance Criteria
- Scope / Non-scope
- Open Issues
- Security requirements
- Permission / auth / role conditions
- DB schema / migration critical changes
- External IF / contract breaking changes
- Lõi của Tool failure
- Veto candidates
- Human decisions required
- Rollback / deploy constraints
```

### Input có thể nén

```text
- Khối lượng lớn output của successful log
- Stack trace lặp lại
- Mô tả background dài trong README
- File đã được File Summary Cache hóa
- Chi tiết generated code. Tuy nhiên, public interface phải giữ lại
- Finding trùng lặp trong Agent output
- CI progress logs
```

---

## A-4. Thành quả cần tạo / cập nhật

### Thư mục riêng của pack

```text
docs/changes/{{TICKET}}/44-token-cost-control/
```

### Thành quả tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/44-token-cost-control/token-budget-record.md
docs/changes/{{TICKET}}/44-token-cost-control/prompt-cache-design.md
docs/changes/{{TICKET}}/44-token-cost-control/compression-safety-checklist.md
docs/changes/{{TICKET}}/44-token-cost-control/agent-context-budget.md
docs/changes/{{TICKET}}/44-token-cost-control/tool-output-summary.md
docs/changes/{{TICKET}}/44-token-cost-control/token-cost-audit.md
```

### Thành quả tạo khi cần

```text
docs/changes/{{TICKET}}/44-token-cost-control/cache-key-design.md
docs/changes/{{TICKET}}/44-token-cost-control/file-summary-cache.md
docs/changes/{{TICKET}}/44-token-cost-control/code-skeleton.md
docs/changes/{{TICKET}}/44-token-cost-control/recursive-state-summary.md
docs/changes/{{TICKET}}/44-token-cost-control/token-regression-test.md
docs/changes/{{TICKET}}/44-token-cost-control/cost-review.md
docs/changes/{{TICKET}}/44-token-cost-control/46-handoff.md
docs/changes/{{TICKET}}/44-token-cost-control/49-feedback.md
docs/changes/{{TICKET}}/44-token-cost-control/promotion-candidates.md
```

### Có thể phản ánh vào Core artifacts

```text
docs/changes/{{TICKET}}/impl-plan.md
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/test-plan.md
docs/changes/{{TICKET}}/report.md
```

---

## A-5. Quy trình thực hiện

### Step 1. Tạo Token Budget Plan

Trước hết quyết định các nội dung sau.

```text
- Tổng Token/Cost giới hạn
- Ngân sách theo stage
- Ngân sách theo Agent
- Ngân sách tool output
- Cache policy
- Compression policy
- Điều kiện Early Exit
- Điều kiện Degrade
- Quality Guardrails
```

### Step 2. Tách Static Prefix và Dynamic Suffix

```text
Static Prefix:
- SDD rules
- Fixed output Schema
- Common prohibitions
- Common review perspectives
- role definition

Dynamic Suffix:
- ticket spec
- diff
- test result
- Tool failure
- Context cho từng Agent
- quyết định mới nhất
```

Static Prefix dễ tái sử dụng, còn Dynamic Suffix được xem là thay đổi mỗi lần.

### Step 3. Quyết định Cache Strategy

```text
Exact Cache:
- fixed prompt, Schema, common rules

File Summary Cache:
- mục đích của file dài, public interface, side effects, tests, do not omit

Tool Output Summary:
- summary của CI/log/SAST/test

Retrieval Cache:
- kết quả tìm kiếm RAG. Tuy nhiên phải luôn có freshness và invalidation condition
```

Những điều cần giữ khi dùng Cache.

```text
- Không chia sẻ vượt Security boundary
- Không cache secret/PII
- Có invalidation condition
- Không xem cache cũ là source of truth
```

### Step 4. Thực hiện Compression Safety Review

Kiểm tra trước/sau nén xem các nội dung sau còn được giữ hay không.

```text
- AC
- Security
- Permission
- DB migration
- Contract
- Tool failure
- Veto
- Human decision required
- Rollback
- Confidence / limitations
```

### Step 5. Trong lúc thực thi, phán định Early Exit / Degrade

```text
Early Exit:
- Vì có Veto nghiêm trọng nên review Agent tiếp không còn nhiều giá trị
- Tool failure là Blocker, trước khi sửa thì thêm review có giá trị thấp

Degrade:
- Chuyển từ full multi-agent sang single reviewer
- Chuyển từ raw log sang compressed output
- Bỏ qua Option rủi ro thấp
```

### Step 6. Tạo Token / Cost Audit

Cuối cùng, ghi lại các nội dung sau.

```text
- cost theo stage
- cost theo agent
- cache hit / miss
- hiệu quả compression
- chất lượng finding
- có missed risk hay không
- đề xuất cải thiện lần sau
```

---

## A-6. Dùng để copy-paste: Prompt bắt đầu

```text
Bạn là người hỗ trợ thực thi “44 Token Optimization and Cost Control Option” của SDD Ver.04.
Từ bây giờ, hãy lập Plan để kiểm soát Token/Cost/Latency cho {{TICKET}}（{{FEATURE_NAME}}）mà không làm giảm chất lượng.

【Quy tắc quan trọng nhất】
- Không đột ngột cắt Context.
- Trước hết chỉ trình bày Token Budget Plan.
- Cho tới khi tôi phê duyệt Plan, không thay đổi thiết kế Prompt, thiết kế Cache, cách chạy Agent hoặc chỉnh sửa file.
- Không cắt lõi của AC, Security, quyền hạn, DB migration, external IF, Tool failure.
- Hãy tách Static Prefix và Dynamic Suffix.
- Cache không được chia sẻ vượt Security boundary.
- Nếu nén, hãy ghi rõ phần giữ lại, phần loại bỏ và thiếu sót nguy hiểm.
- Nếu token reduction làm giảm chất lượng Finding thì không xem là thành công.
- Không đưa secret, PII, credential, log production gốc vào cache/summary.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Optimization Objective: {{OPTIMIZATION_OBJECTIVE}}
- Token Budget: {{TOKEN_BUDGET}}
- Cost Limit: {{COST_LIMIT}}
- Latency Limit: {{LATENCY_LIMIT}}
- Quality Guardrails: {{QUALITY_GUARDRAILS}}
- Static Context Candidates: {{STATIC_CONTEXT_CANDIDATES}}
- Dynamic Context Candidates: {{DYNAMIC_CONTEXT_CANDIDATES}}
- Cache Security Boundary: {{CACHE_SECURITY_BOUNDARY}}

【Plan bắt buộc phải bao gồm】
1. Có cần áp dụng 44 hay không
2. Token Budget
3. Ngân sách theo Stage / Agent / Tool
4. Tách Static Prefix / Dynamic Suffix
5. Cache Strategy
6. Compression Strategy
7. Compression Safety Checklist
8. Điều kiện Early Exit / Degrade
9. Quality Guardrails
10. Cost Observability
11. Thành quả cần tạo/cập nhật và nơi lưu
12. Điều kiện Stop/Ask
13. Cổng hoàn tất

Trước hết chỉ trình bày Plan. Chưa được cắt Context hay chỉnh sửa file.
```

---

## A-7. Dùng để copy-paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật các thành quả của 44 Token Optimization and Cost Control.

【Quy tắc thực thi】
- Trước hết hãy tạo token-budget-record.md.
- Trong prompt-cache-design.md, hãy tách Static Prefix / Dynamic Suffix.
- Nếu tạo cache-key-design.md, bắt buộc phải ghi invalidation và security boundary.
- Trong file-summary-cache.md và tool-output-summary.md, bắt buộc giữ Do Not Omit và Raw Ref.
- Trong compression-safety-checklist.md, kiểm tra AC/Security/Permission/Tool failure/Veto có bị rơi không.
- Nếu dùng Agent, hãy quản lý ngân sách theo Agent trong agent-context-budget.md.
- Sau khi thực thi, ghi hiệu quả cắt giảm và ảnh hưởng chất lượng vào token-cost-audit.md.
- Nếu nghi ngờ suy giảm chất lượng, hãy xử lý là NEEDS_UPDATE chứ không phải cắt giảm thành công.
```

---

## A-8. Dùng để copy-paste: Prompt review thành quả / phán định hoàn tất

```text
Bạn là reviewer độc lập của SDD Ver.04.
Hãy review các thành quả 44 Token Optimization dưới đây và phán định xem Token/Cost có được kiểm soát mà không làm giảm chất lượng hay không.

【Đối tượng review】
@docs/changes/{{TICKET}}/44-token-cost-control/token-budget-record.md
@docs/changes/{{TICKET}}/44-token-cost-control/prompt-cache-design.md
@docs/changes/{{TICKET}}/44-token-cost-control/compression-safety-checklist.md
@docs/changes/{{TICKET}}/44-token-cost-control/agent-context-budget.md
@docs/changes/{{TICKET}}/44-token-cost-control/tool-output-summary.md
@docs/changes/{{TICKET}}/44-token-cost-control/token-cost-audit.md

【Góc nhìn review】
1. Token reduction có bị mục đích hóa không
2. Lõi của AC/Security/Permission/DB/Contract/Tool failure có bị rơi không
3. Static Prefix và Dynamic Suffix có được tách không
4. Security boundary và invalidation của Cache có rõ không
5. secret/PII có nằm trong cache hoặc summary không
6. Compression Safety Checklist có thực sự hoạt động không
7. Agent-specific Context Budget có thừa/thiếu không
8. Điều kiện Early Exit / Degrade có an toàn không
9. Có nhìn cả Token/Cost reduction và finding quality không
10. Có thể trả đánh giá/cải tiến về 49 không
11. Có đáp ứng cổng hoàn tất không

【Định dạng output】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Quality degradation risks
- Context omission risks
- Cache security risks
- Cost reduction validity
- Required human decisions
- Required updates before reuse
- 49 feedback candidates
- Final completion gate checklist
- Next action
```

---

## A-9. Dùng để copy-paste: Prompt trả về sửa lại

```text
Hãy sửa các thành quả 44 Token Optimization dựa trên các chỉ摘 review dưới đây.

【Quy tắc sửa】
- Trước hết diễn giải lại ý định của chỉ摘 trong 1 dòng rồi mới bắt tay vào.
- Liệt kê trước các thành quả bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Nếu thông tin không được cắt đã bị rơi, hãy cập nhật compression-safety-checklist.md và summary liên quan.
- Nếu cache boundary hoặc invalidation chưa rõ, hãy cập nhật cache-key-design.md.
- Nếu token reduction làm giảm finding quality, hãy ghi vào token-cost-audit.md như một suy giảm chất lượng.
- Nếu nội dung chuyển sang 46/49 thay đổi, hãy cập nhật handoff/feedback.

【Chỉ摘 review】
Dán chỉ摘 vào đây
```

---

## A-10. Điều kiện Stop/Ask dành cho người mới

Nếu rơi vào một trong các trường hợp sau, hãy dừng tối ưu và quay lại xác nhận với con người.

```text
- Không thể phán định được thông tin nào có thể cắt
- Đang định cắt lõi của AC, Security, quyền hạn, DB migration, external IF, Tool failure
- Có khả năng Cache chứa secret/PII
- Đang định chia sẻ Cache ra ngoài repo, tenant hoặc khách hàng
- Không có invalidation condition
- Sau token reduction, Finding giảm rõ rệt quá mức
- Veto hoặc Human Review Required biến mất do compression
- Đang định chạy Multi-Agent hoặc RAG khi chưa xác định Cost limit
- Không còn lại trọng điểm của failure log
- Không có tiêu chí chất lượng để xem kết quả cắt giảm của 44 là thành công
```

Định dạng output khi Stop/Ask.

```text
- Stop Reason:
- Context / cache / compression affected:
- Quality risk:
- Security risk:
- Required human decision:
- Minimal safe next step:
```

---

## A-11. Cổng hoàn tất

Pack này chỉ hoàn tất khi đáp ứng tất cả điều sau.

```text
- [ ] Token Budget Record đã được tạo
- [ ] Ngân sách theo Stage / Agent / Tool đã rõ
- [ ] Static Prefix và Dynamic Suffix đã được tách
- [ ] Cache Strategy có security boundary và invalidation
- [ ] secret/PII không nằm trong cache hoặc summary
- [ ] Compression Safety Checklist đã được tạo
- [ ] AC/Security/Permission/DB/Contract/Tool failure/Veto không bị rơi
- [ ] Agent Context Budget được tạo khi cần
- [ ] Tool Output Summary có Raw Ref và Do Not Infer
- [ ] Điều kiện Early Exit / Degrade an toàn
- [ ] Token / Cost Audit đã được tạo
- [ ] Không chỉ ghi hiệu quả cắt giảm, mà còn ghi cả ảnh hưởng chất lượng
- [ ] Review không còn Blocker
- [ ] Nội dung cần phản ánh sang 46/49 đã được ghi rõ
```

---

## A-12. Đi tiếp sang đâu

```text
Muốn triển khai sang RAG/CodeMap        → Đi sang 46
Muốn đánh giá liên tục Cost/chất lượng  → Đi sang 49
Cần tích hợp Tool output                → Đi sang 43
Thiết kế lại Context cho Multi-Agent    → Quay lại 42
Source Context quá lớn                  → Quay lại 41
Context boundary nguy hiểm              → Quay lại 31
Không rõ freshness của Artifact         → Quay lại 33
Không rõ Security/Privacy boundary      → Quay lại 25 hoặc 45
```

Cuối cùng, hãy tóm tắt kết quả của 44 vào `report.md` dưới dạng “Token / Cost Control Summary”, để có thể giải thích được những gì đã cắt giảm, những gì không cắt, ảnh hưởng chất lượng và cải thiện cho lần sau.
