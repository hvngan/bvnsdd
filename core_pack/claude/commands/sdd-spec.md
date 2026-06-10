---
description: BVN-SDD Phase 1 — turn requirements into an implementable spec-pack.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are the SDD analyst for ticket **$ARGUMENTS**. Work in
`docs/changes/$ARGUMENTS/`.

**Plan first.** State goal, reads, writes, Stop/Ask points, steps. Do not edit until acknowledged.

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
- Read `.bvn-sdd/config.yml` `platforms:`. Keep Acceptance Criteria, Input/Output,
  Validation, and Security strictly platform-neutral (the WHAT — never name
  Kotlin/Swift/Compose/SwiftUI). Fill section 8 *Surface impact (per platform)*
  with one row per in-scope platform, and write section 9 as ONE shared contract
  consumed identically by every client. If `platforms:` lists one platform, keep
  only its row. Multi-platform delivery raises baseline scope — flag M3+.

When done: report the preliminary mode recommendation (Light / Standard / Heavy),
list open issues needing human decisions, and tell the user to run
`/sdd-rightsize $ARGUMENTS` next to formalise the mode decision before
proceeding to `/sdd-context`.
