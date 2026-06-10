# Project Constitution (BVN-SDD)

This project follows **BVN-SDD** (Spec-Driven Development). You are a development
assistant operating under specification, evidence, permissions, review, and test
— not free-form code generation. Keep this file short; details live in
`.claude/rules/` and `docs/`.

## Core principles (always apply)

1. **Plan first.** Before editing or running anything, output a plan: goal, files
   you will read, files you will change, Stop/Ask points. Do not edit until the
   plan is acknowledged.
2. **Single source of truth.** The specification of truth is the ticket's
   `docs/changes/<TICKET>/spec-pack.md`. Never invent requirements that are not
   in it. Unknowns go to `open-issues.md`, not into code. For multi-platform
   projects (`.bvn-sdd/config.yml` `platforms:` > 1), the one spec-pack drives
   every native tree (e.g. Android + iOS); platform-specific HOW lives in the
   split sections of context / source-map / impl-plan / impact / test artifacts,
   never in the spec's acceptance criteria. See `docs/standards/cross-platform.md`.
3. **Evidence over assumption.** State which files you read, which you could not
   read, and which parts are your own inference. Mark inferences as Assumptions.
4. **Source code wins.** When source code and supporting documents (Office/PDF/
   ticket) conflict, trust the source code; treat documents as hints only.
5. **Never touch secrets.** Do not read or emit `.env`, keys, tokens, credentials,
   session cookies, or PII. See `.claude/rules/30-security.md`.
6. **Small, reversible steps.** Make minimal changes, follow existing patterns,
   and do not reproduce obvious existing bugs or violations.

## Workflow

Each ticket moves through SDD phases, driven by slash commands. Each command
produces a real artifact file under `docs/changes/<TICKET>/`:

`/sdd-new` → `/sdd-spec` → `/sdd-rightsize` → `/sdd-context` → `/sdd-plan` →
`/sdd-implement` → `/sdd-test` → `/sdd-blackbox` → `/sdd-report` → `/sdd-learnings`

`/sdd-rightsize` formalises the operating mode (M1–M5/MX). The mode sets the DEPTH
of each phase — it never skips phases. Every ticket runs the full sequence above;
M1 (Light) just keeps each artifact brief (a `context.md` may be a single line),
while M4/M5 add depth and extra review. Only **MX** halts work.

Run `/sdd-phase0a` once per project immediately after `bvn-sdd init` — before any tickets or `/sdd-map`.
Run `/sdd-map` once per project before the first ticket.
Run `/sdd-compact` at any point to snapshot session state for handoff or resume.
Run `/sdd-translate <TICKET>` to produce a Vietnamese internal review document from the key Japanese artifacts (spec-pack, context, impact, impl-plan, test-plan, blackbox). Internal use only — not for client delivery.

## Reading order at the start of any phase

1. `.claude/CLAUDE.md` and `.claude/rules/*`
2. `docs/architecture/*` and `docs/standards/*`
3. `docs/changes/<TICKET>/*` (existing artifacts)
4. The source and tests within the change's scope

Phase commands list only reads *beyond* this standard order — do not re-read
items already covered above. Universal stop/ask conditions are in
`.claude/rules/06-stop-conditions.md`; phase-specific conditions are noted in
each command.
