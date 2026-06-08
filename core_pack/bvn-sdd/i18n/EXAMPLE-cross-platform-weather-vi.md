# Hướng dẫn: Thêm màn hình dự báo vào WeatherNow (codebase Android + iOS có sẵn)

**Bối cảnh**: *WeatherNow* đã tồn tại trên **cả Android và iOS** với màn hình thời tiết
hiện tại đang hoạt động. Bạn thêm **màn hình dự báo 5 ngày** (T-001) vào cả hai nền tảng
theo BVN-SDD.

> Đây là **ví dụ tài liệu** — minh hoạ artifact trông như thế nào ở chế độ **codebase có
> sẵn + đa nền tảng**, không phải code thật cần chạy. Xem `EXAMPLE-ios-weather-vi.md` (đơn
> nền tảng, greenfield) để so sánh khi không có codebase sẵn.

**Tổng quan dự án**

| | |
|---|---|
| Nền tảng | Android (Kotlin, Jetpack Compose, Hilt) **+** iOS (Swift, SwiftUI, async/await) |
| Trạng thái | Cả hai nền tảng có sẵn: màn hình thời tiết hiện tại đã hoạt động |
| Bố cục repo | monorepo: `android/` + `ios/` + `docs/` |
| Ticket trong hướng dẫn này | **T-001** — Màn hình dự báo 5 ngày |
| API ngoài | OpenWeatherMap REST API (`/data/2.5/forecast`) |

Xem `docs/standards/cross-platform.md` để biết mô hình đầy đủ và quy tắc quyết định.

**Quy ước đọc hướng dẫn này:**  
Mỗi phase có khối **"Bạn gõ vào Claude Code:"** — chính xác văn bản bạn gõ vào cửa sổ Claude Code.  
- Phần lớn command chỉ cần slash command + ticket ID; Claude tự đọc artifact trước đó.  
- `/sdd-spec` là ngoại lệ duy nhất: dán yêu cầu gốc (từ Jira / email / brief) cùng lệnh.

---

## 0. Thiết lập

```bash
bvn-sdd init --here --lang vi
```

Sửa `.bvn-sdd/config.yml` để khai báo cả hai nền tảng:

```yaml
platforms:
  - android
  - ios

platform_stack:
  shared: "spec-pack là single source of truth (phần WHAT)"
  android: "Kotlin, Jetpack Compose, Hilt, StateFlow"
  ios: "Swift, SwiftUI, @Observable, async/await"
```

Mở project trong **Claude Code** và chạy `/sdd-phase0a` ngay lập tức.

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**Bạn gõ vào Claude Code:**
```
/sdd-phase0a
```
*Không cần argument — command tự đọc cấu trúc project, `config.yml`, và `.gitignore`.*

Phase 0-A phát hiện cả hai cây native đã tồn tại và ghi lại rủi ro đặc thù mobile.

```markdown
# Phase 0 Plan

## Project Type: existing
Source files found in android/ and ios/ — running in SURVEY MODE.

## Tech Stack
- Android: Kotlin, minSdkVersion 26, Jetpack Compose, Hilt, StateFlow
- iOS: Swift 5.9, deployment target iOS 16, SwiftUI, @Observable (iOS 17)

## Mobile platform check
- android/local.properties: có (API key reference — không đọc giá trị)
- AndroidManifest.xml permissions: INTERNET, ACCESS_FINE_LOCATION
- ios/Info.plist: NSLocationWhenInUseUsageDescription có
- google-services.json: không có (Firebase không dùng trong project này)

## Risk Register
| Rủi ro | Severity | Mitigation |
|---|---|---|
| API key trong local.properties | Medium | Đã có trong .gitignore — không commit |
| GPS foreground permission | Low | Chỉ foreground; không background |
```

Bạn duyệt `docs/maintenance/phase0/phase0-review.md`, ký nhận các mục còn lại.
Sau đó chạy `/sdd-map`.

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

**Bạn gõ vào Claude Code:**
```
/sdd-map
```
*Không cần argument — command phát hiện chế độ Survey/Green-field từ `phase0-plan.md`, sau đó đọc toàn bộ codebase.*

Survey Mode đọc cả hai cây native và tạo **platform map riêng** cho từng nền tảng —
đây là điểm khác biệt chính so với greenfield.

