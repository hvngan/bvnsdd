---
description: BVN-SDD Phase 0-B — map the codebase before working on tickets.
argument-hint: (no arguments)
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are performing **Source Intelligence** (BVN-SDD Phase 0-B) for this project.
Run this once per project, before the first ticket.

Read `.claude/CLAUDE.md` and `.claude/rules/*` first.

Goal: give future phases a map so the AI never gets lost. Do a *shallow* survey
of the repository — do not read every file.

Plan first (output only the plan, then proceed once acknowledged):
1. Goal of this mapping pass
2. Directories/entry points you will sample
3. Files you will create or update
4. Anything that needs a human decision (Stop/Ask)

Then produce/update under `docs/architecture/`:
- `system-map.md` — high-level components and how they relate
- `source-inventory.md` — key files/directories and their purpose
- As applicable: `entrypoint-map.md`, `route-api-map.md`, `service-layer-map.md`,
  `repository-db-map.md`, `data-flow-map.md`, `external-interface-map.md`,
  `fe-be-contract-map.md` (FE/BE API contracts and DTO shapes),
  `test-map.md` (existing test coverage per layer — unit / integration / e2e)

Rules: record what you read and could not read; mark inferences as Assumptions;
never open secrets/.env/PII. When done, summarize the map and list which
`docs/standards/*` files should be created or updated (coding, testing, security,
logging) based on patterns observed in the codebase.
