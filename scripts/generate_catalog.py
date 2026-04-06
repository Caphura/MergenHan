from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from script_common import (
    add_locale_argument,
    locale_root,
    normalize_list,
    normalize_mapping,
    parse_frontmatter,
    parse_meta_yaml,
)

STATUS_ORDER = {
    "active": 0,
    "stable": 1,
    "draft": 2,
    "deprecated": 3,
    "archived": 4,
}
PROMPT_SECTION_ORDER = {
    "master": 0,
    "module": 1,
    "blueprint": 2,
}
TEXT = {
    "tr": {
        "prompt_catalog_title": "Prompt Catalog",
        "skill_catalog_title": "Skill Catalog",
        "dependency_catalog_title": "Dependency Catalog",
        "prompt_catalog_intro": "Bu katalog, repodaki aktif ve tarihsel prompt varliklarini insan-okunur bir indeks halinde listeler.",
        "prompt_catalog_note": "Not: Bu katalog `python scripts/generate_catalog.py` ile uretilir. Runtime'a ozel uyarlamalar `adapters/` katmaninda tutulur ve burada promptun kendisiyle karistirilmaz.",
        "skill_catalog_intro": "Bu katalog, `skills/` altindaki paketlenmis ve tekrar kullanilabilir hale getirilmis becerileri listeler.",
        "skill_catalog_note": "Not: Bu katalog `python scripts/generate_catalog.py` ile uretilir.",
        "dependency_catalog_intro": "Bu belge, cekirdek varliklar arasindaki bagimlilik iliskilerini ozetler. Adapter dosyalari bu katalogda cekirdek bagimlilik olarak sayilmaz; onlar uyumluluk katmanidir.",
        "dependency_catalog_note": "Not: Bu katalog `python scripts/generate_catalog.py` ile uretilir.",
        "ownership_title": "Sahiplik Notu",
        "ownership_notes": [
            "Adapter mapping'leri cekirdek dependency sahipligini degistirmez.",
            "Cekirdek ID'ler, blueprint kaynaklari ve `depends_on` zinciri `prompts/` ile `skills/` altinda sahiplenilmeye devam eder.",
            "Adapterler bu cekirdek sahipligi referans alir; yeni runtime destegi eklemek cekirdekte yeni bagimlilik sahibi yaratmaz.",
        ],
        "skills_to_blueprints": "Skills -> Blueprints",
        "blueprints_to_dependencies": "Blueprints -> Masters / Modules / Blueprints",
        "masters_to_modules": "Masters -> Modules",
        "modules_title": "Modules",
        "modules_note": "Moduller su anda cekirdek katalogda bagimsiz destek birimleri olarak listelenir; kataloglanan moduller icin ikincil bir `depends_on` iliskisi bulunmamaktadir.",
        "prompt_section_titles": {
            "master": "Master Prompts",
            "module": "Modules",
            "blueprint": "Skill Blueprints",
        },
        "prompt_headers": ["ID", "Baslik", "Durum", "Surum", "Etiketler", "Bagimliliklar", "Yol"],
        "skill_headers": ["ID", "Baslik", "Durum", "Surum", "Etiketler", "Kaynak Blueprint", "Adapter Support", "Dosyalar"],
        "skill_dependency_headers": ["Skill", "Baglidir", "Not"],
        "dependency_headers": ["Blueprint", "Bagimliliklar"],
        "master_headers": ["Master", "Bagimliliklar"],
        "packaged_skill_note": "Paketlenmis skill, kaynak blueprint bagini korur",
        "generated_label": "Catalogs generated:",
    },
    "en": {
        "prompt_catalog_title": "Prompt Catalog",
        "skill_catalog_title": "Skill Catalog",
        "dependency_catalog_title": "Dependency Catalog",
        "prompt_catalog_intro": "This catalog lists active and historical prompt assets in the repository as a human-readable index.",
        "prompt_catalog_note": "Note: This catalog is generated with `python scripts/generate_catalog.py`. Runtime-specific adaptations live in the `adapters/` layer and are not mixed with the prompt definition here.",
        "skill_catalog_intro": "This catalog lists packaged, reusable skills under `skills/`.",
        "skill_catalog_note": "Note: This catalog is generated with `python scripts/generate_catalog.py`.",
        "dependency_catalog_intro": "This document summarizes dependency relationships between core assets. Adapter files are not treated as core dependencies in this catalog; they are compatibility-layer material.",
        "dependency_catalog_note": "Note: This catalog is generated with `python scripts/generate_catalog.py`.",
        "ownership_title": "Ownership Notes",
        "ownership_notes": [
            "Adapter mappings do not change core dependency ownership.",
            "Core IDs, blueprint sources, and the `depends_on` chain continue to be owned under `prompts/` and `skills/`.",
            "Adapters reference that core ownership; adding support for a new runtime does not create a new dependency owner in the core layer.",
        ],
        "skills_to_blueprints": "Skills -> Blueprints",
        "blueprints_to_dependencies": "Blueprints -> Masters / Modules / Blueprints",
        "masters_to_modules": "Masters -> Modules",
        "modules_title": "Modules",
        "modules_note": "Modules are currently listed in the core catalog as independent support units; cataloged modules do not have a secondary `depends_on` relationship at this time.",
        "prompt_section_titles": {
            "master": "Master Prompts",
            "module": "Modules",
            "blueprint": "Skill Blueprints",
        },
        "prompt_headers": ["ID", "Title", "Status", "Version", "Tags", "Dependencies", "Path"],
        "skill_headers": ["ID", "Title", "Status", "Version", "Tags", "Source Blueprint", "Adapter Support", "Files"],
        "skill_dependency_headers": ["Skill", "Depends On", "Notes"],
        "dependency_headers": ["Blueprint", "Dependencies"],
        "master_headers": ["Master", "Dependencies"],
        "packaged_skill_note": "Packaged skill keeps its source blueprint link",
        "generated_label": "Catalogs generated:",
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate prompt, skill, and dependency catalogs.")
    add_locale_argument(parser)
    return parser


def relative_link(catalog_path: Path, target: Path) -> str:
    return Path(os.path.relpath(target, catalog_path.parent)).as_posix()


def code_cell(items: list[str]) -> str:
    if not items:
        return "`-`"
    return ", ".join(f"`{item}`" for item in items)


def format_path_link(catalog_path: Path, target: Path, content_root: Path) -> str:
    rel = relative_link(catalog_path, target)
    label = target.relative_to(content_root).as_posix()
    return f"[`{label}`]({rel})"


def status_sort_key(status: object) -> tuple[int, str]:
    status_text = str(status or "").strip()
    return (STATUS_ORDER.get(status_text, 99), status_text)


def prompt_sort_key(record: dict) -> tuple[int, tuple[int, str], str]:
    return (
        PROMPT_SECTION_ORDER.get(str(record.get("type", "")).strip(), 99),
        status_sort_key(record.get("status")),
        str(record.get("title", "")).lower(),
    )


def skill_sort_key(record: dict) -> tuple[tuple[int, str], str]:
    return (status_sort_key(record.get("status")), str(record.get("title", "")).lower())


def prompt_records(content_root: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted((content_root / "prompts").rglob("*.md")):
        data = parse_frontmatter(path)
        if not data:
            continue
        records.append(
            {
                "id": str(data.get("id", "")).strip(),
                "title": str(data.get("title", "")).strip(),
                "type": str(data.get("type", "")).strip(),
                "status": str(data.get("status", "")).strip(),
                "version": str(data.get("version", "")).strip(),
                "tags": normalize_list(data.get("tags")),
                "depends_on": normalize_list(data.get("depends_on")),
                "path": path,
            }
        )
    return sorted(records, key=prompt_sort_key)


def skill_records(content_root: Path) -> list[dict]:
    records: list[dict] = []
    for meta_path in sorted((content_root / "skills").rglob("meta.yaml")):
        data = parse_meta_yaml(meta_path)
        source_blueprint = str(data.get("source_blueprint", "")).strip()
        source_path = (meta_path.parent / source_blueprint).resolve() if source_blueprint else None
        source_blueprint_id = ""
        if source_path and source_path.exists():
            source_blueprint_id = str(parse_frontmatter(source_path).get("id", "")).strip()
        records.append(
            {
                "id": str(data.get("id", "")).strip(),
                "title": str(data.get("title", "")).strip(),
                "status": str(data.get("status", "")).strip(),
                "version": str(data.get("version", "")).strip(),
                "tags": normalize_list(data.get("tags")),
                "depends_on": normalize_list(data.get("depends_on")),
                "adapter_support": normalize_mapping(data.get("adapter_support")),
                "meta_path": meta_path,
                "skill_path": meta_path.with_name("SKILL.md"),
                "source_blueprint_path": source_path if source_path and source_path.exists() else None,
                "source_blueprint_id": source_blueprint_id,
            }
        )
    return sorted(records, key=skill_sort_key)


def render_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def write_catalog(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def adapter_support_cell(adapter_support: dict[str, str]) -> str:
    names = [name for name, state in adapter_support.items() if state and state.lower() != "unsupported"]
    return code_cell(names)


def generate_prompt_catalog(records: list[dict], content_root: Path, catalog_path: Path, locale: str) -> str:
    text = TEXT[locale]
    lines = [
        f"# {text['prompt_catalog_title']}",
        "",
        text["prompt_catalog_intro"],
        "",
        text["prompt_catalog_note"],
    ]
    for prompt_type in ("master", "module", "blueprint"):
        rows = []
        for record in records:
            if record["type"] != prompt_type:
                continue
            rows.append(
                [
                    f"`{record['id']}`",
                    record["title"] or "-",
                    f"`{record['status']}`" if record["status"] else "`-`",
                    f"`{record['version']}`" if record["version"] else "`-`",
                    code_cell(record["tags"]),
                    code_cell(record["depends_on"]),
                    format_path_link(catalog_path, record["path"], content_root),
                ]
            )
        lines.extend(
            [
                "",
                f"## {text['prompt_section_titles'][prompt_type]}",
                "",
                render_table(text["prompt_headers"], rows),
            ]
        )
    return "\n".join(lines)


def generate_skill_catalog(records: list[dict], content_root: Path, catalog_path: Path, locale: str) -> str:
    text = TEXT[locale]
    rows = []
    for record in records:
        source_cell = "`-`"
        if record["source_blueprint_path"]:
            source_cell = format_path_link(catalog_path, record["source_blueprint_path"], content_root)
        rows.append(
            [
                f"`{record['id']}`",
                record["title"] or "-",
                f"`{record['status']}`" if record["status"] else "`-`",
                f"`{record['version']}`" if record["version"] else "`-`",
                code_cell(record["tags"]),
                source_cell,
                adapter_support_cell(record["adapter_support"]),
                ", ".join(
                    [
                        format_path_link(catalog_path, record["skill_path"], content_root),
                        format_path_link(catalog_path, record["meta_path"], content_root),
                    ]
                ),
            ]
        )
    return "\n".join(
        [
            f"# {text['skill_catalog_title']}",
            "",
            text["skill_catalog_intro"],
            "",
            text["skill_catalog_note"],
            "",
            render_table(text["skill_headers"], rows),
        ]
    )


def generate_dependency_catalog(prompt_records_list: list[dict], skill_records_list: list[dict], locale: str) -> str:
    text = TEXT[locale]
    master_rows = []
    blueprint_rows = []
    for record in prompt_records_list:
        if record["type"] == "master":
            master_rows.append([f"`{record['id']}`", code_cell(record["depends_on"])])
        elif record["type"] == "blueprint":
            blueprint_rows.append([f"`{record['id']}`", code_cell(record["depends_on"])])

    skill_rows = []
    for record in skill_records_list:
        skill_rows.append(
            [
                f"`{record['id']}`",
                f"`{record['source_blueprint_id']}`" if record["source_blueprint_id"] else "`-`",
                text["packaged_skill_note"] if record["source_blueprint_id"] else "-",
            ]
        )

    return "\n".join(
        [
            f"# {text['dependency_catalog_title']}",
            "",
            text["dependency_catalog_intro"],
            "",
            text["dependency_catalog_note"],
            "",
            f"## {text['ownership_title']}",
            "",
            *[f"- {item}" for item in text["ownership_notes"]],
            "",
            f"## {text['skills_to_blueprints']}",
            "",
            render_table(text["skill_dependency_headers"], skill_rows),
            "",
            f"## {text['blueprints_to_dependencies']}",
            "",
            render_table(text["dependency_headers"], blueprint_rows),
            "",
            f"## {text['masters_to_modules']}",
            "",
            render_table(text["master_headers"], master_rows),
            "",
            f"## {text['modules_title']}",
            "",
            text["modules_note"],
        ]
    )


def main() -> int:
    args = build_parser().parse_args()
    content_root = locale_root(args.locale)
    prompt_catalog = content_root / "catalog" / "prompts.md"
    skill_catalog = content_root / "catalog" / "skills.md"
    dependency_catalog = content_root / "catalog" / "dependencies.md"

    prompts = prompt_records(content_root)
    skills = skill_records(content_root)

    write_catalog(prompt_catalog, generate_prompt_catalog(prompts, content_root, prompt_catalog, args.locale))
    write_catalog(skill_catalog, generate_skill_catalog(skills, content_root, skill_catalog, args.locale))
    write_catalog(dependency_catalog, generate_dependency_catalog(prompts, skills, args.locale))

    print(TEXT[args.locale]["generated_label"])
    print(f"- {prompt_catalog.relative_to(content_root)}")
    print(f"- {skill_catalog.relative_to(content_root)}")
    print(f"- {dependency_catalog.relative_to(content_root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
