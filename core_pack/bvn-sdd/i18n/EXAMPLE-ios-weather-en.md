# Walkthrough: Building WeatherNow (iOS) from Scratch with BVN-SDD

**Scenario**: You are building a brand-new iOS weather app called *WeatherNow* — no existing codebase.  
This walkthrough shows every BVN-SDD command, the key artifact content each command produces,  
and the decision you make at each step.

> This is a **documentation example** — it shows what the artifacts look like, not real Swift code you must run.

**App overview**

| | |
|---|---|
| Platform | iOS 17+, Swift 5.9, SwiftUI |
| Architecture | MVVM + Clean Architecture |
| Ticket in this walkthrough | **T-001** — Current weather screen (location-based) |
| External API | OpenWeatherMap REST API |
| Dependencies | Swift Package Manager |

---

## 0. Setup

```bash
bvn-sdd check
# ✓ git 2.44.0
# ✓ claude (Claude Code)

git clone git@github.com:my-org/weathernow-ios.git
cd weathernow-ios

bvn-sdd init --here --lang en
# ✓ .claude/ created
# ✓ .bvn-sdd/ created
# ✓ docs/ created
```

Open the project in **Claude Code**, then immediately run:

```
/sdd-phase0a
```

---

## Phase 0-A — Safety Gate

> **Mechanism**: `/sdd-phase0a` loads generic "audit the safety environment" instructions. It has no idea what you are building. **You describe the app in the same message** so the AI records it in the artifacts and carries it forward into Phase 0-B.

**Message you type in Claude Code**:

```
/sdd-phase0a

Project: WeatherNow — brand new iOS weather app, no code yet.
Platform: iOS 17+, SwiftUI, MVVM + Clean Architecture, Swift Package Manager.
External API: OpenWeatherMap (REST, authenticated with an API key).
Offline: cache last successful response; show "Last updated X min ago" banner.
```

**What AI does**: Scans the repo — finds no source files — records `project_type = new`. Writes the information you provided into the output artifacts.

**Generated**: `docs/maintenance/phase0/phase0-plan.md`

```markdown
# Phase 0-A Safety Gate — WeatherNow iOS

## Project Type
new (greenfield) — no source files detected

## Tech Stack (from user description)
- iOS 17+, Swift 5.9, SwiftUI
- MVVM + Clean Architecture
- Swift Package Manager
- External API: OpenWeatherMap REST

## Safety Constraints Recorded
- DENY: read or emit .env, API keys, tokens, PII
- DENY: push to remote without explicit human approval
- DENY: destructive git operations (reset --hard, force-push) without confirmation
- ASK: before any file deletion
- ASK: before writing code that calls external APIs (confirm key-handling approach)

## Context Policy
- Source of truth priority: spec-pack.md > architecture docs > AI inference
- Summarise files > 500 lines instead of loading full content

## Open Questions for /sdd-map
1. Preferred module structure (Features/, Data/, Core/ or other)?
2. Cache staleness threshold — how old before showing a "stale" indicator?
3. Any UI design documents (Figma, mockups) available?
```

**You**: Read `phase0-plan.md`. Answer the remaining open questions.

**Your answer**:
> Features/Data/Core structure is fine. Stale after 30 minutes. No Figma yet. Continue.

---

## Phase 0-B — Source Intelligence (Green-field Mode)

**Command**: `/sdd-map`

**What AI does**: Reads `phase0-plan.md` (which now has the tech stack you provided in Phase 0-A) → detects `project_type = new` → runs in **green-field mode**. The architecture documents are built from the information you already gave — not guessed. No source to scan — produces architecture *decision* documents. Every entry is marked `[PLANNED]`.

**Generated**: `docs/architecture/system-map.md`

