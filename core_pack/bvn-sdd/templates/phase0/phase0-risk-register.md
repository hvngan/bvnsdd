# Phase 0-A Risk Register — <PROJECT>

> Risks identified during the Safety Gate phase. Reviewed at the start of each
> project and updated whenever new risks are discovered.

| ID | Risk | Area | Severity | Mitigation | Status |
|---|---|---|---|---|---|
| R-001 | | Secrets | | | Open |
| R-002 | | Permissions | | | Open |
| R-003 | | External docs | | | Open |
| R-004 | | Hooks / MCP | | | Open |
| R-005 | | Context size | | | Open |

## Severity guide

| Level | Meaning |
|---|---|
| **High** | Could cause data loss, secret leak, production impact, or irreversible damage |
| **Medium** | Could cause incorrect output, spec drift, or significant wasted work |
| **Low** | Minor inconvenience; easy to detect and fix |

## Risk areas

- **Secrets** — credential files, keys, `.env` committed or accessible
- **Permissions** — AI can run commands with destructive or external effects
- **External docs** — Office/PDF injected directly as source of truth
- **Hooks / MCP** — hooks or MCP servers with unreviewed external access
- **Context size** — large auto-generated directories consuming AI context
- **Source conflict** — spec documents contradict source code

## Review history

| Date | Reviewer | Changes |
|---|---|---|
| | | Initial registration |
