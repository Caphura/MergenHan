from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path

from script_common import add_locale_argument, read_text

SUPPORTED_EXTENSIONS = (".json", ".txt", ".md")
TOKEN_KEYS = ("output_tokens", "completion_tokens", "response_tokens")
TEXT_KEYS = ("output_text", "response_text", "text", "output", "content")
TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)
TEXT = {
    "en": {
        "description": "Build a markdown-ready Cave Man benchmark summary from baseline and Cave Man outputs.",
        "missing_dir": "Directory not found: {path}",
        "placeholder_hint": "The '/path/to/...' form is only a placeholder. Replace it with a real directory such as './baseline' or '/Users/name/run/baseline'.",
        "duplicate_case": "Duplicate case ID '{case_id}' in {directory}",
        "missing_pairs": "Missing matching case files: {details}",
        "no_cases": "No matching case files found.",
        "json_text_missing": "Could not find output text in JSON file: {path}",
        "summary_title": "## Token Summary",
        "cases": "Cases",
        "median_saving": "Median saving",
        "highest_saving": "Highest saving",
        "lowest_saving": "Lowest saving",
        "count_source": "Count source",
        "reported": "reported",
        "estimated": "estimated",
        "mixed": "mixed",
    },
    "tr": {
        "description": "Baseline ve Cave Man ciktilarindan markdown'a hazir bir benchmark ozeti olustur.",
        "missing_dir": "Dizin bulunamadi: {path}",
        "placeholder_hint": "'/path/to/...' formu sadece yer tutucudur. Bunu './baseline' veya '/Users/name/run/baseline' gibi gercek bir dizinle degistir.",
        "duplicate_case": "Ayni case ID birden fazla kez bulundu: '{case_id}' in {directory}",
        "missing_pairs": "Eslesen case dosyalari eksik: {details}",
        "no_cases": "Eslesen case dosyasi bulunamadi.",
        "json_text_missing": "JSON dosyasinda output text bulunamadi: {path}",
        "summary_title": "## Token Ozet",
        "cases": "Case sayisi",
        "median_saving": "Median saving",
        "highest_saving": "En yuksek saving",
        "lowest_saving": "En dusuk saving",
        "count_source": "Sayim kaynagi",
        "reported": "reported",
        "estimated": "estimated",
        "mixed": "mixed",
    },
}


@dataclass
class CaseResult:
    case_id: str
    baseline_tokens: int
    cave_man_tokens: int
    saving_percent: float
    note: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=TEXT["en"]["description"])
    add_locale_argument(parser)
    parser.add_argument("--baseline-dir", required=True, type=Path, help="Directory that holds baseline case outputs.")
    parser.add_argument("--cave-man-dir", required=True, type=Path, help="Directory that holds Cave Man case outputs.")
    parser.add_argument(
        "--ids",
        help="Optional comma-separated case order such as CMB1,CMB2,CMB3. Defaults to sorted shared file stems.",
    )
    return parser


def is_placeholder_path(directory: Path) -> bool:
    parts = directory.parts
    return len(parts) >= 3 and parts[:3] == ("/", "path", "to")


def discover_cases(directory: Path, text: dict[str, str]) -> dict[str, Path]:
    if not directory.is_dir():
        message = text["missing_dir"].format(path=directory)
        if is_placeholder_path(directory):
            message = f"{message}\n{text['placeholder_hint']}"
        raise ValueError(message)

    cases: dict[str, Path] = {}
    for path in sorted(directory.iterdir()):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        case_id = path.stem
        if case_id in cases:
            raise ValueError(text["duplicate_case"].format(case_id=case_id, directory=directory))
        cases[case_id] = path
    return cases


def ordered_case_ids(raw_ids: str | None, baseline_cases: dict[str, Path], cave_cases: dict[str, Path], text: dict[str, str]) -> list[str]:
    if raw_ids:
        ids = [item.strip() for item in raw_ids.split(",") if item.strip()]
    else:
        ids = sorted(set(baseline_cases) & set(cave_cases))

    missing: list[str] = []
    for case_id in ids:
        if case_id not in baseline_cases:
            missing.append(f"{case_id}:baseline")
        if case_id not in cave_cases:
            missing.append(f"{case_id}:cave-man")
    if missing:
        raise ValueError(text["missing_pairs"].format(details=", ".join(missing)))
    if not ids:
        raise ValueError(text["no_cases"])
    return ids


