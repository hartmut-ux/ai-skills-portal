---
name: academic-research-suite
description: "Comprehensive academic research suite: 4 sub-skills covering the full research-to-publication pipeline. (1) deep-research — 13-agent team, 7 modes incl. PRISMA systematic review, Socratic guidance, meta-analysis; (2) academic-paper — 12-agent writing pipeline, 10 modes, APA/Chicago/MLA/IEEE/Vancouver, LaTeX/DOCX output; (3) academic-paper-reviewer — 7-agent peer review simulation, 0-100 rubrics; (4) academic-pipeline — 10-stage orchestrator with integrity gates. Also includes: CLAUDE.md project templates, mywritingstyle.md, pre-edit backup hooks, Zotero/Mendeley/Consensus/Exa MCP setup, parallel sub-agent review guides, scholar-evaluator recipes. Use for: academic research, literature review, systematic review, peer review, write paper, citation check, APA 7, abstract, LaTeX, project setup, Zotero, Mendeley, parallel review, independent critique, theory evaluator, scheduled literature search, fact-check, annotated bibliography, research pipeline, revision, DOCX."
metadata:
  version: "3.11.2"
  source: "https://github.com/Imbad0202/academic-research-skills"
  license: "CC BY-NC 4.0"
  original_author: "Cheng-I Wu (Imbad0202)"
  packaged_for: "the assistant Cowork"
  packaged_date: "2026-06-07"
  webinar_additions: "Mushtaq Bilal — your AI assistant for Academics webinar, 6 June 2026"
---

# Academic Research Suite — Full Research-to-Publication Pipeline

