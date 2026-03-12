# Tasks: AI Pull Request Workflow

## Spec

- [x] Define explicit Codex and Claude Code responsibilities
- [x] Record the pull-request based AI delivery model
- [x] Define the required automation and review gates

## Documentation

- [x] Update `AGENTS.md` with role boundaries and commit rules
- [x] Update `CLAUDE.md` with implementation and PR expectations
- [x] Add a durable ADR for the AI development workflow

## GitHub Workflow

- [x] Replace the placeholder AI review workflow with a self-hosted Codex PR review workflow
- [x] Add a durable Codex review prompt file
- [x] Add a structured review schema for machine-readable results
- [x] Add a pull request template for AI-authored work
- [x] Add default repository ownership metadata
- [x] Add local runner setup and review orchestration scripts

## Validation

- [ ] Register the Windows self-hosted runner with the `codex` label
- [ ] Configure the local Codex review adapter on the runner host
- [ ] Enable branch protection rules for `main`
- [ ] Confirm required checks include `CI`, `PR Guard`, and `AI Review`
- [ ] Confirm at least one human approval is required before merge
- [ ] Open a test pull request and verify sticky review comments plus blocking verdict behavior

## Follow-Up

- [ ] Decide whether Claude PR creation should later be triggered from issues or slash commands
- [ ] Decide whether low-severity review findings should remain non-blocking forever
