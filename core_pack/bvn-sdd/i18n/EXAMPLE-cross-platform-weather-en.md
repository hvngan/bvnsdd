# Walkthrough: Building WeatherNow for Android + iOS from one shared spec

**Scenario**: You are building *WeatherNow* as **two native apps at once** —
Android (Kotlin / Jetpack Compose) and iOS (Swift / SwiftUI) — driven by a
**single shared spec**. Platform-specific work is separated cleanly inside the
artifacts.

> This is a **documentation example** — it shows what the artifacts look like in
> multi-platform mode, not real code you must run. Compare it with
> `EXAMPLE-ios-weather-en.md` (single-platform) to see what the split adds.

**App overview**

| | |
|---|---|
| Platforms | Android (Kotlin, Jetpack Compose) **+** iOS (Swift, SwiftUI) |
| Single source of truth | `spec-pack.md` — the WHAT (acceptance criteria, contract) |
| Repo layout | monorepo: `android/` + `ios/` + `docs/` |
| Ticket in this walkthrough | **T-001** — Current weather screen (location-based) |
| External API | OpenWeatherMap REST API (one contract, both clients) |

See `docs/standards/cross-platform.md` for the full model and decision rule.

---

## 0. Setup — declare both platforms

```bash
bvn-sdd init --here --lang en
```

Then edit `.bvn-sdd/config.yml` to list both platforms — **this one line turns on
the Shared / Android / iOS split** in every artifact:

```yaml
platforms:
  - android
  - ios

platform_stack:
  shared: "spec-pack is the single source of truth (the WHAT)"
  android: "Kotlin, Jetpack Compose"
  ios: "Swift, SwiftUI"
```

Open the project in **Claude Code** and run `/sdd-phase0a`, describing both
native trees (`android/`, `ios/`) and the shared OpenWeatherMap contract.

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

Because `platforms:` lists two platforms, `system-map.md` gets a shared-spec
layer plus one layer per native tree:

```markdown
# System Map — WeatherNow (multi-platform)
## Status: GREEN-FIELD — all entries [PLANNED]

## Platforms
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared (spec / contract) | docs/, contract | spec-pack SSOT | [PLANNED] |
| Android | android/ | Kotlin, Jetpack Compose, MVVM | [PLANNED] |
| iOS | ios/ | Swift, SwiftUI, MVVM | [PLANNED] |

## Shared contract layer
- WeatherService.getCurrentWeather(lat, lon) -> WeatherData
  (OpenWeatherMap GET /data/2.5/weather — identical request/response for both clients)
- WeatherData { city, tempC, description, iconCode, observedAt }
```

---

## T-001 — Current Weather Screen

### Bootstrap — `/sdd-new T-001 Current weather screen`

One ticket folder, one shared spec. The downstream artifacts will carry the
Shared / Android / iOS split.

---

### Phase 1 — Spec Pack (`/sdd-spec T-001`)

The spec stays **platform-neutral** for the WHAT. Platform appears only as
*surface impact* (§8) and the contract stays singular (§9).

```markdown
# Spec Pack — T-001: Current Weather Screen

## 6. Acceptance Criteria        (neutral — no Kotlin/Swift here)
- [ ] AC-1: App requests location permission on first launch.
- [ ] AC-2: Permission denied → show "Location access required" + a way to open OS settings.
- [ ] AC-3: Permission granted → fetch weather from the shared service.
- [ ] AC-4: Display city, temperature (°C), description, weather icon.
- [ ] AC-5: Show a loading indicator while fetching.
- [ ] AC-6: Network failure with cache → show cache + "Last updated X min ago".
- [ ] AC-7: Network failure with no cache → "No connection" + Retry.
- [ ] AC-8: Pull-to-refresh reloads manually.

## 8. Surface impact (per platform)
| Platform | Screens / surfaces touched | Backend / API touched | Data / events |
|---|---|---|---|
| Shared (contract) | — | OpenWeatherMap GET /weather | WeatherData model |
| Android | CurrentWeather Compose screen | (via shared service) | local cache (DataStore) |
| iOS | CurrentWeather SwiftUI screen | (via shared service) | local cache (UserDefaults) |

## 9. Client/Service contract (platform-neutral)
GET /data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}
Response → WeatherData { city: String, tempC: Double, description: String,
           iconCode: String, observedAt: epochSeconds }
Both Android and iOS consume this identically. No [android-only]/[ios-only] fields.

## 15. Complexity Classification
Two native trees from one spec → multi-platform factor → recommend M3+.
```

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-001`)

The **multi-platform factor** forces a floor of **M3**:

```markdown
# Mode Decision — T-001

## Scoring
- Reversibility: 2  | Uncertainty: 2 | Risk: 1 | Scope: 3 (two native trees from one spec)

## Multi-platform factor
platforms: [android, ios] → Scope = 3 contributor → mode floor M3 applied.

