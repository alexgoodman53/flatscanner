# Self-Hosted Codex Review Setup

This repository expects automated PR review to run on a Windows self-hosted GitHub Actions runner labeled `codex`.

## One-Time Runner Setup

1. In GitHub, open repository settings and create a new self-hosted runner for Windows.
2. Copy the registration token shown by GitHub.
3. Run:
   `powershell -ExecutionPolicy Bypass -File .\scripts\setup-self-hosted-runner.ps1 -RepoUrl https://github.com/alexgoodman53/flatscanner -RegistrationToken <token> -AsService`
4. Confirm the runner appears online in GitHub with labels `self-hosted`, `windows`, and `codex`.

## Local Codex Adapter Setup

1. Copy `scripts\codex-review-adapter-template.ps1` to a machine-local path outside the repository if desired.
2. Replace the template body with the actual local Codex CLI invocation for your machine.
3. Set a machine-level environment variable:
   `CODEX_REVIEW_ADAPTER=<full path to your adapter ps1 file>`
4. Restart the runner service so the environment variable is picked up.

## Review Flow

- A new pull request triggers `.github/workflows/ai-review.yml`
- GitHub schedules the job on the self-hosted runner
- The runner executes `scripts\run-codex-pr-review.ps1`
- That script builds review context, calls the local adapter, posts a sticky PR comment, and fails the job when verdict is `request_changes`

## Required GitHub Branch Protection

- Protect `main`
- Require pull requests before merge
- Require status checks `CI`, `PR Guard`, and `AI Review`
- Require at least one human approval
- Restrict direct pushes to `main`
