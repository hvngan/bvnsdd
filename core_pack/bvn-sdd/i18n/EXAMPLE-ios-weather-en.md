# Example: Building WeatherNow (iOS) from Scratch

**Scenario**: You are building a brand-new iOS weather app called *WeatherNow* — no existing codebase.

| | |
|---|---|
| Platform | iOS 17+, Swift 5.9, SwiftUI |
| Status | Greenfield — no code yet |
| Ticket | **T-001** — Current weather screen (location-based) |

Compare with `EXAMPLE-cross-platform-weather-en.md` to see the difference when a codebase already exists.

---

## 0. Setup

```bash
bvn-sdd check
git clone git@github.com:my-org/weathernow-ios.git
cd weathernow-ios
bvn-sdd init --here --lang en
```

Open the project in **Claude Code**.

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**Run** — describe the project directly below the command (required since no source exists):
```
/sdd-phase0a

Project: WeatherNow — brand-new iOS weather app, no code yet.
Platform: iOS 17+, SwiftUI, MVVM + Clean Architecture, Swift Package Manager.
External API: OpenWeatherMap (REST, authenticated with an API key).
Offline: cache last successful response; show "Last updated X min ago" banner.
```

**You need to:**
- Read `docs/maintenance/phase0/phase0-plan.md`
- Answer any open questions AI raises (module structure, cache staleness threshold, etc.)

---

## Phase 0-B — Source Intelligence — Green-field mode (`/sdd-map`)

**Run:**
```
/sdd-map
```

**You need to:**
- Read `docs/architecture/system-map.md` — this is an **architecture decision document**, all entries marked `[PLANNED]`
- Adjust the module structure if needed — this file is the blueprint for every subsequent ticket
- Approve before starting the first ticket

---

## Bootstrap (`/sdd-new T-001`)

**Run:**
```
/sdd-new T-001 Current weather screen
```

---

## Phase 1 — Spec Pack (`/sdd-spec T-001`)

**Run** — paste original requirements directly below the command:
```
/sdd-spec T-001

[Paste requirements from Jira / email / brief here]
```
This is the only phase where you need to provide manual input.

**You need to:**
- Verify ACs are correct and complete
- Answer all items in `open-issues.md` before moving to the next step

---

## Phase 1 — Right-sizing (`/sdd-rightsize T-001`)

**Run:**
```
/sdd-rightsize T-001
```

**You need to:**
- Read `mode-decision.md`, confirm the mode (M1–M5)
- The first ticket of a greenfield project is typically M2–M3 because multiple layers are created at once

---

## Phase 2 — Context (`/sdd-context T-001`)

**Run:**
```
/sdd-context T-001
```

**You need to:**
- Confirm the conventions and patterns being established (marked `[PLANNED]` — no real code yet)
- Check that `source-map.md` lists files to **create**, not files to modify

---

## Phase 3 — Impact & Plan (`/sdd-plan T-001`)

**Run:**
```
/sdd-plan T-001
```

**You need to:**
- Read the implementation order in `impl-plan.md` (are dependencies in the right order?)
- Note any manual steps AI cannot perform (e.g. adding a key to Info.plist in Xcode)
- **Explicitly approve** — AI will not write code until you confirm

---

## Phase 4+5 — Implement (`/sdd-implement T-001`)

**Run:**
```
/sdd-implement T-001
```

**You need to:**
- Approve the review checklist before AI starts coding (AI will pause and wait)
- Perform manual steps in parallel (e.g. adding Info.plist strings in Xcode)
- Read all code AI has written (diff)
- Fill in `human-review.md` — AI must not fill this file

---

## Phase 6 — Test (`/sdd-test T-001`)

**Run:**
```
/sdd-test T-001
```

**You need to:**
- Run: `xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,...'`
- Confirm all tests PASS before continuing

---

## Phase 7 — Black-box Test (`/sdd-blackbox T-001`)

**Run:**
```
/sdd-blackbox T-001
```

**You need to:**
- Manually test each case in `blackbox-testcases.md` on the iOS Simulator or a real device
- Mark Pass / Fail for each case
- Fill in required fixtures in `test-data.md`

---

## Phase 8 — Final Report (`/sdd-report T-001`)

**Run:**
```
/sdd-report T-001
```

**You need to:**
- Read `report.md`, confirm accepted risks and follow-up tickets

---

## Phase 9 — Learnings (`/sdd-learnings T-001`)

**Run:**
```
/sdd-learnings T-001
```

**You need to:**
- Read `promotion-candidates.md`
- Confirm which patterns go into `docs/standards/` and which failure modes go into `failure-mode-index.md`

---

## After T-001: update the architecture maps

**Re-run `/sdd-map`** to replace `[PLANNED]` entries with real source paths:
```
/sdd-map
```

From T-002 onward, Phase 2 will find real patterns in the source to reference instead of designing from scratch.
