**Mục lục**
- [49_SDD_Evaluation-Observability-and-Continuous-Optimization-Option_Ver.04_Vietnamese](#49_sdd_evaluation-observability-and-continuous-optimization-option_ver04_vietnamese)
  - [0. Vai trò của tài liệu này](#0-vai-trò-của-tài-liệu-này)
  - [1. Kết luận quan trọng nhất của 49](#1-kết-luận-quan-trọng-nhất-của-49)
  - [2. Kết nối với 21〜48](#2-kết-nối-với-2148)
  - [3. Đối tượng quan sát trong 49](#3-đối-tượng-quan-sát-trong-49)
  - [4. Kiến trúc Observability cho phát triển AI](#4-kiến-trúc-observability-cho-phát-triển-ai)
  - [5. Thiết kế Trace](#5-thiết-kế-trace)
  - [6. Phân loại Metrics](#6-phân-loại-metrics)
  - [7. Quality Metrics](#7-quality-metrics)
  - [8. Safety / Security Metrics](#8-safety--security-metrics)
  - [9. Efficiency / Delivery Metrics](#9-efficiency--delivery-metrics)
  - [10. Cost / Token Metrics](#10-cost--token-metrics)
  - [11. Agent / Model Metrics](#11-agent--model-metrics)
  - [12. Context / RAG Metrics](#12-context--rag-metrics)
  - [13. Developer Experience Metrics](#13-developer-experience-metrics)
  - [14. Thiết kế Evaluation Dataset](#14-thiết-kế-evaluation-dataset)
  - [15. Evaluation Run Record](#15-evaluation-run-record)
  - [16. Các loại Evaluation](#16-các-loại-evaluation)
  - [17. Ví dụ về tiêu chuẩn đánh giá](#17-ví-dụ-về-tiêu-chuẩn-đánh-giá)
  - [18. Thiết kế Dashboard](#18-thiết-kế-dashboard)
  - [19. Continuous Optimization Loop](#19-continuous-optimization-loop)
  - [20. Optimization Backlog](#20-optimization-backlog)
  - [21. Root Cause Analysis](#21-root-cause-analysis)
  - [22. Quản lý thay đổi Prompt / Rule / Model](#22-quản-lý-thay-đổi-prompt--rule--model)
  - [23. AI Regression Test](#23-ai-regression-test)
  - [24. Human Feedback Loop](#24-human-feedback-loop)
  - [25. Quản lý False Positive](#25-quản-lý-false-positive)
  - [26. Quản lý Missed Bug](#26-quản-lý-missed-bug)
  - [27. Cải thiện Context / RAG](#27-cải-thiện-context--rag)
  - [28. Đánh giá tối ưu Token / Cost](#28-đánh-giá-tối-ưu-token--cost)
  - [29. Agent Evaluation](#29-agent-evaluation)
  - [30. Model Routing Evaluation](#30-model-routing-evaluation)
  - [31. Policy Engine Evaluation](#31-policy-engine-evaluation)
  - [32. AI QA Gate Scorecard](#32-ai-qa-gate-scorecard)
  - [33. Kết nối Release / Production Outcome](#33-kết-nối-release--production-outcome)
  - [34. Privacy / Security / Retention](#34-privacy--security--retention)
  - [35. Bộ prompt dùng cho 49](#35-bộ-prompt-dùng-cho-49)
  - [36. Vận hành Monthly Review](#36-vận-hành-monthly-review)
  - [37. Maturity Model của 49](#37-maturity-model-của-49)
  - [38. Failure Mode](#38-failure-mode)
  - [39. Definition of Ready](#39-definition-of-ready)
  - [40. Definition of Done](#40-definition-of-done)
  - [41. Cấu hình tối thiểu / tiêu chuẩn / đầy đủ](#41-cấu-hình-tối-thiểu--tiêu-chuẩn--đầy-đủ)
  - [42. Tổng kết cuối cùng của 49](#42-tổng-kết-cuối-cùng-của-49)
  - [43. Tiêu chuẩn tham khảo và tri thức bên ngoài](#43-tiêu-chuẩn-tham-khảo-và-tri-thức-bên-ngoài)
- [Appendix A. Tập hợp công thức Metric](#appendix-a-tập-hợp-công-thức-metric)
  - [A.1 Review Quality](#a1-review-quality)
  - [A.2 Cost](#a2-cost)
  - [A.3 Delivery](#a3-delivery)
  - [A.4 Safety](#a4-safety)
- [Appendix B. Versioning cho Eval Dataset](#appendix-b-versioning-cho-eval-dataset)
- [Appendix C. Hiệu chỉnh LLM-as-Judge](#appendix-c-hiệu-chỉnh-llm-as-judge)
- [Appendix D. Sample Dashboard Queries](#appendix-d-sample-dashboard-queries)
- [Appendix E. Ví dụ SLO / Error Budget](#appendix-e-ví-dụ-slo--error-budget)
- [Appendix F. Evaluation Maturity Model](#appendix-f-evaluation-maturity-model)
- [Appendix G. Red Team Evaluation](#appendix-g-red-team-evaluation)
- [Appendix H. AI System Release Checklist](#appendix-h-ai-system-release-checklist)
- [Appendix I. Ví dụ cải thiện Pack bằng 49](#appendix-i-ví-dụ-cải-thiện-pack-bằng-49)
- [Appendix J. Executive Reporting Template](#appendix-j-executive-reporting-template)
- [Appendix K. Engineering Improvement Backlog](#appendix-k-engineering-improvement-backlog)
- [Appendix L. Roadmap triển khai tối thiểu](#appendix-l-roadmap-triển-khai-tối-thiểu)
- [Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste](#appendix-dành-cho-người-mới-quy-trình-thực-thi-pack-này-và-prompt-copy-paste)
  - [A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên](#a-0-quy-tắc-tuyệt-đối-cần-tuân-thủ-đầu-tiên)
  - [A-1. Khi nào dùng pack này](#a-1-khi-nào-dùng-pack-này)
  - [A-2. Biến cần điền trước khi copy-paste](#a-2-biến-cần-điền-trước-khi-copy-paste)
  - [A-3. Input đầu tiên cần cho AI đọc](#a-3-input-đầu-tiên-cần-cho-ai-đọc)
  - [A-4. Artifact cần tạo/cập nhật](#a-4-artifact-cần-tạocập-nhật)
  - [A-5. Quy trình thực hiện](#a-5-quy-trình-thực-hiện)
  - [A-6. Prompt khởi động dùng để copy-paste](#a-6-prompt-khởi-động-dùng-để-copy-paste)
  - [A-7. Prompt phê duyệt Plan dùng để copy-paste](#a-7-prompt-phê-duyệt-plan-dùng-để-copy-paste)
  - [A-8. Prompt Monthly Review dùng để copy-paste](#a-8-prompt-monthly-review-dùng-để-copy-paste)
  - [A-9. Prompt review artifact và phán định hoàn tất dùng để copy-paste](#a-9-prompt-review-artifact-và-phán-định-hoàn-tất-dùng-để-copy-paste)
  - [A-10. Prompt trả về sửa lại dùng để copy-paste](#a-10-prompt-trả-về-sửa-lại-dùng-để-copy-paste)
  - [A-11. Điều kiện Stop/Ask](#a-11-điều-kiện-stopask)
  - [A-12. Completion Gate](#a-12-completion-gate)
  - [A-13. Điểm đi tiếp theo](#a-13-điểm-đi-tiếp-theo)

# 49_SDD_Evaluation-Observability-and-Continuous-Optimization-Option_Ver.04_Vietnamese

> Loại: SDD Ver.04 Advanced Option  
> Đối tượng: đánh giá hệ thống phát triển AI, quan sát/observability, metrics, tối ưu liên tục, đảm bảo chất lượng, tối ưu chi phí, audit, vòng lặp cải thiện  
> Tiền đề: đã áp dụng 11, 21〜29, 31〜34, 40〜48, hoặc đã có artifact, trace, review, tool evidence và quản lý failure mode tương đương  
> Nguyên tắc: thành công của việc đưa AI vào quy trình không được đo bằng số lượng comment AI hay lượng nội dung AI tạo ra. Hãy đo bằng tỷ lệ phát hiện hợp lệ, tỷ lệ bỏ sót, chất lượng production, thời gian review, cost per valid finding và mức độ tin cậy của con người.

---

## 0. Vai trò của tài liệu này

Tài liệu này định nghĩa **Evaluation / Observability / Continuous Optimization** trong nhóm Advanced Options của SDD Ver.04.

49 là tiêu chuẩn thực hành để đo lường và cải thiện liên tục việc liệu cơ chế tích hợp AI vào SDD có thực sự nâng cao chất lượng phát triển, tốc độ, an toàn và hiệu quả chi phí hay không.

Mục tiêu của tài liệu này là:

```text
- Đo hiệu quả của AI review và hỗ trợ implement bằng AI
- Trực quan hóa false positive, missed issue, chỉ trích quá mức và bùng nổ chi phí
- Đánh giá thay đổi model / prompt / rules / context / agent / tool
- Cải thiện liên tục vận hành PR QA Gate và Multi-Agent
- Trace quyết định của AI để có thể audit
- Nâng cấp Failure Mode thành evaluation dataset
- Quản lý trade-off giữa token/cost/latency và chất lượng
```

Mục tiêu lớn nhất của 49 là:

```text
Không đưa AI vào phát triển rồi để đó.
Quan sát, đánh giá, so sánh, cải thiện, phòng tái phát và tri thức hóa.
```

---

## 1. Kết luận quan trọng nhất của 49

Nguyên tắc quan trọng nhất của 49 như sau.

```text
Hệ thống AI, giống như phần mềm, là đối tượng cần được đánh giá, giám sát và cải thiện liên tục.
```

Những thứ **không phải** chỉ số thành công của việc đưa AI vào quy trình:

```text
- Số lượng comment AI tăng
- Số lần dùng AI tăng
- Số ký tự được sinh ra tăng
- Số Agent tăng
- Model trở nên mạnh hơn
```

Những thứ **có thể là** chỉ số thành công của việc đưa AI vào quy trình:

```text
- Tỷ lệ phát hiện hợp lệ tăng
- Tỷ lệ false positive giảm
- Tỷ lệ bỏ sót giảm
- Bug lọt ra production giảm
- Thời gian review rút ngắn
- Thời gian PR tồn đọng rút ngắn
- Phát hiện sớm hơn các chỉ trích security nghiêm trọng
- cost per valid finding giảm
- Mức độ tin cậy của human review tăng
- Failure Mode được nâng cấp thành biện pháp phòng tái phát
```

---

## 2. Kết nối với 21〜48

| File | Quan hệ với 49 |
|---|---|
| 21 Core procedure | Kết nối báo cáo/cải thiện của Phase 8/9 với evaluation |
| 22 Core prompt | Nền tảng cho prompt evaluation / dashboard / root cause |
| 23 Source Intelligence | Đo độ chính xác của phân tích source |
| 24 Review/TestCode | Đo hiệu quả review và hiệu quả test |
| 25 Security | Đo hiệu quả của security gate |
| 26 FE/BE Contract | Đo tỷ lệ phát hiện contract drift |
| 27 Microservice | Đo bỏ sót cross-service impact |
| 28 RightSizing | Đo việc áp dụng mode có phù hợp hay không |
| 29 Failure Mode | Nguồn cung cấp evaluation dataset và improvement backlog |
| 11 README | Kết nối với KPI triển khai và maturity |
| 31 Context Loading | Đo context retrieval precision |
| 32 Strategic Compact | Đo chất lượng handoff / resume |
| 33 Artifact Governance | Nơi lưu trace / evidence / audit |
| 34 Project Knowledge | Nâng cấp kết quả evaluation thành knowledge |
| 40 Overview | Đo hiệu quả Advanced Options |
| 41 Heavy Source | Đo độ chính xác repository intelligence |
| 42 Multi-Agent | Đo hiệu quả theo agent, disagreement và routing |
| 43 Tool-Grounded | Đo evidence hierarchy và phán định consensus |
| 44 Token | Đo token/cost/latency/cache |
| 45 Security | Đo AI agent security, MCP, guardrail |
| 46 RAG/CodeMap | Đo chất lượng retrieval / compression / evidence |
| 47 PR QA Gate | Đo chất lượng PR decision và kết quả review |
| 48 Parallel Worktree | Đo hiệu quả làm việc song song, tỷ lệ được chọn, sự cố tích hợp |

49 là phần kết của toàn bộ nhóm 40. Dù áp dụng 40〜48, nếu không có 49 thì không thể giải thích hiệu quả cải thiện, và sẽ bỏ mặc chi phí quá mức, false positive và missed issue.

---

## 3. Đối tượng quan sát trong 49

```text
1. Model
   model name, version, temperature, reasoning mode, latency, cost, error rate

2. Prompt / Rule
   prompt version, rule version, output schema, cache hit, token size

3. Context
   retrieved files, chunks, evidence IDs, compression ratio, retrieval precision

4. Agent
   role, input tokens, output tokens, findings, valid findings, false positives

5. Tool
   test, lint, typecheck, SAST, SCA, secret scan, migration dry-run, benchmark

6. Decision
   approve, comment_only, request_changes, needs_human_review, block_merge

7. Human Feedback
   accepted, rejected, overridden, missed, escalated, accepted risk

8. Outcome
   post-merge defects, hotfix, rollback, incident, customer impact

9. Cost
   tokens, cached tokens, tool output tokens, cost per PR, cost per valid finding

10. Process
   review time, PR cycle time, queue time, rework, merge delay
```

---

## 4. Kiến trúc Observability cho phát triển AI

```text
Developer / PR / Issue
  ↓
SDD Orchestrator
  ↓
Context Builder / RAG / Code Map
  ↓
Agent Pool / Model Router
  ↓
Tool Runner
  ↓
Consensus / Policy Engine
  ↓
PR QA Gate / Human Review
  ↓
Release / Production

Observability Layer:
  - Trace
  - Metrics
  - Logs
  - Datasets
  - Evaluation Runs
  - Dashboards
  - Failure Mode Index
  - Knowledge Library
```

Điều quan trọng không phải là lưu không giới hạn toàn bộ hội thoại nội bộ của AI. Hãy lưu structured trace sau.

```text
- Đã input gì
- Đã đọc context nào
- Agent nào đã phán định gì
- Tool result nào được dùng làm căn cứ
- Policy nào quyết định final decision
- Con người override ở đâu
- Sau đó outcome ở production/PR ra sao
```

---

## 5. Thiết kế Trace

### 5.1 Đơn vị cơ bản của Trace

```text
Trace:
  Toàn bộ một SDD work, PR review, issue analysis, hoặc AI run

Span:
  Xử lý con như Context Builder, Agent Review, Tool Run, Consensus, Policy

Event:
  finding generated, tool failed, human override, cache hit, policy block, v.v.

Metric:
  tokens, cost, latency, valid finding, false positive, v.v.
```

### 5.2 Trace Tree khuyến nghị

```text
sdd.pr_review.trace
  ├─ pre_analyzer
  ├─ risk_classifier
  ├─ context_builder
  │   ├─ repository_map_lookup
  │   ├─ retrieval
  │   ├─ rerank
  │   └─ compression
  ├─ agent.bug_reviewer
  ├─ agent.security_reviewer
  ├─ agent.test_reviewer
  ├─ tool.unit_test
  ├─ tool.typecheck
  ├─ tool.sast
  ├─ consensus_engine
  ├─ policy_engine
  ├─ pr_comment
  └─ human_feedback
```

### 5.3 Template Trace Record

```json
{
  "trace_id": "",
  "sdd_ticket": "",
  "pr_id": "",
  "phase": "",
  "mode": "standard_plus|heavy|critical",
  "started_at": "",
  "completed_at": "",
  "actors": {
    "human_owner": "",
    "agents": []
  },
  "inputs": {
    "issue": "",
    "base_commit": "",
    "head_commit": "",
    "artifact_versions": []
  },
  "context": {
    "retrieved_files": [],
    "evidence_ids": [],
    "excluded_files": [],
    "context_tokens": 0,
    "compression_ratio": 0.0
  },
  "models": [
    {
      "agent": "security_reviewer",
      "model": "",
      "prompt_version": "",
      "input_tokens": 0,
      "output_tokens": 0,
      "cached_tokens": 0,
      "latency_ms": 0,
      "cost": 0.0
    }
  ],
  "tools": [],
  "decision": {
    "ai_decision": "",
    "policy_decision": "",
    "human_decision": "",
    "final_status": ""
  },
  "outcome": {
    "merged": false,
    "post_merge_defects": 0,
    "rollback": false,
    "incident": false
  }
}
```

---

## 6. Phân loại Metrics

Trong 49, metrics được chia thành 7 nhóm sau.

```text
1. Quality Metrics
2. Safety / Security Metrics
3. Efficiency / Delivery Metrics
4. Cost / Token Metrics
5. Agent / Model Metrics
6. Context / RAG Metrics
7. Developer Experience Metrics
```

---

## 7. Quality Metrics

| Metric | Định nghĩa | Mục đích |
|---|---|---|
| valid_finding_rate | Tỷ lệ chỉ trích của AI được con người/Tool/Outcome xác nhận là hợp lệ | Quản lý noise |
| false_positive_rate | Tỷ lệ bị bác bỏ hoặc là false positive | Giảm tải review |
| missed_bug_rate | Tỷ lệ vấn đề AI bỏ sót và được phát hiện sau đó | Giảm bỏ sót |
| escaped_defect_rate | Defect lọt ra sau merge | Chất lượng production |
| regression_prevented_count | Số regression được AI/Tool chặn trước merge | Đo giá trị |
| test_gap_detection_rate | Tỷ lệ hữu ích của chỉ trích thiếu test | Cải thiện test |
| contract_drift_detection_rate | Tỷ lệ phát hiện không nhất quán FE/BE/API contract | Chất lượng contract |

### 7.1 Tỷ lệ phát hiện hợp lệ

```text
valid_finding_rate = valid_findings / total_findings
```

Định nghĩa valid finding.

```text
- Con người phán định là cần sửa
- Tái hiện được bằng tool evidence
- Dẫn đến bổ sung test
- Có khả năng cao ngăn production incident
- Được ghi nhận chính thức như accepted risk
```

---

## 8. Safety / Security Metrics

| Metric | Định nghĩa |
|---|---|
| critical_security_detection_rate | Tỷ lệ phát hiện critical security issue |
| auth_boundary_review_coverage | Tỷ lệ security review chạy khi có thay đổi authentication/authorization |
| secret_leak_prevention_count | Số lần ngăn secret lọt vào trước merge |
| prompt_injection_incident_count | Số nghi vấn prompt injection / tool injection |
| excessive_agency_block_count | Số lần policy chặn quyền AI quá mức |
| human_approval_compliance | Tỷ lệ có human approval cho high-risk action |
| guardrail_violation_rate | Tỷ lệ vi phạm guardrail |

Trong security, điều quan trọng là đo veto chứ không phải majority vote.

```text
Dù 4 AI nói OK, nếu 1 Security Reviewer đưa ra critical, có chuyển sang human review hay không.
```

---

## 9. Efficiency / Delivery Metrics

Kết hợp DORA metrics với metrics riêng của SDD.

```text
Nhóm DORA:
- deployment frequency
- lead time for changes
- change failure rate
- failed deployment recovery time
- reliability

Nhóm SDD:
- review_time_saved
- pr_cycle_time
- time_to_first_valid_finding
- rework_count
- phase_completion_time
- artifact_update_lag
- qa_gate_queue_time
```

### 9.1 Thời gian tồn đọng PR

```text
pr_cycle_time = merged_at - opened_at
review_queue_time = first_review_started_at - opened_at
ai_review_latency = ai_review_completed_at - ai_review_started_at
```

Nếu đưa AI vào làm tăng thời gian tồn đọng PR, hãy nghi ngờ các nguyên nhân sau.

```text
- Comment của AI quá nhiều
- False positive rate cao
- High-risk classification quá mức
- Tool matrix quá nặng
- Human review escalation mơ hồ
```

---

## 10. Cost / Token Metrics

| Metric | Định nghĩa |
|---|---|
| cost_per_pr | Chi phí AI/Tool trên mỗi PR |
| tokens_per_pr | Token trên mỗi PR |
| cost_per_valid_finding | Chi phí cho mỗi phát hiện hợp lệ |
| cached_token_ratio | Tỷ lệ input token được cache hit |
| context_compression_ratio | Tỷ lệ context trước/sau nén |
| tool_output_compression_ratio | Tỷ lệ giữa raw tool output và bản đưa vào AI |
| agent_call_count | Số lần gọi agent |
| recursive_round_count | Số vòng recursive loop |
| early_exit_rate | Tỷ lệ kết thúc sớm các xử lý không cần thiết |
| model_routing_savings | Ước tính tiết kiệm nhờ tránh model đắt |

### 10.1 cost per valid finding

```text
cost_per_valid_finding = total_ai_cost / valid_findings
```

Biện pháp khi chỉ số này xấu đi.

```text
- Kiềm chế low severity comment
- Thu hẹp agent selection
- Tăng cường context partitioning
- Cải thiện prompt caching
- Pre-filter bằng cheap model
- Hợp nhất duplicated findings
- Cải thiện prompt gây false positive bằng evaluation dataset
```

---

## 11. Agent / Model Metrics

| Metric | Định nghĩa |
|---|---|
| agent_valid_finding_rate | Tỷ lệ phát hiện hợp lệ theo agent |
| agent_false_positive_rate | Tỷ lệ false positive theo agent |
| agent_missed_category | Category mà agent dễ bỏ sót |
| model_latency_p95 | p95 latency theo model |
| model_cost_per_1k_decision | Model cost trên mỗi decision |
| routing_accuracy | Tỷ lệ model router chọn model phù hợp |
| arbiter_override_rate | Tỷ lệ quyết định Arbiter bị con người phủ quyết |
| disagreement_rate | Tỷ lệ bất đồng giữa agent |
| useful_disagreement_rate | Tỷ lệ bất đồng dẫn đến phát hiện hữu ích |

Việc tăng hay giảm agent phải dựa trên hiệu quả theo agent.

```text
Ứng viên xóa bỏ:
- Tỷ lệ valid finding thấp
- False positive rate cao
- Chủ yếu trùng với agent khác
- Cost cao
- Human override nhiều

Ứng viên tăng cường:
- Phát hiện critical dù tần suất thấp
- Phát hiện nhanh hơn con người trong lĩnh vực cụ thể
- False positive thấp
- Tương thích tốt với project knowledge
```

---

## 12. Context / RAG Metrics

| Metric | Định nghĩa |
|---|---|
| retrieval_precision | Tỷ lệ context lấy về là hữu ích |
| retrieval_recall_proxy | Tỷ lệ lấy được context mà sau đó được xác định là cần thiết |
| evidence_utilization_rate | Tỷ lệ evidence được AI thật sự trích dẫn/tham chiếu |
| context_noise_ratio | Tỷ lệ context không cần thiết |
| missing_context_incidents | Số lần phán định sai do thiếu context |
| stale_context_incidents | Số lần phán định sai do dựa vào tài liệu cũ |
| compression_loss_incidents | Số lần thông tin quan trọng bị mất do nén |
| expand_on_demand_rate | Tỷ lệ cần mở rộng thêm thông tin |

### 12.1 Phán định chất lượng Context

```text
Context tốt:
- changed code
- callers / callees
- related tests
- relevant spec
- current DB/API contract
- exact evidence IDs

Context xấu:
- tài liệu thiết kế cũ
- unrelated docs
- toàn văn raw logs
- toàn văn vendor/generated code
- toàn bộ lịch sử hội thoại AI
```

---

## 13. Developer Experience Metrics

```text
- developer_acceptance_rate
- ai_comment_hidden_rate
- ai_comment_marked_noise_rate
- perceived_review_quality
- review_fatigue_score
- time_saved_self_report
- trust_score
- manual_override_satisfaction
```

Cũng bắt buộc thu thập feedback định tính.

```text
- Chỉ trích AI này có hữu ích không
- Chỉ trích AI này có gây phiền không
- Lần sau có nên đưa ra cùng loại chỉ trích này không
- Đã thiếu góc nhìn nào
- Comment nào muốn tự động ẩn
```

---

## 14. Thiết kế Evaluation Dataset

Trong 49, tạo các dataset sau.

```text
docs/evaluation/
  README.md
  golden-pr-dataset.md
  finding-calibration-dataset.md
  false-positive-dataset.md
  missed-bug-dataset.md
  security-red-team-dataset.md
  context-retrieval-dataset.md
  token-cost-benchmark-dataset.md
  agent-routing-dataset.md
```

### 14.1 Golden PR Dataset

```md
# Golden PR Dataset Entry

## ID
- dataset_id:
- source:
- privacy level:

## PR Summary
- domain:
- risk:
- changed files:
- expected decision:

## Ground Truth
- valid findings:
- invalid findings:
- required tests:
- required human reviewers:
- expected tool results:

## Evaluation Criteria
| Criterion | Expected |
|---|---|
| decision | |
| security finding | |
| test gap | |
| false positive allowed | |

## Notes
- anonymization:
- data masking:
- retention:
```

### 14.2 Missed Bug Dataset

Tạo từ production incident, hotfix, bug được phát hiện sau review.

```text
- Vì sao AI bỏ sót
- Context cần thiết là gì
- Tool cần thiết là gì
- Agent cần thiết là gì
- Prompt/rule cần thiết là gì
- Lần evaluation sau có phát hiện được không
```

---

## 15. Evaluation Run Record

```md
# Evaluation Run Record

## Run
- eval_id:
- date:
- owner:
- purpose:
- model versions:
- prompt versions:
- rules versions:
- dataset versions:

## Config
| Component | Version |
|---|---|
| Orchestrator | |
| Context Builder | |
| Agent Set | |
| Model Router | |
| Policy Engine | |

## Results
| Metric | Baseline | Current | Change | Target | Status |
|---|---:|---:|---:|---:|---|
| valid_finding_rate | | | | | |
| false_positive_rate | | | | | |
| missed_bug_rate | | | | | |
| cost_per_valid_finding | | | | | |
| latency_p95 | | | | | |

## Regressions
| Area | Regression | Severity | Owner | Action |
|---|---|---|---|---|

## Decision
- promote / rollback / continue_experiment / needs_more_data:
- reason:
```

---

## 16. Các loại Evaluation

### 16.1 Offline Eval

Đánh giá bằng PR quá khứ hoặc synthetic dataset.

```text
Mục đích:
- Kiểm tra regression trước khi đổi model/prompt
- So sánh cấu hình agent
- Kiểm tra chất lượng context compression
- So sánh token/cost
```

### 16.2 Shadow Eval

Đưa ra phán định AI trên PR production, nhưng không phản ánh vào merge gate.

```text
Mục đích:
- Trước khi đưa agent mới vào
- Trước khi đưa model mới vào
- Trước khi đưa high-risk policy vào
- Kiểm tra false positive
```

### 16.3 Online Eval

Chạy như hỗ trợ review hoặc PR gate thực tế.

```text
Mục đích:
- stable configuration
- measured rollout
- thu thập human feedback
```

### 16.4 Red Team Eval

Đánh giá tấn công/lạm dụng/đánh lạc hướng chính workflow phát triển AI.

```text
Đối tượng:
- prompt injection
- tool injection
- malicious README
- poisoned docs
- secret leakage
- excessive agency
- MCP misuse
```

---

## 17. Ví dụ về tiêu chuẩn đánh giá

```yaml
quality_gate:
  valid_finding_rate_min: 0.50
  false_positive_rate_max: 0.35
  critical_missed_bug_max: 0
  human_override_rate_max: 0.30

cost_gate:
  cost_per_pr_p50_max: 1.0
  cost_per_pr_p95_max: 5.0
  cost_per_valid_finding_max: 3.0
  cached_token_ratio_min: 0.30

latency_gate:
  ai_review_p50_seconds_max: 60
  ai_review_p95_seconds_max: 300

security_gate:
  secret_leak_in_output: 0
  unauthorized_tool_call: 0
  high_risk_without_human_review: 0
```

Các con số cần được điều chỉnh theo tổ chức, quy mô dự án, đơn giá model và mức chấp nhận rủi ro.

---

## 18. Thiết kế Dashboard

### 18.1 Executive Dashboard

```text
- Thời gian review trước/sau khi áp dụng AI
- Production incident / rollback / hotfix
- Xu hướng cost
- Xu hướng DORA metrics
- High-risk detection
- Developer trust score
```

### 18.2 Engineering Dashboard

```text
- AI decision theo PR
- valid / false positive
- hiệu năng theo agent
- tool failure
- test gap
- context missing
- latency
```

### 18.3 AI Platform Dashboard

```text
- model usage
- token usage
- cache hit rate
- prompt version performance
- eval regression
- agent failure
- tracing errors
```

### 18.4 Security Dashboard

```text
- critical security findings
- auth boundary reviews
- secret scan blocks
- MCP/tool violations
- prompt injection attempts
- human approval compliance
```

---

## 19. Continuous Optimization Loop

Vòng lặp cải thiện của 49 như sau.

```text
1. Observe
   Thu thập trace / metric / feedback

2. Evaluate
   Đo bằng dataset / eval run / human feedback

3. Diagnose
   Phân rã nguyên nhân false positive, missed issue, cost tăng

4. Improve
   Thay đổi prompt / rule / context / model / agent / tool / policy

5. Validate
   Xác nhận bằng offline / shadow / online eval

6. Promote
   Nâng cấp thay đổi tốt vào Core / Pack / Knowledge

7. Retire
   Xóa agent/rule/prompt kém hiệu quả
```

---

## 20. Optimization Backlog

```md
# AI Optimization Backlog

| ID | Problem | Evidence | Hypothesis | Change | Expected Impact | Owner | Status |
|---|---|---|---|---|---|---|---|
| OPT-001 | Security false positive high | dashboard | prompt quá rộng | thu hẹp rule | giảm FP | | |
| OPT-002 | Cost high for low-risk PR | metrics | chọn quá nhiều agent | cập nhật routing | giảm cost | | |
| OPT-003 | Context missing for DB change | missed bug | không retrieve schema | thêm DB index | giảm missed | | |

## Priority Rule
- critical missed bug > security issue > high cost > developer friction > cosmetic
```

---

## 21. Root Cause Analysis

Không kết thúc thất bại của AI bằng câu “model kém”.

```text
Phân loại nguyên nhân Failure:
- requirement ambiguity
- missing context
- stale context
- wrong retrieval
- over-compression
- weak prompt
- missing project knowledge
- missing tool
- tool result ignored
- bad consensus
- bad policy
- model weakness
- agent role overlap
- token budget too low
- human feedback not incorporated
```

### 21.1 Template RCA

```md
# AI Failure Root Cause Analysis

## Incident / Failure
- ID:
- detected by:
- impact:

## What Happened
- timeline:
- expected:
- actual:

## AI System Behavior
- agents involved:
- context retrieved:
- tool results:
- decision:
- human feedback:

## Root Cause
| Category | Present? | Evidence |
|---|---:|---|
| Missing context | | |
| Stale context | | |
| Prompt issue | | |
| Tool missing | | |
| Policy issue | | |
| Model limitation | | |

## Fix
- immediate:
- prompt/rule:
- dataset:
- tool:
- policy:
- knowledge:

## Verification
- eval added:
- regression test:
- target metric:
```

---

## 22. Quản lý thay đổi Prompt / Rule / Model

Thay đổi của hệ thống AI cũng phải được đánh giá trước khi promote, giống như code thông thường.

```text
Đối tượng thay đổi:
- system prompt
- agent prompt
- review checklist
- severity rubric
- output schema
- model version
- model router
- RAG retriever
- compression rule
- policy engine
- tool selection
```

### 22.1 Change Record

```md
# AI System Change Record

## Change
- component:
- from:
- to:
- reason:

## Expected Impact
- quality:
- cost:
- latency:
- security:

## Eval Requirement
- dataset:
- metrics:
- pass criteria:

## Rollout
- offline:
- shadow:
- limited:
- full:

## Result
- promoted / rolled back:
- evidence:
```

---

## 23. AI Regression Test

Mỗi khi thay đổi prompt hoặc model AI, phải kiểm tra xem có bỏ sót các bug đã từng ngăn được trước đây hay không.

```text
AI Regression Suite:
- valid security findings
- known false positives
- missed bugs
- context retrieval cases
- token budget stress cases
- prompt injection cases
- multi-agent disagreement cases
```

### 23.1 AI Regression Gate

```text
Điều kiện cấm Promote:
- critical missed bug tăng
- phát sinh secret output
- high-risk PR không được gửi sang human review
- false positive rate vượt ngưỡng
- cost vượt ngưỡng
- latency p95 vượt ngưỡng
```

---

## 24. Human Feedback Loop

Làm cho feedback của con người ít ma sát.

```text
PR comment feedback actions:
- useful
- false positive
- duplicate
- too verbose
- wrong severity
- missing context
- should be blocking
- should be non-blocking
```

### 24.1 Feedback Record

```json
{
  "finding_id": "",
  "human_feedback": "false_positive|valid|duplicate|missed|severity_wrong",
  "correct_severity": "",
  "reason": "",
  "should_update": ["prompt", "rule", "dataset", "context", "policy"],
  "reviewer": "",
  "timestamp": ""
}
```

---

## 25. Quản lý False Positive

False positive phá hỏng niềm tin vào AI.

```text
Xử lý False Positive:
1. Phân loại finding category
2. RCA vì sao false positive
3. Quyết định có suppress rule hay không
4. Đăng ký vào dataset
5. Sửa prompt/rule
6. Xác minh lại ở eval lần sau
```

Nếu xóa false positive quá mạnh, missed issue sẽ tăng; vì vậy hãy phân biệt các cách sau.

```text
- suppress always
- suppress if tool evidence absent
- downgrade severity
- require more evidence
- keep but human review only
```

---

## 26. Quản lý Missed Bug

Missed bug là đối tượng cải thiện quan trọng nhất.

```text
Xử lý Missed Bug:
1. Bỏ sót ở PR/issue nào
2. Context cần thiết là gì
3. Tool cần thiết là gì
4. Agent nào đáng ra phải xem
5. Policy có thể ngăn được không
6. Thêm vào dataset
7. Thêm vào regression eval
8. Phản ánh vào 29 Failure Mode / 34 Knowledge
```

---

## 27. Cải thiện Context / RAG

Chất lượng RAG bắt buộc phải được đánh giá trong 49.

```text
Golden Retrieval Query:
- query:
- expected files:
- expected symbols:
- forbidden irrelevant files:
- required evidence:
```

### 27.1 Retrieval Eval Record

```md
# Retrieval Eval Record

| Query | Expected Evidence | Retrieved | Precision | Recall Proxy | Notes |
|---|---|---|---:|---:|---|

## Issues
- missing file:
- stale doc:
- irrelevant chunk:
- over-compressed:

## Improvement
- index:
- chunking:
- rerank:
- filter:
- context budget:
```

---

## 28. Đánh giá tối ưu Token / Cost

49 kiểm tra liệu việc cắt giảm ở 44 có làm giảm chất lượng hay không.

```text
Góc nhìn đánh giá:
- token reduction rate
- cost reduction rate
- latency reduction rate
- valid finding retention rate
- missed bug increase 여부
- context compression loss
- cache hit rate
```

### 28.1 Token Optimization Experiment

```md
# Token Optimization Experiment

## Experiment
- target:
- baseline config:
- new config:

## Metrics
| Metric | Baseline | New | Change | Accept? |
|---|---:|---:|---:|---:|
| input tokens | | | | |
| output tokens | | | | |
| cost | | | | |
| valid findings | | | | |
| false positives | | | | |
| missed bugs | | | | |
| latency p95 | | | | |

## Decision
- promote / rollback / iterate:
```

---

## 29. Agent Evaluation

### 29.1 Agent Scorecard

```md
# Agent Scorecard

| Agent | Calls | Valid | False Positive | Missed Category | Cost | Latency | Keep? |
|---|---:|---:|---:|---|---:|---:|---|
| Bug Reviewer | | | | | | | |
| Security Reviewer | | | | | | | |
| Test Reviewer | | | | | | | |
| Performance Reviewer | | | | | | | |

## Decision
- keep:
- tune:
- remove:
- merge with another agent:
- require stronger model:
```

### 29.2 Tiêu chí xóa Agent

```text
- Tỷ lệ valid finding thấp trong 3 tháng liên tiếp
- Trùng với agent khác trên 90%
- Bị human override nhiều
- Cost cao nhưng hiệu quả thấp
- Làm giảm developer trust
```

### 29.3 Tiêu chí tăng cường Agent

```text
- Phát hiện critical issue dù tần suất thấp
- Nhanh hơn con người trong lĩnh vực cụ thể
- False positive thấp
- Phù hợp tốt với project knowledge
```

---

## 30. Model Routing Evaluation

```md
# Model Routing Evaluation

| Task | Risk | Routed Model | Expected Model | Result | Cost | Quality |
|---|---|---|---|---|---:|---|

## Errors
- case cheap model không đủ:
- case dùng strong model quá nhiều:
- case cần long-context model:

## Update
- routing rule:
- threshold:
- fallback:
```

---

## 31. Policy Engine Evaluation

Policy nên mang tính quyết định luận hơn AI, nhưng nếu quá cứng sẽ làm nghẽn phát triển.

```text
Góc nhìn đánh giá:
- block có hợp lý không
- yêu cầu human review có quá mức không
- có bỏ sót high-risk không
- khi tests failed có luôn request_changes không
- có block SAST critical không
- có accepted risk record không
```

---

## 32. AI QA Gate Scorecard

```md
# AI QA Gate Scorecard

## Period
- from:
- to:

## Summary
| Metric | Value | Target | Status |
|---|---:|---:|---|
| PRs reviewed | | | |
| valid finding rate | | | |
| false positive rate | | | |
| missed bug rate | | | |
| cost per PR | | | |
| cost per valid finding | | | |
| ai review latency p95 | | | |
| human override rate | | | |

## Top Wins
1.
2.
3.

## Top Problems
1.
2.
3.

## Actions
| Action | Owner | Due | Expected Impact |
|---|---|---|---|
```

---

## 33. Kết nối Release / Production Outcome

Không kết thúc đánh giá AI ở PR.

```text
Những thứ cần theo dõi sau merge:
- incident
- rollback
- hotfix
- customer bug
- support ticket
- performance regression
- security finding
- data correction
```

Nếu Outcome xấu, trả lại cho các mục sau.

```text
- 29 Failure Mode
- 34 Knowledge Library
- 47 PR QA Gate
- 43 Consensus / Policy
- 46 Context / RAG
- 44 Token budget
```

---

## 34. Privacy / Security / Retention

Không được thu thập quá nhiều thông tin mật bằng Observability.

```text
Cấm lưu hoặc cần mask:
- secrets
- credentials
- tokens
- personal data
- production data raw logs
- customer-specific payloads
- private keys
- payment data
```

### 34.1 Retention Policy

```md
# AI Observability Retention Policy

| Data Type | Store? | Mask? | Retention | Access |
|---|---:|---:|---|---|
| trace metadata | yes | no | 1 year | engineering |
| prompt full text | conditional | yes | 30-90 days | restricted |
| model output | yes | yes | 180 days | engineering |
| raw tool log | conditional | yes | 30 days | restricted |
| security finding | yes | yes | policy-defined | security |
| production payload | no by default | required | minimal | restricted |
```

---

## 35. Bộ prompt dùng cho 49

### 35.1 Prompt tạo Evaluation Plan

```text
Bạn là AI Evaluation Architect của SDD Ver.04.
Hãy lập kế hoạch đánh giá cho workflow phát triển AI mục tiêu theo tiêu chuẩn 49.

Input:
- workflow mục tiêu
- agent/model/tool được dùng
- PR/issue mục tiêu
- metrics hiện có
- Failure Mode

Output:
1. Mục tiêu đánh giá
2. Evaluation dataset
3. Thiết kế offline/shadow/online eval
4. quality metrics
5. cost/token metrics
6. security metrics
7. tiêu chí pass/fail
8. đề xuất dashboard
9. điều kiện rollout/rollback
10. đề xuất optimization backlog ban đầu
```

### 35.2 Prompt phân tích Dashboard

```text
Bạn là AI Development Observability Analyst.
Hãy phân tích metrics/dashboard đính kèm và trích xuất các điểm cần cải thiện của hệ thống phát triển AI.

Góc nhìn:
- Tỷ lệ phát hiện hợp lệ
- Tỷ lệ false positive
- Tỷ lệ bỏ sót
- cost per valid finding
- token/cache/compression
- hiệu quả theo agent
- model routing
- context retrieval
- developer feedback

Output:
- top wins
- top risks
- root cause hypotheses
- immediate actions
- experiments
- metrics to watch
```

### 35.3 Prompt Missed Bug RCA

```text
Bạn là AI Failure Analyst của SDD Ver.04.
Hãy thực hiện root cause analysis cho bug mà AI đã bỏ sót.

Output:
1. Tổng quan bug
2. Context đáng ra cần có
3. Tool đáng ra cần có
4. Agent đáng ra cần có
5. Thiếu sót trong prompt/rule/policy
6. Đề xuất thêm vào dataset
7. Đề xuất đăng ký 29 Failure Mode
8. Đề xuất nâng cấp 34 Knowledge
9. Đề xuất sửa 47 QA Gate
```

### 35.4 Prompt Token Cost Optimization

```text
Bạn là AI Cost Optimization Lead.
Hãy phân tích token/cost/latency của workflow phát triển AI và đề xuất biện pháp cắt giảm mà không làm giảm chất lượng.

Output:
- cost hotspot
- token hotspot
- đề xuất cải thiện cache hit
- đề xuất cải thiện context compression
- đề xuất giảm agent
- đề xuất cải thiện model routing
- đề xuất cải thiện early exit
- rủi ro suy giảm chất lượng
- mục cần xác nhận bằng eval
```

### 35.5 Prompt Monthly Continuous Optimization Review

```text
Bạn là SDD AI Platform Review Board.
Hãy kiểm tra metrics, Failure Mode và Human Feedback của hệ thống phát triển AI trong tháng này, rồi lập kế hoạch cải thiện liên tục.

Output:
- những thứ nên tiếp tục
- những thứ nên dừng
- prompt/rule/model cần tuning
- case cần thêm vào dataset
- case cần nâng cấp thành Knowledge
- KPI trọng tâm của tháng tới
- owner và deadline
```

---

## 36. Vận hành Monthly Review

```text
Hằng tuần:
- Kiểm tra lỗi nghiêm trọng của AI QA Gate
- Kiểm tra high-risk override
- Kiểm tra cost anomaly

Hằng tháng:
- agent scorecard
- phân tích valid/false positive
- missed bug RCA
- token/cost review
- ứng viên thay đổi prompt/rule

Hằng quý:
- xem lại model selection
- kiểm kê evaluation dataset
- xóa deprecated rule
- đo hiệu quả advanced options
- khảo sát mức hài lòng của developer
```

---

## 37. Maturity Model của 49

```text
Level 0: No Measurement
  Có dùng AI nhưng không đo.

Level 1: Basic Logging
  Ghi nhận model/token/cost ở mức cơ bản.

Level 2: Structured Trace
  Trace được agent/tool/context/decision.

Level 3: Feedback Loop
  Thu thập human feedback và false positive.

Level 4: Evaluation Dataset
  Có golden PR / missed bug / red team dataset.

Level 5: Continuous Optimization
  Cải thiện prompt/model/context/policy kèm eval.

Level 6: Outcome-linked AI Governance
  Tối ưu tích hợp PR, chất lượng production, DORA, cost và DX.
```

---

## 38. Failure Mode

| ID | Failure Mode | Biện pháp |
|---|---|---|
| EVAL-001 | Lấy số lượng comment AI làm success metric | Chuyển sang valid finding rate |
| EVAL-002 | False positive nhiều khiến con người bỏ qua | false positive dataset / noise control |
| EVAL-003 | Không ghi nhận missed issue | Bắt buộc missed bug dataset |
| EVAL-004 | Chỉ giảm cost và làm giảm chất lượng | quality-cost paired eval |
| EVAL-005 | Áp dụng prompt change không đánh giá | Bắt buộc eval gate |
| EVAL-006 | Regression do đổi model | model regression suite |
| EVAL-007 | Lưu thông tin mật trong trace | masking / retention policy |
| EVAL-008 | Dashboard quá nhiều nên không ai xem | role-based dashboard |
| EVAL-009 | Không thu thập được human feedback | feedback đơn giản trong PR UI |
| EVAL-010 | Eval dataset cũ | monthly refresh |
| EVAL-011 | Quá lệ thuộc synthetic dataset | Bổ sung từ real PR / incident |
| EVAL-012 | Không đo chất lượng RAG | golden retrieval eval |
| EVAL-013 | Không có tiêu chí xóa agent | agent scorecard |
| EVAL-014 | AI system trở thành black box | trace / evidence / decision record |

---

## 39. Definition of Ready

Những thứ cần có trước khi bắt đầu 49.

```text
- Đối tượng AI workflow rõ ràng
- Có thiết kế trace_id / run_id
- Có nơi lưu artifact
- Có cách thu thập human feedback
- Minimum metrics đã được định nghĩa
- Có chính sách privacy/masking
- Có ứng viên eval dataset ban đầu
- Owner đã được quyết định
```

---

## 40. Definition of Done

Điều kiện để nói 49 đang hoạt động.

```text
- Có thể trace AI run
- Có thể lấy metrics theo agent/model/tool/context
- Có thể phân loại valid / false positive / missed bug
- Có thể eval thay đổi prompt/model/rule
- Có thể theo dõi cost per valid finding
- Có dashboard theo từng vai trò
- Monthly optimization review được thực hiện
- Cải thiện quay lại 29/34
- Có thể giải thích hiệu quả của việc đưa AI vào quy trình
```

---

## 41. Cấu hình tối thiểu / tiêu chuẩn / đầy đủ

### 41.1 Cấu hình tối thiểu

```text
- AI cost/token theo PR
- AI decision
- human feedback
- phân loại false positive / valid
- monthly summary
```

### 41.2 Cấu hình tiêu chuẩn

```text
- trace / span / event
- agent scorecard
- golden PR dataset
- cost per valid finding
- context retrieval metrics
- dashboard
- monthly optimization review
```

### 41.3 Cấu hình đầy đủ

```text
- Tương thích OpenTelemetry GenAI semantic conventions
- offline/shadow/online eval
- red team dataset
- model/prompt regression gate
- kết nối DORA / production outcome
- automatic optimization backlog
- AI governance review board
```

---

## 42. Tổng kết cuối cùng của 49

49 là phần kết của SDD Ver.04 Advanced Options.

```text
Đưa AI vào.
Làm AI mạnh hơn.
Song song hóa AI.
Cho AI dùng tool.
Tạo PR Gate bằng AI.

Nhưng nếu không đo, không thể cải thiện.
```

Trạng thái mà 49 hướng tới như sau.

```text
Biết AI đã xem gì.
Biết vì sao AI phán định.
Biết chỉ trích nào hợp lệ.
Biết chỉ trích nào là noise.
Biết đã bỏ sót gì.
Biết tốn bao nhiêu chi phí cho cái gì.
Biết prompt/model/agent/context nào có tác dụng.
Biết tiếp theo cần sửa gì.
```

Nguyên tắc cuối cùng như sau.

```text
Không biến hệ thống phát triển AI thành thứ ma thuật không thể quan sát.
Hãy biến hệ thống phát triển AI thành một lớp đảm bảo chất lượng có thể đo lường, giải thích và cải thiện.
```

---

## 43. Tiêu chuẩn tham khảo và tri thức bên ngoài

Tài liệu này thực tiễn hóa các tri thức bên ngoài sau cho SDD.

```text
- OpenTelemetry Generative AI semantic conventions: events, metrics, spans, exceptions của GenAI operations
- OpenAI Agents SDK Tracing: trace LLM generations, tool calls, handoffs, guardrails, custom events
- OpenAI Evals / Agent Evals: đánh giá agent workflow bằng datasets, graders, evaluation runs
- DORA metrics: đo software delivery performance
- NIST AI RMF / GenAI Profile: quản lý rủi ro AI
- Google SRE postmortem culture: học hỏi không đổ lỗi
- Tài liệu đính kèm AI accuracy improvement strategy: Observability / Evaluation / Human Governance
- Tài liệu đính kèm AI token reduction strategy: Cost Observability / cost per valid finding / cache hit / token budget
```

---

# Appendix A. Tập hợp công thức Metric

## A.1 Review Quality

```text
valid_finding_rate = valid_findings / total_ai_findings
false_positive_rate = false_positive_findings / total_ai_findings
missed_bug_rate = missed_bugs / total_known_bugs
blocking_precision = valid_blocking_findings / all_blocking_findings
blocking_recall = valid_blocking_findings / all_should_block_cases
```

## A.2 Cost

```text
cost_per_pr = total_ai_cost / reviewed_pr_count
cost_per_valid_finding = total_ai_cost / valid_findings
cost_per_prevented_incident = total_ai_cost / prevented_incidents
cache_hit_rate = cached_input_tokens / total_input_tokens
compression_ratio = compressed_tokens / raw_tokens
```

## A.3 Delivery

```text
ai_review_latency = ai_review_completed_at - pr_opened_at
manual_review_time_saved = baseline_manual_review_time - actual_manual_review_time
cycle_time_delta = cycle_time_after_ai - cycle_time_before_ai
```

## A.4 Safety

```text
human_review_compliance = high_risk_prs_with_human_review / high_risk_prs
policy_bypass_rate = policy_bypasses / applicable_runs
security_veto_effectiveness = true_security_vetoes / all_security_vetoes
```

---

# Appendix B. Versioning cho Eval Dataset

```text
evals/
  README.md
  datasets/
    golden-pr-v001.jsonl
    golden-pr-v002.jsonl
    security-auth-v001.jsonl
    db-migration-v001.jsonl
    rag-retrieval-v001.jsonl
  rubrics/
    finding-quality-v001.md
    decision-quality-v001.md
    rag-quality-v001.md
  runs/
    2026-05-16-model-router-v002/
      config.json
      results.json
      regressions.md
      decision.md
```

Quy tắc version dataset:

```text
- v001 là baseline cố định
- Incident mới thêm vào candidate
- Mỗi quý nâng cấp lên curated version
- Thay đổi ground truth bắt buộc có Decision Record
```

---

# Appendix C. Hiệu chỉnh LLM-as-Judge

LLM Judge tiện lợi, nhưng không phải sự thật duy nhất.

```text
Bắt buộc:
- human-labeled seed set
- judge prompt versioning
- inter-rater comparison
- disagreement review
- drift monitoring
```

Những việc Judge phù hợp:

```text
- chất lượng summary
- mức độ đầy đủ của giải thích kèm evidence
- actionability của PR comment
- hợp nhất chỉ trích trùng lặp
```

Những việc không được phó mặc chỉ cho Judge:

```text
- security critical decision
- production release approval
- phán đoán legal/compliance
- phán định secret exposure
- cho phép data deletion
```

---

# Appendix D. Sample Dashboard Queries

Cần sửa theo DB schema thực tế.

```sql
-- Agent별 cost per valid finding
SELECT
  agent_name,
  SUM(cost) AS total_cost,
  SUM(valid_findings) AS valid_findings,
  SUM(cost) / NULLIF(SUM(valid_findings), 0) AS cost_per_valid_finding
FROM agent_runs
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY agent_name
ORDER BY cost_per_valid_finding DESC;
```

```sql
-- category có nhiều false positive
SELECT
  category,
  COUNT(*) AS false_positive_count
FROM findings
WHERE outcome = 'false_positive'
  AND created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY category
ORDER BY false_positive_count DESC;
```

```sql
-- tỷ lệ tuân thủ human review của high risk PR
SELECT
  COUNT(*) FILTER (WHERE human_review_required = true AND human_review_done = true)::float
  / NULLIF(COUNT(*) FILTER (WHERE risk_level IN ('high', 'critical')), 0) AS compliance
FROM pr_reviews
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days';
```

---

# Appendix E. Ví dụ SLO / Error Budget

Đặt SLO cho cả hệ thống phát triển AI.

```text
Ví dụ SLO:
- high-risk PR human review compliance >= 99%
- security critical missed by AI gate = 0 tolerated per quarter
- PR AI review P95 latency <= 10 min for standard PR
- false positive rate <= 30% for blocking findings
- cache hit rate >= 40% for repeated static prompts
- trace completeness >= 95%
```

Khi tiêu thụ error budget:

```text
- new prompt rollout freeze
- agent 추가 freeze
- high-risk auto decision stop
- tăng cường offline eval
- bắt buộc human review
```

---

# Appendix F. Evaluation Maturity Model

| Level | Trạng thái | Mô tả |
|---|---|---|
| L0 | No Measurement | Chỉ nhìn lượng dùng AI |
| L1 | Basic Logs | Lưu AI result và cost theo PR |
| L2 | Outcome Feedback | Phân loại valid/false positive |
| L3 | Offline Eval | Dataset eval trước khi đổi prompt/model |
| L4 | Trace Observability | Có trace của agent/tool/context |
| L5 | Continuous Optimization | Từ metrics tự động quay cải thiện về chuẩn SDD |

Mục tiêu:

```text
Team thông thường: L2〜L3
Vận hành high-risk AI review: L4
Vận hành AI QA Gate nghiêm túc: L5
```

---

# Appendix G. Red Team Evaluation

Kết quả AI security red team của 45 cũng được đánh giá liên tục trong 49.

```text
Scenarios:
- prompt injection in README
- malicious PR comment
- tool output injection
- poisoned RAG document
- MCP server over-permission
- secret exfiltration attempt
- fake test result in log
- AI asked to bypass policy
```

Đánh giá:

```text
- attack detected
- unsafe instruction ignored
- tool permission blocked
- human escalation triggered
- trace captured
- failure mode updated
```

---

# Appendix H. AI System Release Checklist

Kiểm tra trước khi áp dụng thay đổi prompt/model/tool/policy vào production.

```text
- Change Record exists
- Offline eval passed
- No critical regression
- Cost impact estimated
- Security review done if tool/context changed
- Trace redaction still works
- Rollback prompt/model version available
- Shadow rollout completed for high-risk change
- Monitoring alerts configured
```

---

# Appendix I. Ví dụ cải thiện Pack bằng 49

```text
Observation:
  Security Reviewer false positive rate cao, 60%.

Diagnosis:
  Đưa quá nhiều all files context, suy đoán khi không có chứng minh auth boundary.

Change:
  Giới hạn 46 Security Context Pack vào auth routes + service permission + tests.
  43 cấm High severity nếu không có evidence.

Evaluation:
  Với golden security dataset, giữ valid finding và cải thiện false positive 25%.

Promotion:
  Cập nhật prompt 42 Security Agent.
  Phản ánh vào 31 Context Loading.
  Cập nhật 34 Security Pattern.
```

---

# Appendix J. Executive Reporting Template

```md
# AI-driven SDD Executive Summary

## Period

## Business Impact
- Delivery impact:
- Quality impact:
- Security impact:
- Cost impact:

## Key Metrics
| Metric | Current | Previous | Trend | Target |
|---|---:|---:|---:|---:|

## Major Wins

## Major Risks

## Decisions Needed

## Next Quarter Focus
```

---

# Appendix K. Engineering Improvement Backlog

Kết quả của 49 được đưa vào improvement backlog.

```md
# AI Development Improvement Backlog

| ID | Source Metric | Problem | Proposed Fix | Owner | Priority | Due |
|---|---|---|---|---|---|---|
| AI-001 | false_positive_rate | Security FP high | tighten evidence rule | Sec Lead | High | 2026-06-01 |
| AI-002 | cache_hit_rate | prompt prefix unstable | static prefix refactor | AI Platform | Medium | 2026-06-10 |
| AI-003 | missed_bug | FE/BE validation drift | add contract eval case | QA Lead | High | 2026-06-05 |
```

---

# Appendix L. Roadmap triển khai tối thiểu

```text
Week 1:
  - Lưu PR Review Record
  - Ghi token/cost
  - Thêm phân loại human feedback

Week 2:
  - Golden PR Dataset 20 case
  - offline eval trước khi đổi prompt
  - bắt đầu monthly review

Month 1:
  - dashboard hiệu quả theo agent
  - RAG eval
  - cost per valid finding

Quarter 1:
  - trace observability
  - shadow eval
  - AI system change control
  - continuous optimization loop
```

---

# Appendix. Dành cho người mới: Quy trình thực thi pack này và prompt copy-paste

> Appendix này là “execution wrapper” để cả người mới cũng có thể đưa Evaluation / Observability / Continuous Optimization được định nghĩa trong phần chính vào thực tế.  
> Không thay đổi nội dung phần chính. Hãy dùng phần chính như “thiết kế spec cho đánh giá hệ thống phát triển AI, trace, metrics, dashboard, optimization loop”, và dùng Appendix này như quy trình “đo cái gì đầu tiên, ghi nhận ra sao, và đưa vào cải thiện hằng tháng như thế nào”.

---

## A-0. Quy tắc tuyệt đối cần tuân thủ đầu tiên

49 là Advanced Option để đo liệu vận hành SDD có tích hợp AI có thật sự cải thiện chất lượng, tốc độ, an toàn và hiệu quả chi phí hay không.  
Người mới không được xem 49 là “việc tạo dashboard”, mà phải xem nó là **vòng lặp cải thiện liên tục đo valid finding, missed bug, false positive, cost, latency và niềm tin của con người, thay vì đưa AI vào rồi kết thúc**.

```text
1. Không lấy số comment AI, số ký tự sinh ra, số Agent làm success metric.
2. Trước tiên chỉ yêu cầu đưa ra Evaluation / Observability Plan.
3. Cho đến khi con người phê duyệt Plan, không thay đổi nền tảng đo lường, công khai dashboard, đổi policy, đổi model/prompt.
4. Không nhắm đến full configuration ngay từ đầu. Tách tối thiểu, tiêu chuẩn, đầy đủ.
5. Có thể phân loại valid finding, false positive, missed bug, accepted risk, human override.
6. Đo cost per valid finding, review latency, PR tồn đọng, developer trust.
7. Không thu trace/logs khi chưa quyết định privacy, retention, redaction.
8. Quản lý thay đổi model / prompt / rule / context / tool / agent bằng AI System Change Record và Eval.
9. Không dùng metrics để đổ lỗi cá nhân. Trả về workflow improvement, prompt improvement, context improvement, tool improvement.
10. Cuối cùng tạo improvement feedback cho 29/34/44/47 và Monthly Review.
```

Nơi lưu cơ bản trong Appendix này như sau.

```text
Artifact riêng của pack:
docs/changes/{{TICKET}}/49-evaluation-observability/

Ứng viên nâng cấp thành vận hành liên tục:
docs/changes/{{TICKET}}/49-evaluation-observability/promotion-candidates.md

Feedback cho 29/34/44/47:
docs/changes/{{TICKET}}/49-evaluation-observability/29-feedback.md
docs/changes/{{TICKET}}/49-evaluation-observability/34-knowledge-candidates.md
docs/changes/{{TICKET}}/49-evaluation-observability/44-optimization-feedback.md
docs/changes/{{TICKET}}/49-evaluation-observability/47-gate-feedback.md

Ứng viên đăng ký vào 33 Artifact Governance:
docs/changes/{{TICKET}}/49-evaluation-observability/33-registration.md
```

Tư tưởng quan trọng:

```text
Mục tiêu của 49 không phải là “tăng lượng dùng AI”,
mà là làm cho AI thật sự tăng chỉ trích hữu ích, giảm bỏ sót, và làm cho chi phí/lượng tải có thể giải thích được.
```

---

## A-1. Khi nào dùng pack này

### Trường hợp nên dùng

```text
- Vận hành liên tục AI review, hỗ trợ implement bằng AI, PR Gate, Multi-Agent, RAG, Tool-Grounded judgment
- Muốn đo valid finding rate, false positive rate, missed issue rate, review time, cost của AI
- Muốn đo hiệu quả 47 Automated PR Review / AI QA Gate
- Muốn xác minh việc cắt giảm ở 44 Token Optimization không làm giảm chất lượng
- Muốn đo retrieval miss, context quality, compression loss của 46 RAG
- Muốn so sánh hiệu quả của 42 Agent hoặc Model Routing
- Muốn theo dõi tính hợp lý của Veto và Accepted Risk trong 43 Tool-Grounded
- Muốn nâng cấp 29 Failure Mode và 34 Knowledge thành evaluation dataset
- Muốn tạo tài liệu giải thích cho monthly improvement meeting, executive reporting, AI Governance Board
```

### Trường hợp có thể lightweight

```text
- Vẫn đang ở PoC và chỉ muốn thu minimum metrics
- Số PR hoặc số lần dùng AI ít, bảng monthly là đủ thay vì dashboard
- Chỉ review retrospective theo từng ticket
- Đã được 28 phán định vận hành nhẹ
- Không có trace platform nghiêm túc và muốn bắt đầu bằng manual record
```

Ngay cả khi lightweight, tối thiểu vẫn giữ:

```text
- cost hoặc token theo AI run / PR
- AI decision
- human feedback
- phân loại valid / false positive / missed bug
- monthly summary
- improvement backlog
```

### Trường hợp không dùng, hoặc cần quay lại pack khác trước

```text
- Đối tượng AI workflow không rõ
- Không thể liên kết trace_id / run_id / PR ID / ticket ID
- Chưa có chính sách privacy / retention / redaction
- Không có cách thu thập human feedback
- Chưa quyết định ai phán định valid finding hoặc false positive
- Metrics owner không rõ
- Định quan sát sensitive logs hoặc production data mà chưa có 45 Security Governance
```

---

## A-2. Biến cần điền trước khi copy-paste

```text
{{TICKET}}:
{{FEATURE_NAME}}:
{{BRANCH_NAME}}:
{{PACK_NO}}: 49
{{PACK_NAME}}: Evaluation Observability and Continuous Optimization Option
{{PACK_SLUG}}: evaluation-observability
{{SCOPE_NOTE}}:
{{RISK_LEVEL}}: Low / Medium / High / Critical
{{SDD_MODE}}: M0 / M1 / M2 / M3 / M4 / M5 / MX
{{TIMEBOX}}:
{{HUMAN_OWNER}}:
{{METRICS_OWNER}}:
{{REVIEWER}}:
{{EVALUATION_SCOPE}}:
{{OBSERVABILITY_LEVEL}}: Minimal / Standard / Full
{{TRACE_ID_RULE}}:
{{PRIMARY_METRICS}}:
{{BASELINE_PERIOD}}:
{{EVAL_DATASET_SOURCE}}:
{{DASHBOARD_TARGETS}}:
{{RETENTION_POLICY}}:
{{MONTHLY_REVIEW_OWNER}}:
```

Ví dụ điền:

```text
{{TICKET}}: ABC-123
{{FEATURE_NAME}}: Thêm người dùng bằng email mời
{{BRANCH_NAME}}: feature/ABC-123-invite-user
{{SCOPE_NOTE}}: Đo hiệu quả của 47 PR Gate và 43 Tool-Grounded
{{RISK_LEVEL}}: Medium
{{SDD_MODE}}: M3
{{TIMEBOX}}: 90 phút đến bản nháp Evaluation Plan, Metrics Catalog, Monthly Review
{{HUMAN_OWNER}}: Tech Lead
{{METRICS_OWNER}}: QA Lead / AI Platform
{{EVALUATION_SCOPE}}: AI PR Review, Security Review, Tool-Grounded Gate
{{OBSERVABILITY_LEVEL}}: Bắt đầu từ Minimal
{{TRACE_ID_RULE}}: ticket_id + pr_id + ai_run_id + tool_run_id
{{PRIMARY_METRICS}}: valid finding rate, false positive rate, missed bug, review latency, cost per valid finding
{{BASELINE_PERIOD}}: 4 tuần gần nhất
{{EVAL_DATASET_SOURCE}}: PR quá khứ, review findings, incidents, 29 Failure Mode
{{DASHBOARD_TARGETS}}: Engineering, Security, AI Platform
{{RETENTION_POLICY}}: 90 ngày, bắt buộc redaction secret/PII
{{MONTHLY_REVIEW_OWNER}}: QA Lead
```

---

## A-3. Input đầu tiên cần cho AI đọc

### Input dùng chung

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
@docs/changes/{{TICKET}}/29-failure-mode-learning/failure-mode-index.md
@docs/changes/{{TICKET}}/34-project-knowledge/ai-context-pack.md
@docs/changes/{{TICKET}}/42-multi-agent-orchestrator/agent-outputs.md
@docs/changes/{{TICKET}}/43-tool-grounded-verification/consensus-record.md
@docs/changes/{{TICKET}}/44-token-cost-control/token-cost-audit.md
@docs/changes/{{TICKET}}/45-full-security-agentic-ai/security-signoff.md
@docs/changes/{{TICKET}}/46-rag-codemap-context-compression/retrieval-eval.md
@docs/changes/{{TICKET}}/47-automated-pr-review-qa-gate/pr-review-record.md
@docs/changes/{{TICKET}}/47-automated-pr-review-qa-gate/qa-gate-record.md
@docs/changes/{{TICKET}}/48-parallel-worktree-refactoring/49-metrics-handoff.md
```

### Dữ liệu ứng viên cần thu thập ban đầu

```text
- PR ID / ticket ID / branch / author / reviewer
- AI run ID / model / prompt version / rules version / context pack version
- tool run ID / CI status / test result / security scan result
- AI findings / human feedback / final disposition
- valid finding / false positive / duplicate / style-only / missed bug
- accepted risk / human override / veto
- token / cost / latency
- review time / PR lead time / rerun count
- production outcome / escaped defect / incident
```

Lưu ý:

```text
- Dùng để cải thiện workflow, không phải đánh giá cá nhân
- Không để secret, PII, customer data, raw production log trong trace
- Quyết định trước độ chi tiết và retention khi đưa lên dashboard
- Nếu dùng LLM-as-Judge, vẫn phải có human calibration và ground truth
```

---

## A-4. Artifact cần tạo/cập nhật

```text
Artifact bắt buộc:
- docs/changes/{{TICKET}}/49-evaluation-observability/README.md
- docs/changes/{{TICKET}}/49-evaluation-observability/evaluation-observability-plan.md
- docs/changes/{{TICKET}}/49-evaluation-observability/trace-schema.md
- docs/changes/{{TICKET}}/49-evaluation-observability/metrics-catalog.md
- docs/changes/{{TICKET}}/49-evaluation-observability/baseline-measurement.md
- docs/changes/{{TICKET}}/49-evaluation-observability/evaluation-dataset-plan.md
- docs/changes/{{TICKET}}/49-evaluation-observability/golden-pr-dataset.md
- docs/changes/{{TICKET}}/49-evaluation-observability/eval-run-record.md
- docs/changes/{{TICKET}}/49-evaluation-observability/dashboard-plan.md
- docs/changes/{{TICKET}}/49-evaluation-observability/dashboard-review.md
- docs/changes/{{TICKET}}/49-evaluation-observability/optimization-backlog.md
- docs/changes/{{TICKET}}/49-evaluation-observability/monthly-review.md
- docs/changes/{{TICKET}}/49-evaluation-observability/retention-policy.md
- docs/changes/{{TICKET}}/49-evaluation-observability/review.md
```

Artifact tạo khi cần:

```text
- docs/changes/{{TICKET}}/49-evaluation-observability/ai-system-change-record.md
- docs/changes/{{TICKET}}/49-evaluation-observability/ai-regression-gate.md
- docs/changes/{{TICKET}}/49-evaluation-observability/agent-scorecard.md
- docs/changes/{{TICKET}}/49-evaluation-observability/model-routing-evaluation.md
- docs/changes/{{TICKET}}/49-evaluation-observability/retrieval-eval-record.md
- docs/changes/{{TICKET}}/49-evaluation-observability/token-optimization-experiment.md
- docs/changes/{{TICKET}}/49-evaluation-observability/ai-qa-gate-scorecard.md
- docs/changes/{{TICKET}}/49-evaluation-observability/missed-bug-rca.md
- docs/changes/{{TICKET}}/49-evaluation-observability/false-positive-analysis.md
- docs/changes/{{TICKET}}/49-evaluation-observability/executive-summary.md
- docs/changes/{{TICKET}}/49-evaluation-observability/33-registration.md
- docs/changes/{{TICKET}}/49-evaluation-observability/29-feedback.md
- docs/changes/{{TICKET}}/49-evaluation-observability/34-knowledge-candidates.md
- docs/changes/{{TICKET}}/49-evaluation-observability/44-optimization-feedback.md
- docs/changes/{{TICKET}}/49-evaluation-observability/47-gate-feedback.md
- docs/changes/{{TICKET}}/49-evaluation-observability/promotion-candidates.md
```

Phản ánh vào Core artifact:

```text
report.md:
- hiệu quả hỗ trợ AI, kết quả review, rủi ro còn lại, cải thiện tiếp theo

review-checklist.md:
- phân loại valid / false positive / missed bug, ghi human feedback

test-plan.md:
- eval dataset, AI regression, retrieval eval, red team eval

standards / rules candidates:
- định nghĩa metrics, phân loại feedback, quản lý thay đổi prompt, quản lý thay đổi model
```

---

## A-5. Quy trình thực hiện

```text
Step 1. Dán prompt bắt đầu phase chung của 22
Step 2. Dán prompt khởi động 49 và chỉ yêu cầu Evaluation / Observability Plan
Step 3. Kiểm tra Plan có evaluation target, Trace ID, metrics, privacy, owner, Stop/Ask hay không
Step 4. Sau khi phê duyệt Plan, tạo Trace Schema
Step 5. Tạo Metrics Catalog
Step 6. Tạo Baseline Measurement
Step 7. Tạo Evaluation Dataset Plan và Golden PR Dataset
Step 8. Tạo Eval Run Record
Step 9. Tạo Dashboard Plan / Dashboard Review
Step 10. Tạo Optimization Backlog
Step 11. Tạo Monthly Review
Step 12. Nếu cần, tạo AI System Change Record / Regression Gate
Step 13. Tạo Feedback cho 29/34/44/47
Step 14. Dán prompt review và phán định hoàn tất 49
```

### Minimum Metrics cần đo đầu tiên

```text
Quality:
- valid finding count
- false positive count
- missed bug count
- duplicate / noise count

Safety:
- security high detected
- secret leakage prevented
- human override count
- accepted risk count

Efficiency:
- review latency
- PR lead time
- rerun count

Cost:
- token per PR
- cost per PR
- cost per valid finding

Trust:
- human accepted AI finding
- human rejected AI finding
- reviewer satisfaction note
```

---

## A-6. Prompt khởi động dùng để copy-paste

```text
Bạn là người hỗ trợ thực thi “49 Evaluation / Observability / Continuous Optimization Option” của SDD Ver.04.
Từ bây giờ, hãy thiết kế đánh giá và cải thiện liên tục cho hỗ trợ phát triển AI, AI review, PR Gate, RAG và Tool-Grounded judgment của {{TICKET}}（{{FEATURE_NAME}}）.

【Quy tắc quan trọng nhất】
- Không ngay lập tức thay đổi nền tảng đo lường, công khai dashboard, đổi policy, đổi model/prompt.
- Trước tiên chỉ trình bày Evaluation / Observability Plan.
- Cho đến khi tôi phê duyệt Plan, không tạo/cập nhật file hay thay đổi setting.
- Không dùng số lượng comment AI, lượng nội dung sinh ra, số Agent làm success metric.
- Tập trung vào valid finding, false positive, missed bug, cost per valid finding, review latency, human trust.
- Không đưa secret, PII, customer data, raw production log vào trace hoặc dashboard.
- Nếu privacy, redaction, retention, owner không rõ thì Stop/Ask.
- Quản lý thay đổi model / prompt / rule / context / tool / agent bằng AI System Change Record và Eval.

【Tiền đề lần này】
- Ticket: {{TICKET}}
- Feature: {{FEATURE_NAME}}
- Branch: {{BRANCH_NAME}}
- Scope: {{SCOPE_NOTE}}
- Risk Level: {{RISK_LEVEL}}
- SDD Mode: {{SDD_MODE}}
- Timebox: {{TIMEBOX}}
- Human Owner: {{HUMAN_OWNER}}
- Metrics Owner: {{METRICS_OWNER}}
- Evaluation Scope: {{EVALUATION_SCOPE}}
- Observability Level: {{OBSERVABILITY_LEVEL}}
- Trace ID Rule: {{TRACE_ID_RULE}}
- Primary Metrics: {{PRIMARY_METRICS}}
- Baseline Period: {{BASELINE_PERIOD}}
- Eval Dataset Source: {{EVAL_DATASET_SOURCE}}
- Dashboard Targets: {{DASHBOARD_TARGETS}}
- Retention Policy: {{RETENTION_POLICY}}
- Monthly Review Owner: {{MONTHLY_REVIEW_OWNER}}

【Plan bắt buộc bao gồm】
1. Có áp dụng 49 hay không
2. AI workflow cần đánh giá
3. Thiết kế Trace ID / Run ID / Artifact ID
4. Minimum Metrics và Standard Metrics
5. privacy / redaction / retention
6. baseline measurement
7. evaluation dataset / golden PR dataset
8. dashboard / monthly review
9. optimization backlog
10. Điều kiện Stop/Ask
11. Feedback cho 29/34/44/47

Trước tiên chỉ trình bày Plan. Chưa chỉnh sửa file hay setting.
```

---

## A-7. Prompt phê duyệt Plan dùng để copy-paste

```text
Tôi phê duyệt 49 Evaluation / Observability Plan.
Hãy tạo/cập nhật artifact của 49 theo đúng quy trình đã đề xuất.

【Quy tắc thực thi】
- Trình bày nơi lưu và tóm tắt từng artifact.
- Tách minimum configuration, standard configuration, full configuration.
- Metrics phải có định nghĩa, công thức tính, owner, nguồn thu thập, tần suất cập nhật và lưu ý.
- Trong Trace Schema, hãy liên kết ticket_id, pr_id, ai_run_id, tool_run_id, prompt/rule/context version.
- Làm rõ tiêu chí phân loại valid finding / false positive / missed bug / accepted risk / human override.
- Ghi rõ privacy, redaction, retention trong retention-policy.md.
- Ghi improvement proposal vào optimization-backlog.md kèm owner và priority.
- Tách feedback trả về 29/34/44/47.
- Nội dung muốn nâng cấp thành dashboard thường trực hoặc standard metrics thì ghi vào promotion-candidates.md, không cập nhật trực tiếp.
- Cuối cùng tự phán định completion gate.
```

---

## A-8. Prompt Monthly Review dùng để copy-paste

```text
Bạn là AI Development Optimization Reviewer của SDD Ver.04.
Hãy tạo Monthly Review cho hỗ trợ phát triển AI trong khoảng thời gian sau.

【Khoảng thời gian】
Ghi {{BASELINE_PERIOD}} hoặc tháng mục tiêu vào đây

【Đọc】
@docs/changes/{{TICKET}}/49-evaluation-observability/metrics-catalog.md
@docs/changes/{{TICKET}}/49-evaluation-observability/eval-run-record.md
@docs/changes/{{TICKET}}/49-evaluation-observability/dashboard-review.md
@docs/changes/{{TICKET}}/49-evaluation-observability/optimization-backlog.md
@docs/changes/{{TICKET}}/47-automated-pr-review-qa-gate/feedback-record.md
@docs/changes/{{TICKET}}/44-token-cost-control/token-cost-audit.md
@docs/changes/{{TICKET}}/46-rag-codemap-context-compression/retrieval-eval.md
@docs/changes/{{TICKET}}/29-failure-mode-learning/failure-mode-index.md

【Góc nhìn output】
- Top wins
- Top problems
- xu hướng valid finding / false positive / missed bug
- cost per valid finding
- review latency / PR lead time
- security / safety events
- context / RAG quality
- ứng viên cải thiện agent / model / prompt / rule
- action cụ thể trả về 29/34/44/47
- KPI và owner của tháng tới

【Output】
docs/changes/{{TICKET}}/49-evaluation-observability/monthly-review.md
```

---

## A-9. Prompt review artifact và phán định hoàn tất dùng để copy-paste

```text
Bạn là Evaluation / Observability Reviewer độc lập của SDD Ver.04.
Hãy review các artifact 49 sau và phán định có thể hoàn tất pack này hay không.

【Đối tượng review】
@docs/changes/{{TICKET}}/49-evaluation-observability/
@docs/changes/{{TICKET}}/29-failure-mode-learning/
@docs/changes/{{TICKET}}/34-project-knowledge/
@docs/changes/{{TICKET}}/44-token-cost-control/
@docs/changes/{{TICKET}}/47-automated-pr-review-qa-gate/

【Góc nhìn review】
1. AI workflow cần đánh giá có rõ không
2. Có liên kết Trace ID / Run ID / Artifact ID không
3. Minimum Metrics đã được định nghĩa chưa
4. Có tiêu chí phân loại valid finding / false positive / missed bug không
5. Có thể đo cost per valid finding, review latency, human trust không
6. Privacy / redaction / retention đã được định nghĩa chưa
7. Có Evaluation Dataset hoặc Golden PR Dataset bản đầu chưa
8. Có thể kiểm tra liên tục bằng Dashboard hoặc Monthly Review không
9. Optimization Backlog có owner và priority không
10. Cải thiện có quay lại 29/34/44/47 không

【Output format】
- Verdict: PASS / NEEDS_UPDATE / BLOCKED
- Findings
  - [Blocker]
  - [Major]
  - [Minor]
- Missing metrics
- Privacy / retention risk
- Evaluation bias risk
- Dashboard gap
- Required human decisions
- Required artifact updates
- Required 29/34/44/47 feedback
- Final completion gate checklist
- Next action
```

---

## A-10. Prompt trả về sửa lại dùng để copy-paste

```text
Dựa trên các review finding dưới đây, hãy sửa artifact Evaluation / Observability của 49.

【Quy tắc sửa】
- Trước khi bắt đầu, hãy diễn giải ý định của finding trong 1 dòng.
- Liệt kê trước các artifact bị ảnh hưởng.
- Xử lý theo thứ tự Blocker / Major / Minor.
- Nếu định nghĩa metrics mơ hồ, hãy thêm công thức tính, owner, nguồn thu thập, tần suất cập nhật.
- Thiếu privacy / retention / redaction là ưu tiên sửa cao nhất.
- Khi thường trực hóa dashboard hoặc metrics, không cập nhật trực tiếp; ghi ứng viên vào promotion-candidates.md.
- Tách feedback cho 29/34/44/47.
- Sau khi sửa, ghi kết quả xử lý vào review.md.

【Review findings】
Dán finding vào đây
```

---

## A-11. Điều kiện Stop/Ask

```text
- Đối tượng AI workflow, owner, metrics owner không rõ
- Không thể liên kết trace_id / run_id / PR ID / ticket ID
- Cần đưa secret, PII, customer data, raw production log vào trace hoặc dashboard
- Chưa có chính sách privacy, redaction, retention
- Chưa có cách thu thập human feedback hoặc người phán định
- Không thể phân loại valid finding / false positive / missed bug
- Metrics có nguy cơ bị dùng cho đánh giá cá nhân hoặc trừng phạt
- Phạm vi công khai dashboard hoặc quyền truy cập không rõ
- Định áp dụng model / prompt / rule / tool change vào production mà không Eval
- Thiết kế chỉ coi cost reduction là thành công và không nhìn chất lượng suy giảm
```

---

## A-12. Completion Gate

```text
- [ ] Đã ghi lý do áp dụng hoặc lightweight 49
- [ ] Có Evaluation / Observability Plan
- [ ] Có Trace Schema
- [ ] Có Metrics Catalog
- [ ] Minimum Metrics đã được định nghĩa
- [ ] Có tiêu chí phân loại valid finding / false positive / missed bug
- [ ] Có baseline measurement, hoặc kế hoạch thu thập
- [ ] Có Evaluation Dataset Plan hoặc Golden PR Dataset bản đầu
- [ ] Có Eval Run Record, hoặc kế hoạch run đầu tiên
- [ ] Có Dashboard Plan hoặc Dashboard Review
- [ ] Optimization Backlog có owner và priority
- [ ] Định nghĩa vận hành Monthly Review
- [ ] Ghi rõ privacy / redaction / retention
- [ ] Tách Feedback cho 29/34/44/47
- [ ] Không còn Blocker
```

---

## A-13. Điểm đi tiếp theo

```text
- Tái phát false positive / missed bug / recurring issue → 29 Failure Mode
- Tri thức hóa prompt, Context Pack, review pattern tốt → 34 Project Knowledge
- cost per valid finding xấu → 44 Token Optimization
- Điều chỉnh noise hoặc block condition của PR Gate → 47 Automated PR Review / AI QA Gate
- Retrieval miss hoặc compression loss nhiều → 46 RAG / CodeMap / Context Compression
- Cải thiện Security event hoặc Red Team result → 45 Security Governance
- Cải thiện Tool evidence hoặc Veto policy → 43 Tool-Grounded Verification
- Hiệu quả Agent kém → xem lại cấu hình Agent của 42 Multi-Agent Orchestrator
```
