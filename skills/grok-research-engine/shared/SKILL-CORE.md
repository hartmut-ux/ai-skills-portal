---
name: grok-research-engine
description: "Deep research engine powered by the Grok API with web search, X/Twitter search, and multi-agent reasoning. Use this skill whenever the user wants to research a topic before creating content, needs current trends/news/statistics with source links, wants to find top-performing tweets or LinkedIn posts on a topic, needs scientific papers or expert opinions, or asks for market/competitor analysis with citations. Triggers on: 'recherchiere', 'research', 'finde aktuelle Quellen', 'was sagt die Forschung', 'aktuelle Trends zu', 'top posts zum Thema', 'Quellenrecherche', 'Deep Research', 'Grok research', 'find sources', 'what are people saying about', 'trending on X', or any research-before-content request. Also triggers when content-engine or content-strategist need a research foundation — this skill runs BEFORE content creation. Always use this skill when the user needs current, sourced information that goes beyond the assistant's training data."
---

# Grok Research Engine

A deep research skill that uses the xAI Grok API to gather current, sourced intelligence for content creation and strategic analysis.

## Prerequisites

- **xAI API Key**: Must be provided by the user (set as environment variable `XAI_API_KEY`)
- If no key is available, ask the user to provide one or create one at https://console.x.ai/

## How This Skill Works

This skill calls the Grok API's Responses endpoint with server-side tools (web_search, x_search) to gather real-time intelligence. It structures findings into a **Research Brief** that can be used standalone or fed into other skills (content-engine, content-strategist, newsletter-editor, etc.).

## Step 1: Determine Research Scope

Ask or infer from context:

| Parameter | Options | Default |
|-----------|---------|---------|
| **Topic** | User-defined | Required |
| **Brand context** | mmind.ai, FlowState Cyclist, ABCC, Kaizen, neutral | neutral |
| **Language** | DE, EN, or both | Infer from brand |
| **Depth** | Quick (1 API call) / Standard (2-3 calls) / Deep (4-6 calls) | Standard |
| **Focus areas** | See Research Modules below | All applicable |

### Research Modules (select based on query)

| Module | What it delivers | Grok tool config |
|--------|-----------------|------------------|
| **Trends & News** | Latest developments, breaking news, industry shifts | `web_search` with date filter (last 30 days) |
| **Statistics & Data** | Hard numbers, survey results, market data with source URLs | `web_search` with `allowed_domains` for trusted sources |
| **Expert Voices** | Quotes, opinions, thought leader positions | `web_search` + `x_search` |
| **Social Pulse** | Top-performing tweets and LinkedIn posts on the topic | `x_search` (primary), `web_search` for LinkedIn |
| **Scientific Sources** | Research papers, academic findings, meta-analyses | `web_search` with academic domain filter |
| **Competitor/Market** | What competitors are doing/saying, market positioning | `web_search` + `x_search` |
| **Authority Links** | ONE high-quality original source per content angle for LinkedIn post inclusion | `web_search` for papers, essays, primary reports |
| **Engagement Network** | DACH + UK LinkedIn/X accounts to comment on post-publication | `web_search` + `x_search` |

## Step 2: Execute Research via Grok API

Run the Python script at `scripts/grok_research.py` with the appropriate parameters.

### API Call Structure

The script uses the **Responses API** (`/v1/responses`) with these tools:

```
Tools:
  - type: web_search (for web content, statistics, papers)
  - type: web_search with x_search sources (for X/Twitter content)
```

### Model Selection

| Depth | Model | Why |
|-------|-------|-----|
| Quick | `grok-3-fast` | Speed, low cost |
| Standard | `grok-4.20-reasoning` | Good balance, reasoning enabled |
| Deep | `grok-4.20-reasoning` with extended reasoning | Maximum depth, cross-verification |

### Prompt Templates (built into the script)

The script assembles a research prompt based on selected modules. Each module has a specific instruction block:

**Trends & News:**
> "Search for the latest developments, news, and emerging trends about [TOPIC] from the past 30 days. Focus on credible sources (major publications, industry outlets, official announcements). For each finding, provide: the key insight, the source name, the source URL, and the publication date."

**Statistics & Data:**
> "Find current statistics, survey data, market figures, and quantitative evidence about [TOPIC]. Prioritize: government/institutional data, peer-reviewed studies, reputable research firms (Gartner, IDC, Statista, McKinsey Global Institute). For each statistic, provide: the exact figure, what it measures, the source with URL, and the date of the data."

**Expert Voices:**
> "Find notable expert opinions, thought leader statements, and authoritative commentary about [TOPIC]. Search both web publications and X/Twitter for influential voices. For each quote or opinion, provide: the person's name and title, their key statement (paraphrased), the source/platform, and the URL."

**Social Pulse:**
> "Search X/Twitter for the most engaging and insightful posts about [TOPIC] from the past 14 days. Focus on posts with high engagement (likes, reposts, replies) from credible accounts. Also search the web for recent high-performing LinkedIn posts on this topic. For each post, provide: the author and their role, the key message, engagement metrics if visible, and the URL."

**Scientific Sources:**
> "Search for peer-reviewed research papers, academic studies, and scientific publications about [TOPIC]. Focus on: recent publications (last 2 years preferred), high-impact journals, meta-analyses and systematic reviews. For each paper, provide: title, authors, journal/publication, year, key finding, and DOI or URL."

**Competitor/Market:**
> "Analyze the competitive landscape around [TOPIC]. Search for: what key players are doing/announcing, market positioning, product launches, strategic moves, and public commentary. For each competitor insight, provide: the company/person, what they did/said, the source with URL, and the date."

### Language Handling

