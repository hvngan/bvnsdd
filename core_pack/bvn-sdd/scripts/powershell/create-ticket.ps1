<#
.SYNOPSIS
  Create a new BVN-SDD ticket folder and seed it with blank artifacts.
.EXAMPLE
  .\create-ticket.ps1 T-001
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Ticket
)

$ErrorActionPreference = "Stop"

# Resolve the project root (two levels up from .bvn-sdd/scripts/powershell).
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDir "..\..\..")).Path
$templatesDir = Join-Path $projectRoot ".bvn-sdd\templates"
$ticketDir = Join-Path $projectRoot "docs\changes\$Ticket"

if (-not (Test-Path $ticketDir)) {
    New-Item -ItemType Directory -Path $ticketDir -Force | Out-Null
}

$artifacts = @(
    "spec-pack.md", "source-availability.md", "open-issues.md",
    "mode-decision.md",
    "context.md", "source-map.md", "ticket-rules.md",
    "impact-analysis.md", "impl-plan.md",
    "review-checklist.md", "self-review.md", "human-review.md",
    "test-plan.md", "test-results.md", "blackbox-testcases.md",
    "blackbox-review-checklist.md", "test-data.md",
    "strategic-compact.md",
    "report.md"
)

foreach ($name in $artifacts) {
    $src = Join-Path $templatesDir $name
    $dst = Join-Path $ticketDir $name
    if (-not (Test-Path $src)) {
        Write-Warning "template not found: $name"
        continue
    }
    if (Test-Path $dst) {
        Write-Host "skip (exists): $name"
        continue
    }
    (Get-Content $src -Raw).Replace("<TICKET>", $Ticket) | Set-Content -Path $dst -NoNewline
    Write-Host "created: docs/changes/$Ticket/$name"
}

Write-Host "`nTicket $Ticket ready. Next: run /sdd-spec $Ticket in Claude Code."
