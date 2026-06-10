---
description: BVN-SDD Phase 8 — write the final report for the ticket.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are writing the final report for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Update `report.md` with:
- summary of the change
- mapping to specification / acceptance criteria
- impact scope
- what was implemented
- review and test results
- accepted risks
- remaining open issues
- human decisions made
- what worked / what failed
- failure-mode candidates to register in `docs/maintenance/failure-mode-index.md`

Keep it factual: if tests failed or steps were skipped, say so. When done,
summarize the ticket outcome and list any follow-up items for a human. Tell the
user to run `/sdd-learnings $ARGUMENTS` to register failure modes and close the
learning loop.