| Brand | Search Language | Output Language |
|-------|----------------|-----------------|
| mmind.ai | DE + EN (parallel searches) | DE |
| FlowState Cyclist | EN | EN |
| ABCC | EN | EN |
| Kaizen | EN (+ DE for DACH) | Match user request |
| neutral | Match user language | Match user language |

For bilingual research (DE + EN), the script runs two separate API calls and merges results, de-duplicating overlapping sources.

## Step 3: Structure the Research Brief

The script outputs a structured **Research Brief** in Markdown format:

```markdown
# Research Brief: [TOPIC]
**Date:** [today]  |  **Depth:** [Quick/Standard/Deep]  |  **Brand:** [brand]

## Key Findings Summary
[3-5 bullet points with the most important takeaways]

## Trends & News
| # | Insight | Source | Date | URL |
|---|---------|--------|------|-----|
| 1 | ... | ... | ... | ... |

## Statistics & Data
| # | Figure | What it measures | Source | URL |
|---|--------|-----------------|--------|-----|
| 1 | ... | ... | ... | ... |

## Expert Voices
| # | Person & Title | Key Statement | Platform | URL |
|---|---------------|---------------|----------|-----|
| 1 | ... | ... | ... | ... |

## Social Pulse (Top Posts)
### X/Twitter
| # | Author | Key Message | Engagement | URL |
|---|--------|-------------|------------|-----|
| 1 | ... | ... | ... | ... |

### LinkedIn (if found)
| # | Author | Key Message | URL |
|---|--------|-------------|-----|
| 1 | ... | ... | ... |

## Scientific Sources
| # | Title | Authors | Journal/Year | Key Finding | URL/DOI |
|---|-------|---------|-------------|-------------|---------|
| 1 | ... | ... | ... | ... | ... |

## Competitor/Market Intelligence
| # | Player | Action/Statement | Source | Date | URL |
|---|--------|------------------|--------|------|-----|
| 1 | ... | ... | ... | ... | ... |

## Content Angles (suggested)
Based on this research, the strongest content angles are:
1. [angle with reasoning]
2. [angle with reasoning]
3. [angle with reasoning]

## Authority Links (for LinkedIn posts)
For each suggested content angle, identify ONE high-quality link suitable for direct inclusion in a LinkedIn post body. Must be:
- An academic paper, original essay, or primary data report
- From a recognized authority (Karpathy, Amodei, Lütke, a16z, academic institutions)
- NOT a news article summarizing someone else's work — the ORIGINAL source

| # | Post/Angle | Authority Link | Why it qualifies | URL |
|---|-----------|---------------|-----------------|-----|
| 1 | ... | ... | ... | ... |

## Engagement Network (Must-Comment Accounts)
Identify 8-12 LinkedIn and X/Twitter accounts in DACH + UK who are active on this topic and whose posts Hartmut should comment on after publishing. Focus on:
- Practitioners and executives (not just influencers)
- Accounts with relevant, engaged audiences
- Mix of DACH and UK voices

### LinkedIn Accounts (DACH + UK)
| # | Name | Role/Company | Why relevant | Profile URL |
|---|------|-------------|-------------|-------------|
| 1 | ... | ... | ... | ... |

### X/Twitter Accounts (DACH + UK)
| # | Name / @handle | Role | Why relevant | Profile URL |
|---|---------------|------|-------------|-------------|
| 1 | ... | ... | ... | ... |

## Source Quality Assessment
- Total sources found: [n]
- Tier 1 (institutional/academic): [n]
- Tier 2 (major media/industry): [n]
- Tier 3 (social/blog): [n]
- Consultancy/vendor sources: [n] (flag if data quality is low)
```

## Step 4: Handoff to Content Skills

The Research Brief is designed to feed directly into other skills:

| Next Skill | What to pass | How |
|------------|-------------|-----|
| `content-engine` | Full brief + suggested angles | User says "create LinkedIn post from this research" |
| `content-strategist` | Brief + brand context | User says "plan content calendar based on this" |
| `newsletter-editor` | Brief sections as article seeds | User says "use this for the next newsletter" |
| `brand-guardian` | Brief for graphic prompt inspiration | User says "create visual for this topic" |

The brief stays in the conversation context, so any subsequent content skill can reference it.

## Step 5: Export Options

After generating the Research Brief, offer:

1. **Markdown in chat** (default) — for immediate use in content creation
2. **DOCX export** — for sharing with team/clients (use the docx skill)
3. **Save as reference** — write to a file for later use in this session

## Error Handling

| Issue | Action |
|-------|--------|
| No API key | Ask user to provide one; link to https://console.x.ai/ |
| API rate limit | Wait 10 seconds, retry once; if still failing, inform user |
| Empty results for a module | Note in brief; suggest alternative search terms |
| API error | Show error message; suggest checking key validity |

## Usage Examples

**Quick research for a LinkedIn post:**
> "Recherchiere aktuelle AI-Adoption-Zahlen für DACH-KMU"
→ Runs: Statistics & Data + Trends & News (Quick depth, DE, mmind.ai brand)

**Deep research for a newsletter:**
> "Deep Research zum Thema cycling coaching technology trends für den nächsten Journal-Artikel"
→ Runs: All modules (Deep depth, EN, ABCC brand)

**Social pulse check:**
> "Was sind die top tweets und LinkedIn posts zu AI in SMEs diese Woche?"
→ Runs: Social Pulse + Expert Voices (Standard depth, EN, mmind.ai brand)

**Research + immediate content creation:**
> "Recherchiere zum Thema Digitalisierung im Gewerbe Liechtenstein und erstelle daraus einen LinkedIn Post"
→ Runs: This skill first, then hands off to content-engine/content-strategist