```markdown
# System Map — WeatherNow iOS
## Status: GREEN-FIELD — all entries [PLANNED]

## Layer Overview
| Layer | Technology | Status |
|---|---|---|
| Presentation | SwiftUI Views | [PLANNED] |
| State / ViewModel | @Observable (iOS 17) | [PLANNED] |
| Domain (Use Cases) | Pure Swift structs | [PLANNED] |
| Data (Repository) | Protocol + URLSession impl | [PLANNED] |
| Location | CoreLocation async wrapper | [PLANNED] |
| Cache | UserDefaults (simple JSON) | [PLANNED] |

## Module Structure [PLANNED]
WeatherNow/
├── App/
│   └── WeatherNowApp.swift          # Entry point, dependency injection root
├── Features/
│   └── CurrentWeather/
│       ├── View/                    # SwiftUI Views
│       ├── ViewModel/               # @Observable ViewModels
│       └── Model/                   # Domain models (WeatherData, etc.)
├── Data/
│   ├── Repository/                  # WeatherRepository protocol + implementation
│   ├── Network/                     # URLSession wrapper + Codable DTOs
│   └── Location/                    # CLLocationManager async wrapper
└── Core/
    └── Config/                      # AppConfig — reads keys from Info.plist

## Planned API Contracts
- WeatherRepository.fetchCurrentWeather(lat:lon:) async throws -> WeatherData
- LocationService.requestCurrentLocation() async throws -> CLLocationCoordinate2D

## External API [PLANNED]
- OpenWeatherMap: GET /data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric
- Auth: API key in query param (stored in Info.plist, NOT hardcoded in source)
```

**Generated**: `docs/architecture/api-contracts.md` *(all `[PLANNED]`)*  
**Generated**: `docs/architecture/db-schema.md` *(marks UserDefaults cache schema as `[PLANNED]`)*

**You**: Review the module structure. Adjust if needed. This document is the architectural blueprint all tickets will reference.

**Your confirmation**: Approved. Proceed to first ticket.

---

## T-001: Current Weather Screen

### Bootstrap

**Command you type** (short title is optional but helpful):

```
/sdd-new T-001 Current weather screen
```

```
✓ docs/changes/T-001/ created
✓ 20 blank artifact files ready:
    spec-pack.md, source-availability.md, open-issues.md
    mode-decision.md, context.md, source-map.md, ticket-rules.md
    impact-analysis.md, impl-plan.md, review-checklist.md
    self-review.md, human-review.md, test-plan.md, test-results.md
    blackbox-testcases.md, test-data.md, blackbox-review-checklist.md
    report.md, promotion-candidates.md, strategic-compact.md
```

---

### Phase 1 — Spec Pack

> **How does AI know the T-001 requirements?**  
> `/sdd-spec` only contains generic instructions — "write a spec-pack from the provided requirements". The ticket-specific requirements must come from **you, written directly below the command** in the same message. The AI combines your input with `docs/architecture/system-map.md` (from Phase 0-B) to produce a complete spec.

**Message you type in Claude Code** (command + requirements together):

```
/sdd-spec T-001

Requirements for T-001 — Current weather screen:

Goal: user opens app → sees weather at their current GPS location immediately.

Display: city name, temperature (°C), short description (e.g. "Partly cloudy"), weather icon.

Location permission flow:
- First launch → request location permission
- User denies → show "Location access required" + "Open Settings" button
- Permission granted → fetch weather automatically

Loading states:
- API in progress → loading indicator
- Network error + cache exists → show stale data + "Last updated X min ago" banner
- Network error + no cache → empty state "No connection" + Retry button

Interaction: pull-to-refresh to reload manually.

Out of scope for T-001: hourly/daily forecast, multiple locations, settings screen, push notifications.

Open question: API key storage — Info.plist (simple) or Keychain (secure)? Log in open-issues.
```

**What AI reads before writing** `spec-pack.md`:
1. `.claude/CLAUDE.md`, `.claude/rules/*` — project rules
2. `docs/architecture/system-map.md` — iOS/SwiftUI/MVVM architecture decided in Phase 0-B
3. **Your requirements written above** — the primary source for acceptance criteria and open issues

**Generated**: `docs/changes/T-001/spec-pack.md`

```markdown
# Spec Pack — T-001: Current Weather Screen

## Summary
Display current weather conditions for the user's GPS location.

## Acceptance Criteria
1. App requests location permission on first launch.
2. If permission denied → show "Location access required" message + "Open Settings" button.
3. On permission granted → fetch weather from OpenWeatherMap.
4. Display: city name, temperature (°C), weather description, weather icon.
5. Show loading indicator while fetching.
6. Show error state on network failure, with a "Retry" button.
7. Pull-to-refresh supported.
8. If cached data exists and network fails → show cache with "Last updated X min ago" banner.

## Out of Scope (T-001)
- Hourly / daily forecast
- Multiple saved locations
- Settings screen (units, theme)
- Push notifications

## Source Availability
- OpenWeatherMap API: documented at openweathermap.org/api — key required
- CoreLocation: Apple SDK, always available
- No existing Swift code to reuse
```

