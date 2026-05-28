#!/usr/bin/env python3
import json
import re
from pathlib import Path

import yaml


BASE_DIR = Path(__file__).resolve().parent
OUTLINE_PATH = BASE_DIR / "outline.yaml"
FIELDS_PATH = BASE_DIR / "fields.yaml"
REPORT_PATH = BASE_DIR / "report.md"

CATEGORY_MAPPING = {
    "Basic Info": ["basic_info", "Basic Info"],
    "Technical Features": ["technical_features", "technical_characteristics", "Technical Features"],
    "Performance Metrics": ["performance_metrics", "performance", "Performance Metrics"],
    "Milestone Significance": ["milestone_significance", "milestones", "Milestone Significance"],
    "Business Info": ["business_info", "commercial_info", "Business Info"],
    "Competition & Ecosystem": ["competition_ecosystem", "competition", "Competition & Ecosystem"],
    "History": ["history", "History"],
    "Market Positioning": ["market_positioning", "market", "Market Positioning"],
}

SUMMARY_FIELDS = ["category", "first_public_release", "autonomy_level"]
INTERNAL_FIELDS = {"_source_file", "uncertain"}
NESTED_CATEGORY_KEYS = {key for values in CATEGORY_MAPPING.values() for key in values}


def load_yaml(path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def slugify(text):
    text = str(text).strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text.strip("-")


def titleize(name):
    return str(name).replace("_", " ").replace("-", " ").title()


def is_uncertain_value(value):
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip() or "[uncertain]" in value
    if isinstance(value, list):
        return len(value) == 0 or any(is_uncertain_value(item) for item in value)
    if isinstance(value, dict):
        return len(value) == 0 or any(is_uncertain_value(item) for item in value.values())
    return False


def find_nested(obj, field_name):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == field_name:
                return value
        for value in obj.values():
            result = find_nested(value, field_name)
            if result is not None:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = find_nested(item, field_name)
            if result is not None:
                return result
    return None


def get_field(data, category, field_name):
    if field_name in data:
        return data[field_name]

    category_keys = [category, titleize(category)]
    category_keys.extend(CATEGORY_MAPPING.get(category, []))
    category_keys.extend(CATEGORY_MAPPING.get(titleize(category), []))
    category_keys.append(category.lower().replace(" ", "_"))

    for key in category_keys:
        value = data.get(key)
        if isinstance(value, dict) and field_name in value:
            return value[field_name]

    return find_nested(data, field_name)


def filter_uncertain_list(values):
    return [item for item in values if not is_uncertain_value(item)]


def format_scalar(value):
    value = str(value).strip()
    if len(value) > 100:
        return "> " + value.replace("\n", "<br>")
    return value.replace("\n", "<br>")


def format_value(value, indent=0):
    if isinstance(value, list):
        values = filter_uncertain_list(value)
        if not values:
            return ""
        if all(not isinstance(item, (dict, list)) for item in values):
            rendered = [format_scalar(item) for item in values]
            if len(", ".join(rendered)) <= 120 and len(rendered) <= 5:
                return ", ".join(rendered)
            return "\n".join(f"{'  ' * indent}- {item}" for item in rendered)
        lines = []
        for item in values:
            if isinstance(item, dict):
                parts = [f"{titleize(k)}: {format_value(v, indent + 1)}" for k, v in item.items() if not is_uncertain_value(v)]
                if parts:
                    lines.append(f"{'  ' * indent}- " + " | ".join(parts))
            else:
                rendered = format_value(item, indent + 1)
                if rendered:
                    lines.append(f"{'  ' * indent}- {rendered}")
        return "\n".join(lines)
    if isinstance(value, dict):
        parts = []
        for key, item in value.items():
            if is_uncertain_value(item):
                continue
            rendered = format_value(item, indent + 1)
            if rendered:
                parts.append(f"**{titleize(key)}:** {rendered}")
        return "; ".join(parts) if len("; ".join(parts)) <= 140 else "<br>".join(parts)
    return format_scalar(value)


def load_field_structure(fields_data):
    categories = []
    known_fields = set()
    for category in fields_data.get("field_categories", []):
        name = category.get("category", "Other")
        fields = []
        for field in category.get("fields", []):
            field_name = field["name"]
            known_fields.add(field_name)
            fields.append(field_name)
        categories.append((name, fields))
    return categories, known_fields


def collect_extra_fields(data, known_fields):
    extras = []
    for key, value in data.items():
        if key in INTERNAL_FIELDS or key in known_fields or key in NESTED_CATEGORY_KEYS:
            continue
        if isinstance(value, dict) and key in NESTED_CATEGORY_KEYS:
            continue
        extras.append((key, value))
    return extras


def render_field(label, value):
    rendered = format_value(value)
    if not rendered:
        return ""
    if "\n" in rendered or rendered.startswith("> "):
        return f"**{label}:**\n\n{rendered}\n"
    return f"**{label}:** {rendered}\n"


def main():
    outline = load_yaml(OUTLINE_PATH)
    fields_data = load_yaml(FIELDS_PATH)
    result_dir = BASE_DIR / outline.get("execution", {}).get("output_dir", "./results")
    if not result_dir.is_absolute():
        result_dir = (BASE_DIR / result_dir).resolve()

    categories, known_fields = load_field_structure(fields_data)
    records = []
    for path in sorted(result_dir.glob("*.json")):
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        data["_source_file"] = path.name
        records.append(data)

    records.sort(key=lambda item: str(item.get("name", item.get("_source_file", ""))).lower())

    lines = [
        f"# {outline.get('topic', 'Research Report')}",
        "",
        outline.get("subtitle", "Structured research report generated from deep research JSON results."),
        "",
        f"- Generated from: `{result_dir}`",
        f"- Items: {len(records)}",
        f"- Last verified in source records: {max((str(r.get('last_verified_at', '')) for r in records), default='')}",
        "",
        "## Table of Contents",
        "",
    ]

    for index, record in enumerate(records, 1):
        name = record.get("name", record["_source_file"])
        summary = []
        uncertain = set(record.get("uncertain", []))
        for field in SUMMARY_FIELDS:
            if field in uncertain:
                continue
            value = get_field(record, "", field)
            if is_uncertain_value(value):
                continue
            rendered = format_value(value)
            if rendered:
                summary.append(f"{titleize(field)}: {rendered}")
        suffix = f" - {' | '.join(summary)}" if summary else ""
        lines.append(f"{index}. [{name}](#{slugify(name)}){suffix}")

    lines.extend(["", "## Detailed Content", ""])

    for record in records:
        name = record.get("name", record["_source_file"])
        uncertain = set(record.get("uncertain", []))
        lines.extend([f"### {name}", ""])
        for category, field_names in categories:
            section = []
            for field_name in field_names:
                if field_name in uncertain:
                    continue
                value = get_field(record, category, field_name)
                if is_uncertain_value(value):
                    continue
                rendered = render_field(titleize(field_name), value)
                if rendered:
                    section.append(rendered)
            if section:
                lines.extend([f"#### {titleize(category)}", ""])
                for entry in section:
                    lines.extend([entry, ""])

        extras = []
        for key, value in collect_extra_fields(record, known_fields):
            if key in uncertain or is_uncertain_value(value):
                continue
            rendered = render_field(titleize(key), value)
            if rendered:
                extras.append(rendered)
        if extras:
            lines.extend(["#### Other Info", ""])
            for entry in extras:
                lines.extend([entry, ""])

        if uncertain:
            filtered = [field for field in uncertain if field]
            if filtered:
                lines.extend(["#### Uncertain Fields", ""])
                lines.extend(f"- {field}" for field in sorted(filtered))
                lines.append("")

    REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
