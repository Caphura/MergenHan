from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from script_common import add_locale_argument, display_path, locale_root, read_text

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IGNORE_PREFIXES = ("http://", "https://", "mailto:")
TEXT = {
    "tr": {
        "broken": "Broken link in {path}: {link}",
        "failed": "Link check failed:",
        "passed": "Link check passed.",
    },
    "en": {
        "broken": "Broken link in {path}: {link}",
        "failed": "Link check failed:",
        "passed": "Link check passed.",
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check relative markdown links.")
    add_locale_argument(parser)
    return parser


def markdown_files(content_root: Path) -> list[Path]:
    files = [content_root / "README.md", content_root / "AGENTS.md"]
    for folder in ["catalog", "docs", "examples", "prompts", "skills", "templates", "adapters"]:
        files.extend((content_root / folder).rglob("*.md"))
    seen: set[Path] = set()
    result: list[Path] = []
    for path in files:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        result.append(path)
    return result


def main() -> int:
    args = build_parser().parse_args()
    text = TEXT[args.locale]
    content_root = locale_root(args.locale)
    errors: list[str] = []

    for path in markdown_files(content_root):
        current_text = read_text(path)
        for link in LINK_RE.findall(current_text):
            if link.startswith("#") or link.startswith(IGNORE_PREFIXES):
                continue
            clean = link.split("#", 1)[0]
            target = (path.parent / clean).resolve()
            if not target.exists():
                errors.append(text["broken"].format(path=display_path(path), link=link))

    if errors:
        print(text["failed"])
        for item in errors:
            print(f"- {item}")
        return 1

    print(text["passed"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

