# Walkthrough: Xây dựng WeatherNow (iOS) từ đầu với BVN-SDD

**Kịch bản**: Bạn đang xây dựng một ứng dụng thời tiết iOS tên *WeatherNow* hoàn toàn mới — chưa có codebase nào.  
Walkthrough này trình bày mọi lệnh BVN-SDD, nội dung artifact quan trọng mà mỗi lệnh tạo ra,  
và quyết định bạn cần đưa ra ở mỗi bước.

> Đây là **ví dụ tài liệu** — minh hoạ các artifact trông như thế nào, không phải code Swift thật để chạy.

**Tổng quan ứng dụng**

| | |
|---|---|
| Nền tảng | iOS 17+, Swift 5.9, SwiftUI |
| Kiến trúc | MVVM + Clean Architecture |
| Ticket trong walkthrough | **T-001** — Màn hình thời tiết hiện tại (dựa trên vị trí) |
| API bên ngoài | OpenWeatherMap REST API |
| Quản lý thư viện | Swift Package Manager |

---

## 0. Cài đặt

```bash
bvn-sdd check
# ✓ git 2.44.0
# ✓ claude (Claude Code)

git clone git@github.com:my-org/weathernow-ios.git
cd weathernow-ios

bvn-sdd init --here --lang vi
# ✓ .claude/ đã tạo
# ✓ .bvn-sdd/ đã tạo
# ✓ docs/ đã tạo
```

Mở dự án trong **Claude Code**, rồi chạy ngay:

```
/sdd-phase0a
```

---

## Phase 0-A — Safety Gate

> **Cơ chế**: `/sdd-phase0a` load instruction từ `.claude/commands/sdd-phase0a.md`. Lệnh đó chỉ biết "hãy audit môi trường an toàn". **Bạn mô tả ứng dụng trong cùng tin nhắn** để AI ghi vào artifact và dùng cho các phase sau.

**Tin nhắn bạn gõ trong Claude Code**:

```
/sdd-phase0a

Dự án: WeatherNow — ứng dụng xem thời tiết iOS mới hoàn toàn, chưa có code.
Nền tảng: iOS 17+, SwiftUI, MVVM + Clean Architecture, Swift Package Manager.
API bên ngoài: OpenWeatherMap (REST, xác thực bằng API key).
Offline: cache dữ liệu cuối, hiện banner "Cập nhật lần cuối X phút trước".
```

**AI làm gì**: Quét repo — không tìm thấy file source — ghi nhận `project_type = new`. Ghi thông tin bạn cung cấp vào artifact.

**Tạo ra**: `docs/maintenance/phase0/phase0-plan.md`

```markdown
# Phase 0-A Safety Gate — WeatherNow iOS

## Loại dự án
new (greenfield) — không phát hiện file source

## Tech Stack (từ mô tả của người dùng)
- iOS 17+, Swift 5.9, SwiftUI
- MVVM + Clean Architecture
- Swift Package Manager
- API bên ngoài: OpenWeatherMap REST

## Ràng buộc an toàn đã ghi nhận
- DENY: đọc hoặc in .env, API key, token, PII
- DENY: push lên remote khi chưa có người phê duyệt
- DENY: thao tác git phá huỷ (reset --hard, force-push) mà không xác nhận
- ASK: trước khi xoá bất kỳ file nào
- ASK: trước khi viết code gọi API bên ngoài (xác nhận cách xử lý key)

## Chính sách context
- Ưu tiên nguồn đúng: spec-pack.md > tài liệu kiến trúc > suy luận AI
- Tóm tắt file > 500 dòng thay vì load toàn bộ

## Câu hỏi mở cho /sdd-map
1. Cấu trúc module mong muốn (Features/, Data/, Core/ hay khác)?
2. Yêu cầu offline cụ thể: cache bao lâu thì coi là stale?
3. Có tài liệu thiết kế UI (Figma, mockup) không?
```

**Bạn**: Đọc `phase0-plan.md`. Trả lời câu hỏi mở còn lại.

