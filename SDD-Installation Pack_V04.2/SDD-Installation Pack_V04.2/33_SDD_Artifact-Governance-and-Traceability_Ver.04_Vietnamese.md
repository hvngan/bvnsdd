**Mục lục**
- [33_SDD_Artifact-Governance-and-Traceability_Ver.04_Vietnamese](#33_sdd_artifact-governance-and-traceability_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Kết luận](#1-kết-luận)
  - [2. Phân loại Artifact](#2-phân-loại-artifact)
  - [3. Trạng thái Artifact](#3-trạng-thái-artifact)
  - [4. Tiêu chuẩn Front Matter](#4-tiêu-chuẩn-front-matter)
  - [5. Cấu trúc thư mục khuyến nghị](#5-cấu-trúc-thư-mục-khuyến-nghị)
  - [6. Artifact Inventory](#6-artifact-inventory)
  - [7. Traceability Matrix](#7-traceability-matrix)
  - [8. Decision Record](#8-decision-record)
  - [9. Evidence Record](#9-evidence-record)
  - [10. Human Approval Record](#10-human-approval-record)
  - [11. Artifact Freshness Check](#11-artifact-freshness-check)
  - [12. Artifact Reconciliation](#12-artifact-reconciliation)
  - [13. Quy tắc quản lý bản chính](#13-quy-tắc-quản-lý-bản-chính)
  - [14. Cách xử lý AI Output](#14-cách-xử-lý-ai-output)
  - [15. Tư duy về Provenance](#15-tư-duy-về-provenance)
  - [16. Audit Package](#16-audit-package)
  - [17. Release Readiness Record](#17-release-readiness-record)
  - [18. Prompt chuyên dụng cho 33](#18-prompt-chuyên-dụng-cho-33)
  - [19. Metrics](#19-metrics)
  - [20. Failure Mode tiêu biểu](#20-failure-mode-tiêu-biểu)
  - [21. Definition of Done](#21-definition-of-done)
  - [22. Kết nối với CI/CD](#22-kết-nối-với-cicd)
  - [23. Kết nối với PR template](#23-kết-nối-với-pr-template)
  - [24. Kết nối với SBOM / Attestation](#24-kết-nối-với-sbom--attestation)
  - [25. Artifact Naming Convention](#25-artifact-naming-convention)
  - [26. Artifact Retention Policy](#26-artifact-retention-policy)
  - [27. Chia nhỏ Artifact cho dự án quy mô lớn](#27-chia-nhỏ-artifact-cho-dự-án-quy-mô-lớn)
  - [27-A. Quản lý Artifact của Advanced Options nhóm 40](#27-a-quản-lý-artifact-của-advanced-options-nhóm-40)
  - [28. Artifact Quality Checklist](#28-artifact-quality-checklist)
  - [Tài liệu, tiêu chuẩn công khai đã tham khảo](#tài-liệu-tiêu-chuẩn-công-khai-đã-tham-khảo)
- [Appendix. Dành cho người mới: Quy trình thực thi và prompt copy-paste của pack này](#appendix-dành-cho-người-mới-quy-trình-thực-thi-và-prompt-copy-paste-của-pack-này)
  - [A-0. Quy tắc tuyệt đối phải tuân thủ trước tiên](#a-0-quy-tắc-tuyệt-đối-phải-tuân-thủ-trước-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Artifact cần tạo/cập nhật](#a-4-artifact-cần-tạocập-nhật)
  - [A-5. Quy trình thực thi cho người mới](#a-5-quy-trình-thực-thi-cho-người-mới)
  - [A-6. Dùng để copy-paste: Prompt bắt đầu chỉ lập Plan](#a-6-dùng-để-copy-paste-prompt-bắt-đầu-chỉ-lập-plan)
  - [A-7. Checklist kiểm tra Plan](#a-7-checklist-kiểm-tra-plan)
  - [A-8. Dùng để copy-paste: Prompt phê duyệt Plan](#a-8-dùng-để-copy-paste-prompt-phê-duyệt-plan)
  - [A-9. Dùng để copy-paste: Prompt review artifact và phán định hoàn tất](#a-9-dùng-để-copy-paste-prompt-review-artifact-và-phán-định-hoàn-tất)
  - [A-10. Dùng để copy-paste: Prompt trả về sửa](#a-10-dùng-để-copy-paste-prompt-trả-về-sửa)
  - [A-11. Điều kiện Stop/Ask](#a-11-điều-kiện-stopask)
  - [A-12. Completion Gate](#a-12-completion-gate)
  - [A-13. Điểm tiếp theo cần đi tới](#a-13-điểm-tiếp-theo-cần-đi-tới)
  - [A-14. Lỗi người mới hay mắc và cách phòng tránh](#a-14-lỗi-người-mới-hay-mắc-và-cách-phòng-tránh)
  - [A-15. Lộ trình ngắn nhất](#a-15-lộ-trình-ngắn-nhất)

# 33_SDD_Artifact-Governance-and-Traceability_Ver.04_Vietnamese

Ngày tạo: 2026-05-16  
Đối tượng: Quản lý bản chính, quản lý bằng chứng, kiểm toán, bảo đảm chất lượng, review bằng nhiều AI, dự án dài hạn đối với artifact SDD  
Kết nối tới: 21〜32, 34, 40〜49

---

## 0. Vai trò của tài liệu này

Tài liệu này là tiêu chuẩn để quản lý **bản chính, trạng thái, độ mới, căn cứ, quan hệ phái sinh, phê duyệt và truy xuất nguồn gốc** của các artifact được tạo ra trong SDD.

Trong SDD Ver.04, số lượng artifact sẽ tăng lên.

```text
- source-availability.md
- context-manifest.md
- source-inventory.md
- spec-pack.md
- impact-analysis.md
- impl-plan.md
- review-checklist.md
- security-review.md
- self-review.md
- codex-review.md
- test-plan.md
- test-results.md
- strategic-compact.md
- final-report.md
- failure-mode-entry.md
- pattern-card.md
```

Artifact càng nhiều thì càng dễ xảy ra các sự cố sau.

```text
- Không biết đâu là bản chính.
- spec-pack vẫn cũ nhưng chỉ report được cập nhật.
- impl-plan và phần triển khai bị lệch nhau.
- review-checklist đang nhìn vào đặc tả cũ.
- Không biết test-results tương ứng với test-plan nào.
- Không biết các finding trong AI review đã được chấp nhận hay bác bỏ.
- Quyết định cuối cùng của con người chỉ còn nằm trong chat.
- AI hiểu nhầm artifact cũ là artifact mới nhất.
- Khi kiểm toán hoặc bảo đảm chất lượng thì không truy vết được căn cứ.
```

Tệp này biến artifact SDD từ trạng thái “tạo xong là kết thúc” thành **một hệ thống bằng chứng có thể vận hành**.

---

## 1. Kết luận

Trong SDD Artifact Governance, các điểm sau là bắt buộc.

```text
1. Artifact phải có status.
2. Phân biệt bản chính và tài liệu tham khảo.
3. Làm rõ Draft / Reviewed / Approved / Superseded / Deprecated.
4. Kết nối Requirement → Spec → Plan → Code → Test → Review → Report.
5. Phân biệt quyết định của con người, phán đoán của AI, bằng chứng và suy đoán.
6. Khi artifact trở nên cũ, phát hiện bằng Freshness Check.
7. Không chỉ cập nhật Report mà bỏ mặc Spec Pack.
8. Ghi Accepted Risk và Test Skip vào Decision Record.
9. Giải quyết mâu thuẫn giữa các artifact bằng Artifact Reconciliation.
10. Có luồng đưa nội dung lên Failure Mode và Project Knowledge.
```

---

## 2. Phân loại Artifact

| Category | Ví dụ | Tính bản chính |
|---|---|---|
| Governance | README, Right-sizing Decision, Context Policy | Cao |
| Requirement | ticket, AC, spec-pack | Cao |
| Source Intelligence | source availability, inventory, maps | Trung bình〜cao |
| Planning | impl-plan, phase plan, impact analysis | Trung bình |
| Review | review-checklist, self-review, codex-review | Trung bình |
| Test | test-plan, test-results, test-data | Cao |
| Security | security gate, threat model, findings | Cao |
| Operation | runbook, rollback, monitoring notes | Cao |
| Learning | failure mode, postmortem, pattern card | Trung bình〜cao |
| AI Output | AI draft, brainstorm | Thấp. Không coi là bản chính trước khi được phê duyệt |

---

## 3. Trạng thái Artifact

| Status | Ý nghĩa | Có được dùng không |
|---|---|---|
| Draft | Đang tạo | Cần thận trọng khi dùng làm căn cứ |
| ReviewReady | Chờ review | Đối tượng review |
| Reviewed | Đã review | Có thể dùng có điều kiện |
| Approved | Đã được con người phê duyệt | Có thể dùng làm bản chính |
| Superseded | Đã được thay bằng phiên bản mới | Không dùng cho phán đoán mới |
| Deprecated | Đã bị loại bỏ | Không cho AI đọc |
| Archived | Lưu lịch sử | Chỉ dùng cho mục đích kiểm toán |
| Blocked | Bị dừng do thiếu thông tin | Không dùng làm căn cứ triển khai |
| AcceptedRisk | Đã chấp nhận rủi ro | Chỉ dùng với thời hạn và điều kiện đi kèm |

---

## 4. Tiêu chuẩn Front Matter

Với artifact Markdown, nên đặt front matter ở đầu file nhiều nhất có thể.

```yaml
---
artifact_id: SDD-ART-0001
title: 
artifact_type: spec-pack
status: Draft
mode: M2
owner: 
reviewer: 
approver: 
created_at: 2026-05-16
updated_at: 2026-05-16
source_commit: 
ticket: 
related_artifacts:
  - 
supersedes:
  - 
superseded_by:
  - 
confidence: C3
contains_sensitive_data: false
requires_human_approval: true
---
```

---

## 5. Cấu trúc thư mục khuyến nghị

```text
docs/sdd/
  README.md
  00_governance/
    right-sizing-decision.md
    context-loading-policy.md
    artifact-inventory.md
    traceability-matrix.md
    decision-ledger.md
  01_investigation/
    source-availability.md
    context-manifest.md
    source-inventory.md
    source-maps/
  02_spec/
    spec-pack.md
    reference-extracts/
  03_plan/
    impact-analysis.md
    impl-plan.md
    phase-plan.md
  04_review/
    review-checklist.md
    self-review.md
    codex-review.md
    human-review.md
  05_test/
    test-plan.md
    test-results.md
    test-data.md
    blackbox-testcases.md
  06_security/
    repo-intake.md
    threat-model.md
    security-review.md
    accepted-risks.md
  07_handoff/
    strategic-compact.md
    session-handoff.md
    resume-pack.md
  08_report/
    final-report.md
    release-readiness.md
  09_learning/
    failure-mode-entry.md
    postmortem.md
    pattern-candidates.md
```

---

## 6. Artifact Inventory

```md
# Artifact Inventory

| ID | Artifact | Type | Status | Owner | Updated | Source Commit | Related Ticket | Freshness | Notes |
|---|---|---|---|---|---|---|---|---|---|
| ART-001 | spec-pack.md | spec | Approved | | | | | Fresh | |
```

Freshness:

```text
Fresh
NeedsReview
Stale
Conflicting
Unknown
```

---

## 7. Traceability Matrix

Trong SDD, cần có khả năng truy vết từ yêu cầu đến test, review và report.

```md
# SDD Traceability Matrix

| Req ID | Acceptance Criteria | Spec Section | Impact Area | Impl Plan | Code Change | Test Case | Review Finding | Security Finding | Final Status |
|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | | | | | | | | | |
```

### 7.1 Đối tượng cần trace

```text
- Requirement
- Acceptance Criteria
- Source Evidence
- Spec Section
- Impact Analysis
- Implementation Plan
- Code Change
- Test Case
- Test Result
- Review Finding
- Security Finding
- Human Decision
- Final Report
```

---

## 8. Decision Record

Các phán đoán của con người, chấp nhận rủi ro, lược bỏ và ngoại lệ phải luôn được lưu lại.

```md
# Decision Record

## Decision ID
DEC-

## Date

## Context

## Decision

## Decider

## Evidence

## Alternatives Considered

## Impact
- Requirement:
- Code:
- Test:
- Security:
- Operation:
- Cost:

## Reversibility
- reversible / difficult / irreversible

## Conditions / Expiry

## Related Artifacts

## Follow-up
```

---

## 9. Evidence Record

```md
# Evidence Record

## Evidence ID
EVD-

## Claim Supported

## Evidence Type
- source
- test
- log
- document
- human decision
- security scan
- external standard

## Location

## Commit / Version / Date

## Reliability
- high / medium / low

## Limitations

## Related Requirement

## Related Artifact
```

---

## 10. Human Approval Record

```md
# Human Approval Record

## Approval ID
APR-

## Artifact

## Approved by

## Approval Scope

## Conditions

## Exclusions

## Date

## Expiry / Re-review Trigger

## Notes
```

---

## 11. Artifact Freshness Check

Artifact sẽ trở nên cũ theo thời gian, thay đổi source hoặc quyết định của con người.

```md
# Artifact Freshness Check

## Target Artifacts
- spec-pack:
- impl-plan:
- review-checklist:
- test-plan:
- security-review:
- final-report:

## Freshness Triggers
- [ ] source changed
- [ ] test changed
- [ ] requirement changed
- [ ] human decision changed
- [ ] security finding changed
- [ ] failure mode added
- [ ] project knowledge updated
- [ ] branch changed
- [ ] external dependency changed

## Findings

| Artifact | Current Status | Issue | Required Update | Owner |
|---|---|---|---|---|

## Verdict
- Fresh / NeedsReview / Stale / Stop
```

---

## 12. Artifact Reconciliation

Khi có mâu thuẫn giữa các artifact, thực hiện Reconciliation.

```md
# Artifact Reconciliation Record

## Conflict ID
ARC-

## Artifacts in Conflict
- A:
- B:

## Conflict Summary

## Source of Truth

## Decision

## Artifacts to Update

## Human Approval Required

## Completion Checklist
- [ ] spec-pack updated
- [ ] impl-plan updated
- [ ] review-checklist updated
- [ ] test-plan updated
- [ ] final-report updated
- [ ] failure-mode considered
- [ ] project knowledge considered
```

---

## 13. Quy tắc quản lý bản chính

```text
- Chỉ có một bản chính.
- Bản nháp phải được ghi rõ là Draft.
- AI output là Draft hoặc Reference cho đến khi được phê duyệt.
- Artifact Superseded không dùng cho phán đoán mới.
- Deprecated phải bị loại khỏi AI context ở 31.
- Khi thay đổi đặc tả, cập nhật spec-pack trước.
- Khi thay đổi triển khai, kiểm tra chênh lệch với impl-plan.
- Khi thêm test, cập nhật test-plan và traceability.
- Việc chấp nhận/bác bỏ review finding không chỉ ghi vào final-report mà phải lưu vào review record.
```

---

## 14. Cách xử lý AI Output

AI output hữu ích nhưng không phải bản chính.

```text
AI brainstorm:
- Xử lý như ý tưởng.
- Cần căn cứ để nâng lên spec.

AI generated spec:
- Xử lý như Draft.
- Chuyển thành Approved sau khi con người review.

AI review finding:
- Xử lý như finding.
- Ghi lại phán định false positive.

AI test proposal:
- Xử lý như ứng viên test-plan.
- Không coi là đã xác minh nếu chưa có kết quả thực thi.
```

---

## 15. Tư duy về Provenance

Artifact cần lưu lại các nội dung sau.

```text
Entity:
- Artifact, source, kết quả test, kết quả review

Activity:
- Điều tra, triển khai, review, test, phê duyệt, cập nhật

Agent:
- Con người, AI, CI, tool

Relationship:
- used
- generated
- derivedFrom
- attributedTo
- wasRevisionOf
```

Đây là cách đơn giản hóa tư duy W3C PROV cho SDD.

---

## 16. Audit Package

Khi cần kiểm toán, bảo đảm chất lượng hoặc giải thích với khách hàng, hãy gom các nội dung sau.

```text
audit-package/
  README.md
  right-sizing-decision.md
  context-manifest.md
  spec-pack.md
  traceability-matrix.md
  decision-ledger.md
  review-summary.md
  test-summary.md
  security-summary.md
  accepted-risks.md
  final-report.md
  sbom/
  ci-evidence/
```

---

## 17. Release Readiness Record

```md
# Release Readiness Record

## Scope

## Traceability
- [ ] Requirements traced
- [ ] Tests traced
- [ ] Reviews traced
- [ ] Security findings closed or accepted

## Quality
- [ ] Build passed
- [ ] Tests passed
- [ ] Known failures documented
- [ ] Performance impact assessed
- [ ] Rollback plan prepared

## Security
- [ ] secrets scan
- [ ] SCA
- [ ] SAST
- [ ] SBOM
- [ ] accepted risks approved

## Operation
- [ ] monitoring
- [ ] logging
- [ ] alert
- [ ] runbook
- [ ] support handoff

## Approval
- Approver:
- Date:
- Conditions:
```

---

## 18. Prompt chuyên dụng cho 33

### 18.1 Tạo Artifact Inventory

```text
Bạn là Artifact Governor của SDD Ver.04.
Hãy đọc danh sách artifact dưới đây và tạo Artifact Inventory.

# Input
- Danh sách file:
- Ticket:
- mode:
- branch/commit:
- Trạng thái công việc:

# Output
Hãy xuất theo định dạng Artifact Inventory.
Với từng artifact, hãy phán định type, status, owner, freshness, artifact liên quan và nhu cầu cập nhật.
```

### 18.2 Tạo Traceability Matrix

```text
Hãy đọc spec-pack, impl-plan, diff, test-plan và kết quả review dưới đây, sau đó tạo Traceability Matrix từ Requirement đến Final Status.

# Input
- spec-pack:
- impl-plan:
- git diff:
- test-plan:
- test-results:
- review findings:
- security findings:
- final report:

# Output
Hãy xuất theo định dạng SDD Traceability Matrix.
Hãy nêu rõ các yêu cầu chưa được kết nối, test chưa tương ứng, review chưa xử lý và thiếu bằng chứng.
```

### 18.3 Freshness Check

```text
Hãy kiểm tra các artifact SDD dưới đây có khớp với source/diff/decision/test result hiện tại hay không.

# Input
- Artifact Inventory:
- Context Manifest:
- Decision Ledger:
- current diff:
- current test status:
- updated spec / requirement:

# Output
1. Verdict
2. Stale artifacts
3. Conflicting artifacts
4. Required updates
5. Stop conditions
6. Final recommendation
```

### 18.4 Review tính nhất quán của Report

```text
Hãy kiểm tra Final Report có mâu thuẫn với spec-pack, impl-plan, review, test-results và decision record hay không.

# Input
- final-report:
- spec-pack:
- impl-plan:
- review records:
- test-results:
- decision records:

# Output
- Mâu thuẫn
- Thiếu sót
- Tuyên bố quá mức
- Thiếu ghi nhận accepted risk
- Che giấu test chưa thực hiện
- Đề xuất sửa
```

---

## 19. Metrics

| Metric | Ý nghĩa |
|---|---|
| Traceability Coverage | Tỷ lệ yêu cầu được kết nối tới triển khai, test và review |
| Artifact Freshness Pass Rate | Tỷ lệ artifact vượt qua kiểm tra độ mới |
| Orphan Artifact Count | Số artifact không rõ liên kết |
| Decision Capture Rate | Tỷ lệ quyết định quan trọng được ghi lại |
| Report Consistency Rate | Tỷ lệ nhất quán giữa Final Report và artifact khác |
| Review Finding Resolution Rate | Tỷ lệ ghi nhận trạng thái chấp nhận, xử lý, hoãn của finding |
| Accepted Risk Expiry Compliance | Tỷ lệ tái xác nhận rủi ro đã chấp nhận có thời hạn |
| Audit Package Completion | Tỷ lệ hoàn thiện audit package |

---

## 20. Failure Mode tiêu biểu

```text
ART-001 spec-pack vẫn cũ nhưng vẫn được dùng để triển khai
ART-002 chỉ final-report được cập nhật, test-plan vẫn cũ
ART-003 không rõ review finding đã được chấp nhận hay bác bỏ
ART-004 accepted risk không có trong decision record
ART-005 AI draft bị xem như bản chính
ART-006 AI đọc artifact đã Superseded
ART-007 không có traceability matrix nên không phát hiện yêu cầu chưa được kiểm chứng
ART-008 không rõ test-results là kết quả của test plan nào
ART-009 human approval chỉ còn trong chat
ART-010 khi tạo audit package không truy được căn cứ
```

---

## 21. Definition of Done

Trạng thái hoàn tất của vận hành 33 như sau.

```text
- Có Artifact Inventory.
- Mỗi artifact có status.
- Phân biệt Draft / Approved / Superseded / Deprecated.
- Có Traceability Matrix.
- Có Decision Record.
- Có Evidence Record.
- Đã thực hiện Freshness Check.
- Final Report nhất quán với các artifact khác.
- AI output không bị biến thành bản chính khi chưa được phê duyệt.
- Artifact cũ bị loại khỏi context ở 31.
- Có đường dẫn để đưa nội dung học hỏi/tri thức hóa sang 29/34.
```

---

---

## 22. Kết nối với CI/CD

33 không chỉ là quản lý tài liệu.  
Khi kết nối với CI/CD, có thể phát hiện bằng máy các trường hợp quên cập nhật artifact.

### 22.1 Những điều muốn phát hiện bằng CI

```text
- Code thay đổi nhưng spec-pack không được cập nhật.
- Có migration nhưng không có DB review.
- API contract thay đổi nhưng không có contract test.
- File nhạy cảm về bảo mật thay đổi nhưng không có security review.
- review finding vẫn open nhưng release readiness lại Approved.
- Không có test skip reason.
- Accepted risk không có người phê duyệt.
```

### 22.2 Ví dụ Artifact Gate

```yaml
artifact_gates:
  require_traceability_matrix: true
  require_test_results_if_code_changed: true
  require_security_review_for:
    - auth
    - permission
    - crypto
    - ci
    - secrets
    - infra
  require_contract_test_for_api_change: true
  block_deprecated_artifacts_in_context: true
```

---

## 23. Kết nối với PR template

```md
# PR Checklist

## SDD Mode
- [ ] M1
- [ ] M2
- [ ] M3
- [ ] M4/M5

## Artifacts
- [ ] spec-pack updated
- [ ] impl-plan updated
- [ ] review-checklist updated
- [ ] test-plan updated
- [ ] test-results attached
- [ ] traceability matrix updated
- [ ] decision record updated if needed
- [ ] security review attached if needed
- [ ] failure mode / project knowledge considered

## Risks
- [ ] accepted risks documented
- [ ] rollback plan available
- [ ] monitoring/logging considered
```

---

## 24. Kết nối với SBOM / Attestation

Khi có dependency, artifact sinh ra hoặc rủi ro chuỗi cung ứng, Artifact Governance sẽ tham chiếu SBOM và attestation.

```text
- SBOM file path
- generated date
- tool
- package manager
- vulnerability scan result
- license risk
- VEX status if available
- build provenance
- release artifact hash
```

Template:

```md
# Supply Chain Evidence

## SBOM
- format:
- path:
- generated by:
- generated at:

## Dependency Scan
- tool:
- result:
- critical:
- high:

## Build Provenance
- CI run:
- commit:
- artifact:
- hash:
- signer:

## Decision
- release allowed:
- conditions:
```

---

## 25. Artifact Naming Convention

```text
YYYYMMDD_ticketid_artifact-type_short-title.md
```

Ví dụ:

```text
20260516_API-123_spec-pack_order-cancel.md
20260516_API-123_traceability_order-cancel.md
20260516_API-123_codex-review_order-cancel.md
```

Tuy nhiên, nếu dùng thư mục theo ticket thì cũng có thể dùng tên cố định.

```text
docs/sdd/API-123/spec-pack.md
docs/sdd/API-123/test-results.md
```

---

## 26. Artifact Retention Policy

```text
Draft:
- Giữ trong khi đang làm việc.
- Sau khi Approved, đưa Draft không cần thiết vào archive.

Approved:
- Giữ lại cả sau khi hoàn tất dự án.

Superseded:
- Giữ lại kèm link tới phiên bản mới.

Deprecated:
- Loại khỏi AI context.
- Chỉ giữ cho mục đích kiểm toán.

Sensitive:
- Làm rõ thời hạn lưu giữ và kiểm soát truy cập.
```

---

## 27. Chia nhỏ Artifact cho dự án quy mô lớn

Với dự án quy mô lớn, không nên gom tất cả vào một spec-pack khổng lồ.

```text
spec/
  overview.md
  requirements.md
  api.md
  db.md
  fe.md
  security.md
  operation.md
  test-strategy.md
```

Tuy nhiên, điểm vào của bản chính chỉ nên có một.

```text
spec/index.md
```

index cần chứa các nội dung sau.

```text
- status của từng spec
- owner
- updated date
- related requirement
- traceability link
```

---

## 27-A. Quản lý Artifact của Advanced Options nhóm 40

Khi dùng nhóm 40, ngoài artifact SDD thông thường, các bằng chứng riêng của Advanced Option cũng phải được quản lý trong 33.

| Option | Artifact bổ sung | Lưu ý về quản lý bản chính |
|---|---|---|
| 40 | advanced-option-selection-record.md | Cũng ghi lại Option không áp dụng và lý do |
| 41 | repository-intelligence.md / impact-slice.md | Tách riêng source chưa đọc và suy đoán |
| 42 | orchestrator-plan.md / agent-output-record.md | Không để output của Agent chỉ ở dạng tự do, cần cấu trúc hóa |
| 43 | tool-result-record.md / consensus-record.md | Tách ý kiến AI và Tool evidence |
| 44 | token-cost-audit.md | Ghi cache hit, tỷ lệ nén và cost |
| 45 | ai-permission-matrix.md / mcp-security-review.md | Lưu quyền hạn, phê duyệt và audit log |
| 46 | rag-evidence-pack.md / code-map.md | Lưu căn cứ truy xuất, index version và điều kiện cache invalidation |
| 47 | pr-qa-gate-record.md | Lưu phán định PR, lý do block và human override |
| 48 | worktree-inventory.md / merge-integration-record.md | Lưu phương án được chọn, không chọn và diff tích hợp |
| 49 | evaluation-run-record.md / dashboard-metrics.md | Tách định nghĩa KPI và kết quả đo |

Artifact của nhóm 40 không phải ghi chú trung gian tiện lợi, mà là căn cứ ra quyết định.  
Đặc biệt, 43, 45, 47, 48, 49 liên quan trực tiếp tới kiểm toán, tái hiện và cải tiến, nên không được bỏ mặc ở trạng thái `Draft`.

## 28. Artifact Quality Checklist

```md
# Artifact Quality Checklist

- [ ] title rõ ràng
- [ ] có status
- [ ] có owner
- [ ] có source commit
- [ ] có related artifacts
- [ ] assumptions được tách riêng
- [ ] có human decisions
- [ ] nếu có accepted risks thì có phê duyệt
- [ ] có liên kết với test
- [ ] không mâu thuẫn với final report
- [ ] không tham chiếu artifact đã deprecated
```

## Tài liệu, tiêu chuẩn công khai đã tham khảo

Pack này tái cấu trúc các tư duy từ những tiêu chuẩn và tài liệu công khai dưới đây cho phù hợp với ngữ cảnh SDD.  
Các tiêu chuẩn bên ngoài không phải đối tượng để “copy-paste nguyên văn”, mà cần điều chỉnh mức áp dụng theo quy định nội bộ, đặc thù dự án, yêu cầu khách hàng và quy định pháp lý.

| Lĩnh vực | Nguồn tham khảo | Cách dùng trong SDD |
|---|---|---|
| Vận hành AI Agent | Everything Claude Code | Đưa các tư duy về skills / rules / hooks / MCP / memory optimization / continuous learning / security scanning / research-first development vào một cách chọn lọc và an toàn. |
| Secure SDLC | NIST SP 800-218 SSDF | Dùng làm nền tảng cho Phase 0-A, thiết kế an toàn, phòng ngừa tái phát lỗ hổng, bằng chứng và CI security. |
| AI Risk | NIST AI RMF | Xử lý rủi ro của phát triển có AI hỗ trợ theo vòng lặp Govern / Map / Measure / Manage. |
| LLM Security | OWASP Top 10 for LLM Applications 2025 | Dùng cho đối sách với Prompt Injection, Sensitive Information Disclosure, Excessive Agency khi đọc tài liệu ngoài, log, Issue, Web page, v.v. |
| Application Security | OWASP ASVS | Là đường dẫn phụ trợ cho yêu cầu bảo mật Web/API, góc nhìn review và góc nhìn test. |
| Supply Chain | SLSA / OpenSSF | Là đường dẫn phụ trợ để xem xét build, dependency, artifact sinh ra, CI/CD, bằng chứng, chữ ký và chống chỉnh sửa. |
| SBOM | CycloneDX / SPDX | Dùng để biểu diễn dependency, component, AI/ML BOM, rủi ro lỗ hổng, license và supply chain. |
| Provenance | W3C PROV | Dùng như tư duy để xử lý nguồn gốc, người tạo, căn cứ, quan hệ phái sinh và đánh giá độ tin cậy của artifact. |
| Delivery Metrics | DORA | Là chỉ số phụ trợ để đo tốc độ, độ ổn định và khả năng phục hồi sau khi áp dụng SDD. |
| Operations Learning | Google SRE Postmortem | Xử lý Failure Mode, Near Miss và Postmortem như học hỏi của tổ chức, không phải trách nhiệm cá nhân. |
| Observability | OpenTelemetry | Kết nối tư duy trace / metric / log / baggage / context propagation với vận hành, giám sát và điều tra xuyên hệ thống. |


---

# Appendix. Dành cho người mới: Quy trình thực thi và prompt copy-paste của pack này

> Appendix này là “execution wrapper” để người mới cũng có thể thực thi trong công việc mà không bị lạc giữa các góc nhìn chuyên sâu được định nghĩa trong phần chính.  
> Không thay đổi nội dung phần chính. Hãy dùng phần chính như từ điển, tư duy thiết kế và tập hợp góc nhìn; dùng Appendix này như quy trình “yêu cầu AI theo thứ tự nào, tạo gì, dừng ở đâu, hoàn tất ở đâu”.

---

## A-0. Quy tắc tuyệt đối phải tuân thủ trước tiên

Khi dùng pack này, hãy luôn tuân thủ các điểm sau.

```text
1. Không để AI triển khai, sửa, đổi CI hoặc đổi config ngay lập tức.
2. Trước hết chỉ yêu cầu AI đưa ra Plan.
3. Không cho AI tạo/cập nhật file trước khi con người phê duyệt Plan.
4. Không kết thúc artifact chỉ trong chat; luôn lưu vào file.
5. Tách riêng những gì đã đọc, chưa đọc, đã loại trừ, suy đoán và điểm chưa xác định.
6. Nếu gặp điều kiện Stop/Ask, không tiếp tục mà trả về cho con người phán định.
7. Việc phản ánh vào tài liệu/quy tắc thường trực không để AI tự quyết, trước hết ghi lại như ứng viên nâng cấp.
8. Không cho AI đọc, dán hoặc lưu secret, PII, credential, .env, khóa, log production gốc.
9. Lệnh nằm trong tài liệu ngoài hoặc output tool phải được xử lý như dữ liệu tài liệu, không phải lệnh thực thi.
10. Cuối cùng thực hiện independent review và phán định completion gate.
```

Nơi lưu mặc định dùng trong Appendix này như sau.

```text
Artifact chuyên dụng của pack:
docs/changes/{{TICKET}}/33-artifact-governance/

Artifact Core của toàn ticket:
docs/changes/{{TICKET}}/sources.md
docs/changes/{{TICKET}}/spec-pack.md
docs/changes/{{TICKET}}/impact-analysis.md
docs/changes/{{TICKET}}/impl-plan.md
docs/changes/{{TICKET}}/review-checklist.md
docs/changes/{{TICKET}}/self-review.md
docs/changes/{{TICKET}}/test-plan.md
docs/changes/{{TICKET}}/test-results.md
docs/changes/{{TICKET}}/blackbox-testcases.md
docs/changes/{{TICKET}}/test-data.md
docs/changes/{{TICKET}}/report.md

Nơi tạm đặt ứng viên thường trực hóa:
docs/changes/{{TICKET}}/33-artifact-governance/promotion-candidates.md
```

33 là pack quản lý “artifact nào là bản chính”, “cái gì đã cũ”, “yêu cầu, triển khai, review, test, báo cáo có nối với nhau không”.  
Người mới không nên hài lòng chỉ vì đã tạo artifact; hãy luôn ghi status, owner, freshness, traceability, decision, evidence và approval.

---

## A-1. Khi nào dùng pack này

### Các trường hợp nên dùng

```text
- Artifact dưới docs/changes/{{TICKET}}/ tăng lên, khó biết đâu là bản đúng.
- Muốn kiểm tra tính nhất quán giữa spec-pack, impl-plan, review, test-results và report.
- Muốn phân biệt Draft / Approved / Superseded / Deprecated của artifact.
- Muốn lưu Traceability từ requirement đến triển khai, review, test và báo cáo cuối.
- Muốn lưu human approval, Accepted Risk, Decision Record dưới dạng file.
- Muốn chuyển thông tin cho 31 để tránh đọc nhầm artifact cũ hoặc AI draft.
- Muốn sắp xếp bằng chứng trước release, trước PR, trước audit hoặc trước handoff.
- Artifact bổ sung tăng lên do dùng Advanced Options nhóm 40.
```

### Trường hợp có thể làm nhẹ

```text
- Thay đổi nhỏ M1, artifact chỉ giới hạn ở spec-pack và report.
- Đã có Artifact Inventory và Traceability Matrix mới nhất.
- Không có thay đổi code, chỉ hoàn tất bằng tham chiếu tới artifact hiện có.
```

Dù làm nhẹ, tối thiểu vẫn phải lưu các mục sau.

```text
- Artifact Inventory
- Artifact Status
- Freshness Check
- Kiểm tra Traceability tối thiểu
- Có hay không Decision / Approval
```

### Trường hợp không dùng, hoặc cần quay lại pack khác trước

```text
- Chưa sắp xếp cần cho AI đọc context nào, cần 31 trước.
- Không rõ bản chính/độ mới của artifact, cần 32 trước để cố định trạng thái dài hạn.
- Chưa tạo bản chính của đặc tả, cần Spec Pack trước.
- Mục tiêu chính là Failure Mode hoặc Knowledge hóa, cần 29/34 trước.
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 33
{{PACK_NAME}}: Artifact Governance and Traceability Pack
{{PACK_SLUG}}: artifact-governance
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{REVIEWER}}:
{{RELEASE_OR_PR_TARGET}}:
{{CURRENT_BRANCH_COMMIT}}:
{{ARTIFACT_SCOPE}}:
```

Ví dụ điền:

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{RISK_LEVEL}}: Medium
{{SDD_MODE}}: M3
{{TIMEBOX}}: Đến khi tạo xong Inventory và Traceability Matrix
{{RELEASE_OR_PR_TARGET}}: Review trước khi tạo PR
{{CURRENT_BRANCH_COMMIT}}: Nếu chưa xác nhận thì ghi 未確認/chưa xác nhận
{{ARTIFACT_SCOPE}}: Toàn bộ artifact dưới docs/changes/ABC-123 + review liên quan + kết quả test
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
@docs/changes/{{TICKET}}/self-review.md
@docs/changes/{{TICKET}}/test-plan.md
@docs/changes/{{TICKET}}/test-results.md
@docs/changes/{{TICKET}}/blackbox-testcases.md
@docs/changes/{{TICKET}}/test-data.md
@docs/changes/{{TICKET}}/report.md
@docs/architecture/
@docs/standards/
@.claude/CLAUDE.md
@.claude/rules/
```

### Input đặc biệt cần đọc trong pack này

```text
@docs/changes/{{TICKET}}/31-context-loading/context-manifest.md
@docs/changes/{{TICKET}}/32-strategic-compact/decision-ledger.md
@docs/changes/{{TICKET}}/32-strategic-compact/changed-files-summary.md
@docs/changes/{{TICKET}}/25-security-gate-ci/security-review-findings.md
@docs/changes/{{TICKET}}/24-review-testcode/independent-review.md
@docs/changes/{{TICKET}}/29-failure-mode-learning/failure-mode-candidates.md
git diff summary
PR review comments
CI/test kết quả
Ghi nhận phê duyệt của con người
Ghi nhận Accepted Risk
```

### Lưu ý trước khi đọc

```text
- Artifact Deprecated / Superseded không được cho đọc như bản chính.
- AI draft không phải bản chính cho đến khi Approved.
- Phê duyệt chỉ nằm trên chat là bằng chứng yếu cho đến khi được chuyển vào Human Approval Record.
- Không chỉ đọc report.md để quyết định hoàn tất.
- Không trộn bằng chứng chứa secret hoặc PII vào audit package.
```

---

## A-4. Artifact cần tạo/cập nhật

### Thư mục chuyên dụng của pack

```text
docs/changes/{{TICKET}}/33-artifact-governance/
```

### Artifact tối thiểu cần tạo

```text
docs/changes/{{TICKET}}/33-artifact-governance/artifact-inventory.md
docs/changes/{{TICKET}}/33-artifact-governance/traceability-matrix.md
docs/changes/{{TICKET}}/33-artifact-governance/freshness-check.md
docs/changes/{{TICKET}}/33-artifact-governance/artifact-quality-review.md
docs/changes/{{TICKET}}/33-artifact-governance/31-context-exclusion-update.md
```

### Artifact tạo khi cần

```text
docs/changes/{{TICKET}}/33-artifact-governance/decision-records.md
docs/changes/{{TICKET}}/33-artifact-governance/evidence-records.md
docs/changes/{{TICKET}}/33-artifact-governance/human-approval-records.md
docs/changes/{{TICKET}}/33-artifact-governance/artifact-reconciliation-record.md
docs/changes/{{TICKET}}/33-artifact-governance/release-readiness-record.md
docs/changes/{{TICKET}}/33-artifact-governance/audit-package.md
docs/changes/{{TICKET}}/33-artifact-governance/supply-chain-evidence.md
docs/changes/{{TICKET}}/33-artifact-governance/promotion-candidates.md
```

---

## A-5. Quy trình thực thi cho người mới

### Step 1. Kiểm kê docs/changes/{{TICKET}}/

Trước hết, liệt kê toàn bộ artifact dưới ticket. Dù artifact ít, việc tạo Inventory sẽ giúp thấy “đang có gì” và “đang thiếu gì”.

### Step 2. Gán Artifact Status

Gán cho từng artifact một trong các trạng thái sau.

```text
Draft
Review Ready
Approved
Superseded
Deprecated
Rejected
External Reference
Sensitive / Restricted
```

### Step 3. Quyết định bản chính

Làm rõ đâu là bản chính cho spec, implementation plan, review, test và report. Không coi AI draft hoặc phiên bản cũ là bản chính.

### Step 4. Tạo Traceability Matrix

Tối thiểu cần nối các mục sau.

```text
Requirement / AC
→ Design / Impl Plan
→ Changed File / Module
→ Review Finding
→ Test Case / Test Result
→ Decision / Accepted Risk
→ Final Report Status
```

### Step 5. Thực hiện Freshness Check

Kiểm tra artifact có khớp với branch, commit, diff, test status, kết quả review và phán đoán của con người hay không.

### Step 6. Nếu có mâu thuẫn thì Reconciliation

Nếu spec, impl-plan, test-results và report mâu thuẫn nhau, không tự ý chọn một bên là đúng; hãy ghi vào `artifact-reconciliation-record.md` và trả về cho con người phán định.

### Step 7. Trả Context Exclusion về 31

Artifact Deprecated, Superseded, Rejected, Sensitive phải được đưa về 31 Context Manifest dưới dạng loại trừ hoặc Ask Before Include.

### Step 8. Phán định Release Readiness

Trước PR, trước release hoặc trước audit, dùng Release Readiness Record để kiểm tra bằng chứng đã đủ hay chưa.

---

## A-6. Dùng để copy-paste: Prompt bắt đầu chỉ lập Plan

```text
Bạn là Artifact Governor của SDD Ver.04.
Từ giờ sẽ áp dụng 33_Artifact Governance and Traceability Pack cho {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không triển khai, sửa, chỉnh file hoặc đổi CI ngay lập tức.
- Trước hết chỉ trình bày Plan.
- Không tạo/cập nhật file trước khi tôi phê duyệt Plan.
- Không coi AI draft là artifact Approved.
- Không coi phê duyệt chỉ nằm trên chat là bằng chứng đầy đủ.
- Luôn phân biệt Draft / Approved / Superseded / Deprecated / Rejected.
- Không phán định hoàn tất chỉ bằng report.md; hãy kiểm tra tính nhất quán với spec, impl-plan, review, test-results và decision.
- Không trộn secret, PII, credential, log production gốc vào bằng chứng kiểm toán.
- Hãy đề xuất lưu artifact dưới docs/changes/{{TICKET}}/33-artifact-governance/.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Release/PR Target: {{RELEASE_OR_PR_TARGET}}
- Current Branch/Commit: {{CURRENT_BRANCH_COMMIT}}
- Artifact Scope: {{ARTIFACT_SCOPE}}

【Plan bắt buộc phải gồm】
1. Có cần áp dụng 33 hay không
2. Phạm vi artifact cần kiểm kê
3. Phương châm tạo Artifact Inventory
4. Quy tắc gán Status
5. Phương châm tạo Traceability Matrix
6. Có cần ghi Decision / Evidence / Human Approval hay không
7. Góc nhìn Freshness Check
8. Ứng viên mâu thuẫn cần Reconciliation
9. Ứng viên artifact cũ cần trả về 31 Context Exclusion
10. Có cần phán định Release Readiness hay không
11. Artifact sẽ tạo/cập nhật và nơi lưu
12. Điều kiện Stop/Ask

Trước hết chỉ trình bày Plan. Chưa chỉnh sửa file.
```

---

## A-7. Checklist kiểm tra Plan

```text
- [ ] Plan không đi theo hướng chỉnh sửa artifact ngay lập tức.
- [ ] Phạm vi kiểm kê rõ ràng.
- [ ] Cách gán Artifact Status rõ ràng.
- [ ] Có phân biệt AI draft và Approved.
- [ ] Đối tượng của Traceability Matrix rõ ràng.
- [ ] Có cách xử lý Decision / Evidence / Approval.
- [ ] Có Freshness Check.
- [ ] Có luồng loại trừ artifact cũ ở 31.
- [ ] Nêu rõ có cần Release Readiness hay không.
- [ ] Nêu rõ điều kiện Stop/Ask.
```

---

## A-8. Dùng để copy-paste: Prompt phê duyệt Plan

```text
Tôi phê duyệt Plan.
Hãy tạo/cập nhật artifact của 33_Artifact Governance and Traceability Pack theo đúng thủ tục đã đề xuất.

【Quy tắc thực thi】
- Trước hết tạo artifact-inventory.md.
- Với mỗi Artifact, gán type / status / owner / freshness / related artifacts / update needed.
- Trong traceability-matrix.md, hãy nối từ Requirement / AC đến Final Report Status.
- Nếu có quyết định của con người, Accepted Risk hoặc quyết định kỹ thuật quan trọng, hãy ghi vào decision-records.md.
- Những claim cần căn cứ phải được ghi vào evidence-records.md.
- Nội dung cần human approval phải được tách vào human-approval-records.md.
- Trong freshness-check.md, hãy kiểm tra tính nhất quán giữa branch / diff / test / review / decision hiện tại và artifact.
- Nếu có mâu thuẫn, hãy tách vào artifact-reconciliation-record.md và không tự ý giải quyết.
- Artifact Deprecated / Superseded / Sensitive phải được ghi vào 31-context-exclusion-update.md.
- Sau khi làm xong, hãy tự phán định completion gate.
```

---

## A-9. Dùng để copy-paste: Prompt review artifact và phán định hoàn tất

```text
Bạn là independent reviewer của SDD Ver.04.
Hãy review các artifact của 33_Artifact Governance and Traceability Pack dưới đây và phán định có thể hoàn tất pack này hay chưa.

【Đối tượng review】
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-inventory.md
@docs/changes/{{TICKET}}/33-artifact-governance/traceability-matrix.md
@docs/changes/{{TICKET}}/33-artifact-governance/freshness-check.md
@docs/changes/{{TICKET}}/33-artifact-governance/decision-records.md
@docs/changes/{{TICKET}}/33-artifact-governance/evidence-records.md
@docs/changes/{{TICKET}}/33-artifact-governance/human-approval-records.md
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-reconciliation-record.md
@docs/changes/{{TICKET}}/33-artifact-governance/release-readiness-record.md
@docs/changes/{{TICKET}}/33-artifact-governance/artifact-quality-review.md
@docs/changes/{{TICKET}}/33-artifact-governance/31-context-exclusion-update.md

File không tồn tại thì xử lý là “không tồn tại” và phán định mức cần thiết.

【Góc nhìn review】
1. Artifact Inventory có đủ không
2. Có phân biệt Draft / Approved / Superseded / Deprecated / Rejected không
3. AI draft có bị biến thành bản chính khi chưa phê duyệt không
4. Traceability Matrix có truy được từ AC đến implementation, review, test, report không
5. Decision / Evidence / Human Approval có được lưu thành file không
6. Freshness Check có nhất quán với diff, test, review, decision hiện tại không
7. report.md có tuyên bố quá mức không
8. Có che giấu test chưa thực hiện, review chưa xử lý, accepted risk chưa phê duyệt không
9. Có luồng loại trừ artifact Deprecated / Superseded ở 31 không
10. Có đủ bằng chứng để phán định Release Readiness không

【Định dạng output】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Orphan artifacts
- Stale artifacts
- Traceability gaps
- Missing decisions / approvals
- Missing evidence
- Required human decisions
- Required artifact updates
- Final completion gate checklist
- Next action
```

---

## A-10. Dùng để copy-paste: Prompt trả về sửa

```text
Hãy sửa artifact của 33_Artifact Governance and Traceability Pack dựa trên các chỉ摘 review dưới đây.

【Quy tắc sửa】
- Trước khi bắt tay, hãy diễn giải ý định của chỉ摘 bằng 1 dòng.
- Liệt kê trước các artifact bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Không chuyển AI draft thành Approved.
- Không tự ý xóa artifact cũ; hãy xử lý là Superseded / Deprecated và Reconciliation nếu cần.
- Nội dung cần phê duyệt phải được tách vào Human Approval Record.
- Với lỗ hổng Traceability, hãy nêu rõ thiếu ở đâu: yêu cầu, triển khai, review, test hay báo cáo.
- Sau khi sửa, hãy ghi kết quả xử lý vào artifact-quality-review.md.

【Review findings】
Dán chỉ摘 vào đây
```

---

## A-11. Điều kiện Stop/Ask

```text
- spec-pack không tồn tại hoặc không rõ bản chính.
- Trong Artifact Inventory, Approved và Superseded mâu thuẫn nhau.
- final report mâu thuẫn với artifact khác.
- Test chưa thực hiện nhưng bị xử lý như đã hoàn tất.
- Không rõ review finding đã được chấp nhận/bác bỏ/xử lý ra sao.
- Có Accepted Risk nhưng không có approver,期限/điều kiện.
- Human approval chỉ còn trên chat.
- AI draft được xử lý như bản chính.
- Đang định cho 31 đọc artifact Deprecated / Superseded.
- Artifact chứa secret, PII, log production gốc.
- Thiếu bằng chứng cần thiết để phán định release.
- AC quan trọng bị cô lập trong Traceability Matrix.
```

---

## A-12. Completion Gate

```text
- [ ] artifact-inventory.md đã được tạo.
- [ ] Mỗi artifact đều có status.
- [ ] Draft / Approved / Superseded / Deprecated / Rejected được phân biệt.
- [ ] Có Traceability Matrix.
- [ ] Có thể truy từ Requirement / AC đến triển khai, review, test và report.
- [ ] Decision Record đã được tạo cho các quyết định cần thiết.
- [ ] Evidence Record đã được tạo cho các claim cần căn cứ.
- [ ] Human Approval Record đã được tạo cho các phê duyệt cần thiết.
- [ ] Đã thực hiện Freshness Check.
- [ ] Final Report nhất quán với các artifact khác.
- [ ] Artifact cũ được loại khỏi Context của 31 hoặc được xử lý dạng Ask.
- [ ] Có thể phán định Release Readiness, hoặc có lý do chưa phán định.
- [ ] Đã review và không còn Blocker.
```

---

## A-13. Điểm tiếp theo cần đi tới

```text
- Loại artifact cũ khỏi Context → quay lại 31 Context Loading
- Đồng bộ trạng thái của công việc dài hạn → đi tới 32 Strategic Compact
- Có Failure Mode hoặc chỉ摘 tái phát → trả về 29 Failure Mode
- Có rule/pattern có thể tái sử dụng → đưa ứng viên nâng cấp tới 34 Project Knowledge
- Release Readiness PASS → đi tới PR / Phase 8 report / phán định release
- Traceability thiếu → quay lại spec-pack / impl-plan / test-plan / review-checklist
- Có artifact của Advanced Option → quay lại pack tương ứng trong nhóm 40 để bổ sung bằng chứng
```

---

## A-14. Lỗi người mới hay mắc và cách phòng tránh

| Lỗi | Nguy hiểm ở đâu | Cách phòng tránh |
|---|---|---|
| Tạo artifact xong là kết thúc | Không phát hiện cũ/chưa phê duyệt/mâu thuẫn | Gán Inventory và Status |
| Chỉ đọc report.md | Bỏ sót tuyên bố quá mức hoặc test chưa thực hiện | Đối chiếu với spec/impl/review/test/decision |
| Biến AI draft thành bản chính | Thông tin sai chưa phê duyệt bị lan rộng | Làm rõ điều kiện Approved |
| Để human approval trong chat | Sau này không truy vết được | Ghi vào Human Approval Record |
| Xóa artifact cũ | Mất audit/lịch sử | Quản lý bằng Superseded / Deprecated |
| Không tạo Traceability | Không phát hiện yêu cầu chưa kiểm chứng | Matrix hóa theo từng AC |
| Trộn bằng chứng Sensitive | Gây rò rỉ thông tin | Đánh dấu Restricted, loại trừ, masking |

---

## A-15. Lộ trình ngắn nhất

```text
1. Dán prompt bắt đầu.
2. Kiểm kê dưới docs/changes/{{TICKET}}/.
3. Tạo artifact-inventory.md.
4. Gán status và freshness.
5. Tạo traceability-matrix.md.
6. Đối chiếu hiện trạng bằng freshness-check.md.
7. Trả artifact cũ/nguy hiểm về 31.
8. Phán định hoàn tất bằng artifact-quality-review.md.
```
