from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IGNORE_PREFIXES = ("http://", "https://", "mailto:")


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp1254", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", raw, 0, 1, f"Could not decode {path}")


def markdown_files() -> list[Path]:
    files = [ROOT / "README.md"]
    for folder in ["catalog", "docs", "examples", "prompts", "skills", "templates", "adapters"]:
        files.extend((ROOT / folder).rglob("*.md"))
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
    errors: list[str] = []

    for path in markdown_files():
        text = read_text(path)
        for link in LINK_RE.findall(text):
            if link.startswith("#") or link.startswith(IGNORE_PREFIXES):
                continue
            clean = link.split("#", 1)[0]
            target = (path.parent / clean).resolve()
            if not target.exists():
                errors.append(f"Broken link in {path.relative_to(ROOT)}: {link}")

    if errors:
        print("Link check failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
