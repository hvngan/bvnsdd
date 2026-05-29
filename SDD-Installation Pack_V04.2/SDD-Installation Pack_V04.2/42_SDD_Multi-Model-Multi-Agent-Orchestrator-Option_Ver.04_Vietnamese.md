# 42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Vietnamese

> Loại: SDD Ver.04 Advanced Option  
> Tiền đề: Đã áp dụng Core / Extension / Operations Pack của 11 và 21〜29・31〜34, hoặc có cơ chế quản lý artifact, quản lý context và Security Gate tương đương  
> Nguyên tắc: Không làm Core trở nên nặng nề. Advanced Option chỉ được áp dụng có chọn lọc cho các案件 phức tạp, rủi ro cao, yêu cầu độ chính xác cao hoặc yêu cầu tối ưu chi phí.  
> Lưu ý: Tài liệu này không khuyến nghị AI tự trị thực thi. Các quyết định rủi ro cao, thao tác ghi, merge, release, deploy bắt buộc phải có phê duyệt của con người.

---

## Mục lục
- [42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Vietnamese](#42_sdd_multi-model-multi-agent-orchestrator-option_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Mục đích sử dụng 42](#1-mục-đích-sử-dụng-42)
  - [2. Điều kiện nên dùng / không nên dùng](#2-điều-kiện-nên-dùng--không-nên-dùng)
  - [3. Kết nối với 21〜44](#3-kết-nối-với-2144)
  - [4. Kiến trúc khuyến nghị](#4-kiến-trúc-khuyến-nghị)
  - [5. Trách nhiệm của Orchestrator](#5-trách-nhiệm-của-orchestrator)
  - [6. Agent Role Catalog](#6-agent-role-catalog)
  - [7. Model Router](#7-model-router)
  - [8. Agent Context Partitioning](#8-agent-context-partitioning)
  - [9. Blackboard Architecture](#9-blackboard-architecture)
  - [10. Recursive Review Loop](#10-recursive-review-loop)
  - [11. Agent Output Schema](#11-agent-output-schema)
  - [12. Orchestrator Plan](#12-orchestrator-plan)
  - [13. Prompt Multi-Agent Review](#13-prompt-multi-agent-review)
  - [14. Prompt Arbiter](#14-prompt-arbiter)
  - [15. Mô hình quyền của Agent](#15-mô-hình-quyền-của-agent)
  - [16. Failure Mode](#16-failure-mode)
  - [17. Metrics](#17-metrics)
  - [18. Definition of Ready](#18-definition-of-ready)
  - [19. Definition of Done](#19-definition-of-done)
  - [20. Độ chi tiết trong thiết kế Agent](#20-độ-chi-tiết-trong-thiết-kế-agent)
  - [21. Agent Trigger Matrix](#21-agent-trigger-matrix)
  - [22. Do / Do Not theo từng Agent](#22-do--do-not-theo-từng-agent)
  - [23. Siết chặt Structured Output](#23-siết-chặt-structured-output)
  - [24. Agent Evaluation Dataset](#24-agent-evaluation-dataset)
  - [25. Lộ trình đưa Multi-Agent vào vận hành](#25-lộ-trình-đưa-multi-agent-vào-vận-hành)
  - [26. Prefix chung cho Agent Prompt](#26-prefix-chung-cho-agent-prompt)
  - [27. Thiết kế Human-in-the-loop](#27-thiết-kế-human-in-the-loop)
  - [28. Handoff từ 42 sang 43](#28-handoff-từ-42-sang-43)
  - [Tài liệu tham khảo / tiêu chuẩn công khai đã tham chiếu](#tài-liệu-tham-khảo--tiêu-chuẩn-công-khai-đã-tham-chiếu)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy/paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-copypaste)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy/paste](#a-2-biến-cần-điền-trước-khi-copypaste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Artifact cần tạo / cập nhật](#a-4-artifact-cần-tạo--cập-nhật)
  - [A-5. Quy trình thực thi](#a-5-quy-trình-thực-thi)
  - [A-6. Prompt copy/paste: Prompt bắt đầu](#a-6-prompt-copypaste-prompt-bắt-đầu)
  - [A-7. Prompt copy/paste: Prompt phê duyệt Plan](#a-7-prompt-copypaste-prompt-phê-duyệt-plan)
  - [A-8. Prompt copy/paste: Prompt chung cho Agent](#a-8-prompt-copypaste-prompt-chung-cho-agent)
  - [A-9. Prompt copy/paste: Prompt review artifact và phán định hoàn tất](#a-9-prompt-copypaste-prompt-review-artifact-và-phán-định-hoàn-tất)
  - [A-10. Prompt copy/paste: Prompt trả lại để sửa](#a-10-prompt-copypaste-prompt-trả-lại-để-sửa)
  - [A-11. Điều kiện Stop/Ask cho người mới](#a-11-điều-kiện-stopask-cho-người-mới)
  - [A-12. Cổng hoàn tất](#a-12-cổng-hoàn-tất)
  - [A-13. Điểm đến tiếp theo](#a-13-điểm-đến-tiếp-theo)

---

## 0. Vai trò của tài liệu này

Tài liệu này là Advanced Option về Multi-Model / Multi-Agent / Orchestrator trong SDD Ver.04. Nó đưa các thành phần cốt lõi trong tài liệu đính kèm “Chiến lược bổ sung để nâng cao độ chính xác AI” — gồm Orchestrator, Context Builder, Multi-Model Router, Multi-Agent System, Recursive Review Loop, Consensus, Policy và Human Governance — vào quy trình thực tế của SDD một cách an toàn.

Tiền đề quan trọng như sau.

```text
Không phải cứ tăng số lượng AI là độ chính xác tự động tăng.
Càng tăng số lượng Agent, context management, token cost, xung đột ý kiến, ranh giới trách nhiệm và security risk cũng tăng theo.
Vì vậy, Multi-Agent chỉ mạnh khi được thiết kế đúng.
```

## 1. Mục đích sử dụng 42

```text
- Tách các góc nhìn mà một AI đơn lẻ dễ bỏ sót thành các Agent chuyên trách
- Đánh giá độc lập các góc nhìn như Bug / Security / Test / Performance / Maintainability / Ops
- Dùng Model Router để chuyển việc nhẹ cho model rẻ/nhanh, và việc rủi ro cao cho model mạnh hơn
- Cải thiện độ thô của review lần đầu bằng Recursive Review Loop
- Tích hợp và kiểm soát ý kiến AI bằng Arbiter / Judge / Policy Engine
- Cấu trúc hóa vật liệu phán đoán để chuyển cho Human Review
```

## 2. Điều kiện nên dùng / không nên dùng

### 2.1 Điều kiện nên dùng

```text
- PR có rủi ro cao trên nhiều góc nhìn
- Muốn tách Bug review và Security review
- Có nhiều góc nhìn như FE/BE/DB/API/Batch/Event
- Có nhiều Tech Stack khiến chuyên môn của một AI đơn lẻ không đủ
- Muốn đưa AI review tiến gần hơn tới PR Gate
- Muốn sắp xếp findings trước khi con người review
- Cần Veto hoặc Human Escalation cho finding rủi ro cao
```

### 2.2 Điều kiện không nên dùng

```text
- Thay đổi nhẹ
- Review đơn giản, 1 Agent là đủ
- Có thể phán đoán chỉ bằng Tool result
- Không kiểm soát được context hoặc token
- Con người không có khả năng review output của Agent
- Buộc phải cấp quyền nguy hiểm cho Agent
```

## 3. Kết nối với 21〜44

| Kết nối | Vai trò |
|---|---|
| 40 | Chọn có áp dụng 42 hay không |
| 41 | Tạo Impact Slice để chuyển cho Agent |
| 43 | Phán đoán Agent output bằng Tool evidence và Consensus |
| 44 | Kiểm soát context theo Agent, token budget và nén output |
| 31 | Kiểm soát include/exclude context cho Agent đọc |
| 32 | Quản lý handoff và compact cho tác vụ dài / nhiều AI |
| 33 | Artifact hóa Agent output, quyết định và evidence |
| 34 | Cung cấp tri thức đặc thù project cho Agent |

## 4. Kiến trúc khuyến nghị

```text
Input: Issue / PR / Requirement / Diff
  ↓
Orchestrator
  ↓
Risk Classifier
  ↓
Context Builder
  ↓
Token Budget Controller
  ↓
Model Router
  ↓
Agent Selector
  ↓
Specialist Agents
  ├─ Requirement Clarifier
  ├─ Architect Agent
  ├─ Bug Reviewer
  ├─ Security Reviewer
  ├─ Test Reviewer
  ├─ Performance Reviewer
  ├─ Maintainability Reviewer
  ├─ SRE/Ops Reviewer
  └─ Documentation Reviewer
  ↓
Agent Output Normalizer
  ↓
Arbiter / Judge
  ↓
43 Tool-Grounded Verification / Consensus
  ↓
Policy Engine
  ↓
Human Governance
  ↓
33 Artifact / PR Comment / Review Decision
```

## 5. Trách nhiệm của Orchestrator

Orchestrator không phải là “Agent thông minh nhất”, mà là **người điều phối giao thông có tính quyết định luận**.

```text
- Phân loại input
- Quyết định risk level
- Quyết định gọi Agent nào
- Quyết định context nào sẽ được chuyển cho Agent nào
- Tuân thủ token budget
- Quyết định có cần tool execution hay không
- Ép buộc output schema
- Kiểm soát số round của recursive loop
- Phán định điều kiện Stop/Human Review
- Chuyển Agent output sang Arbiter/43
```

Những việc Orchestrator không được làm.

```text
- Chuyển toàn bộ context cho toàn bộ Agent
- Đẩy nguyên câu trả lời tự do dài dòng của Agent đi tiếp
- Giao phó toàn bộ quyền cho Agent
- Bỏ qua tool failure
- Dập tắt security veto bằng đa số phiếu
- Chạy recursive loop vô hạn
```

## 6. Agent Role Catalog

### 6.1 Requirement Clarifier

| Mục | Nội dung |
|---|---|
| Mục đích | Sắp xếp specification, AC, phạm vi không làm, điểm chưa xác định |
| Đọc | issue, spec-pack, tài liệu nghiệp vụ, AC |
| Không đọc | Toàn văn source dung lượng lớn |
| Output | open questions, assumptions, AC gap |
| Human Escalation | Specification không rõ, AC mâu thuẫn |

### 6.2 Architect Agent

| Mục | Nội dung |
|---|---|
| Mục đích | Kiểm tra tính nhất quán thiết kế, layer, phân tách trách nhiệm, khả năng mở rộng |
| Đọc | architecture map, source map, impl-plan |
| Output | architecture risk, alternative, boundary issue |
| Human Escalation | Phá vỡ layer, thiết kế không thể đảo ngược, ảnh hưởng bảo trì dài hạn |

### 6.3 Bug Reviewer

| Mục | Nội dung |
|---|---|
| Mục đích | Phát hiện bug triển khai, giá trị biên, null, state transition, xử lý exception |
| Đọc | diff, source liên quan, test, AC |
| Output | concrete bug finding, điều kiện tái hiện, đề xuất sửa |
| Human Escalation | Khả năng gây sự cố nghiêm trọng hoặc phá hủy dữ liệu |

### 6.4 Security Reviewer

| Mục | Nội dung |
|---|---|
| Mục đích | Kiểm tra authentication, authorization, input validation, secret, audit, AI permission risk |
| Đọc | diff, auth/permission map, threat model, security rules |
| Output | security finding, severity, evidence, điều kiện block |
| Human Escalation | Bắt buộc nếu Critical/High |

### 6.5 Test Reviewer

| Mục | Nội dung |
|---|---|
| Mục đích | Kiểm tra mapping giữa AC và test, giá trị biên, contract, regression |
| Đọc | test plan, test diff, tool results, AC |
| Output | missing tests, weak tests, test command |
| Human Escalation | Không thể test dù rủi ro cao |

### 6.6 Performance Reviewer

```text
- N+1
- large query
- full scan
- cache invalidation
- algorithmic complexity
- log explosion
- payload size
- batch execution time
- external API latency
```

### 6.7 Maintainability Reviewer

```text
- Magic Number / Literal
- Logic trùng lặp
- Khả năng đọc hiểu
- Phân tách trách nhiệm
- Lệch khỏi project pattern
- Comment và implementation không khớp
- Có bị hỏng khi thêm master trong tương lai không
```

### 6.8 SRE / Ops Reviewer

```text
- log / metric / trace
- alert
- retry / idempotency
- rollback
- feature flag
- operational runbook
- failure behavior
- manual recovery
```

### 6.9 Arbiter / Judge

Arbiter không phải là người đếm phiếu đa số. Vai trò của Arbiter là tích hợp Agent output đã được cấu trúc hóa và chuyển sang 43.

```text
- Hợp nhất duplicate finding
- Chuẩn hóa severity
- Phát hiện thiếu evidence
- Làm rõ disagreement
- Tách riêng đối tượng veto
- Sắp xếp luận điểm cần human review
```

## 7. Model Router

### 7.1 Chính sách cơ bản

```text
- Không dùng high-performance model thường trực
- Rủi ro thấp thì xử lý bằng lightweight model, rules, tool
- Chỉ nâng lên high-performance model cho phần rủi ro cao
- Cascade khi uncertainty cao
- Tận dụng khác biệt giữa model, nhưng phán đoán cuối cùng phải chuyển sang 43
```

### 7.2 Ví dụ Router

| Input | Phán đoán của Router |
|---|---|
| README only | L0 summary model hoặc không dùng AI |
| Phân loại test failure | lightweight model + tool parser |
| Review bug thông thường | standard reviewer model |
| Authorization / payment | high-reasoning model + Security Reviewer + Human |
| Architecture phức tạp | high-reasoning model + Architect + Arbiter |
| Phân loại log dung lượng lớn | tool compression + lightweight model |

### 7.3 Model Cascade

```text
Step 1: cheap/tool/rule judgement
Step 2: review bằng standard model
Step 3: chỉ chuyển high-risk findings lên high-performance model
Step 4: chỉ disagreement sang Arbiter
Step 5: unresolved chuyển cho Human
```

## 8. Agent Context Partitioning

Không chuyển cùng một context cho toàn bộ Agent. Hãy tách common context và individual context.

```md
# Agent Context Partition Plan

## Common Context
- Ticket summary:
- AC summary:
- Diff summary:
- Risk hotspots:
- Source confidence:

## Agent-specific Context
| Agent | Must read | May read | Must not read | Budget |
|---|---|---|---|---|
| Bug Reviewer | diff, impacted functions, tests | callers/callees | unrelated docs | |
| Security Reviewer | auth map, permission diff, input handling | threat model | toàn văn build logs | |
| Test Reviewer | AC, test plan, test diff, failures | related source | unrelated architecture docs | |
| Performance Reviewer | query, loops, payload, benchmark | db map | UI docs | |
| Arbiter | agent summaries, evidence IDs | selected snippets | raw full logs | |
```

## 9. Blackboard Architecture

Nếu chuyển toàn bộ lịch sử hội thoại cho mọi Agent trong Multi-Agent, token sẽ bùng nổ. Thay vào đó, dùng Blackboard.

```text
Blackboard = Trạng thái chia sẻ giữa các Agent

Những thứ lưu:
- facts
- decisions
- findings
- evidence ids
- unresolved questions
- veto flags
- required tools
- human review flags

Những thứ không lưu:
- Toàn bộ lịch sử hội thoại
- verbose reasoning
- toàn văn raw tool output
- giải thích trùng lặp
```

```md
# Multi-Agent Blackboard

## Facts
| ID | Fact | Evidence | Confidence |
|---|---|---|---|

## Findings
| ID | Agent | Severity | Summary | Evidence | Status |
|---|---|---|---|---|---|

## Disagreements
| ID | Agents | Topic | Conflict | Required resolution |
|---|---|---|---|---|

## Veto Flags
| ID | Category | Raised by | Reason | Required action |
|---|---|---|---|---|

## Human Review Required
| ID | Reason | Owner | Deadline |
|---|---|---|---|
```

## 10. Recursive Review Loop

Recursive Review Loop dùng để cải thiện review lần đầu. Tuy nhiên, cấm chạy không giới hạn.

### 10.1 Round tiêu chuẩn

```text
Round 0: Context Builder
Round 1: Specialist Agents review độc lập
Round 2: Agents xem finding có cấu trúc của Agent khác và đánh giá lại
Round 3: Arbiter tích hợp và chuyển sang 43
```

### 10.2 Điều kiện tiếp tục

```text
- Có Critical/High finding nhưng thiếu evidence
- Có disagreement nghiêm trọng giữa các Agent
- Tool result và ý kiến Agent mâu thuẫn
- Phán đoán Security/DB/Contract bị chia rẽ
```

### 10.3 Điều kiện dừng

```text
- Đạt số round tối đa
- Không tăng thêm valid finding mới
- Đạt token budget
- Đang chờ Tool evidence
- Cần Human Review
```

### 10.4 Vận hành theo hướng RecursiveMAS-inspired

Không đưa nguyên nghiên cứu RecursiveMAS vào nghiệp vụ, mà trong SDD chỉ áp dụng có giới hạn như sau.

```text
- Không chuyển latent state, mà chuyển structured summary
- Tối đa 2〜3 round
- Agent output ở dạng JSON/bảng
- Không chuyển raw conversation history
- Rủi ro nghiêm trọng phải escalate cho con người
- Quản lý token budget bằng 44
```

## 11. Agent Output Schema

```json
{
  "agent_name": "security_reviewer",
  "agent_version": "sdd-v04",
  "scope": {
    "ticket": "",
    "files_reviewed": [],
    "files_not_reviewed": [],
    "context_limitations": []
  },
  "findings": [
    {
      "id": "SEC-001",
      "severity": "critical|high|medium|low|info",
      "confidence": "high|medium|low",
      "category": "authorization|input-validation|secret|audit|other",
      "summary": "",
      "evidence": [
        {"file": "", "line": "", "detail": ""}
      ],
      "impact": "",
      "recommended_action": "",
      "requires_human_review": true,
      "requires_tool_verification": true
    }
  ],
  "no_finding_areas": [
    {
      "area": "",
      "reason": "",
      "evidence": []
    }
  ],
  "open_questions": [],
  "token_usage_estimate": {
    "input": 0,
    "output": 0
  }
}
```

## 12. Orchestrator Plan

```md
# Multi-Agent Orchestrator Plan

## 1. Objective
- What decision is needed:
- What risk must be reduced:

## 2. Agents
| Agent | Apply | Reason | Model tier | Context | Budget |
|---|---|---|---|---|---|

## 3. Tools Required
| Tool | Required before agent? | Required after agent? | Owner |
|---|---|---|---|

## 4. Rounds
- Max rounds:
- Continue condition:
- Stop condition:

## 5. Policy
- Veto conditions:
- Human review conditions:
- Merge block conditions:

## 6. Output
- Blackboard location:
- Consensus record location:
- PR comment location:
```

## 13. Prompt Multi-Agent Review

```md
Bạn là Orchestrator của SDD Ver.04.
Hãy lập kế hoạch review PR/thay đổi dưới đây bằng cấu hình Agent tối thiểu cần thiết.

# Input
- Ticket / PR:
- Change summary:
- Risk classification:
- Impact Slice:
- Tool results:
- Token budget:
- Human review constraints:

# Rule
- Không chuyển toàn bộ context cho toàn bộ Agent
- Chia context cần thiết theo từng Agent
- Chỉ chuyển phần rủi ro cao cho high-performance model
- Chỉ định output schema
- recursive loop tối đa 3 round
- critical security/data findings được xử lý như veto
- Nêu rõ phán đoán nào cần tool evidence

# Output
1. Agent composition
2. Model Router judgement
3. Context theo từng Agent
4. Token budget
5. Tool bắt buộc
6. Consensus method
7. Human Review conditions
8. Stop conditions
```

## 14. Prompt Arbiter

```md
Bạn là Arbiter của SDD Ver.04.
Hãy tích hợp kết quả review có cấu trúc của nhiều Agent và tạo Consensus Record để chuyển sang 43 Tool-Grounded Verification.

# Input
- Agent outputs:
- Tool results:
- Risk policy:
- Human review rules:

# Rule
- Không phán đoán chỉ bằng đa số phiếu
- Security/data issue Critical/High phải là veto candidate
- Finding không có evidence phải được ghi rõ như vậy
- Finding trùng lặp phải được hợp nhất
- Mâu thuẫn không được che giấu, phải đưa ra dưới dạng Disagreement
- Liệt kê các điểm có thể xác minh bằng Tool

# Output
1. Consolidated findings
2. Veto candidates
3. Disagreements
4. Tool verification required
5. Human review required
6. Suggested PR decision
7. Confidence and limitations
```

## 15. Mô hình quyền của Agent

| Agent | Read | Write patch | Run tool | Network | Human approval |
|---|---|---|---|---|---|
| Requirement Clarifier | Yes | No | No | No | N/A |
| Architect | Yes | Proposal only | No | No | For major design |
| Coder | Yes | Proposal only | Limited sandbox | No | Required before apply |
| Bug Reviewer | Yes | No | Test read | No | For high severity |
| Security Reviewer | Yes | No | SAST read | No | Critical/High |
| Test Reviewer | Yes | Proposal only | Test sandbox | No | For missing high-risk tests |
| Arbiter | Summaries only | No | No | No | For final decision |

Không cấp cho AI quyền push, merge, deploy, production access.

## 16. Failure Mode

| ID | Failure Mode | Mitigation |
|---|---|---|
| MAG-001 | Nghĩ rằng chỉ cần tăng số Agent là độ chính xác tăng | Thiết kế Agent Role / Context / Schema |
| MAG-002 | Chuyển toàn bộ context cho toàn bộ Agent | Context Partitioning + 44 |
| MAG-003 | Dập tắt finding nghiêm trọng bằng majority vote | Veto Rule |
| MAG-004 | Agent output dài dòng, không thể tích hợp | Structured Output |
| MAG-005 | Recursive loop không dừng | Max round / Stop condition |
| MAG-006 | Ranh giới trách nhiệm giữa Agent mơ hồ | Role Catalog |
| MAG-007 | Consensus mà không xem Tool result | Bắt buộc kết nối 43 |
| MAG-008 | Cấp quyền nguy hiểm cho Agent | Permission Matrix |
| MAG-009 | Chuyển quá nhiều thông tin cho Human Review | Arbiter summary |
| MAG-010 | Dùng high-performance model thường trực, làm chi phí bùng nổ | Model Router + 44 |

## 17. Metrics

```text
- valid finding rate by agent
- false positive rate by agent
- missed bug rate
- disagreement rate
- human override rate
- token per agent
- cost per valid finding
- average review latency
- recursive round count
- tool verification pass/fail rate
```

Các metric này được quan sát dài hạn trong 49.

## 18. Definition of Ready

```text
- 42 đã được chọn áp dụng trong 40
- Có Impact Slice từ 41 hoặc 23
- Có điều kiện loại trừ context theo từng Agent trong 31
- Có token budget trong 44
- Có phương châm verification trong 43
- Human Review conditions rõ ràng
- Quyền Agent được kiểm soát chủ yếu ở read-only/proposal-only
```

## 19. Definition of Done

```text
- Orchestrator Plan đã được tạo
- Có Agent Context Partition Plan
- Agent output tuân theo schema
- Blackboard đã được tạo
- Arbiter đã tạo Consensus Record
- Tool verification được kết nối sang 43
- Human Review conditions đã được thỏa mãn
- Thực tế token/cost được ghi vào 44
- Failure Mode candidate được gửi sang 29
```

---

## 20. Độ chi tiết trong thiết kế Agent

Agent quá thô hay quá vụn đều thất bại.

```text
Agent quá thô:
  Vì nhìn mọi thứ nên góc nhìn bị nông.

Agent quá vụn:
  coordination cost, token cost, xung đột ý kiến tăng.
```

Khuyến nghị là bắt đầu với 3〜5 Agent.

```text
Tối thiểu:
- Bug Reviewer
- Test Reviewer
- Security Reviewer only if risk exists
- Arbiter

Tiêu chuẩn:
- Requirement Clarifier
- Architect
- Bug Reviewer
- Security Reviewer
- Test Reviewer
- Arbiter

Đầy đủ:
- Các Agent trên + Performance + Maintainability + SRE/Ops + Documentation + Domain Specialist
```

## 21. Agent Trigger Matrix

| Trigger | Agent |
|---|---|
| AC không rõ | Requirement Clarifier |
| Thay đổi layer/trách nhiệm | Architect |
| Thay đổi production code | Bug Reviewer |
| auth/permission/PII | Security Reviewer |
| Test thay đổi/thiếu | Test Reviewer |
| query/loop/payload | Performance Reviewer |
| refactor/duplication | Maintainability Reviewer |
| batch/retry/monitoring | SRE/Ops Reviewer |
| tài liệu hướng user | Documentation Reviewer |
| Xung đột ý kiến | Arbiter |

## 22. Do / Do Not theo từng Agent

| Agent | Do | Do Not |
|---|---|---|
| Requirement | Nêu AC gap | Tự ý chốt specification |
| Architect | Nêu design risk | Tự ý thay đổi implementation |
| Coder | Tạo patch proposal | Apply/commit khi chưa có human approval |
| Bug Reviewer | Chỉ ra finding kèm điều kiện tái hiện | Chỉ góp ý style theo sở thích |
| Security | Nêu rõ severity/evidence | Rút lại critical chỉ vì majority vote |
| Test | Nêu AC-test gap | Chỉ phán đoán bằng coverage number |
| Arbiter | Tích hợp và sắp xếp mâu thuẫn | Tự ý xóa finding nghiêm trọng theo độc đoán |

## 23. Siết chặt Structured Output

Agent output không được chỉ là văn tự nhiên. Tối thiểu phải bắt buộc các trường sau.

```text
- finding id
- severity
- confidence
- category
- evidence
- affected file/line
- impact
- recommended action
- requires tool verification
- requires human review
```

Structured output giúp 43 chuẩn hóa, 33 lưu evidence và 49 đánh giá.

## 24. Agent Evaluation Dataset

Để cải thiện liên tục 42, cần tạo evaluation dataset theo từng Agent.

```md
# Agent Evaluation Dataset Entry

## Case
- PR / Ticket:
- Domain:
- Risk:

## Ground Truth
- Valid findings:
- False positives:
- Missed bugs:
- Human decision:

## Agent Outputs
| Agent | Findings | Valid | False Positive | Missed |
|---|---:|---:|---:|---:|

## Lessons
- Prompt update:
- Context update:
- Tool update:
- Rule update:
```

## 25. Lộ trình đưa Multi-Agent vào vận hành

```text
Stage 1: Single Reviewer + structured output
Stage 2: Bug/Test/Security 3Agent
Stage 3: Đưa Arbiter vào
Stage 4: Kết nối Tool-Grounded Verification
Stage 5: Đưa Model Router vào
Stage 6: Recursive Review Loop 2 round
Stage 7: Agent evaluation dataset
Stage 8: Kết nối giới hạn vào PR Gate / QA Gate
```

## 26. Prefix chung cho Agent Prompt

```md
Bạn là Agent chuyên trách của SDD Ver.04.
Output của bạn không phải là phán đoán cuối cùng.
Vai trò của bạn là trích xuất rủi ro thuộc góc nhìn phụ trách kèm evidence, rồi chuyển cho 43 Tool-Grounded Verification và Human Review.

# Quy tắc chung
- Không viết suy đoán như sự thật
- Không nêu finding nghiêm trọng nếu không có evidence
- Nếu thiếu evidence, hãy ghi là thiếu evidence
- Nội dung ngoài chuyên môn của mình phải đưa vào open question
- Không xâm lấn vai trò của Agent khác
- Tuân thủ output schema
- Tuân thủ token budget
```

## 27. Thiết kế Human-in-the-loop

Multi-Agent không thay thế human review. Nó xử lý trước để human review thông minh hơn.

```text
AI làm:
- Thu thập finding theo từng góc nhìn
- Chỉ ra evidence candidate
- Đưa ra tool verification candidate
- Hiển thị disagreement

Con người làm:
- Phán đoán đúng/sai về nghiệp vụ
- risk acceptance
- Phán đoán security high/critical
- Phê duyệt merge/release/deploy
- Cấp phép exception
```

## 28. Handoff từ 42 sang 43

```md
# 42 to 43 Handoff

## Agent Plan Ref

## Agent Outputs
| Agent | Output file | Scope | Limitations |
|---|---|---|---|

## Blackboard Ref

## Findings Requiring Tool Verification
| Finding | Required tool | Reason |
|---|---|---|

## Veto Candidates

## Disagreements

## Human Review Candidates

## Token / Cost Summary
```

## Tài liệu tham khảo / tiêu chuẩn công khai đã tham chiếu

Advanced Options này lấy các SDD nội bộ, các artifact V04 của 11 và 21〜29・31〜34, cùng các tài liệu đính kèm “AI精度向上のための追加戦略_20260516.md” và “AIトークン削減のための追加戦略_20260516.md” làm input chính, sau đó đưa tư tưởng của các tài liệu/tiêu chuẩn công khai sau vào ngữ cảnh SDD.

- OpenAI Agents SDK: các yếu tố thiết kế Agent như handoffs, guardrails, function tools, MCP server tool calling, sandbox agents.
- OpenAI Prompt Caching / Cost Optimization / Batch API / Flex Processing: exact prefix caching, thiết kế static prefix, xử lý bất đồng bộ / chi phí thấp.
- OpenAI Structured Outputs: cải thiện khả năng xử lý máy và khả năng tái hiện bằng output có cấu trúc theo JSON Schema.
- Model Context Protocol Security Best Practices: vector tấn công, quyền và rủi ro tool execution đặc thù MCP.
- NIST SSDF SP 800-218: secure development practices có thể tích hợp vào Secure SDLC.
- OWASP ASVS / OWASP LLM Top 10 / OWASP GenAI Security: bảo mật Web/API và rủi ro đặc thù LLM/Agent.
- SLSA / OpenSSF Scorecard: software supply chain, dependency, build evidence, đánh giá mức độ lành mạnh OSS.
- OpenTelemetry GenAI semantic conventions: thiết kế quan sát cho AI/Agent call, tool call, latency, token, error.
- Recursive Multi-Agent Systems: nghiên cứu coi Multi-Agent collaboration là recursive computation. Trong thực tế áp dụng dưới dạng RecursiveMAS-inspired có giới hạn.
- LongLLMLingua / Prompt Compression: mật độ thông tin quan trọng trong context dài, position bias và tư tưởng nén.
- RTK / Rust Token Killer: tư tưởng thực hành nén CLI output trước khi chuyển vào LLM context.
- SWE-bench / SWE-bench Verified: tham khảo thiết kế dataset đánh giá coding Agent và regression evaluation.
- everything-claude-code: tư tưởng vận hành skills, rules, hooks, MCP, security scanning, continuous learning, cross-harness. Tuy nhiên trong SDD chỉ lựa chọn áp dụng theo hướng an toàn.

---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy/paste

> Appendix này là “execution wrapper” để người mới cũng có thể vận hành an toàn Multi-Model / Multi-Agent Orchestrator được định nghĩa trong phần thân tài liệu.  
> Không thay đổi nội dung phần thân. Hãy dùng phần thân như “spec của thiết kế Agent / Orchestrator / Arbiter / Blackboard”, và dùng Appendix này như quy trình “khi nào, dùng bao nhiêu Agent, theo thứ tự nào, dừng ở đâu”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

42 là Option dùng nhiều AI/Agent/Model để nâng cao độ chính xác phân tích và review.  
Người mới không được coi 42 là “cơ chế tăng AI lên để bỏ phiếu đa số”, mà phải coi đây là **cơ chế thu thập nhiều góc nhìn có vai trò giới hạn, sắp xếp bằng Arbiter, rồi chuyển cho Tool và con người phán đoán**.

```text
1. Không chạy nhiều Agent ngay lập tức.
2. Trước tiên chỉ yêu cầu Orchestrator Plan.
3. Cho đến khi con người phê duyệt Plan, không chạy Agent, không tạo file, không thay đổi CI.
4. Số lượng Agent phải là tối thiểu cần thiết.
5. Không chuyển toàn bộ Context cho mọi Agent.
6. Output của Agent là “ý kiến”, không phải quyết định cuối cùng.
7. Security, Tool failure, Test failure, Policy violation không được bị dập tắt bằng đa số phiếu.
8. Trong Blackboard, phải tách Facts, Findings, Disagreements, Veto, Human Review Required.
9. Arbiter thực hiện tích hợp và sắp xếp luận điểm, nhưng không tự ý chốt phán đoán cần human approval.
10. Sau 42, tùy nhu cầu, chuyển sang 43 Tool-Grounded Verification.
```

Nơi lưu cơ bản dùng trong Appendix này như sau.

```text
Artifact riêng của pack:
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/

Handoff sang Option sau:
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/43-handoff.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/44-cost-summary.md

Nơi tạm đặt candidate thường trực hóa:
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/promotion-candidates.md
```

Tư tưởng quan trọng.

```text
Mục tiêu của 42 không phải là “tăng số AI”,
mà là tách các góc nhìn chuyên môn cần thiết, hiển thị mâu thuẫn và Veto, rồi chuẩn bị vật liệu để con người và Tool có thể phán đoán.
```

---

## A-1. Khi nào dùng pack này

### Trường hợp nên dùng

```text
- Cần nhiều góc nhìn chuyên môn như Security, performance, design, test, operation
- Chỉ review bằng một AI thì sợ bỏ sót
- Thay đổi lớn hoặc rủi ro cao, cần review độc lập theo từng góc nhìn
- Muốn chia Impact Slice của 41 cho từng Agent review
- Muốn sắp xếp Findings cần verification trước khi sang 43
- Cần góc nhìn có quyền Veto như Security Reviewer hoặc Test Reviewer
- 42 đã được chọn áp dụng trong 40, và có thể đặt Token/Cost budget trong 44
```

### Trường hợp có thể lightweight

```text
- Thay đổi nhỏ, góc nhìn review đơn giản
- Independent review của 24 là đủ
- Có thể phán đoán chỉ bằng Tool result của 43
- Không có nguồn lực con người để tích hợp / verify Agent output
- Token/Cost/Latency không tương xứng
```

Kể cả khi lightweight, tối thiểu vẫn ghi lại các điểm sau.

```text
- Lý do không dùng 42
- Phương pháp review thay thế
- Rủi ro bỏ sót
- Trigger nên chạy lại 42 sau này
```

### Trường hợp không dùng, hoặc phải quay lại pack khác trước

```text
- 42 chưa được phê duyệt áp dụng trong 40
- Context Partition của 31 chưa được sắp xếp
- Không có Impact Slice của 41, nên không biết chuyển gì cho Agent
- Không có Token/Cost budget của 44, nên không kiểm soát được số Agent hoặc số Round
- Định xử lý Security/Tool/CI result bằng đa số phiếu AI
- Chưa xác định vai trò Arbiter và điểm cần human approval
```

---

## A-2. Biến cần điền trước khi copy/paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 42
{{PACK_NAME}}: Multi-Model Multi-Agent Orchestrator Option
{{PACK_SLUG}}: multi-agent-orchestrator
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{ORCHESTRATION_OBJECTIVE}}:
{{AGENT_CANDIDATES}}:
{{MAX_AGENTS}}:
{{MAX_ROUNDS}}:
{{TOKEN_COST_LIMIT}}:
{{VETO_POLICIES}}:
{{ARBITER_POLICY}}:
```

Ví dụ điền.

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{SCOPE_NOTE}}: Bao gồm API, permission, gửi email, E2E
{{RISK_LEVEL}}: High
{{SDD_MODE}}: M3
{{TIMEBOX}}: Đến Orchestrator Plan và Round 1 review
{{ORCHESTRATION_OBJECTIVE}}: Giảm bỏ sót bằng góc nhìn độc lập Security/Test/Architecture
{{AGENT_CANDIDATES}}: Architect, Security Reviewer, Test Reviewer, Arbiter
{{MAX_AGENTS}}: 4
{{MAX_ROUNDS}}: 2
{{TOKEN_COST_LIMIT}}: Trong ngân sách đã định nghĩa ở 44
{{VETO_POLICIES}}: Security High, test failure, policy violation không được bác bỏ bằng đa số phiếu
{{ARBITER_POLICY}}: Chỉ tích hợp và sắp xếp luận điểm. Phán đoán cuối cùng dựa vào con người hoặc Tool evidence của 43
```

---

## A-3. Input đầu tiên cần cho AI đọc

### Input chung cần đọc

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
@docs/changes/{{TICKET}}/41-heavy-source-analysis/risk-hotspot-map.md
@docs/changes/{{TICKET}}/31-context-loading/context-manifest.md
@docs/changes/{{TICKET}}/44-token-cost-control/token-budget-record.md
```

### Input cần chia trước khi chuyển cho Agent

```text
Common Context:
- Tóm tắt ticket
- AC
- scope / non-scope
- ràng buộc quan trọng
- cấm kỵ chung
- tóm tắt Impact Slice của 41

Agent-specific Context:
- Architect Agent: architecture/module/call dependency
- Security Reviewer: auth/permission/input/log/PII/security rules
- Test Reviewer: AC/test-plan/test-results/gaps
- Performance Reviewer: heavy query, N+1, latency, batch/event
- SRE/Ops Reviewer: logs, metrics, rollback, deploy, observability
- Arbiter: toàn bộ Agent output, Blackboard, Veto policy
```

---

## A-4. Artifact cần tạo / cập nhật

### Thư mục riêng của pack

```text
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/
```

### Artifact tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/orchestrator-plan.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-context-partition.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/blackboard.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-outputs.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/arbiter-consensus.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/human-review-required.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/43-handoff.md
```

### Artifact tạo khi cần

```text
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/model-router.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/round-log.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/disagreement-log.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/veto-log.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-evaluation-record.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/44-cost-summary.md
docs/changes/{{TICKET}}/42-multi-agent-orchestrator/promotion-candidates.md
```

### Nội dung có thể phản ánh vào Core artifacts

```text
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/test-plan.md
docs/changes/{{TICKET}}/impl-plan.md
docs/changes/{{TICKET}}/report.md
```

---

## A-5. Quy trình thực thi

### Step 1. Kiểm tra selection của 40 và budget của 44

Vì 42 dễ làm tăng Token/Cost, chỉ dùng khi đã được chọn trong 40 và có thể đặt budget trong 44.

```text
Những thứ cần kiểm tra:
- 40 advanced-option-selection-record.md
- 44 token-budget-record.md hoặc token-cost guardrail
- 31 context-manifest.md
- 41 impact-slice.md
```

### Step 2. Chỉ tạo Orchestrator Plan

Những điều cần quyết định đầu tiên.

```text
- Muốn phán đoán điều gì
- Agent nào cần thiết
- Agent nào không cần
- Context chuyển cho từng Agent
- Context không chuyển cho từng Agent
- Số Round
- Veto policy
- Arbiter policy
- Human Review conditions
```

### Step 3. Tạo Agent Context Partition

Không chuyển toàn bộ nội dung cho toàn bộ Agent, mà tách common context và Agent-specific context.

```text
Common Context ngắn và cố định
Agent-specific Context tối thiểu cần thiết
Không chuyển secret/PII/huge log
```

### Step 4. Thực hiện Round 1

Mỗi Agent chỉ được yêu cầu các output sau.

```text
- Facts used
- Findings
- Severity
- Evidence
- Confidence
- Tool verification needed
- Human review needed
- No final decision
```

### Step 5. Tích hợp vào Blackboard

Trong Blackboard, tách các phần sau.

```text
Facts
Findings
Disagreements
Veto Flags
Human Review Required
Tool Verification Required
```

### Step 6. Tích hợp bằng Arbiter

Arbiter thực hiện các việc sau.

```text
- Hợp nhất Findings trùng lặp
- Sắp xếp mâu thuẫn
- Giữ lại Veto candidates
- Sắp xếp Tool verification candidates để chuyển sang 43
- Tách các mục cần con người phán đoán
```

Những việc Arbiter không được làm.

```text
- Bác bỏ Security High bằng đa số phiếu
- Bỏ qua Tool failure và cho PASS
- Tự ý chốt phán đoán cần human approval
- Coi ý kiến Agent không có evidence là sự thật đã xác định
```

### Step 7. Handoff sang 43

Kết quả cuối cùng của 42 được chuẩn bị để 43 có thể verify bằng Tool-grounded.

```text
- Tool verification needed
- Veto candidates
- Disagreements
- Human review candidates
- Token / Cost summary
```

---

## A-6. Prompt copy/paste: Prompt bắt đầu

```text
Bạn là người hỗ trợ thực thi “42 Multi-Model Multi-Agent Orchestrator Option” của SDD Ver.04.
Từ giờ, hãy lập kế hoạch xem có nên dùng nhiều Agent cho {{TICKET}}（{{FEATURE_NAME}}）hay không, và nếu dùng thì thiết kế thế nào cho an toàn.

【Quy tắc quan trọng nhất】
- Không chạy nhiều Agent ngay lập tức.
- Trước tiên chỉ trình bày Orchestrator Plan.
- Cho đến khi tôi phê duyệt Plan, không chạy Agent, không tạo file, không thay đổi CI.
- Số lượng Agent phải là tối thiểu cần thiết.
- Không chuyển toàn bộ Context cho toàn bộ Agent.
- Không coi Agent output là quyết định cuối cùng.
- Security High, Tool failure, Test failure, Policy violation không được bị bác bỏ bằng đa số phiếu.
- Arbiter thực hiện tích hợp và sắp xếp luận điểm, rồi chuyển phán đoán cuối cùng cho con người hoặc Tool evidence của 43.
- Không đọc secret, PII, .env, credential, bản gốc production log.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Objective: {{ORCHESTRATION_OBJECTIVE}}
- Agent Candidates: {{AGENT_CANDIDATES}}
- Max Agents: {{MAX_AGENTS}}
- Max Rounds: {{MAX_ROUNDS}}
- Token/Cost Limit: {{TOKEN_COST_LIMIT}}
- Veto Policies: {{VETO_POLICIES}}
- Arbiter Policy: {{ARBITER_POLICY}}

【Plan phải bao gồm】
1. Có cần áp dụng 42 hay không
2. Agent được chọn và Agent không được chọn
3. Vai trò, input, output, điều cấm của từng Agent
4. Common Context và Agent-specific Context
5. Thiết kế Round và điều kiện dừng
6. Veto policy
7. Arbiter policy
8. Thiết kế Blackboard
9. Thiết kế Handoff sang 43
10. Human Review Required conditions
11. Artifact cần tạo/cập nhật và nơi lưu
12. Cổng hoàn tất

Trước tiên chỉ trình bày Plan. Chưa chạy Agent và chưa chỉnh sửa file.
```

---

## A-7. Prompt copy/paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật artifact của 42 Multi-Agent Orchestrator.

【Quy tắc thực thi】
- Trước tiên hãy tạo orchestrator-plan.md và agent-context-partition.md.
- Agent execution chỉ được giới hạn trong Agent và Round đã được phê duyệt trong Plan.
- Output của từng Agent phải được ghi vào agent-outputs.md, tách Facts / Findings / Evidence / Confidence / Tool verification needed / Human review needed.
- Trong Blackboard, hãy tách Facts, Findings, Disagreements, Veto Flags, Human Review Required.
- Arbiter chỉ thực hiện tích hợp và sắp xếp luận điểm, không tự ý chốt quyết định cuối cùng.
- Hãy tổng hợp các mục cần verification trong 43 vào 43-handoff.md.
- Thực tế hoặc quan ngại về Token/Cost phải được ghi vào 44-cost-summary.md.
- Sau khi làm xong, hãy tự phán định cổng hoàn tất.
```

---

## A-8. Prompt copy/paste: Prompt chung cho Agent

```text
Bạn là Agent chuyên trách của SDD Ver.04.
Vai trò của bạn là “{{AGENT_ROLE}}”.

【Quy tắc tuyệt đối】
- Chỉ review trong phạm vi vai trò của bạn.
- Không quyết định phán đoán cuối cùng hoặc merge khả thi hay không.
- Không viết suy đoán không có Evidence như sự thật.
- Không xem nhẹ Security High, Tool failure, Test failure, Policy violation.
- Không yêu cầu secret, PII, credential, bản gốc production log.
- Output phải tuân theo Schema được chỉ định.

【Input】
Common Context:
Dán Common Context ở đây

Agent-specific Context:
Dán Context riêng của vai trò ở đây

【Output format】
- Agent Role:
- Scope reviewed:
- Facts used:
- Findings:
  - [Severity] Title
    - Evidence:
    - Impact:
    - Recommendation:
    - Confidence:
    - Tool verification needed: Yes / No
    - Human review needed: Yes / No
- Disagreements / uncertainties:
- Veto candidates:
- What I did not review:
```

---

## A-9. Prompt copy/paste: Prompt review artifact và phán định hoàn tất

```text
Bạn là independent reviewer của SDD Ver.04.
Hãy review các artifact 42 Multi-Agent dưới đây và phán định có được chuyển sang 43 Tool-Grounded Verification hay không, hoặc phải quay lại human judgement.

【Đối tượng review】
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/orchestrator-plan.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-context-partition.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/blackboard.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-outputs.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/arbiter-consensus.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/human-review-required.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/43-handoff.md

【Góc nhìn review】
1. Số lượng Agent có quá mức không
2. Vai trò từng Agent có trùng lặp quá nhiều không
3. Agent-specific Context có được chia phù hợp không
4. Có chuyển toàn bộ Context cho toàn bộ Agent không
5. Blackboard có tách Facts/Findings/Disagreements/Veto/Human Review không
6. Arbiter có dập tắt rủi ro nghiêm trọng bằng đa số phiếu không
7. Các mục cần Tool verification trong 43 có rõ không
8. Token/Cost có được kiểm soát không
9. Human Review Required có bị che giấu không
10. Có thỏa mãn cổng hoàn tất không

【Output format】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Over-agent risks
- Context leakage risks
- Unresolved disagreements
- Veto candidates
- Required tool verification
- Required human decisions
- Required updates before 43
- Final completion gate checklist
- Next action
```

---

## A-10. Prompt copy/paste: Prompt trả lại để sửa

```text
Dựa trên các review finding dưới đây, hãy sửa artifact 42 Multi-Agent.

【Quy tắc sửa】
- Trước khi bắt tay, hãy diễn giải ý định của finding trong 1 dòng.
- Trước tiên hãy liệt kê artifact bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Nếu cần thêm/xóa/hợp nhất Agent, hãy ghi lý do vào orchestrator-plan.md.
- Nếu thay đổi context partition, hãy cập nhật agent-context-partition.md.
- Nếu thay đổi Disagreement hoặc Veto, hãy cập nhật blackboard.md và arbiter-consensus.md.
- Nếu nội dung chuyển sang 43 thay đổi, hãy cập nhật 43-handoff.md.
- Những gì cần human judgement phải được tách vào human-review-required.md.

【Review finding】
Dán finding ở đây
```

---

## A-11. Điều kiện Stop/Ask cho người mới

Nếu rơi vào một trong các điều kiện sau, hãy dừng Agent execution hoặc tích hợp và quay lại hỏi con người.

```text
- 42 chưa được phê duyệt áp dụng trong 40
- Không có Context partition của 31
- Không có Token/Cost budget của 44
- Số Agent quá nhiều, hoặc vai trò mơ hồ
- Định chuyển toàn bộ Context cho toàn bộ Agent
- Định bác bỏ Security High hoặc Tool failure bằng đa số phiếu
- Arbiter định tự ý chốt human judgement
- Agent output mâu thuẫn nhưng không để lại dưới dạng Disagreement
- Không rõ Tool verification candidate để chuyển sang 43
- Token/Cost vượt Timebox hoặc budget
```

Output format khi Stop/Ask.

```text
- Stop Reason:
- Affected agents:
- Risk:
- Required human decision:
- Minimal safe next step:
```

---

## A-12. Cổng hoàn tất

Pack này chỉ được coi là hoàn tất khi thỏa mãn toàn bộ các điều kiện sau.

```text
- [ ] Orchestrator Plan đã được phê duyệt
- [ ] Lý do chọn Agent và không chọn Agent đã được ghi lại
- [ ] Common Context và Agent-specific Context được tách riêng
- [ ] Mỗi Agent output có Evidence, Confidence, Tool verification needed
- [ ] Blackboard có Facts / Findings / Disagreements / Veto Flags / Human Review Required
- [ ] Arbiter không dập tắt rủi ro nghiêm trọng bằng đa số phiếu
- [ ] Security, Tool failure, Test failure, Policy violation được xử lý như Veto candidate
- [ ] 43-handoff.md đã được tạo
- [ ] Token/Cost summary được ghi lại
- [ ] Các mục cần human judgement được tách riêng
- [ ] Không còn Blocker sau review
- [ ] Nội dung cần phản ánh vào Core artifact đã được nêu rõ
```

---

## A-13. Điểm đến tiếp theo

```text
Cần Tool verification               → Đi sang 43
Token/Cost phình to                  → Quay lại 44
Security/Agent permission có vấn đề  → Đi sang 45
Cần chia lại Context                 → Quay lại 31
Thiếu Source evidence                → Quay lại 41
Tăng thêm review perspective         → Phản ánh vào review-checklist
Tăng thêm test perspective           → Phản ánh vào test-plan
Cần rule hóa cải tiến                → Phản ánh vào 29/34
Muốn đưa vào evaluation              → Phản ánh vào 49
```

Cuối cùng, kết quả của 42 cần được tóm tắt trong `report.md` dưới mục “Multi-Agent Review Summary”, để có thể giải thích Agent nào đã xem gì và nội dung nào đã được chuyển sang 43.