**Generated**: `docs/changes/T-001/open-issues.md`

```markdown
# Open Issues — T-001

OI-001: API key storage strategy
  Options: (a) Info.plist — simple but key visible in binary
           (b) Keychain — secure but complex setup for first ticket
  → Needs decision before Phase 4.

OI-002: Location accuracy threshold
  What happens if CLLocation.horizontalAccuracy > 5000m?
  → Show warning? Accept silently?

OI-003: Offline mode — empty state or cached data?
  If no network AND no cache → what does the user see?
```

**You**: Answer open issues before running `/sdd-rightsize`.

**Your answers** (write into `open-issues.md` or reply in chat):
- OI-001 → Info.plist for now. Document as tech debt AR-001. Migrate to proxy before App Store.
- OI-002 → Accept any accuracy. Show a subtle "Approximate location" label if > 2 km.
- OI-003 → Show "No connection — check your network" empty state with a Retry button.

---

### Phase 1 — Right-sizing

**Command**: `/sdd-rightsize T-001`

**Generated**: `docs/changes/T-001/mode-decision.md`

```markdown
# Mode Decision — T-001

## Assessment
- New project: no existing patterns to reuse, all layers created from scratch.
- Layers touched: UI (SwiftUI), ViewModel (@Observable), Repository (protocol),
  Network (URLSession), Location (CoreLocation), Cache (UserDefaults).
- Estimated new files: 12–14.
- Complexity: medium-high — async/await chains, error state machine, permission flow.

## Decision: Mode M3 (Plus)

Reason: Multiple architectural layers being established simultaneously.
The "front-end / back-end contract" (View ↔ ViewModel ↔ Repository) must be
defined explicitly in Phase 2–3 before any code is written.
Skipping Phases 2–3 would leave the implementation order undefined on a greenfield project.

## Adapted Workflow
All phases apply (no skips).
Phase 3 must produce a complete file list before Phase 4 begins.
```

**You**: Confirm M3. No objections → proceed.

---

### Phase 2 — Ticket Context & Rules

**Command**: `/sdd-context T-001`

**Generated**: `docs/changes/T-001/context.md`

```markdown
# Context — T-001

## Architecture Decisions in Effect (from system-map.md)
- Use @Observable (iOS 17 Observation framework). Do NOT use ObservableObject/Published.
- Repository pattern: protocol-first so ViewModels can be tested with mocks.
- Network: plain URLSession + async/await. No third-party networking library.
- Error handling: typed enums (WeatherError, LocationError), not generic Error strings.

## Dependency Injection Pattern
- ViewModel is initialised with its dependencies passed via init (no singletons).
- Root injection in WeatherNowApp.swift.

## Async / Threading Rules
- All @MainActor state mutations in ViewModel.
- NEVER use DispatchQueue.main.async in new code — use @MainActor instead.
- LocationService returns via async/await continuation.
```

**Generated**: `docs/changes/T-001/ticket-rules.md`

```markdown
# Ticket Rules — T-001

## Forbidden Patterns
- NEVER call URLSession directly from a SwiftUI View.
- NEVER hardcode the API key or base URL in source files.
- NEVER use force-unwrap (!) on Optional network response fields.

## Required Patterns
- Every async ViewModel function must set state = .loading before the await.
- All error cases must be caught and stored in ViewState, not crash or be silently ignored.
- Cache writes must happen after a successful network response, not on app launch.
```

**Generated**: `docs/changes/T-001/source-map.md`

