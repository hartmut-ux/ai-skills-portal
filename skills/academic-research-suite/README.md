# academic-research-suite

Comprehensive academic research suite: 4 sub-skills covering the full research-to-publication pipeline. (1) deep-research — 13-agent team, 7 modes incl. PRISMA systematic review, Socratic guidance, meta-analysis; (2) academic-paper — 12-agent writing pipeline, 10 modes, APA/Chicago/MLA/IEEE/Vancouver, LaTeX/DOCX output; (3) academic-paper-reviewer — 7-agent peer review simulation, 0-100 rubrics; (4) academic-pipeline — 10-stage orchestrator with integrity gates. Also includes: CLAUDE.md project templates, mywritingstyle.md, pre-edit backup hooks, Zotero/Mendeley/Consensus/Exa MCP setup, parallel sub-agent review guides, scholar-evaluator recipes. Use for: academic research, literature review, systematic review, peer review, write paper, citation check, APA 7, abstract, LaTeX, project setup, Zotero, Mendeley, parallel review, independent critique, theory evaluator, scheduled literature search, fact-check, annotated bibliography, research pipeline, revision, DOCX."

## Structure

```text
academic-research-suite/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/academic-research-suite/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/academic-research-suite/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/academic-research-suite/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py academic-research-suite
```
