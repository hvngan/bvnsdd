# Walkthrough: Adding a forecast screen to WeatherNow (existing Android + iOS codebase)

**Scenario**: *WeatherNow* already exists on **both Android and iOS** with a working
current weather screen. You are adding a **5-day forecast screen** (T-001) to both
platforms following BVN-SDD.

> This is a **documentation example** — it shows what the artifacts look like in
> **existing codebase + multi-platform** mode, not real code you must run. Compare
> with `EXAMPLE-ios-weather-en.md` (single-platform, greenfield) to see the
> difference when no codebase exists yet.

**Project overview**

| | |
|---|---|
| Platforms | Android (Kotlin, Jetpack Compose, Hilt) **+** iOS (Swift, SwiftUI, async/await) |
| Status | Both platforms exist: current weather screen already working |
| Repo layout | monorepo: `android/` + `ios/` + `docs/` |
| Ticket in this walkthrough | **T-001** — 5-day forecast screen |
| External API | OpenWeatherMap REST API (`/data/2.5/forecast`) |

See `docs/standards/cross-platform.md` for the full model and decision rule.

**How to read this walkthrough:**  
Each phase has a **"You type into Claude Code:"** block — the exact text you enter in the Claude Code window.  
- Most commands only need the slash command + ticket ID; Claude reads all previous artifacts automatically.  
- `/sdd-spec` is the only exception: paste the original requirements (from Jira / email) together with the command.

---

## 0. Setup

```bash
bvn-sdd init --here --lang en
```

Edit `.bvn-sdd/config.yml` to declare both platforms:

```yaml
platforms:
  - android
  - ios

platform_stack:
  shared: "spec-pack is the single source of truth (the WHAT)"
  android: "Kotlin, Jetpack Compose, Hilt, StateFlow"
  ios: "Swift, SwiftUI, @Observable, async/await"
```

Open the project in **Claude Code** and run `/sdd-phase0a` immediately.

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**You type into Claude Code:**
```
/sdd-phase0a
```
*No argument needed — the command reads project structure and `config.yml` automatically.*

Phase 0-A detects both native trees already exist and records mobile-specific risks.

```markdown
# Phase 0 Plan

## Project Type: existing
Source files found in android/ and ios/ — running in SURVEY MODE.

## Tech Stack
- Android: Kotlin, minSdkVersion 26, Jetpack Compose, Hilt, StateFlow
- iOS: Swift 5.9, deployment target iOS 16, SwiftUI, @Observable (iOS 17)

## Mobile platform check
- android/local.properties: present (API key reference — values not read)
- AndroidManifest.xml permissions: INTERNET, ACCESS_FINE_LOCATION
- ios/Info.plist: NSLocationWhenInUseUsageDescription present
- google-services.json: absent (Firebase not used in this project)

## Risk Register
| Risk | Severity | Mitigation |
|---|---|---|
| API key in local.properties | Medium | Already in .gitignore — not committed |
| GPS foreground permission | Low | Foreground only; no background |
```

Review `docs/maintenance/phase0/phase0-review.md`, sign off remaining items.
Then run `/sdd-map`.

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

**You type into Claude Code:**
```
/sdd-map
```
*No argument needed — the command detects Survey/Green-field mode from `phase0-plan.md` and then reads the whole codebase.*

Survey Mode reads both native trees and produces a **dedicated platform map** for
each — this is the key difference from a greenfield run.

```markdown
# System Map — WeatherNow (multi-platform, existing codebase)

## Platforms
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared (contract) | docs/, contract | spec-pack SSOT | IMPLEMENTED |
| Android | android/ | Kotlin, Compose, Hilt, MVVM | IMPLEMENTED |
| iOS | ios/ | Swift, SwiftUI, @Observable, MVVM | IMPLEMENTED |

## Shared contract layer (in use)
- GET /data/2.5/weather → WeatherData { city, tempC, description, iconCode, observedAt }
- Not yet: contract for /data/2.5/forecast endpoint

## Parity Status
| Feature | Android | iOS | Notes |
|---|---|---|---|
| Current weather screen | ✓ Implemented | ✓ Implemented | Parity intact |
| 5-day forecast screen | ✗ Not yet | ✗ Not yet | New feature — T-001 |
→ No parity debt. Both platforms are even before T-001.
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
Pattern in CurrentWeatherViewModel is the project standard — reuse for Forecast.

## Test infrastructure
- Unit: JUnit 5 + MockK (Mockito not used)
- UI: Compose UI testing (no tests written yet for CurrentWeather)
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
Pattern in CurrentWeatherViewModel is the project standard — reuse for Forecast.

## Test infrastructure
- Unit: XCTest + protocol-based mocking (no external mocking framework)
- UI: XCUITest (no tests written yet)
- Run: xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,name=iPhone 16'
```

