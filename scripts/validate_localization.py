from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from script_common import (
    SUPPORTED_LOCALES,
    locale_root,
    normalize_list,
    normalize_mapping,
    parse_frontmatter,
    parse_meta_yaml,
    read_text,
)

SURFACE_DIRS = ["README.md", "catalog", "docs", "examples", "prompts", "skills", "adapters", "templates"]
TRACKED_SUFFIXES = {".md", ".yaml", ".yml", ".json"}
PROMPT_INVARIANTS = {
    "id",
    "type",
    "status",
    "version",
    "tags",
    "depends_on",
    "last_reviewed",
    "portability",
    "adapter_support",
    "runtime_dependencies",
    "tool_dependencies",
}
SKILL_META_INVARIANTS = {
    "id",
    "type",
    "status",
    "version",
    "tags",
    "depends_on",
    "last_reviewed",
    "source_blueprint",
    "portability",
    "adapter_support",
    "runtime_dependencies",
    "tool_dependencies",
}
TEXT = {
    "missing_target_file": "Missing target file: {path}",
    "unexpected_target_file": "Unexpected target-only file: {path}",
    "missing_target_dir": "Missing target directory: {path}",
    "unexpected_target_dir": "Unexpected target-only directory: {path}",
    "prompt_invariant_mismatch": "Prompt invariant mismatch for {path}: {field} != {target_value} (source={source_value})",
    "skill_invariant_mismatch": "Skill invariant mismatch for {path}: {field} != {target_value} (source={source_value})",
    "skill_name_mismatch": "Skill frontmatter name mismatch for {path}: {source_value} != {target_value}",
    "json_keys_mismatch": "JSON key mismatch for {path}",
    "failed": "Localization validation failed:",
    "passed": "Localization validation passed.",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate TR/EN localization mirror integrity.")
    parser.add_argument("--source-locale", choices=SUPPORTED_LOCALES, default="en")
    parser.add_argument("--target-locale", choices=SUPPORTED_LOCALES, default="tr")
    return parser


def tracked_files(content_root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for surface in SURFACE_DIRS:
        current = content_root / surface
        if current.is_file():
            files[surface] = current
            continue
        for path in current.rglob("*"):
            if path.is_file() and path.suffix.lower() in TRACKED_SUFFIXES:
                files[path.relative_to(content_root).as_posix()] = path
    return files


def tracked_dirs(content_root: Path) -> set[str]:
    dirs: set[str] = set()
    for surface in SURFACE_DIRS:
        current = content_root / surface
        if current.is_dir():
            dirs.add(surface)
            for path in current.rglob("*"):
                if path.is_dir():
                    dirs.add(path.relative_to(content_root).as_posix())
    return dirs


def canonical_value(value: object) -> object:
    if isinstance(value, list):
        return normalize_list(value)
    if isinstance(value, dict):
        return normalize_mapping(value)
    if isinstance(value, str):
        return value.strip()
    return value


def compare_invariants(errors: list[str], relative_path: str, source_data: dict, target_data: dict, fields: set[str], label: str) -> None:
    for field in sorted(fields):
        source_value = canonical_value(source_data.get(field))
        target_value = canonical_value(target_data.get(field))
        if source_value != target_value:
            errors.append(
                TEXT[f"{label}_invariant_mismatch"].format(
                    path=relative_path,
                    field=field,
                    source_value=source_value,
                    target_value=target_value,
                )
            )


def normalized_json(path: Path) -> object:
    return json.loads(read_text(path))


def main() -> int:
    args = build_parser().parse_args()
    if args.source_locale == args.target_locale:
        print("Source and target locales must be different.", file=sys.stderr)
        return 1

    source_root = locale_root(args.source_locale)
    target_root = locale_root(args.target_locale)
    errors: list[str] = []

    source_files = tracked_files(source_root)
    target_files = tracked_files(target_root)
    source_dirs = tracked_dirs(source_root)
    target_dirs = tracked_dirs(target_root)

    for relative_dir in sorted(source_dirs - target_dirs):
        errors.append(TEXT["missing_target_dir"].format(path=relative_dir))
    for relative_dir in sorted(target_dirs - source_dirs):
        errors.append(TEXT["unexpected_target_dir"].format(path=relative_dir))

    for relative_path, source_path in source_files.items():
        target_path = target_files.get(relative_path)
        if target_path is None:
            errors.append(TEXT["missing_target_file"].format(path=relative_path))
            continue

        if relative_path.startswith("prompts/"):
            compare_invariants(
                errors,
                relative_path,
                parse_frontmatter(source_path),
                parse_frontmatter(target_path),
                PROMPT_INVARIANTS,
                "prompt",
            )
        elif relative_path.startswith("skills/") and relative_path.endswith("meta.yaml"):
            compare_invariants(
                errors,
                relative_path,
                parse_meta_yaml(source_path),
                parse_meta_yaml(target_path),
                SKILL_META_INVARIANTS,
                "skill",
            )
        elif relative_path.startswith("skills/") and relative_path.endswith("SKILL.md"):
            source_skill = parse_frontmatter(source_path)
            target_skill = parse_frontmatter(target_path)
            if canonical_value(source_skill.get("name")) != canonical_value(target_skill.get("name")):
                errors.append(
                    TEXT["skill_name_mismatch"].format(
                        path=relative_path,
                        source_value=source_skill.get("name"),
                        target_value=target_skill.get("name"),
                    )
                )
        elif relative_path.startswith("templates/") and relative_path.endswith(".md"):
            source_template = parse_frontmatter(source_path)
            target_template = parse_frontmatter(target_path)
            compare_invariants(errors, relative_path, source_template, target_template, PROMPT_INVARIANTS, "prompt")
            if relative_path.endswith("SKILL.md") and canonical_value(source_template.get("name")) != canonical_value(target_template.get("name")):
                errors.append(
                    TEXT["skill_name_mismatch"].format(
                        path=relative_path,
                        source_value=source_template.get("name"),
                        target_value=target_template.get("name"),
                    )
                )
        elif relative_path.endswith(".json"):
            source_json = normalized_json(source_path)
            target_json = normalized_json(target_path)
            if isinstance(source_json, dict) and isinstance(target_json, dict):
                if sorted(source_json.keys()) != sorted(target_json.keys()):
                    errors.append(TEXT["json_keys_mismatch"].format(path=relative_path))

    for relative_path in sorted(target_files.keys() - source_files.keys()):
        errors.append(TEXT["unexpected_target_file"].format(path=relative_path))

    if errors:
        print(TEXT["failed"])
        for item in errors:
            print(f"- {item}")
        return 1

    print(TEXT["passed"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
