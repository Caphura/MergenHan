from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from script_common import (
    add_locale_argument,
    display_path,
    locale_root,
    normalize_list,
    parse_frontmatter,
    parse_meta_yaml,
    read_text,
)

ALLOWED_PROMPT_TYPES = {"master", "module", "blueprint"}
ALLOWED_STATUSES = {"draft", "active", "stable", "deprecated", "archived"}
PROMPT_REQUIRED = {
    "id",
    "title",
    "type",
    "status",
    "version",
    "summary",
    "tags",
    "depends_on",
    "last_reviewed",
}
SKILL_META_REQUIRED = {
    "id",
    "title",
    "type",
    "status",
    "version",
    "summary",
    "tags",
    "depends_on",
    "last_reviewed",
    "source_blueprint",
    "input_contract",
    "output_contract",
}
SKILL_FRONTMATTER_REQUIRED = {"name", "description"}
RECOMMENDED = {"portability", "adapter_support", "runtime_dependencies", "tool_dependencies"}
PORTABILITY_PRIORITY_PROMPT_IDS = {
    "mh-master-prompt-library-orchestrator",
    "mh-blueprint-prompt-library-curator",
    "mh-blueprint-onboarding-router",
    "mh-blueprint-catalog-validator",
    "mh-blueprint-skill-packager",
    "mh-blueprint-adapter-mapper",
}
TEXT = {
    "tr": {
        "missing_frontmatter": "Missing frontmatter: {path}",
        "missing_prompt_fields": "Missing prompt fields in {path}: {fields}",
        "invalid_prompt_type": "Invalid prompt type in {path}: {value}",
        "invalid_status": "Invalid status in {path}: {value}",
        "unknown_tag": "Unknown tag in {path}: {tag}",
        "recommended_prompt_field": "Recommended prompt field missing in {path}: {field}",
        "duplicate_id": "Duplicate ID: {item_id} in {left} and {right}",
        "missing_skill_meta_fields": "Missing skill meta fields in {path}: {fields}",
        "invalid_skill_type": "Invalid skill type in {path}: {value}",
        "recommended_skill_field": "Recommended skill field missing in {path}: {field}",
        "broken_source_blueprint": "Broken source_blueprint in {path}: {value}",
        "missing_skill_md": "Missing SKILL.md next to {path}",
        "missing_skill_frontmatter": "Missing SKILL.md frontmatter: {path}",
        "missing_skill_fields": "Missing SKILL.md fields in {path}: {fields}",
        "broken_depends_on": "Broken depends_on in {path}: {dep}",
        "failed": "Metadata validation failed:",
        "passed": "Metadata validation passed.",
        "warnings": "Warnings:",
    },
    "en": {
        "missing_frontmatter": "Missing frontmatter: {path}",
        "missing_prompt_fields": "Missing prompt fields in {path}: {fields}",
        "invalid_prompt_type": "Invalid prompt type in {path}: {value}",
        "invalid_status": "Invalid status in {path}: {value}",
        "unknown_tag": "Unknown tag in {path}: {tag}",
        "recommended_prompt_field": "Recommended prompt field missing in {path}: {field}",
        "duplicate_id": "Duplicate ID: {item_id} in {left} and {right}",
        "missing_skill_meta_fields": "Missing skill meta fields in {path}: {fields}",
        "invalid_skill_type": "Invalid skill type in {path}: {value}",
        "recommended_skill_field": "Recommended skill field missing in {path}: {field}",
        "broken_source_blueprint": "Broken source_blueprint in {path}: {value}",
        "missing_skill_md": "Missing SKILL.md next to {path}",
        "missing_skill_frontmatter": "Missing SKILL.md frontmatter: {path}",
        "missing_skill_fields": "Missing SKILL.md fields in {path}: {fields}",
        "broken_depends_on": "Broken depends_on in {path}: {dep}",
        "failed": "Metadata validation failed:",
        "passed": "Metadata validation passed.",
        "warnings": "Warnings:",
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate prompt and skill metadata.")
    add_locale_argument(parser)
    return parser


def portability_warning_targets_prompt(data: dict) -> bool:
    return data.get("id") in PORTABILITY_PRIORITY_PROMPT_IDS


def normalize_dep_list(value: object) -> list[str]:
    return normalize_list(value)


def normalize_tag_list(value: object) -> list[str]:
    return normalize_list(value)


def allowed_tags(taxonomy_path: Path) -> set[str]:
    tags: set[str] = set()
    for line in read_text(taxonomy_path).splitlines():
        match = re.match(r"^\| `([^`]+)` \|", line.strip())
        if match:
            tags.add(match.group(1))
    return tags


def main() -> int:
    args = build_parser().parse_args()
    text = TEXT[args.locale]
    content_root = locale_root(args.locale)
    taxonomy_path = content_root / "catalog" / "taxonomy.md"

    errors: list[str] = []
    warnings: list[str] = []
    all_ids: dict[str, Path] = {}
    taxonomy_tags = allowed_tags(taxonomy_path)

    prompt_files = list((content_root / "prompts").rglob("*.md"))
    for path in prompt_files:
        data = parse_frontmatter(path)
        if not data:
            errors.append(text["missing_frontmatter"].format(path=display_path(path)))
            continue
        missing = sorted(PROMPT_REQUIRED - data.keys())
        if missing:
            errors.append(text["missing_prompt_fields"].format(path=display_path(path), fields=", ".join(missing)))
        if data.get("type") not in ALLOWED_PROMPT_TYPES:
            errors.append(text["invalid_prompt_type"].format(path=display_path(path), value=data.get("type")))
        if data.get("status") not in ALLOWED_STATUSES:
            errors.append(text["invalid_status"].format(path=display_path(path), value=data.get("status")))
        for tag in normalize_tag_list(data.get("tags", [])):
            if tag not in taxonomy_tags:
                errors.append(text["unknown_tag"].format(path=display_path(path), tag=tag))
        if portability_warning_targets_prompt(data):
            for field in sorted(RECOMMENDED - data.keys()):
                warnings.append(text["recommended_prompt_field"].format(path=display_path(path), field=field))
        item_id = data.get("id")
        if item_id:
            if item_id in all_ids:
                errors.append(
                    text["duplicate_id"].format(
                        item_id=item_id,
                        left=display_path(path),
                        right=display_path(all_ids[item_id]),
                    )
                )
            else:
                all_ids[item_id] = path

    skill_meta_files = list((content_root / "skills").rglob("meta.yaml"))
    for path in skill_meta_files:
        data = parse_meta_yaml(path)
        missing = sorted(SKILL_META_REQUIRED - data.keys())
        if missing:
            errors.append(text["missing_skill_meta_fields"].format(path=display_path(path), fields=", ".join(missing)))
        if data.get("type") != "skill":
            errors.append(text["invalid_skill_type"].format(path=display_path(path), value=data.get("type")))
        if data.get("status") not in ALLOWED_STATUSES:
            errors.append(text["invalid_status"].format(path=display_path(path), value=data.get("status")))
        for tag in normalize_tag_list(data.get("tags", [])):
            if tag not in taxonomy_tags:
                errors.append(text["unknown_tag"].format(path=display_path(path), tag=tag))
        for field in sorted(RECOMMENDED - data.keys()):
            warnings.append(text["recommended_skill_field"].format(path=display_path(path), field=field))
        item_id = data.get("id")
        if item_id:
            if item_id in all_ids:
                errors.append(
                    text["duplicate_id"].format(
                        item_id=item_id,
                        left=display_path(path),
                        right=display_path(all_ids[item_id]),
                    )
                )
            else:
                all_ids[item_id] = path
        source_blueprint = data.get("source_blueprint")
        if source_blueprint:
            blueprint_path = (path.parent / str(source_blueprint)).resolve()
            if not blueprint_path.exists():
                errors.append(text["broken_source_blueprint"].format(path=display_path(path), value=source_blueprint))

        skill_md = path.with_name("SKILL.md")
        if not skill_md.exists():
            errors.append(text["missing_skill_md"].format(path=display_path(path)))
        else:
            skill_data = parse_frontmatter(skill_md)
            if not skill_data:
                errors.append(text["missing_skill_frontmatter"].format(path=display_path(skill_md)))
            else:
                missing_skill_fields = sorted(SKILL_FRONTMATTER_REQUIRED - skill_data.keys())
                if missing_skill_fields:
                    errors.append(
                        text["missing_skill_fields"].format(
                            path=display_path(skill_md),
                            fields=", ".join(missing_skill_fields),
                        )
                    )

    for path in prompt_files:
        data = parse_frontmatter(path)
        for dep in normalize_dep_list(data.get("depends_on", [])):
            if dep and dep not in all_ids:
                errors.append(text["broken_depends_on"].format(path=display_path(path), dep=dep))

    for path in skill_meta_files:
        data = parse_meta_yaml(path)
        for dep in normalize_dep_list(data.get("depends_on", [])):
            if dep and dep not in all_ids:
                errors.append(text["broken_depends_on"].format(path=display_path(path), dep=dep))

    if errors:
        print(text["failed"])
        for item in errors:
            print(f"- {item}")
    else:
        print(text["passed"])

    if warnings:
        print(text["warnings"])
        for item in warnings:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
