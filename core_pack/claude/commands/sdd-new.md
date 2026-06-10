---
description: Start a new BVN-SDD ticket — create its folder and blank artifacts.
argument-hint: <TICKET-ID> [short title]
allowed-tools: Bash, Read, Write, Edit, Glob
---

You are bootstrapping a new BVN-SDD ticket: **$ARGUMENTS**.

Goal: create the ticket workspace so later phases have somewhere to write.

Steps:
1. Determine the ticket id from the first token of `$ARGUMENTS` (e.g. `T-001`).
2. Create the directory `docs/changes/<TICKET>/` if it does not exist.
3. Copy each template from `.bvn-sdd/templates/` into that directory as a blank,
   ready-to-fill artifact (keep the same filename), unless it already exists:
   - `spec-pack.md`, `source-availability.md`, `open-issues.md`
   - `mode-decision.md`
   - `context.md`, `source-map.md`, `ticket-rules.md`
   - `impact-analysis.md`, `impl-plan.md`
   - `review-checklist.md`, `self-review.md`, `human-review.md`
   - `test-plan.md`, `test-results.md`, `blackbox-testcases.md`
   - `blackbox-review-checklist.md`, `test-data.md`
   - `strategic-compact.md`
   - `report.md`
   You may instead run the helper script if you prefer:
   `.bvn-sdd/scripts/powershell/create-ticket.ps1 <TICKET>` (Windows) or
   `.bvn-sdd/scripts/bash/create-ticket.sh <TICKET>` (macOS/Linux).
4. In each copied file, replace the `<TICKET>` placeholder with the ticket id.

Do **not** start filling content yet. After creating the files, report the list
of artifacts created and tell the user to run `/sdd-spec <TICKET>` next, then
`/sdd-rightsize <TICKET>` after that.
