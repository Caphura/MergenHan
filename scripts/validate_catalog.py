from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from script_common import add_locale_argument, display_path, locale_root, parse_frontmatter, parse_meta_yaml, read_text

TABLE_LINE_RE = re.compile(r"^\|.*\|$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
TEXT = {
    "tr": {
        "failed": "Catalog validation failed:",
        "passed": "Catalog validation passed.",
        "warnings": "Warnings:",
        "duplicate_prompt_id": "Duplicate prompt catalog ID: {catalog_id}",
        "prompt_row_missing_file_link": "Prompt catalog row missing file link: {catalog_id}",
        "prompt_target_missing": "Prompt catalog target missing: {catalog_id} -> {link}",
        "prompt_id_mismatch": "Prompt catalog ID mismatch: {catalog_id} != {file_id} ({link})",
        "duplicate_skill_id": "Duplicate skill catalog ID: {catalog_id}",
        "skill_row_missing_file_link": "Skill catalog row missing file link: {catalog_id}",
        "skill_row_missing_meta_link": "Skill catalog row missing meta.yaml link: {catalog_id}",
        "skill_target_missing": "Skill catalog target missing: {catalog_id} -> {link}",
        "skill_id_mismatch": "Skill catalog ID mismatch: {catalog_id} != {file_id} ({link})",
        "skill_link_missing": "Skill catalog link missing: {catalog_id} -> {link}",
        "prompt_missing_from_catalog": "Prompt file missing from catalog: {file_id} ({path})",
        "skill_missing_from_catalog": "Skill file missing from catalog: {file_id} ({path})",
    },
    "en": {
        "failed": "Catalog validation failed:",
        "passed": "Catalog validation passed.",
        "warnings": "Warnings:",
        "duplicate_prompt_id": "Duplicate prompt catalog ID: {catalog_id}",
        "prompt_row_missing_file_link": "Prompt catalog row missing file link: {catalog_id}",
        "prompt_target_missing": "Prompt catalog target missing: {catalog_id} -> {link}",
        "prompt_id_mismatch": "Prompt catalog ID mismatch: {catalog_id} != {file_id} ({link})",
        "duplicate_skill_id": "Duplicate skill catalog ID: {catalog_id}",
        "skill_row_missing_file_link": "Skill catalog row missing file link: {catalog_id}",
        "skill_row_missing_meta_link": "Skill catalog row missing meta.yaml link: {catalog_id}",
        "skill_target_missing": "Skill catalog target missing: {catalog_id} -> {link}",
        "skill_id_mismatch": "Skill catalog ID mismatch: {catalog_id} != {file_id} ({link})",
        "skill_link_missing": "Skill catalog link missing: {catalog_id} -> {link}",
        "prompt_missing_from_catalog": "Prompt file missing from catalog: {file_id} ({path})",
        "skill_missing_from_catalog": "Skill file missing from catalog: {file_id} ({path})",
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate prompt and skill catalogs.")
    add_locale_argument(parser)
    return parser


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
    args = build_parser().parse_args()
    text = TEXT[args.locale]
    content_root = locale_root(args.locale)
    prompt_catalog = content_root / "catalog" / "prompts.md"
    skill_catalog = content_root / "catalog" / "skills.md"

    errors: list[str] = []
    warnings: list[str] = []

    prompt_rows = parse_catalog_rows(prompt_catalog)
    skill_rows = parse_catalog_rows(skill_catalog)

    prompt_ids: set[str] = set()
    for row in prompt_rows:
        catalog_id = row[0].strip("`")
        if catalog_id in prompt_ids:
            errors.append(text["duplicate_prompt_id"].format(catalog_id=catalog_id))
        prompt_ids.add(catalog_id)
        links = catalog_links(row)
        if not links:
            errors.append(text["prompt_row_missing_file_link"].format(catalog_id=catalog_id))
            continue
        target = relative_target(prompt_catalog, links[0])
        if not target.exists():
            errors.append(text["prompt_target_missing"].format(catalog_id=catalog_id, link=links[0]))
            continue
        file_id = parse_frontmatter(target).get("id")
        if file_id and file_id != catalog_id:
            errors.append(text["prompt_id_mismatch"].format(catalog_id=catalog_id, file_id=file_id, link=links[0]))

    skill_ids: set[str] = set()
    for row in skill_rows:
        catalog_id = row[0].strip("`")
        if catalog_id in skill_ids:
            errors.append(text["duplicate_skill_id"].format(catalog_id=catalog_id))
        skill_ids.add(catalog_id)
        links = catalog_links(row)
        if not links:
            errors.append(text["skill_row_missing_file_link"].format(catalog_id=catalog_id))
            continue
        meta_links = [link for link in links if link.endswith("meta.yaml")]
        if not meta_links:
            errors.append(text["skill_row_missing_meta_link"].format(catalog_id=catalog_id))
            continue
        meta_target = relative_target(skill_catalog, meta_links[0])
        if not meta_target.exists():
            errors.append(text["skill_target_missing"].format(catalog_id=catalog_id, link=meta_links[0]))
            continue
        file_id = parse_meta_yaml(meta_target).get("id")
        if file_id and file_id != catalog_id:
            errors.append(text["skill_id_mismatch"].format(catalog_id=catalog_id, file_id=file_id, link=meta_links[0]))
        for link in links:
            target = relative_target(skill_catalog, link)
            if not target.exists():
                errors.append(text["skill_link_missing"].format(catalog_id=catalog_id, link=link))

    prompt_files = [path for path in (content_root / "prompts").rglob("*.md")]
    skill_meta_files = [path for path in (content_root / "skills").rglob("meta.yaml")]

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
            errors.append(text["prompt_missing_from_catalog"].format(file_id=file_id, path=display_path(path)))
    for file_id, path in skill_file_ids.items():
        if file_id not in skill_ids:
            errors.append(text["skill_missing_from_catalog"].format(file_id=file_id, path=display_path(path)))

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
