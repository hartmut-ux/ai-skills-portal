---
title: "AI Skills for Kimi, Claude & Codex"
description: "Download AI skills that run on Kimi Code CLI, Claude Code and Codex CLI. One shared core, thin per-platform wrappers."
keywords:
  - Kimi Code CLI skills
  - Claude Code skills
  - Codex CLI skills
  - AI skill library
  - multi-platform AI skills
---

# AI Skills for Kimi, Claude & Codex

A library of reusable AI skills that work across **Kimi Code CLI**, **Claude Code**, and **Codex CLI**. Each skill is maintained once and packaged automatically for every assistant.

## Why multi-platform skills matter

Most skills are tied to one assistant. This portal uses a **shared core + thin wrapper** pattern so you can:

- Write a skill once and ship it everywhere.
- Let users pick their favorite AI assistant.
- Keep maintenance low as assistants evolve.

## How to install a skill

### Kimi Code CLI

```bash
# Download the -kimi.zip or -all.zip, extract it, then:
cp -R .kimi/skills/<skill-name> ~/.kimi/skills/
```

Invoke in Kimi with `/<skill-name>`.

### Claude Code

```bash
# Download the -claude.zip or -all.zip, extract it, then:
cp -R .claude/skills/<skill-name> ~/.claude/skills/
```

Invoke in Claude with `<skill-name>`.

### Codex CLI

```bash
# Download the -codex.zip or -all.zip, extract it, then:
cp -R .codex/skills/<skill-name> ~/.codex/skills/
```

Invoke in Codex with `<skill-name>`.

## Available skills

> Downloads work after you publish a release. Replace `v0.1.0` in the links below with your actual release tag, or use `latest` once a release exists.