**Câu trả lời của bạn**:
> Cấu trúc Features/Data/Core là ổn. Cache stale sau 30 phút. Chưa có Figma. Tiếp tục.

---

## Phase 0-B — Source Intelligence (Chế độ Green-field)

**Lệnh**: `/sdd-map`

**AI làm gì**: Đọc `phase0-plan.md` (có tech stack từ Phase 0-A) → phát hiện `project_type = new` → chạy **chế độ green-field**. Tài liệu kiến trúc được tạo dựa trên thông tin bạn đã cung cấp ở Phase 0-A — không phải AI tự đoán. Không có source để quét — tạo tài liệu *quyết định* kiến trúc. Mọi mục đều đánh dấu `[PLANNED]`.

**Tạo ra**: `docs/architecture/system-map.md`

```markdown
# System Map — WeatherNow iOS
## Trạng thái: GREEN-FIELD — tất cả mục [PLANNED]

## Tổng quan các tầng
| Tầng | Công nghệ | Trạng thái |
|---|---|---|
| Presentation | SwiftUI Views | [PLANNED] |
| State / ViewModel | @Observable (iOS 17) | [PLANNED] |
| Domain (Use Cases) | Pure Swift structs | [PLANNED] |
| Data (Repository) | Protocol + URLSession impl | [PLANNED] |
| Location | CoreLocation async wrapper | [PLANNED] |
| Cache | UserDefaults (JSON đơn giản) | [PLANNED] |

## Cấu trúc module [PLANNED]
WeatherNow/
├── App/
│   └── WeatherNowApp.swift          # Entry point, root dependency injection
├── Features/
│   └── CurrentWeather/
│       ├── View/                    # SwiftUI Views
│       ├── ViewModel/               # @Observable ViewModels
│       └── Model/                   # Domain models (WeatherData, v.v.)
├── Data/
│   ├── Repository/                  # WeatherRepository protocol + implementation
│   ├── Network/                     # URLSession wrapper + Codable DTOs
│   └── Location/                    # CLLocationManager async/await wrapper
└── Core/
    └── Config/                      # AppConfig — đọc key từ Info.plist

## API Contract dự kiến
- WeatherRepository.fetchCurrentWeather(lat:lon:) async throws -> WeatherData
- LocationService.requestCurrentLocation() async throws -> CLLocationCoordinate2D

## API bên ngoài [PLANNED]
- OpenWeatherMap: GET /data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric
- Xác thực: API key trong query param (lưu trong Info.plist, KHÔNG hardcode trong source)
```

**Tạo thêm**: `docs/architecture/api-contracts.md` *(tất cả `[PLANNED]`)*  
**Tạo thêm**: `docs/architecture/db-schema.md` *(đánh dấu schema cache UserDefaults là `[PLANNED]`)*

**Bạn**: Xem lại cấu trúc module. Điều chỉnh nếu cần. Tài liệu này là bản thiết kế kiến trúc cho mọi ticket.

**Xác nhận của bạn**: Duyệt. Tiến hành ticket đầu tiên.

---

## T-001: Màn hình Thời tiết Hiện tại

### Bootstrap

**Lệnh bạn gõ** (có thể kèm tên ngắn):

```
/sdd-new T-001 Màn hình thời tiết hiện tại
```

```
✓ docs/changes/T-001/ đã tạo
✓ 20 file artifact trống đã sẵn sàng:
    spec-pack.md, source-availability.md, open-issues.md
    mode-decision.md, context.md, source-map.md, ticket-rules.md
    impact-analysis.md, impl-plan.md, review-checklist.md
    self-review.md, human-review.md, test-plan.md, test-results.md
    blackbox-testcases.md, test-data.md, blackbox-review-checklist.md
    report.md, promotion-candidates.md, strategic-compact.md
```

---

### Phase 1 — Spec Pack

