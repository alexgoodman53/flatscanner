# Implementation Plan: AI Pull Request Workflow

## Summary

Upgrade the repository from a placeholder AI review scaffold to an enforceable pull-request workflow where Claude Code authors implementation PRs, Codex reviews them automatically through a self-hosted GitHub runner, and a human remains the final merge authority.

## Files And Areas

- `AGENTS.md` and `CLAUDE.md` for explicit agent responsibilities
- `docs/adr/002-ai-development-workflow.md` for the durable workflow decision
- `specs/002-ai-pr-workflow/` for execution tracking
- `.github/workflows/ai-review.yml` for automated Codex PR review on a self-hosted runner
- `.github/pull_request_template.md` for consistent PR metadata
- `.github/CODEOWNERS` for repository ownership defaults
- `.github/codex/` for reusable review prompts and schema files
- `scripts/` for runner setup and local review orchestration

## Proposed Workflow

1. Claude implements a scoped task from the active spec in a feature branch
2. Claude opens a pull request using the repository template
3. GitHub Actions runs CI, PR guard, and Codex review automatically
4. The self-hosted runner invokes the local Codex review adapter and posts a sticky review comment on the pull request
5. A human decides whether to merge after required checks are green

## Self-Hosted Design

- Use a Windows self-hosted runner labeled `codex`
- Keep the runner on the same machine where local Codex CLI access is configured
- Build the Codex prompt from durable repository context plus pull-request metadata
- Route the actual Codex CLI invocation through a local adapter script so the repository workflow stays stable even if the local command changes
- Fail the workflow when the review verdict is `request_changes`

## Risks

- The local runner must remain online for PR review jobs to start
- Codex CLI accessibility on Windows must be validated on the runner host
- Review quality still depends on disciplined specs and up-to-date durable docs

## Validation

- Confirm the workflow parses as valid YAML
- Confirm the prompt and schema files are present in the repository
- Confirm the PR template guides contributors to the active spec and validation notes
- Confirm the local review scripts are present and executable on the runner host
- Confirm the runner is registered with the `codex` label

## Notes

The simplest stable model is to let GitHub Actions enforce that review happened and to fail the review job on blocking findings, while still keeping a human merge gate.
