# Hướng dẫn: Xây dựng WeatherNow cho Android + iOS từ một spec chung

**Bối cảnh**: Bạn xây dựng *WeatherNow* thành **hai app native cùng lúc** —
Android (Kotlin / Jetpack Compose) và iOS (Swift / SwiftUI) — được điều khiển bởi
**một spec chung duy nhất**. Phần đặc thù theo nền tảng được tách bạch rõ ràng
ngay trong các artifact.

> Đây là **ví dụ tài liệu** — minh hoạ artifact trông như thế nào ở chế độ đa nền
> tảng, không phải code thật cần chạy. So sánh với `EXAMPLE-ios-weather-en.md`
> (đơn nền tảng) để thấy phần split mang lại điều gì.

**Tổng quan app**

| | |
|---|---|
| Nền tảng | Android (Kotlin, Jetpack Compose) **+** iOS (Swift, SwiftUI) |
| Single source of truth | `spec-pack.md` — phần WHAT (acceptance criteria, contract) |
| Bố cục repo | monorepo: `android/` + `ios/` + `docs/` |
| Ticket trong hướng dẫn này | **T-001** — Màn hình thời tiết hiện tại (theo vị trí) |
| API ngoài | OpenWeatherMap REST API (một contract, cả hai client dùng chung) |

Xem `docs/standards/cross-platform.md` để biết đầy đủ mô hình và quy tắc quyết định.

---

## 0. Thiết lập — khai báo cả hai nền tảng

```bash
bvn-sdd init --here --lang vi
```

Sau đó sửa `.bvn-sdd/config.yml` để liệt kê cả hai nền tảng — **chỉ một dòng này
sẽ bật phần split Shared / Android / iOS** trong mọi artifact:

```yaml
platforms:
  - android
  - ios

platform_stack:
  shared: "spec-pack là single source of truth (phần WHAT)"
  android: "Kotlin, Jetpack Compose"
  ios: "Swift, SwiftUI"
```

Mở project trong **Claude Code** và chạy `/sdd-phase0a`, mô tả cả hai cây native
(`android/`, `ios/`) cùng contract OpenWeatherMap dùng chung.

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

Vì `platforms:` liệt kê hai nền tảng, `system-map.md` có thêm một layer spec/contract
dùng chung cộng với mỗi cây native một layer:

```markdown
# System Map — WeatherNow (đa nền tảng)
## Status: GREEN-FIELD — mọi mục đều [PLANNED]

## Platforms
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared (spec / contract) | docs/, contract | spec-pack SSOT | [PLANNED] |
| Android | android/ | Kotlin, Jetpack Compose, MVVM | [PLANNED] |
| iOS | ios/ | Swift, SwiftUI, MVVM | [PLANNED] |

## Shared contract layer
- WeatherService.getCurrentWeather(lat, lon) -> WeatherData
  (OpenWeatherMap GET /data/2.5/weather — request/response giống hệt cho cả hai client)
- WeatherData { city, tempC, description, iconCode, observedAt }
```

---

## T-001 — Màn hình thời tiết hiện tại

### Bootstrap — `/sdd-new T-001 Current weather screen`

Một thư mục ticket, một spec chung. Các artifact phía sau sẽ mang phần split
Shared / Android / iOS.

---

### Phase 1 — Spec Pack (`/sdd-spec T-001`)

Spec giữ **trung lập nền tảng** cho phần WHAT. Nền tảng chỉ xuất hiện dưới dạng
*ảnh hưởng bề mặt* (§8) và contract vẫn ở dạng số ít (§9).

```markdown
# Spec Pack — T-001: Màn hình thời tiết hiện tại

## 6. Acceptance Criteria        (trung lập — không có Kotlin/Swift ở đây)
- [ ] AC-1: App xin quyền vị trí ở lần mở đầu tiên.
- [ ] AC-2: Từ chối quyền → hiện "Cần quyền truy cập vị trí" + cách mở cài đặt OS.
- [ ] AC-3: Cấp quyền → lấy thời tiết từ service dùng chung.
- [ ] AC-4: Hiển thị thành phố, nhiệt độ (°C), mô tả, icon thời tiết.
- [ ] AC-5: Hiện loading khi đang lấy dữ liệu.
- [ ] AC-6: Lỗi mạng có cache → hiện cache + "Cập nhật X phút trước".
- [ ] AC-7: Lỗi mạng không có cache → "Không có kết nối" + Thử lại.
- [ ] AC-8: Kéo-để-làm-mới reload thủ công.

## 8. Surface impact (per platform)
| Platform | Màn hình / bề mặt bị tác động | Backend / API bị tác động | Dữ liệu / sự kiện |
|---|---|---|---|
| Shared (contract) | — | OpenWeatherMap GET /weather | model WeatherData |
| Android | màn hình Compose CurrentWeather | (qua service chung) | cache cục bộ (DataStore) |
| iOS | màn hình SwiftUI CurrentWeather | (qua service chung) | cache cục bộ (UserDefaults) |

## 9. Client/Service contract (trung lập nền tảng)
GET /data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}
Response → WeatherData { city: String, tempC: Double, description: String,
           iconCode: String, observedAt: epochSeconds }
Cả Android và iOS dùng giống hệt. Không có field [android-only]/[ios-only].

## 15. Complexity Classification
Hai cây native từ một spec → yếu tố đa nền tảng → đề xuất M3+.
```

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-001`)

**Yếu tố đa nền tảng** đẩy sàn lên **M3**:

```markdown
# Mode Decision — T-001

