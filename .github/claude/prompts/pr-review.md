Claude Code is acting as the pull-request reviewer for this repository.

Review the current pull request using this repository's governing context before reading the changed code:

1. `.specify/memory/constitution.md`
2. `docs/README.md`
3. `docs/project-idea.md`
4. `docs/project/frontend/frontend-docs.md`
5. `docs/project/backend/backend-docs.md`
6. `docs/adr/*.md`
7. The active feature folder under `specs/<feature-id>/`

Review goals:

- Prioritize correctness, architectural alignment, regressions, missing tests, and operational risk
- Focus on substantive findings instead of style-only comments
- Verify that code changes remain aligned with the active spec and plan
- Check whether durable docs or spec artifacts should have been updated
- Treat CI/CD, safety, and data-flow risks as first-class review concerns
- Stay read-only and do not edit files

Output rules:

- Return JSON only
- Use this exact shape: `{"summary":"...","verdict":"approve|comment|request_changes","findings":[...]}`
- Keep the summary short and high-signal
- Use `approve` only when there are no material findings
- Use `comment` for minor risks or follow-ups that should not block merge
- Use `request_changes` when you find correctness, regression, architectural, or testing gaps that should be addressed before merge
- Each finding object must contain `severity`, `file`, `line`, `title`, and `body`
- Findings should reference the changed file path and line number when practical