> **Làm thế nào AI biết yêu cầu của T-001?**  
> `/sdd-spec` chỉ chứa instruction chung — "hãy viết spec-pack từ yêu cầu đầu vào". Yêu cầu cụ thể của ticket phải do **bạn viết ngay bên dưới lệnh** trong cùng một tin nhắn. AI kết hợp yêu cầu đó với `docs/architecture/system-map.md` (từ Phase 0-B) để tạo ra spec đầy đủ.

**Tin nhắn bạn gõ trong Claude Code** (lệnh + yêu cầu viết liền):

```
/sdd-spec T-001

Yêu cầu T-001 — Màn hình thời tiết hiện tại:

Mục tiêu: mở app → thấy thời tiết tại vị trí GPS hiện tại ngay lập tức.

Hiển thị: tên thành phố, nhiệt độ (°C), mô tả ngắn (VD: "Partly cloudy"), icon thời tiết.

Luồng quyền vị trí:
- Lần đầu mở app → xin quyền vị trí
- Người dùng từ chối → hiện "Cần quyền truy cập vị trí" + nút "Mở Cài đặt"
- Được cấp quyền → tự động tải thời tiết

Trạng thái tải:
- Đang gọi API → hiện loading indicator
- Mất mạng + có cache → hiện dữ liệu cũ + banner "Cập nhật lần cuối X phút trước"
- Mất mạng + không có cache → empty state "Không có kết nối" + nút Thử lại

Tương tác: pull-to-refresh để tải lại thủ công.

Ngoài phạm vi T-001: dự báo theo giờ/ngày, nhiều địa điểm, màn hình cài đặt, push notification.

Câu hỏi chưa quyết: cách lưu API key (Info.plist hay Keychain?) — ghi vào open-issues.
```

**AI đọc gì trước khi viết** `spec-pack.md`:
1. `.claude/CLAUDE.md`, `.claude/rules/*` — quy tắc dự án
2. `docs/architecture/system-map.md` — kiến trúc iOS/SwiftUI/MVVM đã quyết ở Phase 0-B
3. **Yêu cầu bạn vừa viết ở trên** — nguồn chính cho acceptance criteria và open issues

**Tạo ra**: `docs/changes/T-001/spec-pack.md`

```markdown
# Spec Pack — T-001: Màn hình Thời tiết Hiện tại

## Tóm tắt
Hiển thị điều kiện thời tiết hiện tại dựa trên vị trí GPS của người dùng.

## Acceptance Criteria
1. App yêu cầu quyền vị trí khi lần đầu khởi động.
2. Nếu bị từ chối → hiện thông báo "Cần quyền truy cập vị trí" + nút "Mở Cài đặt".
3. Khi được cấp quyền → lấy dữ liệu thời tiết từ OpenWeatherMap.
4. Hiển thị: tên thành phố, nhiệt độ (°C), mô tả thời tiết, icon thời tiết.
5. Hiện loading indicator trong khi đang tải.
6. Hiện trạng thái lỗi khi mất mạng, kèm nút "Thử lại".
7. Hỗ trợ pull-to-refresh.
8. Nếu có cache và mạng lỗi → hiện dữ liệu cũ kèm banner "Cập nhật lần cuối X phút trước".

## Ngoài phạm vi (T-001)
- Dự báo theo giờ / theo ngày
- Nhiều vị trí đã lưu
- Màn hình Cài đặt (đơn vị, giao diện)
- Thông báo đẩy

## Nguồn dữ liệu
- OpenWeatherMap API: có tài liệu tại openweathermap.org/api — cần API key
- CoreLocation: Apple SDK, luôn sẵn có
- Không có Swift code có sẵn để tái sử dụng
```

**Tạo ra**: `docs/changes/T-001/open-issues.md`

```markdown
# Open Issues — T-001

OI-001: Chiến lược lưu API key
  Lựa chọn: (a) Info.plist — đơn giản nhưng key có thể đọc được từ binary
             (b) Keychain — bảo mật hơn nhưng phức tạp hơn cho ticket đầu
  → Cần quyết định trước Phase 4.

OI-002: Ngưỡng độ chính xác vị trí
  Nếu CLLocation.horizontalAccuracy > 5000m thì xử lý thế nào?
  → Hiện cảnh báo? Chấp nhận im lặng?

OI-003: Offline mode — trạng thái trống hay dữ liệu cache?
  Nếu không có mạng VÀ không có cache → người dùng thấy gì?
```

