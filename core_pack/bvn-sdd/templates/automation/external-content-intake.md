# External Content Intake Policy — <PROJECT>

> Rules for handling Word, Excel, PowerPoint, PDF, web pages, and other external
> content. Prevents context pollution, stale data, and prompt injection.
> Filled by `/sdd-phase0a`.

## Core rule

External documents are **hints only** — never the source of truth.
The source of truth is always the ticket's `spec-pack.md` or the source code.

## Intake process (all external content types)

1. **Extract** — pull out only the relevant sections into `reference-extracts.md`
   inside the ticket folder. Do not paste the entire document.
2. **Review** — a human or AI confirms the extracted content is accurate and
   not outdated.
3. **Promote** — move confirmed points into `spec-pack.md` as requirements or
   assumptions.
4. **Conflict rule** — if the document contradicts source code, trust source code
   and raise an open issue.

## Content types found in this project

| Type | Location(s) | Handling |
|---|---|---|
| Excel / `.xlsx` | | Extract → review → promote |
| Word / `.docx` | | Extract → review → promote |
| PDF | | Extract → review → promote |
| Web pages | | Summarise URL + key points only |
| External repo | | See `repo-intake-checklist.md` |

## Warning signs to stop and escalate

- Document contains personal data (names, emails, IDs, financial data)
- Document is password-protected or cannot be fully read
- Document version is unknown or potentially outdated
- Document and source code contradict each other on business rules
- Document contains executable content (macros, scripts)

## Project-specific notes

_Any project-specific external content decisions made during Phase 0-A._
