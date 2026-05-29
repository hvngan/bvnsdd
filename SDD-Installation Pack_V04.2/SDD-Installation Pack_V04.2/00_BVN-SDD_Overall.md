<!-- TOC:START -->
**Mục lục**
- [Bản sửa đổi・Giải thích chi tiết SDD Introduction Pack V04.2](#bản-sửa-đổigiải-thích-chi-tiết-sdd-introduction-pack-v042)
- [0. Tóm tắt điều hành](#0-tóm-tắt-điều-hành)
  - [0.1 Vấn đề cốt lõi mà bộ tài liệu này giải quyết](#01-vấn-đề-cốt-lõi-mà-bộ-tài-liệu-này-giải-quyết)
  - [0.2 Phân định vai trò giữa sử dụng AI đơn giản, vibe coding và SDD](#02-phân-định-vai-trò-giữa-sử-dụng-ai-đơn-giản-vibe-coding-và-sdd)
  - [0.3 Cách phối hợp lý tưởng giữa vibe coding và SDD](#03-cách-phối-hợp-lý-tưởng-giữa-vibe-coding-và-sdd)
  - [0.4 Giá trị cuối cùng của bộ tài liệu này](#04-giá-trị-cuối-cùng-của-bộ-tài-liệu-này)
- [1. Vị trí của bộ tài liệu nhập môn này trong tổng thể](#1-vị-trí-của-bộ-tài-liệu-nhập-môn-này-trong-tổng-thể)
- [2. Giải thích kỹ thuật ngữ nền tảng cho người mới bắt đầu](#2-giải-thích-kỹ-thuật-ngữ-nền-tảng-cho-người-mới-bắt-đầu)
- [3. Cấu trúc tổng thể của bộ tài liệu nhập môn](#3-cấu-trúc-tổng-thể-của-bộ-tài-liệu-nhập-môn)
- [4. Luồng cơ bản của Core](#4-luồng-cơ-bản-của-core)
- [5. Mục đích, cách dùng, ưu điểm, nhược điểm, giải thích cho người mới và ví dụ của từng file](#5-mục-đích-cách-dùng-ưu-điểm-nhược-điểm-giải-thích-cho-người-mới-và-ví-dụ-của-từng-file)
- [6. Rà soát lại các yếu tố kỹ thuật chính được đưa vào](#6-rà-soát-lại-các-yếu-tố-kỹ-thuật-chính-được-đưa-vào)
- [7. Đào sâu khái niệm đảm bảo chất lượng](#7-đào-sâu-khái-niệm-đảm-bảo-chất-lượng)
- [8. Lộ trình khuyến nghị khi áp dụng SDD](#8-lộ-trình-khuyến-nghị-khi-áp-dụng-sdd)
- [9. Mẫu thực tế để kết nối từ vibe coding sang SDD](#9-mẫu-thực-tế-để-kết-nối-từ-vibe-coding-sang-sdd)
- [10. Đánh giá tổng hợp](#10-đánh-giá-tổng-hợp)
- [11. Tổng kết cuối cùng](#11-tổng-kết-cuối-cùng)
<!-- TOC:END -->

---
# Bản sửa đổi・Giải thích chi tiết SDD Introduction Pack V04.2

Dưới đây là phiên bản được mở rộng đáng kể dựa trên câu trả lời trước, có phản ánh các góc nhìn mà người dùng chỉ định. Lần này đặc biệt tăng cường các điểm sau:

* Thêm **Tóm tắt điều hành** ở đầu tài liệu.
* Làm rõ ranh giới giữa **sử dụng AI đơn giản / vibe coding / SDD**.
* Thêm luồng **chuyển yêu cầu/yêu cầu nghiệp vụ thu được từ vibe coding sang SDD**.
* Với từng file, mở rộng phần **vai trò, cách dùng, ưu điểm, nhược điểm, giải thích thuật ngữ cho người mới, chi tiết, ví dụ và use case**.
* Rà soát lại các yếu tố kỹ thuật, bao gồm **ECC / Everything Claude Code, giảm token, RAG, Code Map, Multi-Agent, RecursiveMAS, Consensus, quản trị AI**.
* Đào sâu đảm bảo chất lượng theo các góc nhìn **chất lượng, năng suất, an toàn, tính tái lập, khả năng kiểm toán và quản trị AI**.

Sau khi kiểm tra lại trong ZIP, không thấy chính chữ viết tắt `ECC`. Khái niệm tương ứng được ghi là `Everything Claude Code`. Trong tài liệu, Everything Claude Code được xem như một AI agent harness mạnh mẽ bao gồm `skills / rules / agents / hooks / MCP / continuous learning / security scanning`; chính sách được nêu là không đưa tất cả vào một cách không qua thẩm định, mà áp dụng từng bước các thành phần đã được rà soát.  
Căn cứ nội bộ: `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` L1103-L1133, `25_SDD_Security-Gate-and-CI-Security_Ver.04_Japanese.md` L101-L109

---

# 0. Tóm tắt điều hành

SDD Introduction Pack V04.2 này không chỉ là một tập prompt AI, cũng không phải là bộ hướng dẫn cách dùng Claude Code / Codex / Copilot. Cốt lõi của nó là một **hệ điều hành phát triển** để đưa AI vào phát triển nghiệp vụ một cách an toàn. Chính bộ tài liệu cũng định vị SDD V04 là “hệ điều hành phát triển để AI có thể hỗ trợ phát triển một cách an toàn, có độ chính xác cao, có tính tái lập và có thể kiểm toán”.  
Căn cứ nội bộ: `10_BVN-SDD_GuideLine.md` L56-L72

Thông điệp quan trọng nhất của bộ tài liệu này có thể tóm gọn như sau:

> **Đây là bộ tài liệu để chuyển từ phát triển “giao phó cho AI” sang phát triển “sử dụng AI dưới sự kiểm soát của đặc tả, bằng chứng, quyền hạn, artifact, review, test và phán đoán của con người”.**

Bộ tối thiểu nên áp dụng đầu tiên:

```text
10 + 11 + 21 + 22 + 28
```

Bộ tiêu chuẩn nên bổ sung sớm trong dự án thực tế:

```text
23 + 24 + 31 + 33
```

Khi chú trọng bảo mật và quản trị AI, bổ sung sớm:

```text
25 + 43 + 45
```

Với dự án lớn, rủi ro cao hoặc phức tạp, chọn các phần cần thiết từ nhóm 40:

```text
40 + 41 + 42 + 44 + 46 + 47 + 48 + 49
```

Trong chính bộ tài liệu cũng khuyến nghị bộ tối thiểu cần áp dụng đầu tiên là `10, 11, 21, 22, 28`, và trong phát triển thực tế nên sớm đưa vào `23, 24, 31, 33`.  
Căn cứ nội bộ: `10_BVN-SDD_GuideLine.md` L1437-L1439

---

## 0.1 Vấn đề cốt lõi mà bộ tài liệu này giải quyết

Thất bại trong phát triển có AI không chỉ xảy ra vì năng lực của AI chưa đủ. Trong thực tế, các vấn đề sau thường xuyên xảy ra:

* AI suy đoán và triển khai khi đặc tả vẫn mơ hồ.
* AI hiểu nhầm tài liệu đặc tả hoặc Excel cũ là bản chính xác.
* Triển khai khi chưa đọc source mới nhất, định nghĩa DB, hợp đồng API.
* Chỉ nhìn FE và bỏ sót ảnh hưởng BE.
* Chỉ nhìn BE và bỏ sót hiển thị hoặc ràng buộc nhập liệu ở FE.
* Bỏ sót ảnh hưởng đến xác thực, phân quyền, audit log, PII.
* Xem câu “không có vấn đề” từ AI review như bằng chứng.
* Báo cáo như thể đã chạy test dù thực tế chưa chạy.
* Cấp quyền quá rộng cho MCP / hooks / công cụ bên ngoài.
* Lỗi của AI không được tận dụng cho lần sau, dẫn tới lặp lại cùng sai sót.

Bộ tài liệu này không ngăn các vấn đề đó bằng “sự cẩn thận của từng cá nhân”, mà bằng **quy trình, artifact, gate, bằng chứng, quyền hạn và chỉ số đánh giá**.

---

## 0.2 Phân định vai trò giữa sử dụng AI đơn giản, vibe coding và SDD

Để hiểu đúng ý nghĩa của bộ tài liệu này, cần tách ba khái niệm sau.

| Phân loại | Mục đích chính | Phù hợp với tình huống | Chỉ số thành công | Rủi ro chính |
| --------- | -------------- | ---------------------- | ----------------- | ------------ |
| Sử dụng AI đơn giản | Tăng hiệu suất công việc cá nhân | Khảo sát, giải thích, sinh đoạn code, hỗ trợ review | Rút ngắn thời gian, tăng hiểu biết | Phụ thuộc cá nhân, thiếu tái lập, thiếu bằng chứng |
| Vibe coding | Xoay vòng giả thuyết và kiểm chứng thị trường thật nhanh | MVP, prototype, xác nhận phản ứng khách hàng, khám phá ý tưởng | Tốc độ học hỏi, phản ứng người dùng, kiểm chứng PMF | Thiếu chất lượng, bảo trì, bảo mật, kiểm toán |
| SDD | Triển khai, bảo trì và kiểm toán an toàn như phát triển nghiệp vụ | Đưa vào production, dự án khách hàng, hệ thống lõi, bảo trì dài hạn, nhiều người phát triển | Chất lượng, tính tái lập, bằng chứng, review, test, bảo trì | Chi phí học ban đầu, chi phí vận hành artifact |

Vibe coding được biết đến rộng rãi từ năm 2025 như một phong cách phát triển trong đó con người truyền đạt bằng ngôn ngữ tự nhiên điều muốn làm cho AI, rồi nhanh chóng lặp lại sinh code, chạy và sửa. Merriam-Webster giới thiệu vibe coding như một trào lưu bắt đầu từ bài đăng tháng 2 năm 2025 của Andrej Karpathy, tức là dùng ngôn ngữ tự nhiên để AI viết code. Collins cũng giải thích `vibe coding` là hành vi dùng ngôn ngữ tự nhiên để AI viết code. ([Merriam-Webster][1])

Tuy nhiên, vibe coding mạnh ở việc “làm nhanh”, nhưng không tự động đảm bảo “bảo trì dài hạn được”, “kiểm toán được”, “xử lý được quyền hạn và thông tin cá nhân”, hay “nhiều team có thể thay đổi an toàn”. Vì vậy, SDD không cạnh tranh với vibe coding; cách hiểu đúng là **phân vai giữa giai đoạn khám phá và giai đoạn sản phẩm hóa**.

---

## 0.3 Cách phối hợp lý tưởng giữa vibe coding và SDD

Vibe coding đóng vai trò gần với Build-Measure-Learn trong Lean Startup. Trong Lean Startup, MVP được nhấn mạnh như cách để thu được nhiều học hỏi đã kiểm chứng nhất về khách hàng với nỗ lực tối thiểu. Tài liệu chính thức của Lean Startup cũng giải thích MVP là đơn vị tối thiểu để thu được lượng học hỏi đã kiểm chứng lớn nhất về khách hàng. ([Lean Startup Co.][2])

Khi nối tư duy này với SDD, luồng sẽ như sau:

```text
Giả thuyết thị trường
  ↓
Tạo MVP / prototype bằng vibe coding
  ↓
Thu thập phản ứng người dùng, phản ứng sales, feedback từ bộ phận nghiệp vụ
  ↓
Chọn lọc thứ có vẻ bán được / có vẻ được dùng / có giá trị
  ↓
Sắp xếp thành ứng viên yêu cầu
  ↓
Chuyển đổi thành Spec Pack của SDD
  ↓
Source Intelligence / Impact Analysis / Review / Test / Security Gate
  ↓
Triển khai, kiểm chứng, release ở chất lượng production
  ↓
Đưa ngược về Failure Mode / Project Knowledge / Evaluation
```

Nói cách khác, không đưa thẳng thứ tạo ra từ vibe coding vào production. Học hỏi thu được từ vibe coding cần được chuyển đổi thành **yêu cầu, yêu cầu nghiệp vụ và Spec Pack**, là đầu vào của SDD.

---

## 0.4 Giá trị cuối cùng của bộ tài liệu này

Giá trị của bộ tài liệu này không nằm ở việc viết code bằng AI. Giá trị thực sự là tạo ra trong tổ chức trạng thái sau:

* Thông tin đưa cho AI được quản lý.
* Những gì AI đã đọc và chưa đọc được ghi lại.
* Đặc tả, triển khai, review, test và báo cáo được liên kết với nhau.
* Ý kiến của AI được tách khỏi bằng chứng như test, build, SAST.
* Quyền đối với thông tin xác thực, PII, công cụ bên ngoài, MCP, hooks được kiểm soát.
* Thất bại được nâng cấp thành Failure Mode hoặc Project Knowledge.
* Hiệu quả áp dụng AI được đo bằng valid finding rate, missed finding rate, review time, production quality, cost per valid finding, chứ không phải bằng số lượng comment.

Theo nghĩa này, SDD Introduction Pack là **bộ tài liệu để biến phát triển có AI từ kỹ năng cá nhân thành năng lực tổ chức**.

---

# 1. Vị trí của bộ tài liệu nhập môn này trong tổng thể

## 1.1 SDD không phải là “cách bắt AI viết code”

Trung tâm của bộ tài liệu này là **SDD: Specification Driven Development, phát triển định hướng đặc tả**.

Phát triển định hướng đặc tả có thể hiểu đơn giản là:

> **Phương thức chuẩn bị trước đặc tả, điều kiện nghiệm thu, phạm vi ảnh hưởng, kế hoạch triển khai, góc nhìn review và kế hoạch test, rồi dựa vào đó để AI và con người cùng phát triển.**

Trong bộ tài liệu, SDD được nói rõ là “không phải cách để AI tự do viết code”. Đây là thiết kế hiện trường trong đó đặc tả, căn cứ, rule, artifact, review, test và record được chuẩn bị trước để AI có thể hỗ trợ phát triển một cách an toàn, có tính tái lập và có thể review.  
Căn cứ nội bộ: `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` L80-L93

Chỉ cần yêu cầu AI “hãy làm chức năng này”, ta vẫn có thể nhận được thứ chạy được. Nhưng trong hệ thống nghiệp vụ, như vậy là chưa đủ. Cần trả lời được:

* Vì sao chức năng đó cần thiết.
* Ai sẽ sử dụng.
* Điều kiện nào thì được coi là hoàn thành.
* Những gì không được làm.
* Có ảnh hưởng gì tới chức năng hiện có.
* DB hoặc hợp đồng API có thay đổi không.
* Có ảnh hưởng đến quyền hạn hoặc thông tin cá nhân không.
* Kiểm chứng bằng test nào.
* Cần để lại bằng chứng nào.
* Ai đưa ra phán đoán cuối cùng.

SDD thiết kế những điều này như **một quy trình phát triển nằm bên ngoài AI**.

---

## 1.2 Khác biệt với việc sử dụng AI đơn giản

Sử dụng AI đơn giản rất hữu ích để nâng cao năng suất cá nhân, ví dụ:

* Nhờ giải thích nguyên nhân lỗi.
* Hỏi cách viết SQL.
* Nhờ đề xuất test case.
* Nhờ đưa ra góc nhìn review code.
* Nhờ tóm tắt tài liệu.

Tuy nhiên, chỉ như vậy thì không đảm bảo được:

* Cùng một người làm có tạo ra cùng chất lượng hay không.
* Người khác có truy vết được không.
* Thay đổi đặc tả đã được phản ánh ở đâu.
* AI đã dựa trên căn cứ nào để phán đoán.
* Thông tin đưa cho AI có được phép đọc về mặt bảo mật không.
* Khi sự cố production xảy ra có truy lại được lịch sử phán đoán không.
* Thất bại có được tận dụng cho lần sau không.

Sử dụng AI đơn giản là **hỗ trợ công việc**. SDD là **kiểm soát phát triển**.

---

## 1.3 Khác biệt với vibe coding

Vibe coding rất mạnh khi cần nhanh chóng biến ý tưởng thành hình và đưa ra thị trường hoặc người dùng để thử. Nó phù hợp với:

* Demo đơn giản để sales cho khách hàng xem.
* MVP của dịch vụ mới.
* Công cụ thử nghiệm cải thiện nghiệp vụ nội bộ.
* Xác nhận phản ứng UI/UX.
* Khám phá chức năng nào được dùng, chức năng nào không được dùng.
* Kiểm chứng giả thuyết sản phẩm có khả năng bán được.

Theo cách nói của Lean Startup, đây là phương tiện tăng tốc **Build-Measure-Learn**.

Ngược lại, thành quả của vibe coding thường yếu ở:

* Văn bản hóa đặc tả.
* Yêu cầu phi chức năng.
* Thiết kế bảo mật.
* Thiết kế DB migration.
* Thiết kế quyền hạn.
* Audit log.
* Hệ thống test.
* Khả năng bảo trì.
* Khả năng hiểu code.
* Vận hành dài hạn.
* Bàn giao.
* Trách nhiệm giải trình khi có sự cố.

Vì vậy, vibe coding **mạnh ở khám phá**; SDD **mạnh ở chuyển đổi thành chất lượng nghiệp vụ**.

---

## 1.4 Liên kết yêu cầu/yêu cầu nghiệp vụ từ vibe coding sang SDD

Đưa thẳng prototype tạo bằng vibe coding vào production là nguy hiểm. Tuy nhiên, học hỏi thu được ở đó rất có giá trị.

Thứ cần chuyển sang SDD không phải là bản thân code, mà là **học hỏi đã được kiểm chứng** như sau.

| Thứ thu được ở phía vibe coding | Nơi tiếp nhận ở phía SDD |
| ------------------------------ | ------------------------- |
| Chức năng người dùng thật sự muốn | Business Requirement |
| Thao tác được dùng nhiều | User Story / Use Case |
| Màn hình khiến người dùng bối rối | Yêu cầu UX / yêu cầu FE |
| Luồng nghiệp vụ tạo ra giá trị | Business rule |
| Chức năng không cần thiết | Ngoài phạm vi |
| Hạng mục dữ liệu được phản ứng tốt | Đặc tả input/output |
| Điểm có vẻ cần billing, quyền hạn, audit | Security / Compliance Impact |
| Phần bị hỏng trong prototype | Ứng viên Failure Mode |
| Điều kiện khách hàng chấp nhận | Acceptance Criteria |
| Chỉ số kiểm chứng thị trường | Success Metrics |

Khi chuyển từ vibe coding sang SDD, lý tưởng là tạo artifact trung gian như sau.

```md
# Discovery-to-SDD Handoff

## 1. Giả thuyết đã kiểm chứng
- Giả thuyết giải quyết vấn đề nào, cho ai

## 2. Prototype đã tạo
- Đã tạo những gì
- Không tạo những gì

## 3. Phản ứng người dùng
- Đã cho ai xem
- Điều gì được đánh giá cao
- Điều gì bị nói là không cần

## 4. Ứng viên yêu cầu muốn đưa vào production
- Chức năng bắt buộc
- Chức năng tùy chọn
- Chức năng tương lai

## 5. Những điểm SDD cần xác nhận
- Dữ liệu
- Quyền hạn
- Audit
- Bảo mật
- Vận hành
- Hiệu năng
- Bảo trì

## 6. Nội dung nâng cấp thành Spec Pack
- Yêu cầu đã chốt
- Acceptance Criteria
- Phạm vi không làm
- Open Issues
```

Nhờ đó, vibe coding không kết thúc như một “prototype thô”, mà có thể kết nối sang Spec Pack của SDD.

---

## 1.5 Nói ngắn gọn ý nghĩa của SDD

Ý nghĩa của bộ tài liệu nhập môn này là:

> **Một cơ chế đặc tả, bằng chứng, chất lượng, bảo mật và cải tiến liên tục để chuyển những yêu cầu có giá trị thu được trong giai đoạn khám phá thành chất lượng production an toàn bằng AI.**

Nếu vibe coding là để “tìm thứ bán được”, thì SDD là để “chuyển thứ đã biết là bán được thành hệ thống nghiệp vụ khó hỏng, giải thích được và bảo trì được”.

---

# 2. Giải thích kỹ thuật ngữ nền tảng cho người mới bắt đầu

Phần này giải thích các thuật ngữ tối thiểu cần biết trước khi đọc SDD Introduction Pack. Trong bộ tài liệu cũng có bảng thuật ngữ nền tảng, sắp xếp các khái niệm như AI-driven development, SDD, Spec Pack, Impl Plan, Review Checklist, Source Intelligence, Context, Traceability.  
Căn cứ nội bộ: `10_BVN-SDD_GuideLine.md` L168-L195

---

## 2.1 Spec / Specification / Đặc tả

**Spec** là viết tắt của Specification, nghĩa là “đặc tả”. Với người mới, đó là:

> **Bản cam kết ghi rõ cần tạo gì và điều kiện nào thì được xem là đúng.**

Ví dụ, chỉ yêu cầu “hãy làm màn hình đăng ký người dùng” là còn mơ hồ. Trong Spec cần làm rõ:

* Hạng mục nhập liệu là gì.
* Hạng mục nào bắt buộc.
* Kiểm tra định dạng email như thế nào.
* Điều kiện mật khẩu là gì.
* Nếu email đã đăng ký thì xử lý ra sao.
* Khi thành công thì chuyển sang màn hình nào.
* Khi thất bại thì hiển thị thông báo nào.
* Có khác nhau giữa admin và user thường không.
* Có cần log hoặc audit không.
* Test cần xác nhận gì.

Nếu chỉ nói với AI “hãy làm màn hình đăng ký”, AI sẽ suy đoán những phần thiếu. Spec dùng để giảm suy đoán đó.

---

## 2.2 Spec Pack

**Spec Pack** là artifact gom các tiền đề cần thiết để AI và con người phát triển, lấy đặc tả làm trung tâm. Nó không phải là memo yêu cầu đơn thuần.

Các thành phần nên bao gồm:

* Bối cảnh.
* Mục đích.
* Phạm vi.
* Ngoài phạm vi.
* Acceptance Criteria.
* Business rule.
* Input/output.
* Lỗi.
* Quyền hạn.
* Ảnh hưởng DB.
* Hợp đồng API.
* Góc nhìn test.
* Điểm chưa xác định.
* Điểm AI đã suy đoán.
* Điểm cần con người xác nhận.

Trong bộ tài liệu, Spec Pack được định vị là artifact trung tâm của Phase 1, nơi sắp xếp đặc tả, AC, điểm chưa xác định và phạm vi ảnh hưởng.  
Căn cứ nội bộ: `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` L481-L535

Với người mới, Spec Pack là:

> **“Bản chính của thay đổi lần này” để AI và con người cùng hiểu giống nhau khi làm việc.**

---

## 2.3 Acceptance Criteria / AC / Điều kiện nghiệm thu

**Acceptance Criteria** là “điều kiện nghiệm thu”, thường viết tắt là **AC**.

Đây là:

> **Các điều kiện kiểm tra cụ thể để có thể kết luận rằng công việc đã hoàn thành.**

Ví dụ:

```text
AC của chức năng đăng ký người dùng

1. Có thể nhập email, mật khẩu và họ tên
2. Nếu email sai định dạng thì không đăng ký được
3. Nếu email đã tồn tại thì hiển thị lỗi trùng lặp
4. Khi đăng ký thành công, gửi email xác nhận
5. Mật khẩu phải có ít nhất 8 ký tự
6. Thao tác đăng ký được lưu vào audit log
```

Nếu không có AC, cả AI lẫn con người đều không biết “làm đến đâu thì xong”. Trong SDD, AC là điểm xuất phát của đặc tả, review và test.

---

## 2.4 Single Source of Truth / Nguồn đúng duy nhất

**Single Source of Truth** là “nguồn thông tin đúng duy nhất”. Với người mới, đó là:

> **Nơi thông tin đúng cần xem khi có nghi ngờ.**

Trong SDD, về nguyên tắc, `spec-pack.md` theo từng ticket trở thành nguồn đúng duy nhất. Bộ tài liệu trình bày cấu trúc trong đó `docs/changes/<TICKET>/spec-pack.md` là nguồn đúng duy nhất, còn Impl Plan, Review Checklist, Test Plan, Report được xử lý như các nguồn đúng phụ trợ.  
Căn cứ nội bộ: `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` L108-L129

Nếu không có điều này, các sự cố sau sẽ xảy ra:

* Đặc tả đã đổi trong chat nhưng chưa phản ánh vào Spec.
* Report có nội dung sửa nhưng test plan vẫn cũ.
* Đặc tả Excel và source mâu thuẫn.
* AI nhìn tài liệu cũ để triển khai.
* Mỗi người có một “đặc tả đúng” khác nhau.

Trong SDD, quản lý bản chính rất quan trọng.

---

## 2.5 Context

**Context** là thông tin đưa cho AI, ví dụ:

* Nội dung ticket.
* Tài liệu đặc tả.
* Source code.
* Định nghĩa DB.
* Đặc tả API.
* Test hiện có.
* Error log.
* Thuật ngữ nghiệp vụ.
* Coding convention.
* Ví dụ thất bại trong quá khứ.

Chất lượng đầu ra của AI thay đổi rất lớn tùy theo Context.

Ví dụ Context xấu:

* Tài liệu đặc tả cũ.
* Source không liên quan.
* Toàn bộ log khổng lồ.
* File `.env` chứa secret.
* Dữ liệu khách hàng.
* Chỉ thị độc hại từ web bên ngoài.
* Generated code không cần đọc.

Ví dụ Context tốt:

* Source mới nhất.
* API liên quan.
* Định nghĩa DB.
* Ví dụ triển khai đúng đang tồn tại.
* Spec Pack của lần thay đổi này.
* File xung quanh phạm vi thay đổi.
* Tóm tắt kết quả test cần thiết.

Trong SDD, không “đưa tất cả” context cho AI, mà phải chọn.

---

## 2.6 Context Loading

**Context Loading** là công việc quyết định AI nên đọc gì, không nên đọc gì, và đọc theo thứ tự nào.

Tài liệu số 31 giải thích rằng độ chính xác của AI không chỉ do prompt hay, mà còn phụ thuộc rất lớn vào chất lượng Context đã đưa cho AI. Các ví dụ tai nạn được nêu gồm: tài liệu thiết kế cũ, sinh SQL khi không có định nghĩa DB, chỉ thị độc hại trong PDF/web page, lẫn secret, và bùng nổ token cost do nạp quá nhiều tài liệu.  
Căn cứ nội bộ: `31_SDD_Context-Loading-and-Exclusion_Ver.04_Japanese.md` L55-L95

Với người mới, đó là:

> **Công việc biên tập tài liệu sẽ đưa cho AI.**

---

## 2.7 Artifact / Thành quả đầu ra

**Artifact** là các thành quả đầu ra được tạo trong SDD, ví dụ:

* `spec-pack.md`
* `source-availability.md`
* `impact-analysis.md`
* `impl-plan.md`
* `review-checklist.md`
* `test-plan.md`
* `test-results.md`
* `report.md`
* `failure-mode-entry.md`
* `pattern-card.md`

Trong Artifact Governance số 33, tiêu chuẩn quản lý bản chính, trạng thái, độ mới, căn cứ, quan hệ phái sinh, phê duyệt và traceability của artifact được định nghĩa.  
Căn cứ nội bộ: `33_SDD_Artifact-Governance-and-Traceability_Ver.04_Japanese.md` L60-L118

Với người mới, đó là:

> **Các bản ghi có thể kiểm tra về sau được tạo trong quá trình phát triển với AI.**

---

## 2.8 Traceability / Khả năng truy vết

**Traceability** là “khả năng truy vết”. Với người mới, đó là:

> **Việc có thể lần theo mối liên hệ từ yêu cầu đến triển khai, test, review và phán đoán cuối cùng.**

Ví dụ:

```text
Yêu cầu
  ↓
Spec Pack
  ↓
Impl Plan
  ↓
Code Diff
  ↓
Review Checklist
  ↓
Test Plan
  ↓
Test Results
  ↓
Final Report
  ↓
Failure Mode / Knowledge
```

Khi có khả năng này, ta trả lời được:

* Vì sao đã thay đổi code này.
* Nó tương ứng với yêu cầu nào.
* Đã xác nhận bằng test nào.
* Rủi ro nào đã được chấp nhận.
* Ai đã phê duyệt.
* Đã cập nhật gì để tránh lỗi tương tự.

Điều này rất quan trọng cho kiểm toán, đảm bảo chất lượng và bảo trì.

---

## 2.9 Source Intelligence

**Source Intelligence** là tư duy lập bản đồ cấu trúc source code trước khi để AI đọc source.

Ví dụ, nó sắp xếp:

* Màn hình nào gọi API nào.
* API gọi Service nào.
* Service dùng Repository nào.
* Repository dùng bảng DB nào.
* Test nào tương ứng.
* Kiểm tra phân quyền nằm ở đâu.
* Tích hợp bên ngoài nằm ở đâu.

Tài liệu số 23 chuẩn hóa Source Availability, Source Inventory, System / Entry / Route / API / Service / DB Map, FE/BE Contract Map, Impact Analysis và Evidence-linked Review.  
Căn cứ nội bộ: `23_SDD_Source-Intelligence-Pack_Ver.04_Japanese.md` L58-L98

Với người mới, đó là:

> **Tạo bản đồ trước khi để AI đi vào mê cung source.**

---

## 2.10 Review Checklist

**Review Checklist** là danh sách các góc nhìn cần kiểm tra khi review, ví dụ:

* Có khớp với đặc tả không.
* Có kiểm tra số không.
* Có xét số full-width không.
* Type DB và validation có nhất quán không.
* Có kiểm tra phân quyền không.
* Thông báo lỗi có đúng không.
* Có ghi secret ra log không.
* Có rollback được không.
* Có test không.

Tài liệu số 21 nêu rằng Review Checklist không được tạo sau khi triển khai, mà phải được tạo trước khi triển khai.  
Căn cứ nội bộ: `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` L657-L739

Với người mới, đó là:

> **Bảng kiểm để không bỏ sót khi review.**

---

## 2.11 Tool-Grounded Verification

**Tool-Grounded Verification** là kiểm chứng ý kiến của AI bằng kết quả từ các công cụ thực tế như test và build.

Tài liệu số 43 trình bày luồng AI Opinion → Evidence Required → Tool-Grounded Verification → Consensus / Veto / Policy → Human Governance.  
Căn cứ nội bộ: `43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Japanese.md` L57-L75

Với người mới, đó là:

> **Xác minh điều AI nói bằng test và công cụ thật.**

---

## 2.12 Orchestrator

**Orchestrator** là trung tâm điều phối nhiều Agent và nhiều tool. Tuy nhiên, tài liệu số 42 định nghĩa Orchestrator không phải là “Agent thông minh nhất”, mà là **người điều tiết giao thông có tính quyết định luận**.  
Căn cứ nội bộ: `42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Japanese.md` L160-L175

Với người mới, đó là:

> **Người điều phối quyết định AI nào đọc gì, tạo gì và tích hợp như thế nào.**

---

## 2.13 MCP

**MCP** là viết tắt của Model Context Protocol, cơ chế để AI kết nối với công cụ bên ngoài, database, API, công cụ giám sát, issue tracker, v.v. Tài liệu chính thức của Claude Code cũng giải thích rằng MCP server cấp cho Claude Code quyền truy cập công cụ bên ngoài, database và API. ([Claude][3])

Với người mới, đó là:

> **Cổng kết nối để AI truy cập hệ thống bên ngoài.**

Nó tiện lợi nhưng cũng nguy hiểm, vì nếu MCP được cấp quyền write/delete/send/deploy, AI có thể gây ảnh hưởng đến hệ thống bên ngoài do phán đoán sai.

---

## 2.14 Hooks

**Hooks** là xử lý tự động được chạy tại các thời điểm nhất định trong vòng đời của công cụ AI.

Tài liệu chính thức của Claude Code giải thích hooks là shell command, HTTP endpoint hoặc LLM prompt do user định nghĩa, được tự động chạy ở một số thời điểm nhất định trong lifecycle của Claude Code. ([Claude][4])

Với người mới, đó là:

> **Các kiểm tra hoặc xử lý tự động chạy trước/sau khi AI làm việc.**

Ví dụ:

* Chạy lint sau khi chỉnh sửa file.
* Thông báo khi test fail.
* Chặn trước khi chạy lệnh nguy hiểm.
* Ghi lại bằng chứng khi kết thúc công việc.

Nó tiện lợi, nhưng hooks xấu rất nguy hiểm. Vì vậy trong SDD, hooks được đưa vào từng bước.

---

## 2.15 Token

**Token** là đơn vị chuỗi ký tự mà AI xử lý. Input càng lớn thì càng tăng:

* Chi phí.
* Độ trễ.
* Ô nhiễm context.
* Rủi ro thông tin quan trọng bị chìm.

Tài liệu chính thức của Claude Code cũng giải thích rằng token cost tăng theo context size, và có thể giảm chi phí bằng context management, model selection, preprocessing hooks, v.v. ([Claude][5])

Với người mới, đó là:

> **Đơn vị tính phí và xử lý cho lượng chữ đưa vào AI.**

Trong SDD, giảm token không phải là “cắt cho ngắn”, mà là **thiết kế để chỉ đưa thông tin cần thiết mà không làm giảm chất lượng**.


---

# 3. Cấu trúc tổng thể của bộ tài liệu nhập môn

Bộ tài liệu nhập môn được cấu thành bởi các lớp lớn sau.

```text
ReadMe / Guide
  10: Hướng dẫn tổng thể
  11: README nhóm 20

Core Pack
  21: Quy trình cụ thể
  22: Tập prompt

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
  40: Tổng quan Advanced Options
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

Cấu trúc này cũng được nêu rõ trong bộ tài liệu, được chia thành Core, Extension, Operations và Advanced Options.  
Căn cứ nội bộ: `10_BVN-SDD_GuideLine.md` L76-L112

---

# 4. Luồng cơ bản của Core

Core flow của SDD V04 như sau.

| Phase | Tên | Mục đích | Artifact chính |
| ----- | --- | -------- | -------------- |
| 0-A | Safety Gate | Tạo môi trường để AI có thể làm việc an toàn | `.claude/`, bằng chứng phase0 |
| 0-B | Common Base / Source Intelligence | Tạo bản đồ source, DB, API, tiêu chuẩn | architecture, standards |
| 1 | Investigation / Spec Pack | Chốt đặc tả ở dạng có thể triển khai | `spec-pack.md` |
| 2 | Ticket Context / Rules | Sắp xếp tiền đề và điều cấm theo ticket | `context.md`, `ticket-rules.md` |
| 3 | Impact Analysis / Impl Plan | Đồng thuận phạm vi ảnh hưởng và kế hoạch triển khai | `impact-analysis.md`, `impl-plan.md` |
| 4 | Review Checklist | Định nghĩa trước góc nhìn review | `review-checklist.md` |
| 5 | Implementation / Review | Triển khai, AI review, human review | code diff, kết quả review |
| 6 | Test Plan / Test Code | Thiết kế test và test code | `test-plan.md` |
| 7 | Black-box Test | Kiểm thử từ góc nhìn khách hàng/QA | `blackbox-testcases.md` |
| 8 | Test Results / Report | Báo cáo kết quả, rủi ro và phán đoán | `test-results.md`, `report.md` |
| 9 | Living Docs / Failure Mode Update | Đưa học hỏi thành tài sản cho lần sau | failure-mode, cập nhật standards |

Tài liệu số 21 định nghĩa Phase 0-A đến 9 này là Core phase.  
Căn cứ nội bộ: `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md` L133-L149

---

# 5. Mục đích, cách dùng, ưu điểm, nhược điểm, giải thích cho người mới và ví dụ của từng file

Từ đây, giải thích từng file một.

---

## 10. `10_BVN-SDD_GuideLine.md`

### Vai trò

Đây là bản đồ của toàn bộ bộ tài liệu nhập môn. Nó sắp xếp SDD là gì, dùng file nào khi nào, người mới nên đọc từ đâu, PM/PL và người phụ trách Security nên chú trọng điểm nào.

### Giải thích thuật ngữ cho người mới

* **GuideLine**: Tài liệu hướng dẫn cách dùng.
* **Hệ điều hành phát triển**: Nền tảng phát triển bao gồm không chỉ triển khai mà cả đặc tả, review, test, bằng chứng và bảo mật.
* **Chế độ áp dụng**: Cách thay đổi độ nặng của quy trình theo dự án, như Light / Standard / Heavy / Critical.
* **Right-sizing**: Điều chỉnh để tránh vừa quá mức vừa thiếu.

### Cách dùng

* Tài liệu giải thích trước khi áp dụng.
* Cửa vào cho đào tạo nội bộ.
* Giải thích cho ban lãnh đạo, PM, PL.
* Quyết định dùng file nào.
* Thống nhất thuật ngữ SDD.
* Lập roadmap áp dụng.

### Ưu điểm

* Dễ nắm toàn cảnh.
* Người mới ít bị lạc.
* Có thể so sánh vai trò từng file.
* Dễ quyết định thứ tự áp dụng.
* Có thể hiểu SDD không phải là “quy trình nặng phải làm hết”, mà là hệ thống chọn theo rủi ro.

### Nhược điểm / điểm cần chú ý

* Chỉ đọc file này thì chưa làm thực tế được.
* Trong thực tế cần dùng kèm 21, 22, 28, 31, 33, v.v.
* Vì khái niệm rộng, người mới không nên cố hiểu hết trong một lần.

### Ví dụ

Khi áp dụng SDD cho team mới, đầu tiên dùng file 10 để giải thích:

```text
SDD không phải là tập prompt AI.
SDD là hệ điều hành phát triển để dùng AI an toàn.
Sửa nhỏ thì dùng Light là đủ.
Nếu liên quan phân quyền, thông tin cá nhân, DB change thì nâng lên Heavy/Critical.
```

---

## 11. `11_SDD_20s-Pack-README-and-Integration-Guide_Ver.04_Japanese.md`

### Vai trò

Đây là README sắp xếp cách đọc và dùng nhóm 20, tức 21 đến 29. Nó giải thích cách kết hợp Core Pack và Extension Pack.

### Giải thích thuật ngữ cho người mới

* **README**: Tài liệu nên đọc đầu tiên.
* **Integration Guide**: Hướng dẫn cách nối và dùng nhiều tài liệu với nhau.
* **Definition of Done**: Điều kiện hoàn thành.
* **Anti-pattern**: Mẫu thất bại điển hình không nên làm.

### Cách dùng

* Quyết định cách đọc 21–29.
* Lập kế hoạch áp dụng ngày 1, tuần 1, tháng 1.
* Chọn bộ tối thiểu theo loại dự án như sửa UI nhỏ, lỗi nhập số, thêm chức năng FE/BE, sửa xuyên microservice.
* Kiểm tra độ trưởng thành áp dụng và KPI.

### Ưu điểm

* Phù hợp đưa vào thực tế.
* Biết được “thứ tự đọc”.
* Không cần đọc toàn bộ nhóm 20, vẫn chọn được phần cần cho dự án.
* Có thể dùng như curriculum đào tạo.

### Nhược điểm / điểm cần chú ý

* File 11 là cửa vào; chi tiết của từng pack chuyên môn nằm ở file khác.
* Trong thực tế vẫn cần tham chiếu các tài liệu 21–29 tương ứng.
* Chưa đào sâu chi tiết Advanced Options.

### Ví dụ

Với chức năng FE/BE tách rời, dùng 11 để chọn như sau.

```text
21 Core
22 Prompt
23 Source Intelligence
24 Review/Test
25 Security
26 FE/BE Contract
28 Right-sizing
31 Context Loading
33 Artifact Governance
```

---

## 21. `21_SDD_1st-Step-Pack_02_具体的手順_Core_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu trung tâm của SDD, là phần thân của quy trình tiêu chuẩn và được tham chiếu thường xuyên nhất trong thực tế.

### Giải thích thuật ngữ cho người mới

* **Core**: Phần cốt lõi tối thiểu dùng cho mọi dự án.
* **Phase**: Công đoạn.
* **Safety Gate**: Kiểm tra an toàn trước khi AI làm việc.
* **Spec Pack**: Bản chính của đặc tả.
* **Impl Plan**: Kế hoạch triển khai.
* **Review Checklist**: Bảng góc nhìn review.
* **Test Plan**: Kế hoạch test.
* **Final Report**: Báo cáo cuối.
* **Living Docs**: Tài liệu sống, được cập nhật liên tục.

### Cách dùng

* Thực hiện Phase 0-A đến 9.
* Tạo artifact SDD theo từng ticket.
* Chính sách ban đầu cho `.claude/CLAUDE.md` và `settings.json`.
* Tạo Spec Pack, Impact Analysis, Impl Plan, Review Checklist, Test Plan, Report.
* Dùng Light / Standard / Heavy đúng cách.

### Ưu điểm

* Ai cũng có thể đi theo cùng một luồng.
* Không phó mặc cho AI, mà thiết kế đặc tả, ảnh hưởng, review, test trước khi triển khai.
* Người mới, Bridge SE, Reviewer, QA có thể trao đổi trên cùng artifact.
* Chuyển phát triển bị khóa trong chat thành phát triển dựa trên artifact.
* Có thể trả học hỏi về lần sau ở Phase 9.

### Nhược điểm / điểm cần chú ý

* Lần đầu sẽ cảm thấy nặng.
* Áp dụng toàn bộ cho sửa nhỏ thì quá mức.
* Nếu chỉ tạo artifact mà nội dung mỏng thì sẽ hình thức hóa.
* Nếu không cập nhật `spec-pack.md` mà chỉ cập nhật `report.md` thì bản chính bị phá vỡ.

### Chi tiết

Những điểm đặc biệt quan trọng trong file 21:

1. **SDD không phải là giao phó cho AI**.
2. **Core nhẹ, Option sâu**.
3. **Single Source of Truth về nguyên tắc là `spec-pack.md`**.
4. **Phase 0-A tạo hàng rào an toàn**.
5. **Phase 0-B tạo bản đồ source**.
6. **Phase 1 tạo Spec Pack**.
7. **Phase 3 tạo Impact Analysis và Impl Plan**.
8. **Phase 4 tạo Review Checklist trước khi triển khai**.
9. **Phase 9 trả về Failure Mode và Rules**.

### Ví dụ

Trường hợp thêm field API:

```text
Phase 1:
  Đưa đặc tả field thêm, type, bắt buộc/tùy chọn, điều kiện hiển thị vào Spec Pack

Phase 3:
  Đưa ảnh hưởng FE, BE, DTO, DB, validation, test vào Impact Analysis

Phase 4:
  Thêm hợp đồng API, type DB, quyền hạn, lỗi vào Review Checklist

Phase 6:
  Thiết kế Unit / Integration / Contract Test

Phase 8:
  Đưa Test Results và rủi ro còn lại vào Report

Phase 9:
  Nếu có lỗi cùng loại, đăng ký vào Failure Mode
```

---

## 22. `22_SDD_1st-Step-Pack_03_プロンプト集_Core_Ver.04_Japanese.md`

### Vai trò

Đây là tập prompt để yêu cầu AI thực hiện quy trình ở file 21.

### Giải thích thuật ngữ cho người mới

* **Prompt**: Câu chỉ thị cho AI.
* **Plan-only**: Chỉ yêu cầu lập kế hoạch trước, không triển khai ngay.
* **Prompt trả lại/sửa lại**: Chỉ thị yêu cầu AI làm lại khi đầu ra chưa đủ.
* **Stop/Ask prompt**: Chỉ thị buộc AI dừng và hỏi khi thiếu thông tin hoặc có nguy hiểm.

### Cách dùng

* Yêu cầu AI khi bắt đầu từng Phase.
* Tạo Spec Pack.
* Tạo Impact Analysis.
* Tạo Review Checklist.
* Tạo Test Plan.
* Tạo Final Report.
* Trả lại khi thiếu hoặc sai.

### Ưu điểm

* Chuẩn hóa chất lượng yêu cầu gửi cho AI.
* Giảm prompt mang tính cá nhân.
* Người mới dễ dùng AI theo luồng SDD.
* Bridge SE / developer / reviewer có thể dùng cùng hệ chỉ thị.

### Nhược điểm / điểm cần chú ý

* Chỉ prompt không đảm bảo chất lượng.
* Context xấu thì đầu ra xấu.
* Không được chỉ copy prompt rồi bỏ qua xác nhận Spec/Source.
* Dù AI nói “có thể triển khai”, nếu rơi vào Stop/Ask thì cần con người xác nhận.

### Ví dụ

Trước khi người mới nhờ AI triển khai, dùng prompt của file 22 để yêu cầu:

```text
Trước hết không được triển khai.
Hãy chỉ tạo bản nháp Spec Pack, Source Availability, Impact Analysis, Impl Plan.
Tách riêng các điểm thiếu thông tin, mâu thuẫn và cần con người xác nhận vào Open Issues.
```

Điều này ngăn AI chỉnh code ngay lập tức.

---

## 23. `23_SDD_Source-Intelligence-Pack_Ver.04_Japanese.md`

### Vai trò

Đây là pack chuyên dụng để tăng độ chính xác khi phân tích source. Nó tạo bản đồ source trước khi để AI đọc source.

### Giải thích thuật ngữ cho người mới

* **Source Availability**: Xác nhận đã đọc được source/định nghĩa DB cần thiết hay chưa.
* **Source Inventory**: Kiểm kê repository, module, setting, test, v.v.
* **Entry Point**: Điểm vào của xử lý, như màn hình, API, Batch, Job.
* **Call Graph**: Quan hệ gọi hàm/method.
* **External IF**: Liên kết với hệ thống bên ngoài.
* **Evidence-linked Review**: Review kèm file căn cứ và điều kiện tái hiện.

### Cách dùng

* Nắm cấu trúc repository lớn.
* Phân tích hệ thống hiện có bằng AI.
* Khảo sát phạm vi ảnh hưởng.
* Tạo căn cứ cho phán đoán “không có ảnh hưởng”.
* Sắp xếp quan hệ FE/BE, DB, Batch, Event, external IF.

### Ưu điểm

* Giảm việc AI đọc sót.
* Giảm rủi ro AI tạo method không tồn tại.
* Tăng độ chính xác của impact analysis.
* Review và test có thể làm việc trên cùng bản đồ.
* Cũng dùng được cho onboarding hệ thống hiện có.

### Nhược điểm / điểm cần chú ý

* Tốn thời gian tạo ban đầu.
* Nếu không cập nhật theo thay đổi source thì sẽ cũ.
* Nếu bản đồ sai, phán đoán của AI cũng sai.
* Có thể quá mức với sửa nhỏ một file.

### Chi tiết

File 23 chuẩn hóa Source Availability, Source Inventory, System / Entry / Route / API / Service / DB Map, FE/BE Contract Map, Impact Analysis, Evidence-linked Review.  
Căn cứ nội bộ: `23_SDD_Source-Intelligence-Pack_Ver.04_Japanese.md` L68-L98

### Ví dụ

Khi “thay đổi logic tính số tiền hóa đơn”, không để AI triển khai ngay mà trước tiên sắp xếp:

```text
Màn hình: Màn hình đăng ký hóa đơn
API: /billing/calculate
Service: BillingCalculationService
Repository: BillingRepository
DB: billing_detail, tax_master
External IF: Liên kết hệ thống kế toán
Test: BillingCalculationServiceTest
Rủi ro: thuế suất, làm tròn, dữ liệu quá khứ, tính lại
```

Nhờ bản đồ này, AI không đọc quá nhiều file không liên quan và ít bỏ sót điểm quan trọng.

---

## 24. `24_SDD_Review-TestCode-Enhancement_Ver.04_Japanese.md`

### Vai trò

Đây là pack nâng cao chất lượng review và test code.

### Giải thích thuật ngữ cho người mới

* **High-signal review**: Chỉ ra lỗi hữu ích có tác hại thực tế.
* **False Positive**: Chỉ ra vấn đề dù thực tế không phải vấn đề.
* **Self Review**: Review bởi chính người triển khai.
* **Independent Review**: Review độc lập bởi AI khác hoặc người khác.
* **Test Plan**: Kế hoạch test cái gì và test như thế nào.
* **Black-box Test**: Test bằng input/output mà không nhìn vào triển khai bên trong.
* **Regression Test**: Test để xác nhận chức năng cũ không bị hỏng.

### Cách dùng

* Tạo góc nhìn review trước khi triển khai.
* Nâng chất lượng AI review.
* Giảm false positive.
* Sắp xếp góc nhìn sinh test code.
* Chọn giữa Unit / Integration / Contract / E2E.
* Đưa kết quả review về Failure Mode.

### Ưu điểm

* Giảm bỏ sót khi review.
* Phát hiện sớm lỗi có tác hại thực tế.
* AI review dễ trở thành chỉ ra có căn cứ thay vì “cảm tưởng”.
* Test và AC được liên kết.
* Giảm tải human review.

### Nhược điểm / điểm cần chú ý

* Nếu mục tiêu trở thành tăng số lượng chỉ trích thì phản tác dụng.
* Không được tin nguyên xi AI review.
* Thêm quá nhiều test làm tăng chi phí bảo trì.
* False positive nhiều làm con người mệt mỏi.

### Chi tiết

File 24 cho rằng review và sinh test code không ổn định chỉ bằng prompt, nên cần giữ luồng Spec Pack → Impact Analysis → Impl Plan → Review Checklist → Self Review → Independent Review → Test Plan → Test Code / Black-box Test → Test Results / Report.  
Căn cứ nội bộ: `24_SDD_Review-TestCode-Enhancement_Ver.04_Japanese.md` L57-L98

### Ví dụ

Khi sửa lỗi nhập số, góc nhìn review là:

```text
- Xử lý số full-width như thế nào
- Xử lý trộn half-width / full-width như thế nào
- Có cho phép số kèm dấu phẩy không
- Xử lý số thập phân, số âm, zero, chuỗi rỗng, null như thế nào
- Có khớp precision / scale của DB không
- FE validation và BE validation có khớp không
- Error message có hỗ trợ đa ngôn ngữ không
```

---

## 25. `25_SDD_Security-Gate-and-CI-Security_Ver.04_Japanese.md`

### Vai trò

Đây là pack xử lý bảo mật môi trường phát triển AI và bảo mật ứng dụng/CI.

### Giải thích thuật ngữ cho người mới

* **Security Gate**: Kiểm tra an toàn trước khi đi vào công việc nguy hiểm.
* **CI**: Continuous Integration, cơ chế tự động build/test.
* **SAST**: Static Application Security Testing, phân tích tĩnh source để tìm lỗ hổng.
* **SCA**: Software Composition Analysis, kiểm tra lỗ hổng và license của thư viện phụ thuộc.
* **SBOM**: Software Bill of Materials, bảng thành phần phần mềm.
* **Secrets Scan**: Phát hiện API key, password và secret.
* **Prompt Injection**: Tấn công nhúng chỉ thị độc hại cho AI trong tài liệu ngoài.
* **Deny / Ask / Allow**: Phân loại quyền cấm / cần hỏi / cho phép.

### Cách dùng

* Biến Phase 0-A thành Security Gate thật sự.
* Thiết kế quyền trong `.claude/settings.json`.
* Cấm đọc `.env`, key, PII, dữ liệu khách hàng.
* Đưa hooks / MCP / DXT / subagents / parallelization vào từng bước.
* Đưa SAST / Secrets / IaC / SCA / SBOM vào CI.
* Lưu severity, căn cứ, phương án sửa, quyết định chấp nhận của security finding.

### Ưu điểm

* Ngăn tai nạn để AI đọc secret.
* Ngăn chạy nhầm lệnh nguy hiểm.
* Ngăn MCP/hooks chưa thẩm định gây sự cố.
* Có thể hóa bằng chứng các chỉ ra bảo mật.
* Không chặn AI, mà làm rõ phạm vi dùng an toàn.

### Nhược điểm / điểm cần chú ý

* Ban đầu cấu hình hơi mất công.
* Hạn chế quá mạnh thì giảm hiệu suất.
* MCP / hooks / DXT nguy hiểm nếu đưa vào khi chưa hiểu.
* Chỉ file 25 có thể chưa đủ cho quản trị Agentic AI nâng cao; có lúc cần file 45.

### Chi tiết

File 25 chia bảo mật thành hai lớp:

```text
Layer A: Bảo mật môi trường phát triển AI
  Claude Code / Codex / agent harness / rules / skills / hooks / MCP / DXT / tài liệu bên ngoài / quyền hạn / memory / logs

Layer B: Bảo mật ứng dụng và CI/CD
  Xác thực / phân quyền / input validation / SAST / Secrets / IaC / SCA / SBOM / Container / DAST / supply chain / release gate
```

Căn cứ nội bộ: `25_SDD_Security-Gate-and-CI-Security_Ver.04_Japanese.md` L59-L93

### Ví dụ

Không được cho phép AI thực hiện các thao tác sau.

```text
- Đọc .env
- Đọc AWS key
- Kết nối production DB
- kubectl apply
- terraform apply
- Gửi ra ngoài qua MCP chưa thẩm định
- force push
```

Ngược lại, các thao tác sau tương đối an toàn hơn để cho phép.

```text
- git status
- git diff
- rg
- find
- lint
- unit test
- typecheck
```

---

## 26. `26_SDD_FE-BE-Contract-and-Impact-Analysis_Ver.04_Japanese.md`

### Vai trò

Đây là pack xử lý hợp đồng và phân tích ảnh hưởng trong hệ thống tách FE/BE.

### Giải thích thuật ngữ cho người mới

* **FE**: Frontend, phía màn hình.
* **BE**: Backend, phía server.
* **Contract**: Thỏa thuận giữa FE và BE; không chỉ API mà còn DTO, validation, lỗi, quyền hạn, test.
* **DTO**: Data Transfer Object, hình dạng dữ liệu trao đổi qua API.
* **Validation**: Kiểm tra input.
* **i18n**: internationalization, hỗ trợ đa ngôn ngữ.
* **Contract Test**: Test để xác nhận thỏa thuận FE/BE không bị phá vỡ.

### Cách dùng

* Thay đổi API.
* Thêm/sửa DTO.
* Đồng bộ FE validation và BE validation.
* Đồng bộ error code và message.
* Sắp xếp permission, role, tenant, owner.
* Thiết kế Contract Test và E2E Test.

### Ưu điểm

* Tránh lỗi chỉ nhìn FE mà bỏ sót ảnh hưởng BE.
* Tránh lỗi chỉ nhìn BE mà bỏ sót hiển thị và ràng buộc input ở FE.
* Tránh lệch validation, lỗi, quyền hạn, test mà danh sách API đơn thuần không nhìn thấy.
* FE/BE cùng làm việc trên Contract Map.

### Nhược điểm / điểm cần chú ý

* Quá mức nếu chỉ sửa text đơn giản.
* Contract Map cũ thì lại nguy hiểm.
* Nguy hiểm khi thay đổi contract mà chỉ đọc được một phía FE hoặc BE.
* Không được hài lòng chỉ vì đã tạo OpenAPI.

### Chi tiết

File 26 nêu rằng hợp đồng FE/BE không chỉ là OpenAPI hay danh sách API, mà bao gồm Endpoint, DTO, Validation, Error, Permission, FE state, BE invariant và Test contract.  
Căn cứ nội bộ: `26_SDD_FE-BE-Contract-and-Impact-Analysis_Ver.04_Japanese.md` L63-L117

### Ví dụ

Khi thêm `customerRank` vào response API:

```text
FE:
  Vị trí hiển thị
  Hiển thị khi chưa có giá trị
  Message đa ngôn ngữ
  Cập nhật cache

BE:
  Thêm DTO
  Lấy từ DB
  Quyền được/không được hiển thị
  Cho phép null
  error handling

Test:
  Contract Test
  API Integration Test
  FE Component Test
  E2E Test
```

---

## 27. `27_SDD_Microservice-and-MultiRepo-Analysis_Ver.04_Japanese.md`

### Vai trò

Đây là pack xử lý phân tích ảnh hưởng trong microservice, nhiều repository và nhiều tech stack.

### Giải thích thuật ngữ cho người mới

* **Microservice**: Hệ thống được chia thành các service nhỏ.
* **MultiRepo**: Phát triển với nhiều repository.
* **Service Catalog**: Danh sách service và trách nhiệm của chúng.
* **Service Dependency Map**: Bản đồ phụ thuộc giữa service.
* **Event Schema**: Định dạng dữ liệu của event message.
* **Idempotency / Tính lũy đẳng**: Chạy cùng xử lý nhiều lần vẫn không làm sai kết quả.
* **Eventual Consistency**: Hệ phân tán có thể lệch tạm thời nhưng cuối cùng sẽ nhất quán.
* **Correlation ID**: ID dùng để truy vết xử lý đi qua nhiều service.

### Cách dùng

* Thay đổi API giữa microservice.
* Thay đổi Event / Queue / Webhook.
* Thay đổi đồng thời nhiều repo.
* Sắp xếp ownership của DB.
* Thiết kế thứ tự deploy và rollback.
* Thiết kế observability.
* Xác nhận retry / duplicate / ordering.

### Ưu điểm

* Ít bỏ sót ảnh hưởng giữa service.
* Ngăn thay đổi làm hỏng consumer.
* Có thể suy nghĩ trước rollback và thứ tự deploy.
* Kết nối với distributed tracing và thiết kế log.

### Nhược điểm / điểm cần chú ý

* Quá mức với ứng dụng đơn.
* Nếu chưa có service map thì chi phí tạo cao.
* Cần đồng thuận nhiều team.
* Nguy hiểm nếu AI chỉ nhìn một service để phán đoán.

### Chi tiết

File 27 giải thích rằng trong microservice hoặc nhiều repo, vấn đề không dừng ở từng file, mà mở rộng sang hợp đồng giữa service, event, ownership DB, thứ tự deploy, observability, retry, idempotency và lan truyền lỗi.  
Căn cứ nội bộ: `27_SDD_Microservice-and-MultiRepo-Analysis_Ver.04_Japanese.md` L70-L107

### Ví dụ

Khi order service thay đổi event `OrderCreated`:

```text
Producer:
  order-service

Consumers:
  billing-service
  inventory-service
  notification-service

Xác nhận:
  tính tương thích của event schema
  topic name
  retry
  nhận trùng lặp
  đảm bảo thứ tự
  rollback
  test phía consumer
  trace id
```

---

## 28. `28_SDD_Applicability-and-RightSizing_Ver.04_Japanese.md`

### Vai trò

Đây là pack quyết định nên áp dụng SDD ở độ sâu nào cho dự án nào.

### Giải thích thuật ngữ cho người mới

* **Applicability**: Khả năng áp dụng.
* **Right-sizing**: Điều chỉnh độ nặng vừa đủ.
* **Light / Standard / Heavy / Critical**: Độ sâu áp dụng.
* **Stop / Do Not Proceed**: Phán đoán không được tiếp tục vì nguy hiểm.
* **Reversibility / Khả năng đảo ngược**: Có thể hoàn tác thay đổi hay không.
* **Uncertainty / Độ bất định**: Mức độ còn chưa biết.

### Cách dùng

* Không áp dụng SDD quá nặng cho sửa nhỏ.
* Không áp dụng quy trình quá nhẹ cho dự án rủi ro cao.
* Ghi lại bằng chứng mode đã chọn.
* PM/PL giải thích vì sao quy trình nặng/nhẹ như vậy.
* Làm rõ điều kiện Stop/Ask.

### Ưu điểm

* Giảm phản ứng “SDD quá nặng”.
* Không bỏ sót dự án nguy hiểm.
* Chọn quy trình phù hợp theo từng dự án.
* Có thể giải thích “vì sao làm đến mức này”.

### Nhược điểm / điểm cần chú ý

* Người phán đoán cần kinh nghiệm.
* Ban đầu dễ nghiêng quá mức về Heavy.
* Ngược lại, cũng có thể vì hiệu suất mà xem nhẹ nguy hiểm.
* Nếu không ghi lại mode, về sau không giải thích được.

### Chi tiết

File 28 nêu rằng độ sâu SDD không quyết định bởi khối lượng công việc, mà bởi rủi ro, độ phức tạp, độ bất định và khả năng đảo ngược.  
Căn cứ nội bộ: `28_SDD_Applicability-and-RightSizing_Ver.04_Japanese.md` L69-L101

### Ví dụ

```text
Sửa text:
  M1 Light

Thêm field cho một API:
  M2 Core Standard

Thay đổi hợp đồng FE/BE:
  M3 Standard Plus

Nhiều repo + DB migration:
  M4 Heavy

Phân quyền / thông tin cá nhân / thanh toán:
  M5 Critical

Không có source mới nhất / không có định nghĩa DB:
  MX Stop
```

---

## 29. `29_SDD_Failure-Mode-and-Continuous-Learning_Ver.04_Japanese.md`

### Vai trò

Đây là pack chuyển thất bại, near miss, nhận nhầm của AI, bỏ sót review, bỏ sót test thành tài sản nâng chất lượng lần sau.

### Giải thích thuật ngữ cho người mới

* **Failure Mode**: Mẫu dễ thất bại.
* **Near Miss**: Suýt gây sự cố nhưng chưa thành sự cố.
* **Continuous Learning**: Học hỏi liên tục.
* **Root Cause**: Nguyên nhân gốc.
* **Prevention**: Biện pháp phòng tái diễn.
* **Rule hóa**: Biến thành rule cần tuân thủ từ lần sau.

### Cách dùng

* Không lặp lại cùng lỗi AI.
* Biến các chỉ trích review thường gặp thành checklist.
* Phản ánh thất bại vào rules / prompts / tests / CI / docs.
* Nâng cấp từ 29 sang Project Knowledge của 34.
* Kết nối sang Evaluation Dataset của 49.

### Ưu điểm

* Phát triển bằng AI thông minh hơn qua từng dự án.
* Biến phản tỉnh cá nhân thành tri thức tổ chức.
* Ngăn tái diễn cùng lỗi.
* Cải thiện góc nhìn review và test.

### Nhược điểm / điểm cần chú ý

* Nếu chỉ đăng ký mà không dùng lại thì vô nghĩa.
* Failure Mode cũ để mãi sẽ thành nhiễu.
* Rule hóa tất cả sẽ làm giảm độ linh hoạt của AI.
* Nguy hiểm nếu cho tự động học mà không có phê duyệt con người.

### Chi tiết

File 29 trình bày vòng lặp: cấu trúc hóa thất bại thành Failure Mode, sắp xếp nguyên nhân và cách phát hiện, phản ánh vào rules / prompts / checklists / tests / CI / docs, tái sử dụng ở dự án sau, đo hiệu quả, dọn rule không còn cần.  
Căn cứ nội bộ: `29_SDD_Failure-Mode-and-Continuous-Learning_Ver.04_Japanese.md` L67-L111

### Ví dụ

Nếu AI tạo lỗi nhập số vì không xét full-width number `１２３`:

```text
Failure Mode:
  Không xét số full-width

Root Cause:
  Review Checklist không có góc nhìn số full-width

Prevention:
  Thêm góc nhìn số full-width vào review input số
  Thêm case số full-width vào Unit Test
  Ghi rõ “full-width / half-width / mixed” trong prompt

Escalation:
  Đăng ký vào Project Knowledge
```


---

## 31. `31_SDD_Context-Loading-and-Exclusion_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu định nghĩa AI nên đọc gì, không nên đọc gì, đọc theo thứ tự nào và lấy gì làm bản chính.

### Giải thích thuật ngữ cho người mới

* **Context Loading**: Chọn thông tin đưa cho AI.
* **Exclusion**: Loại trừ.
* **Source Priority**: Thứ tự ưu tiên nguồn thông tin.
* **Prompt Injection**: Chỉ thị độc hại nhúng trong tài liệu bên ngoài.
* **Context Manifest**: Danh sách thông tin đã cho đọc / không cho đọc.

### Cách dùng

* Ngăn AI tin tài liệu cũ.
* Không đưa secret hoặc PII cho AI.
* Quyết định thứ tự ưu tiên latest source / DB / API / test.
* Phân loại tài liệu trước khi đưa RAG vào.
* Bàn giao sang Strategic Compact của 32 trong công việc dài.

### Ưu điểm

* Tăng độ chính xác AI.
* Giảm token cost.
* Ngăn tai nạn bảo mật.
* Ghi lại bằng chứng đã đọc / chưa đọc / không đọc được.
* Ít nhầm tài liệu cũ hoặc tài liệu ngoài là bản chính.

### Nhược điểm / điểm cần chú ý

* Cần con người phán đoán nguồn nào là bản chính.
* Dự án nhiều tài liệu tốn thời gian phân loại ban đầu.
* Loại trừ quá nhiều làm giảm độ chính xác AI.
* Đưa quá nhiều làm tăng token và nhiễu.

### Ví dụ

Khi có Excel đặc tả, PDF và source mới nhất:

```text
Source mới nhất:
  Ưu tiên làm căn cứ triển khai

Định nghĩa DB:
  Bắt buộc khi có thay đổi DB

Excel/PDF:
  Không dùng trực tiếp làm bản chính
  Trích xuất vào reference-extracts.md
  Chỉ nâng nội dung đã chốt lên Spec Pack

Web bên ngoài:
  Xem là tham khảo
  Xử lý như rủi ro prompt injection
```

---

## 32. `32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu để không làm mất tiền đề, quyết định, tiến độ và vấn đề chưa giải quyết trong các dự án dài, lớn, nhiều ngày, nhiều AI, nhiều người phụ trách.

### Giải thích thuật ngữ cho người mới

* **Long Context**: Trạng thái xử lý hội thoại dài hoặc nhiều thông tin.
* **Compact**: Tóm tắt / nén.
* **Strategic Compact**: Nén an toàn những thông tin cần để tiếp tục công việc.
* **Decision Ledger**: Sổ cái ghi quyết định.
* **Handoff Pack**: Gói bàn giao.
* **Work State Board**: Danh sách trạng thái công việc.

### Cách dùng

* Triển khai kéo dài nhiều ngày.
* Phân tích source lớn.
* Review nhiều AI.
* Review nhiều lớp Claude → Codex → Human.
* Tạm dừng / tiếp tục session.
* Thay người phụ trách.
* Khôi phục sau compact context.

### Ưu điểm

* AI và con người ít quên tiền đề.
* Tiếp tục công việc dài an toàn hơn.
* Dễ bàn giao giữa nhiều AI/người phụ trách.
* Có ký ức đã được artifact hóa, không phụ thuộc vào chat.

### Nhược điểm / điểm cần chú ý

* Compact xấu sẽ cố định hiểu nhầm.
* Không cập nhật thì nhanh chóng lỗi thời.
* Chỉ tóm tắt là chưa đủ.
* Nguy hiểm nếu không làm rõ file đã đọc và chưa đọc.

### Chi tiết

File 32 sắp xếp rằng 31 là “đưa gì vào context”, còn 32 là “cách không làm mất context và phán đoán đó khi làm việc dài, handoff, hoặc sau compact”.  
Căn cứ nội bộ: `32_SDD_Long-Context-and-Strategic-Compact_Ver.04_Japanese.md` L58-L118

### Ví dụ

Với thay đổi logic phân quyền kéo dài nhiều ngày, Strategic Compact ghi:

```text
Mục đích:
  Đổi kiểm tra quyền admin sang đặc tả mới

File đã đọc:
  AuthService
  PermissionRepository
  role_master
  admin screen route

Chưa đọc:
  Kiểm tra quyền phía batch

Quyết định:
  Không chỉ điều khiển hiển thị FE, mà BE cũng enforce

Chưa giải quyết:
  Tính tương thích role cũ
  Mức độ chi tiết audit log

Hành động tiếp theo:
  Cập nhật Impact Analysis
  Chuyển cho Security Reviewer
```

---

## 33. `33_SDD_Artifact-Governance-and-Traceability_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu quản lý bản chính, trạng thái, độ mới, căn cứ, quan hệ phái sinh, phê duyệt và traceability của artifact SDD.

### Giải thích thuật ngữ cho người mới

* **Artifact Governance**: Quản trị artifact.
* **Status**: Trạng thái như Draft / Reviewed / Approved / Superseded / Deprecated.
* **Freshness Check**: Kiểm tra artifact có còn mới không.
* **Decision Record**: Ghi chép quyết định.
* **Accepted Risk**: Rủi ro đã nhận biết và chấp nhận.
* **Audit Package**: Gói bằng chứng cho kiểm toán.

### Cách dùng

* Dự án có nhiều artifact.
* Dự án dài hạn.
* Review nhiều AI.
* Dự án cần kiểm toán hoặc giải thích với khách hàng.
* PR Gate hoặc phán đoán release.
* Truy vết từ yêu cầu đến test.

### Ưu điểm

* Biết đâu là bản chính.
* Phát hiện lệch giữa đặc tả, kế hoạch, triển khai, test và báo cáo.
* Quyết định của con người không bị chôn trong chat.
* Mạnh cho kiểm toán và đảm bảo chất lượng.
* Quản lý việc nâng cấp lên Failure Mode và Knowledge.

### Nhược điểm / điểm cần chú ý

* Artifact tăng quá nhiều thì nặng.
* Nếu không cập nhật status sẽ hình thức hóa.
* Nếu chỉ cập nhật Report mà bỏ Spec Pack thì hỏng.
* Cần vận hành để không trộn secret/PII vào bằng chứng.

### Chi tiết

File 33 yêu cầu nối Requirement → Spec → Plan → Code → Test → Review → Report, đồng thời tách quyết định con người, phán đoán AI, bằng chứng và suy đoán.  
Căn cứ nội bộ: `33_SDD_Artifact-Governance-and-Traceability_Ver.04_Japanese.md` L60-L118

### Ví dụ

Khi kiểm toán, cần truy được:

```text
Yêu cầu:
  Chỉ admin được xóa user

Spec:
  delete user requires ADMIN role

Code:
  UserController.delete
  UserService.delete

Test:
  admin can delete
  normal user cannot delete

Review:
  Security Reviewer approved

Decision:
  Audit log ghi user_id và actor_id

Risk:
  Tương thích API cũ xử lý ở phase sau
```

---

## 34. `34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu tích lũy và duy trì tri thức riêng của project ở dạng AI có thể tái sử dụng.

### Giải thích thuật ngữ cho người mới

* **Project Knowledge**: Tri thức riêng của project.
* **Pattern Library**: Tập các pattern triển khai đúng thường dùng.
* **Known Good Example**: Ví dụ triển khai đúng.
* **Known Bad Example**: Ví dụ không nên làm.
* **Expiry**: Hạn hiệu lực.
* **Owner**: Người chịu trách nhiệm quản lý tri thức.

### Cách dùng

* Sắp xếp thuật ngữ nghiệp vụ.
* Rule đặt tên DB.
* Ràng buộc framework hiện có.
* Method được dùng / method bị cấm.
* Ví dụ triển khai đúng/sai.
* Tiêu chuẩn log / kiểm tra quyền.
* Quy tắc xử lý số, ký tự, ngày tháng.

### Ưu điểm

* AI hiểu project sâu hơn.
* Dùng cho đào tạo người mới.
* Không phải giải thích lại cùng nội dung cho AI nhiều lần.
* Chuyển Failure Mode thành tri thức dùng ở lần sau.
* Biến tri thức cá nhân thành tri thức tổ chức.

### Nhược điểm / điểm cần chú ý

* Tri thức cũ là nguy hiểm.
* Ghi tất cả vào CLAUDE.md sẽ hỏng.
* Knowledge hóa không qua review sẽ cố định thói quen sai.
* Cần owner, evidence, status, expiry.

### Chi tiết

File 34 giải thích rằng file 29 là cơ chế học từ thất bại, còn file 34 là tổ chức học hỏi đó và các pattern thành công thành tri thức để AI dùng ở lần sau.  
Căn cứ nội bộ: `34_SDD_Project-Knowledge-and-Pattern-Library_Ver.04_Japanese.md` L67-L120

### Ví dụ

```md
# Pattern Card: Kiểm tra quyền

## Use When
Khi triển khai API chỉ dành cho admin

## Good Example
Ở đầu UserService.deleteUser(), gọi PermissionService.requireAdmin(actor)

## Bad Example
Chỉ điều khiển bằng cách ẩn button ở FE

## Evidence
Sự cố quá khứ: user thường gọi API xóa bằng cách nhập URL trực tiếp

## Tests
normal user receives 403
admin receives 200
```

---

## 40. `40_SDD_Advanced-Options-Overview-and-Selection-Guide_Ver.04_Japanese.md`

### Vai trò

Đây là cửa vào của toàn bộ Advanced Options nhóm 40.

### Giải thích thuật ngữ cho người mới

* **Advanced Option**: Tính năng nâng cao chỉ dùng cho dự án phức tạp hoặc rủi ro cao.
* **Selection Guide**: Hướng dẫn chọn cái nào để dùng.
* **Human Governance**: Phán đoán và phê duyệt cuối cùng bởi con người.
* **Ngăn áp dụng quá mức**: Không đưa vào quá nhiều quy trình nâng cao không cần thiết.

### Cách dùng

* Quyết định dùng phần nào trong 41–49.
* Chọn option nâng cao cho dự án lớn/rủi ro cao.
* Phán đoán đưa vào Multi-Agent, RAG, PR Gate, Token Optimization, v.v.
* Lưu Option Selection Record.

### Ưu điểm

* Tránh lạm dụng tính năng nâng cao.
* Xem Advanced là phần bổ sung chứ không thay thế Core.
* Nhận ra rủi ro khi đưa 42 hoặc 48 vào lúc 31–33 còn yếu.
* Xác nhận nguyên tắc: dù làm AI mạnh hơn cũng không biến AI thành quyền uy.

### Nhược điểm / điểm cần chú ý

* Nặng với người mới.
* Cần kinh nghiệm để phán đoán.
* Đưa toàn bộ nhóm 40 vào sẽ làm tải áp dụng rất cao.
* Advanced tiện lợi nhưng nếu không quản lý token/cost/security thì phản tác dụng.

### Chi tiết

File 40 nêu rằng nhóm 40 không thay thế Core; nó được thêm vào cho các dự án có source cực lớn/phức tạp, vùng rủi ro cao, tự động hóa AI review, nhiều AI, kiểm soát token, trace/evidence/evaluation.  
Căn cứ nội bộ: `40_SDD_Advanced-Options-Overview-and-Selection-Guide_Ver.04_Japanese.md` L53-L88

### Ví dụ

Nếu thay đổi logic phân quyền và thuộc đối tượng đưa PR Gate vào:

```text
Chọn ở file 40
43 Tool-Grounded Verification
45 Full Security
47 Automated PR Review
49 Evaluation
```

---

## 41. `41_SDD_Heavy-Source-Analysis-and-Repository-Intelligence-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu tạo Repository Intelligence cho dự án rất lớn, phức tạp, nhiều tech stack, nhiều repo hoặc legacy.

### Giải thích thuật ngữ cho người mới

* **Repository Intelligence**: Tri thức có cấu trúc về toàn bộ repository.
* **Repository Map**: Bản đồ toàn repo.
* **Module Map**: Bản đồ theo module.
* **Risk Hotspot Map**: Bản đồ điểm rủi ro.
* **Source Confidence Score**: Điểm tin cậy về mức hiểu source.
* **Impact Slice**: Phần thông tin được cắt ra, chỉ gồm phạm vi cần cho thay đổi lần này.

### Cách dùng

* Phân tích legacy lớn.
* Thay đổi nhiều module.
* Thay đổi xuyên FE / BE / DB / Batch / external IF.
* Dự án có nhiều framework riêng hoặc common platform.
* Dự án trước đây AI đã dùng method không tồn tại.
* Cần căn cứ mạnh cho phán đoán không ảnh hưởng.

### Ưu điểm

* Giúp AI xử lý source lớn dễ hơn.
* Tăng độ chính xác Impact Analysis.
* Có thể đưa cho AI phần quan trọng nhất.
* Review/Test/Security cùng nhìn một bản đồ.

### Nhược điểm / điểm cần chú ý

* Dễ hỏng nếu làm khi chưa có 31 Context Loading và 44 Token Optimization.
* Chi phí ban đầu cao.
* Cần vận hành cập nhật bản đồ.
* Không được phân tích chi tiết toàn bộ source cùng lúc.

### Chi tiết

File 41 nhấn mạnh thứ tự Repository Map → Module Map → Relevant Slice → Evidence Expansion.  
Căn cứ nội bộ: `41_SDD_Heavy-Source-Analysis-and-Repository-Intelligence-Option_Ver.04_Japanese.md` L59-L135

### Ví dụ

Khi thay đổi xử lý billing trong legacy lớn:

```text
Repository Inventory
  billing module
  customer module
  tax module
  accounting adapter

Risk Hotspot
  rounding
  transaction
  retry
  external accounting IF
  batch recalculation

Impact Slice
  BillingService
  BillingRepository
  TaxMaster
  BillingBatch
  BillingServiceTest
```

---

## 42. `42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu để sử dụng an toàn nhiều model, nhiều Agent và Orchestrator.

### Giải thích thuật ngữ cho người mới

* **Multi-Model**: Dùng nhiều model AI khác nhau.
* **Multi-Agent**: Dùng nhiều AI theo vai trò.
* **Specialist Agent**: AI có vai trò chuyên môn như Security Reviewer, Test Reviewer.
* **Model Router**: Cơ chế chuyển tác vụ nhẹ sang model rẻ/nhanh, phán đoán rủi ro cao sang model mạnh.
* **Arbiter / Judge**: Vai trò tích hợp và phân xử đầu ra từ nhiều Agent.
* **Policy Engine**: Cơ chế phán đoán dựa trên rule.
* **Recursive Review Loop**: Vòng lặp đánh giá lại review đầu tiên để cải thiện.

### Cách dùng

* PR review rủi ro cao.
* Tách góc nhìn Security / Bug / Test / Performance / Ops.
* Sắp xếp thông tin đưa cho human review.
* Model Routing.
* Recursive Review Loop.
* Consensus / Veto / Human Escalation.

### Ưu điểm

* Tách được các góc nhìn mà một AI dễ bỏ sót.
* Tăng độ chính xác review ở vùng rủi ro cao.
* Sắp xếp thông tin trước khi chuyển cho human review.
* Chỉ dùng model mạnh ở nơi cần.

### Nhược điểm / điểm cần chú ý

* Càng tăng Agent càng tăng token cost.
* Tăng xung đột ý kiến.
* Cho mọi Agent đọc toàn bộ sẽ hỏng.
* Đầu ra nhiều đến mức con người không review được thì phản tác dụng.
* Không được cấp quyền nguy hiểm cho Agent.

### Chi tiết

Kiến trúc khuyến nghị của file 42 là: Issue / PR / Requirement / Diff → Orchestrator → Risk Classifier → Context Builder → Token Budget Controller → Model Router → Agent Selector → Specialist Agents → Arbiter / Judge → 43 → Policy Engine → Human Governance.  
Căn cứ nội bộ: `42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Japanese.md` L119-L177

### Về RecursiveMAS

`RedursiveMAS` mà người dùng nhắc đến có thể là `RecursiveMAS-inspired` trong tài liệu. Trong ZIP không thấy cách viết `RedursiveMAS`, mà xác nhận có `RecursiveMAS-inspired`.

File 42 không đưa nghiên cứu RecursiveMAS nguyên bản vào, mà áp dụng có giới hạn như sau.

```text
- Không truyền latent state, chỉ truyền structured summary
- Tối đa 2–3 round
- Đầu ra Agent ở dạng JSON/bảng
- Không truyền raw conversation history
- Rủi ro nghiêm trọng chuyển cho con người
- Quản lý token budget bằng file 44
```

Căn cứ nội bộ: `42_SDD_Multi-Model-Multi-Agent-Orchestrator-Option_Ver.04_Japanese.md` L393-L435

### Ví dụ

Khi xem PR thay đổi API phân quyền bằng Multi-Agent:

```text
Bug Reviewer:
  Xem logic bug

Security Reviewer:
  Xem auth bypass, privilege escalation

Test Reviewer:
  Xem test gap

Architect Agent:
  Xem boundary thiết kế

Arbiter:
  Gộp chỉ trích trùng lặp, chuyển critical sang 43
```

---

## 43. `43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu kiểm chứng AI review hoặc đầu ra Multi-Agent bằng Tool result, Evidence, Policy và Human Governance.

### Giải thích thuật ngữ cho người mới

* **Opinion**: Ý kiến của AI.
* **Evidence**: Bằng chứng.
* **Tool Result**: Kết quả test, build, SAST, v.v.
* **Veto**: Điều kiện bác bỏ / dừng.
* **Weighted Consensus**: Đồng thuận có trọng số theo mức quan trọng.
* **Policy Engine**: Phán đoán bằng rule.
* **Human Escalation**: Chuyển phán đoán lên con người.

### Cách dùng

* Nối AI review với PR Gate.
* Tích hợp Tool result và AI finding.
* Giảm false positive.
* Phán đoán rủi ro cao như Security / DB / API / Contract.
* Tích hợp ý kiến nhiều Agent.

### Ưu điểm

* Không xem câu “không có vấn đề” của AI là bằng chứng.
* Có thể xác minh bằng kết quả thực như test và SAST.
* Không để critical finding bị đa số phiếu phủ lấp.
* Chuyển summary có căn cứ cho human review.

### Nhược điểm / điểm cần chú ý

* Cần chuẩn bị tool.
* Tool result cũng có false positive / false negative.
* Evidence Linking cẩu thả sẽ dẫn đến phán đoán sai.
* Thiết kế Policy phức tạp.

### Chi tiết

File 43 nêu rằng đầu ra AI về cơ bản là ý kiến và cần tách khỏi Evidence. Evidence hierarchy phân tầng từ Level 0 là phát biểu AI không căn cứ đến Level 5 là telemetry production / bằng chứng incident. Không nên phán đoán rủi ro cao chỉ bằng Level 0–2.  
Căn cứ nội bộ: `43_SDD_Tool-Grounded-Verification-and-Consensus-Option_Ver.04_Japanese.md` L79-L123

### Ví dụ

Dù 3 AI Agent nói “không có vấn đề”, nếu contract test fail thì không được merge.

```text
AI Opinion:
  Không có vấn đề

Tool Evidence:
  contract test failed

Policy:
  API contract failure blocks merge

Decision:
  Human Review / Block
```

---

## 44. `44_SDD_Token-Optimization-and-Cost-Control-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu kiểm soát số lượng token, latency, chi phí AI và ô nhiễm context.

### Giải thích thuật ngữ cho người mới

* **Token Budget**: Ngân sách token được phép dùng.
* **Prompt Caching**: Cơ chế tái sử dụng prefix giống nhau để giảm chi phí.
* **Context Caching**: Cơ chế tái sử dụng context hay dùng.
* **Exact Cache**: Cache khớp hoàn toàn.
* **Semantic Cache**: Cache cho truy vấn có ý nghĩa tương tự.
* **Embedding Cache**: Cache vector cho tìm kiếm.
* **Retrieval Cache**: Cache kết quả tìm kiếm.
* **File Summary Cache**: Cache tóm tắt file.
* **Tool Output Compression**: Tóm tắt log test, v.v. trước khi đưa cho AI.
* **Agent Context Partitioning**: Chỉ đưa thông tin cần thiết cho từng Agent.
* **Recursive State Compression**: Không đưa toàn bộ hội thoại cũ, chỉ đưa trạng thái.
* **Model Routing / Cascade**: Dùng model rẻ/nhanh và model mạnh đúng chỗ.

### Cách dùng

* Khi dùng Multi-Agent.
* Khi Heavy Source Analysis.
* Xử lý test log hoặc build log khổng lồ.
* Giảm cost trên mỗi PR.
* Xử lý phình context trong session dài.
* Kiểm soát Recursive Review Loop.

### Ưu điểm

* Ngăn bùng nổ chi phí.
* Không để thông tin quan trọng bị chìm.
* Dùng model mạnh chỉ ở nơi cần.
* Không phải cho AI đọc lại cùng thông tin nhiều lần.
* Vận hành Multi-Agent trở nên thực tế.

### Nhược điểm / điểm cần chú ý

* Cắt quá mức làm giảm chất lượng.
* Nguy hiểm nếu nén làm mất điều kiện phân quyền, DB write, transaction, migration, security setting.
* Không được chia sẻ cache vượt qua security boundary.
* Nếu chỉ giảm cost nhưng valid finding giảm thì thất bại.

### Chi tiết

File 44 xem giảm token không phải là làm prompt ngắn đơn thuần, mà thiết kế theo 4 nguyên tắc:

```text
1. Không gửi
2. Làm ngắn
3. Tái sử dụng
4. Xử lý rẻ hơn
```

Token Optimization Layer gồm Token Budget Controller, Prompt Caching, Context Caching, Exact Cache, Semantic Cache, Embedding Cache, Retrieval Cache, File Summary Cache, Repository Map / Code Map, RAG Optimization, Context Compression, Tool Output Compression, Agent Context Partitioning, Recursive State Compression, Model Routing / Model Cascade, Early Exit, Batch / Flex Processing, Cost Observability, v.v.  
Căn cứ nội bộ: `44_SDD_Token-Optimization-and-Cost-Control-Option_Ver.04_Japanese.md` L63-L113

Phía Claude API cũng giải thích prompt caching là tính năng giúp xử lý hiệu quả nội dung lặp lại bằng automatic caching hoặc explicit cache breakpoints. ([Claude Platform][6])

### Ví dụ

Ví dụ xấu:

```text
Đưa toàn bộ repo, toàn bộ log, toàn bộ lịch sử hội thoại cho mọi Agent
```

Ví dụ tốt:

```text
Common Context:
  ticket summary
  AC summary
  diff summary
  risk hotspots

Security Agent:
  auth code
  permission map
  secret scan summary

Test Agent:
  changed tests
  failed test summary

Architect Agent:
  module map
  dependency map
```

---

## 45. `45_SDD_Full-Security-and-Agentic-AI-Governance-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu quản trị an toàn vận hành nâng cao gồm AI Agent, MCP, hooks, công cụ bên ngoài, PR auto review, RAG, cache, CI/CD và nhiều Agent.

### Giải thích thuật ngữ cho người mới

* **Agentic AI**: Dạng AI dùng tool và tự chủ tiến hành công việc.
* **Governance**: Kiểm soát / quản trị.
* **Threat Model**: Sắp xếp các tấn công hoặc tai nạn giả định.
* **Permission Broker**: Cơ chế trung gian kiểm soát quyền.
* **Tool Gateway**: Cổng quản lý thực thi tool.
* **RAG Poisoning**: Tấn công trộn thông tin độc hại vào nguồn tìm kiếm.
* **Excessive Agency**: Vấn đề cấp cho AI quyền tự chủ quá mức.
* **Human-in-the-loop**: Vận hành có bước xác nhận của con người.

### Cách dùng

* Dùng MCP server / connector.
* Dùng hooks / plugin / extension.
* Đưa AI vào PR review hoặc QA Gate.
* Để AI chạy và giải thích test / lint / SAST / secret scan.
* Xử lý xác thực, phân quyền, thông tin cá nhân, thanh toán, audit, infra, DB migration.
* Để AI đề xuất patch hoặc phương án sửa tự động.

### Ưu điểm

* Kiểm soát vùng càng tiện càng nguy hiểm của AI.
* Chuẩn bị cho prompt injection, tool misuse, secret leakage, RAG poisoning.
* Có thể kiểm toán hành động của AI.
* Đưa human approval vào merge/deploy/write/delete/send.
* Vận hành an toàn nền tảng phát triển AI nâng cao.

### Nhược điểm / điểm cần chú ý

* Là option nặng, không nên full apply cho mọi dự án.
* Cần người phụ trách security tham gia.
* Thiết kế quyền sai có thể gây tai nạn.
* Không được biến AI thành người phê duyệt.
* Vận hành không có audit log là nguy hiểm.

### Chi tiết

File 45 nêu rằng AI là trợ lý phát triển mạnh, nhưng không phải chủ thể quyền hạn mà là đối tượng cần kiểm soát; phán đoán của AI không phải bằng chứng mà là đối tượng cần kiểm chứng; hành động của AI là đối tượng kiểm toán; các thao tác ghi, gửi ra ngoài, ảnh hưởng production cần con người phê duyệt.  
Căn cứ nội bộ: `45_SDD_Full-Security-and-Agentic-AI-Governance-Option_Ver.04_Japanese.md` L57-L134

### Ví dụ

Khi dùng MCP để kết nối GitHub, JIRA hoặc DB:

```text
Read:
  issue, PR, logs, metrics

Ask:
  đăng comment
  tạo PR
  chạy test

Deny:
  DB write
  lấy secret
  deploy
  xóa branch
  force push
```

---

## 46. `46_SDD_RAG-CodeMap-and-Context-Compression-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu lấy ra an toàn các phần code, tài liệu thiết kế, test, log và knowledge khổng lồ ở đúng lúc, kèm căn cứ, đúng độ chi tiết, rồi nén và phân phối cho từng Agent.

### Giải thích thuật ngữ cho người mới

* **RAG**: Retrieval Augmented Generation, cơ chế tìm kiếm thông tin cần thiết rồi đưa cho AI.
* **Code Map**: Bản đồ cấu trúc code.
* **Chunking**: Chia tài liệu/code thành đơn vị nhỏ.
* **Lexical Index**: Chỉ mục tìm kiếm theo keyword.
* **Vector Index**: Chỉ mục tìm kiếm theo ý nghĩa.
* **Symbol Index**: Chỉ mục theo tên hàm/class.
* **Rerank**: Sắp xếp lại kết quả tìm kiếm.
* **Evidence ID**: ID để truy vết căn cứ.
* **Context Compression**: Nén thông tin nhưng giữ phần quan trọng.

### Cách dùng

* Dự án mà đọc toàn repo bằng AI không thực tế.
* Dự án băng qua quan hệ FE/BE/DB/API/test.
* Microservice / multi-repo.
* Tham chiếu sự cố quá khứ, tri thức review, project knowledge.
* Phân phối context cho nhiều Agent.
* Giảm token/cost.
* Đánh giá chất lượng tìm kiếm RAG.

### Ưu điểm

* Tránh đưa toàn văn.
* Ít bỏ sót nơi liên quan.
* Có thể cấp context cần thiết cho từng Agent.
* Truy vết căn cứ bằng evidence ID.
* Dễ kết hợp giảm token và tăng độ chính xác.

### Nhược điểm / điểm cần chú ý

* Chất lượng tìm kiếm RAG kém sẽ tạo nhiễu.
* Nguy hiểm nếu nhặt branch cũ hoặc tài liệu bị nhiễm độc.
* Nguy hiểm nếu tóm tắt làm rơi mất kiểm tra phân quyền hoặc xử lý exception.
* Không được index hóa PII hoặc secret.
* Dự án nhỏ thì chỉ định trực tiếp thường nhanh và an toàn hơn.

### Chi tiết

File 46 nêu rằng không đưa toàn bộ repo cho AI đọc; thay vào đó đưa bản đồ repo, không đưa toàn văn mà đưa evidence ID và chỗ cần thiết, không đưa lịch sử hội thoại mà đưa trạng thái và rủi ro chưa giải quyết.  
Căn cứ nội bộ: `46_SDD_RAG-CodeMap-and-Context-Compression-Option_Ver.04_Japanese.md` L57-L149

### Ví dụ

Khi dùng RAG để tìm điểm kiểm tra phân quyền:

```text
Index:
  symbol index
  call graph
  permission map
  API contract index

Query:
  delete user permission check

Retrieved:
  UserController.delete
  UserService.delete
  PermissionService.requireAdmin
  UserServiceTest.delete_forbidden_for_normal_user

Evidence:
  file path
  line
  commit hash
  source confidence
```

---

## 47. `47_SDD_Automated-PR-Review-and-AI-QA-Gate-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu định nghĩa Automated PR Review / AI QA Gate.

### Giải thích thuật ngữ cho người mới

* **PR / Pull Request**: Đơn vị review trước khi nhập code change.
* **MR / Merge Request**: Khái niệm tương đương trong GitLab.
* **QA Gate**: Gate xác nhận chất lượng.
* **Policy > Tool Result > Human Review > AI Finding > Heuristic**: Thứ tự ưu tiên của căn cứ phán đoán.
* **Critical Finding**: Chỉ ra nghiêm trọng chặn merge.
* **PR Comment Quality**: Độ hữu ích, ngắn gọn và có căn cứ của PR comment.

### Cách dùng

* Tìm lỗi rõ ràng trước human review.
* Giảm thiếu sót góc nhìn review.
* Tích hợp test / lint / SAST / SCA / secret scan vào phán đoán.
* Escalate thay đổi high-risk cho con người.
* Tạo PR comment ngắn và có căn cứ.
* Cải thiện liên tục false positive và miss.

### Ưu điểm

* Giảm tải review.
* Phân loại rủi ro theo PR.
* Tích hợp AI review và kết quả CI.
* Làm nổi bật tự động thay đổi high-risk.
* Lưu PR Gate như audit evidence.

### Nhược điểm / điểm cần chú ý

* AI review không thay thế human review.
* Cần đánh giá block nhầm và bỏ sót.
* Cần thiết kế quyền CI và quyền PR.
* PR comment quá nhiều sẽ thành nhiễu.
* Vùng high-risk cần human review hoặc block, không dùng đa số phiếu.

### Chi tiết

File 47 nêu rằng AI review là một phần của PR Gate chứ không có quyền cuối cùng; AI review được đánh giá bằng valid finding rate, missed finding rate, human review time và production quality, không phải bằng số lượng comment AI.  
Căn cứ nội bộ: `47_SDD_Automated-PR-Review-and-AI-QA-Gate-Option_Ver.04_Japanese.md` L61-L99

### Ví dụ

Khi có thay đổi logic phân quyền trong PR:

```text
CI:
  unit test pass
  integration test pass
  SAST no critical
  secret scan pass

AI:
  Security Reviewer finds possible auth bypass

Policy:
  critical security candidate -> Human Review required

Decision:
  merge block until security reviewer approves
```

---

## 48. `48_SDD_Parallel-Worktree-and-Large-Refactoring-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu tiến hành an toàn Parallel Worktree, refactor lớn và so sánh nhiều phương án triển khai.

### Giải thích thuật ngữ cho người mới

* **git worktree**: Tính năng Git tạo thư mục làm việc khác của cùng repository.
* **Parallel Worktree**: Kiểm chứng song song nhiều phương án trong các vùng làm việc tách biệt.
* **Large Refactoring**: Cải thiện cấu trúc nội bộ quy mô lớn.
* **Branch by Abstraction**: Cách thêm lớp trừu tượng rồi chuyển dần.
* **Strangler Fig**: Cách thay thế hệ thống cũ dần dần bằng hệ thống mới.
* **Feature Flag**: Cờ bật/tắt chức năng.
* **Dual Run / Shadow Mode**: Chạy song song xử lý cũ và mới để so sánh.
* **Expand-Contract Migration**: Cách thay đổi DB an toàn theo thứ tự mở rộng → di chuyển → thu hẹp.

### Cách dùng

* So sánh nhiều phương án bởi nhiều AI / nhiều người.
* Chia refactor lớn thành phần nhỏ.
* Di chuyển legacy từng bước.
* Thay đổi xuyên FE/BE/DB/Batch/Microservice.
* Tích hợp nhiều patch.
* Tránh PR quá lớn.

### Ưu điểm

* Tăng tốc khám phá.
* So sánh nhiều phương án.
* Chia thay đổi lớn thành diff nhỏ an toàn.
* Dễ giữ khả năng rollback.
* Tránh AI làm việc song song bị lẫn lộn.

### Nhược điểm / điểm cần chú ý

* Song song hóa làm tăng tai nạn tích hợp.
* Nếu không tách worktree / branch / artifact / context / test thì sẽ hỏng.
* PR cuối cùng chỉ nên là patch tích hợp.
* Đây không phải cơ chế để AI tự do tạo nhiều triển khai.

### Chi tiết

File 48 nêu rằng Parallel worktree không phải là cơ chế để AI tự do triển khai nhiều phương án, mà là quy trình khám phá, so sánh và tích hợp có kiểm soát, có giả thuyết rõ, boundary, artifact, tiêu chí kiểm chứng và người chịu trách nhiệm tích hợp.  
Căn cứ nội bộ: `48_SDD_Parallel-Worktree-and-Large-Refactoring-Option_Ver.04_Japanese.md` L83-L131

### Ví dụ

Tách trách nhiệm của một Service khổng lồ:

```text
worktree-A:
  Tách Service bằng diff tối thiểu

worktree-B:
  Đưa Adapter mới vào

worktree-C:
  Sắp xếp tầng DB access

So sánh:
  diff size
  test pass
  performance
  migration risk
  maintainability

Cuối cùng:
  Tích hợp các phần tốt của A và B thành patch cuối
```

---

## 49. `49_SDD_Evaluation-Observability-and-Continuous-Optimization-Option_Ver.04_Japanese.md`

### Vai trò

Đây là tài liệu xử lý evaluation, observability, metrics, tối ưu liên tục, đảm bảo chất lượng, tối ưu chi phí, kiểm toán và vòng lặp cải tiến của hệ thống phát triển AI.

### Giải thích thuật ngữ cho người mới

* **Evaluation**: Đánh giá.
* **Observability**: Khả năng quan sát.
* **Metric**: Chỉ số.
* **Trace**: Bản ghi truy vết luồng xử lý.
* **Golden PR Dataset**: Bộ dữ liệu PR có đáp án chuẩn để đánh giá.
* **False Positive**: Phát hiện nhầm.
* **False Negative / Missed Bug**: Bỏ sót bug.
* **Cost per Valid Finding**: Chi phí cho mỗi chỉ ra hữu ích.
* **AI Regression Test**: Test để xác nhận thay đổi cấu hình AI không làm giảm chất lượng.
* **Red Team Eval**: Đánh giá từ góc nhìn tấn công.

### Cách dùng

* Đo hiệu quả áp dụng AI.
* Cải thiện PR QA Gate.
* Quản lý thay đổi Agent / Model / Prompt / Rule / Context.
* Phân tích phát hiện nhầm và bỏ sót.
* Quản lý trade-off giữa token/cost/latency và chất lượng.
* Nâng Failure Mode thành evaluation dataset.
* Tạo Executive Dashboard.

### Ưu điểm

* Không để áp dụng AI thành “cài vào là xong”.
* Đo được thứ gì có tác dụng.
* Nhìn hiệu quả thật chứ không nhìn số comment AI.
* Đánh giá được thay đổi model / prompt / rules / context.
* Giải thích hiệu quả với ban lãnh đạo.

### Nhược điểm / điểm cần chú ý

* Thiết kế metric khó.
* Làm dashboard hoàn chỉnh ngay từ đầu sẽ nặng.
* Cần thu thập dữ liệu.
* Chỉ số không thể đo toàn bộ niềm tin và chất lượng của con người.
* Cần hiệu chỉnh LLM-as-Judge.

### Chi tiết

File 49 nêu rằng thành công của áp dụng AI không đo bằng số comment AI hay lượng sinh ra, mà bằng valid finding rate, missed finding rate, production quality, review time, cost per valid finding và niềm tin của con người.  
Căn cứ nội bộ: `49_SDD_Evaluation-Observability-and-Continuous-Optimization-Option_Ver.04_Japanese.md` L79-L135

### Ví dụ

Đánh giá hằng tháng nền tảng AI PR review:

```text
Valid finding rate:
  42%

False positive rate:
  28%

Missed critical bug:
  1 mục

Average review latency:
  Giảm 12 phút

Cost per valid finding:
  $1.80

Action:
  Cải thiện prompt của Security Agent
  Cải thiện RAG retrieval filter
  Giảm comment severity thấp
```


---

# 6. Rà soát lại các yếu tố kỹ thuật chính được đưa vào

Phần này sắp xếp lại đầy đủ các kỹ thuật và cơ chế chính có trong bộ tài liệu.

---

## 6.1 SDD / Specification Driven Development

Đây là phát triển định hướng đặc tả.

Trung tâm gồm:

* Tạo đặc tả trước.
* Làm rõ AC.
* Phân tích phạm vi ảnh hưởng.
* Tạo kế hoạch triển khai.
* Tạo góc nhìn review trước.
* Tạo kế hoạch test.
* Lưu bằng chứng.
* Đưa học hỏi về lần sau.

---

## 6.2 Spec Pack

Đây là bản chính để AI và con người làm việc với cùng một hiểu biết.

Bao gồm:

* Bối cảnh.
* Mục đích.
* Phạm vi.
* Ngoài phạm vi.
* AC.
* Business rule.
* Lỗi.
* Quyền hạn.
* DB.
* API.
* Góc nhìn test.
* Điểm chưa xác định.
* Suy đoán của AI.
* Human Decision Required.

---

## 6.3 Source Availability

Ghi lại việc đã đọc được source, định nghĩa DB, đặc tả API, test và tài liệu bên ngoài cần thiết hay chưa.

Điều quan trọng là **không che giấu thứ chưa đọc được**.

---

## 6.4 Source Intelligence

Đây là hệ thống kỹ thuật tạo bản đồ source.

Bao gồm:

* Source Inventory.
* Entry Point Map.
* Route / API Map.
* Service Layer Map.
* Repository / DB Map.
* Data Flow Map.
* External Interface Map.
* Batch / Job Map.
* Event / Message Map.
* FE/BE Contract Map.
* Test Map.

---

## 6.5 Repository Intelligence

Đây là bản nâng cao của Source Intelligence cho repo lớn.

Bao gồm:

* Repository Inventory.
* Architecture / Module Map.
* Call Graph.
* Dependency Map.
* DB / Migration Map.
* External IF / Batch / Event Map.
* Test / CI / Tool Map.
* Risk Hotspot Map.
* Source Confidence Score.
* Impact Slice.

---

## 6.6 Context Loading / Exclusion

Đây là kỹ thuật kiểm soát thông tin đưa cho AI.

Phân loại:

* Always Include.
* Include if relevant.
* Ask before include.
* Exclude.
* Never include.

Đối tượng quan trọng:

* latest source.
* định nghĩa DB.
* API contract.
* test.
* project knowledge.
* external docs.
* Office files.
* logs.
* secrets.
* PII.

---

## 6.7 Strategic Compact

Đây là nén trạng thái cho công việc dài.

Bao gồm:

* Mục tiêu hiện tại.
* Stable Facts.
* File đã đọc.
* File chưa đọc.
* Quyết định.
* Vấn đề chưa giải quyết.
* Rủi ro.
* Hành động tiếp theo.
* Nơi bàn giao.

---

## 6.8 Artifact Governance

Đây là quản lý bản chính của artifact.

Quản lý:

* status.
* owner.
* freshness.
* evidence.
* derived from.
* approved by.
* superseded by.
* traceability.
* accepted risk.
* test skip reason.

---

## 6.9 Traceability Matrix

Đây là bảng nối yêu cầu, đặc tả, triển khai, test, review và báo cáo.

Ví dụ:

```text
REQ-001
  -> SPEC-001
  -> PLAN-003
  -> CODE UserService.java
  -> TEST UserServiceTest
  -> REVIEW Security Reviewer
  -> REPORT accepted
```

---

## 6.10 Review / TestCode Enhancement

Đây là tăng cường review và thiết kế test.

Bao gồm:

* High-signal review.
* Severity model.
* False Positive triage.
* Self Review.
* Independent Review.
* Unit Test.
* Integration Test.
* Contract Test.
* E2E Test.
* Black-box Test.
* Regression Test.
* Test Results Evidence.

---

## 6.11 Security Gate

Đây là hàng rào an toàn cho môi trường phát triển AI và ứng dụng.

Bao gồm:

* `.claude/CLAUDE.md`
* `.claude/settings.json`
* deny / ask / allow
* secrets exclusion
* chống prompt injection
* external content intake
* SAST
* SCA
* Secrets Scan
* SBOM
* CI Security

Tài liệu chính thức của Claude Code cũng giải thích rằng Claude Code đọc `CLAUDE.md`, `settings.json`, hooks, skills, commands, subagents, rules, auto memory từ thư mục `.claude`. ([Claude][7])  
Ngoài ra, phần cấu hình quyền giải thích có rule allow / ask / deny, deny được ưu tiên, và quyền được cưỡng chế bởi phía Claude Code chứ không phải model. ([Claude][8])

---

## 6.12 FE/BE Contract

Đây là quản lý hợp đồng giữa FE và BE.

Bao gồm:

* endpoint.
* method.
* path.
* request DTO.
* response DTO.
* schema.
* validation.
* error code.
* message.
* i18n.
* permission.
* role.
* tenant.
* ownership.
* audit.
* FE state.
* BE invariant.
* transaction.
* test contract.

---

## 6.13 Microservice / MultiRepo Analysis

Đây là phân tích ảnh hưởng của hệ phân tán.

Bao gồm:

* Service Catalog.
* Service Dependency Map.
* API Contract.
* Event Contract.
* Schema Ownership.
* DB Ownership.
* Retry.
* Idempotency.
* Eventual Consistency.
* Deploy Order.
* Rollback Sequence.
* Trace ID / Correlation ID.
* Logs / Metrics / Alerts.

---

## 6.14 Failure Mode and Continuous Learning

Đây là cơ chế biến thất bại thành tài sản cho lần sau.

Bao gồm:

* Failure Mode Index.
* Root Cause.
* Detection.
* Prevention.
* Rule update.
* Prompt update.
* Checklist update.
* Test template update.
* CI rule update.
* Knowledge promotion.
* Evaluation dataset promotion.

---

## 6.15 Project Knowledge and Pattern Library

Đây là nền tảng tái sử dụng tri thức riêng của project.

Bao gồm:

* business glossary.
* DB naming rule.
* framework constraint.
* allowed method.
* denied method.
* known good example.
* known bad example.
* security pattern.
* logging pattern.
* test data standard.
* expiry.
* owner.
* evidence.

---

## 6.16 Multi-Model / Multi-Agent

Đây là việc dùng nhiều model và nhiều Agent.

Ví dụ Agent:

* Requirement Clarifier.
* Architect Agent.
* Bug Reviewer.
* Security Reviewer.
* Test Reviewer.
* Performance Reviewer.
* Maintainability Reviewer.
* SRE/Ops Reviewer.
* Documentation Reviewer.
* Arbiter / Judge.

---

## 6.17 Orchestrator

Đây là vai trò điều phối nhiều Agent.

Trách nhiệm:

* phân loại rủi ro.
* chọn Agent.
* phân bổ context.
* quản lý token budget.
* cưỡng chế output schema.
* kiểm soát recursive loop.
* phán đoán Stop/Human Review.
* bàn giao cho Arbiter / 43.

---

## 6.18 Recursive Review Loop / RecursiveMAS-inspired

Đây là cơ chế đánh giá lại review đầu tiên để cải thiện.

Round tiêu chuẩn:

```text
Round 0: Context Builder
Round 1: Specialist Agents review độc lập
Round 2: Xem structured finding của Agent khác và đánh giá lại
Round 3: Arbiter tích hợp và chuyển sang 43
```

Giới hạn:

* Tối đa 2–3 round.
* Cấm raw conversation history.
* Chỉ structured summary.
* Quản lý token budget.
* Rủi ro nghiêm trọng chuyển cho con người.

---

## 6.19 Tool-Grounded Verification

Đây là cơ chế kiểm chứng ý kiến AI bằng kết quả công cụ thực tế.

Ví dụ tool:

* unit test.
* integration test.
* build.
* typecheck.
* lint.
* SAST.
* SCA.
* secret scan.
* migration dry-run.
* contract test.
* benchmark.
* e2e.
* a11y.

---

## 6.20 Evidence Hierarchy

Đây là tầng bậc độ mạnh của bằng chứng.

```text
Level 0: Unsupported AI assertion
Level 1: AI assertion with source reference
Level 2: Multiple agents agree with source reference
Level 3: Tool result supports/contradicts
Level 4: Human reviewer verifies
Level 5: Production telemetry / incident evidence
```

Không phán đoán rủi ro cao chỉ bằng Level 0–2.

---

## 6.21 Veto + Weighted Consensus

Đây là cách hình thành đồng thuận không dùng đa số phiếu đơn thuần, mà dừng rủi ro nghiêm trọng.

Ví dụ:

* Security Critical dù chỉ 1 trường hợp cũng là ứng viên Veto.
* Data loss risk cần Human Review.
* Tool failure ưu tiên hơn AI consensus.
* Coverage gap tăng trọng số của Test Reviewer.
* Architecture issue tăng trọng số của Architect/Human.

---

## 6.22 Token Optimization

Đây là hệ thống quản lý token, chi phí và độ trễ.

Bao gồm:

* Token Budget Controller.
* Prompt Caching.
* Context Caching.
* Exact Cache.
* Semantic Cache.
* Embedding Cache.
* Retrieval Cache.
* File Summary Cache.
* Repository Map / Code Map.
* RAG Optimization.
* Context Compression.
* Tool Output Compression.
* Agent Context Partitioning.
* Recursive State Compression.
* Model Routing / Model Cascade.
* Early Exit.
* Batch / Flex Processing.
* Cost Observability.

---

## 6.23 Prompt Caching

Đây là thiết kế tái sử dụng prefix giống nhau để tăng hiệu quả xử lý.

Nguyên tắc cơ bản trong SDD là:

```text
Static First, Dynamic Last
```

Static prefix:

* Chính sách SDD chung.
* Agent role catalog.
* severity model.
* output schema.
* security hard rules.
* phần ổn định của project glossary.

Dynamic suffix:

* ticket summary.
* diff summary.
* changed files.
* tool result summary.
* human instruction.

---

## 6.24 Context Compression

Đây không chỉ là làm thông tin ngắn hơn, mà là nén vẫn giữ boundary an toàn quan trọng.

Các thứ cần chú ý khi nén:

* điều kiện phân quyền.
* điều kiện validation.
* tính toán số tiền/số lượng.
* DB write.
* transaction boundary.
* retry/idempotency.
* error handling.
* bước migration.
* security setting.

---

## 6.25 Tool Output Compression

Không đưa log khổng lồ nguyên văn cho AI, mà giữ lại thông tin cần thiết.

Cần giữ:

* command.
* exit code.
* verdict.
* failed tests.
* first stack frame.
* file/line.
* skipped tests and risk.
* raw log path/hash.

---

## 6.26 RAG

Đây là cơ chế tìm kiếm và đưa căn cứ cần thiết cho AI.

Tuy nhiên, RAG trong SDD không chỉ là vector search.

Các index gồm:

* lexical index.
* vector index.
* symbol index.
* call graph.
* dependency graph.
* API contract index.
* DB schema index.
* test index.
* failure mode index.
* project knowledge index.

---

## 6.27 Code Map

Đây là bản đồ để xử lý code lớn.

Bao gồm:

* module responsibility.
* file purpose.
* public interface.
* side effects.
* DB access.
* external API.
* permission check.
* error handling.
* related tests.
* critical branches.
* do-not-omit invariants.

---

## 6.28 Agentic AI Governance

Đây là quản trị vận hành nâng cao trong đó AI dùng tool.

Bao gồm:

* Input Security.
* Tool Security.
* Data Security.
* Governance Security.
* Supply Chain Security.
* Permission Broker.
* Tool Gateway.
* MCP Gateway.
* Human approval.
* Audit log.
* Red Team Eval.

---

## 6.29 MCP Governance

Đây là quản trị kết nối MCP.

Điểm cần kiểm tra:

* MCP server nào.
* Chỉ read hay có cả write.
* Có quyền delete/send/deploy không.
* token scope là gì.
* Có audit log không.
* Có rủi ro prompt injection không.
* scope theo project hay global.
* có allowlist / denylist không.

---

## 6.30 Hooks Governance

Đây là quản trị hooks.

Cách dùng tốt:

* lint.
* test.
* formatting.
* notification.
* evidence logging.
* safety check.

Cách dùng nguy hiểm:

* auto deploy.
* auto DB write.
* gửi secret.
* liên lạc ra ngoài chưa thẩm định.
* destructive command.

---

## 6.31 Everything Claude Code / yếu tố tương tự ECC

Sau khi kiểm tra lại, trong ZIP không có chính chữ viết tắt `ECC`. Tuy nhiên, có nhiều chỗ nhắc đến `Everything Claude Code`.

Repository công khai Everything Claude Code giải thích đây là performance optimization system cho AI agent harness, bao gồm skills, instincts, memory optimization, continuous learning, security scanning, research-first development, agents, hooks, rules, MCP configurations, v.v. ([GitHub][9])

Các yếu tố tương tự ECC được đưa vào SDD pack như sau.

| Yếu tố tương tự ECC | Cách xử lý trong SDD |
| ------------------ | -------------------- |
| skills | Đưa vào sau thẩm định như quy trình tái sử dụng |
| rules | Chỉ phản ánh phần cần thiết vào `.claude/rules` hoặc `docs/standards` |
| agents | Đưa vào có kiểm soát bằng Specialist Agents ở file 42 |
| hooks | Theo 25/45, đưa vào từng bước từ notification, log, lint |
| MCP | Kiểm kê theo project scope, cẩn trọng với write/delete/send |
| memory optimization | Kết nối với 32 Strategic Compact và 44 State Compression |
| continuous learning | Kết nối với 29 Failure Mode và 34 Knowledge |
| security scanning / AgentShield | Kết nối với 25/45/CI |
| AGENTS.md | Chuẩn bị như chỉ thị chung cho Codex / Cursor / OpenCode |
| research-first development | Kết nối với tư tưởng SDD: khảo sát Spec / Source / Impact trước khi triển khai |

Điểm quan trọng là trong SDD, các yếu tố ECC không được đưa vào vì “tiện thì dùng hết”, mà được **chọn đưa vào an toàn như các bộ phận đã qua thẩm định**.

---

## 6.32 Automated PR Review / AI QA Gate

Đây là kỹ thuật đưa AI review vào PR.

Bao gồm:

* PR Risk Classifier.
* Trigger Policy.
* Agent Selection Matrix.
* Tool Result Intake.
* PR Review Record.
* QA Gate Record.
* Policy Engine.
* Human Escalation.
* Valid Finding Rate.
* Missed Bug Tracking.

---

## 6.33 Parallel Worktree / Large Refactoring

Đây là kỹ thuật khám phá và tích hợp song song thay đổi lớn một cách an toàn.

Bao gồm:

* git worktree.
* alternative implementation.
* option record.
* diff comparison.
* integration branch.
* baseline test.
* characterization test.
* slice refactoring.
* feature flag.
* rollout / rollback.
* disposal / archive.

---

## 6.34 Evaluation / Observability

Đây là cơ chế đánh giá liên tục hệ thống phát triển AI.

Bao gồm:

* Trace.
* Metrics Taxonomy.
* Quality Metrics.
* Safety Metrics.
* Efficiency Metrics.
* Cost Metrics.
* Agent / Model Metrics.
* Context / RAG Metrics.
* Developer Experience Metrics.
* Golden PR Dataset.
* Missed Bug Dataset.
* Offline Eval.
* Shadow Eval.
* Online Eval.
* Red Team Eval.
* AI Regression Test.

---

# 7. Đào sâu khái niệm đảm bảo chất lượng

Trong bộ tài liệu này, đảm bảo chất lượng không chỉ là test.

Đảm bảo chất lượng là:

> **Cơ chế liên kết yêu cầu, đặc tả, triển khai, review, test, bằng chứng, quyền hạn, phán đoán, học hỏi và đánh giá để việc dùng AI vẫn giải thích được chất lượng nghiệp vụ.**

---

## 7.1 Bốn trụ cột của đảm bảo chất lượng

Đảm bảo chất lượng trong SDD dễ hiểu nhất khi nhìn theo bốn trụ cột:

```text
1. Chất lượng
2. Năng suất
3. An toàn
4. Tính tái lập
```

Bên cạnh đó, do đặc thù thời đại AI, có thêm:

```text
5. Quản trị AI
6. Khả năng kiểm toán
7. Cải tiến liên tục
```

---

## 7.2 Đảm bảo chất lượng

Cơ chế đảm bảo chất lượng gồm:

### Chất lượng đặc tả

* Spec Pack.
* AC.
* Phạm vi không làm.
* Open Issues.
* Human Decision Required.
* Assumptions and Inference Log.

### Chất lượng thiết kế

* Impact Analysis.
* Impl Plan.
* FE/BE Contract Map.
* Service Dependency Map.
* DB / Migration Impact.
* Rollout / Rollback Plan.

### Chất lượng triển khai

* Source Intelligence.
* Project Knowledge.
* Known Good Example.
* Method allowlist / denylist.
* Review Checklist.
* Self Review.

### Chất lượng kiểm chứng

* Unit Test.
* Integration Test.
* Contract Test.
* E2E Test.
* Black-box Test.
* Regression Test.
* Migration dry-run.
* SAST / SCA / Secrets Scan.

### Chất lượng phán đoán

* Tool-Grounded Verification.
* Evidence Hierarchy.
* Veto Rule.
* Weighted Consensus.
* Human Governance.

Như vậy, chất lượng không chỉ là “test ở cuối”, mà được đảm bảo từng bước ở **trước đặc tả, trước triển khai, trước review, trước test, trước PR và trước release**.

---

## 7.3 Đảm bảo năng suất

Nhìn qua, SDD có nhiều artifact và có vẻ chậm. Nhưng mục tiêu không phải chỉ là giảm khối lượng công việc đơn giản, mà là **giảm làm lại, triển khai sai, bỏ sót review, điều tra lại và xử lý sự cố**.

Cơ chế tăng năng suất:

* Dùng Right-sizing để sửa nhỏ vẫn nhẹ.
* Giảm điều tra lặp lại bằng Source Intelligence.
* Tăng độ chính xác AI bằng Context Loading.
* Không phải giải thích lại cùng điều bằng Project Knowledge.
* Chuẩn hóa góc nhìn review bằng Review Checklist.
* Giảm chi phí AI và thời gian chờ bằng Token Optimization.
* Sắp xếp vấn đề trước human review bằng PR Gate.
* Không tái diễn cùng thất bại bằng Failure Mode.
* Chỉ giữ biện pháp có hiệu quả bằng Evaluation.

Điều quan trọng là SDD không phải “làm nặng mọi thứ”. Bộ tài liệu cũng nêu rằng không phải lần nào cũng làm hết, mà chọn tiêu chuẩn cần thiết tùy độ phức tạp và rủi ro của dự án.  
Căn cứ nội bộ: `10_BVN-SDD_GuideLine.md` L70-L72, `28_SDD_Applicability-and-RightSizing_Ver.04_Japanese.md` L69-L101

---

## 7.4 Đảm bảo an toàn

Trong phát triển AI, ngoài an toàn phát triển thông thường còn cần an toàn đặc thù của AI.

### An toàn phát triển thông thường

* Xác thực.
* Phân quyền.
* Input validation.
* Chống SQL injection.
* Chống XSS.
* Quản lý secret.
* Lỗ hổng thư viện phụ thuộc.
* CI/CD security.
* rollback.
* audit log.

### An toàn đặc thù AI

* Không để AI đọc `.env`.
* Không đưa log production hoặc dữ liệu khách hàng vào context.
* Cảnh giác prompt injection trong tài liệu bên ngoài.
* Không đưa hooks / MCP / plugin vào khi chưa thẩm định.
* Không cấp quá nhiều quyền write/delete/deploy/send cho AI.
* Không xem phán đoán của AI là bằng chứng.
* Không đưa PII vào cache hoặc RAG index.
* Chia quyền Agent theo vai trò.

File 45 nêu rằng AI không phải chủ thể quyền hạn mà là đối tượng kiểm soát; phán đoán AI là đối tượng kiểm chứng, hành động AI là đối tượng kiểm toán.  
Căn cứ nội bộ: `45_SDD_Full-Security-and-Agentic-AI-Governance-Option_Ver.04_Japanese.md` L126-L134

---

## 7.5 Đảm bảo tính tái lập

Tính tái lập nghĩa là:

> **Với cùng input, cùng đặc tả và cùng quy trình, ai làm cũng tiến gần đến cùng mức chất lượng.**

Các cơ chế đảm bảo tính tái lập trong SDD:

* Phase tiêu chuẩn.
* Thư mục tiêu chuẩn.
* Artifact tiêu chuẩn.
* Spec Pack.
* Impl Plan.
* Review Checklist.
* Test Plan.
* Test Results.
* Report.
* Artifact Status.
* Decision Record.
* Source Availability.
* Context Manifest.
* Token Budget Record.
* PR Review Record.

AI tạo đầu ra có tính xác suất và dao động. Vì vậy, phía quy trình phải bù lại tính tái lập.

---

## 7.6 Quản trị AI

Quản trị AI là:

> **Xem AI không phải người làm việc tự do, mà là trợ lý hoạt động dưới kiểm soát của quyền hạn, input, output, bằng chứng, kiểm chứng và phê duyệt của con người.**

Các yếu tố chính của quản trị AI:

| Đối tượng kiểm soát | Cơ chế trong SDD |
| ----- | ---------------------------------- |
| Input | 31 Context Loading |
| Output | 22 Prompt / schema / Review Record |
| Quyền hạn | 25 / 45 deny / ask / allow |
| Tool | 43 Tool-Grounded Verification |
| Agent | 42 Orchestrator / Agent Selector |
| RAG | 46 Evidence ID / source provenance |
| Cost | 44 Token Budget |
| Phán đoán | 43 Policy / Human Governance |
| Bằng chứng | 33 Artifact Governance |
| Cải tiến | 29 / 34 / 49 |

Các nguyên tắc quan trọng của quản trị AI:

```text
AI là trợ lý.
AI không phải bằng chứng.
AI không phải người phê duyệt.
Hành động của AI là đối tượng kiểm toán.
Con người chịu trách nhiệm cuối cùng.
```

Tư duy này cũng xuất hiện trong nguyên tắc vận hành của bộ tài liệu. File 10 nêu các nguyên tắc như: không xem ý kiến AI là bằng chứng, không gắn Security ở cuối, quản lý artifact như bản chính, con người chịu trách nhiệm.  
Căn cứ nội bộ: `10_BVN-SDD_GuideLine.md` L1950-L1961

---

## 7.7 Đáp ứng kiểm toán bằng bằng chứng

Khi kiểm toán, cần trả lời được:

* Vì sao thay đổi này được thực hiện.
* Dựa trên đặc tả nào.
* Đã đọc source nào.
* Source nào chưa đọc được.
* AI đã phán đoán dựa trên căn cứ nào.
* Đã chạy test nào.
* Test nào chưa chạy.
* Vì sao chấp nhận rủi ro.
* Ai đã phê duyệt.
* Ảnh hưởng production sẽ được giám sát thế nào.
* Thất bại được phản ánh cho lần sau ra sao.

SDD hỗ trợ điều này bằng:

* Source Availability.
* Spec Pack.
* Impact Analysis.
* Impl Plan.
* Review Checklist.
* Self Review.
* Independent Review.
* Tool Result Record.
* Test Results.
* Decision Record.
* Accepted Risk Record.
* Final Report.
* Audit Package.
* Failure Mode Entry.
* Evaluation Record.

Vì vậy, SDD không chỉ là “hỗ trợ phát triển bằng AI”, mà có thể nói là **kiểm soát phát triển để đảm bảo khả năng kiểm toán việc sử dụng AI**.

---

## 7.8 Hệ thống Gate đảm bảo chất lượng

Các Gate của SDD có thể được sắp xếp như sau.

| Gate | Mục đích | Kiểm tra chính |
| ------------------------ | ------------ | --------------------------------- |
| Safety Gate | Kiểm tra an toàn trước khi AI làm việc | Quyền hạn, secret, tài liệu bên ngoài, nơi làm việc |
| Source Availability Gate | Thông tin cần thiết đã đủ chưa | source, DB, API, test |
| Spec Gate | Đặc tả có triển khai được không | AC, điểm chưa xác định, ngoài phạm vi |
| Impact Gate | Đã thấy phạm vi ảnh hưởng chưa | FE, BE, DB, API, Batch, Ops |
| Review Gate | Góc nhìn có đủ không | Security, DB, Operation, Test |
| Test Gate | Đã kiểm chứng được chưa | test plan, result, skip reason |
| Security Gate | Có vấn đề bảo mật không | SAST, secret, auth, PII |
| PR Gate | Có thể merge không | policy, tool, human, AI finding |
| Release Gate | Có thể đưa production không | rollback, monitoring, risk |
| Learning Gate | Học hỏi đã quay lại lần sau chưa | Failure Mode, Knowledge, Evaluation |

---

## 7.9 Cân bằng chất lượng, năng suất, an toàn và tính tái lập

Điều quan trọng trong SDD không phải là tối đa hóa mọi thứ. Điều quan trọng là cân bằng theo từng dự án.

| Dự án | Chất lượng | Năng suất | An toàn | Tính tái lập | Khuyến nghị |
| ------------ | --: | --: | --: | --: | ------------- |
| Sửa text | thấp–trung | cao | thấp | trung | Light |
| Thêm một API | trung | trung | trung | trung | Standard |
| Thay đổi hợp đồng FE/BE | cao | trung | trung–cao | cao | Standard Plus |
| DB migration | cao | thấp–trung | cao | cao | Heavy |
| Thay đổi phân quyền | rất cao | trung | rất cao | rất cao | Critical |
| Đưa AI PR Gate vào | cao | trung–cao | cao | cao | Advanced |
| Refactor lớn | cao | trung | cao | cao | 48 |

---

# 8. Lộ trình khuyến nghị khi áp dụng SDD

## 8.1 Day 1

Mục tiêu: Tạo nền tảng.

Nội dung cần đọc:

```text
10
11
21
22
28
```

Việc cần làm:

* Giải thích mục tiêu của SDD.
* Chia sẻ Light / Standard / Heavy / Critical.
* Tạo chính sách tối thiểu cho `.claude/CLAUDE.md`.
* Quyết định deny / ask / allow trong `settings.json`.
* Tạo template Spec Pack.
* Chọn một dự án.

Việc không nên làm:

* Đưa Multi-Agent ngay từ đầu.
* Cấp quyền MCP write ngay từ đầu.
* Đưa RAG ngay từ đầu.
* Tự động block PR ngay từ đầu.
* Đưa toàn bộ yếu tố kiểu ECC vào một lần.

---

## 8.2 Week 1

Mục tiêu: Chạy Core trên một dự án.

Thứ cần bổ sung:

```text
23
24
31
33
```

Việc cần làm:

* Viết Source Availability.
* Viết Spec Pack.
* Viết Impact Analysis.
* Viết Impl Plan.
* Viết Review Checklist.
* Viết Test Plan.
* Viết Test Results và Report.
* Đăng ký một ứng viên Failure Mode.

---

## 8.3 Month 1

Mục tiêu: Chuẩn hóa vận hành.

Ứng viên bổ sung:

```text
25
26
29
34
43
```

Việc cần làm:

* Chuẩn hóa Security Gate.
* Áp dụng FE/BE Contract cho dự án cần thiết.
* Bắt đầu vận hành Failure Mode Index.
* Tạo Project Knowledge.
* Đưa Tool-Grounded Verification vào một phần.
* Bắt đầu đo valid finding rate và rework.

---

## 8.4 Mature

Mục tiêu: Nâng cao.

Ứng viên bổ sung:

```text
40
41
42
44
45
46
47
48
49
```

Việc cần làm:

* Chỉ dùng Multi-Agent cho PR rủi ro cao.
* Quản lý Token Budget.
* RAG / Code Map.
* AI QA Gate.
* Full Security Governance.
* Parallel Worktree.
* Evaluation Dashboard.
* Golden PR Dataset.

---

# 9. Mẫu thực tế để kết nối từ vibe coding sang SDD

Cuối cùng, phần này sắp xếp điểm quan trọng được yêu cầu bổ sung lần này: “liên kết từ yêu cầu/yêu cầu nghiệp vụ sử dụng vibe coding” thành một template thực tế.

---

## 9.1 Thứ tạo bằng vibe coding

```text
Mục đích:
  Kiểm chứng market fit, phản ứng khách hàng, giá trị nghiệp vụ

Artifact:
  MVP
  Prototype
  Demo
  Clickable UI
  Mock API
  Temporary DB
  User feedback
  Usage metrics
  Sales feedback
```

Ở giai đoạn này, tốc độ học hỏi quan trọng hơn đảm bảo chất lượng.

---

## 9.2 Thứ cần bỏ trước khi chuyển sang SDD

Từ thành quả vibe coding, không nên đưa thẳng những thứ sau vào production.

```text
- Code triển khai tạm
- Thiết kế DB tạm
- Giá trị hard-code
- Quyền hạn tạm
- API tạm
- Xử lý lỗi tạm
- Logic không có test
- Code do AI tạo nhưng không ai hiểu
```

---

## 9.3 Thứ nên chuyển sang SDD

```text
- Giá trị nghiệp vụ đã được kiểm chứng
- Chức năng người dùng cần
- UX đã được chấp nhận
- Chức năng đã biết là không cần
- Luồng nghiệp vụ được sử dụng thực tế
- Điều kiện khách hàng đã đồng thuận
- Giả thuyết đã thất bại
- Yêu cầu phi chức năng cần cho production
```

---

## 9.4 Spec Pack tạo ở phía SDD

```md
# Spec Pack

## Background
Trong kiểm chứng MVP bằng vibe coding, sales phản ứng rất tốt với chức năng cho phép xem danh sách lịch sử báo giá theo từng khách hàng.

## Goal
Cung cấp chức năng chính thức để tìm kiếm và xem lịch sử báo giá theo đơn vị khách hàng.

## In Scope
- Danh sách lịch sử báo giá theo khách hàng
- Lọc theo trạng thái
- Điều hướng đến chi tiết báo giá
- Kiểm soát xem theo quyền hạn

## Out of Scope
- Chức năng tạo báo giá
- Xuất PDF
- Chỉnh sửa hàng loạt

## Acceptance Criteria
1. Sales chỉ xem được lịch sử báo giá của khách hàng mình phụ trách
2. Admin xem được lịch sử báo giá của mọi khách hàng
3. Báo giá của khách hàng ngoài quyền hạn không được trả về ngay cả ở API
4. Có thể lọc theo trạng thái báo giá
5. Thao tác được ghi vào audit log

## Open Issues
- Thời hạn lưu báo giá quá khứ
- Hiển thị lịch sử khi hợp nhất khách hàng
- Hỗ trợ xuất PDF trong tương lai
```

---

# 10. Đánh giá tổng hợp

Bộ tài liệu nhập môn này là một hệ thống có độ hoàn thiện rất cao để nâng phát triển có AI từ “sử dụng công cụ tiện ích cá nhân” thành “năng lực phát triển của tổ chức”.

Những điểm đặc biệt tốt:

1. **Không quá tin AI**.
2. **Tạo đặc tả trước**.
3. **Tách ý kiến AI và bằng chứng**.
4. **Ngăn áp dụng quá mức bằng Right-sizing**.
5. **Giảm việc AI đọc sót bằng Source Intelligence**.
6. **Quản lý chất lượng thông tin bằng Context Loading**.
7. **Kiểm soát quyền AI bằng Security Gate**.
8. **Đảm bảo khả năng kiểm toán bằng Artifact Governance**.
9. **Cải tiến liên tục bằng Failure Mode**.
10. **Cân bằng chi phí và độ chính xác bằng Token Optimization**.
11. **Không dùng Multi-Agent hỗn loạn, mà kiểm soát bằng Orchestrator**.
12. **Không xem RAG là phép màu, mà xử lý bằng Code Map và Evidence ID**.
13. **Nối AI review với human decision bằng PR Gate**.
14. **Đo hiệu quả áp dụng bằng Evaluation**.

Điểm cần chú ý lớn nhất:

1. **Không đưa tất cả vào ngay từ đầu**.
2. **Không hài lòng chỉ vì đã tạo artifact**.
3. **Không xem AI review là bằng chứng**.
4. **Không mở rộng quá mức quyền MCP / hooks / Agent**.
5. **Không bỏ mặc Source Map hoặc Knowledge cũ**.
6. **Không cắt mất thông tin quan trọng khi giảm token**.
7. **Không nói về hiệu quả nếu không đo metric**.
8. **Không chuyển trách nhiệm cuối cùng của con người sang AI**.

---

# 11. Tổng kết cuối cùng

SDD Introduction Pack V04.2 này dùng để đưa phát triển có AI sang giai đoạn tiếp theo.

Sử dụng AI đơn giản giúp tăng hiệu suất công việc cá nhân.  
Vibe coding tăng tốc khám phá market fit và giá trị khách hàng.  
SDD chuyển các yêu cầu có giá trị thu được từ đó thành phát triển production có chất lượng nghiệp vụ, an toàn, tính tái lập và khả năng kiểm toán.

Vị trí cuối cùng là:

```text
Sử dụng AI đơn giản:
  Hỗ trợ công việc cá nhân

Vibe coding:
  Market fit, khám phá yêu cầu, kiểm chứng MVP

SDD:
  Đặc tả hóa, thiết kế, triển khai, review, test, kiểm toán, cải tiến liên tục

Advanced SDD:
  Quy mô lớn, rủi ro cao, Multi-Agent, RAG, PR Gate, quản trị AI
```

Bản chất của pack này không phải là để “cho AI tự do tạo”.

> **Mà là để AI làm việc mạnh mẽ hơn bằng cách giúp AI không lạc hướng, không vượt quyền, không nhầm suy đoán với bằng chứng, đồng thời để lại artifact và bằng chứng ở dạng con người có thể phán đoán.**

Vì vậy, thứ tự áp dụng đúng là:

```text
Đầu tiên:
  10 + 11 + 21 + 22 + 28

Sớm trong dự án thực tế:
  23 + 24 + 31 + 33

Tăng cường an toàn:
  25 + 43 + 45

Mở rộng tổ chức / nâng cao:
  40 + 41 + 42 + 44 + 46 + 47 + 48 + 49

Cải tiến liên tục:
  29 + 34 + 49
```

Nếu sử dụng đúng bộ tài liệu này, phát triển AI sẽ không còn chỉ là “coding nhanh”.

* Đặc tả được lưu lại.
* Căn cứ được lưu lại.
* Phạm vi ảnh hưởng được lưu lại.
* Góc nhìn review được lưu lại.
* Kết quả test được lưu lại.
* Lý do phán đoán được lưu lại.
* Thất bại được dùng cho lần sau.
* Security boundary được bảo vệ.
* Chi phí và chất lượng được đo.
* Tổ chức có thể tái lập.

Nói cách khác, SDD pack này là:

> **Framework tổng hợp về đặc tả, chất lượng, an toàn, bằng chứng và quản trị AI để bắc cầu phát triển hệ thống nghiệp vụ thời AI từ khám phá sang chất lượng production.**

[1]: https://www.merriam-webster.com/slang/vibe-coding?utm_source=chatgpt.com "VIBE CODING Slang Meaning | Merriam-Webster"
[2]: https://leanstartup.co/resources/articles/what-is-an-mvp/?utm_source=chatgpt.com "What Is an MVP? Eric Ries Explains - Lean Startup Co."
[3]: https://code.claude.com/docs/en/mcp "Connect Claude Code to tools via MCP - Claude Code Docs"
[4]: https://code.claude.com/docs/en/hooks "Hooks reference - Claude Code Docs"
[5]: https://code.claude.com/docs/en/costs "Manage costs effectively - Claude Code Docs"
[6]: https://platform.claude.com/docs/en/build-with-claude/prompt-caching "Prompt caching - Claude API Docs"
[7]: https://code.claude.com/docs/en/claude-directory "Explore the .claude directory - Claude Code Docs"
[8]: https://code.claude.com/docs/en/permissions "Configure permissions - Claude Code Docs"
[9]: https://github.com/affaan-m/everything-claude-code "GitHub - affaan-m/everything-claude-code: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. · GitHub"
