param(
    [string]$PromptFile,
    [string]$SchemaFile,
    [string]$OutputFile,
    [string]$RepositoryRoot,
    [string]$BaseRef,
    [string]$HeadRef,
    [string]$PullRequestNumber
)

$ErrorActionPreference = 'Stop'

throw @"
Local Codex adapter is not configured yet.

Create a runner-local adapter by copying this file to a machine-specific path and replacing the body with the actual Codex CLI invocation.

Expected responsibilities:
- read the prompt file
- run local Codex CLI in read-only review mode
- write JSON matching .github/codex/schemas/pr-review.schema.json to the output file

Recommended environment variables on the runner host:
- CODEX_CLI_COMMAND: full path to the Codex executable or wrapper
- CODEX_HOME / auth context required by your local Codex installation

Invocation context passed by the workflow:
- PromptFile: $PromptFile
- SchemaFile: $SchemaFile
- OutputFile: $OutputFile
- RepositoryRoot: $RepositoryRoot
- BaseRef: $BaseRef
- HeadRef: $HeadRef
- PullRequestNumber: $PullRequestNumber
"@
