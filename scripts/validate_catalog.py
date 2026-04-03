from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_CATALOG = ROOT / "catalog" / "prompts.md"
SKILL_CATALOG = ROOT / "catalog" / "skills.md"

TABLE_LINE_RE = re.compile(r"^\|.*\|$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


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
    match = FRONTMATTER_RE.match(read_text(path))
    if not match:
        return {}
    return parse_simple_yaml_block(match.group(1))


def parse_meta_yaml(path: Path) -> dict:
    return parse_simple_yaml_block(read_text(path))


def parse_catalog_rows(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in read_text(path).splitlines():
        stripped = line.strip()
        if not TABLE_LINE_RE.match(stripped):
            continue
        if set(stripped.replace("|", "").replace("-", "").replace(" ", "")) == set():
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0] == "ID":
            continue
        rows.append(cells)
    return rows


def catalog_links(cells: list[str]) -> list[str]:
    links: list[str] = []
    for cell in cells:
        links.extend(LINK_RE.findall(cell))
    return links


def relative_target(md_path: Path, link: str) -> Path:
    clean = link.split("#", 1)[0]
    return (md_path.parent / clean).resolve()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    prompt_rows = parse_catalog_rows(PROMPT_CATALOG)
    skill_rows = parse_catalog_rows(SKILL_CATALOG)

    prompt_ids: set[str] = set()
    for row in prompt_rows:
        catalog_id = row[0].strip("`")
        if catalog_id in prompt_ids:
            errors.append(f"Duplicate prompt catalog ID: {catalog_id}")
        prompt_ids.add(catalog_id)
        links = catalog_links(row)
        if not links:
            errors.append(f"Prompt catalog row missing file link: {catalog_id}")
            continue
        target = relative_target(PROMPT_CATALOG, links[0])
        if not target.exists():
            errors.append(f"Prompt catalog target missing: {catalog_id} -> {links[0]}")
            continue
        file_id = parse_frontmatter(target).get("id")
        if file_id and file_id != catalog_id:
            errors.append(f"Prompt catalog ID mismatch: {catalog_id} != {file_id} ({links[0]})")

    skill_ids: set[str] = set()
    for row in skill_rows:
        catalog_id = row[0].strip("`")
        if catalog_id in skill_ids:
            errors.append(f"Duplicate skill catalog ID: {catalog_id}")
        skill_ids.add(catalog_id)
        links = catalog_links(row)
        if not links:
            errors.append(f"Skill catalog row missing file link: {catalog_id}")
            continue
        meta_links = [link for link in links if link.endswith("meta.yaml")]
        if not meta_links:
            errors.append(f"Skill catalog row missing meta.yaml link: {catalog_id}")
            continue
        meta_target = relative_target(SKILL_CATALOG, meta_links[0])
        if not meta_target.exists():
            errors.append(f"Skill catalog target missing: {catalog_id} -> {meta_links[0]}")
            continue
        file_id = parse_meta_yaml(meta_target).get("id")
        if file_id and file_id != catalog_id:
            errors.append(f"Skill catalog ID mismatch: {catalog_id} != {file_id} ({meta_links[0]})")
        for link in links:
            target = relative_target(SKILL_CATALOG, link)
            if not target.exists():
                errors.append(f"Skill catalog link missing: {catalog_id} -> {link}")

    prompt_files = [path for path in (ROOT / "prompts").rglob("*.md")]
    skill_meta_files = [path for path in (ROOT / "skills").rglob("meta.yaml")]

    prompt_file_ids = {}
    for path in prompt_files:
        data = parse_frontmatter(path)
        file_id = data.get("id")
        if file_id:
            prompt_file_ids[file_id] = path

    skill_file_ids = {}
    for path in skill_meta_files:
        data = parse_meta_yaml(path)
        file_id = data.get("id")
        if file_id:
            skill_file_ids[file_id] = path

    for file_id, path in prompt_file_ids.items():
        if file_id not in prompt_ids:
            warnings.append(f"Prompt file missing from catalog: {file_id} ({path.relative_to(ROOT)})")
    for file_id, path in skill_file_ids.items():
        if file_id not in skill_ids:
            warnings.append(f"Skill file missing from catalog: {file_id} ({path.relative_to(ROOT)})")

    if errors:
        print("Catalog validation failed:")
        for item in errors:
            print(f"- {item}")
    else:
        print("Catalog validation passed.")

    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
