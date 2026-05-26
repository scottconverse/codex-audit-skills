from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "audit-lite": {"references": False, "templates": False},
    "audit-full": {"references": True, "templates": True},
    "audit-team": {"references": False, "templates": False},
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise AssertionError("missing YAML frontmatter")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def main() -> None:
    for skill, requirements in SKILLS.items():
        skill_dir = ROOT / "skills" / skill
        skill_md = skill_dir / "SKILL.md"
        assert skill_md.is_file(), f"{skill}: missing SKILL.md"
        data = frontmatter(read(skill_md))
        assert data.get("name") == skill, f"{skill}: frontmatter name mismatch"
        assert data.get("description"), f"{skill}: missing description"
        assert (skill_dir / "agents" / "openai.yaml").is_file(), f"{skill}: missing agents/openai.yaml"
        if requirements["references"]:
            refs = skill_dir / "references"
            assert refs.is_dir(), f"{skill}: missing references"
            for name in [
                "principal-engineer.md",
                "uiux-designer.md",
                "technical-writer.md",
                "test-engineer.md",
                "qa-engineer.md",
                "severity-framework.md",
                "blast-radius.md",
                "orchestration.md",
            ]:
                assert (refs / name).is_file(), f"{skill}: missing reference {name}"
        if requirements["templates"]:
            templates = skill_dir / "templates"
            assert templates.is_dir(), f"{skill}: missing templates"
            assert (templates / "00-executive-audit.md").is_file(), f"{skill}: missing executive template"

    for path in [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "LICENSE",
        ROOT / ".gitignore",
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "manuals" / "USER_MANUAL.md",
        ROOT / "docs" / "architecture" / "ARCHITECTURE.md",
    ]:
        assert path.is_file(), f"missing required repo artifact: {path.relative_to(ROOT)}"

    print("validate_skills: PASS")


if __name__ == "__main__":
    main()
