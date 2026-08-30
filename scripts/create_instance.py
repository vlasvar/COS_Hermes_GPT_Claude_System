#!/usr/bin/env python
"""Create a private Chief of Staff instance outside the template repository."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KERNEL_FILES = ("SYSTEM.md", "CONTEXT.md", "PERMISSIONS.md", "FINANCE_FIRST.md", "WORKFLOWS.md")
ADAPTERS = {
    "hermes": ("adapters/hermes/HERMES.md", "AGENTS.md"),
    "chatgpt": ("adapters/chatgpt/PROJECT_INSTRUCTIONS.md", "PROJECT_INSTRUCTIONS.md"),
    "claude": ("adapters/claude/CLAUDE.md", "CLAUDE.md"),
}


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def create_instance(target: Path, adapter: str) -> list[Path]:
    target = target.expanduser().resolve()
    root = ROOT.resolve()

    if is_within(target, root):
        raise ValueError("The private instance must be outside the template repository.")
    if target.exists() and any(target.iterdir()):
        raise ValueError("The target directory already exists and is not empty.")

    target.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []

    for name in KERNEL_FILES:
        destination = target / name
        shutil.copy2(root / "kernel" / name, destination)
        created.append(destination)

    copies = [
        (root / "templates/profile/USER_PROFILE.md", target / "USER_PROFILE.md"),
        (root / "config/system.example.yaml", target / "system.yaml"),
        (root / ADAPTERS[adapter][0], target / ADAPTERS[adapter][1]),
    ]
    for source, destination in copies:
        shutil.copy2(source, destination)
        created.append(destination)

    readme = target / "README.md"
    readme.write_text(
        "# Private Chief of Staff instance\n\n"
        f"Primary agent environment: **{adapter}**.\n\n"
        "1. Complete `USER_PROFILE.md`.\n"
        "2. Configure private resource identifiers in `system.yaml`.\n"
        "3. Provision the Google Sheet from the public template.\n"
        "4. Keep credentials in the selected platform's secret store.\n"
        "5. Start at permission level 1 and test with fictional inputs.\n\n"
        "This folder contains private instance configuration and must not be copied "
        "into the public template repository.\n",
        encoding="utf-8",
    )
    created.append(readme)
    return created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a private Chief of Staff instance from the public-safe template."
    )
    parser.add_argument("target", type=Path, help="New or empty directory outside this repository")
    parser.add_argument("--adapter", choices=sorted(ADAPTERS), required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        created = create_instance(args.target, args.adapter)
    except (OSError, ValueError) as exc:
        print(f"Instance creation failed: {exc}", file=sys.stderr)
        return 1

    print(f"Created {args.adapter} instance at {args.target.expanduser().resolve()}")
    for path in created:
        print(f"- {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