| Skill | Description | Download |
|---|---|---|
| [academic-research-suite](skills/academic-research-suite/) | Comprehensive academic research suite: deep research, paper writing, peer review, and publication pipeline. | [all](releases/download/v0.1.0/academic-research-suite-all.zip) · [kimi](releases/download/v0.1.0/academic-research-suite-kimi.zip) · [claude](releases/download/v0.1.0/academic-research-suite-claude.zip) · [codex](releases/download/v0.1.0/academic-research-suite-codex.zip) |
| [branded-visual-factory](skills/branded-visual-factory/) | Generates on-brand HTML/CSS infographics, cheat sheets, data cards, and carousel slides as code. | [all](releases/download/v0.1.0/branded-visual-factory-all.zip) · [kimi](releases/download/v0.1.0/branded-visual-factory-kimi.zip) · [claude](releases/download/v0.1.0/branded-visual-factory-claude.zip) · [codex](releases/download/v0.1.0/branded-visual-factory-codex.zip) |
| [content-engine](skills/content-engine/) | Universal content creation engine for newsletters, LinkedIn posts, blog articles, and multi-format repurposing. | [all](releases/download/v0.1.0/content-engine-all.zip) · [kimi](releases/download/v0.1.0/content-engine-kimi.zip) · [claude](releases/download/v0.1.0/content-engine-claude.zip) · [codex](releases/download/v0.1.0/content-engine-codex.zip) |
| [contentpulse-lead-magnet](skills/contentpulse-lead-magnet/) | Creates professional lead magnets from ContentPulse exports: cheat sheets, whitepapers, and presentations. | [all](releases/download/v0.1.0/contentpulse-lead-magnet-all.zip) · [kimi](releases/download/v0.1.0/contentpulse-lead-magnet-kimi.zip) · [claude](releases/download/v0.1.0/contentpulse-lead-magnet-claude.zip) · [codex](releases/download/v0.1.0/contentpulse-lead-magnet-codex.zip) |
| [critical-thinking-guardian](skills/critical-thinking-guardian/) | Background quality-control skill that applies critical thinking to every response. | [all](releases/download/v0.1.0/critical-thinking-guardian-all.zip) · [kimi](releases/download/v0.1.0/critical-thinking-guardian-kimi.zip) · [claude](releases/download/v0.1.0/critical-thinking-guardian-claude.zip) · [codex](releases/download/v0.1.0/critical-thinking-guardian-codex.zip) |
| [digitalscheck-navigator](skills/digitalscheck-navigator/) | Guides SMEs through all three modules of the Digitalscheck Liechtenstein funding program. | [all](releases/download/v0.1.0/digitalscheck-navigator-all.zip) · [kimi](releases/download/v0.1.0/digitalscheck-navigator-kimi.zip) · [claude](releases/download/v0.1.0/digitalscheck-navigator-claude.zip) · [codex](releases/download/v0.1.0/digitalscheck-navigator-codex.zip) |
| [first-principles-engine](skills/first-principles-engine/) | Strips any topic down to its fundamental truths using first-principles methodology. | [all](releases/download/v0.1.0/first-principles-engine-all.zip) · [kimi](releases/download/v0.1.0/first-principles-engine-kimi.zip) · [claude](releases/download/v0.1.0/first-principles-engine-claude.zip) · [codex](releases/download/v0.1.0/first-principles-engine-codex.zip) |
| [fullstack-app-builder](skills/fullstack-app-builder/) | End-to-end workflow for building production web apps, from idea to deployed product. | [all](releases/download/v0.1.0/fullstack-app-builder-all.zip) · [kimi](releases/download/v0.1.0/fullstack-app-builder-kimi.zip) · [claude](releases/download/v0.1.0/fullstack-app-builder-claude.zip) · [codex](releases/download/v0.1.0/fullstack-app-builder-codex.zip) |
| [grok-research-engine](skills/grok-research-engine/) | Deep research engine powered by the Grok API with web search, X/Twitter search, and multi-agent reasoning. | [all](releases/download/v0.1.0/grok-research-engine-all.zip) · [kimi](releases/download/v0.1.0/grok-research-engine-kimi.zip) · [claude](releases/download/v0.1.0/grok-research-engine-claude.zip) · [codex](releases/download/v0.1.0/grok-research-engine-codex.zip) |
| [humanizer](skills/humanizer/) | Removes typical AI-language patterns from German and English texts so they sound natural and human. | [all](releases/download/v0.1.0/humanizer-all.zip) · [kimi](releases/download/v0.1.0/humanizer-kimi.zip) · [claude](releases/download/v0.1.0/humanizer-claude.zip) · [codex](releases/download/v0.1.0/humanizer-codex.zip) |
| [impact-reporter](skills/impact-reporter/) | Creates impact reports, impact sections for funding proposals, and progress reports for any project. | [all](releases/download/v0.1.0/impact-reporter-all.zip) · [kimi](releases/download/v0.1.0/impact-reporter-kimi.zip) · [claude](releases/download/v0.1.0/impact-reporter-claude.zip) · [codex](releases/download/v0.1.0/impact-reporter-codex.zip) |
| [programmatic-infographics](skills/programmatic-infographics/) | Creates programmatic infographics and generative visual art using p5.js with seeded randomness. | [all](releases/download/v0.1.0/programmatic-infographics-all.zip) · [kimi](releases/download/v0.1.0/programmatic-infographics-kimi.zip) · [claude](releases/download/v0.1.0/programmatic-infographics-claude.zip) · [codex](releases/download/v0.1.0/programmatic-infographics-codex.zip) |
| [rag-text-optimizer](skills/rag-text-optimizer/) | Full RAG document optimization pipeline: re-extracts PDFs, fixes tables and layout, cleans OCR artifacts. | [all](releases/download/v0.1.0/rag-text-optimizer-all.zip) · [kimi](releases/download/v0.1.0/rag-text-optimizer-kimi.zip) · [claude](releases/download/v0.1.0/rag-text-optimizer-claude.zip) · [codex](releases/download/v0.1.0/rag-text-optimizer-codex.zip) |
| [token-saver](skills/token-saver/) | Reduces token consumption in assistant sessions through compression, filtering, and session-state management. | [all](releases/download/v0.1.0/token-saver-all.zip) · [kimi](releases/download/v0.1.0/token-saver-kimi.zip) · [claude](releases/download/v0.1.0/token-saver-claude.zip) · [codex](releases/download/v0.1.0/token-saver-codex.zip) |

## For skill authors

Want to add your own skill? See the [README](README.md) and copy `skills/example-skill/` as a starting point.

---

*Open source under MIT.*
