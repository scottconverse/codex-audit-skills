# Codex Audit Skills

Codex-native audit skills adapted from a Claude audit workflow.

This repository packages three installable Codex skills:

- `audit-lite`: a fast, evidence-based audit for bounded changes.
- `audit-full`: a deep multi-role audit packet for release gates and broad reviews.
- `audit-team`: a compatibility alias for older prompts; it routes to `audit-full`.

The goal is simple: make Codex audits harder to fake and easier to act on. Findings must cite evidence, classify severity, state blast radius when needed, and give a concrete fix path.

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

The last form is supported for compatibility, but `audit-full` is the maintained name.

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
