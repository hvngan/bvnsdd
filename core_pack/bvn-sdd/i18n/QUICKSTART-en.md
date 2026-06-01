# BVN-SDD — Quick Start (1 page)

> You **run commands** — no need to read all the documentation. Each command
> produces a result file under `docs/changes/<TICKET-ID>/`.

## 1. Setup (once)

```bash
bvn-sdd check            # verify git + Claude Code are available
bvn-sdd init my-project  # create a new project (or: bvn-sdd init --here)
```

Then **open the project in Claude Code**.

## 2. Workflow for each ticket

| Step | Type in Claude Code | Produces | You do |
|---|---|---|---|
| 0 | `/sdd-map` | source map (`docs/architecture/`) | **Once per project.** Lets AI understand the codebase |
| 1 | `/sdd-new T-001` | ticket folder + blank artifacts | Set a ticket ID (e.g. `T-001`) |
| 2 | `/sdd-spec T-001` | `spec-pack.md` (specification) | Check ACs are correct; answer Open Issues |
| 2B | `/sdd-rightsize T-001` | `mode-decision.md` — mode M1–M5 | **Important:** confirm mode & adapted workflow |
| 3 | `/sdd-context T-001` | `context.md`, `source-map.md` | Confirm patterns/APIs _(skip for M1)_ |
| 4 | `/sdd-plan T-001` | `impact-analysis.md`, `impl-plan.md` | Review impact scope & plan _(skip for M1)_ |
| 5 | `/sdd-implement T-001` | code + `self-review.md` | Read AI-written code; approve |
| 6 | `/sdd-test T-001` | `test-plan.md`, `test-results.md` | Verify tests actually PASS |
| 7 | `/sdd-blackbox T-001` | `blackbox-testcases.md` | Verify behaviour from the user's perspective _(skip for M1)_ |
| 8 | `/sdd-report T-001` | `report.md` | Read the final report; sign off |

**Modes (decided by `/sdd-rightsize`):**
- **M1 Light** — Bug fix, text change, config: run steps 2 → 5 → 6 → 8. Skip 2B, 3, 4, 7.
- **M2 Standard** — Normal feature: run all steps.
- **M3+ Heavy** — Architecture/DB/multi-service: run all steps + security review.

**Utility command (use any time):**
- `/sdd-compact T-001` → creates `strategic-compact.md` — session snapshot for resuming another day.

## 3. Five non-negotiable rules

1. **Plan before code.** AI always presents a plan first; you approve before any edits happen.
2. **`spec-pack.md` is the single source of truth.** Never add requirements not in it. Unknowns
   go to `open-issues.md` — **never guess**.
3. **Source code beats documents.** When a document (Excel/PDF) conflicts with source code,
   trust the source code.
4. **Never touch secrets.** Do not read or emit `.env`, keys, tokens, passwords, or PII.
5. **You are the final reviewer.** After AI self-reviews, you still read and approve.

## 4. When to STOP and escalate

- Missing source / DB definitions needed to implement correctly
- Secrets or personal data exposed
- Changes touch: payments, login/permissions, production DB migrations

## 5. Tips

- All results live in `docs/changes/<TICKET-ID>/` — open them any time.
- Forgot the next step? At the end of each command, AI tells you what to run next.
- Detailed rules: `.claude/rules/`. Project standards: `docs/standards/`.
