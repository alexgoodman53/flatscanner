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

- [x] Replace the placeholder AI review workflow with a Codex-based PR review workflow
- [x] Add a durable Codex review prompt file
- [x] Add a structured review schema for machine-readable results
- [x] Add a pull request template for AI-authored work
- [x] Add default repository ownership metadata

## Validation

- [ ] Verify the workflow in GitHub with a configured `OPENAI_API_KEY` secret
- [ ] Enable branch protection rules for `main`
- [ ] Confirm required checks include `CI`, `PR Guard`, and `AI Review`
- [ ] Confirm at least one human approval is required before merge

## Follow-Up

- [ ] Decide whether Claude PR creation should later be triggered from issues or slash commands
- [ ] Decide whether severe AI review findings should eventually fail the workflow
