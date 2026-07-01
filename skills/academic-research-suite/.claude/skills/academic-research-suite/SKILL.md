---
name: academic-research-suite
description: Comprehensive academic research suite: 4 sub-skills covering the full research-to-publication pipeline. (1) deep-research — 13-agent team, 7 modes incl. PRISMA systematic review, Socratic guidance, meta-analysis; (2) academic-paper — 12-agent writing pipeline, 10 modes, APA/Chicago/MLA/IEEE/Vancouver, LaTeX/DOCX output; (3) academic-paper-reviewer — 7-agent peer review simulation, 0-100 rubrics; (4) academic-pipeline — 10-stage orchestrator with integrity gates. Also includes: CLAUDE.md project templates, mywritingstyle.md, pre-edit backup hooks, Zotero/Mendeley/Consensus/Exa MCP setup, parallel sub-agent review guides, scholar-evaluator recipes. Use for: academic research, literature review, systematic review, peer review, write paper, citation check, APA 7, abstract, LaTeX, project setup, Zotero, Mendeley, parallel review, independent critique, theory evaluator, scheduled literature search, fact-check, annotated bibliography, research pipeline, revision, DOCX."
---

# Academic Research Suite — Claude Code wrapper

This is the **Claude Code wrapper** for `academic-research-suite`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `academic-research-suite`
- "run academic-research-suite"
- Any trigger described in the core skill

## How to invoke

In Claude Code:

```
academic-research-suite
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Claude Code tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
