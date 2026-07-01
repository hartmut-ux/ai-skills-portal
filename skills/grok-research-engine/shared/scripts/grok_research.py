#!/usr/bin/env python3
"""
Grok Research Engine v2 — calls xAI Responses API with web_search tools.
Outputs a structured Research Brief in Markdown.

Fixes in v2:
- Bilingual search (DE + EN) with Europe/UK focus for all modules
- Social Pulse: no longer requests direct post URLs (hallucination-prone),
  instead requests verifiable web articles ABOUT top posts/discussions
- Content Angles: synthesized via a separate API call at the end

Usage:
    python grok_research.py \
        --topic "AI adoption in DACH SMEs" \
        --modules trends,stats,experts,social,science,competitors \
        --depth standard \
        --language DE \
        --brand mmind

Environment:
    XAI_API_KEY — required, your xAI API key
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta

try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system(f"{sys.executable} -m pip install requests --break-system-packages -q")
    import requests

# ─── Config ───────────────────────────────────────────────────────────────────

API_BASE = "https://api.x.ai/v1/responses"
CHAT_API_BASE = "https://api.x.ai/v1/chat/completions"

MODELS = {
    "quick": "grok-4.20-fast",
    "standard": "grok-4.20-reasoning",
    "deep": "grok-4.20-reasoning",
}

CHAT_MODELS = {
    "quick": "grok-3-fast",
    "standard": "grok-3",
    "deep": "grok-3",
}

# ─── Bilingual search instruction (always applied) ───────────────────────────

BILINGUAL_SEARCH = (
    "IMPORTANT SEARCH INSTRUCTIONS: "
    "You MUST search in BOTH English AND German/local language. "
    "Include sources from across Europe and the UK — not just DACH. "
    "Aim for a balanced mix: at least 40% English-language sources "
    "(e.g. Reuters, Financial Times, The Economist, BBC, TechCrunch, "
    "Wired, European Commission, OECD, Eurostat, UK Government) "
    "and at least 30% German-language sources "
    "(e.g. Handelsblatt, Wirtschaftswoche, Bitkom, KfW, Destatis, NZZ). "
    "Do NOT return only German-language results. "
    "Run separate searches in English and German if needed."
)

# ─── Module prompts ───────────────────────────────────────────────────────────

MODULE_PROMPTS = {
    "trends": {
        "label": "Trends & News",
        "prompt": (
            "Search for the latest developments, news, and emerging trends about {topic} "
            "from the past 30 days. Focus on credible sources: major international publications "
            "(Reuters, Bloomberg, FT, BBC, Wired, TechCrunch), European institutions "
            "(European Commission, OECD, Eurostat), and quality DACH outlets "
            "(Handelsblatt, NZZ, Wirtschaftswoche, Der Standard). "
            "For each finding, provide:\n"
            "- **Insight**: The key finding in 2-3 sentences\n"
            "- **Source**: Publication name\n"
            "- **URL**: Full source URL\n"
            "- **Date**: Publication date\n"
            "- **Language**: EN or DE\n"
            "Return at least 6 findings, with a mix of English and German sources."
        ),
    },
    "stats": {
        "label": "Statistics & Data",
        "prompt": (
            "Find current statistics, survey data, market figures, and quantitative evidence about {topic}. "
            "Prioritize institutional and research sources: "
            "Eurostat, OECD, World Economic Forum, Gartner, IDC, Statista, "
            "Bitkom, KfW, IW Köln, European Commission Digital Economy reports, "
            "UK DSIT (Dept for Science Innovation & Technology). "
            "Consultancy and AI vendor sources (McKinsey, a16z, Anthropic, Deloitte, PwC etc.) "
            "are allowed BUT only when they provide PRIMARY DATA with: large samples (>500 respondents), "
            "transparent methodology, and original research — NOT recycled secondary data or pure opinion pieces. "
            "Flag any source where data quality is questionable.\n"
            "For each data point, provide:\n"
            "- **Figure**: The exact number/percentage\n"
            "- **Measures**: What it quantifies\n"
            "- **Source**: Institution/publication name with full URL\n"
            "- **Sample/Methodology**: Sample size and method if available (flag if unclear)\n"
            "- **Date**: When the data was collected/published\n"
            "- **Language**: EN or DE\n"
            "Return at least 6 data points from diverse sources."
        ),
    },
    "experts": {
        "label": "Expert Voices",
        "prompt": (
            "Find notable expert opinions, thought leader statements, and authoritative commentary "
            "about {topic}. Search for interviews, opinion pieces, keynote summaries, and published "
            "commentary in major outlets (HBR, MIT Sloan, WEF Agenda, Forbes, Handelsblatt, NZZ). "
            "For each expert voice, provide:\n"
            "- **Person**: Full name and title/role\n"
            "- **Key Statement**: Their main argument (paraphrased, 2-3 sentences)\n"
            "- **Source**: The publication where this appeared, with full URL\n"
            "- **Date**: Publication date\n"
            "Return at least 5 expert voices from both English and German sources."
        ),
    },
    "social": {
        "label": "Social Pulse",
        "split": True,  # Signal to orchestrator: run two separate API calls
        "x_prompt": (
            "Find the HIGHEST-PERFORMING posts on X/Twitter about {topic} "
            "from the LAST 5 DAYS ONLY (not older!).\n\n"
            "STRICT QUALITY FILTERS:\n"
            "- MINIMUM 100 likes per post. Ideally 200+ likes. Skip anything below 100 likes.\n"
            "- Posts must be from the last 5 days maximum.\n"
            "- Only include posts from real thought leaders, practitioners, founders, or executives "
            "— NO news bots, NO aggregator accounts, NO accounts with fewer than 1,000 followers.\n"
            "- If you cannot find 5 posts meeting these criteria for this exact topic, "
            "broaden slightly (e.g. AI + business, AI + SME, AI + digital transformation) "
            "but NEVER lower the engagement threshold below 100 likes.\n\n"
            "For each post, provide:\n"
            "- **Author**: Full name, @handle, follower count, and their role/title\n"
            "- **Post Summary**: What they said (key argument in 2-3 sentences)\n"
            "- **Why It Works**: What makes this post successful (hook technique, data usage, "
            "contrarian take, storytelling, visual, thread structure, etc.)\n"
            "- **Engagement**: Likes, reposts, replies, bookmarks, views — all metrics you can see\n"
            "- **Post URL**: The direct X post URL\n"
            "- **Posted**: Exact date\n\n"
            "Rank by engagement (highest first). Return 5-8 posts."
        ),
        "x_tools": [{"type": "x_search"}],
        "linkedin_prompt": (
            "Search for the HIGHEST-PERFORMING LinkedIn posts about {topic} "
            "from the LAST 5 DAYS ONLY (not older!).\n\n"
            "STRICT QUALITY FILTERS:\n"
            "- MINIMUM 100 likes/reactions per post. Ideally 200+. Skip anything below 100.\n"
            "- Posts must be from the last 5 days maximum.\n"
            "- Only include posts from established creators, executives, or domain experts "
            "with genuine authority — NO motivational fluff, NO recycled content.\n"
            "- If you cannot find 5 posts meeting these criteria for this exact topic, "
            "broaden slightly (e.g. AI + business, AI + leadership, digital transformation) "
            "but NEVER lower the engagement threshold below 100 reactions.\n\n"
            "I want to understand:\n"
            "- Which creators consistently drive high engagement on this topic\n"
            "- What content formats work best (text-only, carousel, document, poll, video)\n"
            "- What hook patterns and structures the top performers use\n\n"
            "For each post, provide:\n"
            "- **Author**: Full name, headline/title, approximate follower count if visible\n"
            "- **Post Summary**: Their key argument or insight (2-3 sentences)\n"
            "- **Why It Works**: Format, hook technique, engagement drivers\n"
            "- **Engagement**: Reactions, comments, reposts if visible\n"
            "- **Post URL**: The direct LinkedIn post URL\n"
            "- **Posted**: Exact date\n\n"
            "Rank by engagement (highest first). Return 5-8 posts."
        ),
        "linkedin_tools": [{"type": "web_search"}],
    },
    "science": {
        "label": "Scientific Sources",
        "prompt": (
            "Search for peer-reviewed research papers, academic studies, and scientific publications "
            "about {topic}. Focus on recent publications (last 2 years preferred), high-impact journals, "
            "meta-analyses and systematic reviews. Search Google Scholar, PubMed, arXiv, SSRN, "
            "and European research repositories. "
            "For each paper, provide:\n"
            "- **Title**: Full paper title\n"
            "- **Authors**: First author et al.\n"
            "- **Journal/Publication**: Name and year\n"
            "- **Key Finding**: 1-2 sentence summary of the main result\n"
            "- **URL**: DOI link (preferred) or direct URL to the paper\n"
            "Return at least 5 papers if available."
        ),
    },
    "competitors": {
        "label": "Competitor/Market Intelligence",
        "prompt": (
            "Analyze the competitive landscape around {topic}. Search for: what key players are "
            "doing/announcing, market positioning, product launches, strategic moves, and public "
            "commentary. Include European, UK, and international players. "
            "For each insight, provide:\n"
            "- **Player**: Company or person name\n"
            "- **Action**: What they did/said/launched (2-3 sentences)\n"
            "- **Source**: Publication with full URL\n"
            "- **Date**: When this happened\n"
            "Return at least 6 competitive insights."
        ),
    },
    "authority_links": {
        "label": "Authority Links (for LinkedIn posts)",
        "prompt": (
            "For the topic '{topic}', find 3-5 HIGH-AUTHORITY original source links "
            "suitable for direct inclusion in a LinkedIn post body. "
            "These must be ORIGINAL sources — not news articles summarizing someone else's work.\n\n"
            "Acceptable types:\n"
            "- Academic papers (direct link to paper, DOI, or institutional page)\n"
            "- Original essays or blog posts by recognized AI authorities "
            "(Andrej Karpathy, Dario Amodei, Tobi Lütke, Sam Altman, Jensen Huang, Satya Nadella, "
            "Ethan Mollick, Gary Hamel, etc.)\n"
            "- Primary data reports from institutions (a16z, WEF, OECD, Anthropic, etc.)\n"
            "- YouTube videos or talks by recognized authorities on this topic\n\n"
            "NOT acceptable: news articles, blog posts summarizing others' work, listicles.\n\n"
            "For each link, provide:\n"
            "- **Source**: Who created this (name + role)\n"
            "- **Title**: Title of the paper/essay/report\n"
            "- **Why it qualifies**: Why this is an authority source (1 sentence)\n"
            "- **Key insight**: The main takeaway relevant to our topic (1-2 sentences)\n"
            "- **URL**: Direct, full URL\n"
            "- **Date**: Publication date\n"
            "Rank by authority and relevance. These links will be used as in-post authority signals on LinkedIn."
        ),
    },
    "engagement": {
        "label": "Engagement Network (Must-Comment Accounts)",
        "split": True,
        "x_prompt": (
            "Find 5-8 X/Twitter accounts in the DACH region and UK who are ACTIVE practitioners "
            "and thought leaders on {topic}. NOT generic influencers — real practitioners, executives, "
            "researchers, or founders who regularly post substantive content on this topic.\n\n"
            "Requirements:\n"
            "- Must have posted about this topic in the last 14 days\n"
            "- Must have >1,000 followers\n"
            "- Prefer: CxOs, founders, researchers, senior practitioners\n"
            "- Mix: at least 3 DACH-based, at least 2 UK-based\n\n"
            "For each account, provide:\n"
            "- **Name**: Full name and @handle\n"
            "- **Role**: Current title and company\n"
            "- **Location**: DACH or UK\n"
            "- **Why relevant**: What they contribute to the conversation (1 sentence)\n"
            "- **Recent post**: A recent post URL on this topic\n"
            "- **Follower count**: Approximate"
        ),
        "x_tools": [{"type": "x_search"}],
        "linkedin_prompt": (
            "Find 5-8 LinkedIn accounts in the DACH region and UK who are ACTIVE practitioners "
            "and thought leaders on {topic}. NOT generic motivational posters — real practitioners, "
            "executives, researchers, or founders who regularly post substantive content.\n\n"
            "Requirements:\n"
            "- Must have posted about this topic in the last 14 days\n"
            "- Prefer: CxOs, founders, researchers, senior practitioners in SMEs or tech companies\n"
            "- Mix: at least 3 DACH-based, at least 2 UK-based\n\n"
            "For each account, provide:\n"
            "- **Name**: Full name\n"
            "- **Role**: Current title and company\n"
            "- **Location**: DACH or UK\n"
            "- **Why relevant**: What they contribute (1 sentence)\n"
            "- **Profile/Post URL**: LinkedIn profile or recent post URL\n"
            "- **Follower count**: Approximate if visible"
        ),
        "linkedin_tools": [{"type": "web_search"}],
    },
}

LANGUAGE_INSTRUCTIONS = {
    "DE": (
        "Present all findings in German. "
        "But you MUST search in both German AND English. "
        "Include English-language source URLs as-is (do not translate URLs). "
        "Translate only the insight/summary text into German."
    ),
    "EN": "Respond entirely in English. Search in both English and German but present findings in English.",
    "BOTH": (
        "Search in both German and English. Present findings in the user's primary language "
        "but keep source names and URLs in their original language."
    ),
}

BRAND_CONTEXT = {
    "mmind": (
        "Context: Research for MMIND.ai — an AI integration consultancy targeting SMEs in the "
        "DACH region (Liechtenstein, Switzerland, Austria, Germany) and broader Europe. "
        "Focus on practical, actionable insights for business leaders. "
        "Geographic priority: DACH > Europe > UK > Global."
    ),
    "flowstate": (
        "Context: Research for FlowState Cyclist — a platform for executives who use cycling "
        "and AI tools to improve productivity and leadership. "
        "Geographic priority: UK > Europe > Global."
    ),
    "abcc": (
        "Context: Research for the Association of British Cycling Coaches / Journal of Cycling Coaching. "
        "Geographic priority: UK > Europe > Global."
    ),
    "kaizen": (
        "Context: Research for Kaizen Institute — continuous improvement and lean management. "
        "Geographic priority: Europe > Global."
    ),
    "neutral": "",
}


# ─── API Callers ──────────────────────────────────────────────────────────────

def call_grok_responses_api(prompt, tools, model, api_key, reasoning=False):
    """Call the xAI Responses API (supports server-side tools)."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "model": model,
        "input": [{"role": "user", "content": prompt}],
        "tools": tools,
    }
    if reasoning and "reasoning" in model:
        payload["reasoning"] = {"effort": "high"}

    try:
        resp = requests.post(API_BASE, headers=headers, json=payload, timeout=180)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        return {"error": "API call timed out after 180 seconds"}
    except requests.exceptions.HTTPError:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:500]}"}
    except Exception as e:
        return {"error": str(e)}


