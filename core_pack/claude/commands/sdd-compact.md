---
description: BVN-SDD utility — snapshot current session state into a strategic compact for handoff or resume.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob
---

You are creating a Strategic Compact snapshot for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read first: ALL artifacts for this ticket that exist:
`mode-decision.md`, `spec-pack.md`, `open-issues.md`, `source-availability.md`,
`context.md`, `source-map.md`, `impact-analysis.md`, `impl-plan.md`,
`self-review.md`, `test-plan.md`, `test-results.md`, `blackbox-testcases.md`,
`report.md`.

Do NOT read implementation source code — this command is purely a state snapshot.

Goal: write or update `strategic-compact.md` so that a new Claude session (or a
human) can resume this ticket without re-reading everything from scratch. The
compact must be self-contained and honest about gaps.

## Instructions

1. Identify the **current phase** by checking which artifacts exist and are
   non-empty. State the phase clearly.
2. Extract **Must Not Forget** items — constraints, human decisions already made,
   patterns to follow, things explicitly ruled out. These are facts that would
   cause mistakes if forgotten.
3. Build the **Files Read** list from evidence in `source-availability.md` and
   `context.md`. If these artifacts are absent, note that as a gap.
4. Build the **Files Not Yet Read** list — source files in scope that haven't
   been read yet, based on `source-availability.md` or `impact-analysis.md`.
5. List **Decisions Made** in chronological order with brief rationale. Include
   mode choice, key design decisions, accepted risks.
6. List **Open Issues** — unresolved items from `open-issues.md` and any
   outstanding questions noted in other artifacts.
7. Write **Next Steps** as exact slash commands with ticket ID, in order.

Write the result into `strategic-compact.md`.

## Stop / Ask condition

If critical information is contradictory between artifacts (e.g., spec-pack and
impl-plan disagree on scope), flag it as an open issue rather than resolving it
yourself.

When done: print the compact summary to the user (Current Phase, Must Not Forget
count, Open Issues count, Next Steps). Tell them to paste the content of
`strategic-compact.md` at the start of any new session to resume this ticket.
