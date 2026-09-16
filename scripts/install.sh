#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_repo="wfnuser/skillset"

if [[ "${1:-}" == "--local" ]]; then
  source_repo="$repo_root"
elif [[ $# -gt 0 ]]; then
  echo "Usage: $0 [--local]" >&2
  exit 2
fi

npx -y skills add "$source_repo" \
  --skill '*' \
  --agent '*' \
  --global \
  --yes
