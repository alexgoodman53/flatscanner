# ADR 002: AI Development Workflow

## Status

Accepted

## Context

The repository already uses spec-driven documentation, but the delivery workflow between planning, implementation, review, and merge was not fully defined. The team wants a clear operating model where Claude Code implements application changes, Codex owns architecture and review, and GitHub Actions enforces the process.

## Decision

Adopt the following AI development workflow:

- Codex owns architecture direction, pull request review, and CI/CD policy
- Claude Code is the primary implementation agent for product code
- Product code changes should land through Claude-authored pull requests instead of direct pushes to `main`
- Codex may directly commit durable docs, specs, ADRs, GitHub workflow files, templates, and other non-product process files
- Every pull request must pass CI, PR guard checks, and automated Codex review before merge
- A human remains the final merge authority through GitHub branch protection and pull request approval rules
- Automated Codex review runs on a self-hosted Windows GitHub runner with a local Codex CLI adapter

## Workflow Shape

1. Work is scoped in `specs/<feature-id>/`
2. Claude implements the approved task in a branch and opens a pull request
3. GitHub Actions runs CI, PR guard checks, and Codex review automatically
4. The self-hosted runner checks out the pull request, builds the review prompt, invokes the local Codex adapter, and posts the result back to the pull request
5. A human reviews the result and merges only after required checks are green

## Required GitHub Settings

Configure the repository with these settings in GitHub:

- Protect the `main` branch
- Require a pull request before merging
- Require status checks: `CI`, `PR Guard`, and `AI Review`
- Require at least one human approval before merge
- Dismiss stale approvals when new commits are pushed
- Restrict direct pushes to `main`
- Register a self-hosted Windows runner with the `codex` label for this repository

## Consequences

- AI responsibilities are explicit and auditable
- Architecture decisions remain separated from implementation throughput
- The repository keeps a human-controlled merge gate while still benefiting from automated AI review
- GitHub configuration becomes part of the architecture and must be maintained like other durable process assets
- The repository no longer depends on a hosted Codex action or OpenAI API secret for PR review once the local runner is configured
