# BVN-SDD — Quick Start (1 page)
# Brycen Viet Nam — Spec-Driven Development

> You **run commands** — no need to read all the documentation. Each command maps
> to a phase in SDD-Installation Pack V04.2 and writes a specific artifact file
> under `docs/changes/<TICKET-ID>/`.

## 1. Setup (once)

```bash
bvn-sdd check            # verify git + Claude Code are available
bvn-sdd init my-project  # create a new project (or: bvn-sdd init --here)
```

Choose a language when prompted: 1=Tiếng Việt / 2=English / 3=日本語

Then **open the project in Claude Code** and run `/sdd-phase0a` immediately.

## 2. Which path are you on?

| Step | Existing codebase | Empty / new repo |
|---|---|---|
| Install | `bvn-sdd init --here` in your existing repo | `git clone <empty-repo>`, then `bvn-sdd init --here` |
| Phase 0-A | Audits config + detects tech stack; records `project_type = existing` | Audits config; detects no source; records `project_type = new` |
| Phase 0-B | **Survey mode** — reads source, produces `system-map.md`, `source-inventory.md`, route/DB maps | **Green-field mode** — produces `system-map.md` as architecture decisions; all entries marked `[PLANNED]`; no source-inventory or test-map yet |
| Phase 2 (`/sdd-context`) | Verifies APIs/patterns exist in source | Designs planned APIs/patterns; marks all `[PLANNED]`; `source-map.md` lists files to **create** |
| Phase 3–9 | Plan and implement against existing code | Plan and implement code to be written from scratch |
| After first tickets | Rerun `/sdd-map` to update maps if needed | **Rerun `/sdd-map`** to replace `[PLANNED]` entries with confirmed source maps |

Both paths use the same commands — the commands detect the mode automatically from
`phase0-plan.md` (set by `/sdd-phase0a`).

## 3. Phases from SDD-Installation Pack V04.2

| Phase (V04.2) | Claude Code command | Produces | You do |
|---|---|---|---|
| **Phase 0-A** Safety Gate | `/sdd-phase0a` | `docs/maintenance/phase0/` + `docs/standards/automation/` — safety evidence, context policy | **Once per project.** Run right after `bvn-sdd init`, before `/sdd-map` |
| **Phase 0-B** Common Base / Source Intelligence | `/sdd-map` | `docs/architecture/` — source map, routes, APIs, DB schema, FE/BE contracts, test coverage | **Once per project.** Run before the first ticket |
| **Bootstrap** (before Phase 1) | `/sdd-new T-001` | `docs/changes/T-001/` + all blank artifact files | Set a ticket ID |
| **Phase 1** Investigation / Spec Pack | `/sdd-spec T-001` | `spec-pack.md`, `source-availability.md`, `open-issues.md` | Check ACs are correct; answer Open Issues |
| **Phase 1** Right-sizing | `/sdd-rightsize T-001` | `mode-decision.md` — mode M1–M5/MX + adapted workflow | **Important:** confirm mode before continuing |
| **Phase 2** Ticket Context / Rules | `/sdd-context T-001` | `context.md`, `source-map.md`, `ticket-rules.md` | Confirm patterns, real methods, forbidden patterns *(M1: keep brief, not skipped)* |
| **Phase 3** Impact Analysis / Impl Plan | `/sdd-plan T-001` | `impact-analysis.md`, `impl-plan.md` | Review FE/BE/DB impact scope and plan *(M1: keep brief, not skipped)* |
| **Phase 4+5** Review Checklist + Implementation / AI Review / Human Review | `/sdd-implement T-001` | code + `review-checklist.md`, `self-review.md` | Read AI-written code; check self-review; **fill `human-review.md`** then approve |
| **Phase 6** Test Plan / Test Code | `/sdd-test T-001` | `test-plan.md`, `test-results.md` | Verify tests actually PASS; read results |
| **Phase 7** Black-box Test / Test Data | `/sdd-blackbox T-001` | `blackbox-testcases.md`, `test-data.md`, `blackbox-review-checklist.md` | Verify behaviour from the user/QA perspective *(M1: a few key cases, not skipped)* |
| **Phase 8** Test Results / Final Report | `/sdd-report T-001` | `report.md` | Read the final report; confirm accepted risks and follow-ups |
| **Phase 9** Living Docs / Failure Mode Update | `/sdd-learnings T-001` | `promotion-candidates.md` + updates to `docs/maintenance/failure-mode-index.md` | Review promotion candidates; confirm what gets added to project standards |