**Bạn**: Trả lời open issues trước khi chạy `/sdd-rightsize`.

**Câu trả lời của bạn** (ghi vào `open-issues.md` hoặc trả lời trong chat):
- OI-001 → Info.plist tạm thời. Ghi nhận là tech debt AR-001. Chuyển sang proxy trước App Store.
- OI-002 → Chấp nhận mọi độ chính xác. Hiện nhãn "Vị trí gần đúng" nếu > 2 km.
- OI-003 → Hiện trạng thái trống "Không có kết nối — kiểm tra mạng" kèm nút Thử lại.

---

### Phase 1 — Right-sizing

**Lệnh**: `/sdd-rightsize T-001`

**Tạo ra**: `docs/changes/T-001/mode-decision.md`

```markdown
# Mode Decision — T-001

## Đánh giá
- Dự án mới: không có pattern nào để tái sử dụng, tất cả tầng đều tạo mới.
- Tầng liên quan: UI (SwiftUI), ViewModel (@Observable), Repository (protocol),
  Network (URLSession), Location (CoreLocation), Cache (UserDefaults).
- Số file mới ước tính: 12–14.
- Độ phức tạp: trung bình-cao — chuỗi async/await, state machine lỗi, luồng cấp quyền.

## Quyết định: Mode M3 (Plus)

Lý do: Nhiều tầng kiến trúc được thiết lập đồng thời.
"Contract front-end / back-end" (View ↔ ViewModel ↔ Repository) phải được
định nghĩa rõ trong Phase 2–3 trước khi viết bất kỳ dòng code nào.
Bỏ qua Phase 2–3 sẽ khiến thứ tự implement không xác định trên dự án greenfield.

## Workflow điều chỉnh
Áp dụng tất cả phases (không bỏ qua).
Phase 3 phải tạo ra danh sách file đầy đủ trước khi Phase 4 bắt đầu.
```

**Bạn**: Xác nhận M3. Không có phản đối → tiếp tục.

---

### Phase 2 — Ticket Context & Rules

**Lệnh**: `/sdd-context T-001`

**Tạo ra**: `docs/changes/T-001/context.md`

```markdown
# Context — T-001

## Quyết định kiến trúc đang áp dụng (từ system-map.md)
- Dùng @Observable (iOS 17 Observation framework). KHÔNG dùng ObservableObject/Published.
- Repository pattern: protocol-first để ViewModel có thể test với mock.
- Network: plain URLSession + async/await. Không dùng thư viện networking bên ngoài.
- Xử lý lỗi: typed enum (WeatherError, LocationError), không dùng Error string chung chung.

## Pattern Dependency Injection
- ViewModel khởi tạo với dependencies được truyền qua init (không dùng singleton).
- Root injection trong WeatherNowApp.swift.

## Quy tắc Async / Threading
- Tất cả mutation state @MainActor trong ViewModel.
- KHÔNG BAO GIỜ dùng DispatchQueue.main.async trong code mới — dùng @MainActor.
- LocationService trả về qua async/await continuation.
```

**Tạo ra**: `docs/changes/T-001/ticket-rules.md`

```markdown
# Ticket Rules — T-001

## Pattern bị cấm
- KHÔNG BAO GIỜ gọi URLSession trực tiếp từ SwiftUI View.
- KHÔNG BAO GIỜ hardcode API key hoặc base URL trong source file.
- KHÔNG BAO GIỜ dùng force-unwrap (!) trên Optional từ network response.

## Pattern bắt buộc
- Mọi hàm async trong ViewModel phải set state = .loading trước await.
- Tất cả trường hợp lỗi phải được bắt và lưu vào ViewState, không crash hay bỏ qua.
- Ghi cache sau khi nhận response thành công từ mạng, không phải khi app khởi động.
```

**Tạo ra**: `docs/changes/T-001/source-map.md`

