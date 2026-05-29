# 20 — Architecture & Context Loading

- **Map before you read deeply.** Use `docs/architecture/*` (entry points, API
  routes, service layer, repository/DB, data flow) to navigate. Do not read the
  whole repository.
- **Source priority** (highest first) when sources conflict:
  1. Explicit human instruction / approved decision
  2. Source code on the latest target branch
  3. Automated tests / test data / CI results
  4. DB schema / migration / ERD
  5. API contract (OpenAPI / GraphQL / protobuf)
  6. Operation docs / runbooks
  7. Approved spec / `spec-pack.md`
  8. Ticket / acceptance criteria
  9. Past design docs / PPT / Excel / PDF
  10. AI inference
- **Always include in context:** the ticket & AC, the change diff, files in and
  around the change scope, related tests, schema/migration/DTO/API contract.
- **Ask before including:** production logs, customer documents, PII data, large
  Excel/PDF, external web pages, config of MCP servers, installers/hooks.
- **Never include:** `.env`, secrets, private keys, tokens, credential stores,
  production DB dumps, PII, `node_modules`/`vendor`/`dist`/`build` in bulk,
  binaries, full lock files.