---

## T-001 — 5-day forecast screen

### Bootstrap — `/sdd-new T-001 Forecast screen`

**You type into Claude Code:**
```
/sdd-new T-001 5-day forecast screen
```
*Ticket ID + short name — the command creates `docs/changes/T-001/` and all blank artifact files; it does not fill in any content.*

One ticket folder, one shared spec. Platform maps from Phase 0-B will be read in
Phase 2 to verify real existing patterns.

---

### Phase 1 — Spec Pack (`/sdd-spec T-001`)

**You type into Claude Code:**
```
/sdd-spec T-001

Requirements from PM:
Add a 5-day forecast screen. Each day must show: day name, high/low temperature (°C),
weather description, icon. Source: OpenWeatherMap /data/2.5/forecast.
Cache for 30 minutes; show cache if offline within that window.
Network failure → error message + Retry button, no crash.
```
*Paste the original requirements from Jira / email / brief together with the command. The command reads `docs/architecture/`, source, and combines them with what you provide to produce `spec-pack.md`. This is the only phase where you supply manual input.*

The spec stays **platform-neutral** for the WHAT. `Source Availability` references
code that was actually read — no `[PLANNED]` entries.

```markdown
# Spec Pack — T-001: 5-day forecast screen

## 6. Acceptance Criteria
- [ ] AC-1: App shows a 5-day forecast from the current location.
- [ ] AC-2: Each day shows: day name, high/low temperature (°C), description, icon.
- [ ] AC-3: Show a loading indicator while fetching.
- [ ] AC-4: Network failure → show an error message + Retry button; no crash.
- [ ] AC-5: Data cached for 30 minutes; show cache if offline within that window.

## 8. Surface impact (per platform)
| Platform | Screens / surfaces touched | Backend / API touched | Data / events |
|---|---|---|---|
| Shared (contract) | — | OpenWeatherMap GET /forecast | new ForecastData model |
| Android | new ForecastScreen (Compose) | WeatherApiService extended | cache (DataStore) |
| iOS | new ForecastView (SwiftUI) | WeatherAPIClient extended | cache (UserDefaults) |

## 9. Client/Service contract (platform-neutral)
GET /data/2.5/forecast?lat={lat}&lon={lon}&cnt=40&units=metric&appid={key}
Response → ForecastData {
  days: List<DayForecast>   (5 entries, grouped by day)
  DayForecast { date: String, highC: Double, lowC: Double,
                description: String, iconCode: String }
}
Both Android and iOS consume this identically.

## 14. Source Availability Summary
- WeatherApiService.kt / WeatherAPIClient.swift: EXISTS, needs /forecast endpoint added
- WeatherData model: EXISTS, need new ForecastData model
- ViewState pattern: EXISTS in CurrentWeather — reuse the same structure

## 15. Complexity Classification
Two native trees + existing codebase → M3 Plus.
```

---

### Phase 1-B — Right-sizing (`/sdd-rightsize T-001`)

**You type into Claude Code:**
```
/sdd-rightsize T-001
```
*No extra input needed — the command reads `spec-pack.md` and `config.yml` (`platforms:`) to score and choose the mode.*

The **multi-platform factor** forces a floor of **M3**:

```markdown
# Mode Decision — T-001

## Scoring
- Reversibility: 1 (adding new feature, not modifying existing ones)
- Uncertainty: 2 (contract /forecast is clear but grouping logic needs verification)
- Risk: 1 (no auth, production DB, or payment impact)
- Scope: 3 (two native trees from one spec)

## Multi-platform factor
platforms: [android, ios] → Scope = 3 → mode floor M3 applied.

## Decision: M3 (Plus)
## Adapted workflow: sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report → sdd-learnings
```

> Note: the mode sets the **depth** of each phase, not which phases run. Every
> ticket runs the full sequence above; only MX halts work.

---

### Phase 2 — Context (`/sdd-context T-001`)

**You type into Claude Code:**
```
/sdd-context T-001
```
*No extra input needed — the command reads the platform maps from Phase 0-B, `spec-pack.md`, then Greps source to verify real patterns.*

`context.md` reads the platform maps from Phase 0-B first, then verifies that
patterns **actually exist** in the codebase using Grep — no `[PLANNED]` here.

