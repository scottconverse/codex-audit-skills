---
name: audit-lite
description: Single-pass Codex audit for narrow scopes. Use when the user asks to verify a dev report, review a single PR, check a small branch, inspect up to 10 changed files across up to 3 repos, decide whether something is ready to push or merge, or run a quick evidence-based smoke audit. Prefer this over audit-full for bounded changes; escalate to audit-full when scope becomes whole-project, multi-feature, UI-heavy, release-gate, or adversarial.
---

# Audit Lite

Run a fast but evidence-based audit. Verify the claim, inspect the bounded change, and return a severity-ranked punchlist in chat. Speed comes from limited scope, not from lowering the evidence bar.

## Scope Gate

Use this skill only for bounded audits:

- one PR, branch, or small dev report
- a small bug fix or focused feature
- up to 10 changed files across up to 3 repos
- no full launch or whole-project readiness decision

Stop and recommend `audit-full` if the request is a release gate, multi-feature launch, "tear this apart" review, meaningful UI/UX audit, or whole-repo assessment.

If scope is ambiguous, ask one concise question and then stop until answered.

## Workflow

### 1. Establish Ground Truth

Before deeper review:

- Identify the exact repo, branch, PR, commit, or files.
- Run cheap existence checks for claimed refs and files.
- Inspect recent git history and current working-tree state.
- Tag working notes as `[AUDITOR-RUN]` when you personally verified something and `[DEV-REPORTED]` when it only comes from the user/dev report.

If the basic premise is false, report that directly instead of decorating the failure with a long audit.

### 2. Inspect Through Four Lenses

Use all applicable lenses:

1. **Engineering:** correctness, security, version consistency, dependency hygiene, data contracts, adjacent call sites.
2. **Tests:** collect or run the relevant tests; compare claimed test coverage/counts with reality.
3. **Docs:** check README, changelog, manuals, install snippets, release notes, and version surfaces touched by the change.
4. **Runtime/UX:** run the affected path when practical. If UI is touched, use browser evidence or screenshots where available; if not run, say so.

Do not accept "tests pass" or "verified" without independent evidence.

### 3. Classify Findings

Severity:

- **Blocker:** cannot ship; data loss, security exposure, broken core flow, install path broken as documented.
- **Critical:** must fix before release; reachable security gap, broken primary feature, missing failure state on likely path.
- **Major:** should fix soon; meaningful regression risk, systemic test/docs gap, drift that will mislead users or maintainers.
- **Minor:** low-risk cleanup, single stale reference, local naming inconsistency.
- **Nit:** preference only.

Every Blocker/Critical must include blast radius. Include blast radius for Major when the fix touches shared contracts.

### 4. Return The Chat Punchlist

Default output is chat, not a file. Use this shape:

```markdown
## Verdict
<Ship / do not ship / ship with caveats, with one-sentence reason.>

## Evidence Checked
- [AUDITOR-RUN] <command/file/PR inspected>
- [DEV-REPORTED] <claim not independently verified>

## Findings

### BLOCKER-001: <title>
Evidence: <file:line, command, behavior, screenshot path>
Impact: <why it matters>
Fix: <concrete next step>
Blast radius: <required for Blocker/Critical>

## Working Well
- <specific thing that is actually solid>

## Gaps / Limits
- <what was not checked and why>

## Escalation
<No escalation needed / recommend audit-full because...>
```

If the user explicitly asks for a saved artifact, write one markdown file named `audit-lite-<scope>-<YYYY-MM-DD>.md`.

## Hard Guardrails

- Never fabricate evidence, command output, screenshots, line numbers, or runtime behavior.
- Never weaken severity to avoid conflict.
- Never pad the report with fake nits.
- Test gaps are findings when the change fixes a bug or alters behavior.
- Docs drift is a finding when observable behavior changed.
- Stay in scope; escalate instead of quietly turning lite into a full audit.

## Sign-Off

Before answering:

- Scope and evidence are clear.
- Every finding has severity, evidence, impact, and fix.
- Every Blocker/Critical includes blast radius.
- Unchecked areas are stated.
- Escalation recommendation is explicit.
