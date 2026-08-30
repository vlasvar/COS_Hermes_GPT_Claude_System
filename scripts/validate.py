#!/usr/bin/env python
"""Validate that the repository is structurally complete and publication-safe."""
from __future__ import annotations

import json
import io
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "SECURITY.md", "AGENTS.md",
    "kernel/CONTEXT.md", "kernel/SYSTEM.md", "kernel/PERMISSIONS.md", "kernel/FINANCE_FIRST.md", "kernel/WORKFLOWS.md",
    "schema/sheets.json", "config/system.example.yaml",
    "adapters/hermes/README.md", "adapters/hermes/HERMES.md",
    "adapters/chatgpt/README.md", "adapters/chatgpt/PROJECT_INSTRUCTIONS.md",
    "adapters/claude/README.md", "adapters/claude/CLAUDE.md",
    "docs/privacy.md", "docs/dashboard-gpt-sites.md", "docs/profiles.md",
    "scripts/create_instance.py", "scripts/build_starter_kit.py",
    "starter-kit/00_START_HERE.md", "starter-kit/01_COPY_THIS_PROMPT.txt",
    "starter-kit/COS_DATABASE_TEMPLATE.xlsx", "dist/COS_Finance_First_Starter.zip",
]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".gs", ".py", ".txt"}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Google API key": re.compile(r"AIza[0-9A-Za-z_-]{35}"),
    "GitHub token": re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}"),
    "AWS access key": re.compile(r"(?:AKIA|ASIA)[0-9A-Z]{16}"),
    "Slack token": re.compile(r"xox[baprs]-[0-9A-Za-z-]{20,}"),
    "bearer token": re.compile(
        r"(?i)\b(?:authorization|proxy-authorization)\s*:\s*bearer\s+[A-Za-z0-9._~+/=-]{16,}"
    ),
}
PRIVATE_LINK = re.compile(
    r"https://(?:docs|drive)\.google\.com/"
    r"(?:spreadsheets/d|document/d|file/d|drive/(?:u/\d+/)?folders)/[A-Za-z0-9_-]{20,}"
)
EMAIL_ADDRESS = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
LOCAL_USER_PATH = re.compile(
    r"(?i)(?:[A-Z]:[\\/]+Users[\\/]+[^\\/\s]+|/" r"Users/[^/\s]+|/" r"home/[^/\s]+)"
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def iter_text_files():
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", ".gitignore"}:
            yield path


def scan_sensitive_text(text: str, label: str, errors: list[str]) -> None:
    if PRIVATE_LINK.search(text):
        errors.append(f"private Google resource link in {label}")
    if EMAIL_ADDRESS.search(text):
        errors.append(f"email address in public template file {label}")
    if LOCAL_USER_PATH.search(text):
        errors.append(f"local user path in public template file {label}")
    for secret_label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"possible {secret_label} in {label}")


def scan_xlsx_bytes(data: bytes, label: str, errors: list[str]) -> None:
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as workbook:
            for member in workbook.namelist():
                if not member.endswith((".xml", ".rels")):
                    continue
                text = workbook.read(member).decode("utf-8", errors="ignore")
                scan_sensitive_text(text, f"{label}!{member}", errors)
    except zipfile.BadZipFile:
        errors.append(f"invalid xlsx package: {label}")


def scan_binary_packages(errors: list[str]) -> None:
    for workbook_path in ROOT.rglob("*.xlsx"):
        if ".git" not in workbook_path.parts:
            scan_xlsx_bytes(
                workbook_path.read_bytes(),
                str(workbook_path.relative_to(ROOT)),
                errors,
            )

    for archive_path in ROOT.rglob("*.zip"):
        if ".git" in archive_path.parts:
            continue
        try:
            with zipfile.ZipFile(archive_path) as archive:
                for member in archive.namelist():
                    data = archive.read(member)
                    suffix = Path(member).suffix.lower()
                    label = f"{archive_path.relative_to(ROOT)}!{member}"
                    if suffix == ".xlsx":
                        scan_xlsx_bytes(data, label, errors)
                    elif suffix in TEXT_SUFFIXES or Path(member).name in {"LICENSE", ".gitignore"}:
                        scan_sensitive_text(data.decode("utf-8", errors="ignore"), label, errors)
        except zipfile.BadZipFile:
            errors.append(f"invalid zip package: {archive_path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    schema_path = ROOT / "schema/sheets.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        names = [tab["name"] for tab in schema["tabs"]]
        expected = [
            "System Check", "Income", "Expenses", "Budget", "Recurring Costs",
            "Inbox", "Projects", "Actions", "Commitments", "Decisions",
            "Contacts", "Reviews", "Agent Log",
        ]
        if names != expected:
            errors.append(f"unexpected tab order: {names}")
        for tab in schema["tabs"]:
            if tab["key"] not in tab["columns"]:
                errors.append(f"key missing from columns for {tab['name']}")
            if len(tab["columns"]) != len(set(tab["columns"])):
                errors.append(f"duplicate columns in {tab['name']}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f"invalid schema/sheets.json: {exc}")

    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        scan_sensitive_text(text, str(rel), errors)

        if path.suffix.lower() == ".md":
            for target in MARKDOWN_LINK.findall(text):
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                linked = (path.parent / target).resolve()
                if not linked.exists():
                    errors.append(f"broken relative link in {rel}: {target}")

    scan_binary_packages(errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"Validation passed: {len(REQUIRED)} required files, schema, links, "
        "email addresses, local user paths, private resource links, common secret patterns, "
        "workbook internals, and ZIP contents checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
