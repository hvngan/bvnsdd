**Mục lục**
- [41_SDD_Heavy-Source-Analysis-and-Repository-Intelligence-Option_Ver.04_Japanese](#41_sdd_heavy-source-analysis-and-repository-intelligence-option_ver04_japanese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Điều kiện áp dụng](#1-điều-kiện-áp-dụng)
  - [2. Kết nối với 23・31・33・34・44](#2-kết-nối-với-2331333444)
  - [3. Luồng tổng thể của Repository Intelligence](#3-luồng-tổng-thể-của-repository-intelligence)
  - [4. Danh sách artifact](#4-danh-sách-artifact)
  - [5. Heavy Source Analysis Plan](#5-heavy-source-analysis-plan)
  - [6. Source Availability Advanced](#6-source-availability-advanced)
  - [7. Repository Inventory](#7-repository-inventory)
  - [8. Architecture / Module Map](#8-architecture--module-map)
  - [9. Entry Point Map](#9-entry-point-map)
  - [10. Call Graph / Dependency Map](#10-call-graph--dependency-map)
  - [11. Data / DB / Migration Map](#11-data--db--migration-map)
  - [12. External Interface / Batch / Event Map](#12-external-interface--batch--event-map)
  - [13. Generated / Vendor / Dead Code Map](#13-generated--vendor--dead-code-map)
  - [14. Risk Hotspot Map](#14-risk-hotspot-map)
  - [15. Source Confidence Score](#15-source-confidence-score)
  - [16. Impact Slice](#16-impact-slice)
  - [17. Góc nhìn bổ sung theo từng Tech Stack](#17-góc-nhìn-bổ-sung-theo-từng-tech-stack)
  - [18. Prompt Heavy Source Analysis](#18-prompt-heavy-source-analysis)
  - [19. Human Review Checklist](#19-human-review-checklist)
  - [20. Failure Mode](#20-failure-mode)
  - [21. Definition of Ready](#21-definition-of-ready)
  - [22. Definition of Done](#22-definition-of-done)
  - [23. Thiết kế các vòng phân tích](#23-thiết-kế-các-vòng-phân-tích)
  - [24. Source Expansion Strategy](#24-source-expansion-strategy)
  - [25. Tư tưởng thiết kế lệnh hỗ trợ Static Analysis](#25-tư-tưởng-thiết-kế-lệnh-hỗ-trợ-static-analysis)
  - [26. Repository Intelligence Review Board](#26-repository-intelligence-review-board)
  - [27. Quy tắc đặc biệt cho Large Legacy Analysis](#27-quy-tắc-đặc-biệt-cho-large-legacy-analysis)
  - [28. Cách nâng Source Confidence](#28-cách-nâng-source-confidence)
  - [29. Phản ánh từ Repository Intelligence sang các artifact khác](#29-phản-ánh-từ-repository-intelligence-sang-các-artifact-khác)
  - [30. Prompt review hoàn tất Repository Intelligence](#30-prompt-review-hoàn-tất-repository-intelligence)
  - [Tài liệu tham khảo / tiêu chuẩn công khai đã tham chiếu](#tài-liệu-tham-khảo--tiêu-chuẩn-công-khai-đã-tham-chiếu)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-copy-paste)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Artifact cần tạo/cập nhật](#a-4-artifact-cần-tạocập-nhật)
  - [A-5. Quy trình thực thi](#a-5-quy-trình-thực-thi)
  - [A-6. Dùng để copy-paste: Prompt bắt đầu](#a-6-dùng-để-copy-paste-prompt-bắt-đầu)
  - [A-7. Dùng để copy-paste: Prompt phê duyệt Plan](#a-7-dùng-để-copy-paste-prompt-phê-duyệt-plan)
  - [A-8. Dùng để copy-paste: Prompt review artifact và phán định hoàn tất](#a-8-dùng-để-copy-paste-prompt-review-artifact-và-phán-định-hoàn-tất)
  - [A-9. Dùng để copy-paste: Prompt trả về sửa lại](#a-9-dùng-để-copy-paste-prompt-trả-về-sửa-lại)
  - [A-10. Điều kiện Stop/Ask cho người mới](#a-10-điều-kiện-stopask-cho-người-mới)
  - [A-11. Cổng hoàn tất](#a-11-cổng-hoàn-tất)
  - [A-12. Nơi đi tiếp theo](#a-12-nơi-đi-tiếp-theo)

# 41_SDD_Heavy-Source-Analysis-and-Repository-Intelligence-Option_Ver.04_Japanese

> Loại: SDD Ver.04 Advanced Option  
> Tiền đề: Đã áp dụng 11 và các Core / Extension / Operations Pack từ 21〜29・31〜34, hoặc có cơ chế quản lý artifact, quản lý context, Security Gate tương đương  
> Nguyên tắc: Không làm nặng Core. Advanced Option chỉ được áp dụng có chọn lọc cho các dự án phức tạp, rủi ro cao, yêu cầu độ chính xác cao hoặc có yêu cầu tối ưu chi phí.  
> Chú ý: Tài liệu này không khuyến nghị AI tự trị thực thi. Các quyết định rủi ro cao, thao tác ghi, merge, release, deploy bắt buộc phải có phê duyệt của con người.

---

## 0. Vai trò của tài liệu này

Tài liệu này là Advanced Option của `23 Source Intelligence`. Đối với những dự án mà Source Intelligence thông thường chưa đủ — repository khổng lồ, phức tạp, nhiều Tech Stack, nhiều Repo, Legacy, thiếu tài liệu — tài liệu này định nghĩa tiêu chuẩn để tạo **Repository Intelligence** trước khi giao cho AI triển khai.

Mục đích của 41 không phải là ném cho AI yêu cầu “hãy đọc rồi sửa”. Mục đích là như sau.

```text
- Biến source phức tạp mà AI dễ đọc sai thành bản đồ có cấu trúc
- Trực quan hóa phạm vi ảnh hưởng, entry point, DB, external IF, Batch, Event, quyền hạn, vận hành
- Tách riêng source đã đọc / source chưa đọc được / suy đoán / xác nhận của con người
- Xác định các điểm nguy hiểm trong Repository trước khi triển khai
- Giúp Review/Test/Security cùng nhìn một bản đồ để ra quyết định
```

## 1. Điều kiện áp dụng

### 1.1 Gần như bắt buộc áp dụng

Nếu rơi vào một trong các điều kiện sau, rất nên áp dụng 41.

```text
- Đối tượng thay đổi trải rộng qua nhiều module / nhiều service / nhiều repository
- Có liên quan FE / BE / DB / Batch / external IF
- Khó truy vết Controller → Service → Repository → DB
- Có nhiều framework nội bộ, nền tảng chung, code generation, legacy implementation cũ
- AI trước đây từng dùng method không tồn tại hoặc DB field sai
- Cần kiểm tra tính nhất quán giữa source mới nhất, DB definition, API spec, migration, test
- Cần căn cứ mạnh cho phán định “không ảnh hưởng”
- Thực hiện review quy mô lớn, review xuyên suốt, review nhiều Tech Stack
```

### 1.2 Điều kiện không nên áp dụng quá mức

Trong các trường hợp sau, hãy lightweight hóa hoặc không cần dùng 41.

```text
- Đối tượng thay đổi rõ ràng trong 1 file
- Entry point, call path, test đã rõ
- Không ảnh hưởng DB/API/quyền/external IF
- Đã có bản đồ đủ tốt từ 23 Source Intelligence
```

## 2. Kết nối với 23・31・33・34・44

| Kết nối | Vai trò |
|---|---|
| 23 Source Intelligence | Phiên bản tiêu chuẩn của 41. 41 đào sâu hơn 23 |
| 31 Context Loading | Định nghĩa cần đọc gì, cần loại trừ gì |
| 33 Artifact Governance | Quản lý tính chính bản và bằng chứng của artifact Repository Intelligence |
| 34 Project Knowledge | Cung cấp framework riêng của project, method allowlist, pattern |
| 44 Token Optimization | Kiểm soát token/cost khi phân tích source quy mô lớn |

Nếu thực hiện 41 mà không có 31 và 44 thì khả năng cao sẽ thất bại. Không đưa thẳng lượng lớn source cho AI, mà hãy đi theo thứ tự **Repository Map → Module Map → Relevant Slice → Evidence Expansion**.

## 3. Luồng tổng thể của Repository Intelligence

```text
1. Advanced Repo Intake
2. Context Loading Plan
3. Source Availability Advanced
4. Repository Inventory
5. Architecture / Module Map
6. Entry Point / Route / API Map
7. Call Graph / Dependency Map
8. Data / DB / Migration Map
9. External Interface / Batch / Event Map
10. Test / CI / Tool Map
11. Risk Hotspot Map
12. Source Confidence Score
13. Tạo Impact Slice
14. Thiết lập Human Verification Point
15. Phản ánh vào Spec Pack / Impl Plan / Review Checklist
```

Điểm quan trọng là không phân tích chi tiết toàn bộ source ngay một lần.

```text
Trước tiên tạo bản đồ tổng thể ở mức thô.
Sau đó chỉ đào sâu vùng xung quanh đối tượng thay đổi.
Cuối cùng gắn căn cứ cho các phạm vi được phán định là không ảnh hưởng.
```

## 4. Danh sách artifact

| Artifact | Mức bắt buộc | Nội dung |
|---|---|---|
| heavy-source-analysis-plan.md | Bắt buộc | Phạm vi phân tích, phạm vi loại trừ, ngân sách, điều kiện Stop |
| source-availability-advanced.md | Bắt buộc | Source đọc được/không đọc được và ảnh hưởng |
| repository-inventory.md | Bắt buộc | repo, module, runtime, framework, config quan trọng |
| architecture-map.md | Bắt buộc | logical architecture, layer, boundary |
| entrypoint-map.md | Bắt buộc | Entry point như UI/API/Batch/Event/CLI/Scheduler |
| call-dependency-map.md | Tiêu chuẩn | caller/callee, phụ thuộc service/repository |
| data-db-map.md | Tiêu chuẩn | table, migration, query, transaction |
| external-interface-map.md | Tiêu chuẩn | external API, file, message, hệ thống liên kết |
| risk-hotspot-map.md | Bắt buộc | Vị trí dễ vỡ khi thay đổi |
| generated-vendor-deadcode-map.md | Tiêu chuẩn | Nhận diện generated artifact, vendor, dead code |
| source-confidence-score.md | Bắt buộc | Độ chắc của phân tích và điểm cần con người xác nhận |
| impact-slice.md | Bắt buộc | Context tối thiểu cần thiết cho thay đổi lần này |

## 5. Heavy Source Analysis Plan

```md
# Heavy Source Analysis Plan

## 1. Metadata
- Ticket / PR:
- Date:
- Owner:
- Related SDD Mode:
- Advanced Option Selection Record:

## 2. Analysis Goal
- Điều bắt buộc phải hiểu trước khi triển khai:
- Điều không được suy diễn khi không có bằng chứng:
- Các quyết định kỳ vọng sau phân tích:

## 3. Repository Scope
| Repo | Branch/Commit | Include | Exclude | Reason |
|---|---|---|---|---|

## 4. Source Priority
1. Latest source:
2. Tests:
3. DB / migration:
4. API contract:
5. Architecture docs:
6. Issue / ticket:
7. Old docs:

## 5. Context Budget
- Max token budget:
- Max files to inspect in round 1:
- Expansion condition:
- Compression strategy:

## 6. Required Maps
- Repository Inventory: Yes/No
- Entry Point Map: Yes/No
- Call Graph: Yes/No
- DB Map: Yes/No
- External IF Map: Yes/No
- Risk Hotspot Map: Yes/No

## 7. Stop / Ask Conditions
- Missing latest source:
- Missing DB definition:
- Missing API contract:
- Build/test cannot run:
- Conflicting documents:

## 8. Human Verification Points
- Các hạng mục AI không được tự quyết định:
```

## 6. Source Availability Advanced

Kiểm tra sâu hơn Source Availability thông thường ở các điểm sau.

```md
# Source Availability Advanced

## 1. Verdict
- Proceed / Proceed with constraints / Stop:
- Reason:

## 2. Source Snapshot
| Source | Version / Commit | Available | Freshness | Confidence | Notes |
|---|---|---|---|---|---|

## 3. Missing Critical Sources
| Missing source | Why critical | Expected impact | Required action |
|---|---|---|---|

## 4. Conflicts
| Conflict | Source A | Source B | Impact | Decision |
|---|---|---|---|---|

## 5. AI Assumptions Prohibited
- DB column names:
- API request/response:
- Permission rule:
- Business rule:
- Batch timing:

## 6. Proceed Conditions
- Minimum evidence required:
- Human decision required:
```

### Điều kiện Stop

Không chuyển sang triển khai trong các trường hợp sau.

```text
- Không đọc được latest source
- Không đọc được definition/migration của DB thuộc đối tượng thay đổi
- API contract không rõ nhưng lại định thay đổi cả FE/BE
- Spec phân quyền không rõ nhưng lại định thay đổi kiểm soát quyền
- Không rõ existing test nằm ở đâu
- Các tài liệu quan trọng mâu thuẫn nhau và chưa xác định source of truth
```

## 7. Repository Inventory

```md
# Repository Inventory

## 1. Overview
- Repository:
- Primary language:
- Secondary languages:
- Framework:
- Runtime:
- Package manager:
- Build system:
- Test framework:

## 2. Top-level Structure
| Path | Purpose | Include in AI context? | Notes |
|---|---|---|---|

## 3. Important Config
| File | Purpose | Risk | Notes |
|---|---|---|---|

## 4. Generated / Vendor / Do-not-edit
| Path | Type | Reason to exclude | Exception |
|---|---|---|---|

## 5. Tests
| Path | Test type | Related source | How to run |
|---|---|---|---|

## 6. High-risk Areas
| Area | Why risky | Evidence |
|---|---|---|

## 7. Project-specific Rules
- Must follow:
- Must not use:
- Existing good examples:
- Known bad examples:
```

## 8. Architecture / Module Map

### 8.1 Mục đích

Giúp AI và con người hiểu toàn bộ Repository ở cùng một mức hạt thông tin. Đặc biệt cần trực quan hóa vi phạm layer, phụ thuộc vòng, component dùng chung ẩn, generated code, phụ thuộc cấu hình.

```md
# Architecture / Module Map

## 1. Logical Layers
| Layer | Main paths | Responsibility | Forbidden dependency |
|---|---|---|---|

## 2. Module Map
| Module | Purpose | Owners | Depends on | Used by | Risk |
|---|---|---|---|---|---|

## 3. Boundary Rules
- UI boundary:
- API boundary:
- Domain boundary:
- DB boundary:
- External IF boundary:

## 4. Known Architecture Exceptions
| Exception | Reason | Risk | Expiry / Follow-up |
|---|---|---|---|
```

### 8.2 Góc nhìn review

```text
- Có phụ thuộc vào layer vốn không được phép phụ thuộc không
- Domain logic có bị rò rỉ sang controller hoặc UI không
- Repository có ôm quá nhiều business rule không
- Common module có phình to quá mức không
- Có định chỉnh tay generated code không
```

## 9. Entry Point Map

```md
# Entry Point Map

| Entry type | Path / Route / Job | Handler | Downstream | Auth/Permission | Test | Notes |
|---|---|---|---|---|---|---|
| Web UI | | | | | | |
| API | | | | | | |
| Batch | | | | | | |
| Scheduler | | | | | | |
| Message/Event | | | | | | |
| CLI | | | | | | |
| Webhook | | | | | | |
```

Các entry point dễ bị bỏ sót.

```text
- cron / scheduler
- retry worker
- queue consumer
- webhook
- admin endpoint
- internal API
- migration script
- data repair script
- hidden path qua feature flag
```

## 10. Call Graph / Dependency Map

Nếu tạo Call Graph quá chi tiết thì sẽ khổng lồ. Trong SDD, tạo chủ yếu quanh **Impact Slice** liên quan đến đối tượng thay đổi.

```md
# Call Dependency Map

## 1. Target Function / Endpoint
- Entry:
- Changed functions:
- Related data:

## 2. Callers
| Caller | File | Why relevant | Confidence |
|---|---|---|---|

## 3. Callees
| Callee | File | Side effect | Risk |
|---|---|---|---|

## 4. Side Effects
- DB write:
- External API:
- Message publish:
- File output:
- Cache update:
- Audit log:

## 5. No-impact Decision
| Area | Reason no impact | Evidence |
|---|---|---|
```

### Chú ý khi tạo Call Graph

```text
- Không kết luận dynamic dispatch chỉ bằng static analysis
- Kiểm tra DI/container setting
- Không bỏ sót reflection / annotation / convention-based routing
- Tìm event handler / listener / interceptor
- Kiểm tra AOP / middleware / filter / guard
- Bổ sung path gọi thực tế từ test
```

## 11. Data / DB / Migration Map

```md
# Data / DB / Migration Map

## 1. Tables / Collections
| Table | Purpose | Owner module | Related entity | Risk |
|---|---|---|---|---|

## 2. Columns / Fields Impact
| Table | Column | Type | Nullable | Validation | Used by | Notes |
|---|---|---|---|---|---|---|

## 3. Query Map
| Query / Repository | File | Tables | Where condition | Lock/transaction | Risk |
|---|---|---|---|---|---|

## 4. Migration Map
| Migration | Type | Reversible | Backfill | Lock risk | Rollback |
|---|---|---|---|---|---|

## 5. Data Quality Assumptions
- Null existing data:
- Invalid legacy values:
- Full-width numeric:
- Mixed charset:
- Duplicate records:
- Orphan records:
```

### Những điểm bắt buộc xem khi phân tích DB

```text
- DB definition và validation có khớp nhau không
- Số chữ số, scale, nullable của FE/BE/DB có khớp nhau không
- Dữ liệu hiện hữu có giá trị không thỏa constraint mới không
- Migration có chạy lại được không
- Có rollback được không
- Có ảnh hưởng lock trên large table không
- Có phải xem query plan cho thay đổi này không
```

## 12. External Interface / Batch / Event Map

```md
# External Interface / Batch / Event Map

## 1. External APIs
| API | Direction | Contract | Auth | Timeout | Retry | Owner | Risk |
|---|---|---|---|---|---|---|---|

## 2. File Interfaces
| File | Direction | Format | Encoding | Schedule | Error handling | Risk |
|---|---|---|---|---|---|---|

## 3. Batch Jobs
| Job | Trigger | Input | Output | Idempotent | Retry | Monitoring | Risk |
|---|---|---|---|---|---|---|---|

## 4. Events / Messages
| Topic/Event | Producer | Consumer | Schema | Compatibility | DLQ | Risk |
|---|---|---|---|---|---|---|
```

## 13. Generated / Vendor / Dead Code Map

```md
# Generated / Vendor / Dead Code Map

| Path | Type | Editable? | Generation source | Risk if edited | Notes |
|---|---|---|---|---|---|

## Dead Code Candidates
| Path | Why suspected | Evidence | Safe to ignore? | Human decision |
|---|---|---|---|---|
```

AI không được tự ý xóa code có vẻ là dead code. Việc xóa phải được tách thành ticket riêng, kèm usage evidence và phê duyệt của con người.

## 14. Risk Hotspot Map

```md
# Risk Hotspot Map

| Hotspot | Category | Why risky | Evidence | Required review | Required test |
|---|---|---|---|---|---|
| Authorization | Security | | | Security Human | Permission test |
| Money / quantity | Business | | | Domain owner | Boundary test |
| DB migration | Data | | | DBA/Tech Lead | Dry-run |
| External IF | Integration | | | Integration owner | Contract test |
| Batch retry | Operation | | | SRE/Ops | Idempotency test |
```

Hotspot phải được phản ánh vào Review Checklist và Test Plan.

## 15. Source Confidence Score

Lượng hóa độ chắc của source mà AI đã đọc. Đây không phải “sự tự tin của AI”, mà là **độ mạnh của bằng chứng**.

| Score | Ý nghĩa | Ví dụ |
|---:|---|---|
| 5 | Đã xác nhận bằng latest source + test + kết quả chạy | build/test thành công, có related test |
| 4 | Đọc được latest source và related test | Chưa chạy test nhưng path rõ |
| 3 | Đọc được source nhưng thiếu test/DB/contract | Vẫn còn suy đoán triển khai |
| 2 | Chủ yếu dựa vào document, source không đủ | Có khả năng tài liệu cũ |
| 1 | Nhiều suy đoán | Bắt buộc con người xác nhận |
| 0 | Không thể phán định | Stop |

```md
# Source Confidence Score

| Area | Score | Evidence | Missing | Risk | Required action |
|---|---:|---|---|---|---|
```

## 16. Impact Slice

Impact Slice là context tối thiểu để chuyển cho 42/43/44 Agent.

```md
# Impact Slice

## 1. Change Target
- Endpoint / screen / job:
- Main files:

## 2. Required Context
| Context | Why needed | File/Section | Include level |
|---|---|---|---|

## 3. Excluded Context
| Context | Reason excluded | Risk |
|---|---|---|

## 4. Related Tests
| Test | Reason | Run command |
|---|---|---|

## 5. Related Contracts
- API:
- DB:
- Event:
- Permission:

## 6. Risk Hotspots
- Hotspot:
- Required reviewer:

## 7. Agent Context Partitioning Hint
| Agent | Must read | Should not read |
|---|---|---|
```

## 17. Góc nhìn bổ sung theo từng Tech Stack

### 17.1 Java / Spring

```text
- Layer Controller / Service / Repository / Mapper
- Bean definition, DI, Profile
- Transaction boundary
- Validation annotation và DB constraint
- Filter / Interceptor / AOP
- MyBatis / JPA / native query
- Phụ thuộc module Maven/Gradle
```

### 17.2 TypeScript / React / Next.js

```text
- route / page / component / hook / API client
- boundary giữa server component / client component
- hydration / cache / server action
- validation schema
- generated API client
- state management
- accessibility / error boundary
```

### 17.3 C# / .NET

```text
- Controller / Service / Repository
- middleware / filter / attribute
- DI lifetime
- Entity Framework migration
- async/await và deadlock
- nullable reference types
- config binding
```

### 17.4 PHP / Laravel

```text
- route / controller / service / model
- middleware / policy / gate
- request validation
- migration / seeder
- queue / job / event listener
- config/cache/artisan command
```

### 17.5 Python / FastAPI / Django

```text
- route / dependency injection
- pydantic schema
- ORM migration
- trộn async/sync
- middleware
- celery / background job
- settings / environment
```

## 18. Prompt Heavy Source Analysis

```md
Bạn là Repository Intelligence Analyst của SDD Ver.04.
Chưa thực hiện triển khai; hãy thực hiện Heavy Source Analysis cho repo mục tiêu.

# Input
- Ticket / PR:
- Tóm tắt thay đổi:
- repo/branch mục tiêu:
- source được phép đọc:
- source không được phép đọc:
- token budget:
- artifact SDD liên quan:

# Quy tắc bắt buộc
- Không triển khai
- Không viết suy đoán như sự thật
- Tách riêng source đã đọc và source chưa đọc
- Khi nói “không ảnh hưởng”, phải ghi bằng chứng
- Không suy đoán DB/API/quyền/external IF
- Nếu có nguy cơ vượt token budget thì thu hẹp vào Impact Slice

# Output
1. Source Availability Advanced
2. Repository Inventory
3. Architecture / Module Map
4. Entry Point Map
5. Call Dependency Map
6. Data / DB / Migration Map
7. External IF / Batch / Event Map
8. Risk Hotspot Map
9. Source Confidence Score
10. Impact Slice
11. Điều kiện Stop / Ask
12. Những điểm cần phản ánh vào Spec Pack / Review Checklist / Test Plan
```

## 19. Human Review Checklist

```text
- AI có đang xem latest branch/commit không
- AI có phán định mà chưa đọc source quan trọng không
- AI có định chuyển sang triển khai ở vùng Source Confidence Score thấp không
- Phán định không ảnh hưởng có căn cứ không
- Có xử lý nhầm generated/vendor/dead code thành đối tượng thay đổi không
- Có suy đoán ở DB/API/quyền/external IF không
- Risk Hotspot có được phản ánh vào Review/Test không
- Impact Slice có thiếu hoặc thừa không
- Có vì tiết kiệm token mà làm rơi một dòng quan trọng không
```

## 20. Failure Mode

| ID | Failure Mode | Prevention |
|---|---|---|
| HSA-001 | Ưu tiên tài liệu thiết kế cũ hơn source | Source Priority Rule |
| HSA-002 | Sinh SQL khi chưa có DB definition | Source Availability Stop |
| HSA-003 | Chỉ nhận nhầm API là entry và bỏ sót Batch | Entry Point Map |
| HSA-004 | Sửa tay generated code | Generated Code Map |
| HSA-005 | Đưa toàn bộ file cho AI gây nhiễm context | Impact Slice + 44 |
| HSA-006 | Khẳng định “không ảnh hưởng” không căn cứ | No-impact Evidence |
| HSA-007 | Sai method riêng của framework | 34 Project Knowledge |
| HSA-008 | Bỏ sót dynamic dispatch / DI | Kiểm tra DI/config |
| HSA-009 | Phán định an toàn khi chưa xác nhận test | Tool-Grounded Verification |
| HSA-010 | Tiết kiệm token làm rơi kiểm tra authorization | Compression Safety |

## 21. Definition of Ready

```text
- Theo 28, có lý do áp dụng Heavy Source Analysis
- 31 Context Loading đã định nghĩa include/exclude
- 33 có nơi lưu artifact
- latest source/branch/commit rõ ràng
- Có token budget
- Điều kiện human review trước khi chuyển sang triển khai rõ ràng
```

## 22. Definition of Done

```text
- Có Heavy Source Analysis Plan
- Có Source Availability Advanced
- Có đủ artifact Repository Intelligence
- Đã gán Source Confidence Score
- Impact Slice ở mức hạt có thể chuyển cho 42/43/44
- Điều kiện Stop/Ask đã được giải quyết hoặc ghi nhận
- Đã phản ánh vào Spec Pack / Review Checklist / Test Plan
- Đã trích xuất tri thức cần đăng ký vào 29/34
```

---

## 23. Thiết kế các vòng phân tích

Heavy Source Analysis không đào sâu ngay từ đầu. Hãy chia thành các Round.

| Round | Mục đích | Đọc gì | Output | Điều kiện đi tiếp |
|---|---|---|---|---|
| R0 | Intake | repo tree, README, build files | Bản nháp Repository Inventory | Đã thấy các module chính |
| R1 | Bản đồ tổng thể | route/config/module/test dirs | Architecture/Entry Map | Đã thấy entry và layer |
| R2 | Vùng quanh thay đổi | changed files, callers/callees | Impact Slice | Đã thấy change path |
| R3 | Dữ liệu/tác dụng phụ external | DB, API, events, batch | Data/External Map | Đã thấy side effect |
| R4 | Tập trung rủi ro | auth, validation, transaction, retry | Risk Hotspot | Có được góc nhìn review/test |
| R5 | Chuẩn bị kiểm chứng | tests, CI, scripts | Tool Matrix | Có thể chuyển cho 43 |

Ở mỗi Round, cần kiểm tra `có còn đáng đọc thêm không` và `source đang đọc có cần cho phán định lần này không`.

## 24. Source Expansion Strategy

```text
Level 0: issue / PR / spec summary
Level 1: changed files
Level 2: direct callers/callees
Level 3: entry points and tests
Level 4: DB/API/contracts/events
Level 5: framework/config/interceptor/middleware
Level 6: historical patterns / previous incidents
Level 7: full file or full module only when necessary
```

Điều kiện mở rộng.

```text
- side effect của changed function không rõ
- caller có nhiều và có vẻ khác hành vi
- auth/permission nằm ở phía middleware
- transaction được quản lý ở layer khác
- validation phân tán ở FE/BE/schema
- test thất bại và root cause có vẻ nằm ở vùng xung quanh
```

Điều kiện không mở rộng.

```text
- vùng generated/vendor
- module không liên quan
- archived/old docs
- binary artifacts
- build outputs
- đã có đủ căn cứ không ảnh hưởng
```

## 25. Tư tưởng thiết kế lệnh hỗ trợ Static Analysis

Lệnh cụ thể tùy project, nhưng AI cần có các góc nhìn tìm kiếm như sau.

```text
- đọc file tree
- tìm entry point candidate
- tìm route / controller / handler
- grep changed symbols
- tìm callers / references
- tìm DB table/column name
- tìm validation rule
- tìm permission/auth check
- tìm test name và fixture
- loại trừ vùng generated/vendor/deprecated
```

Nếu cho phép AI chạy shell, phải tuân theo quy tắc quyền của 25/45. Cấm hoặc yêu cầu human approval đối với lệnh nguy hiểm, thao tác ghi, network, tham chiếu secret.

## 26. Repository Intelligence Review Board

Với dự án quy mô lớn, không để một người duy nhất phê duyệt kết quả phân tích.

| Góc nhìn | Reviewer | Nội dung xác nhận |
|---|---|---|
| Architecture | Tech Lead | Layer, dependency, module boundary |
| Domain | Domain owner | Thuật ngữ nghiệp vụ, tính toán, chuyển trạng thái |
| DB | DBA/Backend lead | table, migration, query |
| Security | Security reviewer | auth, secret, PII, audit |
| Ops | SRE/Ops | batch, retry, monitoring, rollback |
| QA | QA/Test lead | test coverage, regression |

## 27. Quy tắc đặc biệt cho Large Legacy Analysis

Trong Legacy, source không nhất thiết là đúng. Tuy nhiên, implementation đang thực sự chạy ở production là bằng chứng hiện trạng mạnh hơn tài liệu spec.

```text
- Chính bản của business spec
- Hiện trạng implementation
- Hiện trạng DB
- Workaround trong vận hành
- Hành vi người dùng thực sự kỳ vọng
```

Hãy tách riêng và ghi nhận các điều này.

```md
# Legacy Behavior Record

## Observed Behavior
- Source behavior:
- DB behavior:
- Test behavior:
- Production/operation behavior:

## Intended Behavior
- Spec says:
- Business owner says:

## Gap
- Difference:
- Risk:
- Decision required:
```

## 28. Cách nâng Source Confidence

```text
- Không chỉ đọc source, mà còn đọc test
- Không chỉ đọc test, mà còn xem kết quả chạy
- Xem DB definition và migration
- Đối chiếu API contract với actual controller
- Đối chiếu FE validation với BE validation
- Kiểm tra freshness của old docs
- Đọc existing correct implementation example từ 34
- Dùng build/typecheck để phát hiện method không tồn tại
- Xác nhận điểm chưa rõ với human owner
```

## 29. Phản ánh từ Repository Intelligence sang các artifact khác

| Artifact 41 | Nơi phản ánh |
|---|---|
| Source Availability Advanced | spec-pack Source Availability Summary |
| Entry Point Map | spec-pack impact / review checklist |
| DB Map | test plan / migration plan |
| Risk Hotspot Map | review checklist / human review |
| Source Confidence Score | impl-plan constraints / PR decision |
| Impact Slice | 42 Agent context / 44 token plan |
| Generated Code Map | project knowledge / denylist |
| External IF Map | contract test / ops runbook |

## 30. Prompt review hoàn tất Repository Intelligence

```md
Bạn là Tech Lead Reviewer của SDD Ver.04.
Hãy review artifact Repository Intelligence và phán định có được chuyển sang triển khai hay không.

# Input
- Heavy Source Analysis Plan
- Source Availability Advanced
- Repository Inventory
- Architecture / Entry / Call / DB / External Maps
- Risk Hotspot Map
- Source Confidence Score
- Impact Slice

# Góc nhìn phán định
- Có thiếu source quan trọng không
- Phán định không ảnh hưởng có căn cứ không
- Suy đoán và sự thật có được tách riêng không
- Risk Hotspot có thể phản ánh vào Review/Test không
- Có làm rơi thông tin quan trọng do tiết kiệm token không
- Các điểm cần human confirmation có được nêu rõ không

# Output
1. Proceed / Proceed with constraints / Stop
2. Thiếu sót phân tích cần sửa
3. Hạng mục cần con người xác nhận
4. Góc nhìn cần phản ánh vào Review/Test/Security
5. Tính phù hợp của Impact Slice chuyển cho 42/43/44
```

## Tài liệu tham khảo / tiêu chuẩn công khai đã tham chiếu

Các Advanced Options này lấy tài liệu SDD nội bộ, các artifact V04 của 11 và 21〜29・31〜34, tài liệu đính kèm “AI精度向上のための追加戦略_20260516.md” và “AIトークン削減のための追加戦略_20260516.md” làm input chính, đồng thời chuyển hóa tư tưởng của các tài liệu/tiêu chuẩn công khai sau vào ngữ cảnh SDD.

- OpenAI Agents SDK: các yếu tố thiết kế Agent như handoffs, guardrails, function tools, MCP server tool calling, sandbox agents.
- OpenAI Prompt Caching / Cost Optimization / Batch API / Flex Processing: exact prefix caching, thiết kế static prefix, xử lý bất đồng bộ/chi phí thấp.
- OpenAI Structured Outputs: nâng cao khả năng xử lý bằng máy và tái lập nhờ structured output theo JSON Schema.
- Model Context Protocol Security Best Practices: vector tấn công đặc thù MCP implementation, quyền hạn, rủi ro tool execution.
- NIST SSDF SP 800-218: secure development practices có thể tích hợp vào Secure SDLC.
- OWASP ASVS / OWASP LLM Top 10 / OWASP GenAI Security: bảo mật Web/API và rủi ro đặc thù LLM/Agent.
- SLSA / OpenSSF Scorecard: đánh giá software supply chain, dependency, build evidence, sức khỏe OSS.
- OpenTelemetry GenAI semantic conventions: thiết kế quan sát cho AI/Agent call, tool call, latency, token, error.
- Recursive Multi-Agent Systems: nghiên cứu xem Multi-Agent collaboration như recursive computation. Trong thực tiễn chỉ áp dụng hạn chế theo hướng RecursiveMAS-inspired.
- LongLLMLingua / Prompt Compression: tư tưởng về mật độ thông tin quan trọng, position bias, nén trong context dài.
- RTK / Rust Token Killer: tư tưởng thực tiễn giảm token trước khi đưa output CLI vào LLM context.
- SWE-bench / SWE-bench Verified: tham khảo thiết kế dataset đánh giá coding agent và regression evaluation.
- everything-claude-code: tư tưởng vận hành cross-harness như skills, rules, hooks, MCP, security scanning, continuous learning. Tuy nhiên trong SDD chỉ chọn lọc áp dụng một cách an toàn.

---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste

> Appendix này là “execution wrapper” giúp người mới cũng có thể thực hiện Heavy Source Analysis / Repository Intelligence một cách an toàn.  
> Không thay đổi nội dung phần chính. Hãy dùng phần chính như “tập hợp góc nhìn phân tích source nặng và định nghĩa artifact”, còn Appendix này như “cách tiến hành các Round phân tích, nơi lưu, điều kiện dừng, phương pháp review”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

41 là Option nâng cao để đọc Repository sâu hơn khi 23 Source Intelligence thông thường không đủ.  
Người mới không được xem 41 là “công việc đọc tất cả”, mà phải xem là **công việc nâng Confidence bằng cách quyết định thứ tự đọc, tách riêng thứ đã đọc / chưa đọc / chưa rõ**.

```text
1. Không cho AI đọc toàn bộ Repository ngay từ đầu.
2. Trước tiên chỉ yêu cầu Heavy Source Analysis Plan.
3. Không tạo/cập nhật file, không triển khai trước khi con người phê duyệt Plan.
4. Chia các Round phân tích; mỗi Round phải có mục đích, input, output, điều kiện dừng.
5. Về nguyên tắc, không đọc generated / vendor / lock / build output / huge log.
6. Luôn tách riêng file đã đọc, file chưa đọc, file đã loại trừ, suy đoán.
7. Phán định “không ảnh hưởng” phải luôn có căn cứ và Confidence.
8. Không chuyển sang triển khai khi Confidence thấp.
9. Không cho AI đọc Security, secret, PII, production raw log.
10. Cuối cùng thực hiện Repository Intelligence Review và phán định cổng hoàn tất.
```

Nơi lưu cơ bản dùng trong Appendix này như sau.

```text
Artifact riêng cho pack:
docs/changes/{{TICKET}}/41-heavy-source-analysis/

Core artifact của toàn ticket:
docs/changes/{{TICKET}}/impact-analysis.md
docs/changes/{{TICKET}}/impl-plan.md
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/test-plan.md
docs/changes/{{TICKET}}/report.md

Handoff sang Option tiếp theo:
docs/changes/{{TICKET}}/41-heavy-source-analysis/42-handoff.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/43-handoff.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/44-handoff.md

Nơi tạm đặt ứng viên thường trực hóa:
docs/changes/{{TICKET}}/41-heavy-source-analysis/promotion-candidates.md
```

Tư tưởng quan trọng:

```text
Mục tiêu của 41 không phải là “đọc thật nhiều”,
mà là đưa hệ thống về trạng thái có thể giải thích căn cứ Source cần thiết cho thay đổi với Confidence đủ cao.
```

---

## A-1. Khi nào dùng pack này

### Trường hợp nên dùng

```text
- 23 Source Intelligence vẫn để lại bất an về phạm vi ảnh hưởng
- Repository là Legacy, quy mô lớn, phức tạp, phân chia chưa đủ, boundary trách nhiệm mơ hồ
- Liên quan rộng tới Entry Point, Call Graph, DB, external IF, Batch/Event, quyền hạn
- Vùng xung quanh đối tượng thay đổi có sự cố quá khứ, điểm mìn, implementation ngoại lệ, spec ngầm
- Có nhiều file candidate và không chắc cần sửa ở đâu
- Cần giải thích No impact decision trong review
- Muốn tạo Context Slice theo từng Agent trước khi chuyển sang 42 Multi-Agent
- Muốn làm rõ đối tượng kiểm chứng và Tool target trước khi chuyển sang 43 Tool-Grounded Verification
- Muốn quyết định Context Budget trước khi chuyển sang 44 Token Optimization
```

### Trường hợp có thể lightweight hóa

```text
- File mục tiêu rõ ràng, thay đổi đóng trong 1〜2 file
- 23 đã tạo đủ Source Availability, Inventory, Impact Analysis, Confidence
- 28 đã quyết định vận hành lightweight M1/M2
- Không liên quan DB, external IF, Batch/Event, authorization, multi-repo
- Existing test và spec rõ ràng, không cần phân tích bổ sung cho No impact decision
```

Dù lightweight hóa, tối thiểu vẫn cần để lại:

```text
- Lý do lightweight hóa 41
- File đã đọc
- File chưa đọc
- Căn cứ phán định không ảnh hưởng
- Confidence Score
- Trigger cần chạy lại 41 sau này
```

### Không dùng, hoặc quay lại pack khác trước

```text
- Spec chưa xác định, trước tiên cần cố định spec-pack
- Context boundary chưa rõ, trước tiên cần 31 Context Loading
- Tính chính bản / freshness của artifact chưa rõ, trước tiên cần 33 Artifact Governance
- Source Availability đã NG, không thể lấy source cần thiết
- Về bảo mật, chưa đánh giá được có được cho AI đọc source/log mục tiêu hay không
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 41
{{PACK_NAME}}: Heavy Source Analysis and Repository Intelligence Option
{{PACK_SLUG}}: heavy-source-analysis
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{REPOSITORY_SCOPE}}:
{{ANALYSIS_GOAL}}:
{{TARGET_ENTRY_POINTS}}:
{{TARGET_MODULES}}:
{{KNOWN_RISK_AREAS}}:
{{EXCLUDED_PATHS}}:
{{CONFIDENCE_TARGET}}: Low / Medium / High
```

Ví dụ điền:

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{SCOPE_NOTE}}: API tạo invitation, gửi email, quyền hạn, đến E2E
{{RISK_LEVEL}}: High
{{SDD_MODE}}: M3
{{TIMEBOX}}: Lần đầu 90 phút đến bản nháp Repository Intelligence
{{REPOSITORY_SCOPE}}: Phạm vi liên quan trong backend/, frontend/, e2e/
{{ANALYSIS_GOAL}}: Nắm phạm vi ảnh hưởng của thay đổi invite và các điểm mìn hiện có
{{TARGET_ENTRY_POINTS}}: POST /invitations, màn hình Admin Invite
{{TARGET_MODULES}}: invitation, mailer, permission, user
{{KNOWN_RISK_AREAS}}: resend email hiện có, permission check, invitation trùng
{{EXCLUDED_PATHS}}: node_modules, dist, build, coverage, vendor, generated
{{CONFIDENCE_TARGET}}: High
```

---

## A-3. Input đầu tiên cần cho AI đọc

### Input chung cần đọc

```text
@docs/changes/{{TICKET}}/sources.md
@docs/changes/{{TICKET}}/spec-pack.md
@docs/changes/{{TICKET}}/impact-analysis.md
@docs/changes/{{TICKET}}/impl-plan.md
@docs/changes/{{TICKET}}/review-checklist.md
@docs/changes/{{TICKET}}/test-plan.md
@docs/architecture/
@docs/standards/
@.claude/CLAUDE.md
@.claude/rules/
```

### Input đặc biệt cần đọc trong pack này

```text
@docs/changes/{{TICKET}}/23-source-intelligence/source-availability.md
@docs/changes/{{TICKET}}/23-source-intelligence/source-inventory.md
@docs/changes/{{TICKET}}/23-source-intelligence/system-map.md
@docs/changes/{{TICKET}}/23-source-intelligence/entry-point-map.md
@docs/changes/{{TICKET}}/31-context-loading/context-manifest.md
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-inventory.md
@docs/changes/{{TICKET}}/40-advanced-options-selection/advanced-option-selection-record.md
```

### Những thứ đưa vào candidate phân tích

```text
- README / architecture docs
- package.json / pyproject / build files / CI files
- routing / controller / handler / page / component
- usecase / service / domain / repository
- schema / migration / ORM model / query
- permission / auth / guard / middleware
- batch / event / queue / scheduler
- external API client / file interface
- tests: unit / integration / e2e / contract
```

### Những thứ nguyên tắc loại trừ

```text
- node_modules / vendor / dist / build / coverage / tmp
- Toàn bộ generated code. Tuy nhiên có thể đọc public interface khi cần
- Toàn bộ lock file. Tuy nhiên khi điều tra conflict dependency thì tóm tắt phần cần thiết
- Toàn bộ huge log. Chỉ tóm tắt phần cần thiết
- .env / secret / credential / private key / token / cookie / password
- production raw log / dữ liệu chưa mask PII
```

---

## A-4. Artifact cần tạo/cập nhật

### Thư mục riêng của pack

```text
docs/changes/{{TICKET}}/41-heavy-source-analysis/
```

### Artifact tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/41-heavy-source-analysis/heavy-source-analysis-plan.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/source-availability-advanced.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/repository-inventory.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/architecture-module-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/entry-point-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/call-dependency-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/risk-hotspot-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/source-confidence-score.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/impact-slice.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/repository-intelligence-review.md
```

### Artifact cần tạo khi cần

```text
docs/changes/{{TICKET}}/41-heavy-source-analysis/data-db-migration-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/external-interface-batch-event-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/generated-vendor-dead-code-map.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/legacy-behavior-record.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/no-impact-decisions.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/round-log.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/42-handoff.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/43-handoff.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/44-handoff.md
docs/changes/{{TICKET}}/41-heavy-source-analysis/promotion-candidates.md
```

### Nội dung có thể phản ánh vào Core artifact

```text
docs/changes/{{TICKET}}/impact-analysis.md
docs/changes/{{TICKET}}/impl-plan.md
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/test-plan.md
docs/changes/{{TICKET}}/report.md
```

---

## A-5. Quy trình thực thi

Người mới phải luôn chia Round phân tích.

### Round 0. Xác nhận tiền đề

```text
Mục đích: Xác nhận có được thực hiện 41 hay không
Input: Kết quả chọn 40, 31 Context Manifest, 33 Artifact Inventory, artifact 23
Output: heavy-source-analysis-plan.md
Điều kiện dừng: source of truth của spec không rõ, context boundary không rõ, security chưa phán định, thiếu source cần thiết
```

### Round 1. Source Availability Advanced

```text
Mục đích: Xác nhận source bắt buộc đã đủ chưa
Output: source-availability-advanced.md
Kiểm tra: source thiếu, source không đọc được, source cũ, mâu thuẫn
Điều kiện dừng: thiếu source bắt buộc và chỉ có thể bù bằng suy đoán
```

### Round 2. Repository Inventory

```text
Mục đích: Vẽ bản đồ nông toàn bộ Repository
Output: repository-inventory.md
Kiểm tra: top-level structure, config, test, generated/vendor, high-risk areas
Chú ý: Chưa đào sâu
```

### Round 3. Architecture / Module Map

```text
Mục đích: Nắm logical layer, trách nhiệm, hướng phụ thuộc, boundary
Output: architecture-module-map.md
Kiểm tra: module boundary, dependency direction, exception, khác biệt với common rule
```

### Round 4. Entry Point / Call Dependency Map

```text
Mục đích: Nắm entry thay đổi và quan hệ gọi
Output: entry-point-map.md, call-dependency-map.md
Kiểm tra: callers, callees, side effects, căn cứ no-impact decision
```

### Round 5. Data / External / Batch / Event

```text
Mục đích: Nắm ảnh hưởng DB, migration, external IF, batch, event
Output: data-db-migration-map.md, external-interface-batch-event-map.md
Kiểm tra: schema, query, migration, API client, file IF, queue, scheduler
Nếu không áp dụng: Ghi là không thuộc phạm vi và lý do
```

### Round 6. Risk Hotspot / Confidence / Impact Slice

```text
Mục đích: Sắp xếp thành phạm vi ảnh hưởng có thể chuyển sang triển khai
Output: risk-hotspot-map.md, source-confidence-score.md, impact-slice.md
Kiểm tra: critical files, hidden dependencies, tests, confidence, human verification
```

### Round 7. Repository Intelligence Review

```text
Mục đích: Xác nhận có được hoàn tất 41 hay không
Output: repository-intelligence-review.md
Kiểm tra: bỏ sót đọc, đọc quá mức, suy đoán, low confidence, phản ánh vào Core artifact
```

---

## A-6. Dùng để copy-paste: Prompt bắt đầu

```text
Bạn là người hỗ trợ thực thi “41 Heavy Source Analysis and Repository Intelligence Option” của SDD Ver.04.
Chúng ta sẽ lập kế hoạch thực hiện Source Analysis nặng cho {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không đọc toàn bộ Repository ngay lập tức.
- Không triển khai, sửa, refactor, thay đổi CI ngay lập tức.
- Trước tiên chỉ trình bày Heavy Source Analysis Plan.
- Cho đến khi tôi phê duyệt Plan, không tạo/cập nhật file.
- Chia các Round phân tích, nêu rõ mục đích/input/output/điều kiện dừng của từng Round.
- Không đọc generated/vendor/build/dist/coverage/huge log khi không có mục đích.
- Không đọc secret, PII, .env, credential, production raw log.
- Tách riêng file đã đọc, file chưa đọc, file bị loại trừ, suy đoán.
- Phán định không ảnh hưởng phải có căn cứ và Confidence.
- Nếu Confidence thấp thì không chuyển sang triển khai, quay lại xác nhận với con người.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Repository Scope: {{REPOSITORY_SCOPE}}
- Analysis Goal: {{ANALYSIS_GOAL}}
- Target Entry Points: {{TARGET_ENTRY_POINTS}}
- Target Modules: {{TARGET_MODULES}}
- Known Risk Areas: {{KNOWN_RISK_AREAS}}
- Excluded Paths: {{EXCLUDED_PATHS}}
- Confidence Target: {{CONFIDENCE_TARGET}}

【Plan bắt buộc bao gồm】
1. Có cần áp dụng 41 hay không
2. Thiết kế các Round phân tích
3. File candidate sẽ đọc trong từng Round
4. File không đọc trong từng Round và lý do loại trừ
5. Artifact sẽ tạo/cập nhật và nơi lưu
6. Source Priority
7. Context Budget
8. Điều kiện Stop/Ask
9. Human Verification Points
10. Dự kiến Handoff sang 42/43/44
11. Cổng hoàn tất

Trước tiên chỉ trình bày Plan. Chưa chỉnh file, chưa triển khai.
```

---

## A-7. Dùng để copy-paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật artifact của 41 Heavy Source Analysis theo từng Round.

【Quy tắc thực thi】
- Trước mỗi Round, hãy xác nhận ngắn mục đích và phạm vi đọc.
- Artifact được tạo với tiền đề lưu dưới docs/changes/{{TICKET}}/41-heavy-source-analysis/.
- Trong mỗi artifact, hãy tách riêng file đã đọc, file chưa đọc, file đã loại trừ, suy đoán, Open Questions.
- Phán định không ảnh hưởng phải có căn cứ và Confidence.
- Nếu Confidence thấp hoặc thiếu source bắt buộc thì chuyển thành Stop/Ask.
- Nội dung cần phản ánh vào Core artifact phải nêu rõ file mục tiêu và chương/mục.
- Nội dung muốn phản ánh vào tài liệu thường trực không được cập nhật trực tiếp, mà ghi thành ứng viên trong promotion-candidates.md.
- Sau khi làm xong, hãy tự phán định Repository Intelligence Review và cổng hoàn tất.
```

---

## A-8. Dùng để copy-paste: Prompt review artifact và phán định hoàn tất

```text
Bạn là independent reviewer của SDD Ver.04.
Hãy review các artifact 41 Heavy Source Analysis sau và phán định có được chuyển sang kế hoạch triển khai hoặc Option tiếp theo không.

【Đối tượng review】
@docs/changes/{{TICKET}}/41-heavy-source-analysis/heavy-source-analysis-plan.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/source-availability-advanced.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/repository-inventory.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/architecture-module-map.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/entry-point-map.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/call-dependency-map.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/risk-hotspot-map.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/source-confidence-score.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/impact-slice.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/repository-intelligence-review.md

【Góc nhìn review】
1. Source bắt buộc đã đủ chưa
2. Đã tách riêng thứ đã đọc / chưa đọc / loại trừ / suy đoán chưa
3. Repository Inventory có quá nông hoặc quá sâu không
4. Architecture / Module / Entry Point / Call Graph có đủ và vừa đủ cho đối tượng thay đổi không
5. DB / External IF / Batch / Event đã được xác nhận khi cần chưa
6. No impact decision có căn cứ và Confidence chưa
7. Risk Hotspot có thể phản ánh vào impl-plan/review-checklist/test-plan không
8. Có che giấu vùng Confidence thấp không
9. Nếu cần Handoff sang 42/43/44 thì đã rõ chưa
10. Có đáp ứng cổng hoàn tất không

【Output format】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Missing sources
- Over-read / under-read risks
- Low-confidence areas
- Suspicious no-impact decisions
- Required human verification
- Required Core artifact updates
- Required handoffs to 42/43/44
- Final completion gate checklist
- Next action
```

---

## A-9. Dùng để copy-paste: Prompt trả về sửa lại

```text
Hãy sửa artifact 41 Heavy Source Analysis dựa trên các chỉ摘 review sau.

【Quy tắc sửa】
- Trước khi bắt tay, hãy diễn giải ý định của chỉ摘 bằng 1 dòng.
- Trước tiên liệt kê artifact và Round phân tích bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Với file cần đọc bổ sung, trước tiên nêu rõ mục đích đọc và artifact kỳ vọng.
- Nếu thay đổi No impact decision, hãy cập nhật lý do và Confidence.
- Nếu cần phản ánh vào Core artifact, hãy đề xuất phản ánh vào file nào, chương/mục nào.
- Nội dung phản ánh vào tài liệu thường trực phải ghi thành ứng viên trong promotion-candidates.md.

【Review findings】
Dán chỉ摘 vào đây
```

---

## A-10. Điều kiện Stop/Ask cho người mới

Nếu rơi vào bất kỳ điều kiện nào sau, hãy dừng phân tích và quay lại xác nhận con người.

```text
- Không tìm thấy source bắt buộc, hoặc source đã cũ
- Source of truth của spec và hiện trạng code mâu thuẫn
- Muốn đọc file đã bị loại trừ trong Context Manifest
- Có nguy cơ lẫn secret, PII, production raw log
- Cần đọc generated/vendor mới phán định được nhưng chưa xác định phạm vi đọc
- Không rõ ảnh hưởng DB migration, quyền, external IF, Batch/Event
- Căn cứ No impact decision yếu
- Source Confidence thấp hơn mục tiêu
- Phân tích lan quá rộng và vượt Timebox
- Human Verification Point cần cho quyết định triển khai vẫn chưa giải quyết
```

Output format khi Stop/Ask:

```text
- Stop Reason:
- Impact:
- Missing / conflicting source:
- Confidence impact:
- Human decision required:
- Minimal safe next step:
```

---

## A-11. Cổng hoàn tất

Pack này chỉ được hoàn tất khi thỏa toàn bộ điều kiện sau.

```text
- [ ] Heavy Source Analysis Plan đã được phê duyệt
- [ ] Source Availability Advanced đã được tạo
- [ ] Repository Inventory đã được tạo
- [ ] Architecture / Module / Entry Point / Call Graph đã được tạo đủ mức cần thiết
- [ ] DB / External IF / Batch / Event đã được xác nhận nếu có liên quan
- [ ] Risk Hotspot Map đã được tạo
- [ ] Source Confidence Score đã được tạo và không che giấu vùng low confidence
- [ ] Impact Slice ở mức hạt có thể phản ánh vào impl-plan/review-checklist/test-plan
- [ ] Đã ghi file đã đọc / chưa đọc / đã loại trừ
- [ ] Đã tách riêng suy đoán và sự thật xác định
- [ ] No impact decision có căn cứ
- [ ] Repository Intelligence Review không còn Blocker
- [ ] Đã tạo Handoff sang 42/43/44 nếu cần
- [ ] Đã nêu rõ nội dung cần phản ánh vào Core artifact
```

---

## A-12. Nơi đi tiếp theo

```text
Phạm vi ảnh hưởng đã xác định              → phản ánh vào impl-plan / impact-analysis
Có thêm góc nhìn review                    → phản ánh vào review-checklist
Có thêm góc nhìn test                      → phản ánh vào test-plan
Muốn chia góc nhìn qua nhiều Agent          → chuyển sang 42
Muốn kiểm chứng bằng Tool/CI/test           → chuyển sang 43
Context quá lớn                             → chuyển sang 44
Liên quan Security/MCP/hooks/tool quyền     → chuyển sang 45
Muốn CodeMap/RAG hóa                        → chuyển sang 46
Tiến tới refactor quy mô lớn                → chuyển sang 48
Muốn đưa vào đánh giá/cải thiện             → chuyển sang 49
```

Cuối cùng, hãy tóm tắt kết quả 41 trong `report.md` dưới dạng “Source Analysis Summary” để có thể review lại về sau.
