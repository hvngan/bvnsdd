---
description: BVN-SDD Phase 4+5 — finalize review checklist, implement to the plan, then self-review.
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are a senior engineer driving Phase 4 (Review Checklist) and Phase 5
(Implementation) for ticket **$ARGUMENTS**. Work in `docs/changes/$ARGUMENTS/`
and the source tree.

**Plan first.** State goal, reads, writes, Stop/Ask points, steps. Do not edit until acknowledged.

## Phase 4 — Finalize Review Checklist

Before writing a single line of code, finalize `review-checklist.md`:

1. Read the blank template created by `/sdd-new`.
2. Extend it with ticket-specific items implied by `spec-pack.md`,
   `impact-analysis.md`, and `impl-plan.md` (e.g. specific edge cases,
   migration concerns, permission boundaries unique to this ticket).
3. Remove generic items that clearly do not apply to this ticket's scope.
4. Present the finalized checklist to the user.

**Stop here until the checklist is acknowledged.** Do not begin coding until
the user confirms the checklist is correct.

## Phase 5 — Implementation

Rules:
- Do not add requirements not in `spec-pack.md`.
- Read the target source and existing tests before editing.
- Make small changes; follow existing patterns but do not reproduce obvious
  existing bugs or violations.
- If unsure, return to `open-issues.md` instead of guessing.
- Run lint/build/test where possible and capture the commands and results.
- **Multi-platform** (when `.bvn-sdd/config.yml` `platforms:` lists more than one):
  implement each native tree from the SAME shared spec; do not let one platform's
  idioms leak into the other. Before self-review, run the **Cross-platform
  consistency** section of `review-checklist.md`: confirm every shared AC is
  observable on both platforms and both clients consume the shared contract
  identically. Record any intentional divergence in `open-issues.md`.

After implementing, fill `self-review.md`:
- implementation overview; files changed; spec/AC mapping; self-check against
  every item in the finalized review checklist; commands run and results; test
  status; known unresolved issues; accepted-risk candidates; points a second
  reviewer should focus on.

When done, summarize the diff and tell the user to run `/sdd-test $ARGUMENTS`.
The ticket folder contains a pre-created `human-review.md` — the human reviewer
fills this after reading the diff. AI must NOT fill `human-review.md`.
