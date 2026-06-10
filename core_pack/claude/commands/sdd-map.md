---
description: BVN-SDD Phase 0-B — map the codebase before working on tickets.
argument-hint: (no arguments)
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are performing **Source Intelligence** (BVN-SDD Phase 0-B) for this project.
Run this once per project, before the first ticket.

Also read `.bvn-sdd/config.yml` (platforms field).

**Multi-platform.** If `platforms:` lists more than one platform, structure
`system-map.md` as a shared-spec/contract layer plus one layer per native tree
(e.g. `android/`, `ios/`). In SURVEY MODE, inventory each native tree separately;
in GREEN-FIELD MODE, mark each platform layer `[PLANNED]`. See the `## Platforms`
and `## Shared contract layer` sections of the `system-map.md` stub.

---

## Detect mode before starting

Check `docs/maintenance/phase0/phase0-plan.md` for the `Project Type` field set
by `/sdd-phase0a`. If the file does not exist, detect directly:
- Use Glob for source files outside scaffolding (`src/**`, `*.py`, `*.ts`, etc.,
  excluding `.bvn-sdd/`, `.claude/`, `docs/`, `node_modules/`, `.git/`)
- Source files found → **SURVEY MODE** (existing codebase)
- No source files → **GREEN-FIELD MODE** (new project)

---

## SURVEY MODE — existing codebase

Goal: give future phases a map so the AI never gets lost. Do a *shallow* survey
of the repository — do not read every file.

**Plan first.** State: goal, directories to sample, files to create/update, Stop/Ask points. Proceed once acknowledged.

Then produce/update under `docs/architecture/`:
- `system-map.md` — high-level components and how they relate
- `source-inventory.md` — key files/directories and their purpose
- As applicable: `entrypoint-map.md`, `route-api-map.md`, `service-layer-map.md`,
  `repository-db-map.md`, `data-flow-map.md`, `external-interface-map.md`,
  `fe-be-contract-map.md` (FE/BE API contracts and DTO shapes),
  `test-map.md` (existing test coverage per layer — unit / integration / e2e)

**Multi-platform survey.** When `platforms:` lists more than one platform, add these files in addition to the standard maps:
- `docs/architecture/platform-android-map.md` — Android tree survey: top-level package structure; architecture pattern (MVVM/MVI/Clean); DI framework; state management (StateFlow/LiveData/Compose State); navigation library; `minSdkVersion`; key ViewModels and Repositories with their file locations; existing test infrastructure (test runner, mocking library, UI test framework).
- `docs/architecture/platform-ios-map.md` — iOS tree survey: module/directory structure; UI framework (UIKit/SwiftUI/mixed); architecture pattern; state management (@Observable/ObservableObject/Combine/async-await); navigation pattern; deployment target; key ViewModels/Services with their file locations; existing test infrastructure (XCTest, XCUITest).

In `system-map.md`, add a **Parity Status** section: list features fully implemented on both platforms (parity intact), features present on only one platform (parity debt), and planned features not yet on either. Parity debt items are candidates for future tickets — do not silently include them in unrelated ticket scope.

Note in `fe-be-contract-map.md` which contracts are consumed by both clients vs. only one.

Rules: record what you read and could not read; mark inferences as Assumptions;
never open secrets/.env/PII. When done, summarize the map and list which
`docs/standards/*` files should be created or updated (coding, testing, security,
logging) based on patterns observed in the codebase.

---

## GREEN-FIELD MODE — new project (no source yet)

Goal: document architecture decisions so the first tickets have a shared blueprint
to build toward.

**Plan first.** State: technology choices to confirm, components/boundaries, files to create, Stop/Ask points. Proceed once acknowledged.

Then create under `docs/architecture/`:
- `system-map.md` — proposed components and their responsibilities; key interfaces
  between components; deployment topology; technology choices (language, framework,
  DB, external services). **Mark every entry `[PLANNED]`.**
- `entrypoint-map.md` — planned entry points (API gateway, CLI, web server, etc.)
  with responsibilities. **Mark every entry `[PLANNED]`.**

Do NOT create `source-inventory.md`, `test-map.md`, or other source-derived maps
— there is nothing to inventory yet.

Mark a note at the top of each file:
```
> [GREEN-FIELD] No source code exists yet. All entries are architecture decisions,
> not observations. Re-run /sdd-map after the first tickets to replace with
> confirmed source maps.
```

List which `docs/standards/*` files should be created based on the chosen stack
(coding conventions, testing approach, security, logging). When done, tell the
user to run `/sdd-new` to start the first ticket.
