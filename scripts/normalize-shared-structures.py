#!/usr/bin/env python3
"""Normalize shared/ folders so assets sit directly under shared/, not under shared/<skill-name>/.

Usage:
    python scripts/normalize-shared-structures.py skills/
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def normalize(skill_dir: Path) -> None:
    shared = skill_dir / "shared"
    if not shared.exists():
        return

    # If there is a subfolder with the same name as the skill, move its contents up
    nested = shared / skill_dir.name
    if nested.exists() and nested.is_dir():
        for item in nested.iterdir():
            dest = shared / item.name
            if dest.exists():
                print(f"  Conflict, skipping: {dest}")
                continue
            shutil.move(str(item), str(dest))
        nested.rmdir()
        print(f"Normalized: {skill_dir.name}")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/normalize-shared-structures.py <skills-dir>")
        return 1

    skills_dir = Path(sys.argv[1]).resolve()
    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir() and not skill_dir.name.startswith("."):
            normalize(skill_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