```markdown
# Context — T-001

## Correct examples in the codebase

### Android patterns
- CurrentWeatherViewModel.kt: @HiltViewModel + StateFlow<ViewState> + viewModelScope.launch
  → THIS is the standard for ForecastViewModel (verified by Read)
- WeatherApiService.kt: @GET + suspend fun + Retrofit interface
  → Add getForecast() using the same pattern

### iOS patterns
- CurrentWeatherViewModel.swift: @Observable final class + enum ViewState + @MainActor func
  → THIS is the standard for ForecastViewModel (verified by Read)
- WeatherAPIClient.swift: func fetch...() async throws → Model
  → Add fetchForecast() using the same pattern

## Allowed vs. forbidden patterns

### Android
- Allowed: StateFlow<ViewState> + @HiltViewModel + @Inject constructor
- Allowed: DataStore for cache (already used in CurrentWeather — reuse)
- Forbidden: LiveData (project has fully migrated to StateFlow)
- Forbidden: network calls from a @Composable

### iOS
- Allowed: @Observable class + @MainActor func load() async
- Allowed: UserDefaults for short-lived cache (same pattern as CurrentWeather)
- Forbidden: ObservableObject (replaced by @Observable in this codebase)
- Forbidden: URLSession directly from a SwiftUI View; DispatchQueue.main in new code

## Methods / classes that actually exist

### Android (verified with Grep)
- WeatherRepositoryImpl.fetchCurrentWeather() — exists ✓
- WeatherApiService.getCurrentWeather() — exists ✓ (need to add getForecast())
- StateFlow<ViewState> in CurrentWeatherViewModel — exists ✓

### iOS (verified with Grep)
- WeatherAPIClient.fetchCurrentWeather() — exists ✓
- @Observable CurrentWeatherViewModel — exists ✓
- ViewState enum (idle/loading/loaded/error) — exists ✓

## Parity gap check
Both platforms have implemented CurrentWeather. No parity debt affects T-001.
```

---

### Phase 3 — Plan (`/sdd-plan T-001`)

**You type into Claude Code:**
```
/sdd-plan T-001
```
*No extra input needed — the command reads `context.md` and `spec-pack.md` to produce impact analysis and implementation plan.*

`impl-plan.md` splits the HOW per native tree; the parity check confirms both
platforms start from the same baseline.

```markdown
# Implementation Plan — T-001

## Files to change

### Shared
| File | Reason | Add / Modify |
|---|---|---|
| docs/changes/T-001/spec-pack.md | SSOT for ForecastData contract | Modify |

### Android
| File | Reason | Add / Modify |
|---|---|---|
| android/.../data/remote/WeatherApiService.kt | Add getForecast() endpoint | Modify |
| android/.../data/remote/ForecastDto.kt | New DTO for /forecast response | Add |
| android/.../domain/model/ForecastData.kt | New domain model | Add |
| android/.../data/repository/WeatherRepositoryImpl.kt | Implement fetchForecast() | Modify |
| android/.../ui/forecast/ForecastViewModel.kt | New ViewModel (StateFlow<ViewState>) | Add |
| android/.../ui/forecast/ForecastScreen.kt | New Compose screen | Add |

### iOS
| File | Reason | Add / Modify |
|---|---|---|
| ios/.../Services/WeatherAPIClient.swift | Add fetchForecast() | Modify |
| ios/.../Models/ForecastData.swift | New model | Add |
| ios/.../Features/Forecast/ForecastViewModel.swift | New ViewModel (@Observable) | Add |
| ios/.../Features/Forecast/ForecastView.swift | New SwiftUI screen | Add |

## Cross-platform parity check
| Shared AC / behavior | Android impl | iOS impl | Identical? |
|---|---|---|---|
| AC-1 5 days from location | ForecastViewModel.loadForecast() | ForecastViewModel.loadForecast() @MainActor | Yes |
| AC-3 loading indicator | ViewState.Loading → CircularProgressIndicator | ViewState.loading → ProgressView | Yes |
| AC-4 network error + retry | ViewState.Error + retry button | ViewState.error + retry button | Yes |
| AC-5 30-minute cache | DataStore + timestamp check | UserDefaults + timestamp check | Yes (same threshold) |

## Mode check
Two native trees, no parity debt → M3 confirmed.
```

---

### Phase 4+5 — Implement (`/sdd-implement T-001`)

**You type into Claude Code:**
```
/sdd-implement T-001
```
*No extra input needed — the command reads `impl-plan.md`, presents the review checklist, and waits for your confirmation before writing any code. Stops at each Stop/Ask point.*

Each tree is extended from the **existing pattern**, in its own idiom.

**Android — `ForecastViewModel.kt` (new, follows CurrentWeatherViewModel standard)**
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

**iOS — `ForecastViewModel.swift` (new, follows CurrentWeatherViewModel standard)**
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

Both satisfy AC-1, AC-3, AC-4, AC-5 identically. Before self-review, the
**Cross-platform consistency** section of `review-checklist.md` is ticked: every
AC is observable on both platforms; ForecastData contract consumed identically.

---

### Phase 6 — Test (`/sdd-test T-001`)

