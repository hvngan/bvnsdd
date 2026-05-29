**Mục lục**
- [48_SDD_Parallel-Worktree-and-Large-Refactoring-Option_Ver.04_Vietnamese](#48_sdd_parallel-worktree-and-large-refactoring-option_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Kết luận quan trọng nhất của 48](#1-kết-luận-quan-trọng-nhất-của-48)
  - [2. Kết nối với 21-47](#2-kết-nối-với-2147)
  - [3. Điều kiện áp dụng](#3-điều-kiện-áp-dụng)
  - [4. Khái niệm cơ bản](#4-khái-niệm-cơ-bản)
  - [5. Các pattern tiêu biểu của song song hóa](#5-các-pattern-tiêu-biểu-của-song-song-hóa)
  - [6. Luồng tổng thể của 48](#6-luồng-tổng-thể-của-48)
  - [7. Danh sách artifact](#7-danh-sách-artifact)
  - [8. Template Parallel Worktree Plan](#8-template-parallel-worktree-plan)
  - [9. Template Worktree Inventory](#9-template-worktree-inventory)
  - [10. Quy tắc đặt tên Branch / Worktree](#10-quy-tắc-đặt-tên-branch--worktree)
  - [11. Agent / Owner Assignment](#11-agent--owner-assignment)
  - [12. Baseline Test / Characterization Test](#12-baseline-test--characterization-test)
  - [13. Trục đánh giá để so sánh các phương án triển khai](#13-trục-đánh-giá-để-so-sánh-các-phương-án-triển-khai)
  - [14. Template Option Record](#14-template-option-record)
  - [15. Diff Comparison Record](#15-diff-comparison-record)
  - [16. Merge Integration Record](#16-merge-integration-record)
  - [17. Nguyên tắc thiết kế Large Refactoring](#17-nguyên-tắc-thiết-kế-large-refactoring)
  - [18. Refactoring Slice Plan](#18-refactoring-slice-plan)
  - [19. Thiết kế Feature Flag / Rollout](#19-thiết-kế-feature-flag--rollout)
  - [20. Khi đi kèm DB / Migration](#20-khi-đi-kèm-db--migration)
  - [21. Khi thay đổi đồng thời FE/BE](#21-khi-thay-đổi-đồng-thời-febe)
  - [22. Khi là Microservice / MultiRepo](#22-khi-là-microservice--multirepo)
  - [23. CI / Test Matrix](#23-ci--test-matrix)
  - [24. Tool Evidence Matrix](#24-tool-evidence-matrix)
  - [25. Conflict Resolution](#25-conflict-resolution)
  - [26. Ràng buộc dành cho AI Agent](#26-ràng-buộc-dành-cho-ai-agent)
  - [27. Quản lý Token / Cost](#27-quản-lý-token--cost)
  - [28. Lưu ý Security / Compliance](#28-lưu-ý-security--compliance)
  - [29. Large Refactoring Review Checklist](#29-large-refactoring-review-checklist)
  - [30. Cách tạo PR cuối cùng](#30-cách-tạo-pr-cuối-cùng)
  - [31. Độ lớn Commit / PR](#31-độ-lớn-commit--pr)
  - [32. Rollout / Rollback Plan](#32-rollout--rollback-plan)
  - [33. Dispose / Archive](#33-dispose--archive)
  - [34. Tập prompt dùng cho 48](#34-tập-prompt-dùng-cho-48)
  - [35. Failure Mode](#35-failure-mode)
  - [36. Metrics](#36-metrics)
  - [37. Definition of Ready](#37-definition-of-ready)
  - [38. Definition of Done](#38-definition-of-done)
  - [39. Roadmap triển khai của 48](#39-roadmap-triển-khai-của-48)
  - [40. Tổng kết cuối](#40-tổng-kết-cuối)
  - [41. Tiêu chuẩn tham khảo / tri thức bên ngoài](#41-tiêu-chuẩn-tham-khảo--tri-thức-bên-ngoài)
- [Appendix A. Template thủ tục thực thi git worktree](#appendix-a-template-thủ-tục-thực-thi-git-worktree)
  - [A.1 Xác nhận Baseline](#a1-xác-nhận-baseline)
  - [A.2 Tạo Worktree](#a2-tạo-worktree)
  - [A.3 Khởi tạo theo từng Worktree](#a3-khởi-tạo-theo-từng-worktree)
  - [A.4 Xóa Worktree](#a4-xóa-worktree)
- [Appendix B. Refactor vs Rewrite Decision Matrix](#appendix-b-refactor-vs-rewrite-decision-matrix)
- [Appendix C. Tách biệt Mechanical Change và Logical Change](#appendix-c-tách-biệt-mechanical-change-và-logical-change)
- [Appendix D. Large Refactoring CI Matrix](#appendix-d-large-refactoring-ci-matrix)
- [Appendix E. Do / Do Not để tránh thất bại khi AI làm việc song song](#appendix-e-do--do-not-để-tránh-thất-bại-khi-ai-làm-việc-song-song)
  - [Do](#do)
  - [Do Not](#do-not)
- [Appendix F. Thiết kế Seams / Anti-Corruption Layer](#appendix-f-thiết-kế-seams--anti-corruption-layer)
- [Appendix G. Large Refactoring Maturity Model](#appendix-g-large-refactoring-maturity-model)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-copy-paste)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Artifact cần tạo/cập nhật](#a-4-artifact-cần-tạocập-nhật)
  - [A-5. Quy trình thực thi](#a-5-quy-trình-thực-thi)
  - [A-6. Prompt bắt đầu dùng để copy-paste](#a-6-prompt-bắt-đầu-dùng-để-copy-paste)
  - [A-7. Prompt phê duyệt Plan dùng để copy-paste](#a-7-prompt-phê-duyệt-plan-dùng-để-copy-paste)
  - [A-8. Prompt so sánh phương án triển khai dùng để copy-paste](#a-8-prompt-so-sánh-phương-án-triển-khai-dùng-để-copy-paste)
  - [A-9. Prompt review artifact / phán định hoàn tất dùng để copy-paste](#a-9-prompt-review-artifact--phán-định-hoàn-tất-dùng-để-copy-paste)
  - [A-10. Prompt trả lại để sửa dùng để copy-paste](#a-10-prompt-trả-lại-để-sửa-dùng-để-copy-paste)
  - [A-11. Điều kiện Stop/Ask](#a-11-điều-kiện-stopask)
  - [A-12. Cổng hoàn tất](#a-12-cổng-hoàn-tất)
  - [A-13. Điểm đi tiếp theo](#a-13-điểm-đi-tiếp-theo)

# 48_SDD_Parallel-Worktree-and-Large-Refactoring-Option_Ver.04_Vietnamese

> Loại: SDD Ver.04 Advanced Option  
> Đối tượng: parallel worktree, refactor quy mô lớn, so sánh nhiều phương án triển khai, làm mới legacy, di trú từng phần, tích hợp an toàn nhiều phương án triển khai do nhiều AI tạo  
> Tiền đề: đã áp dụng 11 và 21-29, 31-34, 40-47, hoặc đã có Source Intelligence, Artifact Governance, Security Gate, PR QA Gate tương đương  
> Nguyên tắc: Song song hóa giúp tăng tốc, nhưng cũng làm tăng rủi ro lỗi tích hợp, lẫn lộn diff, không nhất quán artifact. 48 không phải là “tài liệu để làm nhanh hơn”, mà là “tài liệu để đưa song song hóa hội tụ một cách an toàn”.

---

## 0. Vai trò của tài liệu này

Tài liệu này định nghĩa **Parallel Worktree / Large Refactoring** trong nhóm SDD Ver.04 Advanced Options.

48 là tiêu chuẩn thực tiễn để tiến hành an toàn các công việc như sau.

```text
- Muốn triển khai/kiểm chứng đồng thời bằng nhiều AI / nhiều người phụ trách / nhiều phương án
- Muốn chia refactor quy mô lớn thành các diff nhỏ và an toàn
- Muốn di trú từng bước mà không phá vỡ code legacy
- Muốn tiến hành song song các thay đổi xuyên FE/BE/DB/Batch/Microservice
- Muốn so sánh nhiều phương án triển khai và đánh giá tổng hợp theo diff tối thiểu, an toàn, bảo trì, hiệu năng
- Muốn slice hóa diff và đưa vào QA Gate trước khi PR trở nên quá lớn
- Muốn hội tụ nhiều patch do AI tạo thành đơn vị mà con người có thể review
```

Mục đích lớn nhất của tài liệu này là như sau.

```text
Tăng tốc độkhám phá bằng song song hóa.
Tuy nhiên, phải tách biệt nghiêm ngặt artifact, branch, worktree, artifact, test, review và decision,
rồi cuối cùng tích hợp thành diff nhỏ, an toàn, đã được kiểm chứng và có thể rollback.
```

---

## 1. Kết luận quan trọng nhất của 48

Nguyên tắc quan trọng nhất của 48 như sau.

```text
Parallel worktree không phải là cơ chế để cho AI tự do tạo nhiều bản triển khai.
Đây là quy trìnhkhám phá, so sánh và tích hợp được kiểm soát, có giả thuyết, ranh giới, artifact, tiêu chí kiểm chứng và người chịu trách nhiệm tích hợp rõ ràng.
```

Thứ tự cần tuân thủ khi song song hóa như sau.

```text
1. Tách mục đích
2. Tách worktree
3. Tách artifact
4. Tách context
5. Tách kiểm chứng bằng tool
6. So sánh diff
7. Chọn phương án thắng
8. Tạo patch tích hợp
9. Chỉ patch tích hợp mới trở thành PR cuối cùng
10. Hủy hoặc archive các branchkhám phá
```

Các trạng thái tuyệt đối cần tránh như sau.

```text
- Nhiều AI commit trực tiếp vào cùng một branch
- Tiếp tục khi mục đích của phương án triển khai A/B/C còn mơ hồ
- Không biết diff nào tương ứng với artifact nào
- AI đã tạo patch nhưng không có test matrix
- Sau khi tích hợp patch sinh ra, không biết quyết định nào đã dẫn tới việc adopt nó
- PR cuối cùng trở thành hỗn hợp chắp vá của nhiều phương án, không thể review
```

---

## 2. Kết nối với 21-47

| File | Quan hệ với 48 |
|---|---|
| 21 Core Procedures | Chènkhám phá song song, so sánh và tích hợp vào Phase 3-8 |
| 22 Core Prompts | Nền tảng chung cho prompt lập kế hoạch worktree, so sánh phương án triển khai, phán định tích hợp |
| 23 Source Intelligence | Lập bản đồ đối tượng thay đổi trước khi song song hóa |
| 24 Review/TestCode | Định nghĩa quan điểm review/test cho từng worktree |
| 25 Security | Quản lý branch/worktree/quyền AI/secret |
| 26 FE/BE Contract | Giữ tính nhất quán contract khi triển khai FE/BE song song |
| 27 Microservice/MultiRepo | Kiểm soát công việc song song qua nhiều service / nhiều repo |
| 28 RightSizing | Phán định có dùng 48 hay không |
| 29 Failure Mode | Ghi nhận thất bại phát sinh do song song hóa |
| 11 README | Giới thiệu 48 như một Advanced Option |
| 31 Context Loading | Tách context cần đọc theo từng worktree |
| 32 Strategic Compact | Quản lý handoff / resume cho công việc song song |
| 33 Artifact Governance | Quản lý chính bản artifact, decision, evidence theo từng worktree |
| 34 Project Knowledge | Tái sử dụng pattern refactor an toàn trong quá khứ |
| 40 Advanced Overview | Định nghĩa điều kiện áp dụng 48 |
| 41 Heavy Source | Tạo Repo Intelligence trước thay đổi quy mô lớn |
| 42 Multi-Agent | Tách phương án triển khai A/B/C, Reviewer, Arbiter |
| 43 Tool-Grounded | Quyết định adopt phương án triển khai bằng tool evidence |
| 44 Token | Kiểm soát token/cost khi chạy AI song song |
| 45 Security | Quản trị quyền AI agent, sandbox, thao tác write |
| 46 RAG/CodeMap | Chỉ truyền context cần thiết cho từng worktree |
| 47 PR QA Gate | Kiểm chứng patch tích hợp bằng PR Gate |
| 49 Evaluation | Đo lường xem song song hóa có thật sự tạo hiệu quả hay không |

Không được áp dụng 48 khi 33 còn yếu. Công việc song song không truy vết được artifact và decision sẽ tạo ra hỗn loạn thay vì tốc độ.

---

## 3. Điều kiện áp dụng

### 3.1 Điều kiện áp dụng 48

```text
- PR có khả năng trở nên quá lớn
- Có nhiều phương châm triển khai và muốn so sánh, cân nhắc
- Có legacy refactor / replacement / framework migration
- Phạm vi ảnh hưởng lan sang FE/BE/DB/Batch/Microservice
- Muốn kiểm chứng phương án triển khai A/B trong sandbox nhỏ
- Muốn để AI đề xuất nhiều phương án nhưng con người kiểm soát tích hợp cuối cùng
- Cần branch by abstraction / strangler pattern / feature flag / dual run
- Muốn chia thay đổi lớn thành nhiều slice
- Muốn kiểm tra an toàn migration hoặc rollback bằng nhiều phương án
```

### 3.2 Điều kiện không được áp dụng 48

```text
- Sửa typo
- Chỉ README hoặc comment
- Thay đổi rõ ràng trong 1 file
- Test hiện có đã đủ và thay đổi cũng nhỏ
- Không có giá trị khi so sánh nhiều phương án
- Không có người chịu trách nhiệm quản lý worktree
- Không có artifact governance
- Không có test baseline
- Không thể kiểm soát an toàn quyền write của AI agent
- Case mà song song hóa chỉ làm tăng tải review
```

### 3.3 Trigger phát động 48

| Trigger | Mode khuyến nghị | Artifact bắt buộc |
|---|---|---|
| Có từ 2 phương án triển khai trở lên | Alternative Implementation Mode | option-comparison-record.md |
| Có nguy cơ PR khổng lồ | Slice Refactoring Mode | refactoring-slice-plan.md |
| Thay thế Legacy | Strangler / Bridge Mode | migration-roadmap.md |
| FE/BE thay đổi đồng thời | Contract Parallel Mode | fe-be-contract-test-matrix.md |
| Xuyên Microservice | Cross-Service Mode | service-change-sequence.md |
| Có thay đổi DB | Migration Safe Mode | expand-contract-plan.md |
| Cho nhiều AI tạo phương án triển khai | Multi-Agent Worktree Mode | agent-worktree-assignment.md |
| Ảnh hưởng release lớn | Release Safety Mode | rollout-rollback-plan.md |

---

## 4. Khái niệm cơ bản

### 4.1 worktree là gì

`git worktree` là cơ chế liên kết nhiều working tree với một Git repository, giúp có thể checkout đồng thời nhiều branch.

Mục đích trong SDD như sau.

```text
- Tách biệt vật lý các phương án triển khai A/B/C
- Tách vùng làm việc cho từng AI agent
- Kiểm chứng an toàn branch khác
- Tiến hành refactor quy mô lớn theo nhiều slice
- Có thể so sánh và hủy bỏ mà không làm bẩn main worktree
```

### 4.2 Cách dùng khác nhau giữa clone / branch / worktree

| Cách | Phù hợp khi | Lưu ý |
|---|---|---|
| Chỉ branch | Quy mô nhỏ, một người phụ trách | Dễ lẫn lộn khi AI làm song song |
| git worktree | Làm đồng thời nhiều branch trong cùng repo | Cần hiểu `.git` dùng chung |
| repository clone | Cách ly hoàn toàn, dependency/toolchain khác nhau | Tăng disk/cost |
| fork | External collaborator hoặc tách quyền | Cần upstream sync |
| ephemeral sandbox | Thử nghiệm AI, chạy tool nguy hiểm | Cần thiết kế lưu artifact |

### 4.3 Phương châm cơ bản của worktree

```text
- 1 worktree = 1 mục đích
- 1 branch = 1 giả thuyết
- 1 agent = 1 trách nhiệm
- 1 artifact set = 1 worktree
- PR cuối cùng = một chính bản đã tích hợp
```

---

## 5. Các pattern tiêu biểu của song song hóa

### 5.1 Alternative Implementation Pattern

So sánh nhiều phương án.

```text
worktree-A: Phương án diff tối thiểu
worktree-B: Phương án cải thiện thiết kế
worktree-C: Phương án ưu tiên hiệu năng
```

Phán định adopt dựa trên các yếu tố sau.

```text
- Phù hợp acceptance criteria
- Kích thước diff
- Test pass
- Security risk
- Performance
- Maintainability
- Dễ rollback
- Dễ review
```

### 5.2 Slice Refactoring Pattern

Chia refactor lớn thành các slice nhỏ an toàn.

```text
Slice 0: baseline test / characterization test
Slice 1: trích xuất interface
Slice 2: thêm adapter
Slice 3: di trú call site
Slice 4: xóa old path
Slice 5: cleanup
```

### 5.3 Branch by Abstraction Pattern

Tạo ranh giới trừu tượng giữa triển khai cũ và mới, rồi di trú từng bước.

```text
Client
  ↓
Interface / Facade
  ├─ Legacy Implementation
  └─ New Implementation
```

### 5.4 Strangler Fig Pattern

Không thay thế legacy function cùng lúc, mà chuyển dần sang tuyến mới.

```text
routing cũ
  ↓
Gateway / Router
  ├─ legacy handler
  └─ new handler
```

### 5.5 Dual Run / Shadow Mode Pattern

Chạy đồng thời triển khai cũ và mới, rồi so sánh output difference.

```text
request
  ├─ legacy implementation -> user-facing result
  └─ new implementation -> shadow result / comparison only
```

### 5.6 Feature Flag Pattern

Điều khiển triển khai mới bằng flag để rollout / rollback dễ dàng.

```text
if feature_flag_enabled:
    use_new_path()
else:
    use_legacy_path()
```

### 5.7 Expand-Contract Migration Pattern

Với thay đổi DB schema hoặc API contract, di trú từng bước trong khi vẫn giữ compatibility.

```text
Expand:
  Thêm column/API tương thích

Migrate:
  Hỗ trợ cả old/new, backfill, dual write/read

Contract:
  Xóa old column/API
```

---

## 6. Luồng tổng thể của 48

```text
Phase A: Phán định phát động
  ↓
Phase B: Xác nhận nền tảng Repository / Context / Artifact
  ↓
Phase C: Tạo Parallel Worktree Plan
  ↓
Phase D: Chuẩn bị baseline test / characterization test
  ↓
Phase E: Tạo worktree / assignment
  ↓
Phase F: Triển khai / kiểm chứng trong từng worktree
  ↓
Phase G: So sánh diff / thu thập tool evidence
  ↓
Phase H: Arbiter / Human phán định adopt
  ↓
Phase I: Tạo patch tích hợp
  ↓
Phase J: Xác nhận PR QA Gate / Release Safety
  ↓
Phase K: archive / dispose worktree không adopt
  ↓
Phase L: Phản ánh vào Failure Mode / Knowledge / Evaluation
```

---

## 7. Danh sách artifact

Trong 48, lưu các artifact sau dưới Artifact Governance của 33.

```text
docs/maintenance/<ticket>/parallel-worktree/
  00-parallel-worktree-plan.md
  01-worktree-inventory.md
  02-agent-worktree-assignment.md
  03-baseline-test-record.md
  04-option-a-record.md
  05-option-b-record.md
  06-option-c-record.md
  07-diff-comparison-record.md
  08-tool-evidence-matrix.md
  09-merge-integration-record.md
  10-conflict-resolution-record.md
  11-rollout-rollback-plan.md
  12-final-decision-record.md
  13-disposal-record.md
```

---

## 8. Template Parallel Worktree Plan

```md
# Parallel Worktree Plan

## 1. Ticket / Change
- Ticket:
- Objective:
- Risk level:
- SDD Mode:
- Related specs:
- Related artifacts:

## 2. Why Parallelization
- Lý do không tiến hành bằng một branch duy nhất:
- Giả thuyết muốn so sánh:
- Tri thức muốn thu được nhờ song song hóa:
- Rủi ro của song song hóa:

## 3. Worktree Strategy
| Worktree | Branch | Purpose | Agent/Owner | Scope | Do Not Touch | Expected Output |
|---|---|---|---|---|---|---|
| A | sdd/<ticket>/min-patch | Phương án diff tối thiểu | | | | |
| B | sdd/<ticket>/refactor | Phương án cải thiện thiết kế | | | | |
| C | sdd/<ticket>/perf | Phương án ưu tiên hiệu năng | | | | |

## 4. Shared Baseline
- base branch:
- base commit:
- baseline tests:
- baseline failures:
- known issues:

## 5. Test / Tool Matrix
| Tool | Required | Scope | Blocking | Notes |
|---|---:|---|---:|---|
| build | yes | all | yes | |
| unit test | yes | related | yes | |
| integration test | conditional | impacted | yes | |
| contract test | conditional | FE/BE | yes | |
| SAST | conditional | changed | yes if critical | |
| benchmark | conditional | hot path | conditional | |

## 6. Integration Rule
- Tiêu chí adopt:
- Người phụ trách tích hợp:
- Branch tích hợp:
- Cách xử lý worktree không adopt:
- Độ lớn PR cuối cùng:

## 7. Stop Conditions
- Điều kiện bắt buộc human review:
- Điều kiện block:
- Điều kiện abandon:
```

---

## 9. Template Worktree Inventory

~~~md
# Worktree Inventory

| ID | Path | Branch | Base Commit | Owner/Agent | Purpose | Status | Last Sync | Artifact |
|---|---|---|---|---|---|---|---|---|
| A | ../wt-ticket-a | sdd/T-123/min-patch | abc123 | Claude-A | Diff tối thiểu | active | | |
| B | ../wt-ticket-b | sdd/T-123/refactor | abc123 | Codex-B | Cải thiện thiết kế | active | | |

## Commands

```bash
git worktree list
git worktree add ../wt-T123-a -b sdd/T123/min-patch origin/main
git worktree add ../wt-T123-b -b sdd/T123/refactor origin/main
```

## Guardrails
- Không tạo patch thử nghiệm trong main worktree
- Tách branch và artifact theo từng worktree
- Agent không ghi đè worktree ngoài phạm vi được assign
- Chỉ người chịu trách nhiệm tích hợp mới thực hiện merge/rebase
~~~

---

## 10. Quy tắc đặt tên Branch / Worktree

```text
branch:
  sdd/<ticket>/<mode>-<purpose>

examples:
  sdd/ABC-123/min-patch
  sdd/ABC-123/refactor-service-layer
  sdd/ABC-123/perf-query-plan
  sdd/ABC-123/contract-safe
  sdd/ABC-123/integration-final

worktree path:
  ../wt-<ticket>-<purpose>

examples:
  ../wt-ABC-123-min
  ../wt-ABC-123-refactor
  ../wt-ABC-123-final
```

Những điều cần tuân thủ trong đặt tên.

```text
- Bắt buộc chứa ticket ID
- Nêu rõ purpose
- Tách final integration branch
- Không chỉ dùng tên agent làm branch name
- Không merge trực tiếp experimental branch vào main hoặc release
```

---

## 11. Agent / Owner Assignment

Trong 48, dù coi AI Agent như người triển khai, vẫn bắt buộc phải có human owner.

```md
# Agent Worktree Assignment

| Agent | Human Owner | Worktree | Role | Allowed Actions | Forbidden Actions |
|---|---|---|---|---|---|
| Claude-A | TL | A | minimal patch proposer | edit/test in A | push/merge/deploy |
| Codex-B | TL | B | alternative design proposer | edit/test in B | touch A/C |
| Security Reviewer | Sec | all-readonly | review | read/report | edit |
| Arbiter | TL | records only | compare | analyze/report | apply patch |
```

Nguyên tắc như sau.

```text
AI Agent có thể đề xuất patch.
Không được merge, release, deploy, thao tác production.
Thay đổi high-risk bắt buộc cần human approval.
```

---

## 12. Baseline Test / Characterization Test

Với refactor quy mô lớn, phải cố định baseline trước khi triển khai.

### 12.1 Baseline Test Record

```md
# Baseline Test Record

## Base
- branch:
- commit:
- date:

## Commands
| Command | Result | Duration | Notes |
|---|---|---:|---|
| build | pass/fail | | |
| unit test | pass/fail | | |
| integration test | pass/fail | | |
| e2e | pass/fail | | |

## Known Failures
| Test | Since | Owner | Accept? | Reason |
|---|---|---|---:|---|

## Characterization Tests
- Test cố định hành vi hiện tại:
- Hành vi chưa rõ có đúng theo spec hay không nhưng cần duy trì:
- Hành vi được phép thay đổi:

## Decision
- Có adopt làm baseline không:
- Có thể đi tiếp sang công đoạn tiếp theo không:
```

### 12.2 Mục đích của Characterization Test

```text
- Cố định hành vi hiện trạng của legacy
- Phát hiện khác biệt trước/sau refactor
- Trực quan hóa hành vi ngầm không có trong spec
- Dùng cho phán định rollback của thay đổi quy mô lớn
```

---

## 13. Trục đánh giá để so sánh các phương án triển khai

| Trục đánh giá | Nội dung | Ví dụ Weight |
|---|---|---:|
| Correctness | Đáp ứng AC / spec / existing behavior | 25 |
| Safety | security / data loss / rollback risk | 20 |
| Testability | Dễ thêm test, coverage, khả năng tái hiện | 15 |
| Maintainability | Tách trách nhiệm, dễ đọc, dễ thay đổi tương lai | 15 |
| Minimality | Diff nhỏ, dễ review | 10 |
| Performance | latency, DB, memory, hot path | 5-15 |
| Operability | log, metrics, flag, runbook | 10 |
| Migration | deploy order, backfill, compatibility | 10 |
| Cost | AI cost / runtime cost / migration cost | 5 |

Security critical hoặc data loss risk không xử lý bằng weight, mà xử lý như veto.

---

## 14. Template Option Record

```md
# Option Record: <A/B/C>

## 1. Purpose
- Giả thuyết của worktree này:
- Lợi ích kỳ vọng:
- Thứ cố ý hy sinh:

## 2. Changed Files
| File | Change Type | Reason | Risk |
|---|---|---|---|

## 3. Design Summary
- Thiết kế đã adopt:
- Tính nhất quán với thiết kế hiện có:
- Khác biệt so với alternative:

## 4. Tests
| Test | Result | Evidence |
|---|---|---|

## 5. Tool Results
| Tool | Result | Evidence |
|---|---|---|

## 6. Risks
| Risk | Severity | Mitigation | Remaining |
|---|---|---|---|

## 7. Human Review Notes
- reviewer:
- comment:
- decision:

## 8. Recommendation
- adopt / reject / merge_partial / needs_more_test
- reason:
```

---

## 15. Diff Comparison Record

```md
# Diff Comparison Record

## Summary
| Option | LOC +/- | Files | Tests | Security | Perf | Maintainability | Decision |
|---|---:|---:|---|---|---|---|---|
| A Min Patch | | | | | | | |
| B Refactor | | | | | | | |
| C Perf | | | | | | | |

## Finding Matrix
| Finding | A | B | C | Tool Evidence | Human Decision |
|---|---|---|---|---|---|

## Trade-off
| Topic | A | B | C | Chosen |
|---|---|---|---|---|
| Kích thước diff | | | | |
| rollback | | | | |
| future extensibility | | | | |
| testability | | | | |

## Final Decision
- selected option:
- selected partial changes:
- rejected changes:
- reason:
- conditions:
```

---

## 16. Merge Integration Record

```md
# Merge Integration Record

## Source Options
- adopted from A:
- adopted from B:
- adopted from C:
- not adopted:

## Integration Branch
- branch:
- base commit:
- integration owner:

## Conflict Resolution
| File | Conflict | Resolution | Owner | Evidence |
|---|---|---|---|---|

## Final Diff Scope
| File | Reason | Test |
|---|---|---|

## Re-run Tools
| Tool | Result | Evidence |
|---|---|---|

## Final Review
- AI Arbiter:
- Human Reviewer:
- final decision:
```

---
## 17. Nguyên tắc thiết kế Large Refactoring

### 17.1 Small, Safe, Reversible

```text
Dù là refactor quy mô lớn, đơn vị merge vẫn phải nhỏ.
Diff không thể quay lại là diff nguy hiểm.
```

### 17.2 Behavior Preservation First

```text
Bắt đầu từ slice thay đổi cấu trúc bên trong nhưng không thay đổi hành vi bên ngoài.
Không trộn behavior change và structure change trong cùng một PR.
```

### 17.3 Test Net Before Change

```text
Không thực hiện thay đổi quy mô lớn khi không có lưới an toàn.
Trước tiên tạo baseline / characterization / contract / regression test.
```

### 17.4 One Axis per Slice

```text
Trong một slice, chỉ nên có một trục thay đổi chính.
Ví dụ: chỉ rename, chỉ extract interface, chỉ di trú call site.
```

### 17.5 Deployable Every Step

```text
Mỗi slice nên có thể build/test/deploy được.
Cần thiết kế để trạng thái giữa chừng có thể nằm lâu trong main mà không làm hỏng hệ thống.
```

---

## 18. Refactoring Slice Plan

```md
# Refactoring Slice Plan

## Goal
- Trạng thái cuối cùng:
- non-goals:

## Baseline
- current behavior:
- protected behavior:
- known defects:

## Slices
| Slice | Purpose | Files | Behavior Change | Test | Rollback |
|---|---|---|---:|---|---|
| 0 | baseline test | | no | | |
| 1 | interface extraction | | no | | |
| 2 | adapter introduction | | no | | |
| 3 | call site migration | | conditional | | |
| 4 | legacy path removal | | yes | | |

## Merge Policy
- 1 PR per slice:
- combined PR allowed? no by default
- release flag required:

## Risk Controls
- feature flag:
- fallback path:
- monitoring:
- rollback plan:
```

---

## 19. Thiết kế Feature Flag / Rollout

Trong refactor quy mô lớn, feature flag không chỉ là một câu lệnh if, mà là điều khiển vận hành.

```md
# Feature Flag Plan

## Flag
- name:
- owner:
- default:
- environments:
- kill switch:

## Scope
- user segment:
- tenant:
- percentage rollout:
- service:

## Metrics
- success metric:
- error metric:
- latency metric:
- business metric:

## Rollout Steps
| Step | Population | Condition | Action |
|---|---:|---|---|
| 0 | 0% | deploy only | monitor |
| 1 | internal | no error | expand |
| 2 | 1% | no regression | expand |
| 3 | 10% | no regression | expand |
| 4 | 100% | stable | remove legacy |

## Rollback
- how to disable:
- expected recovery time:
- data rollback needed:
```

---

## 20. Khi đi kèm DB / Migration

Trong công việc quy mô lớn có thay đổi DB, cần ưu tiên compatibility và thứ tự deploy hơn là worktree song song hóa.

### 20.1 Migration Safe Mode

```text
1. schema expand
2. code supports old+new
3. backfill idempotent
4. dual read/write if needed
5. monitoring
6. traffic shift
7. contract old schema
```

### 20.2 DB Migration Checklist

```text
- Đã thực hiện migration dry-run chưa
- Có phương châm rollback hoặc forward fix không
- Đã đánh giá thời gian lock chưa
- Backfill có thể chạy lại không
- Có data validation query không
- Code old/new có compatibility không
- Đã nêu rõ thứ tự deploy chưa
- Có thể chuyển đổi bằng feature flag / config không
- Đã đánh giá ảnh hưởng với large table chưa
```

---

## 21. Khi thay đổi đồng thời FE/BE

Khi thay đổi FE/BE đồng thời, chỉ tách worktree theo FE/BE là chưa đủ. Cần đặt contract làm một chính bản duy nhất.

```text
worktree-FE:
  UI / client / validation / state

worktree-BE:
  API / DTO / validation / permission / DB

contract-worktree:
  OpenAPI / Pact / schema / error map / generated client

integration-worktree:
  Xác nhận tích hợp FE+BE
```

Artifact bắt buộc.

```text
- FE/BE Contract Map
- Validation Parity Matrix
- Error Message Map
- Generated Client Record
- Contract Test Result
- Integration Test Result
```

---

## 22. Khi là Microservice / MultiRepo

Với nhiều repo, không chỉ quản lý worktree của một repo mà quản lý như một repo set.

```md
# MultiRepo Worktree Set

| Service | Repo | Worktree | Branch | Purpose | Owner | Deploy Order |
|---|---|---|---|---|---|---|
| api-gateway | | | | route compatibility | | 1 |
| service-a | | | | producer change | | 2 |
| service-b | | | | consumer change | | 3 |

## Cross-Repo Contract
- API:
- event:
- schema:
- versioning:

## Deployment Sequence
1.
2.
3.

## Rollback Sequence
1.
2.
3.
```

Các điểm cần lưu ý.

```text
- Không phá vỡ compatibility giữa producer/consumer
- Xác nhận forward/backward compatibility của event schema
- Artifact hóa deploy order
- So sánh bằng cross-service tracing
- Cân nhắc trạng thái mixed version khi rollback
```

---

## 23. CI / Test Matrix

Trong 48, không chỉ chạy cùng một test cho từng worktree, mà cần thiết kế matrix để so sánh.

```yaml
name: sdd-parallel-worktree-test

on:
  workflow_dispatch:

jobs:
  test-option:
    strategy:
      fail-fast: false
      matrix:
        option: [min-patch, refactor, perf]
        node: [20, 22]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: sdd/ABC-123/${{ matrix.option }}
      - run: npm ci
      - run: npm test
      - run: npm run typecheck
```

Những điều cần tuân thủ khi chạy Matrix.

```text
- Tạo tình huống fail-fast=false để nắm được lỗi của tất cả option
- Kiểm soát cost bằng max-parallel
- Chạy thêm security/test cho option high-risk
- Lưu kết quả matrix vào Tool Evidence Matrix
```

---

## 24. Tool Evidence Matrix

```md
# Tool Evidence Matrix

| Option | Build | Unit | Integration | Contract | E2E | SAST | SCA | Secret | Benchmark | Decision |
|---|---|---|---|---|---|---|---|---|---|---|
| A | | | | | | | | | | |
| B | | | | | | | | | | |
| C | | | | | | | | | | |

## Raw Evidence
- raw logs location:
- compressed logs location:
- CI run URLs:
- artifact hashes:

## Notes
- Khác biệt so với baseline:
- flaky tests:
- accepted failures:
```

---

## 25. Conflict Resolution

### 25.1 Phân loại Conflict

| Conflict Type | Nội dung | Phương châm giải quyết |
|---|---|---|
| textual | Thay đổi cùng dòng | Con người tích hợp |
| semantic | Khác dòng nhưng xung đột về ý nghĩa | design review |
| contract | API/DTO/schema xung đột | Lấy contract làm chính bản |
| test | Expected value của test xung đột | Quay lại AC và Spec |
| migration | Thứ tự DB xung đột | DBA / migration plan |
| security | Ranh giới quyền xung đột | security veto |

### 25.2 Conflict Resolution Record

```md
# Conflict Resolution Record

| File | Conflict Type | Options | Resolution | Reason | Reviewer |
|---|---|---|---|---|---|

## Re-run Required
- tests:
- security:
- contract:
- performance:
```

---

## 26. Ràng buộc dành cho AI Agent

Khi để AI xử lý parallel worktree, bắt buộc áp dụng 45 Agentic AI Governance.

```text
Cho phép AI:
- read/edit trong assigned worktree
- chạy test/lint/typecheck
- tạo patch proposal
- tạo option record
- tạo self-review

Cấm AI:
- push trực tiếp vào main/release branch
- tạo merge commit
- deploy
- thao tác production DB
- tham chiếu secret
- ghi đè worktree của agent khác
- tự ý ghi đè chính bản artifact
```

### 26.1 AI Worktree System Prompt Skeleton

```text
You are assigned to one isolated worktree only.
Do not modify files outside the assigned worktree.
Do not push, merge, deploy, or run destructive commands.
Your output must include:
- changed files
- rationale
- tests run
- risks
- remaining questions
- option record update
If you need broader context, request it instead of guessing.
```

---

## 27. Quản lý Token / Cost

48 dễ làm tăng số lần gọi AI, vì vậy bắt buộc áp dụng 44.

```text
- Không truyền toàn bộ context cho toàn bộ agent
- Tạo diff summary theo từng worktree
- Dùng file summary cache
- Nén tool log
- Chỉ truyền Option Record và Evidence Matrix cho Arbiter, không truyền toàn bộ lịch sử
- Không lưu hội thoại dài của option không adopt, chỉ giữ decision summary
```

### 27.1 Context tối thiểu truyền cho Arbiter

```text
- objective
- acceptance criteria
- option records
- diff summaries
- tool evidence matrix
- unresolved risks
- human notes
```

Những thứ không được truyền.

```text
- Toàn bộ lịch sử hội thoại của từng agent
- Toàn bộ build/test raw log
- Toàn văn file không liên quan
- Giải thích dài của phương án không adopt
```

---

## 28. Lưu ý Security / Compliance

```text
- Không copy secret hoặc .env vào từng worktree
- Đảm bảo local config không bị commit
- Giới hạn ghi ra ngoài sandbox
- Không đặt dữ liệu tương đương production vào branch thử nghiệm AI
- Kiểm tra patch có lẫn secret hoặc credential hay không
- Nếu thay đổi external dependency, chạy SCA/SBOM
- Trước khi archive/delete, kiểm tra cả branch không adopt có lẫn secret không
```

---

## 29. Large Refactoring Review Checklist

```text
## Scope
- Có thể giải thích mục đích thay đổi trong 1 câu không
- Có trộn behavior change và structure change không
- Có thể merge theo đơn vị slice không

## Safety
- Có baseline test không
- Có characterization test không
- Có thể rollback không
- Có cần feature flag không
- Có compatibility old/new không

## Code
- Có phá public API không
- Có thay đổi exception behavior không
- Có thay đổi transaction boundary không
- Có di chuyển/xóa auth/permission check không
- Có duy trì logging / metrics không

## DB / Data
- Migration có theo expand-contract không
- Backfill có idempotent không
- Đã đánh giá large table lock chưa
- Có data validation query không

## Test
- Có test bảo vệ old behavior không
- Có test cho new behavior không
- Đã phán định cần integration/contract/e2e chưa

## Operations
- Có thủ tục rollout không
- Có thủ tục rollback không
- Có monitoring không
- Có runbook không
```

---

## 30. Cách tạo PR cuối cùng

Không được dùng nguyên exploration branch làm PR cuối cùng. PR cuối cùng phải được tạo từ integration branch.

```text
exploration branches:
  sdd/ABC-123/min-patch
  sdd/ABC-123/refactor
  sdd/ABC-123/perf

integration branch:
  sdd/ABC-123/final
```

PR cuối cùng chỉ bao gồm các nội dung sau.

```text
- Diff đã adopt
- Test cần thiết
- Artifact đã cập nhật
- rollout/rollback
- decision record
```

Không bao gồm các nội dung sau.

```text
- Diff dang dở của phương án không adopt
- debug code dùng thử nghiệm
- comment thừa do AI tạo
- raw log
- commit khổng lồ chỉ để giải thích
```

---

## 31. Độ lớn Commit / PR

Đơn vị commit khuyến nghị.

```text
1. test safety net
2. interface / abstraction
3. implementation addition
4. call site migration
5. cleanup
6. docs / artifacts
```

Ví dụ chia PR.

```text
PR-1: baseline/characterization tests
PR-2: abstraction layer only
PR-3: new implementation behind flag
PR-4: dual run / shadow comparison
PR-5: traffic switch
PR-6: legacy removal
```

---

## 32. Rollout / Rollback Plan

```md
# Rollout / Rollback Plan

## Rollout Type
- normal / canary / blue-green / shadow / flag-based:

## Preconditions
- tests:
- monitoring:
- feature flag:
- runbook:

## Rollout Steps
| Step | Action | Validation | Owner | Stop Condition |
|---|---|---|---|---|

## Rollback Steps
| Step | Action | Validation | Owner |
|---|---|---|---|

## Data Considerations
- rollback with data change:
- forward fix:
- manual recovery:

## Communication
- stakeholder:
- support:
- operations:
```

---

## 33. Dispose / Archive

Ngay cả worktree không adopt cũng phải để lại tối thiểu evidence trước khi xóa.

~~~md
# Disposal Record

| Worktree | Branch | Decision | Preserve? | Reason | Action |
|---|---|---|---:|---|---|

## Before Disposal Checklist
- option record saved
- useful learning extracted
- no secret committed
- xác nhận branch protection
- lưu artifact link

## Commands
```bash
git worktree remove ../wt-ABC-123-refactor
git branch -D sdd/ABC-123/refactor
```
~~~

---

## 34. Tập prompt dùng cho 48

### 34.1 Prompt tạo Parallel Worktree Plan

```text
Bạn là Parallel Worktree Planner của SDD Ver.04.
Hãy phán định có nên dùng parallel worktree cho thay đổi mục tiêu theo tiêu chuẩn 48 hay không.

Input:
- ticket / issue
- spec-pack
- source intelligence
- risk classification
- changed/expected areas

Output:
1. Có áp dụng 48 hay không
2. Nếu áp dụng, đề xuất worktree
3. Mục đích của từng worktree
4. Phạm vi do-not-touch
5. baseline test
6. tool matrix
7. integration policy
8. stop conditions
9. lưu ý token/cost
10. security guardrails

Cấm:
- Chỉ tạo nhiều phương án mà không định nghĩa tiêu chí adopt
- Cho phép AI merge/deploy
- Bỏ qua nơi lưu artifact
```

### 34.2 Prompt so sánh phương án triển khai

```text
Bạn là Implementation Arbiter của SDD Ver.04.
Hãy so sánh diff, kết quả test, kết quả review, tool evidence của Option A/B/C và đưa ra phán định adopt.

Tiêu chí phán định:
- correctness
- safety
- testability
- maintainability
- minimality
- performance
- operability
- rollback
- reviewability

Output:
- summary table
- adopted option
- partially adopted changes
- rejected changes
- veto findings
- additional tests required
- human review required
- final integration recommendation

Quan trọng:
Không dùng đa số AI, hãy ưu tiên tool evidence và high-risk veto.
```

### 34.3 Prompt slice hóa Large Refactoring

```text
Bạn là Large Refactoring Strategist.
Hãy chia thay đổi mục tiêu thành các slice có thể merge an toàn.

Output:
- slice list
- behavior change có/không
- test requirements
- rollback strategy
- feature flag requirement
- dependency order
- PR split proposal
- stop conditions

Ràng buộc:
- Về nguyên tắc, mỗi slice phải deployable
- Đặt baseline test trước
- Không trộn behavior change và structure change
```

### 34.4 Prompt Merge Integration Review

```text
Bạn là Merge Integration Reviewer.
Hãy kiểm tra diff được adopt từ exploration worktree sang integration branch, và review xem có lỗi tích hợp không.

Đối tượng kiểm tra:
- conflict resolution
- omitted required change
- accidental adoption of rejected code
- test matrix re-run
- security and contract preservation
- artifact consistency

Output:
- integration risk
- required fixes
- final PR readiness
- human approval checklist
```

---

## 35. Failure Mode

| ID | Failure Mode | Biện pháp |
|---|---|---|
| PWT-001 | Nhiều AI chỉnh cùng một branch | worktree assignment và write guard |
| PWT-002 | Mục đích của phương án triển khai mơ hồ | bắt buộc option hypothesis |
| PWT-003 | Phương án không adopt bị lẫn vào | bắt buộc merge integration record |
| PWT-004 | Không rõ artifact thuộc branch nào | thêm branch/base commit vào artifact front matter |
| PWT-005 | Refactor không có baseline | bắt buộc characterization test |
| PWT-006 | PR cuối cùng trở nên khổng lồ | slice plan và chia PR |
| PWT-007 | Giải quyết conflict máy móc | semantic conflict review |
| PWT-008 | Feature flag trở thành rác tồn đọng | flag removal plan |
| PWT-009 | Dual run ghi log dữ liệu cá nhân | data masking / privacy review |
| PWT-010 | Branch không adopt lẫn secret | secret scan trước disposal |
| PWT-011 | Cost CI song song bùng nổ | 44 token/cost + max-parallel |
| PWT-012 | AI agent vượt quyền | 45 permission broker |
| PWT-013 | Kết quảkhám phá không được Knowledge hóa | promote vào 29/34 |

---

## 36. Metrics

Không đo hiệu quả của 48 chỉ bằng tốc độ.

```text
quality:
- adopted option defect rate
- post-merge regression
- rollback count
- escaped bug count

reviewability:
- final PR size
- review time
- number of review rounds
- conflict count

efficiency:
- elapsed time to safe patch
- AI cost per adopted patch
- discarded worktree cost
- test matrix duration

safety:
- high-risk veto count
- human override count
- rollback readiness score
- secret scan incidents

learning:
- new patterns promoted to 34
- new failure modes registered in 29
```

---

## 37. Definition of Ready

Trước khi bắt đầu 48, cần thỏa mãn các điều kiện sau.

```text
- Lý do dùng 48 rõ ràng
- base commit đã được cố định
- Có source intelligence
- Có phương châm baseline test
- Có nơi lưu artifact
- worktree owner đã được quyết định
- integration owner đã được quyết định
- allowed/forbidden actions đã được quyết định
- Có test/tool matrix
- Có token/cost budget
- Có security guardrail
```

---

## 38. Definition of Done

Điều kiện để nói rằng 48 đã hoàn tất.

```text
- final integration branch đã được tạo
- Lý do adopt / không adopt đã được ghi lại
- final PR nhỏ và có thể review
- required tests đã pass
- security/contract/db/migration check đã hoàn tất
- Có rollout/rollback plan
- disposal của worktree không adopt đã hoàn tất
- Đã đăng ký các mục cần thiết vào 29 Failure Mode
- Đã đăng ký pattern có thể tái sử dụng vào 34 Knowledge Library
- Đã ghi metrics để có thể đo hiệu quả trong 49
```

---

## 39. Roadmap triển khai của 48

```text
Level 0: Chưa áp dụng
  Chỉ làm bằng branch. Không có công việc song song bằng AI.

Level 1: Manual Worktree
  Con người tạo worktree, AI chủ yếu read/review.

Level 2: AI Patch Proposal
  AI tạo patch proposal trong assigned worktree. Không được push/merge.

Level 3: Alternative Comparison
  So sánh Option A/B/C bằng tool evidence, Arbiter đề xuất tích hợp.

Level 4: Slice Refactoring
  Slice hóa refactor quy mô lớn, chuẩn hóa chia PR, rollout, rollback.

Level 5: Integrated Advanced Flow
  Liên động với 42/43/44/45/46/47/49, vận hành đến đánh giá, quan sát và cải tiến liên tục.
```

---

## 40. Tổng kết cuối

48 là tài liệu kiểm soát để sử dụng song song hóa AI một cách an toàn.

```text
Cho nhiều AI tạo nhiều phương án.
Tuy nhiên, tách branch, worktree, artifact, context, tool evidence và decision.

khám phá thì rộng.
Tích hợp thì hẹp.
PR cuối cùng thì nhỏ.
Phán định dựa trên tool-grounded.
High-risk do con người quản trị.
Thất bại và thành công được trả về 29/34/49.
```

Khi tuân thủ các nguyên tắc này, 48 không phải là “công việc song song gây hỗn loạn”, mà trở thành **vận hành SDD nâng cao để tiến hành thay đổi quy mô lớn nhỏ hơn, an toàn hơn, có thể so sánh và có thể rollback**.

---

## 41. Tiêu chuẩn tham khảo / tri thức bên ngoài

Tài liệu này thực tiễn hóa các tri thức bên ngoài sau cho SDD.

```text
- Git worktree: Cơ chế liên kết nhiều working tree vào cùng một repository
- GitHub Actions Matrix Strategy: Thiết kế CI chạy job với nhiều cấu hình
- GitHub Merge Queue: Vận hành merge thỏa required checks trên base branch mới nhất
- OpenFeature: vendor-agnostic feature flag API
- DORA metrics: Cách đo liên tục delivery performance
- SRE rollout / rollback / postmortem culture
- Tài liệu đính kèm chiến lược nâng cao độ chính xác AI: Orchestrator / Multi-Agent / Tool-Grounded / Human Governance
- Tài liệu đính kèm chiến lược giảm token AI: Agent Context Partitioning / State Compression / Cost Observability
```

---

# Appendix A. Template thủ tục thực thi git worktree

Appendix này là ví dụ thao tác tiêu chuẩn khi dùng 48 trong thực tế. Lệnh thực tế cần được điều chỉnh theo vận hành Git, CI, quyền và branch protection của từng công ty.

## A.1 Xác nhận Baseline

```bash
# Cập nhật mới nhất
git fetch --all --prune

# Xác nhận trạng thái trước khi làm việc
git status
git branch --show-current
git rev-parse HEAD

# Ghi lại base commit
BASE_COMMIT=$(git rev-parse origin/main)
echo $BASE_COMMIT
```

Những thứ cần ghi lại:

```text
- base branch
- base commit
- remote URL
- current uncommitted changes
- submodule state
- lockfile state
```

## A.2 Tạo Worktree

```bash
mkdir -p ../worktrees

git worktree add ../worktrees/wt-1234-minimal -b sdd/1234/minimal origin/main
git worktree add ../worktrees/wt-1234-tests -b sdd/1234/tests origin/main
git worktree add ../worktrees/wt-1234-architecture -b sdd/1234/architecture origin/main
git worktree add ../worktrees/wt-1234-integration -b sdd/1234/integration origin/main
```

Sau khi tạo, bắt buộc xác nhận:

```bash
git worktree list
```

## A.3 Khởi tạo theo từng Worktree

```bash
cd ../worktrees/wt-1234-minimal
# Ví dụ: install dependency. Tuy nhiên không copy secret hoặc .env.
# npm ci / mvn test / dotnet restore, v.v.
```

Cấm:

```text
- Copy .env.production
- Triển khai credential cá nhân vào worktree
- Đặt cấu hình kết nối production DB
- AI agent có deploy key
```

## A.4 Xóa Worktree

```bash
git worktree remove ../worktrees/wt-1234-minimal
# metadata cleanup if needed
git worktree prune
```

Trước khi xóa cần lưu:

```text
- diff summary
- adopted/rejected decision
- tool results
- raw logs reference
- AI output summary
- human review notes
```

---

# Appendix B. Refactor vs Rewrite Decision Matrix

| Quan điểm | Khuyến nghị Refactor | Cân nhắc Rewrite | Điều kiện Stop |
|---|---|---|---|
| Hiểu spec hiện có | Có spec và test | Spec không rõ nhưng có thể xác nhận với business owner | Cả spec và owner đều không rõ |
| Chất lượng hiện có | Chủ yếu là vấn đề cấu trúc | Lỗi thường xuyên, technical debt cực lớn | Không thể tái hiện production behavior |
| Quy mô thay đổi | Có thể di trú từng bước | Có thể cắt boundary | Chỉ có thể thay thế toàn bộ cùng lúc |
| Test | Có thể xây safety net | Có thể golden master | Không thể lấy existing behavior |
| Rủi ro nghiệp vụ | Thấp-trung bình | Cao nhưng có thể rollback | Không thể rollback |
| Data migration | Có thể expand-contract | Có thể đồng bộ hai chiều | Rủi ro mất dữ liệu cao |
| Tổ chức | Có thể review | Có team chuyên trách | Owner không rõ |

Nguyên tắc:

```text
Rewrite là lựa chọn cuối cùng.
Tuy nhiên, nếu kéo dài cấu trúc hiện tại về lâu dài còn nguy hiểm hơn, hãy thay thế từng bước bằng Strangler Fig.
```

---

# Appendix C. Tách biệt Mechanical Change và Logical Change

Trong thay đổi quy mô lớn, cả AI và con người dễ mất dấu “thay đổi bản chất”. Hãy tách các loại sau.

```text
Mechanical:
- formatting
- sắp xếp import
- rename
- file move
- cập nhật generated code
- thay đổi package namespace

Logical:
- thay đổi điều kiện rẽ nhánh
- thay đổi phán định quyền
- thay đổi DB write
- thay đổi exception handling
- thay đổi API contract
- thay đổi transaction boundary
```

Ví dụ chia PR:

```text
PR-A: rename only
PR-B: move only
PR-C: abstraction layer
PR-D: logic behind abstraction
PR-E: cleanup
```

Quy tắc review:

```text
- Trong mechanical PR, cấm behavior change
- Trong logical PR, cấm format hàng loạt
- Trong generated PR, cấm thay đổi viết tay
```

---

# Appendix D. Large Refactoring CI Matrix

```yaml
large_refactor_ci:
  base:
    - build
    - unit
    - integration
  compatibility:
    - contract_test
    - generated_client_check
    - openapi_diff
  migration:
    - migration_dry_run
    - backfill_dry_run
    - query_plan
  behavior:
    - characterization_tests
    - golden_master_diff
  security:
    - sast
    - secret_scan
    - dependency_scan
  performance:
    - benchmark_smoke
    - hot_path_regression
  release:
    - rollback_smoke
    - feature_flag_check
```

Không cần luôn chạy toàn bộ CI cho mọi PR. Trong 48, chọn theo slice/risk.

---

# Appendix E. Do / Do Not để tránh thất bại khi AI làm việc song song

## Do

```text
- Đặt một mục đích cho mỗi worktree
- Nêu rõ file được phép chạm cho từng AI
- Tách common context và individual context
- Xem AI output là patch proposal
- Bắt buộc ghi lại adoption decision
- Lưu cả rejected patch làm tư liệu học tập
- Human/arbiter thực hiện integration
```

## Do Not

```text
- Không giao phó một task khổng lồ giống nhau cho nhiều AI
- Không để toàn bộ Agent đọc toàn bộ repo
- Không handoff toàn bộ lịch sử hội thoại tự nhiên giữa các AI
- Không để AI tự merge branch
- Không để AI tự xóa feature flag
- Không traffic switch khi không có rollback plan
```

---

# Appendix F. Thiết kế Seams / Anti-Corruption Layer

Khi di trú từ Legacy sang triển khai mới, hãy tìm seam.

```text
Seam tốt:
- API boundary
- interface boundary
- service boundary
- repository boundary
- event boundary
- facade / adapter boundary

Seam xấu:
- Giữa global mutable state
- Giữa transaction boundary
- Chỉ phía sau security check
- Giữa business invariant
```

Những việc Anti-Corruption Layer làm:

```text
- Chuyển đổi legacy model sang new domain model
- Nêu rõ mapping enum/master value
- Chuyển đổi error code
- Hấp thụ khác biệt validation
- Hấp thụ khác biệt encoding/locale
- Duy trì audit log
```

---

# Appendix G. Large Refactoring Maturity Model

| Level | Trạng thái | Mô tả |
|---|---|---|
| L0 | Ad-hoc | PR khổng lồ, rollback không rõ, phó mặc AI |
| L1 | Sliced | Có chia PR và thêm test |
| L2 | Worktree Governed | Có worktree plan và integration record |
| L3 | Tool-grounded | Kiểm chứng bằng golden/contract/migration/perf |
| L4 | Progressive Delivery | flag/canary/shadow/rollback là tiêu chuẩn |
| L5 | Learning System | Đo bằng 49 và phản ánh liên tục vào 29/34 |

Mục tiêu không phải đưa tất cả lên L5. Với thay đổi quy mô lớn high-risk thì L4-L5, với thay đổi nhỏ thì L1-L2 là đủ.

---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste

> Appendix này là “execution wrapper” để cả người mới cũng có thể thực thi an toàn Parallel Worktree / Large Refactoring được định nghĩa trong phần chính.  
> Không thay đổi nội dung phần chính. Hãy dùng phần chính như “đặc tả thiết kế về worktree, so sánh phương án song song, refactor quy mô lớn, tích hợp, rollback, disposal”, và dùng Appendix này như “quy trình thực hiện theo thứ tự: cố định base, baseline test, tách worktree, so sánh, tích hợp, hủy bỏ”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

48 là Advanced Option để chia nhỏ, so sánh và tích hợp an toàn các thay đổi lớn hoặc refactor.  
Người mới không được xem 48 là “cơ chế cho AI tạo nhiều phương án cùng lúc”, mà phải xem là **cơ chế cố định base commit, tạo baseline test, tách mục đích theo từng worktree, và cuối cùng human/Arbiter tích hợp**.

```text
1. Không tạo worktree, tạo branch, merge, rebase, force push, delete ngay lập tức.
2. Trước tiên chỉ yêu cầu xuất Parallel Worktree Plan.
3. Cho đến khi con người phê duyệt Plan, không tạo worktree, không chỉnh file, không triển khai, không tích hợp, không xóa.
4. Cố định base branch, base commit, baseline test rồi mới song song hóa.
5. Nêu rõ mục đích, owner, file được phép chạm, file không được chạm cho từng worktree.
6. AI output là patch proposal, không phải quyết định adopt hay quyền merge.
7. Không trộn mechanical change và logical change trong cùng PR.
8. Migration, feature flag, rollout, rollback, contract, security bắt buộc phải có human approval.
9. Worktree không adopt cũng phải ghi lại lý do và bài học trước khi dispose.
10. Cuối cùng tạo Integration Review, Tool evidence, Disposal Record, 49 metrics handoff.
```

Nơi lưu cơ bản dùng trong Appendix này như sau.

```text
Artifact riêng của pack:
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/

Ví dụ thực thể worktree:
../worktrees/{{TICKET}}-option-a/
../worktrees/{{TICKET}}-option-b/
../worktrees/{{TICKET}}-slice-01/

Ứng viên đăng ký vào 33 Artifact Governance:
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/33-registration.md

Feedback cho 29/34/49:
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/29-feedback.md
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/34-knowledge-candidates.md
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/49-metrics-handoff.md

Nơi đặt tạm ứng viên thường trực hóa:
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/promotion-candidates.md
```

Cách nghĩ quan trọng:

```text
Mục tiêu của 48 không phải là “tạo thật nhiều thứ song song”,
mà là tiến hành thay đổi lớn theo cách nhỏ, có thể so sánh và có thể quay lại.
```

---

## A-1. Khi nào dùng pack này

### Case nên dùng

```text
- Thực hiện refactor quy mô lớn, di trú, thay thế, chia nhỏ, sắp xếp lại trách nhiệm
- Muốn so sánh nhiều phương án trước khi quyết định một phương án triển khai
- Di trú từng bước từ Legacy sang cấu trúc mới
- Muốn tách mechanical change và logical change
- Liên quan đến DB migration, contract change, feature flag, dual run, shadow mode, rollout/rollback
- Nhiều AI/Agent/con người làm song song
- Muốn kết hợp 42 Multi-Agent, 43 Tool-Grounded, 44 Cost Control, 45 Security, 46 Context Pack
- Muốn tránh PR khổng lồ và chia thành slice có thể review
```

### Case có thể lightweight

```text
- Thay đổi nhỏ, có thể hoàn tất an toàn trong một branch
- Không cần so sánh alternative
- Baseline test đã đủ, chi phí tách worktree cao
- Đã được phán định là vận hành nhẹ M1/M2 trong 28
- Chỉ mechanical change và không có behavior change
```

Ngay cả khi lightweight, tối thiểu vẫn giữ lại các mục sau.

```text
- Lý do lightweight 48
- base commit
- kết quả baseline test
- phương châm chia PR
- phương châm rollback
- Trigger để đánh giá lại 48 sau này
```

### Case không được dùng, hoặc cần quay lại pack khác trước

```text
- Không thể cố định base branch / base commit
- Không có baseline test nên không bảo vệ được hành vi trước thay đổi
- Spec chưa xác định nên trước tiên cần spec-pack
- Source impact không rõ nên trước tiên cần 23 hoặc 41
- CI đang hỏng nên không thể so sánh các phương án song song
- Người phê duyệt Security / migration / rollout không rõ
- Định giao merge, force push, delete, deploy cho AI
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 48
{{PACK_NAME}}: Parallel Worktree and Large Refactoring Option
{{PACK_SLUG}}: parallel-worktree-refactoring
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{INTEGRATION_OWNER}}:
{{REVIEWER}}:
{{BASE_BRANCH}}:
{{BASE_COMMIT}}:
{{REFACTORING_STRATEGY}}: Alternative Implementation / Slice Refactoring / Branch by Abstraction / Strangler Fig / Dual Run / Feature Flag / Expand-Contract / Other
{{WORKTREE_COUNT}}:
{{WORKTREE_NAMES}}:
{{ALLOWED_PATHS}}:
{{FORBIDDEN_PATHS}}:
{{BASELINE_TEST_COMMANDS}}:
{{REQUIRED_TOOL_MATRIX}}:
{{MERGE_POLICY}}:
{{ROLLBACK_OWNER}}:
```

Ví dụ điền:

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Refactor tách trách nhiệm chức năng invitation
{{BRANCH_NAME}}: feature/ABC-123-invite-refactor
{{SCOPE_NOTE}}: Tách invitation service, giữ behavior, giữ API compatibility
{{RISK_LEVEL}}: High
{{SDD_MODE}}: M4
{{TIMEBOX}}: 120 phút đến Plan, baseline, so sánh option
{{HUMAN_OWNER}}: Tech Lead
{{INTEGRATION_OWNER}}: Senior Engineer
{{BASE_BRANCH}}: main
{{BASE_COMMIT}}: ghi giá trị của git rev-parse HEAD
{{REFACTORING_STRATEGY}}: Slice Refactoring + Branch by Abstraction
{{WORKTREE_COUNT}}: 2
{{WORKTREE_NAMES}}: ABC-123-option-a, ABC-123-option-b
{{ALLOWED_PATHS}}: backend/invitation, tests/invitation, docs/changes/ABC-123
{{FORBIDDEN_PATHS}}: auth core, payment, deploy scripts, production config
{{BASELINE_TEST_COMMANDS}}: npm test, npm run typecheck, npm run e2e:invite
{{REQUIRED_TOOL_MATRIX}}: build, unit, integration, e2e, contract, secret scan
{{MERGE_POLICY}}: Chỉ Human Integration Owner tích hợp. AI chỉ đến patch proposal
{{ROLLBACK_OWNER}}: Release Lead
```

---

## A-3. Input đầu tiên cần cho AI đọc

### Input đọc chung

```text
@docs/changes/{{TICKET}}/sources.md
@docs/changes/{{TICKET}}/spec-pack.md
@docs/changes/{{TICKET}}/impact-analysis.md
@docs/changes/{{TICKET}}/impl-plan.md
@docs/changes/{{TICKET}}/review-checklist.md
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
@docs/changes/{{TICKET}}/23-source-intelligence/impact-analysis.md
@docs/changes/{{TICKET}}/41-heavy-source-analysis/impact-slice.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/tool-result-record.md
@docs/changes/{{TICKET}}/44-token-cost-control/token-budget-record.md
@docs/changes/{{TICKET}}/45-full-security-agentic-ai/security-signoff.md
@docs/changes/{{TICKET}}/46-rag-codemap-context-compression/agent-context-packs.md
@docs/changes/{{TICKET}}/47-automated-pr-review-qa-gate/required-tool-matrix.md
```

### Những thứ cần xác nhận trước khi tạo worktree

```text
- git status có clean không
- base branch có mới nhất không
- base commit đã được ghi lại chưa
- baseline test đã chạy chưa
- known failure đã được ghi lại chưa
- worktree name, branch name, owner đã được quyết định chưa
- allowed/forbidden paths đã được quyết định chưa
- có phương châm không copy secrets và .env không
- có thủ tục cleanup/disposal không
```

---

## A-4. Artifact cần tạo/cập nhật

```text
Artifact bắt buộc:
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/README.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/parallel-worktree-plan.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/worktree-inventory.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/baseline-test-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/characterization-test-plan.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/agent-worktree-assignments.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/option-records.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/diff-comparison-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/merge-integration-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/tool-evidence-matrix.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/rollout-rollback-plan.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/disposal-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/review.md
```

Artifact tạo khi cần:

```text
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/refactoring-slice-plan.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/feature-flag-plan.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/db-migration-checklist.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/contract-compatibility-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/conflict-resolution-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/security-compliance-record.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/33-registration.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/29-feedback.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/34-knowledge-candidates.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/49-metrics-handoff.md
- docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/promotion-candidates.md
```

Phản ánh vào Core artifact:

```text
impl-plan.md:
- refactoring slice, worktree strategy, integration order, rollback

review-checklist.md:
- behavior preservation, mechanical/logical separation, contract/db/security/perf

test-plan.md:
- baseline, characterization, golden master, contract, migration dry-run, performance smoke

report.md:
- phương án adopt, phương án không adopt, lý do so sánh, kết quả tích hợp, disposal, rủi ro còn lại
```

---

## A-5. Quy trình thực thi

```text
Step 1. Dán prompt bắt đầu phase chung của 22
Step 2. Dán prompt bắt đầu của 48 và yêu cầu chỉ xuất Parallel Worktree Plan
Step 3. Kiểm tra Plan có base commit, baseline test, worktree owner, allowed/forbidden paths, Stop/Ask không
Step 4. Sau khi Plan được phê duyệt, ghi lại base branch và base commit
Step 5. Tạo Baseline Test Record và Known Failures
Step 6. Tạo Worktree Inventory
Step 7. Tạo Characterization Test Plan
Step 8. Tạo Agent Worktree Assignments
Step 9. Tạo Option Record hoặc Slice Record theo từng worktree
Step 10. Tạo Tool Evidence Matrix
Step 11. So sánh adopt/không adopt bằng Diff Comparison Record
Step 12. Ghi thủ tục tích hợp và xử lý conflict bằng Merge Integration Record
Step 13. Sau khi tích hợp, chạy lại required tools và tạo Evidence có thể truyền cho 43
Step 14. Tạo Rollout / Rollback Plan
Step 15. Tạo Disposal Record cho worktree không adopt
Step 16. Dán prompt review / phán định hoàn tất của 48
```

### Việc có thể giao cho AI / không được giao cho AI

```text
Có thể giao:
- plan draft
- option comparison draft
- patch proposal
- test candidate proposal
- diff summary
- risk list
- review checklist draft

Không được giao:
- merge
- force push
- branch deletion
- worktree deletion without record
- deploy
- DB migration execution
- feature flag production switch
- accepted risk approval
- final adoption decision
```

---

## A-6. Prompt bắt đầu dùng để copy-paste

```text
Bạn là người hỗ trợ thực thi “48 Parallel Worktree and Large Refactoring Option” của SDD Ver.04.
Từ giờ hãy lập kế hoạch an toàn cho thay đổi quy mô lớn hoặc công việc parallel worktree của {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không tạo worktree, tạo branch, merge, rebase, force push, xóa, triển khai ngay lập tức.
- Trước tiên chỉ trình bày Parallel Worktree Plan.
- Cho đến khi tôi phê duyệt Plan, không tạo/cập nhật file, không thao tác git, không thao tác worktree.
- Hãy cố định base branch, base commit, baseline test, known failures trước khi song song hóa.
- AI chỉ đến patch proposal. Quyết định adopt, tích hợp, merge, deploy, DB migration, feature flag switch là hạng mục cần human approval.
- Tách mục đích, owner, allowed paths, forbidden paths, test/tool matrix theo từng worktree.
- Không trộn mechanical change và logical change.
- Giả định không copy secret, .env, credential vào worktree.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Human Owner: {{HUMAN_OWNER}}
- Integration Owner: {{INTEGRATION_OWNER}}
- Base Branch: {{BASE_BRANCH}}
- Base Commit: {{BASE_COMMIT}}
- Refactoring Strategy: {{REFACTORING_STRATEGY}}
- Worktree Count: {{WORKTREE_COUNT}}
- Worktree Names: {{WORKTREE_NAMES}}
- Allowed Paths: {{ALLOWED_PATHS}}
- Forbidden Paths: {{FORBIDDEN_PATHS}}
- Baseline Test Commands: {{BASELINE_TEST_COMMANDS}}
- Required Tool Matrix: {{REQUIRED_TOOL_MATRIX}}
- Merge Policy: {{MERGE_POLICY}}
- Rollback Owner: {{ROLLBACK_OWNER}}

【Plan bắt buộc gồm】
1. Có áp dụng 48 hay không
2. Phương châm base branch / base commit / baseline test
3. worktree strategy và danh sách worktree
4. owner / allowed paths / forbidden paths
5. Phương châm tách mechanical / logical / generated change
6. test/tool matrix
7. Phương châm integration / conflict resolution / rollback
8. Stop/Ask conditions
9. Artifact cần tạo và nơi lưu
10. Handoff sang 43/45/49

Trước tiên chỉ trình bày Plan. Chưa chỉnh file hoặc thao tác git.
```

---

## A-7. Prompt phê duyệt Plan dùng để copy-paste

```text
Tôi phê duyệt 48 Parallel Worktree Plan.
Hãy tạo/cập nhật các artifact của 48 theo đúng thủ tục đã đề xuất.

【Quy tắc thực thi】
- Hãy trình bày nơi lưu và tóm tắt của từng artifact.
- Nếu cần thực sự tạo hoặc xóa git worktree, chỉ trình bày phương án lệnh và chờ con người thực thi hoặc phê duyệt.
- Trước tiên ghi base commit, baseline test, known failures.
- Nêu rõ mục đích, owner, allowed/forbidden paths theo từng worktree.
- Trong so sánh option, ghi cả lý do của phương án adopt và phương án không adopt.
- Giả định integration do human/Integration Owner thực hiện; AI chỉ trình bày phương án tích hợp và rủi ro.
- Chỉ worktree disposal sau khi tạo disposal-record.md.
- Nội dung muốn phản ánh vào rule hoặc standard thường trực thì không cập nhật trực tiếp, mà ghi vào promotion-candidates.md.
- Cuối cùng tự phán định cổng hoàn tất.
```

---

## A-8. Prompt so sánh phương án triển khai dùng để copy-paste

```text
Hãy so sánh các worktree / option sau và tạo Diff Comparison Record để phán định ứng viên adopt.

【Đối tượng so sánh】
- Option A:
- Option B:
- Option C:

【Quan điểm so sánh】
- Đạt AC
- behavior preservation
- diff size
- complexity
- rollback dễ hay khó
- test coverage
- contract / API compatibility
- DB / migration risk
- security / permission risk
- performance risk
- maintainability
- reviewability
- future extensibility

【Quy tắc quan trọng】
- Không quyết định adopt theo sở thích của AI.
- Ưu tiên Tool evidence, baseline test, characterization test, human review notes.
- Tách phương án adopt, phương án không adopt, phương án bảo lưu.
- Final adoption phải là Human Decision Required.

【Output】
docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/diff-comparison-record.md
```

---

## A-9. Prompt review artifact / phán định hoàn tất dùng để copy-paste

```text
Bạn là Large Refactoring Reviewer độc lập của SDD Ver.04.
Hãy review các artifact 48 sau và phán định có thể hoàn tất pack này hay không.

【Đối tượng review】
@docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/
@docs/changes/{{TICKET}}/impl-plan.md
@docs/changes/{{TICKET}}/review-checklist.md
@docs/changes/{{TICKET}}/test-plan.md
@docs/changes/{{TICKET}}/test-results.md
@docs/changes/{{TICKET}}/report.md

【Quan điểm review】
1. Lý do dùng 48 có hợp lý không
2. base branch / base commit / baseline test có được ghi lại không
3. Mục đích, owner, allowed/forbidden paths theo từng worktree có rõ không
4. Có cân nhắc behavior preservation, characterization test, golden master không
5. Mechanical change và logical change có được tách không
6. So sánh option có Tool evidence và human decision không
7. Merge integration, conflict resolution, required tool rerun có được ghi lại không
8. DB / contract / security / performance / rollout / rollback có được xác nhận không
9. Có disposal record và worktree không adopt được xử lý an toàn không
10. Có bài học và metrics cho 29/34/49 không

【Output format】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Missing baseline evidence
- Integration risk
- Rollback risk
- Disposal risk
- Required human decisions
- Required artifact updates
- Failure Mode / Knowledge / Metrics candidates
- Final completion gate checklist
- Next action
```

---

## A-10. Prompt trả lại để sửa dùng để copy-paste

```text
Hãy sửa artifact Parallel Worktree / Large Refactoring dựa trên các chỉ điểm review 48 dưới đây.

【Quy tắc sửa】
- Trước khi bắt tay, hãy diễn giải ý định của chỉ điểm bằng 1 dòng.
- Trước tiên liệt kê các artifact bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Ưu tiên sửa thiếu sót liên quan đến base commit, baseline test, integration, rollback, disposal.
- Ghi lại lý do adopt / không adopt ở dạng có thể giải thích về sau.
- Thao tác git thực tế, merge, delete, deploy, DB migration phải tách ra chờ human approval.
- Sau khi sửa, ghi kết quảxử lý vào review.md.

【Chỉ điểm review】
Dán chỉ điểm vào đây
```

---

## A-11. Điều kiện Stop/Ask

```text
- base branch / base commit chưa xác định
- git status dirty và trạng thái trước khi làm việc không rõ
- baseline test không chạy được, hoặc lý do fail chưa được ghi lại
- known failures chưa được ghi lại
- worktree owner, integration owner, rollback owner không rõ
- allowed paths / forbidden paths chưa xác định
- Có liên quan DB migration, contract breaking change, feature flag, deploy nhưng approver không rõ
- AI định thực hiện merge, force push, branch delete, worktree delete, deploy, DB migration
- Cần copy secret, .env, credential vào worktree
- So sánh option không có Tool evidence và định adopt chỉ bằng ấn tượng của AI
- required tests sau conflict resolution chưa được chạy
```

---

## A-12. Cổng hoàn tất

```text
- [ ] Lý do áp dụng 48 hoặc lý do lightweight đã được ghi lại
- [ ] base branch / base commit đã được ghi lại
- [ ] Có baseline test record và known failures
- [ ] Có worktree inventory
- [ ] Có owner, mục đích, allowed/forbidden paths theo từng worktree
- [ ] Có characterization test hoặc phương châm behavior preservation
- [ ] Có option records hoặc slice records
- [ ] Có diff comparison record
- [ ] Lý do adopt / không adopt / bảo lưu đã được ghi lại
- [ ] Có merge integration record
- [ ] Có phương châm hoặc kết quả re-run required tools sau tích hợp
- [ ] Có rollout / rollback plan
- [ ] Có disposal record
- [ ] Bài học/metrics cần phản ánh vào 29/34/49 đã được tách riêng
- [ ] Không còn Blocker
```

---

## A-13. Điểm đi tiếp theo

```text
- Muốn phân công chính thức cho Parallel Agent → 42 Multi-Agent Orchestrator
- Muốn dùng option comparison hoặc Tool evidence sau tích hợp để phán định Gate → 43 Tool-Grounded Verification
- Token/Cost tăng quá nhiều → 44 Token Optimization
- Xác nhận security boundary của MCP/tool/worktree/CI → 45 Security Governance
- Chuẩn bị Context Pack theo từng worktree → 46 RAG / CodeMap / Context Compression
- Vận hành AI Gate cho PR cuối cùng → 47 Automated PR Review / AI QA Gate
- Đo hiệu quả, review time, rollback, defect escape → 49 Evaluation / Observability
- Biến thất bại hoặc near miss của refactor thành phòng ngừa tái diễn → 29 Failure Mode
- Knowledge hóa seam, slice, migration pattern tốt → 34 Project Knowledge
```
