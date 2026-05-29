**Mục lục**
- [10_BVN-SDD_GuideLine](#10_bvn-sdd_guideline)
  - [0. Trước khi đọc hướng dẫn này](#0-trước-khi-đọc-hướng-dẫn-này)
  - [1. Toàn cảnh SDD V04](#1-toàn-cảnh-sdd-v04)
  - [2. Dành cho người mới: nên đọc từ đâu trước](#2-dành-cho-người-mới-nên-đọc-từ-đâu-trước)
  - [3. Thuật ngữ nền tảng: từ những điều cơ bản nhất](#3-thuật-ngữ-nền-tảng-từ-những-điều-cơ-bản-nhất)
  - [4. Tư tưởng và bối cảnh được đưa vào SDD V04](#4-tư-tưởng-và-bối-cảnh-được-đưa-vào-sdd-v04)
  - [5. Luồng cơ bản của SDD V04](#5-luồng-cơ-bản-của-sdd-v04)
  - [6. Danh sách file và thông tin đo thực tế](#6-danh-sách-file-và-thông-tin-đo-thực-tế)
  - [7. Chế độ áp dụng và tiêu chí phán đoán](#7-chế-độ-áp-dụng-và-tiêu-chí-phán-đoán)
  - [8. Hướng dẫn chi tiết cho từng file](#8-hướng-dẫn-chi-tiết-cho-từng-file)
  - [9. So sánh các nhóm file: nhìn giống nhau nhưng khác nhau](#9-so-sánh-các-nhóm-file-nhìn-giống-nhau-nhưng-khác-nhau)
  - [10. Lộ trình đưa vào dự án](#10-lộ-trình-đưa-vào-dự-án)
  - [11. Ví dụ áp dụng theo loại案件 / loại việc](#11-ví-dụ-áp-dụng-theo-loại案件--loại-việc)
  - [12. Phiếu assessment khi đưa vào áp dụng](#12-phiếu-assessment-khi-đưa-vào-áp-dụng)
  - [13. Ưu điểm và nhược điểm](#13-ưu-điểm-và-nhược-điểm)
  - [14. Ví dụ cấu trúc thư mục tiêu chuẩn khi dùng tại hiện trường](#14-ví-dụ-cấu-trúc-thư-mục-tiêu-chuẩn-khi-dùng-tại-hiện-trường)
  - [15. Những lỗi thường gặp và cách xử lý](#15-những-lỗi-thường-gặp-và-cách-xử-lý)
  - [16. Cách dùng trong đào tạo và training](#16-cách-dùng-trong-đào-tạo-và-training)
  - [17. FAQ](#17-faq)
  - [18. Chính sách vận hành khuyến nghị cho BVN-SDD](#18-chính-sách-vận-hành-khuyến-nghị-cho-bvn-sdd)
  - [19. Chỉ số thành công](#19-chỉ-số-thành-công)
  - [20. Thông điệp cuối cùng](#20-thông-điệp-cuối-cùng)
  - [21. Cách sử dụng chi tiết theo vai trò](#21-cách-sử-dụng-chi-tiết-theo-vai-trò)
  - [22. Ý nghĩa và cách tạo từng artifact](#22-ý-nghĩa-và-cách-tạo-từng-artifact)
  - [23. Ví dụ: tiến hành một thay đổi API thông thường bằng SDD](#23-ví-dụ-tiến-hành-một-thay-đổi-api-thông-thường-bằng-sdd)
  - [24. Ví dụ: tiến hành thay đổi logic phân quyền bằng SDD](#24-ví-dụ-tiến-hành-thay-đổi-logic-phân-quyền-bằng-sdd)
  - [25. Ví dụ: tiến hành refactor quy mô lớn bằng SDD](#25-ví-dụ-tiến-hành-refactor-quy-mô-lớn-bằng-sdd)
  - [26. Bộ checklist](#26-bộ-checklist)
  - [27. Mô hình trưởng thành](#27-mô-hình-trưởng-thành)
  - [28. Bảng thuật ngữ chi tiết](#28-bảng-thuật-ngữ-chi-tiết)
  - [29. Quan hệ giữa hướng dẫn này và các file khác](#29-quan-hệ-giữa-hướng-dẫn-này-và-các-file-khác)
  - [30. Tóm tắt](#30-tóm-tắt)
  - [31. Giải thích chi tiết về Harness Engineering](#31-giải-thích-chi-tiết-về-harness-engineering)
  - [32. Decision tree chi tiết để chọn file](#32-decision-tree-chi-tiết-để-chọn-file)
  - [33. Ma trận phán đoán đưa vào áp dụng chi tiết](#33-ma-trận-phán-đoán-đưa-vào-áp-dụng-chi-tiết)
  - [34. Ví dụ RACI khi đưa vào áp dụng](#34-ví-dụ-raci-khi-đưa-vào-áp-dụng)
  - [35. Kế hoạch triển khai 30 ngày](#35-kế-hoạch-triển-khai-30-ngày)
  - [36. Đào sâu các góc nhìn review chất lượng](#36-đào-sâu-các-góc-nhìn-review-chất-lượng)
  - [37. 10 nguyên tắc cần tuân thủ khi vận hành SDD V04](#37-10-nguyên-tắc-cần-tuân-thủ-khi-vận-hành-sdd-v04)
  - [38. Cuối cùng: cách dùng hướng dẫn này](#38-cuối-cùng-cách-dùng-hướng-dẫn-này)

# 10_BVN-SDD_GuideLine

| Hạng mục | Nội dung |
|---|---|
| Tên tài liệu | 10_BVN-SDD_GuideLine.md |
| Gói đối tượng | SDD-導入パック_V04.2.zip |
| File đối tượng | 11 và 21〜29・31〜34 Core / Extension / Operations, 40〜49 Advanced Options |
| Ngày tạo | 2026-05-16 |
| Độc giả giả định | Người mới với AI-driven development / specification-driven development, developer, reviewer, PM/PL, QA, Security, SRE, người phụ trách thúc đẩy ứng dụng AI |
| Mục đích tài liệu | Cung cấp hướng dẫn tổng hợp để hiểu SDD V04 một cách xuyên suốt: tư tưởng, thuật ngữ, cấu trúc, quyết định áp dụng, cách dùng từng file và các bước đưa vào hiện trường |

---

## 0. Trước khi đọc hướng dẫn này

`10_BVN-SDD_GuideLine.md` là hướng dẫn tổng hợp để đưa vào áp dụng, giải thích, đào tạo và vận hành tại hiện trường bộ tài liệu Markdown nằm trong `SDD-導入パック_V04.2.zip`.

SDD V04 không chỉ là một bộ prompt. Nó cũng không phải tập hợp các mẹo nhỏ để bắt AI viết code. SDD V04 là một “hệ điều hành phát triển” giúp AI hỗ trợ phát triển phần mềm theo cách an toàn, chính xác cao, có tính tái lập và có thể audit.

Hướng dẫn này trả lời các câu hỏi như sau.

- SDD là gì? Nó khác AI-driven development như thế nào?
- Vì sao cần những artifact như Spec Pack, Impl Plan, Review Checklist, Test Results?
- Các file 11 và 21〜29・31〜49 tồn tại để làm gì?
- Với từng loại案件 / công việc, nên dùng file nào?
- Người mới nên bắt đầu từ đâu?
- Advanced Options nhóm 40 nên dùng trong những trường hợp nào?
- Nên kết hợp nâng cao độ chính xác AI, giảm token, security, RAG, Multi-Agent, PR Gate và Observability như thế nào?

Một tiền đề quan trọng là SDD V04 không phải để “làm tất cả mọi thứ trong mọi lần”. Số lượng file nhiều không phải để ép mọi案件 phải dùng quy trình nặng, mà để có thể chọn tiêu chuẩn cần thiết theo mức độ phức tạp và rủi ro của案件.

---

## 1. Toàn cảnh SDD V04

SDD V04 được chia thành 4 lớp lớn.

```text
ReadMe	
  11: README nhóm 20
Core Pack
  21: Quy trình cụ thể
  22: Bộ prompt
Extension Pack
  23: Source Intelligence
  24: Review / TestCode
  25: Security Gate / CI Security
  26: FE/BE Contract
  27: Microservice / MultiRepo
  28: Applicability / RightSizing
  29: Failure Mode / Continuous Learning
Operations Pack
  31: Context Loading / Exclusion
  32: Long Context / Strategic Compact
  33: Artifact Governance / Traceability
  34: Project Knowledge / Pattern Library
Advanced Options
  40: Advanced Options Overview
  41: Heavy Source Analysis
  42: Multi-Model / Multi-Agent / Orchestrator
  43: Tool-Grounded Verification / Consensus
  44: Token Optimization / Cost Control
  45: Full Security / Agentic AI Governance
  46: RAG / Code Map / Context Compression
  47: Automated PR Review / AI QA Gate
  48: Parallel Worktree / Large Refactoring
  49: Evaluation / Observability / Continuous Optimization
```

Nếu ví cấu trúc này với xây nhà, 21・22 là “quy trình xây dựng và cách dùng công cụ”, 23〜29 là “khảo sát nền móng, chống động đất, điện, nước, quản lý chất lượng”, 11・31〜34 là “quản lý công trường, quản lý bản vẽ, bàn giao, quản lý tri thức”, còn 40〜49 là “thiết kế nâng cao, audit và thiết bị tự động hóa dùng cho案件 có độ khó cao như cao ốc hay bệnh viện”.

---

## 2. Dành cho người mới: nên đọc từ đâu trước

Người lần đầu tiếp xúc với SDD V04 không cần đọc toàn bộ file ngay từ đầu. Thứ tự sau là an toàn nhất.

### 2.1 Lộ trình ngắn nhất

| Thứ tự | File cần đọc | Mục đích |
|---:|---|---|
| 1 | File này `10_BVN-SDD_GuideLine.md` | Hiểu toàn cảnh và thuật ngữ |
| 2 | `11_SDD_20s-Pack-README-and-Integration-Guide` | Hiểu bản đồ của 21〜29・31〜34 |
| 3 | `21_SDD_1st-Step-Pack_02_具体的手順_Core` | Hiểu các Phase tiêu chuẩn của SDD |
| 4 | `22_SDD_1st-Step-Pack_03_プロンプト集_Core` | Hiểu cách yêu cầu AI |
| 5 | `28_SDD_Applicability-and-RightSizing` | Quyết định案件 của mình cần làm đến mức nào |

### 2.2 Bộ cơ bản cho developer

Developer thông thường chỉ cần bắt đầu với bộ sau là đủ.

```text
21 + 22 + 23 + 24 + 28 + 31 + 33
```

Đây là bộ tối thiểu dùng được trong thực tế, gồm quy trình, prompt, phân tích source, review/test, quyết định mức áp dụng, quản lý context và quản lý artifact.

### 2.3 Bộ cơ bản cho PM/PL

Người chịu trách nhiệm dự án hoặc thúc đẩy triển khai đọc bộ sau.

```text
10 + 11 + 28 + 33 + 49
```

Với PM/PL, điều cần thiết không phải prompt chi tiết, mà là quyết định áp dụng, quản lý artifact và đo hiệu quả.

### 2.4 Bộ cơ bản cho phụ trách security

```text
25 + 31 + 33 + 43 + 45 + 47
```

Bộ này tập trung vào Security Gate, loại trừ context, chứng tích, kiểm chứng bằng tool, quyền hạn của Agentic AI và PR Gate.

### 2.5 Bộ cơ bản cho案件 phức tạp / quy mô lớn

```text
23 + 26 + 27 + 31 + 32 + 33 + 40 + 41 + 43 + 44 + 46 + 48 + 49
```

Với案件 phức tạp, không để AI viết code ngay. Trước khi vào implementation, cần chuẩn bị Repository Map, Contract Map, Service Map, Context Budget và Traceability.

---

## 3. Thuật ngữ nền tảng: từ những điều cơ bản nhất

| Thuật ngữ | Giải thích cho người mới |
|---|---|
| AI-driven development | Phương thức phát triển dùng AI không chỉ như trợ lý tìm kiếm mà trong các công đoạn thiết kế, implementation, review, test và cập nhật tài liệu. Tuy nhiên, đây không phải là giao phó toàn bộ cho AI. Chỉ khi thiết kế input, output, kiểm chứng, quyền hạn và chứng tích của AI thì mới có thể dùng trong nghiệp vụ. |
| Specification-driven development / SDD | Trong bộ này, SDD là viết tắt của Specification Driven Development. Đây là phương thức chuẩn bị trước specification, acceptance criteria, phạm vi ảnh hưởng, kế hoạch implementation, góc nhìn review và kế hoạch test; sau đó AI và con người phát triển dựa trên các căn cứ đó. |
| Spec Pack | Bản chính tổng hợp specification, bối cảnh, AC, phạm vi ảnh hưởng, ràng buộc, điểm chưa xác định và việc cần con người phán đoán. Đây là nơi AI quay lại khi bị lúng túng. |
| Impl Plan | Kế hoạch implementation. Ghi lại file nào sẽ được sửa như thế nào, thứ tự thực hiện và test nào cần chạy. Đây không phải là nơi viết toàn bộ code trước, mà là bản thiết kế có thể review. |
| Review Checklist | Danh sách góc nhìn review. Dùng để không bỏ sót các điểm như khớp specification, số, full-width character, Magic Number, FE/BE contract, DB, Security, vận hành/bảo trì. |
| Source Intelligence | Cách nghĩ tạo bản đồ repository, module, entry point, DB, API, external IF trước khi để AI đọc source. |
| Right-sizing | Điều chỉnh độ nặng của SDD theo案件. Không ép quy trình khổng lồ cho sửa nhỏ, và bổ sung option nâng cao cần thiết cho案件 nguy hiểm. |
| Context | Thông tin đưa cho AI: ticket, specification, source, DB definition, test, log, tri thức quá khứ, v.v. AI chính xác và an toàn đến đâu phụ thuộc rất lớn vào việc đưa gì cho AI. |
| Context Loading | Công việc chọn tài liệu AI cần đọc, đặt thứ tự ưu tiên và loại trừ thông tin cần loại trừ. |
| Strategic Compact | Việc lưu lại dạng tóm tắt mục tiêu hiện tại, phán đoán, file đã đọc và việc chưa xong để AI/con người không mất các tiền đề quan trọng trong công việc dài hoặc quy mô lớn. |
| Artifact | Sản phẩm trung gian được tạo trong SDD, như Spec Pack, Impl Plan, Review Checklist, Test Results, Final Report. |
| Traceability | Trạng thái có thể truy vết từ requirement, specification, implementation, test, review đến phán đoán cuối cùng. Rất quan trọng cho audit và đảm bảo chất lượng. |
| Failure Mode | Mẫu thất bại mà AI hoặc con người dễ mắc, ví dụ thiếu DB definition nên viết SQL sai, không xét full-width digit, gọi method không tồn tại. |
| Project Knowledge | Tri thức đặc thù của dự án: thuật ngữ nghiệp vụ, quy ước DB, ràng buộc framework, ví dụ implementation đúng, pattern bị cấm. |
| Harness Engineering | Cách nghĩ thiết kế các thiết bị xung quanh, rule, quyền hạn, tool, đánh giá, audit, context và artifact để AI làm việc an toàn. Không chỉ nhìn vào model AI đơn lẻ, mà thiết kế toàn bộ môi trường nơi AI hoạt động. |
| Agent | Một “nhân sự AI” có vai trò cụ thể, ví dụ Security Reviewer, Test Reviewer, Architect Agent. |
| Orchestrator | Bộ điều phối kiểm soát nhiều Agent hoặc tool: ai đọc gì, xuất gì, kết quả nào được sử dụng. |
| Tool-Grounded Verification | Cách nghĩ kiểm chứng ý kiến của AI bằng kết quả tool thực tế như test, build, lint, SAST, SCA, Secrets Scan. |
| RAG | Viết tắt của Retrieval Augmented Generation. Cơ chế tìm tài liệu/code cần thiết rồi đưa cho AI, để AI trả lời dựa trên căn cứ đã truy xuất. |
| Code Map | Bản đồ hóa source lớn bằng module, file, function, call, DB, test để AI dễ nắm toàn thể. |
| Token | Đơn vị xử lý chuỗi ký tự đầu vào/đầu ra của AI. Đưa quá nhiều thông tin sẽ tăng chi phí và độ trễ; cắt quá nhiều thì giảm độ chính xác. |
| Prompt Caching | Cách nghĩ tái sử dụng cùng một prefix để AI API xử lý nhanh hơn và rẻ hơn. Điều quan trọng là không đặt thông tin thay đổi mỗi lần ở đầu prompt. |
| PR Gate | Cổng chất lượng quyết định có được merge Pull Request hay không. Không chỉ dựa vào AI review mà kết hợp CI, SAST, test và Human Review. |
| Observability | Khả năng quan sát trạng thái của flow phát triển dùng AI: token, cost, latency, tool failure, tỷ lệ phát hiện có ích, tỷ lệ false positive, v.v. |

---

## 4. Tư tưởng và bối cảnh được đưa vào SDD V04

SDD V04 là sự tích hợp nhiều tri thức thực tế và sự phát triển của AI development. Về tư tưởng, nó coi trọng 6 điểm sau.

### 4.1 Không để AI tự do viết, mà tạo môi trường để AI không bị lạc

Nhiều thất bại của AI không chỉ do AI yếu, mà do thông tin đưa cho AI thiếu, cũ, mâu thuẫn, quá nhiều, hoặc lẫn thông tin nguy hiểm. SDD V04 tạo trạng thái để AI phán đoán dựa trên căn cứ thông qua Spec Pack, Source Intelligence, Context Loading và Artifact Governance.

### 4.2 Tạo specification trước

Khi yêu cầu AI “hãy làm tính năng này”, AI sẽ tự suy đoán để bù những thông tin thiếu. Suy đoán có thể tiện, nhưng nguy hiểm với hệ thống nghiệp vụ. Vì vậy cần làm rõ specification, AC, điểm chưa xác định và việc cần con người phán đoán trước. Đây là nền tảng của SDD.

### 4.3 Nâng độ chính xác phân tích bằng bản đồ source

Trong hệ thống phức tạp, đưa toàn bộ source cho AI đọc chưa chắc tăng độ chính xác. Điều cần thiết là bản đồ nối Entry Point, Call Graph, DB, API, Event và External IF. File 23 và 41 là các pack cho mục đích này.

### 4.4 Không xem ý kiến của AI là bằng chứng

AI review rất mạnh, nhưng chỉ là ý kiến. Để phán đoán cuối cùng, cần bằng chứng như test, build, lint, SAST, SCA, Secrets Scan, Human Review. File 43 và 47 đưa tư tưởng này vào vận hành.

### 4.5 Càng nâng cao, càng phải kiểm soát token và quyền hạn

Multi-Agent, RAG và PR Gate rất mạnh, nhưng nếu đưa toàn bộ thông tin cho mọi Agent thì chi phí sẽ bùng nổ. Ngoài ra, nếu cấp write permission hoặc quyền MCP cho AI, ảnh hưởng khi xảy ra sự cố cũng lớn hơn. File 44 và 45 kiểm soát token/cost và permission/security.

### 4.6 Biến thất bại thành tài sản cho lần sau

Các sự kiện như AI sai, review bỏ sót, sự cố production không được kết thúc như chuyện một lần. Chúng được nâng cấp thành Failure Mode, Project Knowledge, Evaluation Dataset. File 29, 34, 49 đảm nhiệm cơ chế này.

---

## 5. Luồng cơ bản của SDD V04

Luồng tiêu chuẩn của SDD có thể hiểu như sau.

```text
Phase 0-A: Safety Gate
  Kiểm tra quyền hạn nguy hiểm, thông tin bí mật, tài liệu ngoài và nơi làm việc
Phase 0-B: Common Base / Source Intelligence
  Tạo bản đồ source, DB, API, test, tài liệu thiết kế
Phase 1: Investigation / Spec Pack
  Sắp xếp specification, AC, điểm chưa xác định, phạm vi ảnh hưởng
Phase 2: Context / Knowledge
  Đưa vào tri thức đặc thù dự án, pattern hiện có, ràng buộc
Phase 3: Impl Plan
  Thiết kế phương châm implementation, file thay đổi, thứ tự và rủi ro
Phase 4: Review Checklist
  Chuẩn bị góc nhìn specification, FE, BE, DB, Security, vận hành, test
Phase 5: Implementation / Self Review
  Implement, AI self-review và nếu cần thì independent AI review
Phase 6: Test Plan
  Thiết kế Unit / Integration / Contract / E2E / Migration / Regression
Phase 7: Test Results
  Ghi lại kết quả chạy, thất bại, chạy lại, lý do không chạy
Phase 8: Final Report
  Tổng hợp nội dung thay đổi, căn cứ, rủi ro còn lại, kết quả review, phán đoán
Phase 9: Living Docs / Learning
  Cập nhật Spec, Knowledge, Failure Mode, Rules, Checklists
```

Điều quan trọng nhất người mới cần nhớ là trong SDD, “suy nghĩ trước khi implement” và “để lại chứng tích sau khi implement” đều quan trọng như nhau.

---

## 6. Danh sách file và thông tin đo thực tế

Kết quả kiểm tra các file Markdown trong `SDD-導入パック_V04.2.zip` như sau.

| No | File | Tóm tắt vai trò | Số dòng | Số ký tự |
|---:|---|---|---:|---:|
| 1 | `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` | Quy trình làm việc tiêu chuẩn của SDD V04. Định nghĩa từ Phase 0-A đến Phase 9: làm gì, theo thứ tự nào, để lại artifact nào. | 1359 | 33005 |
| 2 | `22_SDD_1st-Step-Pack_03_プロンプト集_Core_Ver.04_Japanese.md` | Bộ prompt để thực thi file 21. Tổng hợp câu yêu cầu AI theo từng Phase, định dạng output, điều cấm và góc nhìn review. | 1994 | 39829 |
| 3 | `23_SDD_Source-Intelligence-Pack_Ver.04_Japanese.md` | Tiêu chuẩn tạo bản đồ source, DB, API, màn hình, batch, external IF trước khi để AI implement. | 1414 | 26881 |
| 4 | `24_SDD_Review-TestCode-Enhancement_Ver.04_Japanese.md` | Tiêu chuẩn tăng cường góc nhìn review và test code, bao gồm số, full-width digit, Magic Number, vận hành/bảo trì. | 1123 | 19279 |
| 5 | `25_SDD_Security-Gate-and-CI-Security_Ver.04_Japanese.md` | Biến Phase 0-A thành Security Gate thực sự, định nghĩa cách xử lý môi trường AI development, CI, tài liệu ngoài, thông tin bí mật. | 1283 | 22358 |
| 6 | `26_SDD_FE-BE-Contract-and-Impact-Analysis_Ver.04_Japanese.md` | Quản lý xuyên suốt API contract, DTO, Validation, Error, Permission, State trong hệ thống FE/BE tách biệt. | 1550 | 35850 |
| 7 | `27_SDD_Microservice-and-MultiRepo-Analysis_Ver.04_Japanese.md` | Quản lý contract giữa service, ownership dữ liệu, thứ tự deploy trong microservice, multi-repo, multi-tech-stack. | 1784 | 37469 |
| 8 | `28_SDD_Applicability-and-RightSizing_Ver.04_Japanese.md` | Tiêu chuẩn phán đoán nên áp dụng SDD đến đâu theo độ phức tạp, rủi ro và chi phí của案件. | 1839 | 29720 |
| 9 | `29_SDD_Failure-Mode-and-Continuous-Learning_Ver.04_Japanese.md` | Tích lũy nhầm lẫn AI, bỏ sót review, sự cố production, False Positive thành Failure Mode và nối tới cải tiến lần sau. | 1614 | 25968 |
| 10 | `11_SDD_20s-Pack-README-and-Integration-Guide_Ver.04_Japanese.md` | Cửa vào của 21〜29・31〜34. Hướng dẫn dùng file nào cho案件 nào, thứ tự đưa vào và bộ tối thiểu. | 631 | 14976 |
| 11 | `31_SDD_Context-Loading-and-Exclusion_Ver.04_Japanese.md` | Định nghĩa AI nên đọc gì, không nên đọc gì và xử lý theo thứ tự ưu tiên nào. | 1108 | 18369 |
| 12 | `32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Japanese.md` | Tiêu chuẩn compact/handoff để không mất tiền đề và phán đoán trong công việc dài, nhiều ngày, nhiều AI. | 950 | 14919 |
| 13 | `33_SDD_Artifact-Governance-and-Traceability_Ver.04_Japanese.md` | Quản lý bản chính, trạng thái, căn cứ, lịch sử thay đổi và truy vết từ requirement đến test của artifact SDD. | 940 | 16198 |
| 14 | `34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Japanese.md` | Tích lũy tri thức nghiệp vụ, pattern thành công, pattern cấm, ràng buộc FW của dự án ở dạng AI có thể đọc. | 1075 | 16482 |
| 15 | `40_SDD_Advanced-Options-Overview-and-Selection-Guide_Ver.04_Japanese.md` | Cửa vào của Advanced Options 40〜49. Phán đoán dùng option nâng cao nào cho案件 khó. | 724 | 19015 |
| 16 | `41_SDD_Heavy-Source-Analysis-and-Repository-Intelligence-Option_Ver.04_Japanese.md` | Option phân tích nâng cao để tạo Repository Intelligence sâu cho repo lớn, multi-tech-stack, legacy. | 863 | 20138 |
| 17 | `42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Japanese.md` | Option nâng cao chia việc AI review/design bằng nhiều model, nhiều Agent và Orchestrator. | 804 | 16786 |
| 18 | `43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Japanese.md` | Option nâng cao kiểm chứng ý kiến AI bằng tool evidence như test/build/lint/SAST và hình thành consensus. | 762 | 15458 |
| 19 | `44_SDD_Token-Optimization-and-Cost-Control-Option_Ver.04_Japanese.md` | Option nâng cao kiểm soát token, cost, latency của Advanced Options. | 1075 | 19001 |
| 20 | `45_SDD_Full-Security-and-Agentic-AI-Governance-Option_Ver.04_Japanese.md` | Option security governance nâng cao bao gồm AI Agent, MCP, hooks, tool execution, tài liệu ngoài, CI/CD. | 1203 | 24512 |
| 21 | `46_SDD_RAG-CodeMap-and-Context-Compression-Option_Ver.04_Japanese.md` | Option nâng cao dùng RAG, Code Map, Context Compression để đưa căn cứ cần thiết cho AI với token thấp. | 996 | 18250 |
| 22 | `47_SDD_Automated-PR-Review-and-AI-QA-Gate-Option_Ver.04_Japanese.md` | Option nâng cao tích hợp PR review, CI, tool result, AI review, Policy, human review thành QA Gate. | 1009 | 19610 |
| 23 | `48_SDD_Parallel-Worktree-and-Large-Refactoring-Option_Ver.04_Japanese.md` | Option nâng cao dùng Git worktree và nhiều phương án implementation để tiến hành refactor lớn / AI song song an toàn. | 1758 | 31865 |
| 24 | `49_SDD_Evaluation-Observability-and-Continuous-Optimization-Option_Ver.04_Japanese.md` | Option nâng cao đánh giá, quan sát và cải tiến chính hệ thống AI development; xử lý metrics, trace, dataset, dashboard. | 1939 | 34604 |

---

## 7. Chế độ áp dụng và tiêu chí phán đoán

Trong SDD V04, độ sâu áp dụng thay đổi theo案件. Điều này gọi là Right-sizing.

| Mode | Ví dụ tiêu biểu | File chính dùng | Tiêu chí phán đoán |
|---|---|---|---|
| Light | Sửa README, sửa wording, sửa nhỏ 1 file | 21, 22, 28 | Phạm vi ảnh hưởng rõ, không có DB/Security/external IF |
| Standard | API thông thường, màn hình thông thường, bug fix thông thường | 21, 22, 23, 24, 28, 31, 33 | Cần chứng tích tiêu chuẩn cho specification, implementation, test |
| Standard Plus | Liên quan FE/BE, DB, nhiều layer | 23, 24, 25, 26, 28, 31, 33 | Có contract, Validation, DB hoặc Security |
| Heavy | Repo lớn, nhiều tech stack, microservice | 27, 40, 41, 43, 44, 46 | Chỉ Source Map là không đủ độ chính xác phân tích |
| Critical | Authentication, authorization, payment, personal data, ảnh hưởng production | 25, 43, 45, 47, 49 | Chỉ AI phán đoán là nguy hiểm; bắt buộc Human Governance |
| Stop | Thiếu thông tin, không rõ quyền hạn, thiếu source | 28, 31 | Tiếp tục sẽ nguy hiểm; cần con người xác nhận |

### 7.1 Ví dụ phán đoán cụ thể

| Nội dung thay đổi | Mode khuyến nghị | Lý do |
|---|---|---|
| Đổi wording của button | Light | Ảnh hưởng specification / DB / Security nhỏ |
| Thêm field vào API response | Standard Plus | Cần FE/BE contract, DTO, test |
| Sửa logic tính tiền | Standard Plus〜Critical | Độ chính xác số, làm tròn, độ chính xác DB, test rất quan trọng |
| Sửa logic authorization | Critical | Cần Security Veto và Human Review |
| Sửa field event của nhiều service | Heavy | Cần producer/consumer, tương thích schema, thứ tự deploy |
| Refactor legacy quy mô lớn | Heavy | Cần phân tích, so sánh song song và đánh giá bằng 41, 48, 49 |

---

## 8. Hướng dẫn chi tiết cho từng file

Chương này giải thích từng file một: nội dung, cách dùng, hiệu quả, phán đoán áp dụng, tư tưởng nền và ví dụ.

### 21. `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md`

**Tổng quan:** Quy trình làm việc tiêu chuẩn của SDD V04. Đây là file lõi định nghĩa từ Phase 0-A đến Phase 9: cần làm gì, theo thứ tự nào và để lại artifact nào.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Tài liệu quy trình Core. Khi đưa SDD vào dự án, trước hết đọc file này và chuyển flow phát triển tại hiện trường sang dạng Phase. |
| Khi dùng | Tất cả案件. Đặc biệt khi đưa vào lần đầu, phát triển chức năng thông thường, sắp xếp specification trước khi giao AI implement, hoặc muốn để lại chứng tích review. |
| Hiệu quả chính | Giảm specification mơ hồ, AI tự suy đoán, artifact rải rác, bỏ sót review. Có thể đặt điều kiện cần dừng ở từng Phase. |
| Phán đoán áp dụng | Nhỏ thì vận hành Light, thông thường thì Standard, phức tạp thì dùng 28 để phán đoán Heavy và nối sang 23 trở đi. |
| Ví dụ cụ thể | Với việc thêm field API: ở Phase 0-A tạo nơi làm việc và chứng tích an toàn; Phase 1 tạo Spec Pack; Phase 3 tạo Impl Plan; Phase 4 tạo Review Checklist; Phase 7 tạo Test Results; Phase 9 cập nhật tri thức. |
| Quy mô đo thực tế | Khoảng 1360 dòng / khoảng 33019 ký tự |

**Các chương chính:**

- 0. Cách dùng tài liệu này
- 1. Tư tưởng cơ bản của Ver.04 Core
- 2. Luồng tổng thể của Ver.04
- 3. Right-sizing: phán đoán áp dụng nhẹ / tiêu chuẩn / nặng
- 4. Cấu trúc thư mục khuyến nghị
- 5. Phase 0-A: Safety Gate / nơi đặt / chứng tích
- 6. Phase 0-B: Common Base / Source Intelligence
- 7. Phase 1: Investigation / Spec Pack

**Điểm người mới cần hiểu:**

File này dùng để “con người và AI có cùng tiền đề” trước khi nghĩ đến “yêu cầu AI làm gì”. Trong AI development, thất bại ban đầu thường không nằm ở prompt hay/dở, mà ở việc bắt đầu khi specification, ràng buộc và tiêu chí phán đoán còn mơ hồ. File Core giúp ngăn lỗi đó.

**Lưu ý khi đưa vào:**

- Không chỉ điền Phase cho có hình thức. Điều quan trọng là làm rõ điểm chưa xác định, việc cần con người phán đoán và điều kiện Stop.
- Với案件 nhỏ, không thực hiện nặng toàn bộ Phase; hãy Light hóa bằng 28.

---

### 22. `22_SDD_1st-Step-Pack_03_プロンプト集_Core_Ver.04_Japanese.md`

**Tổng quan:** Bộ prompt để thực thi file 21. Tổng hợp câu yêu cầu AI theo từng Phase, định dạng output, điều cấm và góc nhìn review.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Prompt thực thi Core. Dù biết quy trình, chất lượng vẫn giảm nếu yêu cầu AI mơ hồ, nên file này chuẩn hóa câu yêu cầu. |
| Khi dùng | Khi yêu cầu Claude, Codex, Cursor, Copilot Chat, v.v. tạo artifact SDD. Cũng hữu ích khi người mới chưa biết viết chỉ thị cho AI. |
| Hiệu quả chính | Đồng nhất độ chi tiết output của AI, ổn định tên artifact, cấu trúc chương và tiêu chí phán đoán. Dễ truy vết đã yêu cầu gì khi review. |
| Phán đoán áp dụng | Nếu thông tin đặc thù案件 mỏng, chỉ prompt không đủ độ chính xác. Bổ sung Context bằng 23, 31, 34. |
| Ví dụ cụ thể | Đưa ticket, source liên quan, DB definition, test hiện có vào prompt tạo Spec Pack, và bắt buộc AI xuất điểm chưa xác định cùng việc cần con người xác nhận. |
| Quy mô đo thực tế | Khoảng 1995 dòng / khoảng 39843 ký tự |

**Các chương chính:**

- 0. Cách dùng
- 1. Khối biến dùng chung
- 2. Prompt dùng chung cho toàn Phase
- 3. Phase 0-A: Safety Gate / nơi đặt / chứng tích
- Verdict
- Findings
- Missing safeguards
- Good decisions worth keeping

**Điểm người mới cần hiểu:**

File này cũng phục vụ việc chuẩn bị tiền đề chung giữa người và AI trước khi yêu cầu cụ thể. Prompt không thay thế được specification và context đúng.

**Lưu ý khi đưa vào:**

- Prompt không phải vạn năng. Nếu context đầu vào cũ, thiếu hoặc nguy hiểm thì output cũng xấu. Hãy dùng cùng 31.
- Không xem output là đúng tuyệt đối; cần review bằng 24/43.

---

### 23. `23_SDD_Source-Intelligence-Pack_Ver.04_Japanese.md`

**Tổng quan:** Tiêu chuẩn tạo bản đồ source, DB, API, màn hình, batch, external IF trước khi để AI implement.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Mở rộng tiêu chuẩn để tăng độ chính xác phân tích. Giảm việc AI “chắc là file này” và chuyển sang Impact Analysis có căn cứ. |
| Khi dùng | Source phức tạp, specification hiện có không rõ, liên quan DB/external IF, không chắc phạm vi ảnh hưởng, repository lần đầu tiếp xúc. |
| Hiệu quả chính | Giảm sửa nhầm target, bỏ sót table liên quan, thiếu test hiện có, tin nhầm tài liệu thiết kế cũ. |
| Phán đoán áp dụng | Nếu target rõ và chỉ 1 file thì dùng nhẹ. Nếu nhiều layer / nhiều repository thì mở rộng sang 41. |
| Ví dụ cụ thể | Không chỉ nhìn Controller, mà tạo Source Map nối Route, Service, Repository, DB migration, DTO và test. |
| Quy mô đo thực tế | Khoảng 1415 dòng / khoảng 26881 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 21・22
- 3. Mode áp dụng
- 4. Nguyên tắc Source Intelligence
- 5. Danh sách artifact
- 6. Source Availability Report
- 1. Verdict

**Điểm người mới cần hiểu:**

File này tăng cường chuyên sâu cho quy trình Core. Với案件 thông thường chỉ dùng những chương cần thiết; với案件 phức tạp thì tạo cả template artifact. Điều quan trọng không phải đọc toàn bộ extension mà là dùng 28 để xác định cần dùng đến đâu.

**Lưu ý khi đưa vào:**

- Không dành quá nhiều thời gian tạo Source Map. Hãy chọn độ chi tiết theo phạm vi thay đổi.
- Nếu thiếu source, không tiếp tục bằng suy đoán; ghi rõ vào Source Availability.

---

### 24. `24_SDD_Review-TestCode-Enhancement_Ver.04_Japanese.md`

**Tổng quan:** Tiêu chuẩn tăng cường góc nhìn review và test code, bao gồm số, full-width digit, Magic Number, vận hành/bảo trì.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Mở rộng tiêu chuẩn kiểm tra chất lượng. Không để implementation của AI đi thẳng, mà xem qua các góc nhìn hệ thống chung, FE, BE, DB, Security, Test. |
| Khi dùng | Code review, AI self-review, Codex independent review, thiết kế test, phòng regression. |
| Hiệu quả chính | Dễ phát hiện thiếu input validation phổ biến, lỗi full-width number, phân nhánh literal, thiếu log, thiếu góc nhìn test. |
| Phán đoán áp dụng | Sửa nhẹ thì chỉ dùng góc nhìn chính. Thay đổi rủi ro cao thì nối với 43/47 để Tool-Grounded hóa và đưa vào QA Gate. |
| Ví dụ cụ thể | Với input tiền, review xem có chỉ giả định half-width digit không, có xét full-width digit, dấu phẩy, số thập phân, số âm, chuỗi rỗng, độ chính xác DB không. |
| Quy mô đo thực tế | Khoảng 1124 dòng / khoảng 19279 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 21・22
- 3. Tư tưởng cơ bản của review
- 4. Severity model
- 5. Flow thực hiện review
- 6. Cấu trúc tiêu chuẩn của Review Checklist
- 1. Khớp specification / AC

**Điểm người mới cần hiểu:**

File này tăng cường chuyên sâu cho quy trình Core. Hãy dùng những phần cần thiết theo rủi ro, không biến checklist thành mục tiêu tự thân.

**Lưu ý khi đưa vào:**

- Checklist quá dài sẽ không được dùng. Chọn góc nhìn bắt buộc theo rủi ro案件.
- Kết hợp AI review, human review và tool results.

---

### 25. `25_SDD_Security-Gate-and-CI-Security_Ver.04_Japanese.md`

**Tổng quan:** Biến Phase 0-A thành Security Gate thực sự, định nghĩa cách xử lý môi trường AI development, CI, tài liệu ngoài và thông tin bí mật.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Mở rộng tiêu chuẩn Security. Trước khi cấp quyền tiện lợi cho AI, ngăn rò rỉ, thực thi nhầm và injection từ tài liệu ngoài. |
| Khi dùng | Tối thiểu trong mọi案件; đặc biệt với authentication, authorization, personal data, external integration, CI/CD, MCP/hooks. |
| Hiệu quả chính | Ngăn rò rỉ secret, thực thi command nguy hiểm, đưa Office nguyên bản lộn xộn, quyền MCP/hooks quá rộng. |
| Phán đoán áp dụng | Thường dùng tiêu chuẩn 25 là đủ. Nếu AI Agent thực thi tool hoặc dùng MCP quyền cao thì mở rộng sang 45. |
| Ví dụ cụ thể | Không đưa `.env` hoặc key file vào AI context; dùng bản trích xuất và source availability để specification hóa. |
| Quy mô đo thực tế | Khoảng 1284 dòng / khoảng 22358 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Vị trí của chuẩn ngoài được tham chiếu
- 3. Phase 0-A Security Gate
- 4. Hard Block / Soft Guidance / Human Review
- 5. Phương châm `.claude/settings.json`
- 6. Phương châm `CLAUDE.md`
- 7. Mối đe dọa đặc thù của môi trường AI development

**Điểm người mới cần hiểu:**

File này là extension bảo vệ an toàn cho Core. Nó không nhằm dừng AI vì lý do security, mà nhằm tạo ranh giới an toàn để vẫn dùng AI.

**Lưu ý khi đưa vào:**

- Đừng lấy security làm lý do dừng AI usage; hãy tạo boundary an toàn.
- Không để mơ hồ cách xử lý secrets, `.env`, production log, personal data, tài liệu ngoài.

---

### 26. `26_SDD_FE-BE-Contract-and-Impact-Analysis_Ver.04_Japanese.md`

**Tổng quan:** Quản lý xuyên suốt API contract, DTO, Validation, Error, Permission, State trong hệ thống FE/BE tách biệt.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Extension riêng cho FE/BE. Ngăn tối ưu cục bộ chỉ FE hoặc chỉ BE, phát hiện lệch contract trước implementation. |
| Khi dùng | Màn hình và API tách nhau, OpenAPI/DTO thay đổi, validation thay đổi, error display thay đổi, permission-based display control. |
| Hiệu quả chính | Ngăn lệch giữa FE input constraint và BE Validation, thiếu field API, không khớp error message, authorization chỉ bằng hiển thị. |
| Phán đoán áp dụng | Sửa UI đơn thuần không đổi API contract thì dùng nhẹ. Nếu Request/Response hoặc quyền thay đổi thì bắt buộc. |
| Ví dụ cụ thể | Khi thêm field địa chỉ, đưa FE form, API client, BE DTO, validation, DB, error map, contract test vào một Contract Map. |
| Quy mô đo thực tế | Khoảng 1551 dòng / khoảng 35850 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 21〜25
- 3. Điều kiện áp dụng pack này
- 4. Định nghĩa FE/BE Contract
- 5. Danh sách artifact
- 6. Source Availability Gate
- 1. Ticket

**Điểm người mới cần hiểu:**

FE và BE riêng lẻ đúng vẫn có thể gây lỗi nếu contract lệch. Contract Map nên được xem là bản chính cho thay đổi liên quan FE/BE.

**Lưu ý khi đưa vào:**

- Nếu contract lệch, hệ thống lỗi dù FE/BE riêng lẻ trông đúng.
- Thiết kế chỉ dùng FE display control để thay authorization là nguy hiểm. Phải xác nhận authorization ở BE.

---

### 27. `27_SDD_Microservice-and-MultiRepo-Analysis_Ver.04_Japanese.md`

**Tổng quan:** Quản lý contract giữa service, ownership dữ liệu và thứ tự deploy trong microservice, multi-repo, multi-tech-stack.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Extension cho hệ thống phân tán quy mô lớn. Xử lý rủi ro ranh giới service mà review một repo đơn lẻ không nhìn thấy. |
| Khi dùng | API Gateway, BFF, event integration, nhiều DB, schema change, thay đổi đồng thời nhiều service, deploy/rollback liên quan. |
| Hiệu quả chính | Giảm bỏ sót service dependency, phá event schema, double execution, deploy không tương thích, không thể rollback. |
| Phán đoán áp dụng | Nếu thay đổi trong một service thì 23/26 có thể đủ. Nếu liên quan nhiều service hoặc event/topic thì áp dụng 27. |
| Ví dụ cụ thể | Khi sửa field event của order-service, kiểm tra producer/consumer, schema compatibility, DLQ, retry, trace id, thứ tự deploy. |
| Quy mô đo thực tế | Khoảng 1785 dòng / khoảng 37469 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 21〜26
- 3. Điều kiện áp dụng pack này
- 4. Tư tưởng cơ bản
- 5. Danh sách artifact
- 6. Source Availability Gate
- 1. Change summary

**Điểm người mới cần hiểu:**

Trong microservice, unit test không đủ. Cần kiểm tra contract, event, thứ tự deploy và rollback.

**Lưu ý khi đưa vào:**

- Không để mơ hồ owner và ranh giới trách nhiệm giữa các service.

---

### 28. `28_SDD_Applicability-and-RightSizing_Ver.04_Japanese.md`

**Tổng quan:** Tiêu chuẩn phán đoán nên áp dụng SDD đến đâu theo độ phức tạp, rủi ro và chi phí của案件.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Lõi của việc ngăn áp dụng quá mức và thiếu mức. Điều phối để dùng SDD không quá nhẹ, không quá nặng. |
| Khi dùng | Khi bắt đầu案件, khi giữa chừng trở nên phức tạp, khi phân vân có dùng Advanced Options nhóm 40 hay không. |
| Hiệu quả chính | Ngăn cả hai lỗi: ép quy trình quá nặng cho sửa nhỏ, và vận hành quá nhẹ cho案件 rủi ro cao dẫn đến sự cố. |
| Phán đoán áp dụng | Phán đoán Light / Standard / Standard Plus / Heavy / Critical / Stop và chỉ chọn pack cần thiết. |
| Ví dụ cụ thể | README là Light; API+DB là Standard Plus; authorization + personal data + nhiều service là Critical-ish và dùng 25/27/43/45/47. |
| Quy mô đo thực tế | Khoảng 1840 dòng / khoảng 29709 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 21〜27 và nhóm 40
- 3. Tư tưởng cơ bản của Right-sizing
- 4. Định nghĩa thuật ngữ
- 5. Toàn bộ flow phán đoán
- 6. Định nghĩa Mode
- Stop reason

**Điểm người mới cần hiểu:**

Quyết định làm nhẹ SDD cũng là một quyết định chính thức, nhưng cần để lại lý do.

**Lưu ý khi đưa vào:**

- Nếu rủi ro tăng giữa chừng, hãy phán đoán lại Mode.

---

### 29. `29_SDD_Failure-Mode-and-Continuous-Learning_Ver.04_Japanese.md`

**Tổng quan:** Tích lũy nhầm lẫn AI, bỏ sót review, sự cố production và False Positive thành Failure Mode, kết nối với cải tiến lần sau.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Tiêu chuẩn cải tiến liên tục. Không biến thất bại thành lỗi cá nhân, mà nâng cấp thành rule, prompt, test, CI, Knowledge. |
| Khi dùng | Sau review, sau sự cố, khi AI lặp lại cùng lỗi, khi muốn cải tiến prompt/checklist. |
| Hiệu quả chính | Ngăn tái diễn cùng lỗi, calibrate AI review, tài sản hóa tri thức đặc thù dự án. |
| Phán đoán áp dụng | Dùng nhẹ trong mọi案件. Với sự cố lớn hoặc vận hành AI liên tục thì nối với Evaluation của 49. |
| Ví dụ cụ thể | Nếu AI gọi method không tồn tại, đăng ký Failure Mode, rồi nâng cấp vào method allowlist của 34 và góc nhìn review của 24. |
| Quy mô đo thực tế | Khoảng 1615 dòng / khoảng 25968 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 21〜28
- 3. Tư tưởng cơ bản
- 4. Failure Mode Index là gì
- 5. Đối tượng đăng ký
- 6. Hệ thống phân loại
- 7. Severity / Priority

**Điểm người mới cần hiểu:**

Failure Mode không phải truy tìm người có lỗi. Đây là tài sản học tập để ngăn tái diễn.

**Lưu ý khi đưa vào:**

- Không dừng ở việc đăng ký. Hãy nâng cấp sang Knowledge của 34, Review của 24 và PR Gate của 47.

---

### 11. `11_SDD_20s-Pack-README-and-Integration-Guide_Ver.04_Japanese.md`

**Tổng quan:** Cửa vào của 21〜29・31〜34. Hướng dẫn đọc file nào cho案件 nào, thứ tự đưa vào và bộ tối thiểu.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Navigation cho nhóm 20. Bản đồ giúp người mới đi vào standard pack của SDD V04 mà không bị lạc. |
| Khi dùng | Ngày đầu đưa vào, đào tạo, bắt đầu案件, chuẩn hóa dự án, PM/PL giải thích toàn cảnh. |
| Hiệu quả chính | Giảm rối do số lượng file nhiều, giúp chọn file cần đọc theo mục đích. |
| Phán đoán áp dụng | Luôn đọc đầu tiên. Sau đó dùng 11 làm bản đồ để chọn 21〜29・31〜34. |
| Ví dụ cụ thể | Với案件 FE/BE tách biệt, dùng 11 để dẫn tới 21/22/23/24/26/28/31/33. |
| Quy mô đo thực tế | Khoảng 632 dòng / khoảng 14931 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Toàn cảnh pack nhóm 20
- 2. Thứ tự nên đọc đầu tiên
- 3. Bộ đọc tối thiểu theo loại案件
- 4. Cách dùng theo Mode
- 5. Bảng tương ứng pack theo Phase
- 6. Bảng tương ứng artifact
- 7. Quy trình đưa vào ngày 1, tuần 1, tháng 1

**Điểm người mới cần hiểu:**

File này là bản đồ tổng thể. Quy trình chi tiết nằm trong 21〜29, vận hành chi tiết nằm trong 31〜34.

**Lưu ý khi đưa vào:**

- Khi đào tạo thành viên mới, dùng 11 làm cửa vào và giới hạn phạm vi cần đọc.

---

### 31. `31_SDD_Context-Loading-and-Exclusion_Ver.04_Japanese.md`

**Tổng quan:** Định nghĩa AI nên đọc gì, không nên đọc gì và xử lý theo thứ tự ưu tiên nào.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Kiểm soát Context. Đây là nền tảng ảnh hưởng đồng thời đến độ chính xác và an toàn của AI. |
| Khi dùng | 案件 có nhiều tài liệu, Excel/PDF/log/web ngoài/tài liệu thiết kế cũ/secret trộn lẫn. |
| Hiệu quả chính | Ngăn token bùng nổ, AI tin nhầm tài liệu cũ, Prompt Injection, đưa secret, đọc file không cần thiết. |
| Phán đoán áp dụng | Áp dụng nhẹ cho mọi案件. Nếu dùng RAG hoặc Code Map thì mở rộng sang 46. |
| Ví dụ cụ thể | Khi tài liệu thiết kế cũ và source mới mâu thuẫn, implementation hiện tại căn cứ source; requirement nghiệp vụ căn cứ specification chính; việc cần người xác nhận đưa vào Spec Pack. |
| Quy mô đo thực tế | Khoảng 1109 dòng / khoảng 18364 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Kết nối với 11 và 21〜29
- 3. Tư tưởng cơ bản của Context Loading
- 4. Source Priority Rule
- 5. Phân loại Context
- 6. Include / Ask / Exclude Rule
- 7. Cách xử lý theo loại file

**Điểm người mới cần hiểu:**

Đưa toàn bộ tài liệu cho AI không phải là tử tế. Thông tin không cần thiết, nguy hiểm, cũ cần được loại trừ.

**Lưu ý khi đưa vào:**

- Office nguyên bản và web ngoài phải được xem là dữ liệu, không phải mệnh lệnh; tạo bản trích xuất trước khi dùng.

---

### 32. `32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Japanese.md`

**Tổng quan:** Tiêu chuẩn compact/handoff để không mất tiền đề và phán đoán trong công việc dài, nhiều ngày, nhiều AI.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Nền tảng duy trì công việc. Trước khi trí nhớ của AI trở nên mơ hồ, biến thông tin quan trọng thành artifact. |
| Khi dùng | Phân tích quy mô lớn, implementation dài, nhiều AI review, công việc qua ngày, bàn giao người phụ trách. |
| Hiệu quả chính | Ngăn mất context sau compact, thất lạc quyết định quan trọng, bỏ sót task chưa xong. |
| Phán đoán áp dụng | Bắt buộc với công việc kéo dài. Kết nối với 42 trong Multi-Agent. |
| Ví dụ cụ thể | Trước khi kết thúc ngày làm, snapshot hóa Current Objective, Must Not Forget, Read Files, Decisions, Next Step để hôm sau tiếp tục. |
| Quy mô đo thực tế | Khoảng 951 dòng / khoảng 14919 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Khác gì với 31
- 3. Tư tưởng cơ bản của Strategic Compact
- 4. Khi nào cần Compact
- 5. Strategic Compact Snapshot
- 1. Snapshot Metadata
- 2. Current Objective

**Điểm người mới cần hiểu:**

Compact không phải chỉ là tóm tắt cuộc trò chuyện. Nó là lưu trạng thái và phán đoán cần thiết để tiếp tục công việc.

**Lưu ý khi đưa vào:**

- Luôn để lại điểm chưa xác định và việc cần con người phán đoán.

---

### 33. `33_SDD_Artifact-Governance-and-Traceability_Ver.04_Japanese.md`

**Tổng quan:** Quản lý bản chính, trạng thái, căn cứ, lịch sử thay đổi và truy vết từ requirement đến test của artifact SDD.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Artifact governance. Ngăn bất nhất như Spec Pack cũ còn Report đã mới. |
| Khi dùng | 案件 có nhiều artifact, cần audit, PR/Release decision, QA, nhiều người phụ trách. |
| Hiệu quả chính | Giảm không rõ bản chính, tái sử dụng artifact cũ, thiếu chứng tích review, đứt đoạn giữa requirement và test. |
| Phán đoán áp dụng | Áp dụng từ Standard trở lên. Là tiền đề cho worktree song song của 48 và PR Gate của 47. |
| Ví dụ cụ thể | Liên kết requirement ID, chương Spec, file thay đổi, test case, review finding, final decision trong Traceability Matrix. |
| Quy mô đo thực tế | Khoảng 941 dòng / khoảng 16198 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Phân loại Artifact
- 3. Artifact Status
- 4. Tiêu chuẩn Front Matter
- 5. Cấu trúc thư mục khuyến nghị
- 6. Artifact Inventory
- 7. Traceability Matrix

**Điểm người mới cần hiểu:**

Càng nhiều artifact, quản lý bản chính và trạng thái càng quan trọng.

**Lưu ý khi đưa vào:**

- Quản lý Status và Freshness để AI không đọc Spec Pack cũ như bản đúng.

---

### 34. `34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Japanese.md`

**Tổng quan:** Tích lũy tri thức nghiệp vụ, pattern thành công, pattern cấm và ràng buộc FW đặc thù dự án ở dạng AI có thể đọc.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Tài sản hóa tri thức. Dạy cho AI implementation đúng trong案件 cụ thể, không chỉ lý thuyết chung. |
| Khi dùng | Có framework riêng, thuật ngữ nghiệp vụ, quy ước DB, xử lý exception, chuẩn log, lỗi AI quá khứ. |
| Hiệu quả chính | Giảm việc AI dùng method không tồn tại, phá quy ước dự án, lặp cùng lỗi. |
| Phán đoán áp dụng | Bắt buộc cho dự án trung/dài hạn. Failure Mode đăng ký trong 29 được nâng cấp sang 34. |
| Ví dụ cụ thể | Đăng ký các method được phép dùng như `setString`/`setInt` của DBStatement vào method allowlist, và cấm `setDouble` không tồn tại. |
| Quy mô đo thực tế | Khoảng 1076 dòng / khoảng 16482 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận
- 2. Quan hệ với 29
- 3. Phân loại Knowledge
- 4. Cấu trúc thư mục khuyến nghị
- 5. Knowledge Card
- ID
- Title

**Điểm người mới cần hiểu:**

Knowledge không phải càng nhiều càng tốt. Cần kiểm kê tri thức cũ, tri thức ngoại lệ, tri thức cục bộ.

**Lưu ý khi đưa vào:**

- Sắp xếp tri thức ở độ chi tiết phù hợp để AI đọc trước khi làm việc.

---

### 40. `40_SDD_Advanced-Options-Overview-and-Selection-Guide_Ver.04_Japanese.md`

**Tổng quan:** Cửa vào của Advanced Options 40〜49. Dùng để phán đoán option nâng cao nào nên dùng trong案件 khó.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Selection guide cho Advanced Options. Bảng điều khiển để không áp dụng quá mức các chức năng nâng cao mạnh mẽ. |
| Khi dùng | 案件 phức tạp, rủi ro cao, quy mô lớn, yêu cầu chính xác cao, vận hành AI nâng cao. |
| Hiệu quả chính | Làm rõ cách dùng 41〜49 và chọn đúng phần cần thiết. |
| Phán đoán áp dụng | Đọc khi 28 phán đoán Heavy/Critical. Về nguyên tắc không cần cho Light. |
| Ví dụ cụ thể | Refactor lớn chọn 41/43/44/48/49; AI PR Gate chọn 42/43/45/47/49. |
| Quy mô đo thực tế | Khoảng 725 dòng / khoảng 18921 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận tổng thể của nhóm 40
- 2. Quan hệ với 11 và 21〜29・31〜34
- 3. Tư tưởng cơ bản của nhóm 40
- 4. Điều kiện dùng Advanced Option
- 5. Option Selection Matrix
- 6. Architecture tiêu chuẩn của nhóm 40
- 7. Artifact bổ sung trong nhóm 40

**Điểm người mới cần hiểu:**

Đây là Advanced Option. Mạnh nhưng nặng, không dùng thường trực. Chỉ áp dụng cho案件 rủi ro cao / quy mô lớn / yêu cầu chính xác cao, và phải quản lý token, quyền hạn, Human Review, Tool Evidence, Metrics.

**Lưu ý khi đưa vào:**

- Nhóm 40 mạnh, nhưng áp dụng cho mọi案件 sẽ nặng. Quyết định không dùng cũng quan trọng.

---

### 41. `41_SDD_Heavy-Source-Analysis-and-Repository-Intelligence-Option_Ver.04_Japanese.md`

**Tổng quan:** Option phân tích nâng cao để tạo Repository Intelligence sâu cho repo lớn, multi-tech-stack, legacy.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Bản Advanced của 23. Dùng khi Source Map thông thường không đủ, cần Call Graph và Risk Hotspot. |
| Khi dùng | Monolith lớn, nhiều công nghệ, có generated code, thiếu tài liệu, phạm vi ảnh hưởng không rõ. |
| Hiệu quả chính | Giảm bỏ sót phân tích, bỏ sót thay đổi, hiểu sai dependency, xử lý nhầm dead code, sửa nhầm generated code. |
| Phán đoán áp dụng | 41 nặng. Nếu 23 đủ thì không dùng. Context budget quản lý bằng 44, nhất quán artifact bằng 33. |
| Ví dụ cụ thể | Nếu có nhiều stack như C#/PHP/Java, tách trục review chung và trục review theo stack để Map hóa. |
| Quy mô đo thực tế | Khoảng 864 dòng / khoảng 20116 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Điều kiện áp dụng
- 2. Kết nối với 23・31・33・34・44
- 3. Flow tổng thể của Repository Intelligence
- 4. Danh sách artifact
- 5. Heavy Source Analysis Plan
- 1. Metadata
- 2. Analysis Goal

**Điểm người mới cần hiểu:**

Đây là Advanced Option mạnh nhưng nặng. Chỉ dùng cho案件 cần phân tích sâu; không biến “phân tích toàn bộ file” thành mục tiêu.

**Lưu ý khi đưa vào:**

- Tạo bản đồ cần thiết cho ảnh hưởng thay đổi, không phân tích mọi file vì muốn phân tích.

---

### 42. `42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao chia việc AI review/design bằng nhiều model, nhiều Agent và Orchestrator.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Lõi tăng độ chính xác AI. Tuy nhiên không chỉ tăng số Agent, mà phải kiểm soát vai trò, context và quyền hạn. |
| Khi dùng | Thiết kế rủi ro cao,案件 cần nhiều góc nhìn chuyên môn như security/performance/test. |
| Hiệu quả chính | Giảm bỏ sót và thiên lệch của AI đơn lẻ. Có thể chia cho Security Reviewer, Test Reviewer, Arbiter, v.v. |
| Phán đoán áp dụng | Không cần cho sửa nhẹ. Nếu dùng, quản lý token bằng 44, quyền hạn bằng 45, tool evidence bằng 43. |
| Ví dụ cụ thể | Bug Reviewer, Security Reviewer, Test Reviewer độc lập đưa ra finding; Arbiter hợp nhất trùng lặp và phán đoán có cần Human Review không. |
| Quy mô đo thực tế | Khoảng 805 dòng / khoảng 16764 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Mục đích dùng 42
- 2. Điều kiện nên dùng / không nên dùng
- 3. Kết nối với 21〜44
- 4. Architecture khuyến nghị
- 5. Trách nhiệm của Orchestrator
- 6. Agent Role Catalog
- 7. Model Router

**Điểm người mới cần hiểu:**

Tăng số Agent không đồng nghĩa tăng độ chính xác. Cần thu hẹp vai trò, Context, output schema.

**Lưu ý khi đưa vào:**

- Quản lý Agent bằng Orchestrator và output schema, không để Agent tự do nói dài.

---

### 43. `43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao kiểm chứng ý kiến AI bằng tool evidence như test/build/lint/SAST và hình thành consensus.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Nền tảng kiểm chứng tăng độ tin cậy của AI review. Phán đoán bằng bằng chứng và Veto, không bằng đa số. |
| Khi dùng | Quality gate, PR rủi ro cao, nhiều AI review, DB migration, security critical, release decision. |
| Hiệu quả chính | Ngăn AI phán đoán sai nhưng nghe có vẻ đúng, xóa chỉ trích nghiêm trọng bằng đa số, bỏ sót tool failure. |
| Phán đoán áp dụng | Nếu dùng AI review làm căn cứ phán đoán thì áp dụng. Nếu môi trường không chạy được tool, ghi rõ giới hạn. |
| Ví dụ cụ thể | Dù tất cả AI OK nhưng test fail thì NG. Nếu chỉ một AI chỉ ra authorization leak critical, dừng để Human Review. |
| Quy mô đo thực tế | Khoảng 763 dòng / khoảng 15436 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Tư tưởng cơ bản
- 2. Điều kiện áp dụng
- 3. Verification Pipeline
- 4. Required Tool Matrix
- 5. Tool Result Record
- 1. Metadata
- 2. Summary

**Điểm người mới cần hiểu:**

Không được dùng đa số AI để xóa một finding Security nghiêm trọng. Hãy dùng Veto Rule.

**Lưu ý khi đưa vào:**

- AI opinion là opinion; tool result và human review là evidence/decision quan trọng hơn.

---

### 44. `44_SDD_Token-Optimization-and-Cost-Control-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao kiểm soát token, cost và latency của Advanced Options.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Kết hợp nâng độ chính xác và chi phí vận hành thực tế. Nguyên tắc là không gửi, rút gọn, tái sử dụng, xử lý rẻ hơn. |
| Khi dùng | Multi-Agent, RAG, log lớn, repo lớn, review dài,案件 muốn quản lý API cost. |
| Hiệu quả chính | Ngăn cost bùng nổ do gửi mọi tài liệu cho mọi Agent, log full-text, cache không hit, tái phân tích vô ích. |
| Phán đoán áp dụng | Gần như bắt buộc khi dùng 42/46/47/49. Dùng 43 để kiểm chứng không cắt mất căn cứ cần thiết. |
| Ví dụ cụ thể | Cố định common prefix, đặt thông tin thay đổi mỗi lần như PR diff ở phía sau, nén test log chỉ còn phần thất bại. |
| Quy mô đo thực tế | Khoảng 1076 dòng / khoảng 18979 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận tổng thể về Token Optimization
- 2. Điều kiện áp dụng
- 3. Architecture cơ bản của 44
- 4. Token Budget Controller
- 1. Metadata
- 2. Budget
- 3. Compression Strategy

**Điểm người mới cần hiểu:**

Giảm token không phải xóa thông tin. Đó là thiết kế để không gửi thông tin không cần thiết mà vẫn giữ căn cứ quan trọng.

**Lưu ý khi đưa vào:**

- Không hy sinh quality chỉ để giảm cost.

---

### 45. `45_SDD_Full-Security-and-Agentic-AI-Governance-Option_Ver.04_Japanese.md`

**Tổng quan:** Option security governance nâng cao bao gồm AI Agent, MCP, hooks, tool execution, tài liệu ngoài, CI/CD.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Bản Advanced của 25. Xử lý quyền hạn, tool, prompt injection, audit, incident response của Agentic AI. |
| Khi dùng | AI thực thi tool, dùng MCP/hooks, xử lý dữ liệu tương đương production, đưa AI vào PR Gate. |
| Hiệu quả chính | Ngăn quyền quá rộng, Tool Injection, Prompt Injection, rò rỉ secret, thao tác nguy hiểm do AI. |
| Phán đoán áp dụng | Nếu standard Security đủ thì dùng 25. Nếu Agent có write permission hoặc external connection thì dùng 45. |
| Ví dụ cụ thể | Bắt đầu AI ở read-only; cho phép đề xuất patch nhưng cấm push/merge/deploy; bắt buộc human approval. |
| Quy mô đo thực tế | Khoảng 1203 dòng / khoảng 24512 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận quan trọng nhất của 45
- 2. Kết nối với 21〜44
- 3. Điều kiện áp dụng
- 4. Nguyên tắc cơ bản
- 5. Agentic AI Threat Model
- 6. Agentic AI Security Architecture
- 7. Agent Permission Matrix

**Điểm người mới cần hiểu:**

Trước khi cấp quyền tiện lợi cho AI, cần thiết kế để giảm thiểu thiệt hại khi AI nhầm, bị injection hoặc rò rỉ.

---

### 46. `46_SDD_RAG-CodeMap-and-Context-Compression-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao dùng RAG, Code Map, Context Compression để đưa căn cứ cần thiết cho AI với token thấp.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Nâng cấp context nối 31/41/44. Ngay cả repo lớn cũng đưa cho AI theo evidence-based context. |
| Khi dùng | Nhiều source, nhiều tài liệu thiết kế, Knowledge Library, RAG search, Code Map, long context. |
| Hiệu quả chính | Giảm quá tải thông tin, search miss, lost-in-the-middle, mất nghĩa do compression, đưa context không cần thiết. |
| Phán đoán áp dụng | Không cần cho案件 đơn giản. Khi đưa RAG vào, chú ý RAG poisoning và index cũ, để lại Evidence Pack. |
| Ví dụ cụ thể | Lấy từng bước: Repo Map → File Summary → function thay đổi → code xung quanh → test liên quan → chỉ khi cần mới lấy full text. |
| Quy mô đo thực tế | Khoảng 996 dòng / khoảng 18250 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận quan trọng nhất của 46
- 2. Kết nối với 21〜45
- 3. Điều kiện áp dụng
- 4. RAG / Code Map Architecture
- 5. Index Types
- 6. Repository Map
- Metadata

**Điểm người mới cần hiểu:**

Kết quả RAG search không phải lúc nào cũng đúng. Cần giữ Evidence và trust scoring.

---

### 47. `47_SDD_Automated-PR-Review-and-AI-QA-Gate-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao tích hợp PR review, CI, tool result, AI review, Policy, human review thành QA Gate.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Đưa AI review lên vận hành hiện trường. Không thay thế human review, mà dùng như quality gate ở bước trước. |
| Khi dùng | PR nhiều, tải review cao, muốn tích hợp CI result và AI review, muốn tạo security PR Gate. |
| Hiệu quả chính | Phát hiện sớm vấn đề rõ ràng, đồng nhất góc nhìn review, tự động block critical risk, tạo feedback loop. |
| Phán đoán áp dụng | Giai đoạn đầu nên non-blocking. Đo false positive rate và valid finding rate bằng 49 rồi tăng dần điều kiện block. |
| Ví dụ cụ thể | SAST critical, phát hiện secret, test failure, không có DB rollback, authorization change thì block hoặc bắt buộc Human Review. |
| Quy mô đo thực tế | Khoảng 1009 dòng / khoảng 19610 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận quan trọng nhất của 47
- 2. Kết nối với 21〜46
- 3. Điều kiện áp dụng
- 4. PR Review Architecture
- 5. PR Risk Classifier
- 6. Trigger Policy
- 7. Minimal GitHub Actions Pattern

**Điểm người mới cần hiểu:**

AI PR Review không thay thế human review. Hãy đưa vào như QA Gate ở bước trước.

---

### 48. `48_SDD_Parallel-Worktree-and-Large-Refactoring-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao dùng Git worktree và nhiều phương án implementation để tiến hành refactor lớn hoặc AI song song an toàn.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Kiểm soát song song hóa và thay đổi lớn. Không chỉ để nhanh hơn, mà để ngăn diff lẫn lộn, artifact bất nhất, lỗi tích hợp. |
| Khi dùng | Refactor lớn, làm mới legacy, so sánh nhiều phương án, Strangler, Feature Flag, migration / rollout từng bước. |
| Hiệu quả chính | Ngăn conflict cùng file, không rõ phương án nào đúng, không thể rollback, tích hợp khi thiếu test. |
| Phán đoán áp dụng | Tiền đề là quản lý artifact bằng 33 và kiểm chứng tool bằng 43. Không dùng cho sửa nhỏ. |
| Ví dụ cụ thể | Tách worktree: phương án A sửa tối thiểu, B cải thiện cấu trúc, C thiết kế migration; so sánh bằng cùng một test matrix. |
| Quy mô đo thực tế | Khoảng 1759 dòng / khoảng 31854 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận quan trọng nhất của 48
- 2. Kết nối với 21〜47
- 3. Điều kiện áp dụng
- 4. Khái niệm cơ bản
- 5. Pattern song song hóa tiêu biểu
- 6. Flow tổng thể của 48
- 7. Danh sách artifact

**Điểm người mới cần hiểu:**

Song song hóa nhanh hơn nhưng tích hợp khó hơn. Hãy quyết định tiêu chí so sánh và quy trình tích hợp trước.

---

### 49. `49_SDD_Evaluation-Observability-and-Continuous-Optimization-Option_Ver.04_Japanese.md`

**Tổng quan:** Option nâng cao đánh giá, quan sát và cải tiến chính hệ thống AI development; xử lý metrics, trace, dataset, dashboard.

| Góc nhìn | Nội dung |
|---|---|
| Vị trí | Đo hiệu quả toàn bộ Advanced Options. Trực quan hóa AI có thực sự hữu ích và có xứng chi phí không. |
| Khi dùng | AI PR Gate, Multi-Agent, RAG, token optimization, cải tiến liên tục, triển khai tổ chức, audit. |
| Hiệu quả chính | Không cải tiến bằng số lượng comment AI mà bằng valid finding rate, false positive rate, miss rate, cost per valid finding. |
| Phán đoán áp dụng | Bắt buộc nếu vận hành liên tục nhóm 40. Ngay cả thử nghiệm đơn lẻ cũng nên để lại metrics nhẹ. |
| Ví dụ cụ thể | Hàng tháng xem valid finding rate, False Positive, Missed Bug, token/PR, cache hit, Human Override để cải tiến prompt và Gate. |
| Quy mô đo thực tế | Khoảng 1940 dòng / khoảng 34593 ký tự |

**Các chương chính:**

- 0. Vai trò của tài liệu này
- 1. Kết luận quan trọng nhất của 49
- 2. Kết nối với 21〜48
- 3. Đối tượng quan sát của 49
- 4. AI Development Observability Architecture
- 5. Thiết kế Trace
- 6. Metrics Taxonomy
- 7. Quality Metrics

**Điểm người mới cần hiểu:**

Không xem lượng dùng AI là thành quả. Hãy đánh giá bằng valid finding rate, false positive rate, miss rate và cost efficiency.

---

## 9. So sánh các nhóm file: nhìn giống nhau nhưng khác nhau

Trong SDD V04 có các file có tên hoặc vai trò gần giống nhau. Bảng dưới đây sắp xếp các cặp dễ nhầm lẫn.

| So sánh | Khác nhau |
|---|---|
| 21 và 22 | 21 là quy trình, 22 là prompt. 21 nói “làm gì”, 22 nói “yêu cầu AI như thế nào”. |
| 23 và 41 | 23 là Source Intelligence thông thường, 41 là Heavy Source Analysis nâng cao. Nếu 23 đủ thì không cần 41. |
| 24 và 43 | 24 là góc nhìn review, 43 là kiểm chứng bằng tool evidence và consensus. 24 là mắt nhìn của người/AI, 43 là phán đoán dựa trên bằng chứng. |
| 25 và 45 | 25 là Security Gate tiêu chuẩn, 45 là Security Governance nâng cao gồm Agentic AI, MCP/hooks/tool permission. |
| 26 và 27 | 26 là FE/BE contract, 27 là microservice / multi-repo. Chỉ API contract thì 26; nếu liên quan ranh giới service, event, deploy thì 27. |
| 28 và 40 | 28 là phán đoán độ sâu áp dụng toàn bộ SDD, 40 là selection guide cho Advanced Options. Khi 28 ra Heavy/Critical thì đi tiếp sang 40. |
| 29 và 34 | 29 đăng ký thất bại và vòng cải tiến, 34 biến bài học đó thành tri thức dự án để AI tái sử dụng. |
| 31 và 46 | 31 là chính sách đưa gì cho AI, 46 là option nâng cao thực sự truy xuất và nén thông tin cần thiết bằng RAG/Code Map/Compression. |
| 32 và 33 | 32 giữ trạng thái cho công việc dài, 33 quản lý bản chính/chứng tích của artifact. Cả hai đều ghi chép nhưng đối tượng khác nhau. |
| 42 và 47 | 42 là thiết kế Multi-Agent, 47 là vận hành đưa nó vào PR review / QA Gate. |
| 44 và 46 | 44 kiểm soát token/cost toàn thể, 46 là phương thức cụ thể cho RAG/Code Map/context compression. |
| 48 và 41 | 41 đào sâu phân tích, 48 song song hóa và triển khai từng bước thay đổi quy mô lớn. |
| 49 và 29 | 29 học xoay quanh Failure Mode, 49 đánh giá toàn bộ hệ thống AI development bằng metrics/dataset. |

---

## 10. Lộ trình đưa vào dự án

Khi đưa SDD V04 vào hiện trường, không dùng tất cả file cùng lúc. Hãy triển khai theo giai đoạn.

### 10.1 Day 0: Chuẩn bị đưa vào

- Dùng 10 và 11 để giải thích toàn cảnh.
- Phát 21 và 22 như tiêu chuẩn Core.
- Dùng 28 để phân loại案件.
- Dùng 25 và 31 để quyết định cách xử lý thông tin bí mật, tài liệu ngoài, Context.
- Dùng 33 để quyết định nơi đặt artifact và quy tắc đặt tên.

### 10.2 Week 1: Thử nhỏ

- Dùng 21/22/23/24/28 trong 1〜2案件 thông thường.
- Không cố điền mọi thứ hoàn hảo; chỉ tạo Spec Pack, Impl Plan, Review Checklist, Test Results ở mức tối thiểu.
- Đăng ký điểm chưa tốt vào 29.
- Đăng ký ví dụ implementation đúng đặc thù dự án vào 34.

### 10.3 Month 1: Chuẩn hóa vận hành

- Dùng 11 như README của dự án.
- Thiết lập Context Loading Policy bằng 31.
- Dùng template bàn giao cho công việc dài bằng 32.
- Vận hành Traceability Matrix bằng 33.
- Điều chỉnh góc nhìn review của 24 theo dự án.

### 10.4 Quarter 1: Đưa Advanced vào

- Dùng 40 để phán đoán đưa Advanced Options vào.
- Với repo phức tạp đưa 41, Multi-Agent đưa 42, Tool verification đưa 43, token/cost đưa 44.
- Nếu có MCP/hooks/tool execution thì bắt buộc 45.
- Nếu cần RAG hoặc Code Map thì đưa 46.
- PR review automation bắt đầu từ non-blocking bằng 47.
- Refactor lớn dùng 48 để tách worktree.
- Bắt đầu đo hiệu quả bằng 49.

---

## 11. Ví dụ áp dụng theo loại案件 / loại việc

### Kịch bản A: Sửa wording nhỏ

Dùng quy trình đơn giản của 21, prompt nhẹ của 22, phán đoán Light bằng 28. Không cần 23〜49. Artifact chỉ cần memo đơn giản và xác nhận cuối cùng.

### Kịch bản B: Thêm field cho API thông thường

Dùng 21/22/23/24/28/31/33. Xác nhận API specification, DTO, DB, test; thêm số, null, số chữ số, quyền hạn vào Review Checklist.

### Kịch bản C: Thêm màn hình trong FE/BE tách biệt

Dùng 21/22/23/24/26/28/31/33. Tạo FE/BE Contract Map, Validation Parity, Error Message Map, Contract Test.

### Kịch bản D: Thay đổi event của microservice

Dùng 23/24/25/27/28/31/33/40/43. Kiểm tra Producer/Consumer, tương thích schema, DLQ, retry, thứ tự deploy, rollback.

### Kịch bản E: Thay đổi logic authorization

Dùng 25/31/33/43/45/47. Không chỉ phán đoán bằng AI; bắt buộc SAST, test và Human Security Review.

### Kịch bản F: Phân tích legacy khổng lồ

Dùng 23/31/33/40/41/44/46. Không đưa full text cho AI ngay; tạo Repository Map, Code Map, Risk Hotspot, Context Budget.

### Kịch bản G: Đưa nền tảng AI PR review vào

Dùng 40/42/43/44/45/47/49. Bắt đầu non-blocking, xem valid finding rate và false positive rate rồi tăng cường Gate.

### Kịch bản H: Refactor quy mô lớn

Dùng 21/23/24/28/33/40/41/43/44/48/49. Tách phương án theo worktree, so sánh bằng test matrix, tích hợp vào PR cuối.

---

## 12. Phiếu assessment khi đưa vào áp dụng

Khi bắt đầu dự án, hãy trả lời các câu hỏi sau. Càng nhiều “Yes”, càng cần extension tiêu chuẩn hoặc Advanced Options.

| Câu hỏi | Cách xử lý |
|---|---|
| AI có đọc được latest source không | Nếu No thì bắt buộc 23/31. Không được suy đoán nếu không đọc được. |
| Có thể xác nhận DB definition / migration / ERD không | Nếu No, độ chính xác của SQL/Repository change giảm. Ghi vào Source Availability. |
| FE và BE có tách biệt không | Nếu Yes, xem xét 26. Xác nhận API contract, Validation, Error, Permission. |
| Có liên quan nhiều service / nhiều repo không | Nếu Yes, xem xét 27 hoặc 41. |
| Có liên quan authentication / authorization / personal data / payment không | Nếu Yes, xem xét 25/43/45/47. |
| Có đưa tài liệu ngoài, Office, PDF, Web, OSS README cho AI không | Nếu Yes, dùng 31 và 25. Cần bản trích xuất và biện pháp chống Prompt Injection. |
| AI có thực thi tool không | Nếu Yes, dùng 45. Cần quyền hạn, audit, human approval. |
| Có đưa AI review vào PR Gate không | Nếu Yes, dùng 43/47/49. Khuyến nghị bắt đầu non-blocking. |
| token/cost có thể thành vấn đề không | Nếu Yes, dùng 44/46. Cần Context Budget và compression. |
| Công việc dài / nhiều ngày không | Nếu Yes, dùng 32. Để lại Snapshot và Handoff. |
| Artifact có trải qua nhiều người không | Nếu Yes, dùng 33. Cần artifact status và traceability. |
| Có lặp lại cùng lỗi trong quá khứ không | Nếu Yes, dùng 29/34. Cần Failure Mode và Knowledge hóa. |

---

## 13. Ưu điểm và nhược điểm

### 13.1 Ưu điểm của toàn bộ SDD V04

- Giảm dao động output của AI.
- Trực quan hóa liên kết giữa specification, implementation, review và test.
- Giúp AI phân tích source phức tạp dựa trên căn cứ.
- Giảm bỏ sót góc nhìn trong human review.
- Chuẩn hóa cách xử lý security và thông tin bí mật.
- Phản ánh thất bại vào rule, test, Knowledge cho lần sau.
- Đo được hiệu quả ứng dụng AI bằng metrics.

### 13.2 Nhược điểm / lưu ý của toàn bộ SDD V04

- Lần đầu có thể thấy nhiều artifact và có chi phí học tập.
- Nếu áp dụng quá mức cho sửa nhỏ sẽ nặng.
- Nếu chỉ tạo artifact rồi hài lòng thì sẽ hình thức hóa.
- Nếu không cập nhật Failure Mode và Knowledge, cải tiến liên tục sẽ dừng.
- Advanced Options có thể phản tác dụng nếu không quản lý token/cost/security.

### 13.3 Biện pháp xử lý nhược điểm

| Vấn đề | Biện pháp |
|---|---|
| Nặng | Dùng 28 để Right-size và phân biệt Light/Standard/Heavy |
| Nhiều file | Dùng 10 và 11 làm cửa vào, dùng bộ tối thiểu theo案件 |
| AI tin tài liệu cũ | Dùng 31 để quản lý Source Priority và Freshness |
| Artifact tăng quá nhiều | Dùng 33 để quản lý Artifact Status và bản chính |
| AI review quá ồn | Dùng 49 để đo False Positive rate và điều chỉnh Gate của 47 |
| token/cost cao | Dùng 44 và 46 cho Context Budget, Caching, Compression |
| Lo security | Dùng 25 và 45 để governance quyền hạn, MCP, hooks, tài liệu ngoài |

---

## 14. Ví dụ cấu trúc thư mục tiêu chuẩn khi dùng tại hiện trường

```text
docs/
  sdd/
    00_README.md
    phase0/
      safety-gate.md
      source-availability.md
      context-manifest.md
    tickets/
      TICKET-1234/
        spec-pack.md
        impact-analysis.md
        impl-plan.md
        review-checklist.md
        self-review.md
        codex-review.md
        test-plan.md
        test-results.md
        final-report.md
        traceability-matrix.md
    architecture/
      system-map.md
      source-inventory.md
      api-map.md
      db-map.md
      service-catalog.md
    project-knowledge/
      glossary.md
      coding-patterns.md
      known-good-examples.md
      known-bad-examples.md
      framework-constraints.md
    failure-modes/
      failure-mode-index.md
    evaluation/
      golden-pr-dataset.md
      ai-review-metrics.md
```

Cấu trúc này chỉ là ví dụ. Điều quan trọng là biết artifact nằm ở đâu, cái nào là bản chính, cái nào đã cũ, AI được phép đọc gì.

---

## 15. Những lỗi thường gặp và cách xử lý

| Lỗi | Cách xử lý |
|---|---|
| Nghĩ rằng cho AI đọc tất cả sẽ tăng độ chính xác | Dùng 31/44/46 và chỉ đưa thông tin cần thiết. |
| Tạo Spec Pack nhưng không cập nhật | Dùng 33 kiểm tra Artifact Freshness, không kết thúc bằng việc chỉ cập nhật Report. |
| Review Checklist quá dài nên không được dùng | Dùng 28 để giới hạn góc nhìn theo Mode. Bắt đầu từ góc nhìn bắt buộc của 24. |
| Xem AI review là đúng | Dùng 43 kết hợp tool evidence và Human Review. |
| PR Gate ban đầu quá nghiêm | Bắt đầu 47 ở non-blocking, đo hiệu quả bằng 49 rồi tăng dần. |
| Đưa MCP/hooks vào vì tiện | Kiểm tra quyền, audit, phạm vi thực thi bằng 25/45 trước. |
| Cùng lỗi AI tái diễn | Đăng ký Failure Mode bằng 29 và nâng cấp sang 34/24/47. |
| Merge refactor lớn một lần | Dùng 48 để thiết kế worktree, feature flag, rollback, test matrix. |
| Đo hiệu quả AI bằng số comment | Dùng 49 xem valid finding rate, miss rate, cost per valid finding. |

---

## 16. Cách dùng trong đào tạo và training

### 16.1 Training 2 giờ

```text
00:00-00:20  Khác nhau giữa AI-driven development và SDD
00:20-00:40  Học quy trình Core và prompt bằng 21/22
00:40-01:00  Học Source Intelligence và Review bằng 23/24
01:00-01:20  Học Right-sizing, Context, Artifact bằng 28/31/33
01:20-01:40  Học thời điểm dùng Advanced Options nhóm 40
01:40-02:00  Bài tập: chọn file dùng cho案件 của mình
```

### 16.2 Workshop 1 ngày

```text
AM: Cơ bản
  - Tổng quan SDD
  - Tạo Spec Pack
  - Tạo Impl Plan
  - Tạo Review Checklist
PM: Thực hành
  - Tạo Source Map cho案件 thực tế
  - Thực hiện AI review
  - Tạo Test Plan / Results
  - Đăng ký Failure Mode
  - Assessment đưa vào áp dụng
```

---

## 17. FAQ

### Q1. Có bắt buộc đọc toàn bộ file không?

Không. Nắm toàn cảnh bằng 10 và 11, rồi dùng 28 để chọn file cần thiết.

### Q2. SDD có làm chậm phát triển không?

Nếu áp dụng quá mức cho案件 nhỏ thì có. Vì vậy cần Right-sizing. Với案件 từ trung bình trở lên, có thể kỳ vọng giảm rework và bỏ sót review.

### Q3. Nếu AI giỏi thì Spec Pack có còn cần không?

Vẫn cần. Dù AI giỏi, business specification, điểm chưa xác định, phán đoán con người và ràng buộc hiện có vẫn phải được làm rõ.

### Q4. Chỉ AI review có đủ không?

Không đủ với案件 rủi ro cao. Cần kết hợp AI review, tool evidence và human review.

### Q5. Khi nào dùng nhóm 40?

Khi 28 phán đoán Heavy/Critical, hoặc khi đưa vào AI PR Gate, RAG, Multi-Agent, refactor quy mô lớn.

### Q6. Có thể đưa vào dự án hiện có giữa chừng không?

Có. Trước hết đưa 11/28/31/33, sau đó vận hành nhẹ 21/22, rồi dần mở rộng sang 23/24/29/34.

### Q7. Artifact có quá nhiều không?

Nhìn thì nhiều, nhưng không phải tạo tất cả mỗi lần. Chọn bộ tối thiểu theo rủi ro案件.

### Q8. SDD có mâu thuẫn với Agile không?

Không. SDD là cách hỗ trợ ticket work trong sprint bằng artifact về specification, implementation, review, test và learning.

### Q9. Có thể vừa giảm token AI vừa tăng độ chính xác không?

Có. 44/46 giúp đưa chỉ thông tin cần thiết với mật độ cao và không gửi thông tin thừa.

### Q10. Bộ tối thiểu nên đưa vào đầu tiên là gì?

10, 11, 21, 22, 28. Trong thực development, nên đưa 23, 24, 31, 33 vào sớm.

---

## 18. Chính sách vận hành khuyến nghị cho BVN-SDD

Khi đưa BVN-SDD vào dự án, có thể đặt các chính sách sau làm tiêu chuẩn vận hành.

1. Mọi案件 đều thực hiện phán đoán áp dụng bằng 28.
2. Từ Standard trở lên, để lại Spec Pack, Impl Plan, Review Checklist, Test Results, Final Report.
3. Context đưa cho AI được nêu rõ bằng 31; về nguyên tắc loại trừ thông tin bí mật và production log.
4. Nếu lo ngại về source analysis, dùng 23; nếu phức tạp hơn, dùng 41.
5. FE/BE tách biệt dùng 26; microservice dùng 27.
6. Nếu có ảnh hưởng Security, dùng 25; nếu có quyền Agent nâng cao, dùng 45.
7. AI review tạo góc nhìn bằng 24 và đối chiếu với tool evidence bằng 43.
8. PR automation bắt đầu non-blocking bằng 47.
9. Quản lý token/cost bằng 44, RAG/Code Map bằng 46.
10. Công việc song song quy mô lớn dùng 48, đo hiệu quả dùng 49.
11. Thất bại đăng ký vào 29 và Knowledge hóa bằng 34.
12. Bản chính artifact và chứng tích được quản lý bằng 33.

---

## 19. Chỉ số thành công

Thành công của SDD V04 không được đo bằng số lần dùng AI hay số ký tự sinh ra. Nên xem các chỉ số sau.

| Phân loại | Chỉ số | Ý nghĩa |
|---|---|---|
| Chất lượng | Số sự cố production | Sự cố nghiêm trọng có giảm trước/sau khi đưa vào không |
| Chất lượng | Số rework sau review | Bỏ sót trong review có giảm không |
| AI review | Valid finding rate | Tỷ lệ finding của AI thực sự có giá trị |
| AI review | False positive rate | Finding không cần thiết / sai của AI có quá nhiều không |
| AI review | Miss rate | AI đã bỏ sót bao nhiêu vấn đề nghiêm trọng |
| Delivery | Review time | Thời gian human review có giảm phù hợp không |
| Delivery | Rework time | Thời gian làm lại do specification mơ hồ có giảm không |
| Cost | token/PR | Token trên mỗi PR có tăng quá mức không |
| Cost | cost per valid finding | Chi phí AI trên mỗi finding có giá trị |
| Process | Tỷ lệ tái diễn Failure Mode | Failure Mode đã đăng ký có tái diễn không |
| Process | Artifact Freshness | Có còn artifact cũ không |

---

## 20. Thông điệp cuối cùng

Bản chất của SDD V04 không phải làm AI mạnh hơn. Bản chất là tạo hiện trường nơi AI có thể làm việc mạnh mẽ.

Điều thật sự khó trong AI-driven development không chỉ là chọn model. Cần thiết kế AI đọc gì, không đọc gì, được cấp quyền nào, artifact nào là bản đúng, review nào cần qua, thất bại nào được dùng cho lần sau.

Theo nghĩa đó, SDD V04 không chỉ là quy trình phát triển, mà là một hệ thống tích hợp development governance, quality assurance, knowledge management và continuous improvement cho thời đại AI.

Ban đầu chỉ dùng 21 và 22 cũng được. Sau đó thêm 23, 24, 28; nếu hiện trường gặp vấn đề thì thêm 31, 33, 29, 34. Khi案件 phức tạp, chọn nhóm 40. Điều quan trọng không phải đưa vào một hệ thống hoàn hảo ngay lập tức, mà là chọn đúng theo từng案件, biến thất bại thành học tập và khiến cả team thông minh hơn từng chút một.

BVN-SDD không phải cơ chế để giao phó development cho AI. Đây là cơ chế để con người chịu trách nhiệm, tận dụng tối đa AI, và thông qua specification, chứng tích, review, test, learning để đạt development an toàn hơn và chất lượng cao hơn.

---

## 21. Cách sử dụng chi tiết theo vai trò

Cách nhìn SDD V04 thay đổi theo vai trò của người đọc. Cùng một file nhưng developer, reviewer, PM, QA, Security, SRE sẽ chú trọng các điểm khác nhau. Bảng dưới đây sắp xếp theo vai trò: cần xem gì, tạo artifact nào và phán đoán điều gì.

| Vai trò | File chủ yếu đọc | Mục đích | Artifact chính | Lưu ý |
|---|---|---|---|---|
| Developer | 21,22,23,24,28,31,33 | Giảm mơ hồ specification, xác định phạm vi thay đổi và góc nhìn review trước khi yêu cầu AI implement. | Spec Pack, Impl Plan, Review Checklist, Test Results, Final Report | Không tin code AI đưa ra một cách mù quáng. Luôn xác nhận Source Availability và Test Results. |
| Reviewer | 24,26,27,33,43,47 | Cấu trúc hóa góc nhìn review, tích hợp AI review, tool result và phán đoán con người. | Review Findings, Consensus Record, Human Approval Record | Không nhìn số lượng comment AI; nhìn finding nghiêm trọng, căn cứ và tính tái lập. |
| PM/PL | 10,11,28,33,49 | Quyết định phạm vi đưa SDD vào, quản lý artifact, tiến độ, rủi ro, hiệu quả. | Right-sizing Decision, Traceability Matrix, Evaluation Summary | Không áp dụng cùng một độ nặng cho mọi案件. Áp dụng quá mức cũng là rủi ro chất lượng. |
| QA / Tester | 24,26,27,33,43,47,49 | Quản lý liên kết giữa specification và test, Contract Test, Regression, E2E, xu hướng lỗi. | Test Plan, Test Results, QA Gate Record, Missed Bug Record | Ghi rõ lý do và ràng buộc nếu không thực hiện test. |
| Security | 25,31,33,43,45,47 | Quản lý secret, tài liệu ngoài, MCP/hooks, quyền AI, SAST/SCA/Secrets, Prompt Injection. | Threat Model, Security Review, MCP Review, Security Gate Record | Khi thiết kế quyền cho AI, ưu tiên giảm thiệt hại hơn sự tiện lợi. |
| SRE / Ops | 24,27,33,43,48,49 | Kiểm tra log, monitoring, rollback, retry, idempotency, ứng phó sự cố, chứng tích vận hành. | Runbook, Rollback Plan, Observability Record | Code đúng nhưng không vận hành được thì vẫn chưa đủ. |
| Người thúc đẩy AI | 11,34,40,42,44,46,47,49 | Thiết kế tiêu chuẩn dùng AI, token/cost, RAG, PR Gate, đánh giá Agent, cải tiến liên tục. | AI Policy, Agent Scorecard, Token Audit, Evaluation Dataset | Không đo thành công AI bằng số lần dùng, mà bằng valid finding rate, productivity và quality. |

---

## 22. Ý nghĩa và cách tạo từng artifact

Trong SDD V04 xuất hiện nhiều artifact. Người mới thường vướng ở câu hỏi “vì sao phải viết nhiều tài liệu như vậy”. Artifact không phải mục đích tự thân. Chúng là sản phẩm trung gian giúp AI và con người làm việc với cùng tiền đề, cùng căn cứ và cùng tiêu chí phán đoán.

| Artifact | Nội dung | File liên quan chính | Hiệu quả | Lưu ý |
|---|---|---|---|---|
| Source Availability Report | Ghi AI đã đọc được gì / chưa đọc được gì: source, DB, tài liệu thiết kế, test, external IF. | 23,26,27,41 | Ngăn AI suy đoán do thiếu thông tin. | Không bù thông tin không đọc được bằng “có lẽ”. |
| Spec Pack | Tổng hợp specification, bối cảnh, AC, ràng buộc, điểm chưa xác định, việc cần con người xác nhận. | 21,22 | Đồng bộ hiểu biết specification giữa AI và người. | Nếu specification đổi sau implementation, phải cập nhật. |
| Impact Analysis | Sắp xếp màn hình, API, DB, batch, service, test bị ảnh hưởng bởi thay đổi. | 23,26,27,41 | Ngăn bỏ sót. | Không chỉ liệt kê tên file; viết lý do bị ảnh hưởng. |
| Impl Plan | Thiết kế thứ tự, file và phương châm thay đổi. | 21,22 | Tạo kế hoạch implementation có thể review. | Không viết quá nhiều code full text trước. |
| Review Checklist | Sắp xếp góc nhìn specification, số, ký tự, FE/BE, DB, Security, vận hành, test. | 24 | Giảm bỏ sót review. | Không dùng mọi góc nhìn mỗi lần; chọn theo rủi ro. |
| Self Review | AI hoặc chính developer nhìn lại thay đổi sau implementation. | 21,22,24 | Giảm bất nhất rõ ràng trước human review. | Tránh tự hợp lý hóa; nhìn bằng chứng và diff. |
| Codex / Independent Review | Review độc lập bằng AI khác hoặc góc nhìn khác. | 24,42,43 | Giảm bỏ sót của AI đơn lẻ. | Arbiter hoặc con người xử lý trùng lặp / false positive. |
| Test Plan | Định nghĩa test gì ở level nào. | 21,24,26,27 | Kết nối specification với test. | Nếu không test, ghi lý do. |
| Test Results | Ghi kết quả chạy test, thất bại, chạy lại, lý do chưa chạy. | 21,24,43 | Là căn cứ cho phán đoán chất lượng. | Thay vì dán nhiều passed list, hãy trọng tâm vào thất bại, diff, decision. |
| Final Report | Tổng hợp thay đổi, căn cứ, review, test, rủi ro còn lại, phán đoán con người. | 21,33 | Dùng cho hoàn tất và bàn giao. | Không chỉ cập nhật Final Report mà để Spec Pack cũ. |
| Traceability Matrix | Truy vết từ requirement đến implementation, test, review, final decision. | 33 | Dùng cho audit, QA, xác nhận ảnh hưởng thay đổi. | Càng lớn càng bắt buộc. |
| Failure Mode Entry | Đăng ký pattern thất bại, nhầm lẫn, bỏ sót review, sự cố. | 29 | Dùng cho phòng tái diễn và cải tiến liên tục. | Không công kích cá nhân; nối tới cải tiến cơ chế. |
| Knowledge Card | Tích lũy tri thức đặc thù dự án ở dạng AI có thể đọc. | 34 | Tăng độ chính xác cho lần làm việc AI sau. | Kiểm kê tri thức cũ. |
| Advanced Option Selection Record | Ghi dùng option nào nhóm 40 và vì sao. | 40 | Ngăn áp dụng quá mức quy trình nâng cao. | Ghi cả lý do không dùng. |
| Token Budget Record | Ghi ngân sách token/cost, phương châm compression, điều kiện dừng. | 44 | Ngăn cost bùng nổ trong AI operation nâng cao. | Không cắt mất căn cứ do cắt quá tay. |
| QA Gate Record | Ghi decision cho PR: pass/block/chuyển human review. | 47 | Để lại căn cứ phán đoán của AI PR Gate. | Không merge chỉ dựa trên AI decision. |
| Evaluation Run Record | Ghi lần chạy đánh giá hệ thống AI development, dataset, kết quả. | 49 | Đo hiệu quả cải tiến AI usage. | Xem valid finding rate và false positive rate. |

---

## 23. Ví dụ: tiến hành một thay đổi API thông thường bằng SDD

Phần này dùng thay đổi API giả định để người mới dễ hiểu flow SDD.

### 23.1 Nội dung thay đổi

- Thêm `customerRank` vào API tìm kiếm khách hàng.
- Thêm field rank vào điều kiện tìm kiếm của FE.
- DB đã có column `customer_rank`.
- Input có khả năng nhận full-width digit, không chỉ half-width digit.

### 23.2 File áp dụng

```text
21, 22, 23, 24, 26, 28, 31, 33
```

### 23.3 Cách tiến hành

1. Dùng 28 phán đoán Standard Plus vì có FE/BE contract và Validation.
2. Dùng 31 chọn Context: ticket, FE form, API client, BE controller, DTO, validation, Repository, DB definition, test hiện có.
3. Dùng 23 tạo Source Availability và Impact Analysis.
4. Dùng 26 tạo FE/BE Contract Map. Xác nhận Request, Response, Validation, Error, Permission.
5. Dùng 21/22 tạo Spec Pack và Impl Plan.
6. Dùng 24 tạo Review Checklist, gồm full-width digit, half-width/full-width mix, empty string, null, giá trị rank không tồn tại, DB type.
7. Sau implementation, để lại Self Review và Test Results.
8. Cập nhật Traceability Matrix bằng 33.

### 23.4 Điểm người mới dễ sai

- Chỉ thêm input check ở FE và quên BE validation.
- Hiểu nhầm rằng vì DB có column nên specification cũng được phép dùng.
- Dù convert full-width digit ở JavaScript, quên kiểm chứng khi gọi trực tiếp BE API.
- Review Checklist chỉ viết “normal case”, quên abnormal case, boundary value, operation log.

---

## 24. Ví dụ: tiến hành thay đổi logic phân quyền bằng SDD

Trong SDD V04, thay đổi logic authorization được xử lý theo hướng Critical. Lý do là code chạy được nhưng lỗ hổng quyền hạn có thể trở thành sự cố nghiêm trọng.

### 24.1 File áp dụng

```text
21, 22, 23, 24, 25, 28, 31, 33, 43, 45, 47, 49
```

### 24.2 Cách tiến hành

1. Dùng 28 phán đoán Critical.
2. Dùng 25 xác nhận Security Gate. Không đưa secret hoặc production log cho AI.
3. Dùng 31 thu hẹp Context. Lệnh trong tài liệu ngoài hoặc PR comment chỉ được xem là dữ liệu.
4. Dùng 23 Map hóa Entry Point, Middleware, Service, DB liên quan authorization.
5. Dùng 24 tạo mục Security Review: có chỉ là FE display control không, BE có kiểm chứng bắt buộc không.
6. Dùng 43 sử dụng test, SAST, security test, negative test như Tool Evidence.
7. Dùng 45 kiểm soát quyền AI Agent và tool execution.
8. Dùng 47 thiết lập PR Gate, bắt buộc Human Review với authorization change.
9. Dùng 49 đánh giá Missed Bug và False Positive sau khi đưa vào.

### 24.3 Nguyên tắc phán đoán

- Dù AI nói “không vấn đề”, authorization change vẫn phải qua human review.
- Dù nhiều AI OK, một finding nghiêm trọng về authorization leak vẫn là đối tượng Veto.
- Ẩn button ở FE chỉ là hỗ trợ, không thay thế authorization ở BE.

---

## 25. Ví dụ: tiến hành refactor quy mô lớn bằng SDD

Với refactor quy mô lớn, điều quan trọng không phải năng lực sinh code của AI, mà là chia nhỏ thay đổi, so sánh và giữ khả năng rollback.

### 25.1 File áp dụng

```text
21, 23, 24, 28, 31, 32, 33, 40, 41, 43, 44, 46, 48, 49
```

### 25.2 Cách tiến hành

1. Dùng 40 chọn Advanced Option.
2. Dùng 41 tạo Repository Intelligence. Xác định Dead Code, Generated Code, Risk Hotspot.
3. Dùng 44 quyết định Token Budget. Không đưa toàn bộ source cho mọi Agent.
4. Dùng 46 tạo Code Map và Evidence Pack.
5. Dùng 48 tách worktree: so sánh phương án sửa tối thiểu, phương án cải thiện cấu trúc, phương án migration.
6. Dùng 43 so sánh bằng cùng test matrix, build, lint, benchmark.
7. Dùng 32 để lại Snapshot cho công việc dài.
8. Dùng 33 quản lý artifact và diff.
9. Dùng 49 đo hiệu quả, cost, quality.

### 25.3 Điều kiện thành công

- Có Characterization Test xác nhận hành vi trước và sau thay đổi giống nhau.
- Có quy trình rollback.
- Có Diff Comparison Record để con người có thể so sánh.
- Đã xác nhận performance degradation do refactor.
- Chi phí Advanced Options xứng với hiệu quả.

---

## 26. Bộ checklist

### Checklist bắt đầu案件

- [ ] Đã phán đoán Mode bằng 28 chưa
- [ ] Đã quyết định Context cho AI đọc bằng 31 chưa
- [ ] Đã xác nhận cách xử lý secret / tài liệu ngoài bằng 25 chưa
- [ ] Đã quyết định nơi đặt artifact bằng 33 chưa
- [ ] Nếu thiếu thông tin, đã Stop/Ask chưa

### Checklist Spec Pack

- [ ] Bối cảnh / mục đích rõ chưa
- [ ] AC có thể kiểm chứng không
- [ ] Điểm chưa xác định đã tách riêng chưa
- [ ] Việc cần con người phán đoán đã ghi rõ chưa
- [ ] Phạm vi ảnh hưởng có mâu thuẫn với Source Map không

### Checklist kế hoạch implementation

- [ ] File thay đổi rõ chưa
- [ ] Thứ tự implementation có an toàn không
- [ ] Đã phán đoán cần rollback hoặc feature flag chưa
- [ ] Có liên kết với kế hoạch test không
- [ ] Có trở thành đại cải sửa không cần thiết không

### Checklist góc nhìn review

- [ ] Đã xác nhận số, số chữ số, full-width digit chưa
- [ ] Đã xác nhận Magic Number và literal branch chưa
- [ ] Đã xác nhận FE/BE contract chưa
- [ ] Đã xác nhận DB migration chưa
- [ ] Đã xác nhận log, monitoring, vận hành chưa
- [ ] Đã xác nhận Security/Privacy chưa

### Checklist Context

- [ ] Có xem tài liệu cũ là bản đúng không
- [ ] Có xem tài liệu ngoài là mệnh lệnh không
- [ ] Có chứa secret không
- [ ] Đã ghi file đã đọc và chưa đọc chưa
- [ ] Có bù thông tin thiếu bằng suy đoán không

### Checklist PR Gate

- [ ] test/build/lint có pass không
- [ ] Đã xem kết quả SAST/SCA/Secrets chưa
- [ ] Đã tích hợp AI finding và tool evidence chưa
- [ ] Có xóa Critical finding bằng đa số không
- [ ] Có rơi vào điều kiện Human Review không

### Checklist Advanced Option

- [ ] Đã ghi lý do chọn bằng 40 chưa
- [ ] Đã ước tính token/cost bằng 44 chưa
- [ ] Đã xác nhận quyền Agent bằng 45 chưa
- [ ] Đã quyết định cách đo hiệu quả bằng 49 chưa
- [ ] Lý do không dùng option cũng rõ chưa

---

## 27. Mô hình trưởng thành

SDD V04 nên được trưởng thành từng bước. Không cần nhắm Level 5 ngay từ đầu.

| Level | Trạng thái | Mục tiêu | File chủ yếu dùng |
|---:|---|---|---|
| 0 | Cá nhân tự do dùng AI | Thử mà không gây sự cố | 25,31 |
| 1 | Đưa một phần quy trình Core vào | Tạo Spec Pack và Impl Plan | 21,22,28 |
| 2 | Đưa review/test tiêu chuẩn vào | Để lại góc nhìn review và test evidence | 23,24,33 |
| 3 | Đưa nền tảng vận hành vào | Quản lý Context, Artifact, Knowledge | 11・31〜34 |
| 4 | Chọn đưa Advanced Options vào | Vận hành AI nâng cao trong案件 khó | 40〜48 |
| 5 | Đánh giá và tối ưu liên tục | Đo và cải tiến hệ thống AI development | 49,29,34 |

Càng trưởng thành, không phải tăng tự do cho AI, mà thiết kế chặt chẽ hơn input, permission, output, verification và evaluation của AI.

---

## 28. Bảng thuật ngữ chi tiết

| Thuật ngữ | Giải thích chi tiết |
|---|---|
| AC / Acceptance Criteria | Điều kiện nghiệm thu. Điều kiện để nói implementation đã hoàn tất. “Có thể tìm kiếm” là mơ hồ; cần kiểm chứng được như “khi tìm với điều kiện A thì trả kết quả B”. |
| Hard Block | Điều kiện tuyệt đối không được tiếp tục. Ví dụ: cần đưa secret cho AI nhưng không thể mask, hoặc authorization change nhưng không thể human review. |
| Soft Guidance | Cảnh báo. Có thể tiếp tục nhưng phải ghi rủi ro và ràng buộc. |
| Human Review | Xác nhận cuối cùng bởi con người. Dù AI mạnh, trách nhiệm và phán đoán cuối cùng vẫn ở con người. |
| Veto Rule | Quy tắc dừng khi có finding rủi ro nghiêm trọng dù đa số nói OK. Hữu ích cho Security và Data Loss. |
| False Positive | Chỉ ra vấn đề dù thực tế không phải vấn đề. Đây là nguyên nhân khiến AI review trở nên ồn. |
| Missed Bug | Bug mà AI hoặc review bỏ sót. Đo bằng 49 và đăng ký Failure Mode vào 29. |
| Golden PR Dataset | Bộ PR đại diện để đánh giá AI review. Có đáp án / finding / missed finding đã biết, dùng cho regression evaluation khi đổi model hoặc prompt. |
| Feature Flag | Cơ chế bật/tắt tính năng bằng setting. Hữu ích cho thay đổi lớn và release theo giai đoạn. |
| Strangler Fig Pattern | Pattern migration thay thế hệ thống cũ dần từ xung quanh thay vì thay một lần. |
| Expand-Contract Migration | Cách migration an toàn cho DB/API: mở rộng tương thích trước, sau khi migrate xong mới thu hẹp phần không cần. |
| Idempotency | Tính chất chạy cùng xử lý nhiều lần mà kết quả không hỏng. Quan trọng với retry và distributed system. |
| DLQ / Dead Letter Queue | Queue lưu message không xử lý được. Dùng cho phân tích lỗi xử lý bất đồng bộ. |
| Correlation ID | ID để truy vết request / xử lý qua nhiều service và log. Quan trọng trong microservice và vận hành. |
| SBOM | Software Bill of Materials. Danh sách dependency và component, dùng quản lý supply-chain risk. |
| SAST | Static Application Security Testing. Phân tích tĩnh source code để phát hiện vulnerability. |
| SCA | Software Composition Analysis. Kiểm tra vulnerability và license của dependency. |
| MCP | Model Context Protocol. Cơ chế AI kết nối với tool hoặc dữ liệu ngoài. Tiện nhưng cần quản lý quyền. |
| hooks | Xử lý tự động chạy tại event cụ thể. Trong AI development tiện nhưng cần chú ý unexpected execution và permission incident. |
| Prompt Injection | Tấn công/sự cố trong đó lệnh nằm trong tài liệu ngoài hoặc input người dùng cố ghi đè chỉ thị gốc của AI. |
| RAG Poisoning | Vấn đề thông tin độc hại hoặc cũ đi vào tài liệu/index tìm kiếm, khiến AI dùng căn cứ sai. |

---

## 29. Quan hệ giữa hướng dẫn này và các file khác

`10_BVN-SDD_GuideLine.md` không thay thế 11 và 21〜29・31〜49. Vị trí của nó như sau.

- 10 là hướng dẫn tổng hợp giải thích toàn cảnh, thuật ngữ, quyết định áp dụng, đào tạo, cách dùng theo vai trò.
- 11 và 21〜29・31〜49 là tiêu chuẩn, template, prompt và checklist dùng trong vận hành thực tế.
- Người mới bắt đầu từ 10; khi làm thực tế, dùng 11 như bản đồ và tham chiếu file riêng cần thiết.
- 10 dùng cho đào tạo và giải thích triển khai; công việc cụ thể dùng 11 và 21〜29・31〜49.

---

## 30. Tóm tắt

SDD V04 không chỉ làm development trong thời đại AI “nhanh hơn”, mà là hệ thống để “an toàn hơn, chính xác hơn, tái lập hơn và liên tục cải tiến”.

Người mới trước hết chỉ cần nhớ 3 điều sau.

1. **Không giao phó cho AI. Tạo specification, căn cứ và tiêu chí phán đoán trước.**
2. **Không làm tất cả. Dùng 28 để Right-size và chỉ dùng file cần thiết.**
3. **Không trách thất bại. Dùng 29 và 34 biến nó thành tri thức cho lần sau.**

Chỉ cần tuân thủ 3 điều này, AI-driven development sẽ ổn định hơn nhiều. Với案件 phức tạp hơn, hãy đưa 23〜27, 31〜34, 40〜49 vào theo giai đoạn.

Đích đến của BVN-SDD không phải thế giới nơi AI tự ý development. Đích đến là thế giới nơi con người chịu trách nhiệm, dùng AI đúng cách, tích lũy specification, chứng tích, test, review, learning để đạt development chất lượng cao hơn, an toàn hơn và nhanh hơn.

---

## 31. Giải thích chi tiết về Harness Engineering

Harness Engineering là cách nghĩ không cải tiến chính model AI, mà thiết kế “môi trường xung quanh” nơi AI làm việc. Trong hiện trường AI development, chỉ nhìn vào hiệu năng model là không đủ. Nếu không thiết kế thông tin nào được đưa vào, quyền nào được cấp, tool nào dùng để kiểm chứng, artifact nào ghi lại và thời điểm nào trả về cho con người, AI dù mạnh vẫn không ổn định.

### 31.1 Thành phần của harness

| Lớp | Vai trò | File tương ứng trong SDD V04 |
|---|---|---|
| Input Harness | Kiểm soát thông tin đưa cho AI | 31, 46 |
| Process Harness | Kiểm soát Phase, quy trình, Agent, Orchestrator | 21, 22, 42 |
| Tool Harness | Thực thi test/build/lint/SAST và chỉnh dạng kết quả | 43, 47 |
| Permission Harness | Kiểm soát quyền AI, MCP, hooks, thao tác write | 25, 45 |
| Artifact Harness | Quản lý bản chính, chứng tích, traceability của artifact | 33 |
| Learning Harness | Biến thất bại thành Failure Mode và Knowledge | 29, 34 |
| Evaluation Harness | Đo hiệu quả hệ thống AI development | 49 |

### 31.2 Vì sao cần harness

AI có thể tạo ra câu trả lời nào đó dù input mơ hồ. Điều này tiện nhưng nguy hiểm với hệ thống nghiệp vụ. Ví dụ, AI tạo SQL dù thiếu DB definition, coi tài liệu thiết kế cũ là latest specification, coi lệnh trong web ngoài là chỉ thị thật, hoặc đọc toàn bộ test log rồi bỏ sót vị trí lỗi quan trọng.

Harness Engineering không kỳ vọng vào “sự cẩn thận của AI” để ngăn các vấn đề đó, mà ngăn bằng cơ chế. Trước khi đưa cho AI, chọn Context, loại trừ thông tin nguy hiểm, schema hóa output, kiểm chứng bằng tool, ghi vào artifact và để con người phán đoán ở điểm cần thiết.

### 31.3 Harness tốt và harness xấu

| Góc nhìn | Ví dụ xấu | Ví dụ tốt |
|---|---|---|
| Context | Đưa toàn bộ repository, tài liệu thiết kế, log cho AI | Dùng 31/46 chỉ Evidence Pack hóa thông tin cần thiết |
| Permission | Cho AI tự do command execution, push, merge | Dùng 45 tách read-only, patch proposal, human approval |
| Review | Đưa comment AI thẳng thành PR finding | Dùng 24/43 tích hợp góc nhìn và tool evidence |
| Cost | Đưa cùng context khổng lồ cho mọi Agent | Dùng 42/44 đặt Agent-specific Context và Token Budget |
| Learning | Khi thất bại thì đổ lỗi cho người phụ trách | Dùng 29 để Failure Mode hóa và 34 để Knowledge hóa |
| Evaluation | Xem số lần dùng AI là thành quả | Dùng 49 đo valid finding rate, false positive rate, miss rate |

---

## 32. Decision tree chi tiết để chọn file

Nếu phán đoán theo thứ tự sau, sẽ ít bị lúng túng khi chọn file cần dùng.

### 32.1 Step 1: Thay đổi này có thật sự là code change không

- Nếu chỉ README hoặc comment, Light với 21/22/28 là đủ.
- Nếu chạm execution logic, DB, API, Security, external IF thì đi Step 2.

### 32.2 Step 2: Phạm vi ảnh hưởng có rõ không

- Nếu rõ trong 1 file thì 21/22/24/28.
- Nếu nhiều file, nhiều layer, existing specification không rõ thì thêm 23/31/33.
- Nếu repo lớn hoặc legacy khiến phân tích thông thường không yên tâm thì thêm 41/46.

### 32.3 Step 3: FE/BE contract có thay đổi không

- Nếu Request/Response, DTO, Validation, Error, Permission thay đổi thì dùng 26.
- Nếu còn ảnh hưởng nhiều service thì dùng 27.

### 32.4 Step 4: Có liên quan Security hoặc Privacy không

- Nếu là góc nhìn Security thông thường thì dùng 25.
- Nếu liên quan authentication, authorization, personal data, AI tool execution, MCP/hooks thì dùng 45.
- Nếu cần dừng ở PR Gate thì dùng 43/47.

### 32.5 Step 5: Có nâng cao AI review hoặc automation không

- Nhiều Agent thì dùng 42.
- Tool evidence và Consensus thì dùng 43.
- Quản lý token/cost thì dùng 44.
- PR automated review thì dùng 47.
- Continuous evaluation thì dùng 49.

### 32.6 Step 6: Có công việc song song hoặc refactor lớn không

- So sánh nhiều phương án implementation, worktree, migration từng bước thì dùng 48.
- Công việc dài thì dùng 32; quản lý artifact dùng 33; đo hiệu quả dùng 49.

---

## 33. Ma trận phán đoán đưa vào áp dụng chi tiết

| Trigger | Ứng viên bắt buộc | Ứng viên khuyến nghị | Ứng viên Advanced | Ghi chú |
|---|---|---|---|---|
| Specification mơ hồ | 21,22 | 23,28 | 41 | Trước hết xác nhận specification và Source Availability |
| AI dễ đọc nhầm source | 23,31 | 33,34 | 41,46 | Bản đồ và kiểm soát Context rất quan trọng |
| Muốn tăng góc nhìn review | 24 | 29,34 | 43,47 | Không chỉ xem AI opinion mà cả tool result |
| Muốn tăng cường test code | 24 | 26,27 | 43,47 | Xem xét contract test và migration test |
| Liên quan Security | 25,31 | 33 | 43,45,47 | Chú ý quyền hạn và secret |
| FE/BE tách biệt | 26 | 23,24,31,33 | 43,47 | Tạo Contract Map |
| Microservice | 27 | 23,25,33 | 41,43,48 | Thứ tự deploy và rollback quan trọng |
| Sửa nhỏ | 21,22,28 | - | - | Không áp dụng quá mức |
| Công việc dài | 32 | 33 | 44,49 | Để lại Snapshot và handoff |
| Nhiều rule đặc thù dự án | 34 | 29,31 | 46 | Knowledge hóa |
| AI PR review | 47 | 43,45 | 42,44,49 | Bắt đầu từ non-blocking |
| token/cost lớn | 44 | 31 | 46,49 | Cẩn thận cắt quá tay |
| Refactor quy mô lớn | 48 | 33,41 | 43,44,49 | Song song hóa và quản lý tích hợp rất quan trọng |

---

## 34. Ví dụ RACI khi đưa vào áp dụng

RACI là bảng sắp xếp Responsible (chịu trách nhiệm thực hiện), Accountable (chịu trách nhiệm giải trình), Consulted (được tham vấn), Informed (được thông báo). Khi đưa SDD vào, dù AI hỗ trợ công việc, trách nhiệm giải trình vẫn ở phía con người.

| Hoạt động | Developer | Tech Lead | PM/PL | QA | Security | SRE | AI thúc đẩy |
|---|---|---|---|---|---|---|---|
| Phán đoán Right-sizing | R | A | C | C | C | C | C |
| Tạo Spec Pack | R | A | C | C | C | I | C |
| Source Intelligence | R | A | I | C | C | C | C |
| Tạo Review Checklist | R | A | I | C | C | C | C |
| Security Gate | C | A | I | I | R | C | C |
| Test Plan | R | C | I | A | C | C | I |
| Vận hành PR Gate | R | A | I | C | C | C | C |
| Đăng ký Failure Mode | R | A | I | C | C | C | C |
| Evaluation Review | C | A | C | C | C | C | R |

---

## 35. Kế hoạch triển khai 30 ngày

### Day 1-3: Tạo nền tảng

- Phát 10 và 11, giải thích toàn cảnh.
- Dùng 21/22 để tạo Spec Pack và Impl Plan cho một task nhỏ.
- Luyện phán đoán Light/Standard/Heavy bằng 28.
- Dùng 31 quyết định những gì không được đưa vào Context.

### Day 4-10: Chuẩn hóa

- Dùng 23 tạo Source Availability.
- Dùng 24 điều chỉnh góc nhìn review cho dự án.
- Dùng 25 quyết định mức tối thiểu của Security Gate.
- Dùng 33 tạo nơi đặt artifact.

### Day 11-20: Áp dụng案件 thực tế

- Áp dụng 21〜24 cho 2〜3案件 thông thường.
- Với FE/BE dùng thử 26; với nhiều service dùng thử 27.
- Dùng 29 đăng ký điểm thất bại hoặc điểm gây phiền.
- Dùng 34 đăng ký ví dụ implementation đúng và pattern cấm.

### Day 21-30: Cải tiến và phán đoán nâng cao

- Dùng 11/28 kiểm kê kết quả đưa vào.
- Nếu token/cost nặng, đưa 44 vào.
- Nếu cần AI review automation, thử 47 ở non-blocking.
- Định nghĩa KPI ban đầu bằng 49.

---

## 36. Đào sâu các góc nhìn review chất lượng

Trong SDD V04, review không chỉ xem “code có chạy không”, mà mở rộng đến việc hệ thống có thể vận hành an toàn hay không.

### 36.1 Review số và loại ký tự

- Với field số, kiểm tra không chỉ half-width digit mà cả full-width digit, dấu phẩy, số thập phân, số âm, chuỗi rỗng, null, giá trị lớn nhất, giá trị nhỏ nhất.
- Kiểm tra `number` của JavaScript, `int/long/BigDecimal` của Java, `precision/scale` của DB có khớp nhau không.
- Kiểm tra full-width space, half-width kana, emoji, surrogate pair, Unicode normalization có gây vấn đề không.

### 36.2 Review vận hành / bảo trì

- Khi có sự cố, có thể truy vết nguyên nhân từ log không.
- Có request id, correlation id không.
- Có retry được không, chịu được double execution không.
- Có quy trình khôi phục thủ công không.
- Cấu trúc có để người mới đọc cũng sửa được không.
- Comment và implementation có lệch nhau không.

### 36.3 Security review

- Kiểm tra input validation, authentication, authorization, audit log, secret, PII, external integration.
- Kiểm tra có đang tưởng rằng chỉ FE display control là đủ quyền hạn không.
- Kiểm tra log do AI tạo có xuất personal data hoặc secret không.

### 36.4 Review đặc thù AI

- AI có dùng method hoặc library không tồn tại không.
- AI có ưu tiên best practice chung hơn quy ước của dự án hiện có không.
- AI có xem tài liệu thiết kế cũ hoặc tài liệu ngoài là bản đúng không.
- AI có lấy chính output của mình làm căn cứ không.

---

## 37. 10 nguyên tắc cần tuân thủ khi vận hành SDD V04

1. **Tạo specification trước**: Làm rõ Spec Pack và AC trước implementation.
2. **Không đi tiếp bằng suy đoán**: Thông tin thiếu phải ghi vào Source Availability hoặc Stop Report.
3. **Kiểm soát Context**: Không cho AI đọc tất cả. Chỉ đưa căn cứ cần thiết.
4. **Không xem ý kiến AI là bằng chứng**: Kết hợp tool result, test, human review.
5. **Bắt đầu nhỏ**: Không đưa toàn bộ nhóm 40 vào ngay từ đầu.
6. **Không để Security thành phần bổ sung sau**: Nghĩ từ đầu ở Phase 0-A.
7. **Quản lý bản chính artifact**: Giữ nhất quán Spec, Plan, Review, Test, Report.
8. **Biến thất bại thành tài sản học tập**: Cập nhật 29 và 34.
9. **Đo chi phí**: Xem token, latency, cost per valid finding.
10. **Con người chịu trách nhiệm**: AI là trợ lý; phán đoán cuối cùng do con người thực hiện.

---

## 38. Cuối cùng: cách dùng hướng dẫn này

Hướng dẫn này không phải đọc một lần rồi xong. Sử dụng như sau sẽ hiệu quả.

- Khi đào tạo thành viên mới, đọc chương 1〜7.
- Khi bắt đầu案件, xem chương 7, 8, 12, 32.
- Khi đang phát triển mà phân vân, xem mô tả file liên quan trong chương 8.
- Khi thúc đẩy triển khai, xem chương 10, 27, 35.
- Khi cải tiến chất lượng, xem chương 15, 19, 36, 37.
- Khi vận hành AI nâng cao, xem các file 40〜49 và chương 31〜33.

SDD V04 không cần được dùng hoàn hảo ngay từ đầu. Hãy bắt đầu nhỏ, để lại chứng tích, biến thất bại thành học tập và dần nuôi dưỡng theo dự án.
