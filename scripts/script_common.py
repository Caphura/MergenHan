from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_LOCALE = "en"
SUPPORTED_LOCALES = ("en", "tr")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)


def add_locale_argument(parser: argparse.ArgumentParser, *, default: str = CANONICAL_LOCALE) -> None:
    parser.add_argument(
        "--locale",
        choices=SUPPORTED_LOCALES,
        default=default,
        help=f"Content locale. Defaults to '{default}'.",
    )


def ensure_supported_locale(locale: str) -> str:
    if locale not in SUPPORTED_LOCALES:
        raise ValueError(f"Unsupported locale: {locale}")
    return locale


def locale_root(locale: str) -> Path:
    ensure_supported_locale(locale)
    return ROOT if locale == CANONICAL_LOCALE else ROOT / locale


def display_path(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


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
    text = read_text(path).replace("\r\n", "\n")
    match = FRONTMATTER_RE.match(text)
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
