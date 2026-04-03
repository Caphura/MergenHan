from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
DEFAULT_DESTINATIONS = {
    "master": ROOT / "prompts" / "masters" / "active",
    "blueprint": ROOT / "prompts" / "skill-blueprints",
}
MODULE_CATEGORIES = {"capability", "domain", "tone", "constraints", "output"}


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-") if part)


def destination(args: argparse.Namespace) -> Path:
    if args.kind == "module":
        return ROOT / "prompts" / "modules" / args.category
    return DEFAULT_DESTINATIONS[args.kind]


def target_path(args: argparse.Namespace) -> Path:
    return destination(args) / f"{args.slug}.md"


def render_template(args: argparse.Namespace) -> str:
    template = TEMPLATES[args.kind].read_text(encoding="utf-8-sig")
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
    return parser


def validate_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    if args.kind == "module" and not args.category:
        parser.error("--category is required when kind is 'module'")
    if args.kind != "module" and args.category:
        parser.error("--category can only be used when kind is 'module'")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)
    args.title = args.title or title_from_slug(args.slug)

    path = target_path(args)
    content = render_template(args)

    if args.dry_run:
        print(f"[dry-run] would create: {path.relative_to(ROOT)}")
        print("")
        print(content)
        return 0

    if path.exists() and not args.force:
        print(f"File already exists: {path.relative_to(ROOT)}", file=sys.stderr)
        print("Use --force to overwrite or choose a different slug.", file=sys.stderr)
        return 1

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

    print(f"Created: {path.relative_to(ROOT)}")
    print("Next steps:")
    print("- Fill in the prompt body.")
    print("- Run: python scripts/generate_catalog.py")
    print("- Validate with: python scripts/validate_catalog.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
