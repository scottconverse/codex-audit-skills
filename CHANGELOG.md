# Changelog

## 0.1.0 - 2026-05-25

- Initial public package for Codex audit skills.
- Added `audit-lite`, adapted from the Claude single-pass audit skill.
- Added `audit-full`, adapted from the Claude multi-role audit-team-full bundle.
- Added `audit-team`, preserving the original five-role audit-team workflow for legacy prompts.
- Added install scripts, validation script, user manual, architecture docs, landing page, and seed discussion drafts.

## 0.1.1 - 2026-05-25

- Restored full-fidelity `SKILL.md` control-plane content for `audit-lite`, `audit-team`, and `audit-full`.
- Added `source-originals/claude/` with the original Claude source skills for provenance and future diffing.
- Bundled `references/` and `templates/` under `audit-team` so the original links resolve in Codex.
- Strengthened validation to fail if skill bodies regress to lossy condensed versions.
