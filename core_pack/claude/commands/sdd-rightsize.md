---
description: BVN-SDD Phase 1-B — formalise the mode decision and adapt the workflow.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob
---

You are the SDD mode selector for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read first: this ticket's `spec-pack.md` (especially section 15 Complexity
Classification) and `open-issues.md`.

**Plan first** (goal, files to read, files to update, Stop/Ask points, plan).
Do not edit until acknowledged.

Goal: produce a formal `mode-decision.md` that records the chosen operating mode
and the adapted workflow — so every subsequent phase knows what to skip or
escalate.

## Mode definitions

| Mode | Name | Typical trigger |
|---|---|---|
| M1 | Light | Bug fix, config change, text update, < 3 files, fully reversible |
| M2 | Standard | Normal feature, single service, reversible with effort |
| M3 | Plus | FE + BE impact, API contract change, 10–30 files |
| M4 | Heavy | Architectural change, multi-service, DB migration, major refactor |
| M5 | Critical | Security patch, production incident, data-loss risk |
| MX | Stop | Requirements unclear OR risk too high — do not proceed |

## Scoring matrix

Score each criterion 1–3, then sum:

| Criterion | 1 | 2 | 3 |
|---|---|---|---|
| **Reversibility** | Rollback in minutes | Rollback with moderate effort | Hard to reverse / data destructive |
| **Uncertainty** | Well-understood scope | Some unknowns, risks identified | Many unknowns, requirements unclear |
| **Risk** | No prod / security / data impact | Moderate impact | High prod / security / data impact |
| **Scope** | < 3 files, 1 service | < 10 files or 2 services | Many files or many services |

Score → Mode:
- 4–5 → M1 Light
- 6–7 → M2 Standard
- 8–9 → M3 Plus
- 10–11 → M4 Heavy
- 12 → M5 Critical
- Uncertainty = 3 AND open blocking issues exist → MX Stop (override any score)

## Stop / Ask conditions

Immediately stop and ask a human if:
- Any open issue in `open-issues.md` is marked as blocking and unresolved.
- Scope is unclear enough that you cannot score Uncertainty with confidence.
- Chosen mode is M5 or MX.

## Instructions

1. Score each of the four criteria from the evidence in `spec-pack.md` and
   `open-issues.md`. State each score and its justification in one sentence.
2. Sum the scores and map to a mode.
3. Check the MX override rule.
4. Write the adapted workflow — the ordered list of commands to run for this
   mode. Use the table below as default; note any additions or omissions.

| Mode | Workflow |
|---|---|
| M1 | sdd-implement → sdd-test → sdd-report |
| M2 | sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report |
| M3 | sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report (+ extra attention on FE/BE contract in spec-pack section 9) |
| M4 | sdd-map (re-run) → sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report (+ security review before merge) |
| M5 | Escalate to human lead immediately. Minimal automation. Document decisions in mode-decision.md and stop. |
| MX | Stop. List every blocking issue. Do not run further commands until resolved. |

5. Write `mode-decision.md` using the template structure.

When done: report the chosen mode and the adapted workflow list, then tell the
user to run the first command in the adapted workflow (e.g., `/sdd-context
$ARGUMENTS`) — or to resolve open issues first if mode is MX.
