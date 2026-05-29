#!/usr/bin/env bash
# Create a new BVN-SDD ticket folder and seed it with blank artifacts.
# Usage: ./create-ticket.sh T-001
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <TICKET-ID>" >&2
  exit 1
fi

ticket="$1"

# Resolve the project root (three levels up from .bvn-sdd/scripts/bash).
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd "$script_dir/../../.." && pwd)"
templates_dir="$project_root/.bvn-sdd/templates"
ticket_dir="$project_root/docs/changes/$ticket"

mkdir -p "$ticket_dir"

artifacts=(
  spec-pack.md source-availability.md open-issues.md
  context.md source-map.md
  impact-analysis.md impl-plan.md
  review-checklist.md self-review.md
  test-plan.md test-results.md report.md
)

for name in "${artifacts[@]}"; do
  src="$templates_dir/$name"
  dst="$ticket_dir/$name"
  if [ ! -f "$src" ]; then
    echo "warning: template not found: $name" >&2
    continue
  fi
  if [ -f "$dst" ]; then
    echo "skip (exists): $name"
    continue
  fi
  sed "s/<TICKET>/$ticket/g" "$src" > "$dst"
  echo "created: docs/changes/$ticket/$name"
done

echo
echo "Ticket $ticket ready. Next: run /sdd-spec $ticket in Claude Code."
