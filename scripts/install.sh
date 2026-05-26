#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
skills_dst="$codex_home/skills"

mkdir -p "$skills_dst"

for skill in audit-lite audit-full audit-team; do
  src="$repo_root/skills/$skill"
  dst="$skills_dst/$skill"
  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "Missing skill source: $src" >&2
    exit 1
  fi
  rm -rf "$dst"
  cp -R "$src" "$dst"
  chmod -R u+rwX,go+rX "$dst" 2>/dev/null || true
  echo "Installed Codex skill: $skill -> $dst"
done

echo "Done. Restart Codex to refresh available skills."