## Decision: M3 (Plus)
## Adapted workflow: sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report
```

> Note: the mode sets the **depth** of each phase, not which phases run. Every
> ticket runs the full sequence above; a lighter mode (e.g. M1) would keep each
> artifact brief but still run every phase. Only MX halts work.

---

### Phase 2 — Context (`/sdd-context T-001`)

`context.md` and `source-map.md` split per native tree; the contract/data model
stays shared.

```markdown
# Context — T-001

## Allowed vs. forbidden patterns
### Shared
- Allowed: map the WeatherData contract identically on both clients.
- Forbidden: forking field names or units per platform.
### Android patterns
- Allowed: @Observable-style ViewModel via Jetpack ViewModel + StateFlow; Compose state hoisting.
- Forbidden: network calls from a @Composable.
### iOS patterns
- Allowed: @Observable ViewModel (iOS 17), @MainActor state mutations.
- Forbidden: URLSession calls from a SwiftUI View; DispatchQueue.main in new code.

## DTO / Entity / Table mappings
_Shared across platforms — both clients map to the same WeatherData contract._
```

```markdown
# Source Map — T-001

## Files likely to change
### Shared
| File | Expected change |
| docs/changes/T-001/spec-pack.md (contract) | the one WeatherData contract |
### Android (android/…)
| android/.../CurrentWeatherViewModel.kt | new — StateFlow<ViewState> |
| android/.../CurrentWeatherScreen.kt | new — Compose screen |
### iOS (ios/…)
| ios/.../CurrentWeatherViewModel.swift | new — @Observable ViewModel |
| ios/.../CurrentWeatherView.swift | new — SwiftUI screen |
```

---

### Phase 3 — Plan (`/sdd-plan T-001`)

`impl-plan.md` splits the HOW and adds the **Cross-platform parity check**.

```markdown
# Implementation Plan — T-001

## Classes / functions / methods
### Android
- CurrentWeatherViewModel.loadWeather(): sets ViewState.Loading → calls shared service → Loaded/Error.
- CurrentWeatherScreen: when(state) → Loading / Loaded / PermissionDenied / Error.
### iOS
- CurrentWeatherViewModel.loadWeather() @MainActor: .loading → shared service → .loaded/.error.
- CurrentWeatherView: switch state → ProgressView / content / denied / error.

## Cross-platform parity check
| Shared AC / behavior | Android impl | iOS impl | Identical? |
|---|---|---|---|
| AC-3 fetch on grant | loadWeather() on first composition | loadWeather() in .task | Yes |
| AC-6 stale cache banner | DataStore cache + banner | UserDefaults cache + banner | Yes (same text/threshold) |
| AC-2 open settings | Intent → App settings | UIApplication openSettingsURL | Divergent surface (OI-1) |

## Mode check
Two native trees in scope → mode M3 confirmed.
```

Intentional divergence (AC-2 deep-link mechanism) is logged in `open-issues.md`
as OI-1 — same observable outcome ("user reaches OS settings"), different native
API.

---

### Phase 4+5 — Implement (`/sdd-implement T-001`)

Each tree is implemented from the **same spec**, in its own idiom — no leakage.

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

Both satisfy AC-3, AC-5, AC-6 identically. Before self-review, the
**Cross-platform consistency** section of `review-checklist.md` is ticked.

---

### Phase 6 — Test (`/sdd-test T-001`)

The AC↔test matrix gains a **Platform** column; a parity test asserts equal
output for equal input.

```markdown
## AC ↔ test matrix
| AC | Platform | Test type | Test name / location | Priority |
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

Cases derived from the shared spec, each tagged with `Platform:`. Identical
behavior → one `Both` case; divergent surface → one case per platform.

```markdown
## AC coverage map
| AC | Platform | Happy path | Boundary | Permission | Error | Status |
| AC-3 | Both | TC-1 | — | — | — | Pending |
| AC-2 | Android | — | — | TC-2a | — | Pending |
| AC-2 | iOS | — | — | TC-2b | — | Pending |

### TC-1: Successful weather load
**AC:** AC-3
**Platform:** Both  _(identical observable behavior on Android and iOS)_
**Input:** permission granted, network available, launch app
**Expected output:** city, temperature (°C), description, icon shown; no spinner, no error.

### TC-2a: Permission denied → open settings (Android)
**AC:** AC-2
**Platform:** Android
**Expected output:** "Location access required"; tapping the button opens the Android App settings screen.

### TC-2b: Permission denied → open settings (iOS)
**AC:** AC-2
**Platform:** iOS
**Expected output:** "Location access required"; tapping the button opens iOS Settings → WeatherNow.
```

---

## Summary — what the split buys you

| Without the split | With `platforms: [android, ios]` |
|---|---|
| One implicit codebase | One shared spec, two clearly separated native trees |
| Platform mixed into the spec | Spec stays neutral; HOW lives in Shared/Android/iOS subsections |
| Parity left to memory | Explicit parity table + cross-platform consistency checklist |
| Divergence hidden | Intentional divergence logged as an open issue |

Single-platform projects (`platforms:` with one entry) collapse every subsection
to one — the split costs nothing when you do not need it.
