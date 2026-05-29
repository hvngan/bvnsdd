**Mục lục**
- [43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Vietnamese](#43_sdd_tool-grounded-verification-and-consensus-option_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Tư tưởng cơ bản](#1-tư-tưởng-cơ-bản)
  - [2. Điều kiện áp dụng](#2-điều-kiện-áp-dụng)
  - [3. Verification Pipeline](#3-verification-pipeline)
  - [4. Required Tool Matrix](#4-required-tool-matrix)
  - [5. Tool Result Record](#5-tool-result-record)
  - [6. Tool Output Compression](#6-tool-output-compression)
  - [7. AI Finding Normalization](#7-ai-finding-normalization)
  - [8. Veto Rule](#8-veto-rule)
  - [9. Weighted Consensus](#9-weighted-consensus)
  - [10. Policy Engine](#10-policy-engine)
  - [11. PR Decision Schema](#11-pr-decision-schema)
  - [12. Góc nhìn kiểm tra theo từng Tool](#12-góc-nhìn-kiểm-tra-theo-từng-tool)
  - [13. Human Override](#13-human-override)
  - [14. Prompt thực thi 43](#14-prompt-thực-thi-43)
  - [15. Failure Mode](#15-failure-mode)
  - [16. Metrics](#16-metrics)
  - [17. Definition of Ready](#17-definition-of-ready)
  - [18. Definition of Done](#18-definition-of-done)
  - [19. Quy tắc Evidence Linking](#19-quy-tắc-evidence-linking)
  - [20. Finding Status Lifecycle](#20-finding-status-lifecycle)
  - [21. Xử lý False Positive](#21-xử-lý-false-positive)
  - [22. Xử lý Accepted Risk](#22-xử-lý-accepted-risk)
  - [23. Cách xử lý khi Tool Failure](#23-cách-xử-lý-khi-tool-failure)
  - [24. Phiên bản thực dụng của Consensus Algorithm](#24-phiên-bản-thực-dụng-của-consensus-algorithm)
  - [25. Quy tắc tạo Review Comment](#25-quy-tắc-tạo-review-comment)
  - [26. Những thứ lưu từ 43 sang 33](#26-những-thứ-lưu-từ-43-sang-33)
  - [27. Feedback từ 43 sang 29/49](#27-feedback-từ-43-sang-2949)
  - [28. Prompt Review Consensus](#28-prompt-review-consensus)
  - [Tài liệu/tiêu chuẩn công khai bên ngoài đã tham khảo](#tài-liệutiêu-chuẩn-công-khai-bên-ngoài-đã-tham-khảo)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-copy-paste)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Thành quả cần tạo/cập nhật](#a-4-thành-quả-cần-tạocập-nhật)
  - [A-5. Quy trình thực thi](#a-5-quy-trình-thực-thi)
  - [A-6. Dùng để copy-paste: Prompt bắt đầu](#a-6-dùng-để-copy-paste-prompt-bắt-đầu)
  - [A-7. Dùng để copy-paste: Prompt phê duyệt Plan](#a-7-dùng-để-copy-paste-prompt-phê-duyệt-plan)
  - [A-8. Dùng để copy-paste: Prompt review thành quả và phán định hoàn tất](#a-8-dùng-để-copy-paste-prompt-review-thành-quả-và-phán-định-hoàn-tất)
  - [A-9. Dùng để copy-paste: Prompt trả về sửa](#a-9-dùng-để-copy-paste-prompt-trả-về-sửa)
  - [A-10. Điều kiện Stop/Ask cho người mới](#a-10-điều-kiện-stopask-cho-người-mới)
  - [A-11. Cổng hoàn tất](#a-11-cổng-hoàn-tất)
  - [A-12. Điểm cần đi tiếp theo](#a-12-điểm-cần-đi-tiếp-theo)

# 43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Vietnamese


> Loại: SDD Ver.04 Advanced Option  
> Tiền đề: Đã áp dụng Core / Extension / Operations Pack của 11 và 21〜29・31〜34, hoặc có quản lý thành quả, quản lý Context và Security Gate tương đương  
> Nguyên tắc: Không làm Core trở nên nặng nề. Advanced Option chỉ được chọn áp dụng cho những案件 phức tạp, rủi ro cao, yêu cầu độ chính xác cao hoặc yêu cầu tối ưu chi phí.  
> Chú ý: Tài liệu này không khuyến nghị AI tự trị thực thi. Các phán đoán rủi ro cao, ghi file, merge, release, deploy bắt buộc phải có phê duyệt của con người.


## 0. Vai trò của tài liệu này

Tài liệu này là Advanced Option để kiểm chứng AI review, output Multi-Agent, đề xuất triển khai và phán đoán PR bằng Tool result, Evidence, Policy và Human Governance.

Dù AI có trở nên cao cấp đến đâu, output của AI về cơ bản vẫn là “ý kiến”. Trong SDD Ver.04, không dùng nguyên trạng ý kiến của AI làm phán đoán chất lượng. Cần xử lý theo dòng sau.

```text
AI Opinion
  ↓
Evidence Required
  ↓
Tool-Grounded Verification
  ↓
Consensus / Veto / Policy
  ↓
Human Governance
  ↓
Review Decision / PR Decision / Artifact Evidence
```

43 kết nối chặt chẽ với 24 Review/TestCode, 25 Security, 26 FE/BE Contract, 27 Microservice, 33 Artifact Governance và 42 Multi-Agent.

## 1. Tư tưởng cơ bản

### 1.1 Tách Opinion và Evidence

```text
Opinion:
  - AI nói “không có vấn đề”
  - AI nói “cách sửa này tốt”
  - Nhiều Agent đồng thuận

Evidence:
  - test pass / fail
  - typecheck pass / fail
  - build pass / fail
  - SAST phát hiện critical
  - migration dry-run thành công
  - contract test thất bại
  - benchmark bị suy giảm
  - con người phê duyệt đặc tả nghiệp vụ
```

### 1.2 Evidence hierarchy

```text
Level 0: Khẳng định của AI không có hỗ trợ
Level 1: Khẳng định của AI có source reference
Level 2: Nhiều agent đồng thuận và có source reference
Level 3: Tool result hỗ trợ/phủ định
Level 4: Human reviewer xác minh
Level 5: Production telemetry / incident evidence
```

Không thực hiện phán đoán rủi ro cao chỉ dựa trên Level 0〜2.

### 1.3 Không phải Majority Vote mà là Veto + Weighted Consensus

Biểu quyết đa số chỉ mang tính tham khảo.

```text
- Security Critical dù chỉ có 1件 cũng là ứng viên Veto
- Data loss risk dù chỉ có 1件 cũng phải Human Review
- Tool failure được ưu tiên hơn AI consensus
- Coverage gap thì tăng trọng số của Test Reviewer
- Architecture issue thì tăng trọng số của Architect/Human
```

## 2. Điều kiện áp dụng

### 2.1 Áp dụng bắt buộc

```text
- AI hỗ trợ phán đoán chất lượng PR/patch
- Sử dụng 42 Multi-Agent
- Có ảnh hưởng đến Security/DB/API/contract/operation
- Có nhiều Tool result và cần tích hợp
- Muốn kết nối AI review với PR gate hoặc QA gate
- Muốn chuyển summary có căn cứ cho human reviewer
```

### 2.2 Áp dụng nhẹ

```text
- PR nhỏ, chỉ summary hóa test/lint/build result bằng AI
- Chỉ kết nối một phần Review Checklist với Tool evidence
- Dùng tool để xác nhận AI finding nhằm giảm false positive
```

## 3. Verification Pipeline

```text
1. Input Normalization
2. Quyết định Required Tool Matrix
3. Tool Execution / Tool Result Intake
4. Tool Output Compression
5. AI Finding Intake
6. Evidence Linking
7. Finding Normalization
8. Áp dụng Veto Rule
9. Weighted Consensus
10. Phán định bằng Policy Engine
11. Human Review Escalation
12. PR Decision / Final Report
13. Ghi vào 33 Artifact Governance
14. Kết nối với 29 Failure Mode / 49 Evaluation
```

## 4. Required Tool Matrix

| Loại thay đổi | Tool bắt buộc | Tool khuyến nghị | Human Review |
|---|---|---|---|
| FE UI | unit/component test, lint, typecheck | e2e, a11y | Phán đoán UI/UX |
| BE API | unit/integration, build, typecheck | contract test, SAST | Thay đổi API contract |
| DB migration | migration dry-run | rollback test, query plan | DBA/Tech Lead |
| Auth/Permission | security tests, SAST | threat model, abuse test | Bắt buộc Security |
| Microservice | contract test, integration | trace, chaos/failure test | Service owner |
| Batch | job test, idempotency test | performance, retry test | Ops/SRE |
| Refactor | regression, coverage | mutation/benchmark | Tech Lead |

## 5. Tool Result Record

```md
# Tool Result Record

## 1. Metadata
- Tool:
- Version:
- Command:
- Date:
- Environment:
- Commit:
- Exit code:

## 2. Summary
- Pass / Fail / Warning / Not run:
- Reason:

## 3. Findings
| ID | Severity | File | Line | Message | Raw evidence ref |
|---|---|---|---|---|---|

## 4. Limitations
- Not run because:
- Partial scope:
- Flaky risk:
- Requires human interpretation:

## 5. Link to SDD Artifacts
- Spec Pack:
- Impl Plan:
- Review Checklist:
- Test Plan:
- Final Report:
```

## 6. Tool Output Compression

Không đưa toàn văn Tool result cho AI. Raw log được lưu lại, còn bản nén được đưa cho AI.

### 6.1 Thông tin cần giữ lại

```text
- command
- exit code
- failed test names
- error type
- file/line
- expected/actual
- top stack trace
- SAST rule ID / CWE / severity
- dependency name/version/CVE
- migration error
- performance regression number
```

### 6.2 Thông tin bỏ qua/tỉnh lược

```text
- toàn bộ danh sách passed test
- progress bar
- repeated stack frames
- download logs
- cache hit logs
- unrelated warnings
- ANSI escape sequences
- duplicated messages
```

### 6.3 Template nén

```md
# Compressed Tool Output

## Command
`...`

## Verdict
Pass / Fail / Warning

## Key Failures
| ID | Type | File | Line | Summary | Suggested owner |
|---|---|---|---|---|---|

## Raw Log Reference
- path:
- hash:

## What AI should analyze
- ...

## What AI should not infer
- ...
```

## 7. AI Finding Normalization

Chuyển đổi các chỉ摘 từ nhiều Agent hoặc nhiều model sang schema chung.

```json
{
  "finding_id": "F-001",
  "source": "security_reviewer|bug_reviewer|tool|human",
  "category": "bug|security|test|performance|maintainability|ops|docs",
  "severity": "critical|high|medium|low|info",
  "confidence": "high|medium|low",
  "evidence_level": 0,
  "summary": "",
  "affected_files": [],
  "evidence_refs": [],
  "tool_refs": [],
  "is_veto_candidate": false,
  "requires_human_review": false,
  "recommended_action": "",
  "status": "open|verified|false_positive|accepted_risk|fixed|deferred"
}
```

## 8. Veto Rule

### 8.1 Ứng viên Veto

```text
- thiếu sót authorization
- authentication bypass
- rò rỉ PII/secret
- SQL/command injection
- data loss / irreversible migration
- tính toán sai payment/amount/quantity
- thiếu audit log
- không thể rollback
- đề xuất cho phép AI production access
- test/build/typecheck failure
```

### 8.2 Xử lý Veto

```text
1. Phát hiện ứng viên Veto
2. Kiểm tra Tool evidence hoặc source evidence
3. Đánh giá khả năng false positive
4. Đẩy lên Human Review bắt buộc
5. Không được merge cho đến khi giải quyết, hoặc phải có Accepted Risk rõ ràng
```

## 9. Weighted Consensus

### 9.1 Ví dụ trọng số

| Lĩnh vực | Agent/Tool có trọng số cao |
|---|---|
| Security | Security Reviewer, SAST, Human Security |
| Test | Test Reviewer, test results, coverage |
| Performance | benchmark, query plan, Performance Reviewer |
| Architecture | Architect, Tech Lead |
| Contract | OpenAPI/Pact/contract test, FE/BE owner |
| Operation | SRE/Ops Reviewer, runbook, telemetry |

### 9.2 Consensus Record

```md
# Consensus Record

## 1. Summary
- Overall verdict:
- Recommended PR decision:
- Confidence:

## 2. Inputs
| Source | Type | Version | Scope |
|---|---|---|---|

## 3. Consolidated Findings
| ID | Severity | Category | Summary | Evidence Level | Status |
|---|---|---|---|---|---|

## 4. Veto Candidates
| ID | Reason | Evidence | Required action | Owner |
|---|---|---|---|---|

## 5. Disagreements
| ID | Topic | Agent A | Agent B | Tool result | Resolution |
|---|---|---|---|---|---|

## 6. Tool Results
| Tool | Verdict | Key finding | Raw ref |
|---|---|---|---|

## 7. Human Review Required
| Topic | Reason | Required reviewer | Deadline |
|---|---|---|---|

## 8. Final Decision
- Approve / Request changes / Block / Needs human review / Defer:
- Conditions:
```

## 10. Policy Engine

Policy Engine là quy tắc quyết định luận để chuyển Consensus thành PR judgment.

```yaml
policy:
  block_merge:
    - tool.build == "fail"
    - tool.typecheck == "fail"
    - tool.test.required == "fail"
    - finding.security.severity in ["critical", "high"] and finding.status != "accepted_risk"
    - finding.data_loss == true and human_approval == false
  needs_human_review:
    - agent.disagreement.severity in ["critical", "high"]
    - source_confidence_score < 3
    - db_migration == true
    - auth_permission_changed == true
  allow_with_conditions:
    - low_findings_only == true
    - required_tests_pass == true
    - accepted_risks_documented == true
```

## 11. PR Decision Schema

```json
{
  "decision": "approve|request_changes|block|needs_human_review|defer",
  "confidence": "high|medium|low",
  "blocking_findings": [],
  "non_blocking_findings": [],
  "tool_results": [],
  "human_review_required": [],
  "accepted_risks": [],
  "conditions_to_approve": [],
  "traceability_refs": []
}
```

## 12. Góc nhìn kiểm tra theo từng Tool

### 12.1 Build / Typecheck

```text
- compile error
- missing import
- generated type mismatch
- nullable error
- unreachable code
- framework-specific type error
```

### 12.2 Unit / Integration / E2E

```text
- required tests executed
- thiên lệch kiểu chỉ changed tests pass nhưng regression không được chạy
- có phải flaky test không
- lý do skipped test
- test data có thỏa đặc tả không
```

### 12.3 SAST / Secrets / SCA

```text
- severity
- exploitability
- có phải reachable code không
- khả năng false positive
- có sửa được dependency không
- điều kiện accepted risk
```

### 12.4 Contract Test

```text
- phá vỡ request/response
- không khớp optional/required
- ảnh hưởng khi thêm enum/master
- thay đổi error schema
- backward compatibility
```

### 12.5 Migration Dry-run

```text
- có reversible không
- lock risk
- existing data violation
- backfill có thể chạy lại không
- rollback plan
```

## 13. Human Override

Con người có thể override phán đoán của AI/Tool. Tuy nhiên, phải ghi lại lý do và điều kiện.

```md
# Human Override Record

## Finding / Decision
- ID:
- Original decision:
- Override decision:

## Reason
- Business reason:
- Technical reason:
- Risk acceptance:

## Evidence
- Tool results:
- Human review notes:

## Conditions
- Follow-up ticket:
- Monitoring:
- Expiry / Re-review trigger:
```

## 14. Prompt thực thi 43

```md
Bạn là người phụ trách Tool-Grounded Verification của SDD Ver.04.
Hãy tích hợp kết quả AI review và Tool result, rồi tạo phương án phán đoán cho PR/thay đổi.

# Input
- Agent outputs:
- Tool results:
- Source Confidence Score:
- Risk policy:
- Human review rules:
- Token/cost constraints:

# Quy tắc
- Tách ý kiến AI và Tool evidence
- Ưu tiên Tool failure hơn AI consensus
- Security/Data critical phải là ứng viên Veto
- Không dùng đa số phiếu, hãy dùng Weighted Consensus
- Không che giấu thiếu evidence
- Nêu rõ nơi cần human review
- Chuẩn hóa PR decision bằng schema

# Output
1. Tool Result Summary
2. Consolidated Findings
3. Veto Candidates
4. Disagreements
5. Đánh giá Evidence Level
6. Phán định Policy Engine
7. Human Review Required
8. PR Decision Schema
9. Evidence cần lưu sang 33
10. Ứng viên Failure Mode cần đăng ký sang 29
```

## 15. Failure Mode

| ID | Failure Mode | Mitigation |
|---|---|---|
| TGV-001 | Xem ý kiến AI là evidence | Evidence hierarchy |
| TGV-002 | Bỏ qua Tool failure | Policy block |
| TGV-003 | Bác bỏ chỉ摘 Security bằng đa số phiếu | Veto Rule |
| TGV-004 | Đưa toàn văn raw log làm token bùng nổ | Tool Output Compression |
| TGV-005 | Không học từ false positive | Ghi vào 29/49 |
| TGV-006 | accepted risk chỉ nói miệng | Human Override Record |
| TGV-007 | Xem test chưa chạy là pass | Tool status explicit |
| TGV-008 | approve dù source confidence thấp | Source Confidence gate |
| TGV-009 | PR decision mơ hồ | Decision schema |
| TGV-010 | Không rõ Tool version/env | Tool Result Record |

## 16. Metrics

```text
- tool pass/fail rate
- AI finding verification rate
- false positive rate
- valid finding rate
- veto count
- human review escalation count
- accepted risk count
- PR block accuracy
- time to decision
- cost per verified finding
```

## 17. Definition of Ready

```text
- Có Agent output hoặc review findings
- Required Tool Matrix đã được quyết định
- Có nơi lưu Tool result
- Có điều kiện block/human của Policy Engine
- Có Source Confidence Score
- Human reviewer đã được quyết định
```

## 18. Definition of Done

```text
- Có Tool Result Record
- AI Finding đã được chuẩn hóa
- Có Consensus Record
- Veto / Human Review condition đã được xử lý
- PR Decision Schema đã được output
- evidence đã được lưu sang 33 Artifact Governance
- đã kết nối ứng viên đánh giá/thất bại sang 29/49
```



## 19. Quy tắc Evidence Linking

Tất cả finding quan trọng phải link tới ít nhất 1 Evidence.

```text
Định dạng Evidence ID:
- SRC-xxx: source evidence
- TST-xxx: test evidence
- SEC-xxx: security tool evidence
- DB-xxx: DB/migration evidence
- HUM-xxx: human decision evidence
- OBS-xxx: observability/production evidence
```

```md
# Evidence Link

| Finding | Evidence ID | Evidence Type | Strength | Limitation |
|---|---|---|---|---|
```

Finding không có Evidence được xử lý như `hypothesis` và không dùng để block. Tuy nhiên, nghi ngờ Security/Data critical phải được đẩy lên human review.

## 20. Finding Status Lifecycle

```text
proposed
  ↓
needs_evidence
  ↓
verified / false_positive / accepted_risk / duplicate / deferred
  ↓
fixed
  ↓
regression_tested
  ↓
closed
```

Ý nghĩa từng status.

| Status | Ý nghĩa |
|---|---|
| proposed | Agent/con người đã nêu chỉ摘 nhưng chưa kiểm chứng |
| needs_evidence | Thiếu evidence |
| verified | Đã xác nhận bằng source/tool/human |
| false_positive | Ghi nhận là phát hiện nhầm |
| accepted_risk | Đã chấp nhận rủi ro. Bắt buộc có hạn và điều kiện |
| duplicate | Được gộp vào finding khác |
| deferred | Hoãn sang ticket khác |
| fixed | Đã sửa |
| regression_tested | Đã xác nhận test chống tái phát |
| closed | Hoàn tất |

## 21. Xử lý False Positive

Không vứt bỏ phát hiện nhầm của AI review, mà biến chúng thành tài sản học tập.

```md
# False Positive Record

## Finding
- ID:
- Agent:
- Summary:

## Why False Positive
- Misread source:
- Missing context:
- Project-specific rule:
- Tool limitation:

## Prevention
- Prompt update:
- Context update:
- Project Knowledge update:
- Tool filter update:
```

## 22. Xử lý Accepted Risk

Accepted Risk không phải là “bỏ qua”.

```md
# Accepted Risk Record

## Risk
- ID:
- Severity:
- Impact:

## Acceptance Reason
- Business reason:
- Technical reason:
- Alternatives considered:

## Conditions
- Expiry:
- Monitoring:
- Follow-up ticket:
- Owner:

## Approval
- Approved by:
- Date:
```

## 23. Cách xử lý khi Tool Failure

Khi Tool bị fail, không để AI phán đoán “có lẽ không sao”.

| Trạng thái Tool | Phán đoán |
|---|---|
| pass | Có thể dùng làm evidence |
| fail | Về nguyên tắc block hoặc request changes |
| not run | Xử lý là chưa kiểm chứng |
| flaky | human review hoặc chạy lại |
| partial | Nêu rõ scope limitation |
| tool unavailable | Ghi fallback và để con người phán đoán |

## 24. Phiên bản thực dụng của Consensus Algorithm

```text
1. Chuẩn hóa Findings theo severity
2. Gộp duplicate
3. Gán evidence level
4. Trích xuất ứng viên veto
5. Đối chiếu với tool result
6. Trích xuất disagreement
7. Áp dụng policy engine
8. Gán điều kiện human review
9. Đưa ra PR decision
```

## 25. Quy tắc tạo Review Comment

PR comment quá nhiều thì sẽ không được đọc.

```text
Blocking:
- Bắt buộc comment
- Ghi rõ evidence và điều kiện sửa

High but non-blocking:
- Chỉ summary + vị trí quan trọng

Medium/Low:
- Comment tổng hợp hoặc chỉ ghi trong artifact

Info:
- Về cơ bản không PR comment. Ghi vào report.
```

## 26. Những thứ lưu từ 43 sang 33

| Thành quả 43 | Nơi lưu trong 33 |
|---|---|
| Tool Result Record | Evidence Record |
| Consensus Record | Decision Record / Traceability Matrix |
| PR Decision Schema | Human Approval Record / Release Readiness |
| Accepted Risk Record | Decision Record |
| False Positive Record | Failure Mode / Evaluation dataset |

## 27. Feedback từ 43 sang 29/49

```text
Sang 29:
- missed bug
- repeated false positive
- thiếu source confidence
- tool gap
- human override

Sang 49:
- valid finding rate
- false positive rate
- cost per verified finding
- tool failure rate
- policy decision accuracy
```

## 28. Prompt Review Consensus

```md
Bạn là Consensus Reviewer của SDD Ver.04.
Hãy review Consensus Record dưới đây và xác nhận liệu nó có an toàn như một PR judgment hay không.

# Input
- Consensus Record
- Tool Result Records
- Policy rules
- Human Override / Accepted Risk

# Góc nhìn kiểm tra
- evidence level có thỏa đáng không
- tool failure có bị bỏ qua không
- security/data veto có bị dập đi không
- phán đoán false positive có căn cứ không
- accepted risk có expiry/owner không
- PR comment có quá nhiều/quá ít không

# Output
1. Chất lượng Consensus
2. Thiếu sót phán đoán nguy hiểm
3. tool/human review bổ sung
4. Đề xuất sửa PR decision
```

## Tài liệu/tiêu chuẩn công khai bên ngoài đã tham khảo

Các Advanced Options này lấy tài liệu SDD nội bộ, thành quả V04 của 11 và 21〜29・31〜34, tài liệu đính kèm “AI精度向上のための追加戦略_20260516.md” và “AIトークン削減のための追加戦略_20260516.md” làm input chính, đồng thời đưa tư tưởng của các tài liệu/tiêu chuẩn công khai sau vào ngữ cảnh SDD.

- OpenAI Agents SDK: các yếu tố thiết kế Agent như handoffs, guardrails, function tools, MCP server tool calling, sandbox agents.
- OpenAI Prompt Caching / Cost Optimization / Batch API / Flex Processing: exact prefix caching, thiết kế static prefix, xử lý bất đồng bộ và chi phí thấp.
- OpenAI Structured Outputs: nâng cao khả năng xử lý bằng máy và tính tái hiện bằng output có cấu trúc tuân theo JSON Schema.
- Model Context Protocol Security Best Practices: vector tấn công đặc thù của MCP implementation, quyền hạn, rủi ro thực thi tool.
- NIST SSDF SP 800-218: secure development practice có thể tích hợp vào Secure SDLC.
- OWASP ASVS / OWASP LLM Top 10 / OWASP GenAI Security: rủi ro Web/API security và LLM/Agent đặc thù.
- SLSA / OpenSSF Scorecard: chuỗi cung ứng phần mềm, dependency, build evidence, đánh giá sức khỏe OSS.
- OpenTelemetry GenAI semantic conventions: thiết kế quan sát cho AI/Agent call, tool call, latency, token, error, v.v.
- Recursive Multi-Agent Systems: nghiên cứu xem multi-agent collaboration như recursive computation. Trong thực務, SDD chỉ áp dụng theo hướng RecursiveMAS-inspired có giới hạn.
- LongLLMLingua / Prompt Compression: tư tưởng về mật độ thông tin quan trọng, positional bias và compression trong context dài.
- RTK / Rust Token Killer: tư tưởng thực dụng về giảm token bằng cách nén CLI output trước khi đưa vào LLM context.
- SWE-bench / SWE-bench Verified: tham khảo cho thiết kế coding agent evaluation và regression evaluation dataset.
- everything-claude-code: tư tưởng vận hành skills, rules, hooks, MCP, security scanning, continuous learning, cross-harness. Tuy nhiên trong SDD chỉ chọn áp dụng một cách an toàn.


---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste

> Appendix này là “execution wrapper” để người mới cũng có thể thực thi Tool-Grounded Verification / Consensus được định nghĩa trong phần chính một cách an toàn.  
> Không thay đổi nội dung phần chính. Hãy dùng phần chính như “đặc tả thiết kế cho Tool result, AI Finding, Veto, Consensus”, và dùng Appendix này như quy trình “nhập Tool result theo thứ tự nào, chuẩn hóa ra sao, và chuyển sang Gate judgment như thế nào”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

43 là Option để tích hợp ý kiến AI với Tool/CI/Test/Security result và tiến gần hơn tới phán đoán an toàn.  
Người mới không được coi 43 là “việc cho AI đọc Tool result rồi tóm tắt”, mà phải coi đây là **việc lưu Tool result như Evidence, ưu tiên Tool result hơn ý kiến AI, đồng thời minh thị Veto và phán đoán của con người**.

```text
1. Không xem Tool result nhẹ hơn ý kiến AI.
2. Không PASS bằng AI majority khi Tool result đang thất bại.
3. Trước tiên bắt AI đưa ra Verification Plan בלבד.
4. Không Gate judgment, PR judgment, thay đổi CI setting cho đến khi con người phê duyệt Plan.
5. Raw log nếu có thể phải lưu trong file hoặc CI artifact, còn AI chỉ nhận bản nén.
6. Compressed Tool Output phải luôn để lại Raw Log Reference.
7. AI Finding phải được chuẩn hóa tách riêng với Tool Finding.
8. Security High, test failure, build failure, policy violation phải được xử lý như ứng viên Veto.
9. False Positive, Accepted Risk, Human Override phải được chứng cứ hóa.
10. Cuối cùng thực hiện Consensus Review và phán định cổng hoàn tất.
```

Nơi lưu cơ bản dùng trong Appendix này như sau.

```text
Thành quả chuyên dụng của pack:
docs/changes/{{TICKET}}/43-tool-grounded-verification/

Ví dụ nơi tham chiếu raw artifact của Tool:
CI artifact URL
PR check URL
local log path
screenshots path
coverage report path
SAST/SCA report path

Thành quả đăng ký sang 33:
docs/changes/{{TICKET}}/43-tool-grounded-verification/33-registration.md

Feedback sang 29/49:
docs/changes/{{TICKET}}/43-tool-grounded-verification/29-feedback.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/49-feedback.md
```

Tư tưởng quan trọng.

```text
Mục tiêu của 43 không phải là “làm cho phán đoán của AI thành câu văn thuyết phục hơn”,
mà là tách Tool evidence, AI finding, human judgment và làm cho Gate judgment có thể giải thích được về sau.
```

---

## A-1. Khi nào dùng pack này

### Trường hợp nên dùng

```text
- Muốn tích hợp kết quả Build / typecheck / lint / unit / integration / E2E / SAST / SCA / secrets scan
- Muốn kiểm chứng Findings của 42 Multi-Agent bằng Tool
- Chỉ摘 của Codex/Claude/human review và CI result đang mâu thuẫn
- Muốn phán đoán PR merge, Phase Gate, Release readiness kèm Evidence
- Không muốn bỏ sót Security High, Test failure, Tool failure, Policy violation
- Muốn chứng cứ hóa False Positive hoặc Accepted Risk
- Muốn đăng ký Tool evidence sang 33 Artifact Governance
- Muốn trả vật liệu cải thiện chất lượng sang 29/49
```

### Trường hợp có thể làm nhẹ

```text
- Thay đổi nhỏ, chỉ cần kiểm tra thủ công và test hiện có là đủ
- Tool result đã được sắp xếp rõ trong report.md hoặc test-results.md
- 28 đã phán định vận hành nhẹ và không cần Gate judgment
- Chỉ là điều tra ban đầu hoặc review bản nháp, không phải PR judgment
```

Ngay cả khi làm nhẹ, tối thiểu vẫn phải lưu lại những điểm sau.

```text
- Tool đã chạy
- Tool chưa chạy và lý do
- Summary Tool result
- Không có thất bại, hoặc đã xử lý thất bại như thế nào
- Lý do không thực hiện Gate judgment
```

### Trường hợp không dùng, hoặc cần quay lại pack khác trước

```text
- Tool chưa chạy, hoặc không truy cập được kết quả chạy
- Không có nơi lưu Raw log hoặc artifact
- Có khả năng Tool output chứa secret hoặc PII
- Output quá lớn đến mức cần 44 cho Tool Output Compression hoặc Token Budget
- Agent output của 42 chưa được sắp xếp, chưa rõ cần Tool kiểm chứng điều gì
- 33 chưa có quy tắc đăng ký artifact/chính bản
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 43
{{PACK_NAME}}: Tool-Grounded Verification and Consensus Option
{{PACK_SLUG}}: tool-grounded-verification
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{VERIFICATION_OBJECTIVE}}:
{{REQUIRED_TOOLS}}:
{{RAW_LOG_LOCATIONS}}:
{{GATE_DECISION_TARGET}}: Phase Gate / PR / Release / Advisory only
{{VETO_POLICIES}}:
{{ACCEPTED_RISK_APPROVER}}:
```

Ví dụ điền.

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{SCOPE_NOTE}}: Bao gồm API, quyền hạn, gửi email, E2E
{{RISK_LEVEL}}: High
{{SDD_MODE}}: M3
{{TIMEBOX}}: Đến mức tích hợp Tool result và draft PR Decision
{{VERIFICATION_OBJECTIVE}}: Tích hợp CI/Test/Security/Agent Findings và tạo vật liệu Gate judgment trước merge
{{REQUIRED_TOOLS}}: build, typecheck, lint, unit, integration, e2e, secrets scan
{{RAW_LOG_LOCATIONS}}: CI artifact URL, dưới local logs/
{{GATE_DECISION_TARGET}}: PR
{{VETO_POLICIES}}: build failure, test failure, secrets, Security High là Veto
{{ACCEPTED_RISK_APPROVER}}: Tech Lead / Security Owner
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
@docs/changes/{{TICKET}}/report.md
@docs/architecture/
@docs/standards/
@.claude/CLAUDE.md
@.claude/rules/
```

### Input đặc biệt cần đọc trong pack này

```text
@docs/changes/{{TICKET}}/40-advanced-options-selection/advanced-option-selection-record.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/43-handoff.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/blackboard.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/arbiter-consensus.md
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-inventory.md
@docs/changes/{{TICKET}}/44-token-cost-control/tool-output-summary.md
```

### Ứng viên Tool result cần thu nhận

```text
- build
- typecheck
- lint
- unit test
- integration test
- E2E
- coverage
- SAST
- secrets scan
- SCA / dependency scan
- contract test
- migration dry-run
- performance smoke
- accessibility check
- policy check
```

### Lưu ý trước khi đưa cho AI

```text
- Không đưa toàn bộ Raw log, hãy tóm tắt thành Compressed Tool Output
- Nếu có khả năng chứa secret/PII/token, phải mask trước
- Failure log phải giữ lại vị trí thất bại, bước tái hiện, exit code, tên test liên quan
- Tool đã pass cũng phải giữ lại command và phạm vi thực thi
- Tool chưa chạy phải ghi là “chưa chạy”, không được che giấu
```

---

## A-4. Thành quả cần tạo/cập nhật

### Thư mục chuyên dụng của pack

```text
docs/changes/{{TICKET}}/43-tool-grounded-verification/
```

### Thành quả tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/43-tool-grounded-verification/verification-plan.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/tool-result-record.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/compressed-tool-output.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/ai-finding-normalization.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/consensus-record.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/veto-log.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/human-review-required.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/consensus-review.md
```

### Thành quả cần tạo nếu cần

```text
docs/changes/{{TICKET}}/43-tool-grounded-verification/pr-decision.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/human-override-record.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/false-positive-record.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/accepted-risk-record.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/tool-failure-record.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/33-registration.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/29-feedback.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/49-feedback.md
docs/changes/{{TICKET}}/43-tool-grounded-verification/promotion-candidates.md
```

### Những thứ có thể phản ánh vào Core artifacts

```text
docs/changes/{{TICKET}}/test-results.md
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/report.md
```

---

## A-5. Quy trình thực thi

### Step 1. Tạo Verification Plan

Đầu tiên quyết định các điểm sau.

```text
- Phán đoán điều gì
- Sử dụng Tool result nào
- Nơi lưu Raw log
- Phạm vi Compressed Tool Output đưa cho AI
- Veto policy
- Cách xử lý False Positive / Accepted Risk / Human Override
- Đối tượng của Gate decision
```

### Step 2. Tạo Tool Result Record

Với từng Tool, ghi lại các điểm sau.

```text
- Tool name
- Command / CI job
- Scope
- Result: PASS / FAIL / SKIPPED / ERROR
- Key findings
- Raw log reference
- Limitations
- Related SDD artifacts
```

### Step 3. Nén Tool Output

Trước khi đưa cho AI, tạo bản nén.

```text
Những thứ giữ lại:
- command
- verdict
- exit code
- failed test names
- trọng điểm của error messages
- file/line
- raw log reference
- điểm AI nên phân tích
- điểm AI không được suy đoán

Những thứ loại bỏ:
- log trùng lặp
- lượng lớn success log
- progress bar
- toàn bộ stack trace. Tuy nhiên cần giữ phần quan trọng
- secret/PII/token
```

### Step 4. Chuẩn hóa AI Finding

Agent hoặc chỉ摘 review được chuẩn hóa riêng, không trộn với Tool result.

```text
- Finding ID
- Source: AI / Tool / Human
- Severity
- Evidence
- Confidence
- Tool verified: Yes / No / Needed / Contradicted
- Status
```

### Step 5. Áp dụng Veto Rule

Những mục sau về nguyên tắc là ứng viên Veto.

```text
- build failure
- typecheck failure
- test failure
- secrets detected
- Security High/Critical
- migration dry-run failure
- contract breaking change
- policy violation
- required tool not run
```

### Step 6. Tạo Consensus Record

Consensus không phải đa số phiếu, mà được tạo theo Evidence hierarchy.

```text
1. Tool evidence
2. Human verified evidence
3. Code diff / artifact evidence
4. AI finding with evidence
5. AI opinion without evidence
```

### Step 7. Tách Human Review / Override / Accepted Risk

Không che giấu những thứ cần phê duyệt của con người.

```text
- Human Review Required
- Human Override Record
- Accepted Risk Record
- False Positive Record
```

### Step 8. Chuyển sang Gate Decision

Gate judgment là một trong các giá trị sau.

```text
PASS
PASS_WITH_ACCEPTED_RISK
NEEDS_UPDATE
BLOCKED
ADVISORY_ONLY
```

---

## A-6. Dùng để copy-paste: Prompt bắt đầu

```text
Bạn là người hỗ trợ thực thi “43 Tool-Grounded Verification and Consensus Option” của SDD Ver.04.
Bây giờ hãy tạo Verification Plan để tích hợp Tool result, AI Findings và human judgment cho {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không xem Tool result nhẹ hơn ý kiến AI.
- Không PASS Tool failure bằng đa số phiếu của AI.
- Trước hết chỉ trình bày Verification Plan.
- Không Gate judgment, PR judgment, thay đổi CI setting, chỉnh sửa file cho đến khi tôi phê duyệt Plan.
- Thiết kế theo tiền đề Raw log sẽ được giữ lại bằng reference, còn AI nhận bản nén.
- Hãy tách Tool Finding, AI Finding, Human Finding.
- Security High, test failure, build failure, policy violation phải được xử lý như ứng viên Veto.
- False Positive, Accepted Risk, Human Override phải được chứng cứ hóa.
- Không đưa secret, PII, token, credential, log production nguyên bản.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Verification Objective: {{VERIFICATION_OBJECTIVE}}
- Required Tools: {{REQUIRED_TOOLS}}
- Raw Log Locations: {{RAW_LOG_LOCATIONS}}
- Gate Decision Target: {{GATE_DECISION_TARGET}}
- Veto Policies: {{VETO_POLICIES}}
- Accepted Risk Approver: {{ACCEPTED_RISK_APPROVER}}

【Plan bắt buộc phải bao gồm】
1. Có áp dụng 43 hay không
2. Tool result sử dụng và Tool không sử dụng
3. Nơi lưu Raw log
4. Phương châm tạo Compressed Tool Output
5. Phương châm chuẩn hóa AI Finding
6. Veto Rule
7. Consensus Algorithm
8. Cách xử lý False Positive / Accepted Risk / Human Override
9. Kế hoạch feedback sang 33/29/49
10. Thành quả cần tạo/cập nhật và nơi lưu
11. Điều kiện Stop/Ask
12. Cổng hoàn tất

Trước hết chỉ trình bày Plan. Chưa thực hiện Gate judgment hoặc chỉnh sửa file.
```

---

## A-7. Dùng để copy-paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật thành quả của 43 Tool-Grounded Verification.

【Quy tắc thực thi】
- Trước tiên hãy tạo verification-plan.md.
- Với từng Tool, hãy ghi kết quả, phạm vi, Raw log reference, ràng buộc vào tool-result-record.md.
- Log đưa cho AI phải được tóm tắt thành compressed-tool-output.md.
- Hãy tách và sắp xếp AI Finding, Tool Finding, Human Finding trong ai-finding-normalization.md.
- Ứng viên Veto phải được giữ trong veto-log.md.
- Consensus phải được ghi trong consensus-record.md theo Evidence hierarchy.
- Không che giấu Human Review Required, Accepted Risk, False Positive, Human Override; hãy tách riêng.
- Nếu có nội dung phản ánh sang 33/29/49, hãy ghi vào từng file feedback/registration tương ứng.
- Sau khi làm xong, hãy tự phán định Consensus Review và cổng hoàn tất.
```

---

## A-8. Dùng để copy-paste: Prompt review thành quả và phán định hoàn tất

```text
Bạn là independent reviewer của SDD Ver.04.
Hãy review các thành quả 43 Tool-Grounded Verification dưới đây và phán định có thể tiến tới Gate judgment hay không.

【Đối tượng review】
@docs/changes/{{TICKET}}/43-tool-grounded-verification/verification-plan.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/tool-result-record.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/compressed-tool-output.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/ai-finding-normalization.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/consensus-record.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/veto-log.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/human-review-required.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/consensus-review.md

【Góc nhìn review】
1. Tool result có được ưu tiên hơn ý kiến AI không
2. Tool chưa chạy hoặc Tool failure có bị che giấu không
3. Raw log reference có còn không
4. Compressed Tool Output có làm rơi mất thông tin quan trọng không
5. AI Finding và Tool Finding có bị trộn không
6. Ứng viên Veto có bị dập bằng đa số phiếu không
7. Accepted Risk có người phê duyệt và điều kiện không
8. Xử lý False Positive có căn cứ không
9. Human Override có được chứng cứ hóa không
10. Gate judgment có dựa trên Evidence không
11. Việc phản ánh sang 33/29/49 có được ghi khi cần không
12. Có thỏa cổng hoàn tất không

【Định dạng output】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Tool evidence gaps
- Veto candidates
- Unjustified AI opinions
- Missing raw log references
- Required human decisions
- Gate decision recommendation
- Required updates before PR/Phase Gate
- Final completion gate checklist
- Next action
```

---

## A-9. Dùng để copy-paste: Prompt trả về sửa

```text
Dựa trên các chỉ摘 review dưới đây, hãy sửa thành quả 43 Tool-Grounded Verification.

【Quy tắc sửa】
- Trước khi bắt đầu, hãy diễn giải lại ý định của chỉ摘 trong 1 dòng.
- Hãy liệt kê trước các thành quả bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Nếu cần kiểm tra lại Tool result, hãy ghi rõ Tool nào, Raw log nào, phạm vi nào.
- Nếu thay đổi ứng viên Veto, hãy cập nhật veto-log.md và consensus-record.md.
- Nếu thay đổi Accepted Risk / False Positive / Human Override, hãy ghi rõ người phê duyệt, lý do, điều kiện.
- Nếu thay đổi Gate Decision, hãy ghi căn cứ và ảnh hưởng.
- Nếu nội dung phản ánh sang 33/29/49 thay đổi, hãy cập nhật feedback/registration tương ứng.

【Chỉ摘 review】
Dán chỉ摘 vào đây
```

---

## A-10. Điều kiện Stop/Ask cho người mới

Nếu rơi vào bất kỳ điều kiện nào sau đây, hãy dừng Gate judgment và quay lại hỏi con người.

```text
- Required Tool chưa chạy
- Tool đang fail nhưng nguyên nhân chưa được xác nhận
- Không có Raw log reference
- Đang định đưa Tool output có khả năng chứa secret/PII/token cho AI
- Đang định bỏ qua build/typecheck/test/security scan failure bằng ý kiến AI
- Đang định biến Security High/Critical thành Accepted Risk nhưng không có người phê duyệt
- Lý do False Positive không có Evidence
- Human Override chỉ là phán đoán miệng, chưa được chứng cứ hóa
- Consensus đang trở thành đa số phiếu
- Đối tượng và người chịu trách nhiệm của Gate Decision không rõ
```

Định dạng output khi Stop/Ask.

```text
- Stop Reason:
- Affected tool / finding:
- Evidence gap:
- Risk:
- Required human decision:
- Minimal safe next step:
```

---

## A-11. Cổng hoàn tất

Pack này chỉ hoàn tất khi thỏa tất cả điều kiện sau.

```text
- [ ] Verification Plan đã được phê duyệt
- [ ] Tool Result Record đã được tạo
- [ ] Raw log reference còn lại
- [ ] Compressed Tool Output đã được tạo
- [ ] AI Finding / Tool Finding / Human Finding được tách riêng
- [ ] Ứng viên Veto được ghi lại và không bị dập bằng đa số phiếu
- [ ] Consensus Record tuân theo Evidence hierarchy
- [ ] Tool chưa chạy, Tool failure, ràng buộc không bị che giấu
- [ ] Accepted Risk có người phê duyệt, lý do, điều kiện
- [ ] False Positive có căn cứ và biện pháp chống tái phát
- [ ] Human Override được chứng cứ hóa
- [ ] Gate Decision dựa trên Evidence
- [ ] Consensus Review không còn Blocker
- [ ] Nội dung cần phản ánh sang 33/29/49 đã được minh thị
```

---

## A-12. Điểm cần đi tiếp theo

```text
Gate judgment PASS                     → Đi tiếp tới PR/Phase Gate
Cần sửa                                → Quay lại impl-plan / implementation / test
Tool result quá lớn                    → Quay lại 44 để nén
Agent findings thiếu                   → Quay lại 42
Thiếu căn cứ source                    → Quay lại 41
Cần đăng ký Artifact                   → Phản ánh sang 33
Cần đưa vào Failure Mode               → Phản ánh sang 29
Muốn đưa vào đánh giá/cải thiện        → Phản ánh sang 49
Cần phê duyệt Security                 → Đi tới 25 hoặc 45
```

Cuối cùng, kết quả của 43 được tóm tắt trong `report.md` dưới tên “Tool-Grounded Verification Summary” để sau này có thể giải thích Tool evidence và Gate judgment.
