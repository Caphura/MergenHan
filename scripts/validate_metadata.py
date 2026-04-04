from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)
TAXONOMY_PATH = ROOT / "catalog" / "taxonomy.md"
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


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp1254", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", raw, 0, 1, f"Could not decode {path}")


def parse_simple_yaml_block(block: str) -> dict:
    data: dict[str, object] = {}
    current_list_key: str | None = None
    current_map_key: str | None = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, []).append(line[4:].strip())
            continue
        if line.startswith("  ") and current_map_key and ":" in line:
            key, value = line.strip().split(":", 1)
            current_value = data.get(current_map_key)
            if not isinstance(current_value, dict):
                current_value = {}
                data[current_map_key] = current_value
            current_value[key.strip()] = value.strip()
            continue
        if ":" not in line:
            current_list_key = None
            current_map_key = None
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "[]":
            data[key] = []
            current_list_key = None
            current_map_key = None
            continue
        if value == "{}":
            data[key] = {}
            current_list_key = None
            current_map_key = None
            continue
        if not value:
            current_list_key = key
            current_map_key = key
            if key not in data:
                data[key] = []
            continue
        data[key] = value
        current_list_key = None
        current_map_key = None
    return data


def parse_frontmatter(path: Path) -> dict:
    text = read_text(path).replace("\r\n", "\n")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    return parse_simple_yaml_block(match.group(1))


def parse_meta_yaml(path: Path) -> dict:
    return parse_simple_yaml_block(read_text(path))


def portability_warning_targets_prompt(data: dict) -> bool:
    return data.get("id") in PORTABILITY_PRIORITY_PROMPT_IDS


def normalize_dep_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    if isinstance(value, str):
        return [value] if value else []
    return []


def normalize_tag_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [item.strip() for item in value if isinstance(item, str) and item.strip()]
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    return []


def allowed_tags() -> set[str]:
    tags: set[str] = set()
    for line in read_text(TAXONOMY_PATH).splitlines():
        match = re.match(r"^\| `([^`]+)` \|", line.strip())
        if match:
            tags.add(match.group(1))
    return tags


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    all_ids: dict[str, Path] = {}
    taxonomy_tags = allowed_tags()

    prompt_files = list((ROOT / "prompts").rglob("*.md"))
    for path in prompt_files:
        data = parse_frontmatter(path)
        if not data:
            errors.append(f"Missing frontmatter: {path.relative_to(ROOT)}")
            continue
        missing = sorted(PROMPT_REQUIRED - data.keys())
        if missing:
            errors.append(f"Missing prompt fields in {path.relative_to(ROOT)}: {', '.join(missing)}")
        if data.get("type") not in ALLOWED_PROMPT_TYPES:
            errors.append(f"Invalid prompt type in {path.relative_to(ROOT)}: {data.get('type')}")
        if data.get("status") not in ALLOWED_STATUSES:
            errors.append(f"Invalid status in {path.relative_to(ROOT)}: {data.get('status')}")
        for tag in normalize_tag_list(data.get("tags", [])):
            if tag not in taxonomy_tags:
                errors.append(f"Unknown tag in {path.relative_to(ROOT)}: {tag}")
        if portability_warning_targets_prompt(data):
            for field in sorted(RECOMMENDED - data.keys()):
                warnings.append(f"Recommended prompt field missing in {path.relative_to(ROOT)}: {field}")
        item_id = data.get("id")
        if item_id:
            if item_id in all_ids:
                errors.append(f"Duplicate ID: {item_id} in {path.relative_to(ROOT)} and {all_ids[item_id].relative_to(ROOT)}")
            else:
                all_ids[item_id] = path

    skill_meta_files = list((ROOT / "skills").rglob("meta.yaml"))
    for path in skill_meta_files:
        data = parse_meta_yaml(path)
        missing = sorted(SKILL_META_REQUIRED - data.keys())
        if missing:
            errors.append(f"Missing skill meta fields in {path.relative_to(ROOT)}: {', '.join(missing)}")
        if data.get("type") != "skill":
            errors.append(f"Invalid skill type in {path.relative_to(ROOT)}: {data.get('type')}")
        if data.get("status") not in ALLOWED_STATUSES:
            errors.append(f"Invalid status in {path.relative_to(ROOT)}: {data.get('status')}")
        for tag in normalize_tag_list(data.get("tags", [])):
            if tag not in taxonomy_tags:
                errors.append(f"Unknown tag in {path.relative_to(ROOT)}: {tag}")
        for field in sorted(RECOMMENDED - data.keys()):
            warnings.append(f"Recommended skill field missing in {path.relative_to(ROOT)}: {field}")
        item_id = data.get("id")
        if item_id:
            if item_id in all_ids:
                errors.append(f"Duplicate ID: {item_id} in {path.relative_to(ROOT)} and {all_ids[item_id].relative_to(ROOT)}")
            else:
                all_ids[item_id] = path
        source_blueprint = data.get("source_blueprint")
        if source_blueprint:
            blueprint_path = (path.parent / str(source_blueprint)).resolve()
            if not blueprint_path.exists():
                errors.append(f"Broken source_blueprint in {path.relative_to(ROOT)}: {source_blueprint}")

        skill_md = path.with_name("SKILL.md")
        if not skill_md.exists():
            errors.append(f"Missing SKILL.md next to {path.relative_to(ROOT)}")
        else:
            skill_data = parse_frontmatter(skill_md)
            if not skill_data:
                errors.append(f"Missing SKILL.md frontmatter: {skill_md.relative_to(ROOT)}")
            else:
                missing_skill_fields = sorted(SKILL_FRONTMATTER_REQUIRED - skill_data.keys())
                if missing_skill_fields:
                    errors.append(
                        f"Missing SKILL.md fields in {skill_md.relative_to(ROOT)}: {', '.join(missing_skill_fields)}"
                    )

    for path in prompt_files:
        data = parse_frontmatter(path)
        for dep in normalize_dep_list(data.get("depends_on", [])):
            if dep and dep not in all_ids:
                errors.append(f"Broken depends_on in {path.relative_to(ROOT)}: {dep}")

    for path in skill_meta_files:
        data = parse_meta_yaml(path)
        for dep in normalize_dep_list(data.get("depends_on", [])):
            if dep and dep not in all_ids:
                errors.append(f"Broken depends_on in {path.relative_to(ROOT)}: {dep}")

    if errors:
        print("Metadata validation failed:")
        for item in errors:
            print(f"- {item}")
    else:
        print("Metadata validation passed.")

    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
