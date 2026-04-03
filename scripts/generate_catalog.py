from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_CATALOG = ROOT / "catalog" / "prompts.md"
SKILL_CATALOG = ROOT / "catalog" / "skills.md"
DEPENDENCY_CATALOG = ROOT / "catalog" / "dependencies.md"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
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
PROMPT_SECTION_TITLES = {
    "master": "Master Prompts",
    "module": "Modules",
    "blueprint": "Skill Blueprints",
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
        if not line or line.lstrip().startswith("#"):
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


def normalize_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [item.strip() for item in value if isinstance(item, str) and item.strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_mapping(value: object) -> dict[str, str]:
    if isinstance(value, dict):
        return {
            str(key).strip(): str(raw_value).strip()
            for key, raw_value in value.items()
            if str(key).strip() and str(raw_value).strip()
        }
    return {}


def relative_link(catalog_path: Path, target: Path) -> str:
    return Path(os.path.relpath(target, catalog_path.parent)).as_posix()


def code_cell(items: list[str]) -> str:
    if not items:
        return "`-`"
    return ", ".join(f"`{item}`" for item in items)


def format_path_link(catalog_path: Path, target: Path) -> str:
    rel = relative_link(catalog_path, target)
    label = target.relative_to(ROOT).as_posix()
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


def prompt_records() -> list[dict]:
    records: list[dict] = []
    for path in sorted((ROOT / "prompts").rglob("*.md")):
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


def skill_records() -> list[dict]:
    records: list[dict] = []
    for meta_path in sorted((ROOT / "skills").rglob("meta.yaml")):
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
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def generate_prompt_catalog(records: list[dict]) -> str:
    lines = [
        "# Prompt Catalog",
        "",
        "Bu katalog, repodaki aktif ve tarihsel prompt varliklarini insan-okunur bir indeks halinde listeler.",
        "",
        "Not: Bu katalog `python scripts/generate_catalog.py` ile uretilir. Runtime'a ozel uyarlamalar `adapters/` katmaninda tutulur ve burada promptun kendisiyle karistirilmaz.",
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
                    format_path_link(PROMPT_CATALOG, record["path"]),
                ]
            )
        lines.extend(
            [
                "",
                f"## {PROMPT_SECTION_TITLES[prompt_type]}",
                "",
                render_table(
                    ["ID", "Baslik", "Durum", "Surum", "Etiketler", "Bagimliliklar", "Yol"],
                    rows,
                ),
            ]
        )
    return "\n".join(lines)


def adapter_support_cell(adapter_support: dict[str, str]) -> str:
    names = [name for name, state in adapter_support.items() if state and state.lower() != "unsupported"]
    return code_cell(names)


def generate_skill_catalog(records: list[dict]) -> str:
    rows = []
    for record in records:
        source_cell = "`-`"
        if record["source_blueprint_path"]:
            source_cell = format_path_link(SKILL_CATALOG, record["source_blueprint_path"])
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
                        format_path_link(SKILL_CATALOG, record["skill_path"]),
                        format_path_link(SKILL_CATALOG, record["meta_path"]),
                    ]
                ),
            ]
        )
    return "\n".join(
        [
            "# Skill Catalog",
            "",
            "Bu katalog, `skills/` altindaki paketlenmis ve tekrar kullanilabilir hale getirilmis becerileri listeler.",
            "",
            "Not: Bu katalog `python scripts/generate_catalog.py` ile uretilir.",
            "",
            render_table(
                ["ID", "Baslik", "Durum", "Surum", "Etiketler", "Kaynak Blueprint", "Adapter Support", "Dosyalar"],
                rows,
            ),
        ]
    )


def generate_dependency_catalog(prompt_records_list: list[dict], skill_records_list: list[dict]) -> str:
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
                "Paketlenmis skill, kaynak blueprint bagini korur" if record["source_blueprint_id"] else "-",
            ]
        )

    return "\n".join(
        [
            "# Dependency Catalog",
            "",
            "Bu belge, cekirdek varliklar arasindaki bagimlilik iliskilerini ozetler. Adapter dosyalari bu katalogda cekirdek bagimlilik olarak sayilmaz; onlar uyumluluk katmanidir.",
            "",
            "Not: Bu katalog `python scripts/generate_catalog.py` ile uretilir.",
            "",
            "## Sahiplik Notu",
            "",
            "- Adapter mapping'leri cekirdek dependency sahipligini degistirmez.",
            "- Cekirdek ID'ler, blueprint kaynaklari ve `depends_on` zinciri `prompts/` ile `skills/` altinda sahiplenilmeye devam eder.",
            "- Adapterler bu cekirdek sahipligi referans alir; yeni runtime destegi eklemek cekirdekte yeni bagimlilik sahibi yaratmaz.",
            "",
            "## Skills -> Blueprints",
            "",
            render_table(["Skill", "Baglidir", "Not"], skill_rows),
            "",
            "## Blueprints -> Masters / Modules / Blueprints",
            "",
            render_table(["Blueprint", "Bagimliliklar"], blueprint_rows),
            "",
            "## Masters -> Modules",
            "",
            render_table(["Master", "Bagimliliklar"], master_rows),
            "",
            "## Modules",
            "",
            "Moduller su anda cekirdek katalogda bagimsiz destek birimleri olarak listelenir; kataloglanan moduller icin ikincil bir `depends_on` iliskisi bulunmamaktadir.",
        ]
    )


def main() -> int:
    prompts = prompt_records()
    skills = skill_records()

    write_catalog(PROMPT_CATALOG, generate_prompt_catalog(prompts))
    write_catalog(SKILL_CATALOG, generate_skill_catalog(skills))
    write_catalog(DEPENDENCY_CATALOG, generate_dependency_catalog(prompts, skills))

    print("Catalogs generated:")
    print(f"- {PROMPT_CATALOG.relative_to(ROOT)}")
    print(f"- {SKILL_CATALOG.relative_to(ROOT)}")
    print(f"- {DEPENDENCY_CATALOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