```markdown
# Source Map — T-001 [TẤT CẢ CẦN TẠO MỚI — greenfield]

| File | Mục đích |
|---|---|
| WeatherNow/Core/Config/AppConfig.swift | Đọc WEATHER_API_KEY từ Info.plist |
| WeatherNow/Features/CurrentWeather/Model/WeatherData.swift | Domain model |
| WeatherNow/Data/Network/WeatherDTO.swift | Codable DTO response OpenWeatherMap |
| WeatherNow/Data/Network/WeatherAPIClient.swift | URLSession wrapper + ánh xạ lỗi |
| WeatherNow/Data/Repository/WeatherRepository.swift | Định nghĩa protocol |
| WeatherNow/Data/Repository/WeatherRepositoryImpl.swift | Impl: APIClient + cache UserDefaults |
| WeatherNow/Data/Location/LocationService.swift | CoreLocation async/await wrapper |
| WeatherNow/Features/CurrentWeather/ViewModel/CurrentWeatherViewModel.swift | @Observable ViewModel |
| WeatherNow/Features/CurrentWeather/View/WeatherIconView.swift | Component icon |
| WeatherNow/Features/CurrentWeather/View/CurrentWeatherView.swift | Màn hình chính SwiftUI |
| WeatherNow/App/WeatherNowApp.swift | Entry point + root DI |
| WeatherNowTests/CurrentWeatherViewModelTests.swift | Unit test ViewModel |
| WeatherNowTests/WeatherAPIClientTests.swift | Unit test tầng Network |
```

---

### Phase 3 — Impact Analysis & Kế hoạch Implement

**Lệnh**: `/sdd-plan T-001`

**Tạo ra**: `docs/changes/T-001/impl-plan.md`

```markdown
# Implementation Plan — T-001

## Thứ tự implement (an toàn về dependency)
1. AppConfig.swift               — không có dependency
2. WeatherData.swift             — domain model, không có dependency
3. WeatherDTO.swift              — Codable DTOs, không có dependency
4. WeatherRepository.swift       — chỉ là protocol, chưa có impl
5. LocationService.swift         — CoreLocation wrapper, độc lập
6. WeatherAPIClient.swift        — dùng AppConfig + WeatherDTO
7. WeatherRepositoryImpl.swift   — dùng APIClient + UserDefaults
8. CurrentWeatherViewModel.swift — dùng Repository + LocationService
9. WeatherIconView.swift         — UI component thuần, không có dependency
10. CurrentWeatherView.swift      — dùng ViewModel
11. WeatherNowApp.swift           — kết nối tất cả
12. Tests                         — sau khi implement xong

## Rủi ro chính
- RISK-01: Lưu key trong Info.plist — key có thể đọc được từ binary đã compile.
  Chấp nhận cho giai đoạn dev. Phải giải quyết trước App Store (AR-001).
- RISK-02: NSLocationWhenInUseUsageDescription phải được đặt trong Info.plist
  qua Xcode (AI không thể sửa trực tiếp project file Xcode — bước thủ công của người).
- RISK-03: Không có retry khi network timeout — chấp nhận trong phạm vi M3,
  thêm vào ticket follow-up.
```

**Bạn**: Xem lại kế hoạch. Duyệt danh sách file và thứ tự trước khi AI viết bất kỳ code nào.

**Xác nhận của bạn**:
> Duyệt. Tôi sẽ thêm `NSLocationWhenInUseUsageDescription` vào Info.plist thủ công trong Xcode.

---

### Phase 4+5 — Implement & Review

**Lệnh**: `/sdd-implement T-001`

AI tạo file theo thứ tự trong `impl-plan.md`. Các đoạn code chính:

---

**`WeatherRepository.swift`** — Định nghĩa Protocol:
```swift
// WeatherNow/Data/Repository/WeatherRepository.swift
protocol WeatherRepository {
    func fetchCurrentWeather(lat: Double, lon: Double) async throws -> WeatherData
    func cachedWeather() -> CachedWeather?
}
```

---