```markdown
# System Map — WeatherNow (đa nền tảng, codebase có sẵn)

## Platforms
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared (contract) | docs/, contract | spec-pack SSOT | IMPLEMENTED |
| Android | android/ | Kotlin, Compose, Hilt, MVVM | IMPLEMENTED |
| iOS | ios/ | Swift, SwiftUI, @Observable, MVVM | IMPLEMENTED |

## Shared contract layer (đang dùng)
- GET /data/2.5/weather → WeatherData { city, tempC, description, iconCode, observedAt }
- Chưa có: contract cho /data/2.5/forecast endpoint

## Parity Status
| Feature | Android | iOS | Ghi chú |
|---|---|---|---|
| Màn hình thời tiết hiện tại | ✓ Implemented | ✓ Implemented | Parity intact |
| Màn hình dự báo 5 ngày | ✗ Chưa có | ✗ Chưa có | New feature — T-001 |
→ Không có parity debt. Cả hai nền tảng ngang nhau trước T-001.
```

```markdown
# Platform Android Map — WeatherNow

## Architecture: MVVM + Clean Architecture (partial)
android/app/src/main/java/com/weathernow/
  ui/current/      — CurrentWeatherViewModel.kt, CurrentWeatherScreen.kt
  data/remote/     — WeatherApiService.kt (Retrofit), WeatherDto.kt
  data/repository/ — WeatherRepositoryImpl.kt
  domain/model/    — WeatherData.kt
  di/              — NetworkModule.kt (Hilt)

## State management: StateFlow<ViewState>
ViewState: sealed class { Idle | Loading | Loaded(data) | Error(message) }
Pattern trong CurrentWeatherViewModel là chuẩn dự án — tái sử dụng cho Forecast.

## Test infrastructure
- Unit: JUnit 5 + MockK (không dùng Mockito)
- UI: Compose UI testing (chưa có test viết cho CurrentWeather)
- Run: ./gradlew :app:testDebugUnitTest
```

```markdown
# Platform iOS Map — WeatherNow

## Architecture: MVVM + async/await
ios/WeatherNow/
  Features/CurrentWeather/ — CurrentWeatherViewModel.swift, CurrentWeatherView.swift
  Services/                — WeatherAPIClient.swift, WeatherAPIError.swift
  Models/                  — WeatherData.swift

## State management: @Observable ViewModel (iOS 17)
ViewState: enum { idle, loading, loaded(WeatherData), error(String) }
Pattern trong CurrentWeatherViewModel là chuẩn dự án — tái sử dụng cho Forecast.

## Test infrastructure
- Unit: XCTest + protocol-based mocking (không có mocking framework bên ngoài)
- UI: XCUITest (chưa có test viết)
- Run: xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,name=iPhone 16'
```

---

## T-001 — Màn hình dự báo 5 ngày

### Bootstrap — `/sdd-new T-001 Forecast screen`

**Bạn gõ vào Claude Code:**
```
/sdd-new T-001 Màn hình dự báo 5 ngày
```
*Ticket ID + tên ngắn — command tạo `docs/changes/T-001/` và tất cả file artifact trống, không điền nội dung.*

Một thư mục ticket, một spec chung. Platform map từ Phase 0-B sẽ được đọc trong
Phase 2 để xác minh pattern thực tế.

---

### Phase 1 — Spec Pack (`/sdd-spec T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-spec T-001

Yêu cầu từ PM:
Thêm màn hình dự báo 5 ngày. Mỗi ngày hiển thị: tên ngày, nhiệt độ cao/thấp (°C),
mô tả thời tiết, icon. Nguồn: OpenWeatherMap /data/2.5/forecast.
Cache 30 phút; hiện cache nếu offline trong thời gian đó.
Lỗi mạng → thông báo + nút Thử lại, không crash.
```
*Dán yêu cầu gốc từ Jira / email / brief cùng lệnh. Command đọc `docs/architecture/`, source, rồi kết hợp với yêu cầu bạn cung cấp để tạo `spec-pack.md`. Đây là phase duy nhất bạn cần cung cấp input thủ công.*

Spec giữ **trung lập nền tảng** cho WHAT. `Source Availability` tham chiếu code thực tế
đã đọc được — không phải [PLANNED].

```markdown
# Spec Pack — T-001: Màn hình dự báo 5 ngày

