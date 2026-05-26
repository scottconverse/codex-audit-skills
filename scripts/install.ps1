param(
    [string]$CodexHome = "$env:USERPROFILE\.codex"
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$skillsSrc = Join-Path $repoRoot "skills"
$skillsDst = Join-Path $CodexHome "skills"

New-Item -ItemType Directory -Force -Path $skillsDst | Out-Null

foreach ($skill in @("audit-lite", "audit-full", "audit-team")) {
    $src = Join-Path $skillsSrc $skill
    $dst = Join-Path $skillsDst $skill
    if (-not (Test-Path (Join-Path $src "SKILL.md"))) {
        throw "Missing skill source: $src"
    }
    if (Test-Path $dst) {
        Remove-Item -Recurse -Force $dst
    }
    Copy-Item -Recurse -Force $src $dst
    Write-Host "Installed Codex skill: $skill -> $dst"
}

Write-Host "Done. Restart Codex to refresh available skills."
