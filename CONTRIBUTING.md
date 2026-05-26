# Contributing

Thank you for improving Codex Audit Skills.

## Change Rules

- Keep `SKILL.md` files concise and Codex-native.
- Put long role guidance in `references/`, not in the skill body.
- Keep `audit-full` canonical; `audit-team` remains a compatibility alias.
- Do not add Claude-only tool names to Codex workflows unless clearly marked as historical source material.
- Validate before opening a PR:

```bash
python scripts/validate_skills.py
```

## Pull Request Checklist

- Skills still have valid YAML frontmatter with `name` and `description`.
- `agents/openai.yaml` exists for each skill.
- README, user manual, and architecture docs are updated when behavior changes.
- Screenshots or browser notes are included for landing-page changes.
- Any new reference file is linked from its skill.