## 6. Acceptance Criteria
- [ ] AC-1: App hiển thị dự báo 5 ngày từ vị trí hiện tại.
- [ ] AC-2: Mỗi ngày hiển thị: tên ngày, nhiệt độ cao/thấp (°C), mô tả, icon.
- [ ] AC-3: Hiện loading khi đang lấy dữ liệu.
- [ ] AC-4: Lỗi mạng → thông báo lỗi + nút Thử lại; không crash.
- [ ] AC-5: Dữ liệu cache trong 30 phút; hiện cache nếu offline trong thời gian này.

## 8. Surface impact (per platform)
| Platform | Màn hình / bề mặt | Backend / API | Dữ liệu / sự kiện |
|---|---|---|---|
| Shared (contract) | — | OpenWeatherMap GET /forecast | ForecastData model mới |
| Android | ForecastScreen mới (Compose) | WeatherApiService mở rộng | cache (DataStore) |
| iOS | ForecastView mới (SwiftUI) | WeatherAPIClient mở rộng | cache (UserDefaults) |

## 9. Client/Service contract (trung lập nền tảng)
GET /data/2.5/forecast?lat={lat}&lon={lon}&cnt=40&units=metric&appid={key}
Response → ForecastData {
  days: List<DayForecast>   (5 mục, group by ngày)
  DayForecast { date: String, highC: Double, lowC: Double,
                description: String, iconCode: String }
}
Cả Android và iOS dùng giống hệt.

## 14. Source Availability Summary
- WeatherApiService.kt / WeatherAPIClient.swift: CÓ SẴN, cần thêm endpoint /forecast
- WeatherData model: CÓ SẴN, cần thêm ForecastData model
- ViewState pattern: CÓ SẴN trong CurrentWeather — tái sử dụng nguyên mẫu

## 15. Complexity Classification
Hai cây native + codebase có sẵn → M3 Plus.
```

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-rightsize T-001
```
*Không cần thêm gì — command tự đọc `spec-pack.md` và `config.yml` (`platforms:`) để chấm điểm và chọn mode.*

**Yếu tố đa nền tảng** đẩy sàn lên **M3**:

```markdown
# Mode Decision — T-001

## Scoring
- Reversibility: 1 (thêm tính năng mới, không sửa tính năng cũ)
- Uncertainty: 2 (contract /forecast rõ nhưng grouping logic cần verify)
- Risk: 1 (không đụng auth, DB production, payment)
- Scope: 3 (hai cây native từ một spec)

## Multi-platform factor
platforms: [android, ios] → Scope = 3 → mode floor M3 applied.

## Quyết định: M3 (Plus)
## Workflow: sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report → sdd-learnings
```

> Lưu ý: mode đặt **độ sâu** của mỗi phase, không quyết định phase nào chạy.
> Mọi ticket chạy đủ chuỗi trên; chỉ MX mới dừng việc.

---

### Phase 2 — Context (`/sdd-context T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-context T-001
```
*Không cần thêm gì — command đọc platform map từ Phase 0-B, `spec-pack.md`, rồi Grep source để xác minh pattern thực tế.*

`context.md` đọc platform map từ Phase 0-B trước, sau đó xác minh pattern **thực tế
tồn tại** trong codebase bằng Grep — không có `[PLANNED]` ở đây.

```markdown
# Context — T-001

## Correct examples in the codebase

### Android patterns
- CurrentWeatherViewModel.kt: @HiltViewModel + StateFlow<ViewState> + viewModelScope.launch
  → ĐÂY là chuẩn cho ForecastViewModel (verified bằng Read)
- WeatherApiService.kt: @GET + suspend fun + Retrofit interface
  → Thêm getForecast() cùng pattern này

### iOS patterns
- CurrentWeatherViewModel.swift: @Observable final class + enum ViewState + @MainActor func
  → ĐÂY là chuẩn cho ForecastViewModel (verified bằng Read)
- WeatherAPIClient.swift: func fetch...() async throws → Model
  → Thêm fetchForecast() cùng pattern này

## Allowed vs. forbidden patterns

