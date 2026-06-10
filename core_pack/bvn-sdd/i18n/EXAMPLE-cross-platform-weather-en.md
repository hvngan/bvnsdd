# Example: Adding a forecast screen to WeatherNow (existing Android + iOS codebase)

**Scenario**: *WeatherNow* already exists on both Android and iOS with a working current weather screen.
You are adding a **5-day forecast screen** (T-001) following BVN-SDD.

| | |
|---|---|
| Platforms | Android (Kotlin, Compose, Hilt) **+** iOS (Swift, SwiftUI, async/await) |
| Status | Existing codebase — current weather screen already working |
| Repo | monorepo: `android/` + `ios/` + `docs/` |

Compare with `EXAMPLE-ios-weather-en.md` to see the difference when no codebase exists yet.

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
  android: "Kotlin, Jetpack Compose, Hilt, StateFlow"
  ios: "Swift, SwiftUI, @Observable, async/await"
```

Open the project in **Claude Code**.

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**Run:**
```
/sdd-phase0a
```
No argument needed — the command reads project structure and `config.yml` automatically.

**You need to:**
- Read `docs/maintenance/phase0/phase0-review.md`
- Sign off any pending items

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

**Run:**
```
/sdd-map
```

**You need to:**
- Read `docs/architecture/system-map.md` — check §Parity Status (are both platforms at the same baseline?)
- Read `docs/architecture/platform-android-map.md` and `platform-ios-map.md`
- Correct any misunderstandings before creating the first ticket

---

## Bootstrap (`/sdd-new T-001`)

**Run:**
```
/sdd-new T-001 5-day forecast screen
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
- Ensure the spec is platform-neutral (WHAT, not HOW)
- Answer all items in `open-issues.md` before moving to the next step

---

## Phase 1 — Right-sizing (`/sdd-rightsize T-001`)

**Run:**
```
/sdd-rightsize T-001
```

**You need to:**
- Read `mode-decision.md`, confirm the mode (M1–M5)
- Note: the mode sets the **depth** of each phase — no phases are skipped

---

## Phase 2 — Context (`/sdd-context T-001`)

**Run:**
```
/sdd-context T-001
```

**You need to:**
- Confirm patterns and methods actually exist in the codebase
- Check the parity gap — if one platform is missing a required baseline feature, resolve it before continuing

---

## Phase 3 — Impact & Plan (`/sdd-plan T-001`)

**Run:**
```
/sdd-plan T-001
```

**You need to:**
- Read `impact-analysis.md` and `impl-plan.md`
- Check the cross-platform parity table (do Android and iOS produce identical behaviour?)
- **Explicitly approve** — AI will not write code until you confirm

---

## Phase 4+5 — Implement (`/sdd-implement T-001`)

**Run:**
```
/sdd-implement T-001
```

**You need to:**
- Approve the review checklist before AI starts coding (AI will pause and wait)
- Read all code AI has written (diff)
- Fill in `human-review.md` — AI must not fill this file

---

## Phase 6 — Test (`/sdd-test T-001`)

**Run:**
```
/sdd-test T-001
```

**You need to:**
- Run tests on both platforms and confirm PASS
- Android: `./gradlew :app:testDebugUnitTest`
- iOS: `xcodebuild test -scheme WeatherNow -destination '...'`

---

## Phase 7 — Black-box Test (`/sdd-blackbox T-001`)

**Run:**
```
/sdd-blackbox T-001
```

**You need to:**
- Manually test each case in `blackbox-testcases.md` on **both platforms**
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

## Key differences vs. greenfield

| Existing codebase (this example) | Greenfield |
|---|---|
| Phase 0-A: no project description needed — AI reads source | Phase 0-A: must describe the project in the message |
| Phase 0-B: Survey mode — reads real source | Phase 0-B: Green-field mode — all entries `[PLANNED]` |
| context.md: verifies patterns that already exist | context.md: designs new patterns, marked `[PLANNED]` |
| source-map.md: files to modify + new files | source-map.md: files to create from scratch |
| Parity check: verify both platforms share the same baseline | No parity debt at the start |
| After first ticket: no need to re-run `/sdd-map` | After first ticket: **re-run `/sdd-map`** to replace `[PLANNED]` |
