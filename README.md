# Codex Audit Skills

Codex-native audit skills adapted from a Claude audit workflow.

This repository packages three installable Codex skills:

- `audit-lite`: a fast, evidence-based audit for bounded changes.
- `audit-full`: a deep multi-role audit packet for release gates and broad reviews.
- `audit-team`: the full five-role audit-team workflow under its original prompt name.

The goal is simple: make Codex audits harder to fake and easier to act on. Findings must cite evidence, classify severity, state blast radius when needed, and give a concrete fix path.

## Fidelity To The Source Skills

These are full-function Codex adaptations of the Claude skills in `source-originals/claude/`, not summaries.

- `skills/audit-lite/SKILL.md` preserves the original compact reviewer workflow, report template, severity framework, blast-radius rules, commitments, guardrails, and sign-off checklist.
- `skills/audit-team/SKILL.md` preserves the original single-file five-role workflow and bundles the role references/templates so its links resolve in Codex.
- `skills/audit-full/SKILL.md` preserves the original bundled `audit-team-full` workflow under the Codex-native `audit-full` name.

Only Claude-specific tool references were adapted, such as replacing `present_files` with Codex final-response file paths and replacing `AskUserQuestion` with a direct user question followed by waiting.

## Install

PowerShell:

```powershell
.\scripts\install.ps1
```

Bash:

```bash
./scripts/install.sh
```

Manual install:

```text
copy skills/audit-lite  -> %USERPROFILE%\.codex\skills\audit-lite
copy skills/audit-full  -> %USERPROFILE%\.codex\skills\audit-full
copy skills/audit-team  -> %USERPROFILE%\.codex\skills\audit-team
```

Restart Codex after installation so the skill list refreshes.

## Use

Examples:

```text
Use $audit-lite to verify this PR before merge.
```

```text
Use $audit-full to perform a release-gate audit of this repo.
```

```text
Use $audit-team to review this project.
```

`audit-team` and `audit-full` both provide the full multi-role audit capability. `audit-full` is the Codex-native name; `audit-team` preserves older handoff compatibility.

## Documentation

- [User Manual](docs/manuals/USER_MANUAL.md)
- [Architecture](docs/architecture/ARCHITECTURE.md)
- [Landing Page](docs/index.html)
- [Discussion Seeds](docs/discussions/)

## Validate

```bash
python scripts/validate_skills.py
```

The validator checks required skill files, frontmatter names, metadata, bundled references, templates, and documentation surfaces.

## Repository Layout

```text
skills/
  audit-lite/
  audit-full/
  audit-team/
docs/
  architecture/
  manuals/
  discussions/
scripts/
tests/
```

## License

MIT
