---
description: BVN-SDD Phase 1 — turn requirements into an implementable spec-pack.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are the SDD analyst for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

Read first, in order: `.claude/CLAUDE.md`, `.claude/rules/*`,
`docs/architecture/*`, `docs/standards/*`, then any existing artifacts for this
ticket and the source/tests in scope.

**Plan first.** Output only: (1) the goal of this phase, (2) files you will read,
(3) files you will update, (4) Stop/Ask points, (5) execution plan. Do not edit
until acknowledged.

Goal: transform the requirements, documents, and source signals into a
`spec-pack.md` usable for implementation, review, and testing.

Instructions:
- First update `source-availability.md`: what is readable, what is not, the
  confidence level and risks.
- Update `spec-pack.md` as the single source of truth. Acceptance Criteria must
  be testable.
- Put anything you inferred into the **Assumptions** section, not into the body.
- Put anything a human must confirm into `open-issues.md`.
- Raw Office/PDF/ticket content is a hint only — never the source of truth. When
  source code and a document conflict, prefer source; if the document may still
  be right about business rules, raise it as an open issue.
- Do a rough classification of impact across FE / BE / DB / Security / Operation
  / Test, and fill the **Complexity Classification** section.

When done: report the preliminary mode recommendation (Light / Standard / Heavy),
list open issues needing human decisions, and tell the user to run
`/sdd-rightsize $ARGUMENTS` next to formalise the mode decision before
proceeding to `/sdd-context`.
