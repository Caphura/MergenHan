from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

from script_common import CANONICAL_LOCALE, ROOT, SUPPORTED_LOCALES, locale_root, read_text

TEMPLATES = {
    "master": ROOT / "templates" / "master-prompt.md",
    "module": ROOT / "templates" / "module-prompt.md",
    "blueprint": ROOT / "templates" / "skill-blueprint.md",
}
TITLE_PLACEHOLDERS = {
    "master": "Your Master Prompt Title",
    "module": "Your Module Title",
    "blueprint": "Your Skill Blueprint Title",
}
ID_PLACEHOLDERS = {
    "master": "mh-master-your-slug",
    "module": "mh-module-your-slug",
    "blueprint": "mh-blueprint-your-slug",
}
MODULE_CATEGORIES = {"capability", "domain", "tone", "constraints", "output"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MIRROR_LOCALES = tuple(locale for locale in SUPPORTED_LOCALES if locale != CANONICAL_LOCALE)


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-") if part)


def destination(args: argparse.Namespace, *, locale: str = CANONICAL_LOCALE) -> Path:
    root = locale_root(locale)
    if args.kind == "module":
        return root / "prompts" / "modules" / args.category
    if args.kind == "master":
        return root / "prompts" / "masters" / "active"
    return root / "prompts" / "skill-blueprints"


def target_path(args: argparse.Namespace, *, locale: str = CANONICAL_LOCALE) -> Path:
    return destination(args, locale=locale) / f"{args.slug}.md"


def template_path(kind: str, *, locale: str = CANONICAL_LOCALE) -> Path:
    if locale == CANONICAL_LOCALE:
        return TEMPLATES[kind]
    return locale_root(locale) / "templates" / TEMPLATES[kind].name


def render_template(args: argparse.Namespace, *, locale: str = CANONICAL_LOCALE) -> str:
    template = read_text(template_path(args.kind, locale=locale))
    rendered = template.replace(ID_PLACEHOLDERS[args.kind], f"mh-{args.kind}-{args.slug}", 1)
    rendered = rendered.replace(TITLE_PLACEHOLDERS[args.kind], args.title, 1)
    rendered = rendered.replace("2026-04-03", args.review_date, 1)
    return rendered


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a new prompt, module, or blueprint file from the repo templates."
    )
    parser.add_argument("kind", choices=["master", "module", "blueprint"])
    parser.add_argument("slug", help="kebab-case file slug, for example onboarding-router")
    parser.add_argument("--title", help="Human-readable title. Defaults to a title generated from the slug.")
    parser.add_argument(
        "--category",
        choices=sorted(MODULE_CATEGORIES),
        help="Required for modules. Picks the prompts/modules subfolder.",
    )
    parser.add_argument(
        "--review-date",
        default=date.today().isoformat(),
        help="Value for last_reviewed. Defaults to today's date.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite the file if it already exists.")
    parser.add_argument("--dry-run", action="store_true", help="Print the destination and file content without writing.")
    parser.add_argument(
        "--mirror-locale",
        choices=MIRROR_LOCALES,
        help="Also create a mirrored scaffold file in the selected locale tree.",
    )
    return parser


def validate_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    if args.kind == "module" and not args.category:
        parser.error("--category is required when kind is 'module'")
    if args.kind != "module" and args.category:
        parser.error("--category can only be used when kind is 'module'")
    if not SLUG_RE.fullmatch(args.slug):
        parser.error("slug must be kebab-case and contain only lowercase letters, numbers, and single hyphens")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)
    args.title = args.title or title_from_slug(args.slug)

    primary_path = target_path(args, locale=CANONICAL_LOCALE)
    primary_content = render_template(args, locale=CANONICAL_LOCALE)

    mirror_path: Path | None = None
    mirror_content = ""
    if args.mirror_locale:
        mirror_path = target_path(args, locale=args.mirror_locale)
        mirror_content = render_template(args, locale=args.mirror_locale)

    if args.dry_run:
        print(f"[dry-run] would create: {primary_path.relative_to(ROOT)}")
        print("")
        print(primary_content)
        if mirror_path is not None:
            print("")
            print(f"[dry-run] would create mirror: {mirror_path.relative_to(ROOT)}")
            print("")
            print(mirror_content)
        return 0

    paths_to_check = [primary_path]
    if mirror_path is not None:
        paths_to_check.append(mirror_path)
    for path in paths_to_check:
        if path.exists() and not args.force:
            print(f"File already exists: {path.relative_to(ROOT)}", file=sys.stderr)
            print("Use --force to overwrite or choose a different slug.", file=sys.stderr)
            return 1

    primary_path.parent.mkdir(parents=True, exist_ok=True)
    primary_path.write_text(primary_content, encoding="utf-8")

    if mirror_path is not None:
        mirror_path.parent.mkdir(parents=True, exist_ok=True)
        mirror_path.write_text(mirror_content, encoding="utf-8")

    print(f"Created: {primary_path.relative_to(ROOT)}")
    if mirror_path is not None:
        print(f"Created mirror: {mirror_path.relative_to(ROOT)}")
    print("Next steps:")
    print("- Fill in the prompt body.")
    print("- Run: python scripts/generate_catalog.py")
    if mirror_path is not None:
        print(f"- Run: python scripts/generate_catalog.py --locale {args.mirror_locale}")
    print("- Validate with: python scripts/validate_catalog.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
