---
description: BVN-SDD Phase 2 — pin down the ticket's context and rules.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are preparing the working context for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read first: `.claude/CLAUDE.md`, `.claude/rules/*`, this ticket's `spec-pack.md`
and `open-issues.md`, `docs/architecture/*`, `docs/standards/*`, and
`.bvn-sdd/config.yml` `platforms:`.

**Multi-platform.** If `platforms:` lists more than one platform, populate the
`### Shared` / `### Android patterns` / `### iOS patterns` subsections of
`context.md` and the per-tree groups of `source-map.md`. Verify each platform's
APIs against that platform's own tree (`android/` vs `ios/`). Keep DTO/contract,
master data, and encoding in the shared sections — never fork them per platform.
If `platforms:` lists one platform, keep only that subsection.

**Plan first** (goal, files to read, files to update, Stop/Ask points, plan).
Do not edit until acknowledged.

---

## Detect project mode before proceeding

Check `docs/maintenance/phase0/phase0-plan.md` for `Project Type`. If absent,
check whether the files in this ticket's implementation scope already exist
in the repository.

- Source files exist → **EXISTING PROJECT MODE** (default)
- No source files → **NEW PROJECT MODE**

---

## EXISTING PROJECT MODE (default)

Goal: make sure the implementation phase does not use non-existent APIs or
forbidden patterns.

Update:
- `context.md` — concrete correct examples already in the codebase; allowed vs.
  forbidden patterns; methods/classes that actually exist vs. must not be used;
  DTO/Entity/Table mappings; master-data / code-value mappings; encoding and
  multi-language notes.
- `source-map.md` — the specific files this ticket will read and touch, with a
  one-line purpose each.
- `ticket-rules.md` — rules specific to this ticket only (not already in
  `.claude/rules/*`): number/format rules, encoding, logging requirements,
  forbidden patterns unique to this ticket's scope. If nothing is unique, write
  a single line noting that and leave the table rows empty.

Verify claims against the real source (use Grep/Glob/Read). Mark anything
uncertain in `open-issues.md`.

---

## NEW PROJECT MODE (no existing implementation for this scope)

Goal: establish the conventions and planned APIs that the implementation phase
will build toward — rather than verifying what already exists.

Update:
- `context.md` — planned APIs, interfaces, and patterns to establish; conventions
  to adopt (naming, error handling, logging); technology-specific rules from the
  chosen stack. **Mark every entry `[PLANNED]`.** Do NOT run Grep/Glob to verify
  things that do not exist yet.
- `source-map.md` — files to **CREATE** in this ticket (not read), with a
  one-line purpose each. Include the directory structure.
- `ticket-rules.md` — project-wide conventions being established by this ticket
  (format rules, encoding, logging, forbidden patterns). These should be promoted
  to `.claude/rules/` via `/sdd-learnings` once confirmed.

Mark anything uncertain (technology choices, API shapes, naming) in `open-issues.md`
so the human can decide before implementation begins.

---

**Depth by mode (this phase always runs).** In M1, keep `context.md`,
`source-map.md`, and `ticket-rules.md` brief — if a ticket has no unique pattern or
rule, a one-line note saying so is enough; do not skip the artifact. M2+ uses
standard depth; M4/M5 verify more exhaustively against source.

When done, tell the user to run `/sdd-plan $ARGUMENTS` next.