**`CurrentWeatherViewModel.swift`** — State machine cốt lõi:
```swift
// WeatherNow/Features/CurrentWeather/ViewModel/CurrentWeatherViewModel.swift
@Observable
final class CurrentWeatherViewModel {

    enum ViewState {
        case idle
        case loading
        case loaded(WeatherData)
        case locationPermissionDenied
        case error(String)
    }

    private(set) var state: ViewState = .idle
    private let repository: WeatherRepository
    private let locationService: LocationService

    init(repository: WeatherRepository, locationService: LocationService) {
        self.repository = repository
        self.locationService = locationService
    }

    @MainActor
    func loadWeather() async {
        state = .loading
        do {
            let location = try await locationService.requestCurrentLocation()
            let weather = try await repository.fetchCurrentWeather(
                lat: location.latitude,
                lon: location.longitude
            )
            state = .loaded(weather)
        } catch LocationError.permissionDenied {
            state = .locationPermissionDenied
        } catch {
            if let cached = repository.cachedWeather() {
                state = .loaded(cached.weather)   // hiện dữ liệu cũ kèm banner
            } else {
                state = .error(error.localizedDescription)
            }
        }
    }
}
```

---

**Tạo ra**: `docs/changes/T-001/self-review.md`

```markdown
# AI Self-Review — T-001

## Checklist
- [x] Không hardcode API key trong source file (AppConfig đọc từ Info.plist)
- [x] Dùng @MainActor cho mọi mutation state — không có DispatchQueue.main
- [x] Repository protocol-first — ViewModel có thể test với mock
- [x] Xử lý tất cả trạng thái lỗi: vị trí bị từ chối, lỗi mạng, lỗi decode
- [x] State loading được set trước mọi await
- [x] Hiện cache khi mạng lỗi (OI-003 đã giải quyết)
- [ ] CẢNH BÁO: Lưu key trong Info.plist — chấp nhận là tech debt AR-001
- [ ] CẢNH BÁO: NSLocationWhenInUseUsageDescription — phải đặt thủ công trong Xcode

## Mục yêu cầu người xem lại
1. Đặt NSLocationWhenInUseUsageDescription trong Info.plist (Xcode project file).
2. Thêm giá trị WEATHER_API_KEY vào Info.plist trước khi chạy.
3. Xác nhận banner "Cập nhật lần cuối" hiển thị đúng khi hiện dữ liệu cache.
```

**Bạn**: Đọc tất cả file Swift đã tạo. Sau đó điền `human-review.md`.

**`docs/changes/T-001/human-review.md`** (bạn viết):
```markdown
# Human Review — T-001

Người review: @hv_ngan
Ngày: 2026-06-01

## Kết quả: DUYỆT có lưu ý

## Phát hiện
1. Logic ViewModel rõ ràng. Chuỗi async/await chính xác và dễ đọc.
2. Error enum bao phủ tất cả kịch bản lỗi dự kiến.
3. Hành vi cache-khi-lỗi đúng với quyết định OI-003. ✓
4. Đã thêm NSLocationWhenInUseUsageDescription trong Xcode. ✓
5. Đã thêm WEATHER_API_KEY vào Info.plist. ✓

## Rủi ro chấp nhận
- AR-001: API key trong Info.plist — sẽ chuyển sang server-side proxy trước App Store.
```

---

### Phase 6 — Test Plan & Kết quả

**Lệnh**: `/sdd-test T-001`

**Tạo ra**: `docs/changes/T-001/test-plan.md` (trích đoạn)

