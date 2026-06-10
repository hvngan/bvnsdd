---
description: BVN-SDD Phase 9 — capture learnings, register failure modes, identify promotion candidates.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep
---

You are closing the learning loop for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Also read `docs/maintenance/failure-mode-index.md` and
`docs/maintenance/pattern-library.md` (if present).

**Plan first.** State goal, reads, writes, Stop/Ask points, steps. Do not edit until acknowledged.

## Step 1 — Identify promotion candidates

Scan the ticket artifacts for items worth promoting to shared project standards:
- Patterns in `context.md` not yet captured in `docs/standards/` or `.claude/rules/`
- Constraints or gotchas discovered in `impl-plan.md` or `self-review.md`
- Security or operational findings that apply beyond this ticket
- Open issues that revealed a systemic gap in the project

Write `promotion-candidates.md` in the ticket folder listing each candidate with:
- What it is (pattern, rule, standard, constraint, warning)
- Which file it should be promoted to (`docs/standards/`, `.claude/rules/`, `docs/architecture/`, etc.)
- Priority: High / Medium / Low

If nothing is worth promoting, write a minimal `promotion-candidates.md` noting that.

## Step 2 — Register failure modes

From the "failure-mode candidates" section in `report.md`, update
`docs/maintenance/failure-mode-index.md`:

- Add each new failure mode as a row. Do not duplicate existing entries.
- Columns: `ID | Ticket | Description | Area | Severity | Mitigation | Status`
- Severity: High / Medium / Low
- Status: open / mitigated / accepted

If `docs/maintenance/failure-mode-index.md` does not exist yet, create it with
a header row before adding entries.

## Step 2b — Update pattern library (if applicable)

If this ticket surfaced a reusable implementation pattern (a repeatable solution
to a recurring problem), add it to `docs/maintenance/pattern-library.md`:

- Columns: `ID | Name | Problem | Solution | Example file:line | Ticket`
- Only promote patterns that are genuinely reusable — not one-offs.

If `docs/maintenance/pattern-library.md` does not exist and there is at least
one pattern to add, create it with a header row first.

## Step 3 — Apply high-priority promotions

For each High-priority item in `promotion-candidates.md`:

1. Read the target file (if it exists).
2. Propose the addition or amendment as a diff.
3. **Stop/Ask**: present the proposed change and wait for user confirmation.
4. Apply only after the user confirms.

## Stop / Ask condition

If there are no failure modes and no candidates, confirm with the user before
stopping — they may want to add manual entries.

When done: summarize what was registered in `failure-mode-index.md`, what was
promoted, what remains in `promotion-candidates.md` for human follow-up, and
confirm the ticket is fully closed.
