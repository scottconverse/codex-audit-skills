---
name: audit-team
description: Compatibility alias for audit-full. Use when a prompt, handoff, or older workflow asks Codex for audit-team, multi-role audit team, five-role audit, or Claude-style audit-team behavior. Load audit-full instead for the maintained Codex implementation.
---

# Audit Team Compatibility Alias

This skill exists so older prompts that say `audit-team` still route correctly in Codex.

When invoked:

1. Use `audit-full` as the maintained implementation.
2. Tell the user once, briefly: "`audit-team` is the compatibility alias; using `audit-full`."
3. Follow `../audit-full/SKILL.md` behavior and its bundled `references/` and `templates/`.

Do not maintain separate audit-team behavior here. The canonical Codex full-audit skill is `audit-full`.
