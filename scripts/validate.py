#!/usr/bin/env python3
"""Validate repository-level invariants for the published Skill collection."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
THIRD_PARTY_MANIFEST = ROOT / "third-party-skills.json"
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".html", ".css", ".js", ".cjs", ".mjs", ".py", ".sh"}
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[opsu]_[A-Za-z0-9]{20,}\b"),
    "personal macOS path": re.compile(r"/Users/(?!Shared(?:/|\b))[A-Za-z0-9._-]+(?:/|\b)"),
}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        return {}
    fields: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip('"\'')
    return fields


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())

    if not skill_dirs:
        errors.append("No Skill directories found under skills/.")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        meta = frontmatter(text)
        name = meta.get("name")
        description = meta.get("description")
        if name != skill_dir.name:
            errors.append(f"{skill_file.relative_to(ROOT)}: name {name!r} does not match directory {skill_dir.name!r}")
        if not description:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
        if len(text.splitlines()) > 500:
            warnings.append(f"{skill_file.relative_to(ROOT)}: over 500 lines; consider progressive disclosure")

        for path in skill_dir.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            content = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(content):
                    errors.append(f"{path.relative_to(ROOT)}: contains {label}")

    if not THIRD_PARTY_MANIFEST.is_file():
        errors.append("Missing third-party-skills.json dependency manifest.")
    else:
        try:
            manifest = json.loads(THIRD_PARTY_MANIFEST.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"third-party-skills.json: cannot be read as JSON: {exc}")
        else:
            if manifest.get("schema_version") != 1:
                errors.append("third-party-skills.json: schema_version must be 1")
            dependencies = manifest.get("dependencies")
            if not isinstance(dependencies, list):
                errors.append("third-party-skills.json: dependencies must be a list")
            else:
                seen_names: set[str] = set()
                seen_sources: set[str] = set()
                for index, dependency in enumerate(dependencies):
                    location = f"third-party-skills.json: dependencies[{index}]"
                    if not isinstance(dependency, dict):
                        errors.append(f"{location} must be an object")
                        continue
                    name = dependency.get("name")
                    source = dependency.get("source")
                    skills = dependency.get("skills")
                    license_name = dependency.get("license")
                    purpose = dependency.get("purpose")
                    if not isinstance(name, str) or not name.strip():
                        errors.append(f"{location}: name must be a non-empty string")
                    elif name in seen_names:
                        errors.append(f"{location}: duplicate name {name!r}")
                    else:
                        seen_names.add(name)
                    if not isinstance(source, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", source):
                        errors.append(f"{location}: source must use GitHub owner/repository form")
                    elif source in seen_sources:
                        errors.append(f"{location}: duplicate source {source!r}")
                    else:
                        seen_sources.add(source)
                    if not isinstance(skills, list) or not skills or not all(isinstance(skill, str) and skill for skill in skills):
                        errors.append(f"{location}: skills must be a non-empty list of strings")
                    if not isinstance(license_name, str) or not license_name.strip():
                        errors.append(f"{location}: license must be a non-empty string")
                    if not isinstance(purpose, str) or not purpose.strip():
                        errors.append(f"{location}: purpose must be a non-empty string")

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} Skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