```markdown
# Test Plan — T-001

## Unit Tests: CurrentWeatherViewModel
| Test | Kịch bản | Kết quả mong đợi |
|---|---|---|
| test_loadWeather_success | Được cấp vị trí, API trả về dữ liệu hợp lệ | state == .loaded(weather) |
| test_loadWeather_locationDenied | LocationService ném .permissionDenied | state == .locationPermissionDenied |
| test_loadWeather_networkError_withCache | URLError ném, có cache | state == .loaded(cachedWeather) |
| test_loadWeather_networkError_noCache | URLError ném, không có cache | state == .error("...") |
| test_loadWeather_setsLoadingFirst | Trong lúc await | state == .loading ngay từ đầu |

## Unit Tests: WeatherAPIClient
| Test | Kịch bản | Kết quả mong đợi |
|---|---|---|
| test_fetch_parsesValidJSON | Fixture JSON hợp lệ | Trả về WeatherData đúng |
| test_fetch_throws_on404 | HTTP 404 response | Ném WeatherError.notFound |
| test_fetch_throws_onDecodeError | JSON sai định dạng | Ném WeatherError.decodingFailed |
```

**Tạo ra**: `docs/changes/T-001/test-results.md`

```markdown
# Test Results — T-001

Ngày chạy: 2026-06-01
Tất cả 8 test PASSED ✓

Coverage:
  CurrentWeatherViewModel:  94%
  WeatherAPIClient:         88%
  LocationService:          71% (luồng cấp quyền khó unit-test — đã kiểm tra trong black-box)
```

**Bạn**: Chạy test trong Xcode (`Cmd + U`). Xác nhận pass trước khi tiếp tục.

---

### Phase 7 — Black-box Tests

**Lệnh**: `/sdd-blackbox T-001`

**Tạo ra**: `docs/changes/T-001/blackbox-testcases.md`

```markdown
# Black-box Test Cases — T-001

## TC-001: Lần đầu khởi động — Hộp thoại cấp quyền
Điều kiện: Cài mới (chưa có quyền trước đó).
Bước: Khởi động app.
Mong đợi: Hộp thoại cấp quyền vị trí iOS xuất hiện kèm chuỗi mô tả.
Pass/Fail: [ ]

## TC-002: Từ chối quyền vị trí
Điều kiện: Từ chối trong hộp thoại hoặc trong Cài đặt.
Bước: Mở app.
Mong đợi: Hiện thông báo "Cần quyền truy cập vị trí".
         Nút "Mở Cài đặt" dẫn đến iOS Settings → WeatherNow.
Pass/Fail: [ ]

## TC-003: Tải thời tiết thành công
Điều kiện: Đã cấp quyền vị trí, có kết nối mạng.
Bước: Khởi động app.
Mong đợi: Tên thành phố, nhiệt độ (°C), mô tả, icon đều hiển thị.
         Không có spinner. Không có thông báo lỗi.
Pass/Fail: [ ]

## TC-004: Offline — Không có cache
Điều kiện: Bật Chế độ Máy bay. Cài app mới (không có cache).
Bước: Khởi động app.
Mong đợi: Hiện "Không có kết nối — kiểm tra mạng" + nút Thử lại.
Pass/Fail: [ ]

## TC-005: Offline — Có cache
Điều kiện: Đã tải thời tiết thành công lần trước. Bật Chế độ Máy bay.
Bước: Pull to refresh.
Mong đợi: Hiện dữ liệu cũ. Banner "Cập nhật lần cuối X phút trước" hiển thị.
Pass/Fail: [ ]

## TC-006: Pull-to-Refresh
Điều kiện: Thời tiết đã tải thành công.
Bước: Kéo màn hình xuống.
Mong đợi: Loading indicator xuất hiện, rồi thời tiết tải lại với dữ liệu mới.
Pass/Fail: [ ]

## TC-007: Vị trí độ chính xác thấp
Điều kiện: Ép độ chính xác thấp trong Simulator (mức City).
Bước: Tải thời tiết.
Mong đợi: Thời tiết hiển thị. Nhãn "Vị trí gần đúng" hiển thị.
Pass/Fail: [ ]
```

**Bạn**: Test thủ công trên iOS Simulator và/hoặc thiết bị thật. Đánh dấu pass/fail từng case.

---

### Phase 8 — Báo cáo Cuối

**Lệnh**: `/sdd-report T-001`

**Tạo ra**: `docs/changes/T-001/report.md`