```markdown
# Source Map — T-001 [ALL TO CREATE — greenfield]

| File | Purpose |
|---|---|
| WeatherNow/Core/Config/AppConfig.swift | Reads WEATHER_API_KEY from Info.plist |
| WeatherNow/Features/CurrentWeather/Model/WeatherData.swift | Domain model |
| WeatherNow/Data/Network/WeatherDTO.swift | Codable OpenWeatherMap response DTOs |
| WeatherNow/Data/Network/WeatherAPIClient.swift | URLSession wrapper + error mapping |
| WeatherNow/Data/Repository/WeatherRepository.swift | Protocol definition |
| WeatherNow/Data/Repository/WeatherRepositoryImpl.swift | Impl: APIClient + UserDefaults cache |
| WeatherNow/Data/Location/LocationService.swift | CoreLocation async/await wrapper |
| WeatherNow/Features/CurrentWeather/ViewModel/CurrentWeatherViewModel.swift | @Observable ViewModel |
| WeatherNow/Features/CurrentWeather/View/WeatherIconView.swift | Icon subcomponent |
| WeatherNow/Features/CurrentWeather/View/CurrentWeatherView.swift | Main screen SwiftUI View |
| WeatherNow/App/WeatherNowApp.swift | Entry point + DI root |
| WeatherNowTests/CurrentWeatherViewModelTests.swift | ViewModel unit tests |
| WeatherNowTests/WeatherAPIClientTests.swift | Network layer tests |
```

---

### Phase 3 — Impact Analysis & Implementation Plan

**Command**: `/sdd-plan T-001`

**Generated**: `docs/changes/T-001/impl-plan.md`

```markdown
# Implementation Plan — T-001

## Implementation Order (dependency-safe)
1. AppConfig.swift               — no dependencies
2. WeatherData.swift             — domain model, no dependencies
3. WeatherDTO.swift              — Codable DTOs, no dependencies
4. WeatherRepository.swift       — protocol only, no impl yet
5. LocationService.swift         — CoreLocation wrapper, standalone
6. WeatherAPIClient.swift        — uses AppConfig + WeatherDTO
7. WeatherRepositoryImpl.swift   — uses APIClient + UserDefaults
8. CurrentWeatherViewModel.swift — uses Repository + LocationService
9. WeatherIconView.swift         — pure UI component, no dependencies
10. CurrentWeatherView.swift      — uses ViewModel
11. WeatherNowApp.swift           — wires everything together
12. Tests                         — after implementation complete

## Key Risks
- RISK-01: Info.plist key storage — key visible in compiled binary.
  Accepted for dev phase. Must resolve before App Store (AR-001).
- RISK-02: NSLocationWhenInUseUsageDescription must be set in Info.plist
  via Xcode (AI cannot edit Xcode project file directly — human step required).
- RISK-03: No retry logic on network timeout — acceptable for M3 scope,
  add in a follow-up ticket.
```

**You**: Review the plan. Approve file list and order before AI writes any code.

**Your confirmation**:
> Approved. I'll add `NSLocationWhenInUseUsageDescription` to Info.plist in Xcode manually.

---

### Phase 4+5 — Implementation & Review

**Command**: `/sdd-implement T-001`

AI creates files in the order specified in `impl-plan.md`. Key excerpts:

---

**`WeatherRepository.swift`** — Protocol definition:
```swift
// WeatherNow/Data/Repository/WeatherRepository.swift
protocol WeatherRepository {
    func fetchCurrentWeather(lat: Double, lon: Double) async throws -> WeatherData
    func cachedWeather() -> CachedWeather?
}
```

---

**`CurrentWeatherViewModel.swift`** — Core state machine:
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
                state = .loaded(cached.weather)   // show stale data with banner
            } else {
                state = .error(error.localizedDescription)
            }
        }
    }
}
```

---

**`CurrentWeatherView.swift`** — Main screen:
```swift
// WeatherNow/Features/CurrentWeather/View/CurrentWeatherView.swift
struct CurrentWeatherView: View {
    @State private var viewModel: CurrentWeatherViewModel

    init(viewModel: CurrentWeatherViewModel) {
        _viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        Group {
            switch viewModel.state {
            case .idle:
                Color.clear.task { await viewModel.loadWeather() }
            case .loading:
                ProgressView("Fetching weather…")
            case .loaded(let weather):
                WeatherContentView(weather: weather)
            case .locationPermissionDenied:
                LocationDeniedView()
            case .error(let message):
                ErrorView(message: message) {
                    Task { await viewModel.loadWeather() }
                }
            }
        }
        .refreshable { await viewModel.loadWeather() }
    }
}
```

---

**Generated**: `docs/changes/T-001/self-review.md`

```markdown
# AI Self-Review — T-001

