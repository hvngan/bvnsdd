---
description: BVN-SDD Phase 1-B — formalise the mode decision and adapt the workflow.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob
---

You are the SDD mode selector for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Also read `.bvn-sdd/config.yml` (platforms field).

**Plan first.** State goal, reads, writes, Stop/Ask points, steps. Do not edit until acknowledged.

Goal: produce a formal `mode-decision.md` that records the chosen operating mode
and how deep each phase goes — so every subsequent phase knows its required depth.

**Core principle (V04.2): the mode sets DEPTH, it does not skip phases.** Every
ticket — single-platform or multi-platform, greenfield or existing — runs the full
phase sequence: `/sdd-spec → /sdd-rightsize → /sdd-context → /sdd-plan →
/sdd-implement → /sdd-test → /sdd-blackbox → /sdd-report → /sdd-learnings`. A light
mode means each artifact is brief (a `context.md` may be a single line; an
`impact-analysis.md` a short table), never that the phase is omitted. Only **MX**
halts work.

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

## Multi-platform factor

If `.bvn-sdd/config.yml` `platforms:` lists more than one platform, this ticket
delivers two native trees (e.g. Android + iOS) from a single spec. Treat that as
a **Scope = 3** contributor and apply a **mode floor of M3** (never lower).
Record the multi-platform factor and the floor in `mode-decision.md`.

## Stop / Ask condition

Stop if scope is unclear enough that Uncertainty cannot be scored with confidence.
(Blocking open issues and M5/MX triggers are covered by rule `06-stop-conditions.md`.)

## Instructions

1. Score each of the four criteria from the evidence in `spec-pack.md` and
   `open-issues.md`. State each score and its justification in one sentence.
2. Sum the scores and map to a mode.
3. Check the MX override rule.
4. Write the **per-phase depth** for this mode. The phase sequence is the same in
   every mode (`/sdd-context → /sdd-plan → /sdd-implement → /sdd-test →
   /sdd-blackbox → /sdd-report → /sdd-learnings`); only the depth changes. Use the
   table below as default; note any ticket-specific additions.

| Mode | Depth at each phase (no phase is skipped) |
|---|---|
| M1 | Run every phase, but keep each artifact brief. `context.md` / `impact-analysis.md` / `blackbox-testcases.md` may be a few lines or a short table; if nothing is unique, write a one-line note saying so. Self-review only. |
| M2 | Standard depth for every artifact. Self-review; independent review recommended. |
| M3 | Standard depth + extra attention on the FE/BE contract (spec-pack §9). Add on-demand deep artifacts when relevant: `fe-be-contract-map.md`, `codex-review.md`. |
| M4 | Full depth. Re-run `/sdd-map` for affected areas. Add on-demand deep artifacts: `heavy-source-analysis.md`, `security-review.md`, `codex-review.md`; explicit rollback / migration plan; independent + human review before merge. |
| M5 | Maximum depth + mandatory human gate: threat model, full test evidence, rollback verification, accepted-risk approval, audit trail. Escalate to human lead; do not auto-merge. Still runs every phase. |
| MX | **Stop.** List every blocking issue. Do not run further phases until resolved. This is the only mode that halts work. |

   On-demand deep artifacts (M3+) are created only when the ticket needs them — they
   are not part of the default scaffold, keeping the core light.

5. Write `mode-decision.md` using the template structure (record per-phase depth,
   not skipped phases).

When done: report the chosen mode and the adapted workflow list, then tell the
user to run the first command in the adapted workflow (e.g., `/sdd-context
$ARGUMENTS`) — or to resolve open issues first if mode is MX.