```markdown
# Final Report — T-001: Màn hình Thời tiết Hiện tại

Trạng thái: HOÀN THÀNH ✓
Ngày: 2026-06-01

## Tóm tắt
Đã implement màn hình thời tiết hiện tại cho WeatherNow iOS từ đầu.
Nền tảng MVVM + Clean Architecture đầy đủ đã được thiết lập.
13 file Swift đã tạo. Tất cả unit test pass (8/8). Black-box test pass (7/7).

## Kiến trúc đã thiết lập (tái sử dụng cho ticket tiếp theo)
- Pattern @Observable ViewModel với typed ViewState enum
- Repository protocol + URLSession implementation (mockable trong test)
- CoreLocation async/await wrapper
- Tầng cache UserDefaults với metadata staleness
- Dependency injection tại entry point của app

## Rủi ro đã chấp nhận
- AR-001: API key trong Info.plist — chuyển sang server-side proxy trước App Store (T-003).

## Ticket follow-up đề xuất
- T-002: Màn hình Dự báo theo Giờ (tái dùng WeatherRepository, LocationService)
- T-003: Server Proxy cho API Key (giải quyết AR-001 trước khi phát hành công khai)
- T-004: Home Screen Widget (widget hiện nhiệt độ trên màn hình chính)
- T-005: Thêm retry logic khi network timeout
```

---

### Phase 9 — Learnings & Living Docs

**Lệnh**: `/sdd-learnings T-001`

**Tạo ra**: `docs/changes/T-001/promotion-candidates.md`

```markdown
# Promotion Candidates — T-001

## PC-001: Pattern @Observable ViewModel
→ Promote vào: docs/standards/coding-conventions.md
Nội dung: Tất cả ViewModel dùng @Observable + typed ViewState enum.
Mutation state qua @MainActor. Dependencies inject qua init.

## PC-002: Pattern Repository Protocol
→ Promote vào: docs/standards/coding-conventions.md
Nội dung: Tất cả data source định nghĩa bằng Swift protocol.
Implementation cụ thể được inject — không bao giờ khởi tạo trong ViewModel.

## PC-003: Lưu API Key trong Info.plist (Failure Mode)
→ Promote vào: docs/maintenance/failure-mode-index.md
Lỗi: API key trong Info.plist có thể đọc được từ binary đã compile.
Giải pháp: Dùng server-side proxy endpoint trước bất kỳ phát hành công khai nào.
Mức ưu tiên: CAO — phải giải quyết trước khi submit App Store.
```

**Bạn**: Xác nhận candidate nào được promote. AI cập nhật `docs/standards/` và `docs/maintenance/failure-mode-index.md` với các pattern đã duyệt.

---

## Điều thay đổi sau T-001

Sau khi ticket đầu tiên hoàn thành, chạy lại `/sdd-map` để thay thế các mục `[PLANNED]` bằng đường dẫn source thật:

```
/sdd-map
```

Tài liệu kiến trúc giờ được cập nhật với:
- Đường dẫn file thực tế (không còn `[PLANNED]`)
- Method signature thực (đã xác nhận từ source)
- Bản đồ test coverage

Khi bắt đầu **T-002: Dự báo theo Giờ**, Phase 2 (`/sdd-context`) sẽ tìm thấy các pattern thực trong source code để tham chiếu, thay vì phải lập kế hoạch từ đầu.

---

## Tóm tắt: Điểm mấu chốt cho Dự án Greenfield

| Điểm | Cần lưu ý |
|---|---|
| Output Phase 0-B là `[PLANNED]` | Đúng — là quyết định kiến trúc, không phải quét source |
| M3 phổ biến cho ticket đầu tiên | Nhiều tầng tạo cùng lúc → luôn cần Phase 2+3 |
| Bước thủ công AI không làm được | Thêm chuỗi vào Info.plist, cài đặt Xcode project |
| Chạy lại `/sdd-map` sau T-001 | Chuyển kiến trúc dự kiến thành bản đồ source thực tế cho T-002+ |
| Rủi ro AR-001 đã chấp nhận | Phải theo dõi và giải quyết trước bất kỳ phát hành công khai nào |
