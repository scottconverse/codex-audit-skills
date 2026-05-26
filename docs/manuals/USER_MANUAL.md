# Codex Audit Skills User Manual

## What This Package Installs

This package installs three Codex skills:

- `audit-lite`
- `audit-full`
- `audit-team`

`audit-team` is the original five-role audit name. `audit-full` is the Codex-native name for the bundled full-audit skill. Both provide full multi-role audit capability.

## Installation

From this repository:

```powershell
.\scripts\install.ps1
```

Or on macOS/Linux/WSL:

```bash
./scripts/install.sh
```

Restart Codex after install.

## Choosing The Right Skill

Use `audit-lite` for:

- a single PR
- a small branch
- a dev report that needs verification
- a narrow push/merge readiness check
- up to 10 changed files across up to 3 repos

Use `audit-full` for:

- whole-project reviews
- release gates
- launch readiness
- multi-feature audit packages
- broad UX/docs/tests/runtime QA reviews
- adversarial "tear this apart" audits

Use `audit-team` when an older handoff names it or when you want the original five-role audit-team prompt name.

## Source Fidelity

The adapted Codex skills preserve the original Claude skill behavior:

- `audit-lite` keeps the same compressed five-dimension pass, report template, severity framework, blast-radius rules, and final sign-off checklist.
- `audit-team` keeps the same three-phase five-role workflow and bundles the same references and templates.
- `audit-full` keeps the same bundled full audit capability under a Codex-native name.

The original source files are included in `source-originals/claude/` for comparison. The intended changes are Codex-specific tool substitutions, not workflow reductions.

## Prompt Examples

```text
Use $audit-lite to verify PR #123. Tell me if it is ready to merge.
```

```text
Use $audit-full to audit this repo for release readiness. Include docs, tests, UX, runtime, and install evidence.
```

```text
Use $audit-team on this handoff.
```

## Evidence Rules

The skills are designed to keep Codex honest:

- Claims are marked as directly verified or reported.
- Findings include severity and concrete evidence.
- Blocker, Critical, and Major findings include blast radius when applicable.
- Runtime claims require runtime evidence.
- UI claims require browser or screenshot evidence when the interface is in scope.

## Output Expectations

`audit-lite` returns a chat punchlist by default.

`audit-full` creates a folder such as:

```text
audit-my-project-2026-05-25/
```

with executive summary, deep dives, sprint punchlist, and next-sprint watchlist.

## Updating

Pull the latest repository changes, then rerun the install script.

## Troubleshooting

If Codex does not show the skills:

1. Confirm files exist under `%USERPROFILE%\.codex\skills\`.
2. Confirm each skill directory has `SKILL.md`.
3. Restart Codex.
4. Run `python scripts/validate_skills.py` from the repo.