## Scoring
- Reversibility: 2 | Uncertainty: 2 | Risk: 1 | Scope: 3 (hai cây native từ một spec)

## Yếu tố đa nền tảng
platforms: [android, ios] → đóng góp Scope = 3 → áp sàn mode M3.

## Quyết định: M3 (Plus)
## Workflow điều chỉnh: sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report
```

> Lưu ý: mode đặt **độ sâu** của mỗi phase, không quyết định phase nào chạy. Mọi
> ticket chạy đủ chuỗi trên; mode nhẹ hơn (vd M1) chỉ viết gọn artifact nhưng vẫn
> chạy đủ phase. Chỉ MX mới dừng việc.

---

### Phase 2 — Context (`/sdd-context T-001`)

`context.md` và `source-map.md` split theo cây native; contract/data model giữ
dùng chung.

```markdown
# Context — T-001

## Allowed vs. forbidden patterns
### Shared
- Cho phép: map contract WeatherData giống hệt trên cả hai client.
- Cấm: fork tên field hoặc đơn vị theo nền tảng.
### Android patterns
- Cho phép: ViewModel kiểu @Observable qua Jetpack ViewModel + StateFlow; hoist state ở Compose.
- Cấm: gọi mạng từ @Composable.
### iOS patterns
- Cho phép: ViewModel @Observable (iOS 17), thay đổi state ở @MainActor.
- Cấm: gọi URLSession từ SwiftUI View; DispatchQueue.main trong code mới.

## DTO / Entity / Table mappings
_Dùng chung giữa các nền tảng — cả hai client map vào cùng contract WeatherData._
```

```markdown
# Source Map — T-001

## Files likely to change
### Shared
| File | Thay đổi dự kiến |
| docs/changes/T-001/spec-pack.md (contract) | một contract WeatherData duy nhất |
### Android (android/…)
| android/.../CurrentWeatherViewModel.kt | mới — StateFlow<ViewState> |
| android/.../CurrentWeatherScreen.kt | mới — màn hình Compose |
### iOS (ios/…)
| ios/.../CurrentWeatherViewModel.swift | mới — ViewModel @Observable |
| ios/.../CurrentWeatherView.swift | mới — màn hình SwiftUI |
```

---

### Phase 3 — Plan (`/sdd-plan T-001`)

`impl-plan.md` split phần HOW và thêm **Cross-platform parity check**.

```markdown
# Implementation Plan — T-001

## Classes / functions / methods
### Android
- CurrentWeatherViewModel.loadWeather(): set ViewState.Loading → gọi service chung → Loaded/Error.
- CurrentWeatherScreen: when(state) → Loading / Loaded / PermissionDenied / Error.
### iOS
- CurrentWeatherViewModel.loadWeather() @MainActor: .loading → service chung → .loaded/.error.
- CurrentWeatherView: switch state → ProgressView / nội dung / denied / error.

## Cross-platform parity check
| Shared AC / hành vi | Android impl | iOS impl | Giống hệt? |
|---|---|---|---|
| AC-3 fetch khi được cấp quyền | loadWeather() ở composition đầu | loadWeather() trong .task | Có |
| AC-6 banner cache cũ | cache DataStore + banner | cache UserDefaults + banner | Có (cùng text/ngưỡng) |
| AC-2 mở cài đặt | Intent → cài đặt App | UIApplication openSettingsURL | Khác bề mặt (OI-1) |