> **Source**: [github.com/Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (28k+ stars)  
> **License**: CC BY-NC 4.0 — non-commercial use with attribution  
> **Original author**: Cheng-I Wu  
> **Additional modules**: Project templates, hooks, MCP setup, sub-agent guides

This skill packages four specialized sub-skills into one installable unit, plus a set of workflow guides for serious academic users. Together they cover the complete academic research pipeline from topic exploration to final publication-ready manuscript.

---

## How to Use This Suite

When the user's request matches one of the areas below, load the corresponding file and follow it exactly.

### Core Research & Writing Sub-Skills

| Sub-skill | Load from | When to Use |
|-----------|-----------|-------------|
| `deep-research` | `deep-research.md` | Researching a topic, literature review, systematic review, fact-checking, Socratic research guidance |
| `academic-paper` | `academic-paper.md` | Writing a paper, paper outline, revising a draft, writing an abstract, citation check, format conversion |
| `academic-paper-reviewer` | `academic-paper-reviewer.md` | Reviewing a paper, simulating peer review, methodology check |
| `academic-pipeline` | `academic-pipeline.md` | Full research-to-publication orchestration, end-to-end pipeline |

**Quick dispatch logic:**
```
User wants to:
  Research a topic / find literature / fact-check  → deep-research.md
  Write a paper / outline / abstract / revise      → academic-paper.md
  Review a paper / simulate peer review            → academic-paper-reviewer.md
  Full pipeline from scratch to final paper        → academic-pipeline.md
  "I want to write a research paper on X"          → academic-pipeline.md (if fresh start)
```

### Workflow Guides (read and explain to user; do not execute autonomously)

| Guide | Location | When to Recommend |
|-------|----------|-------------------|
| Project CLAUDE.md template | `templates/CLAUDE-academic-project.md` | User is starting a new academic project |
| Writing style template | `templates/mywritingstyle-template.md` | User wants the assistant to write in their voice |
| Pre-edit backup hook | `hooks/pre-edit-backup.md` | User is about to incorporate reviewer comments or do heavy revision |
| MCP reference managers | `setup/mcp-reference-managers.md` | User mentions Zotero, Mendeley, or wants to search literature |
| Parallel sub-agent review | `subagents/parallel-review-guide.md` | User wants independent critique of multiple dimensions, or dual-screener systematic review |
| Scholar evaluator | `subagents/scholar-evaluator-guide.md` | User works with a specific theoretical framework and wants targeted feedback |

---

## Sub-Skill Summaries

### 1. Deep Research (v2.9.4) — 13-Agent Research Team

**7 Modes**: full, quick, lit-review, fact-check, socratic, systematic-review, review

**Agent team**: research_question_agent, research_architect_agent, bibliography_agent, source_verification_agent, synthesis_agent, report_compiler_agent, editor_in_chief_agent, devils_advocate_agent, ethics_review_agent, socratic_mentor_agent, risk_of_bias_agent, meta_analysis_agent, monitoring_agent

**Key features**:
- FINER-scored research question formulation
- PRISMA 2020 systematic review with RoB 2/ROBINS-I risk of bias
- Meta-analysis (effect sizes, heterogeneity, GRADE)
- Socratic guided research dialogue (intent detection, anti-sycophancy)
- Devil's Advocate with concession threshold protocol
- Post-research literature monitoring (see also `setup/mcp-reference-managers.md` for scheduled daily searches)

**Full instructions**: See `deep-research.md`

---

### 2. Academic Paper (v3.2.0) — 12-Agent Writing Pipeline

**10 Modes**: full, plan, outline-only, revision, revision-coach, abstract-only, lit-review, format-convert, citation-check, disclosure

**Agent team**: intake_agent, literature_strategist_agent, structure_architect_agent, argument_builder_agent, draft_writer_agent, citation_compliance_agent, abstract_bilingual_agent, peer_reviewer_agent, formatter_agent, socratic_mentor_agent, visualization_agent, revision_coach_agent

**Key features**:
- 6 paper structures: IMRaD, Thematic Lit Review, Theoretical, Case Study, Policy Brief, Conference
- 5 citation formats: APA 7.0, Chicago, MLA 9, IEEE, Vancouver
- Bilingual abstracts (zh-TW + EN)
- LaTeX/DOCX/PDF/Markdown output
- Style Calibration — pair with `templates/mywritingstyle-template.md` for voice-matched output
- VLM figure verification
- Anti-leakage protocol

**Full instructions**: See `academic-paper.md`

---

### 3. Academic Paper Reviewer (v1.10.0) — 7-Agent Peer Review

**6 Modes**: full, re-review, quick, methodology-focus, guided, calibration

**Agent team**: field_analyst_agent, eic_agent, methodology_reviewer_agent, domain_reviewer_agent, perspective_reviewer_agent, devils_advocate_reviewer_agent, editorial_synthesizer_agent

**Key features**:
- 0–100 quality rubrics (weighted: Originality 20%, Methodology 25%, Evidence 25%, Coherence 15%, Writing 15%)
- Decision mapping: ≥80 Accept, 65–79 Minor Revision, 50–64 Major Revision, <50 Reject
- Devil's Advocate reviewer (logic chain validation, strongest counter-arguments)
- R&R Traceability Matrix
- Calibration mode with FNR/FPR measurement
- For independent parallel critique, see also `subagents/parallel-review-guide.md`

**Full instructions**: See `academic-paper-reviewer.md`

---

### 4. Academic Pipeline (v3.11.1) — 10-Stage Orchestrator

**10 Stages**:
1. RESEARCH → `deep-research` (socratic/full/quick)
2. WRITE → `academic-paper` (plan/full)
3. **INTEGRITY** → `integrity_verification_agent` (pre-review, mandatory)
4. REVIEW → `academic-paper-reviewer` (full, EIC + R1/R2/R3 + Devil's Advocate)
5. REVISE → `academic-paper` (revision)
6. RE-REVIEW → `academic-paper-reviewer` (re-review)
7. RE-REVISE → `academic-paper` (revision, if needed)
8. **FINAL INTEGRITY** → `integrity_verification_agent` (final-check, mandatory, zero-issues required)
9. FINALIZE → `academic-paper` (format-convert → MD + DOCX + LaTeX → PDF)
10. PROCESS SUMMARY → Collaboration Quality Evaluation (6 dimensions, 1–100 score)

**Key features**:
- Integrity gates at Stage 2.5 and 4.5 (cannot be skipped)
- Adaptive checkpoint system (FULL/SLIM/MANDATORY)
- External review protocol (real journal reviewer comments)
- Material Passport + Artifact Reproducibility Lockfile
- Score trajectory tracking
- Recommend setting up pre-edit backup hook before Stage 5 (see `hooks/pre-edit-backup.md`)

**Full instructions**: See `academic-pipeline.md`

---

## Stage Handoff Schemas

Inter-stage data contracts (9 schemas) are defined in `shared/handoff_schemas.md`:
- RQ Brief, Bibliography, Synthesis, Paper Draft, Integrity Report, Review Report, Revision Roadmap, Response to Reviewers, Material Passport

---

## Getting Started: New Project Checklist

When a user is starting a fresh academic project, recommend this setup sequence:

1. **Project structure** → Copy `templates/CLAUDE-academic-project.md` to their project folder as `CLAUDE.md`, fill in the bracketed fields
2. **Writing style** → Copy `templates/mywritingstyle-template.md`, paste 2–3 paragraphs of their own writing
3. **Reference manager** → If they use Zotero or Mendeley, follow `setup/mcp-reference-managers.md`
4. **Literature monitoring** → Set up a scheduled daily/weekly search (see setup guide)
5. **Backup hook** → Set up `hooks/pre-edit-backup.md` before any draft editing begins
6. **Begin research** → Use `deep-research.md` (socratic mode recommended for new topics)

---

## Important Notes

1. **Human-in-the-loop**: This suite assists researchers — it does not replace human judgment on methodology, interpretation, or academic argument.
2. **Citation verification**: Every claim requires a citation. The integrity gates catch hallucinated references.
3. **AI disclosure**: All outputs include an AI disclosure statement as required by most journals.
4. **Language**: Follows the user's language. Defaults to English; Traditional Chinese supported natively.
5. **CLAUDE.md length**: Keep project CLAUDE.md under 600 words. Detailed instructions belong in separate files (mywritingstyle.md, etc.) referenced from CLAUDE.md.
6. **License**: CC BY-NC 4.0. Non-commercial use only. Attribution required: Cheng-I Wu / github.com/Imbad0202/academic-research-skills

---

## Quick Start Examples

```
# Start a full research pipeline from scratch
"I want to write a research paper on [topic]"

# Start with Socratic research guidance
"Guide my research on [topic]"

# Write a paper with a clear RQ already defined
"Write a paper on [topic]"

# Review a paper
"Review this paper: [paste or attach paper]"

# Do a systematic review
"Systematic review of [topic]"

# Check citations in an existing paper
"Check citations" / "Citation check"

# Convert paper to LaTeX
"Convert to LaTeX" / "Convert citations to IEEE"

# Set up a new project
"Help me set up my research project in your AI assistant"

# Get independent parallel critique
"Critique my draft's methodology and argument independently"

# Set up a theory-specific evaluator
"Build a Foucault evaluator for my discourse analysis project"

# Connect Zotero
"Connect my Zotero library to the assistant"

# Monitor literature automatically
"Set up daily PubMed alerts for [topic]"
```