**Utility** (Spec 32 — Long Context / Strategic Compact):
- `/sdd-compact T-001` → `strategic-compact.md` — session snapshot. Paste at the start of a new session to resume without re-reading everything.
- `/sdd-translate T-001` → `vi-review.md` — translates key decision artifacts (spec-pack, context, impact, impl-plan, test-plan, blackbox) into Vietnamese for dev review. **Internal use only — not for client delivery.**

## 4. Modes (decided by `/sdd-rightsize`)

> **The mode sets the DEPTH of each phase — it does NOT skip phases.** Every ticket,
> single- or multi-platform, runs the full phase sequence; M1 just keeps each
> artifact brief. Only **MX** halts work.

| Mode | Name | When | Depth at this mode |
|---|---|---|---|
| **M1** | Light | Text fix, config, small bug < 3 files | All phases run, artifacts kept brief (a one-line note if nothing unique); self-review only |
| **M2** | Standard | Normal feature, single service | Standard depth for every artifact |
| **M3** | Plus | FE+BE contract change, 10–30 files | Standard + focus on FE/BE contract; add on-demand deep artifacts (contract-map, codex-review) |
| **M4** | Heavy | Architecture change, DB migration | Full + heavy-source-analysis, security-review, rollback/migration plan, independent review |
| **M5** | Critical | Security patch, production incident | Maximum + mandatory human gate (threat model, test evidence, audit); escalate to human lead |
| **MX** | Stop | Requirements unclear or risk too high | Halt — resolve open issues first. The only mode that stops work |

## 5. Five non-negotiable rules

1. **Plan before code.** AI always presents a plan first; you approve before any edits happen.
2. **`spec-pack.md` is the single source of truth.** Unknowns go to `open-issues.md`. Never guess.
3. **Source code beats documents.** When a document (Excel/PDF) conflicts with source code, trust the source code.
4. **Never touch secrets.** Do not read or emit `.env`, keys, tokens, or PII.
5. **You are the final decision maker.** After AI self-reviews, you still read and approve.

## 6. When to STOP and escalate

- Source is missing or unreadable — cannot implement correctly
- Secrets or personal data are exposed
- Changes touch: payments, login/permissions, production DB migrations
- Source code and specification contradict each other
- AI is about to use a method or file that does not exist

## 7. Tips

- All results live in `docs/changes/<TICKET-ID>/` — open them any time.
- At the end of each command, AI tells you what to run next.
- Detailed rules: `.claude/rules/`. Universal stop/ask conditions: `.claude/rules/06-stop-conditions.md`. Project standards: `docs/standards/`.

## 8. Walkthrough Example

See **[EXAMPLE-cross-platform-weather-en.md](EXAMPLE-cross-platform-weather-en.md)** for a complete walkthrough of adding a feature to WeatherNow running on **both existing Android and iOS codebases** using BVN-SDD.

It shows, for every phase:
- The exact command you run
- The key artifact content the AI produces (realistic excerpts)
- The decision or approval you make before the next phase

Covers the full existing-codebase path: Phase 0-A → Phase 0-B (Survey Mode, `platform-android-map.md` + `platform-ios-map.md`) → T-001 Bootstrap → Spec → Rightsize → Context (verifying real patterns, no [PLANNED]) → Plan → Implement → Test → Black-box → Report → Learnings.

Single-platform walkthrough (greenfield, for comparison):
- **[EXAMPLE-ios-weather-en.md](EXAMPLE-ios-weather-en.md)** — iOS only, built from scratch (M2). Compare when no codebase exists yet.