def call_grok_chat_api(prompt, model, api_key, max_tokens=2000):
    """Call the xAI Chat Completions API (no tools, for synthesis)."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    try:
        resp = requests.post(CHAT_API_BASE, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Content angles could not be generated: {e}]"


# ─── Response Parser ─────────────────────────────────────────────────────────

def extract_text_and_citations(response):
    """Extract text content and citations from the Grok Responses API."""
    if "error" in response and "output" not in response:
        return f"ERROR: {response['error']}", []

    text_parts = []
    citations = []
    seen_urls = set()

    for item in response.get("output", response.get("content", [])):
        item_type = item.get("type", "")

        if item_type == "web_search_call":
            for source in item.get("action", {}).get("sources", []):
                url = source.get("url", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    citations.append({
                        "title": source.get("title", ""),
                        "url": url,
                    })

        elif item_type == "message":
            for content_block in item.get("content", []):
                if content_block.get("type") == "output_text":
                    text_parts.append(content_block.get("text", ""))
                    for ann in content_block.get("annotations", []):
                        if ann.get("type") == "url_citation":
                            url = ann.get("url", "")
                            if url and url not in seen_urls:
                                seen_urls.add(url)
                                citations.append({
                                    "title": ann.get("title", ""),
                                    "url": url,
                                })

        elif item_type == "text":
            text_parts.append(item.get("text", ""))

    return "\n".join(text_parts), citations


# ─── Content Angles Synthesizer ───────────────────────────────────────────────

def synthesize_content_angles(topic, research_text, brand, language, api_key, depth):
    """Use a separate API call to synthesize content angles from research findings."""
    lang_map = {"DE": "German", "EN": "English", "BOTH": "German"}
    output_lang = lang_map.get(language, "English")

    brand_angle = {
        "mmind": "for LinkedIn posts targeting DACH SME executives interested in AI adoption",
        "flowstate": "for FlowState Cyclist content targeting executive leaders who cycle",
        "abcc": "for Journal of Cycling Coaching articles and ABCC communications",
        "kaizen": "for Kaizen Institute thought leadership on continuous improvement",
        "neutral": "for professional content marketing",
    }.get(brand, "for professional content")

    prompt = (
        f"You are a senior content strategist. Based on the research findings below about "
        f"'{topic}', suggest exactly 5 concrete, specific content angles {brand_angle}.\n\n"
        f"For each angle, provide:\n"
        f"1. **Headline**: A compelling, specific headline (not generic)\n"
        f"2. **Hook**: The opening statement or question that grabs attention (1 sentence)\n"
        f"3. **Key Data Point**: The most impactful statistic or finding to anchor this piece\n"
        f"4. **Format**: Best format (LinkedIn post, carousel, long-form article, newsletter, infographic)\n"
        f"5. **Why Now**: Why this angle is timely right now (1 sentence)\n\n"
        f"Respond in {output_lang}. Be specific — no generic angles like 'AI is important'. "
        f"Every angle must reference concrete data from the research.\n\n"
        f"=== RESEARCH FINDINGS ===\n"
        f"{research_text[:6000]}"
    )

    model = CHAT_MODELS.get(depth, "grok-3")
    return call_grok_chat_api(prompt, model, api_key, max_tokens=2000)


# ─── Research Orchestrator ────────────────────────────────────────────────────

def run_research(topic, modules, depth, language, brand, api_key):
    """Run the full research pipeline and return a Markdown brief."""
    model = MODELS.get(depth, MODELS["standard"])
    reasoning = depth == "deep"
    lang_instruction = LANGUAGE_INSTRUCTIONS.get(language, LANGUAGE_INSTRUCTIONS["EN"])
    brand_ctx = BRAND_CONTEXT.get(brand, "")

    results = {}
    all_citations = []
    all_text_for_synthesis = []

    print(f"\n{'='*60}")
    print(f"  GROK RESEARCH ENGINE v2")
    print(f"  Topic: {topic}")
    print(f"  Modules: {', '.join(modules)}")
    print(f"  Depth: {depth} | Model: {model}")
    print(f"  Language: {language} | Brand: {brand}")
    print(f"{'='*60}\n")

    for mod_key in modules:
        if mod_key not in MODULE_PROMPTS:
            print(f"  ⚠ Unknown module '{mod_key}', skipping.")
            continue

        mod = MODULE_PROMPTS[mod_key]

        # ─── Split module (Social Pulse = X search + LinkedIn search) ─────
        if mod.get("split"):
            combined_text = []
            combined_citations = []

            # Part 1: X/Twitter via x_search
            print(f"  🔍 Researching: {mod['label']} (X/Twitter)...", end=" ", flush=True)
            x_prompt = (
                f"{brand_ctx}\n\n"
                f"{lang_instruction}\n\n"
                f"{mod['x_prompt'].format(topic=topic)}"
            )
            x_response = call_grok_responses_api(
                prompt=x_prompt,
                tools=mod["x_tools"],
                model=model,
                api_key=api_key,
                reasoning=reasoning,
            )
            x_text, x_citations = extract_text_and_citations(x_response)
            combined_text.append("### X/Twitter — Top Performing Posts\n\n" + x_text)
            combined_citations.extend(x_citations)
            if "ERROR" in x_text:
                print(f"❌ {x_text[:80]}")
            else:
                print(f"✅ ({len(x_citations)} posts)")
            time.sleep(2)

            # Part 2: LinkedIn via web_search
            print(f"  🔍 Researching: {mod['label']} (LinkedIn)...", end=" ", flush=True)
            li_prompt = (
                f"{brand_ctx}\n\n"
                f"{BILINGUAL_SEARCH}\n\n"
                f"{lang_instruction}\n\n"
                f"{mod['linkedin_prompt'].format(topic=topic)}"
            )
            li_response = call_grok_responses_api(
                prompt=li_prompt,
                tools=mod["linkedin_tools"],
                model=model,
                api_key=api_key,
                reasoning=reasoning,
            )
            li_text, li_citations = extract_text_and_citations(li_response)
            combined_text.append("\n### LinkedIn — Top Performing Creators & Posts\n\n" + li_text)
            combined_citations.extend(li_citations)
            if "ERROR" in li_text:
                print(f"❌ {li_text[:80]}")
            else:
                print(f"✅ ({len(li_citations)} posts)")
            time.sleep(2)

            full_text = "\n\n".join(combined_text)
            results[mod_key] = {
                "label": mod["label"],
                "text": full_text,
                "citations": combined_citations,
            }
            all_citations.extend(combined_citations)
            all_text_for_synthesis.append(f"### {mod['label']}\n{full_text[:2000]}")
            continue

        # ─── Standard module (single API call) ───────────────────────────
        print(f"  🔍 Researching: {mod['label']}...", end=" ", flush=True)

        full_prompt = (
            f"{brand_ctx}\n\n"
            f"{BILINGUAL_SEARCH}\n\n"
            f"{lang_instruction}\n\n"
            f"{mod['prompt'].format(topic=topic)}\n\n"
            f"Format your response with clear markdown structure. "
            f"Every source MUST have a working URL."
        )

        response = call_grok_responses_api(
            prompt=full_prompt,
            tools=[{"type": "web_search"}],
            model=model,
            api_key=api_key,
            reasoning=reasoning,
        )

        text, citations = extract_text_and_citations(response)
        results[mod_key] = {"label": mod["label"], "text": text, "citations": citations}
        all_citations.extend(citations)
        all_text_for_synthesis.append(f"### {mod['label']}\n{text[:2000]}")

        if "ERROR" in text:
            print(f"❌ {text[:80]}")
        else:
            print(f"✅ ({len(citations)} sources)")

        time.sleep(2)

    # ─── Synthesize Content Angles ────────────────────────────────────────────
    print(f"  💡 Synthesizing content angles...", end=" ", flush=True)
    synthesis_input = "\n\n".join(all_text_for_synthesis)
    content_angles = synthesize_content_angles(
        topic=topic,
        research_text=synthesis_input,
        brand=brand,
        language=language,
        api_key=api_key,
        depth=depth,
    )
    print("✅")

    # ─── Assemble the Research Brief ──────────────────────────────────────────
    today = datetime.now().strftime("%Y-%m-%d")

    # Rough language balance estimate
    de_indicators = [".de/", ".de.", "handelsblatt", "bitkom", "nzz.ch", "wirtschaftswoche",
                     "destatis", "kfw.", "iwkoeln", "t3n.", "heise.", "golem."]
    de_sources = sum(1 for c in all_citations
                     if any(d in c.get("url", "").lower() for d in de_indicators))
    en_sources = len(all_citations) - de_sources

    brief_lines = [
        f"# Research Brief: {topic}",
        f"**Date:** {today}  |  **Depth:** {depth}  |  **Brand:** {brand}  |  **Language:** {language}",
        f"**Sources:** {len(set(c.get('url', '') for c in all_citations))} unique "
        f"(~{en_sources} EN, ~{de_sources} DE)",
        "",
    ]

    for mod_key in modules:
        if mod_key in results:
            r = results[mod_key]
            brief_lines.append(f"---\n\n## {r['label']}\n")
            brief_lines.append(r["text"])
            brief_lines.append("")
            if r["citations"]:
                brief_lines.append(f"### Sources ({len(r['citations'])})")
                for i, c in enumerate(r["citations"], 1):
                    title = c.get("title", "Untitled")
                    url = c.get("url", "")
                    brief_lines.append(f"{i}. [{title}]({url})")
                brief_lines.append("")

    brief_lines.append("---\n\n## Suggested Content Angles\n")
    brief_lines.append(content_angles)
    brief_lines.append("")

    brief_lines.append("---\n\n## Source Quality Assessment\n")
    brief_lines.append(f"- **Total unique sources:** {len(set(c.get('url', '') for c in all_citations))}")
    brief_lines.append(f"- **Total citations:** {len(all_citations)}")
    brief_lines.append(f"- **English-language sources:** ~{en_sources}")
    brief_lines.append(f"- **German-language sources:** ~{de_sources}")
    brief_lines.append("")

    return "\n".join(brief_lines)


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Grok Research Engine v2")
    parser.add_argument("--topic", required=True, help="Research topic")
    parser.add_argument(
        "--modules", default="trends,stats,experts,social",
        help="Comma-separated: trends,stats,experts,social,science,competitors",
    )
    parser.add_argument("--depth", default="standard", choices=["quick", "standard", "deep"])
    parser.add_argument("--language", default="EN", choices=["DE", "EN", "BOTH"])
    parser.add_argument("--brand", default="neutral",
                        choices=["mmind", "flowstate", "abcc", "kaizen", "neutral"])
    parser.add_argument("--output", default=None, help="Output file path (default: stdout)")
    args = parser.parse_args()

    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("ERROR: XAI_API_KEY environment variable not set.")
        print("Set it with: export XAI_API_KEY='your-key-here'")
        sys.exit(1)

    modules = [m.strip() for m in args.modules.split(",")]
    brief = run_research(
        topic=args.topic, modules=modules, depth=args.depth,
        language=args.language, brand=args.brand, api_key=api_key,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(brief)
        print(f"\n📄 Research Brief saved to: {args.output}")
    else:
        print("\n" + "=" * 60)
        print(brief)

    return brief


if __name__ == "__main__":
    main()
