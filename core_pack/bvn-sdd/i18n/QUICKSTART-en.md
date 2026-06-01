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

Then **open the project in Claude Code**.

## 2. Phases from SDD-Installation Pack V04.2

| Phase (V04.2) | Claude Code command | Produces | You do |
|---|---|---|---|
| **Phase 0-B** Common Base / Source Intelligence | `/sdd-map` | `docs/architecture/` — source map, routes, APIs, DB schema | **Once per project.** Run before the first ticket |
| **Bootstrap** (before Phase 1) | `/sdd-new T-001` | `docs/changes/T-001/` + all blank artifact files | Set a ticket ID |
| **Phase 1** Investigation / Spec Pack | `/sdd-spec T-001` | `spec-pack.md`, `source-availability.md`, `open-issues.md` | Check ACs are correct; answer Open Issues |
| **Phase 1** Right-sizing | `/sdd-rightsize T-001` | `mode-decision.md` — mode M1–M5/MX + adapted workflow | **Important:** confirm mode before continuing |
| **Phase 2** Ticket Context / Rules | `/sdd-context T-001` | `context.md`, `source-map.md` | Confirm patterns, real methods, forbidden patterns *(skip for M1)* |
| **Phase 3** Impact Analysis / Impl Plan | `/sdd-plan T-001` | `impact-analysis.md`, `impl-plan.md` | Review FE/BE/DB impact scope and plan *(skip for M1)* |
| **Phase 4+5** Review Checklist + Implementation / AI Review / Human Review | `/sdd-implement T-001` | code + `review-checklist.md`, `self-review.md` | Read AI-written code; check self-review; approve |
| **Phase 6** Test Plan / Test Code | `/sdd-test T-001` | `test-plan.md`, `test-results.md` | Verify tests actually PASS; read results |
| **Phase 7** Black-box Test / Test Data | `/sdd-blackbox T-001` | `blackbox-testcases.md` | Verify behaviour from the user/QA perspective *(skip for M1)* |
| **Phase 8** Test Results / Final Report | `/sdd-report T-001` | `report.md` | Read the final report; confirm accepted risks and follow-ups |

**Utility** (Spec 32 — Long Context / Strategic Compact):
- `/sdd-compact T-001` → `strategic-compact.md` — session snapshot. Paste at the start of a new session to resume without re-reading everything.

## 3. Modes (decided by `/sdd-rightsize`)

| Mode | Name | When | Commands skipped |
|---|---|---|---|
| **M1** | Light | Text fix, config, small bug < 3 files | context, plan, blackbox |
| **M2** | Standard | Normal feature, single service | None |
| **M3** | Plus | FE+BE contract change, 10–30 files | None |
| **M4** | Heavy | Architecture change, DB migration | None + security review added |
| **M5** | Critical | Security patch, production incident | Escalate to human lead immediately |
| **MX** | Stop | Requirements unclear or risk too high | Halt — resolve open issues first |

## 4. Five non-negotiable rules

1. **Plan before code.** AI always presents a plan first; you approve before any edits happen.
2. **`spec-pack.md` is the single source of truth.** Unknowns go to `open-issues.md`. Never guess.
3. **Source code beats documents.** When a document (Excel/PDF) conflicts with source code, trust the source code.
4. **Never touch secrets.** Do not read or emit `.env`, keys, tokens, or PII.
5. **You are the final decision maker.** After AI self-reviews, you still read and approve.

## 5. When to STOP and escalate

- Source is missing or unreadable — cannot implement correctly
- Secrets or personal data are exposed
- Changes touch: payments, login/permissions, production DB migrations
- Source code and specification contradict each other
- AI is about to use a method or file that does not exist

## 6. Tips

- All results live in `docs/changes/<TICKET-ID>/` — open them any time.
- At the end of each command, AI tells you what to run next.
- Detailed rules: `.claude/rules/`. Project standards: `docs/standards/`.
