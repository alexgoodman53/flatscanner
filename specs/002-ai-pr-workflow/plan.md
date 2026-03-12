# Implementation Plan: AI Pull Request Workflow

## Summary

Upgrade the repository from a placeholder AI review scaffold to an enforceable pull-request workflow where Claude Code authors implementation PRs, Codex reviews them automatically through GitHub Actions, and a human remains the final merge authority.

## Files And Areas

- `AGENTS.md` and `CLAUDE.md` for explicit agent responsibilities
- `docs/adr/002-ai-development-workflow.md` for the durable workflow decision
- `specs/002-ai-pr-workflow/` for execution tracking
- `.github/workflows/ai-review.yml` for automated Codex PR review
- `.github/pull_request_template.md` for consistent PR metadata
- `.github/CODEOWNERS` for repository ownership defaults
- `.github/codex/` for reusable review prompts and schema files

## Proposed Workflow

1. Claude implements a scoped task from the active spec in a feature branch
2. Claude opens a pull request using the repository template
3. GitHub Actions runs CI, PR guard, and Codex review automatically
4. Codex posts a structured review comment on the pull request
5. A human decides whether to merge after required checks are green

## GitHub Action Design

- Trigger on pull request open, synchronize, reopen, and ready-for-review events
- Skip draft pull requests until they are ready for review
- Use the repository checkout plus base/head history so Codex can inspect the real diff
- Build the Codex prompt from a durable repository prompt file and runtime PR metadata
- Return structured JSON that can be posted back as a sticky pull request comment
- Keep the review job read-only with no write access to repository contents

## Risks

- If `OPENAI_API_KEY` is not configured, the AI review gate cannot run
- AI review can produce false positives, so a human merge decision must remain in place
- Review quality depends on disciplined specs and up-to-date durable docs

## Validation

- Confirm the workflow parses as valid YAML
- Confirm the prompt and schema files are present in the repository
- Confirm the PR template guides contributors to the active spec and validation notes
- Confirm the repository instructions match the automated workflow behavior

## Notes

The simplest stable model is to let GitHub Actions enforce that review happened, not to let AI merge code automatically. This keeps the system auditable and easier to trust.