## Mode check
Hai cây native trong scope → xác nhận mode M3.
```

Phần khác biệt có chủ đích (cơ chế deep-link AC-2) được ghi vào `open-issues.md`
dưới dạng OI-1 — cùng kết quả quan sát được ("người dùng tới cài đặt OS"), khác
API native.

---

### Phase 4+5 — Implement (`/sdd-implement T-001`)

Mỗi cây được hiện thực từ **cùng một spec**, theo idiom riêng — không lẫn lộn.

**Android — `android/.../CurrentWeatherViewModel.kt`**
```kotlin
class CurrentWeatherViewModel(
    private val repo: WeatherRepository,
    private val location: LocationService,
) : ViewModel() {
    private val _state = MutableStateFlow<ViewState>(ViewState.Idle)
    val state: StateFlow<ViewState> = _state.asStateFlow()

    fun loadWeather() = viewModelScope.launch {
        _state.value = ViewState.Loading
        runCatching {
            val loc = location.current()
            repo.fetchCurrentWeather(loc.lat, loc.lon)
        }.onSuccess { _state.value = ViewState.Loaded(it) }
         .onFailure { _state.value = repo.cached()?.let(ViewState::Loaded)
                                       ?: ViewState.Error(it.message.orEmpty()) }
    }
}
```

**iOS — `ios/.../CurrentWeatherViewModel.swift`**
```swift
@Observable final class CurrentWeatherViewModel {
    enum ViewState { case idle, loading, loaded(WeatherData), denied, error(String) }
    private(set) var state: ViewState = .idle

    @MainActor func loadWeather() async {
        state = .loading
        do {
            let loc = try await location.current()
            state = .loaded(try await repo.fetchCurrentWeather(lat: loc.lat, lon: loc.lon))
        } catch {
            state = repo.cached().map(ViewState.loaded) ?? .error(error.localizedDescription)
        }
    }
}
```

Cả hai thoả mãn AC-3, AC-5, AC-6 giống hệt. Trước self-review, mục
**Cross-platform consistency** trong `review-checklist.md` được tick.

---

### Phase 6 — Test (`/sdd-test T-001`)

Ma trận AC↔test có thêm cột **Platform**; một parity test khẳng định cùng input
cho cùng output.

```markdown
## AC ↔ test matrix
| AC | Platform | Loại test | Tên test / vị trí | Ưu tiên |
| AC-3 | Android | unit | CurrentWeatherViewModelTest.loadSuccess | H |
| AC-3 | iOS | unit | CurrentWeatherViewModelTests.loadSuccess | H |
| AC-3 | Shared | contract | WeatherContractTest (fixture JSON → WeatherData) | H |
| AC-6 | Android | unit | ...networkError_withCache | H |
| AC-6 | iOS | unit | ...networkError_withCache | H |

## Run commands
# Android
./gradlew :app:testDebugUnitTest
# iOS
xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,name=iPhone 15'
```

---

### Phase 7 — Black-box (`/sdd-blackbox T-001`)

Test case suy ra từ spec chung, mỗi case gắn `Platform:`. Hành vi giống hệt → một
case `Both`; bề mặt khác nhau → mỗi nền tảng một case.

```markdown
## AC coverage map
| AC | Platform | Happy path | Boundary | Permission | Error | Status |
| AC-3 | Both | TC-1 | — | — | — | Pending |
| AC-2 | Android | — | — | TC-2a | — | Pending |
| AC-2 | iOS | — | — | TC-2b | — | Pending |

### TC-1: Tải thời tiết thành công
**AC:** AC-3
**Platform:** Both  _(hành vi quan sát được giống hệt trên Android và iOS)_
**Input:** đã cấp quyền, có mạng, mở app
**Expected output:** hiện thành phố, nhiệt độ (°C), mô tả, icon; không spinner, không lỗi.

### TC-2a: Từ chối quyền → mở cài đặt (Android)
**AC:** AC-2
**Platform:** Android
**Expected output:** "Cần quyền truy cập vị trí"; chạm nút mở màn hình cài đặt App của Android.

### TC-2b: Từ chối quyền → mở cài đặt (iOS)
**AC:** AC-2
**Platform:** iOS
**Expected output:** "Cần quyền truy cập vị trí"; chạm nút mở iOS Settings → WeatherNow.
```

---

## Tóm tắt — phần split mang lại gì

| Không có split | Có `platforms: [android, ios]` |
|---|---|
| Một codebase ngầm định | Một spec chung, hai cây native tách bạch rõ |
| Nền tảng lẫn vào spec | Spec trung lập; phần HOW nằm trong subsection Shared/Android/iOS |
| Parity dựa vào trí nhớ | Bảng parity rõ ràng + checklist cross-platform consistency |
| Khác biệt bị giấu | Khác biệt có chủ đích được ghi thành open issue |

Project đơn nền tảng (`platforms:` một mục) gập mọi subsection về một — phần split
không tốn gì khi bạn không cần đến.