def extract_first_int(payload: object) -> int | None:
    if isinstance(payload, bool):
        return None
    if isinstance(payload, int):
        return payload
    if isinstance(payload, dict):
        for key in TOKEN_KEYS:
            value = payload.get(key)
            if isinstance(value, int) and not isinstance(value, bool):
                return value
        for value in payload.values():
            found = extract_first_int(value)
            if found is not None:
                return found
    if isinstance(payload, list):
        for item in payload:
            found = extract_first_int(item)
            if found is not None:
                return found
    return None


def extract_text(payload: object) -> str | None:
    if isinstance(payload, str):
        return payload.strip()
    if isinstance(payload, dict):
        for key in TEXT_KEYS:
            value = payload.get(key)
            text = extract_text(value)
            if text:
                return text
        if payload.keys() >= {"type", "text"} and payload.get("type") == "text":
            text = extract_text(payload.get("text"))
            if text:
                return text
        for value in payload.values():
            text = extract_text(value)
            if text:
                return text
    if isinstance(payload, list):
        parts: list[str] = []
        for item in payload:
            text = extract_text(item)
            if text:
                parts.append(text)
        if parts:
            return "\n".join(parts)
    return None


def rough_token_count(text: str) -> int:
    stripped = text.strip()
    if not stripped:
        return 0
    regex_based = len(TOKEN_RE.findall(stripped))
    char_based = math.ceil(len(stripped) / 4)
    return max(regex_based, char_based)


def load_case(path: Path, text: dict[str, str]) -> tuple[str, int, str]:
    if path.suffix.lower() == ".json":
        payload = json.loads(read_text(path))
        output_text = extract_text(payload)
        if not output_text:
            raise ValueError(text["json_text_missing"].format(path=path))
        reported_tokens = extract_first_int(payload)
        if reported_tokens is not None:
            return output_text, reported_tokens, text["reported"]
        return output_text, rough_token_count(output_text), text["estimated"]

    output_text = read_text(path).strip()
    return output_text, rough_token_count(output_text), text["estimated"]


def saving_percent(baseline_tokens: int, cave_man_tokens: int) -> float:
    if baseline_tokens <= 0:
        return 0.0
    return ((baseline_tokens - cave_man_tokens) / baseline_tokens) * 100


def format_percent(value: float) -> str:
    return f"{value:.1f}%"


def count_source_label(results: list[CaseResult], text: dict[str, str]) -> str:
    notes = {result.note for result in results}
    if len(notes) == 1:
        return next(iter(notes))
    return text["mixed"]


def render_summary(results: list[CaseResult], text: dict[str, str]) -> str:
    median_value = statistics.median(result.saving_percent for result in results)
    highest = max(results, key=lambda item: item.saving_percent)
    lowest = min(results, key=lambda item: item.saving_percent)
    lines = [
        text["summary_title"],
        "",
        f"- {text['cases']}: {len(results)}",
        f"- {text['median_saving']}: {format_percent(median_value)}",
        f"- {text['highest_saving']}: {highest.case_id} ({format_percent(highest.saving_percent)})",
        f"- {text['lowest_saving']}: {lowest.case_id} ({format_percent(lowest.saving_percent)})",
        f"- {text['count_source']}: {count_source_label(results, text)}",
        "",
        "| Test ID | Baseline Tokens | Cave Man Tokens | Saving % | Meaning | Action | Safety | Compression | Style | Notes |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for result in results:
        lines.append(
            f"| {result.case_id} | {result.baseline_tokens} | {result.cave_man_tokens} | {format_percent(result.saving_percent)} |  |  |  |  |  | {result.note} |"
        )
    return "\n".join(lines)


def main() -> int:
    args = build_parser().parse_args()
    text = TEXT[args.locale]

    try:
        baseline_cases = discover_cases(args.baseline_dir, text)
        cave_cases = discover_cases(args.cave_man_dir, text)
        case_ids = ordered_case_ids(args.ids, baseline_cases, cave_cases, text)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    results: list[CaseResult] = []
    try:
        for case_id in case_ids:
            _, baseline_tokens, baseline_note = load_case(baseline_cases[case_id], text)
            _, cave_tokens, cave_note = load_case(cave_cases[case_id], text)
            note = baseline_note if baseline_note == cave_note else text["mixed"]
            results.append(
                CaseResult(
                    case_id=case_id,
                    baseline_tokens=baseline_tokens,
                    cave_man_tokens=cave_tokens,
                    saving_percent=saving_percent(baseline_tokens, cave_tokens),
                    note=note,
                )
            )
    except (ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(render_summary(results, text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
