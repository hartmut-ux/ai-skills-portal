#!/usr/bin/env python3
"""Migrate extracted Claude skills into the multi-platform portal format.

Usage:
    python scripts/migrate-claude-skills.py "Claude Skills/_extracted" skills/

Assumes each source folder contains a SKILL.md somewhere inside.
Prefers the top-level SKILL.md if present, otherwise searches recursively.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path


def find_skill_md(source_dir: Path) -> Path | None:
    """Find the best candidate SKILL.md in an extracted skill folder."""
    top = source_dir / "SKILL.md"
    if top.exists():
        return top
    # Prefer shorter paths (top-level wins over nested duplicates)
    candidates = sorted(source_dir.rglob("SKILL.md"), key=lambda p: len(str(p)))
    return candidates[0] if candidates else None


def parse_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body). Handles --- YAML frontmatter."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", text


def extract_name_and_description(frontmatter: str, body: str) -> tuple[str, str]:
    """Extract skill name and a short description."""
    name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
    name = name_match.group(1).strip().strip('"') if name_match else ""

    desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE | re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        desc = desc.strip('"').split("\n")[0]
    else:
        # Fallback: first line of H1
        h1_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        desc = h1_match.group(1).strip() if h1_match else "AI skill"

    return name or "unnamed-skill", desc


def make_wrapper(name: str, description: str, platform: str) -> str:
    """Create a thin wrapper SKILL.md for the given platform."""
    platform_title = {"kimi": "Kimi Code CLI", "claude": "Claude Code", "codex": "Codex CLI"}[platform]
    invoke = {
        "kimi": f"/{name}",
        "claude": f"{name}",
        "codex": f"{name}",
    }[platform]

    return f"""---
name: {name}
description: {description}
---

# {name.title().replace('-', ' ')} — {platform_title} wrapper

This is the **{platform_title} wrapper** for `{name}`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `{invoke}`
- "run {name}"
- Any trigger described in the core skill

## How to invoke

In {platform_title}:

```
{invoke}
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using {platform_title} tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
"""


def migrate_skill(source_dir: Path, target_root: Path) -> None:
    skill_md = find_skill_md(source_dir)
    if not skill_md:
        print(f"SKILL.md not found in {source_dir}, skipping")
        return

    skill_name = source_dir.name
    # Clean up trailing .skill if any
    skill_name = skill_name.replace(".skill", "")

    target_dir = target_root / skill_name
    if target_dir.exists():
        print(f"Target already exists, removing: {target_dir}")
        shutil.rmtree(target_dir)

    target_dir.mkdir(parents=True)

    text = skill_md.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    name, description = extract_name_and_description(frontmatter, body)

    # Write shared core (frontmatter + body, neutralized slightly)
    core_text = text
    core_text = re.sub(r'Claude Code', 'your AI assistant', core_text)
    core_text = re.sub(r'Claude', 'the assistant', core_text)
    (target_dir / "shared").mkdir()
    (target_dir / "shared" / "SKILL-CORE.md").write_text(core_text, encoding="utf-8")

    # Copy all other files from source into shared/ while preserving relative structure
    for src_file in source_dir.rglob("*"):
        if src_file.is_file() and src_file.name != "SKILL.md":
            rel = src_file.relative_to(source_dir)
            dst = target_dir / "shared" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dst)

    # Write wrappers
    for platform in ("kimi", "claude", "codex"):
        wrapper_dir = target_dir / f".{platform}" / "skills" / name
        wrapper_dir.mkdir(parents=True)
        (wrapper_dir / "SKILL.md").write_text(
            make_wrapper(name, description, platform), encoding="utf-8"
        )

    # Write skill README
    readme_text = f"""# {name}

{description}

## Structure

```text
{name}/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/{name}/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/{name}/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/{name}/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py {name}
```
"""
    (target_dir / "README.md").write_text(readme_text, encoding="utf-8")

    print(f"Migrated {skill_name} -> {target_dir}")


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python scripts/migrate-claude-skills.py <source-dir> <target-dir>")
        return 1

    source_root = Path(sys.argv[1]).resolve()
    target_root = Path(sys.argv[2]).resolve()

    if not source_root.exists():
        print(f"Source directory does not exist: {source_root}")
        return 1

    target_root.mkdir(parents=True, exist_ok=True)

    for item in sorted(source_root.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            migrate_skill(item, target_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