**You type into Claude Code:**
```
/sdd-test T-001
```
*No extra input needed — the command reads `spec-pack.md` and the implemented source, then writes and runs tests against the AC matrix.*

The AC↔test matrix gains a **Platform** column; a contract test asserts the same
JSON fixture produces the same model on both clients.

```markdown
## AC ↔ test matrix
| AC | Platform | Test type | Test name | Priority |
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

**You type into Claude Code:**
```
/sdd-blackbox T-001
```
*No extra input needed — the command reads `spec-pack.md` and `test-results.md` to generate test cases from the user/QA perspective.*

Cases derived from the shared spec, each tagged with `Platform:`. Identical
observable behavior → one `Both` case.

```markdown
## AC coverage map
| AC | Platform | Happy path | Error | Cache | Status |
|---|---|---|---|---|---|
| AC-1,2 | Both | TC-1 | — | — | Pending |
| AC-4 | Both | — | TC-2 | — | Pending |
| AC-5 | Both | — | — | TC-3 | Pending |

### TC-1: Successful 5-day forecast load
AC: AC-1, AC-2
Platform: Both
Input: location permission granted, network available, open Forecast screen
Expected output: 5 rows; each has day name, high/low temperature (°C), description, icon.

### TC-2: Network failure — no cache
AC: AC-4
Platform: Both
Input: airplane mode, no cache, open Forecast screen
Expected output: error message + "Retry" button visible; no crash.

### TC-3: Cache still valid (< 30 minutes)
AC: AC-5
Platform: Both
Input: successful load → enable airplane mode → reopen within 30 minutes
Expected output: cached data shown; no spinner; no error.
```

---

### Phase 8 — Report (`/sdd-report T-001`)

**You type into Claude Code:**
```
/sdd-report T-001
```
*No extra input needed — the command synthesizes all produced artifacts into the final report.*

```markdown
# Final Report — T-001: 5-day forecast screen

## Acceptance Criteria — completion
| AC | Android | iOS | Notes |
|---|---|---|---|
| AC-1 Show 5 days | PASS | PASS | Both from the same ForecastData contract |
| AC-2 Per-day content | PASS | PASS | Day name, temp, description, icon present |
| AC-3 Loading | PASS | PASS | Platform-native progress indicator |
| AC-4 Network error + retry | PASS | PASS | Correct message + retry |
| AC-5 30-minute cache | PASS | PASS | Same threshold; DataStore vs UserDefaults |

## Cross-platform parity summary
All 5 ACs satisfied on both platforms. No intentional divergence in T-001.

## Accepted risks
- Different cache storage (DataStore vs UserDefaults) — accepted, this is platform idiom.

## Follow-up
- T-002: Day-detail screen (tap-through from the forecast list).
```

---

### Phase 9 — Learnings (`/sdd-learnings T-001`)

**You type into Claude Code:**
```
/sdd-learnings T-001
```
*No extra input needed — the command reads all ticket artifacts, proposes promotion candidates, and updates `failure-mode-index.md`.*

```markdown
# Promotion Candidates — T-001

## Patterns to promote → docs/standards/cross-platform.md
- **Reuse ViewModel pattern**: when adding a new feature to an existing codebase,
  clone the structure of the current ViewModel (StateFlow/ViewState on Android;
  @Observable/ViewState on iOS) rather than designing a new pattern. This
  preserves cross-feature consistency.
- **Platform map before context**: docs/architecture/platform-android-map.md and
  platform-ios-map.md must be read before filling context.md — prevents speccing
  patterns that do not exist in the real trees.

## Parity check result — T-001
No parity debt before T-001. Parity table in impl-plan.md: 4/4 behaviors
identical; 0 intentional divergences.

## Failure mode added → docs/maintenance/failure-mode-index.md
FM-08: Feature added to one platform only — parity debt accumulates across tickets.
  Cause: ticket scoped to one platform without recording the parity gap.
  Detection: §Parity Status in system-map.md; parity table in impl-plan.md.
  Fix: every multi-platform ticket must fill the parity table completely.
```

---

## Summary — what changes when the codebase already exists

| Greenfield (`[PLANNED]`) | Existing codebase (this walkthrough) |
|---|---|
| system-map.md all `[PLANNED]` | system-map.md shows real status + §Parity Status |
| Phase 0-B produces no platform maps | Phase 0-B produces `platform-android-map.md` + `platform-ios-map.md` |
| context.md designs patterns | context.md verifies patterns that already exist (Grep/Read) |
| source-map.md lists files to CREATE | source-map.md lists files to MODIFY + new files |
| Parity check: baseline from scratch | Parity check: verify current baseline before speccing |

Single-platform projects (`platforms:` with one entry) collapse every subsection
to one — the split costs nothing when you do not need it.
