#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
manifest="$repo_root/third-party-skills.json"
own_source="wfnuser/skillset"
dry_run=false

usage() {
  cat <<'EOF'
Usage: ./scripts/bootstrap.sh [--local] [--dry-run]

Installs every Skill from wfnuser/skillset, then installs the recommended
third-party Skills listed in third-party-skills.json for every supported agent.

  --local    Link this checkout as the source of wfnuser/skillset.
  --dry-run  Print the installation commands without running them.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --local)
      own_source="$repo_root"
      ;;
    --dry-run)
      dry_run=true
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
  shift
done

run() {
  printf ' +'
  printf ' %q' "$@"
  printf '\n'
  if [[ "$dry_run" == false ]]; then
    "$@"
  fi
}

if [[ ! -f "$manifest" ]]; then
  echo "Missing dependency manifest: $manifest" >&2
  exit 1
fi

echo "Installing maintained Skills from: $own_source"
run npx -y skills add "$own_source" \
  --skill '*' \
  --agent '*' \
  --global \
  --yes

dependency_rows="$(
  python3 - "$manifest" <<'PY'
import json
import sys
from pathlib import Path

manifest = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
for dependency in manifest["dependencies"]:
    for skill in dependency["skills"]:
        print(dependency["name"], dependency["source"], skill, sep="\t")
PY
)"

while IFS=$'\t' read -r name source skill; do
  [[ -n "$source" && -n "$skill" ]] || continue
  echo "Installing third-party Skill: $name ($skill) from $source"
  run npx -y skills add "$source" \
    --skill "$skill" \
    --agent '*' \
    --global \
    --yes
done <<< "$dependency_rows"

echo "Bootstrap complete. Restart or open a new agent session to refresh its Skill catalog."
