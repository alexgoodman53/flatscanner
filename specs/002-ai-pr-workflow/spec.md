# Feature Spec: AI Pull Request Workflow

## Context

The repository needs a reliable operating model for AI-assisted delivery: Codex defines architecture and reviews changes, Claude Code implements product code in pull requests, and GitHub Actions enforces quality gates before merge.

## Scope

- Record explicit responsibilities for Codex and Claude Code
- Define the pull-request based delivery flow for AI-authored changes
- Add repository files that support automated PR review and consistent PR structure
- Replace the placeholder AI review workflow with a self-hosted local Codex review pipeline
- Document the required GitHub branch protection and runner settings

## Out Of Scope

- Full autonomous merge without human approval
- Production application code changes
- External issue tracker automation

## Requirements

- Codex must be documented as architect, reviewer, and CI/CD owner
- Claude Code must be documented as the primary implementation agent for product code
- Codex must be allowed to commit process-only changes such as docs, specs, ADRs, and GitHub workflows
- Pull requests must run CI, PR guard, and automated Codex review
- The AI review workflow must run on a self-hosted runner and post review output back to the pull request
- The repository must provide a repeatable PR template for AI-authored changes

## Acceptance Criteria

- Agent instructions clearly separate Codex and Claude responsibilities
- A durable ADR records the AI delivery model
- A PR-triggered GitHub Actions workflow runs Codex review through a self-hosted runner
- The repository contains the local review scripts needed by the self-hosted runner
- A pull request template exists for AI-authored changes
- Repository docs identify the GitHub settings needed to make the workflow enforceable

## Open Questions

- Whether a future orchestration layer should automatically open Claude tasks from issues or slash commands
- Whether AI review findings should remain advisory only or eventually block merge based on severity
