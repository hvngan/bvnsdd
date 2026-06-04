# Cross-Platform Standard (Android + iOS from one shared spec)

> How BVN-SDD delivers two native apps from a single source of truth. This
> standard applies only when `.bvn-sdd/config.yml` `platforms:` lists more than
> one platform. For a single platform the splits collapse and this doc applies
> trivially.

## Model

**Shared spec, two separate native codebases.**

- The ticket's `spec-pack.md` is the single source of truth for the **WHAT**
  (acceptance criteria, input/output, validation, security, the client/service
  contract). It stays platform-neutral — it never names Kotlin, Swift, Compose,
  or SwiftUI.
- **Android** (Kotlin / Jetpack Compose) and **iOS** (Swift / SwiftUI) are two
  fully separate native trees. Each implements the **HOW** in its own idiom.
- This is explicitly **not** Kotlin Multiplatform (no shared code module) and
  **not** a backend-only SSOT. The shared thing is the *spec*, not compiled code.

## Decision rule — Shared vs. platform-specific

Ask: *"Is this the WHAT/contract, or is it how one OS renders / stores / threads
it?"*

| Belongs in **Shared** | Belongs in **platform-specific** |
|---|---|
| Acceptance criteria, business rules | UI framework usage (Compose vs SwiftUI) |
| Validation rules & error semantics | Navigation patterns |
| Client/Service contract (fields, types, error codes) | Local storage engine (Room vs Core Data / UserDefaults) |
| Shared data model | Permission request UX |
| User-facing message text & meaning | Build config, dependencies, threading idioms |

Rule of thumb: **WHAT or contract → Shared; how an OS renders/stores/threads it →
platform-specific.**

## Ticket model

**One ticket, split sections** (single traceability thread):

- One shared `spec-pack.md` per ticket — no parent/child sub-tickets.
- The downstream artifacts carry `### Shared` / `### Android` / `### iOS`
  subsections: `context.md`, `source-map.md`, `impl-plan.md`,
  `impact-analysis.md`, `test-plan.md`, `blackbox-testcases.md`.
- `impl-plan.md` includes a **Cross-platform parity check** table; the
  `review-checklist.md` includes a **Cross-platform consistency** section.

## Repo layout

Default — a monorepo so the single spec and both trees live together:

```
<repo>/
  android/          # Kotlin / Jetpack Compose native tree
  ios/              # Swift / SwiftUI native tree
  docs/changes/     # one ticket folder per feature (the shared spec lives here)
  docs/architecture/, docs/standards/, .bvn-sdd/, .claude/
```

Two-repos alternative: if Android and iOS must live in separate repositories,
keep the BVN-SDD scaffold (and therefore `docs/changes/<TICKET>/spec-pack.md`)
in a third shared/spec repo, and have each platform repo reference the same
ticket ID. The single-spec rule is unchanged; only the file layout differs.

## Parity expectations

- Every shared AC must be **observably satisfied on every in-scope platform**.
- The shared contract and data model are **never forked** per platform — both
  clients consume them identically.
- **Intentional divergence** (e.g. a platform-specific permission flow) is
  allowed, but must be recorded as an explicit entry in `open-issues.md` and in
  the `impl-plan.md` parity table — never left implicit.
- Each platform follows its **native idioms**; no cross-contamination (Compose
  patterns must not leak into the SwiftUI tree, and vice versa).

## Mode impact

Delivering two native trees from one spec raises baseline scope. `/sdd-rightsize`
treats multiple `platforms:` as a Scope = 3 contributor and applies a **mode
floor of M3**.

## Single-platform note

If `platforms:` lists one platform, keep only that platform's subsection in each
artifact and delete the others. Every split degrades to a single coherent
section, and this standard imposes no extra work.