### Android
- Cho phép: StateFlow<ViewState> + @HiltViewModel + @Inject constructor
- Cho phép: DataStore cho cache (đã dùng trong CurrentWeather — reuse)
- Cấm: LiveData (dự án đã chuyển hoàn toàn sang StateFlow)
- Cấm: gọi mạng trực tiếp từ @Composable

### iOS
- Cho phép: @Observable class + @MainActor func load() async
- Cho phép: UserDefaults cho cache ngắn hạn (cùng pattern CurrentWeather)
- Cấm: ObservableObject (đã replace bằng @Observable trong codebase này)
- Cấm: URLSession trực tiếp từ SwiftUI View; DispatchQueue.main trong code mới

## Methods / classes that actually exist

### Android (verified với Grep)
- WeatherRepositoryImpl.fetchCurrentWeather() — tồn tại ✓
- WeatherApiService.getCurrentWeather() — tồn tại ✓ (cần thêm getForecast())
- StateFlow<ViewState> trong CurrentWeatherViewModel — tồn tại ✓

### iOS (verified với Grep)
- WeatherAPIClient.fetchCurrentWeather() — tồn tại ✓
- @Observable CurrentWeatherViewModel — tồn tại ✓
- ViewState enum (idle/loading/loaded/error) — tồn tại ✓

## Parity gap check
Cả hai nền tảng đã implement CurrentWeather. Không có parity debt ảnh hưởng T-001.
```

---

### Phase 3 — Plan (`/sdd-plan T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-plan T-001
```
*Không cần thêm gì — command đọc `context.md` và `spec-pack.md` để tạo impact analysis và implementation plan.*

`impl-plan.md` split theo nền tảng; bảng parity check xác nhận cả hai bắt đầu từ
cùng baseline.

```markdown
# Implementation Plan — T-001

## Files to change

### Shared
| File | Lý do | Add / Modify |
|---|---|---|
| docs/changes/T-001/spec-pack.md | SSOT cho ForecastData contract | Modify |

### Android
| File | Lý do | Add / Modify |
|---|---|---|
| android/.../data/remote/WeatherApiService.kt | Thêm getForecast() endpoint | Modify |
| android/.../data/remote/ForecastDto.kt | DTO mới cho /forecast response | Add |
| android/.../domain/model/ForecastData.kt | Domain model mới | Add |
| android/.../data/repository/WeatherRepositoryImpl.kt | Implement fetchForecast() | Modify |
| android/.../ui/forecast/ForecastViewModel.kt | ViewModel mới (StateFlow<ViewState>) | Add |
| android/.../ui/forecast/ForecastScreen.kt | Compose screen mới | Add |

### iOS
| File | Lý do | Add / Modify |
|---|---|---|
| ios/.../Services/WeatherAPIClient.swift | Thêm fetchForecast() | Modify |
| ios/.../Models/ForecastData.swift | Model mới | Add |
| ios/.../Features/Forecast/ForecastViewModel.swift | ViewModel mới (@Observable) | Add |
| ios/.../Features/Forecast/ForecastView.swift | SwiftUI screen mới | Add |

## Cross-platform parity check
| Shared AC / hành vi | Android impl | iOS impl | Giống hệt? |
|---|---|---|---|
| AC-1 5 ngày từ vị trí | ForecastViewModel.loadForecast() | ForecastViewModel.loadForecast() @MainActor | Có |
| AC-3 loading indicator | ViewState.Loading → CircularProgressIndicator | ViewState.loading → ProgressView | Có |
| AC-4 lỗi mạng + retry | ViewState.Error + retry button | ViewState.error + retry button | Có |
| AC-5 cache 30 phút | DataStore + timestamp check | UserDefaults + timestamp check | Có (cùng threshold) |