## Checklist
- [x] No API key hardcoded in source files (AppConfig reads from Info.plist)
- [x] @MainActor used for all state mutations — no DispatchQueue.main
- [x] Protocol-first repository — ViewModel testable with mock
- [x] All error states handled: location denied, network error, decode error
- [x] Loading state set before every await
- [x] Cache shown on network failure (OI-003 resolved)
- [ ] WARN: Info.plist key storage — accepted as AR-001 tech debt
- [ ] WARN: NSLocationWhenInUseUsageDescription — must be set manually in Xcode

## Items Requiring Human Attention
1. Set NSLocationWhenInUseUsageDescription in Info.plist (Xcode project file).
2. Add WEATHER_API_KEY value to Info.plist before running.
3. Confirm the "Last updated" banner displays correctly when showing cached data.
```

**You**: Read all generated Swift files. Then fill in `human-review.md`.

**`docs/changes/T-001/human-review.md`** (you write):
```markdown
# Human Review — T-001

Reviewer: @hv_ngan  
Date: 2026-06-01

## Verdict: APPROVED with notes

## Findings
1. ViewModel logic is clean. async/await chains are correct and readable.
2. Error enum covers all expected failure scenarios.
3. Cache-on-error behaviour matches OI-003 decision. ✓
4. NSLocationWhenInUseUsageDescription added in Xcode. ✓
5. WEATHER_API_KEY added to Info.plist. ✓

## Accepted Risks
- AR-001: API key in Info.plist — will migrate to server-side proxy before App Store.
```

---

### Phase 6 — Test Plan & Results

**Command**: `/sdd-test T-001`

**Generated**: `docs/changes/T-001/test-plan.md` (excerpt)

```markdown
# Test Plan — T-001

## Unit Tests: CurrentWeatherViewModel
| Test | Scenario | Expected Result |
|---|---|---|
| test_loadWeather_success | Location granted, API returns valid data | state == .loaded(weather) |
| test_loadWeather_locationDenied | LocationService throws .permissionDenied | state == .locationPermissionDenied |
| test_loadWeather_networkError_withCache | URLError thrown, cache exists | state == .loaded(cachedWeather) |
| test_loadWeather_networkError_noCache | URLError thrown, no cache | state == .error("...") |
| test_loadWeather_setsLoadingFirst | During async wait | state == .loading at first await |

## Unit Tests: WeatherAPIClient
| Test | Scenario | Expected Result |
|---|---|---|
| test_fetch_parsesValidJSON | Valid fixture JSON | Returns correct WeatherData |
| test_fetch_throws_on404 | HTTP 404 response | Throws WeatherError.notFound |
| test_fetch_throws_onDecodeError | Malformed JSON | Throws WeatherError.decodingFailed |
```

**Generated**: `docs/changes/T-001/test-results.md`

```markdown
# Test Results — T-001

Run date: 2026-06-01
All 8 tests PASSED ✓

Coverage:
  CurrentWeatherViewModel:  94%
  WeatherAPIClient:         88%
  LocationService:          71% (permission flow hard to unit-test — covered in black-box)
```

**You**: Run tests in Xcode (`Cmd + U`). Confirm they pass before proceeding.

---

### Phase 7 — Black-box Tests

**Command**: `/sdd-blackbox T-001`

**Generated**: `docs/changes/T-001/blackbox-testcases.md`

```markdown
# Black-box Test Cases — T-001

## TC-001: First Launch — Permission Dialog
Precondition: Fresh install (no prior permission).
Steps: Launch app.
Expected: iOS system permission dialog appears with the usage description text.
Pass/Fail: [ ]

## TC-002: Location Permission Denied
Precondition: Deny location in dialog or in Settings.
Steps: Open app.
Expected: "Location access required" message visible.
         "Open Settings" button opens iOS Settings → WeatherNow.
Pass/Fail: [ ]

## TC-003: Successful Weather Load
Precondition: Location permission granted, network available.
Steps: Launch app.
Expected: City name, temperature (°C), description, icon all visible.
         No spinner. No error message.
Pass/Fail: [ ]

