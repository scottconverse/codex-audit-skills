---
name: audit-full
description: Deep multi-role Codex audit of a project, repo, release gate, PR set, or readiness claim. Use when the user wants a full audit packet, pre-release review, launch readiness check, broad architecture/UX/docs/tests/runtime QA review, adversarial second opinion, or "tear this apart" assessment. Produces an executive report, per-role deep dives, severity-ranked findings, blast-radius analysis, sprint punchlist, next-sprint watchlist, and optional documentation rewrites.
---

# Audit Full

Run a deep multi-discipline audit. The goal is not to sound thorough; the goal is to verify enough reality that a dev team can safely act on the report.

This skill adapts the original Claude audit-team workflow for Codex. Use Codex tools and local shell/GitHub/browser capabilities. Do not assume Claude-only tools such as `AskUserQuestion` or `present_files` exist.

## Roles

Cover all five roles unless the user explicitly narrows scope:

| Role | Focus | Reference |
|---|---|---|
| Principal Engineer | Architecture, correctness, security, performance, dependencies, provenance | `references/principal-engineer.md` |
| Senior UI/UX Designer | Visual hierarchy, interaction states, copy, accessibility, user journeys | `references/uiux-designer.md` |
| Technical Writer | README, manuals, docs, release notes, landing copy accuracy and honesty | `references/technical-writer.md` |
| Test Engineer | Test coverage reality, blind spots, shortcuts, regression risk | `references/test-engineer.md` |
| QA Engineer | Runtime behavior across web, API, CLI, install, protocol, and data paths | `references/qa-engineer.md` |

Also use:

- `references/severity-framework.md`
- `references/blast-radius.md`
- `references/orchestration.md`

Templates live in `templates/`.

## Intake

Confirm the audit target:

- repo/folder/PR/URL/project description
- scope mode: `full`, `targeted`, or `scoped`
- posture: balanced by default, adversarial if requested or release-gate stakes demand it
- writer mode: `audit-only`, `audit+draft`, or `full-rewrite`

If the user already gave enough context, proceed. If a necessary fact is missing and cannot be discovered, ask one concise question and stop.

Create an output folder:

```text
audit-<project>-<YYYY-MM-DD>/
```

## Execution

### 1. Ground Truth Pass

Before role work:

- inspect local git state and recent commits
- compare local branch/PR/tag/release claims with live remote when relevant
- enumerate durable artifacts: docs, tests, workflows, release assets, installer scripts, QA evidence
- record what is `[AUDITOR-RUN]` versus `[DEV-REPORTED]`

### 2. Role Audits

Run the roles independently. If Codex subagents are available and explicitly authorized, use them. Otherwise run each role sequentially in the main thread while keeping findings separated.

Each role must:

- read its role reference plus severity and blast-radius references
- inspect the agreed scope
- write its deep-dive report using the matching template
- include evidence, severity, blast radius, fix path, and confidence
- include a "what is working" section

Do not skip UI runtime checks for UI products. If the product cannot be run, state that as a verification limit and use screenshots/static checks honestly.

### 3. Synthesis

After role reports:

- deduplicate overlapping findings
- sort by severity and user impact
- write `00-executive-audit.md`
- write `sprint-punchlist.md`
- write `next-sprint-watchlist.md`
- write doc rewrites when writer mode calls for them
- make sure cross-links resolve

## Output Package

```text
audit-<project>-<YYYY-MM-DD>/
  00-executive-audit.md
  01-engineering-deepdive.md
  02-uiux-deepdive.md
  03-documentation-deepdive.md
  04-test-deepdive.md
  05-qa-deepdive.md
  sprint-punchlist.md
  next-sprint-watchlist.md
  doc-rewrites/
```

Only create `doc-rewrites/` when needed.

## Evidence Rules

- Evidence must be concrete: file path, line, commit SHA, command output, screenshot path, browser observation, workflow run, release asset, or live URL.
- Never quote or invent output you did not see.
- Separate static confidence from runtime confidence.
- Treat missing evidence as a gap, not as a defect unless the repo claimed the evidence existed.
- Every Blocker/Critical/Major finding needs blast radius. Minor/Nit may omit it.

## Severity

Use `references/severity-framework.md`. Do not classify by vibes.

Finding schema:

```markdown
### <AREA>-<NNN>: <Severity> - <title>
Confidence: High | Medium | Low
Evidence type: Static | Runtime | Mixed
Status: Durable defect | Likely in-flight cleanup | Needs confirmation
Evidence: <specific proof>
Why it matters: <impact>
Blast radius: <downstream impact>
Fix path: <concrete work>
```

Suggested area prefixes:

- `ENG`
- `SEC`
- `UX`
- `DOC`
- `TEST`
- `QA`
- `REL`
- `BOOT`
- `PM`

## Codex-Specific Behavior

- Use local files and shell evidence first.
- Use GitHub CLI/API for PRs, issues, releases, and workflow runs when available.
- Use browser automation or screenshots for UI evidence when a local or remote app is in scope.
- If no subagent tool is available, do not pretend roles ran in parallel; state that role lenses were run sequentially.
- Present deliverables by giving file paths and a concise summary in final chat.

## Sign-Off

Do not call the audit complete until:

- all in-scope role reports exist
- executive report cross-references deep dives
- every Blocker/Critical has evidence, blast radius, and fix path
- sprint punchlist is actionable
- next-sprint watchlist is populated or explicitly empty with reason
- what-works sections are specific
- verification gaps are stated
- output file paths are provided to the user