## Mode check
Hai cây native + không có parity debt → M3 xác nhận.
```

---

### Phase 4+5 — Implement (`/sdd-implement T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-implement T-001
```
*Không cần thêm gì — command đọc `impl-plan.md`, trình review checklist và chờ xác nhận của bạn trước khi viết code. Dừng tại mỗi Stop/Ask point.*

Mỗi cây được mở rộng từ **pattern đã tồn tại**, theo idiom riêng.

**Android — `ForecastViewModel.kt` (mới, theo chuẩn CurrentWeatherViewModel)**
```kotlin
@HiltViewModel
class ForecastViewModel @Inject constructor(
    private val repo: WeatherRepository,
    private val location: LocationService,
) : ViewModel() {
    private val _state = MutableStateFlow<ViewState>(ViewState.Idle)
    val state: StateFlow<ViewState> = _state.asStateFlow()

    fun loadForecast() = viewModelScope.launch {
        _state.value = ViewState.Loading
        runCatching {
            val loc = location.current()
            repo.fetchForecast(loc.lat, loc.lon)
        }.onSuccess { _state.value = ViewState.Loaded(it) }
         .onFailure { _state.value = repo.cachedForecast()?.let(ViewState::Loaded)
                                       ?: ViewState.Error(it.message.orEmpty()) }
    }
}
```

**iOS — `ForecastViewModel.swift` (mới, theo chuẩn CurrentWeatherViewModel)**
```swift
@Observable final class ForecastViewModel {
    enum ViewState { case idle, loading, loaded([DayForecast]), error(String) }
    private(set) var state: ViewState = .idle

    @MainActor func loadForecast() async {
        state = .loading
        do {
            let loc = try await location.current()
            state = .loaded(try await apiClient.fetchForecast(lat: loc.lat, lon: loc.lon))
        } catch {
            state = cachedForecast().map(ViewState.loaded) ?? .error(error.localizedDescription)
        }
    }
}
```

Cả hai thỏa AC-1, AC-3, AC-4, AC-5 giống hệt. Trước self-review, mục
**Cross-platform consistency** trong `review-checklist.md` được tick: mọi AC quan
sát được trên cả hai nền tảng; ForecastData contract dùng giống hệt.

---

### Phase 6 — Test (`/sdd-test T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-test T-001
```
*Không cần thêm gì — command đọc `spec-pack.md` và source đã implement, viết và chạy test theo ma trận AC.*

Ma trận AC↔test có cột **Platform**; contract test xác nhận cùng JSON fixture
cho cùng model trên cả hai client.

```markdown
## AC ↔ test matrix
| AC | Platform | Loại | Tên test | Ưu tiên |
|---|---|---|---|---|
| AC-1 | Android | unit | ForecastViewModelTest.loadForecast_success | H |
| AC-1 | iOS | unit | ForecastViewModelTests.loadForecast_success | H |
| AC-1 | Shared | contract | ForecastContractTest (JSON fixture → ForecastData) | H |
| AC-4 | Android | unit | ForecastViewModelTest.loadForecast_networkError | H |
| AC-4 | iOS | unit | ForecastViewModelTests.loadForecast_networkError | H |
| AC-5 | Android | unit | ForecastViewModelTest.loadForecast_cacheHit | M |
| AC-5 | iOS | unit | ForecastViewModelTests.loadForecast_cacheHit | M |

## Run commands
# Android
./gradlew :app:testDebugUnitTest --tests "*.ForecastViewModelTest"
# iOS
xcodebuild test -scheme WeatherNow \
  -destination 'platform=iOS Simulator,name=iPhone 16' \
  -only-testing:WeatherNowTests/ForecastViewModelTests
```

---

### Phase 7 — Black-box (`/sdd-blackbox T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-blackbox T-001
```
*Không cần thêm gì — command đọc `spec-pack.md` và `test-results.md` để sinh test case từ góc nhìn user/QA.*

Case suy từ spec chung, tag `Platform:`. Hành vi giống hệt → một case `Both`.

```markdown
## AC coverage map
| AC | Platform | Happy path | Error | Cache | Status |
|---|---|---|---|---|---|
| AC-1,2 | Both | TC-1 | — | — | Pending |
| AC-4 | Both | — | TC-2 | — | Pending |
| AC-5 | Both | — | — | TC-3 | Pending |

### TC-1: Hiển thị dự báo 5 ngày thành công
AC: AC-1, AC-2
Platform: Both
Input: đã cấp quyền vị trí, có mạng, mở màn hình Forecast
Expected output: 5 dòng, mỗi dòng có tên ngày, nhiệt độ cao/thấp (°C), mô tả, icon.