## TC-004: Network Offline — No Cache
Precondition: Enable Airplane Mode. Clear app data (fresh install).
Steps: Launch app.
Expected: "No connection — check your network" empty state + Retry button.
Pass/Fail: [ ]

## TC-005: Network Offline — With Cache
Precondition: Load weather successfully once. Enable Airplane Mode.
Steps: Pull to refresh.
Expected: Stale weather data shown. "Last updated X min ago" banner visible.
Pass/Fail: [ ]

## TC-006: Pull-to-Refresh
Precondition: Weather loaded successfully.
Steps: Pull down on the screen.
Expected: Loading indicator appears, then weather refreshes with updated data.
Pass/Fail: [ ]

## TC-007: Low Accuracy Location
Precondition: Force low-accuracy in simulator (City-level accuracy).
Steps: Load weather.
Expected: Weather displayed. "Approximate location" label visible.
Pass/Fail: [ ]
```

**You**: Test manually on iOS Simulator and/or device. Mark each case pass or fail.

---

### Phase 8 — Final Report

**Command**: `/sdd-report T-001`

**Generated**: `docs/changes/T-001/report.md`

```markdown
# Final Report — T-001: Current Weather Screen

Status: COMPLETE ✓
Completed: 2026-06-01

## Summary
Implemented the current weather screen for WeatherNow iOS from scratch.
Full MVVM + Clean Architecture foundation established.
13 Swift files created. All unit tests pass (8/8). Black-box tests pass (7/7).

## Architecture Established (reusable for future tickets)
- @Observable ViewModel pattern with typed ViewState enum
- Repository protocol + URLSession implementation (mockable in tests)
- CoreLocation async/await wrapper
- UserDefaults cache layer with staleness metadata
- Dependency injection at app entry point

## Accepted Risks
- AR-001: API key in Info.plist — migrate to server-side proxy before App Store (T-003).

## Recommended Follow-up Tickets
- T-002: Hourly Forecast Screen (reuses WeatherRepository, LocationService)
- T-003: API Key Server Proxy (resolve AR-001 before any public release)
- T-004: Home Screen Widget (current temperature widget extension)
- T-005: Add retry logic on network timeout
```

---

### Phase 9 — Learnings & Living Docs

**Command**: `/sdd-learnings T-001`

**Generated**: `docs/changes/T-001/promotion-candidates.md`

```markdown
# Promotion Candidates — T-001

## PC-001: @Observable ViewModel Pattern
→ Promote to: docs/standards/coding-conventions.md
Content: All ViewModels use @Observable + typed ViewState enum.
State mutations via @MainActor only. Dependencies injected via init.

## PC-002: Repository Protocol Pattern
→ Promote to: docs/standards/coding-conventions.md
Content: All data sources defined as Swift protocols.
Concrete implementations injected — never instantiated inside ViewModels.

## PC-003: API Key in Info.plist (Failure Mode)
→ Promote to: docs/maintenance/failure-mode-index.md
Failure: API keys in Info.plist are extractable from the app binary.
Resolution: Use a server-side proxy endpoint before any public distribution.
Priority: HIGH — must resolve before App Store submission.
```

**You**: Approve which candidates to promote. AI updates `docs/standards/` and `docs/maintenance/failure-mode-index.md` with the confirmed patterns.

---

## What Changes After T-001

After the first ticket is done, run `/sdd-map` again to replace `[PLANNED]` entries with real source paths:

```
/sdd-map
```

The architecture docs are now updated with:
- Actual file paths (no longer `[PLANNED]`)
- Real method signatures (confirmed from source)
- Test coverage map

When you start **T-002: Hourly Forecast**, Phase 2 (`/sdd-context`) will find real patterns in source code to reference, instead of planning from scratch.

---

## Summary: Greenfield Project Key Points

| Point | What to watch for |
|---|---|
| Phase 0-B output is `[PLANNED]` | That is correct — architecture decisions, not source scan |
| Mode M3 is common for ticket 1 | Multiple layers created at once → always needs Phases 2+3 |
| Human steps AI cannot do | Add strings to Info.plist, set Xcode project settings |
| Re-run `/sdd-map` after T-001 | Converts planned architecture to real source map for T-002+ |
| AR-001 accepted risk | Must be tracked and resolved before any public release |