### TC-2: Lỗi mạng — không có cache
AC: AC-4
Platform: Both
Input: airplane mode, không có cache, mở màn hình Forecast
Expected output: thông báo lỗi + nút "Thử lại"; không crash.

### TC-3: Cache còn hiệu lực (< 30 phút)
AC: AC-5
Platform: Both
Input: load thành công → bật airplane mode → mở lại trong vòng 30 phút
Expected output: dữ liệu cũ hiển thị; không spinner; không lỗi.
```

---

### Phase 8 — Báo cáo (`/sdd-report T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-report T-001
```
*Không cần thêm gì — command tổng hợp tất cả artifact đã tạo thành báo cáo cuối.*

```markdown
# Final Report — T-001: Màn hình dự báo 5 ngày

## Acceptance Criteria — completion
| AC | Android | iOS | Ghi chú |
|---|---|---|---|
| AC-1 Hiển thị 5 ngày | PASS | PASS | Cả hai từ cùng ForecastData contract |
| AC-2 Nội dung từng ngày | PASS | PASS | Đủ tên ngày, nhiệt độ, mô tả, icon |
| AC-3 Loading | PASS | PASS | Indicator theo chuẩn từng nền tảng |
| AC-4 Lỗi mạng + retry | PASS | PASS | Thông báo + retry đúng |
| AC-5 Cache 30 phút | PASS | PASS | Cùng threshold; DataStore vs UserDefaults |

## Cross-platform parity summary
Tất cả 5 AC đạt trên cả hai nền tảng. Không có khác biệt có chủ đích trong T-001.

## Rủi ro đã chấp nhận
- Cache storage khác nhau (DataStore vs UserDefaults) — chấp nhận, đây là platform idiom.

## Theo dõi
- T-002: Màn hình chi tiết ngày (tap-through từ dự báo).
```

---

### Phase 9 — Learnings (`/sdd-learnings T-001`)

**Bạn gõ vào Claude Code:**
```
/sdd-learnings T-001
```
*Không cần thêm gì — command đọc toàn bộ ticket artifacts, đề xuất promotion candidates và cập nhật `failure-mode-index.md`.*

```markdown
# Promotion Candidates — T-001

## Pattern đề xuất → docs/standards/cross-platform.md
- **Reuse ViewModel pattern**: khi thêm tính năng mới trên codebase có sẵn, nhân bản
  cấu trúc ViewModel hiện có (StateFlow/ViewState trên Android; @Observable/ViewState
  trên iOS) thay vì thiết kế pattern mới. Giữ consistency giữa các feature.
- **Platform map trước context**: docs/architecture/platform-android-map.md và
  platform-ios-map.md phải được đọc trước khi điền context.md — ngăn spec pattern
  không tồn tại trong codebase thực.

## Parity check result — T-001
Không có parity debt trước T-001. Bảng parity trong impl-plan.md: 4/4 hành vi
đồng nhất; 0 khác biệt có chủ đích.

## Failure mode thêm vào → docs/maintenance/failure-mode-index.md
FM-08: Feature added to one platform only — parity debt tích lũy giữa các ticket.
  Nguyên nhân: ticket chỉ scope một nền tảng mà không ghi nhận parity gap.
  Phát hiện: §Parity Status trong system-map.md; bảng parity trong impl-plan.md.
  Cách xử lý: mọi ticket multi-platform phải điền bảng parity đầy đủ.
```

---

## Tóm tắt — điểm khác biệt khi có codebase sẵn

| Greenfield (`[PLANNED]`) | Existing codebase (hướng dẫn này) |
|---|---|
| system-map.md toàn `[PLANNED]` | system-map.md hiển thị trạng thái thực + §Parity Status |
| Phase 0-B không có platform map | Phase 0-B tạo `platform-android-map.md` + `platform-ios-map.md` |
| context.md thiết kế pattern | context.md xác minh pattern đã tồn tại (Grep/Read) |
| source-map.md liệt kê file cần TẠO | source-map.md liệt kê file cần SỬA + file mới |
| Parity check baseline từ đầu | Parity check verify baseline hiện tại trước khi spec |

Project đơn nền tảng (`platforms:` một mục) gập mọi subsection về một — phần split
không tốn gì khi bạn không cần đến.
