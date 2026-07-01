---
name: content-engine
description: "Universal content creation engine for newsletters, LinkedIn posts, blog articles, thought leadership, and multi-format content repurposing. Use this skill whenever the user wants to create a newsletter edition, write LinkedIn posts, draft blog articles, create whiteboard graphic prompts, develop editorial calendars, repurpose content across formats, or produce any structured marketing content — for MMIND.ai, Hartmut Hübner personal, or any new brand. Also triggers when the user mentions 'newsletter', 'LinkedIn post', 'content calendar', 'editorial', 'teaser', 'carousel', 'whiteboard graphic', 'Nano Banana prompt', 'content repurposing', 'ghost-writing', 'thought leadership', 'WEF blog', or any content production task. For Kaizen Institute content, use the dedicated Kaizen skill instead."
---

# Content Engine

A universal system for research-backed, brand-consistent content creation across multiple brands, formats, and channels. Built on First Principles thinking: every sentence proves or illustrates something — or it gets deleted.

## How This Skill Works

This skill separates **process** (always the same) from **brand configuration** (loaded per project). The workflow, quality gates, and research approach are universal. The voice, visual system, and format specs come from brand-specific reference files.

## Step 1: Identify the Brand

Before creating any content, determine which brand context applies:

| Signal | Brand | Reference File |
|--------|-------|----------------|
| MMIND.ai, Flow Factor, Hartmut personal LinkedIn | MMIND.ai / Hartmut Hübner | `references/brand-mmind.md` |
| New or unrecognized brand | Ask the user | Create new reference file |
| Kaizen Institute, KAIZEN™ News | **→ Use dedicated Kaizen skill** | Not in this skill |

Load the relevant reference file before producing any content. If unsure, ask.

## Step 2: Identify the Format

| User Request | Format | Key Constraints |
|-------------|--------|-----------------|
| "Create the next newsletter" | Newsletter Edition | Full deliverable (11 components), 1.200-1.500 words |
| "Write a LinkedIn post" | LinkedIn Post | Hook-bridge-solution-CTA; zero-click value; no external links |
| "Draft a blog article" / "ghost-write for [leader]" | Authored Article | Match named author's voice; evidence-based; structured |
| "Create a carousel" | LinkedIn Carousel | 8-10 slides; one idea per slide; max 40 words per slide |
| "Create a whiteboard graphic prompt" | Visual Prompt | Brand-specific color palette; complete copy-paste-ready prompt |
| "Repurpose this content" | Multi-Format | Apply repurposing workflow from reference file |
| "Write a teaser / intro" | Newsletter Element | Follow fixed structure from brand reference |
| "Plan a content week" | Editorial Calendar | Narrative Arc + First-Principles filter; 5 posts + newsletter |

## Step 3: Research First

Every piece of content is research-backed. The depth scales with complexity.

### Research Protocol

**For weekly planning and newsletters (use Grok research engine):**
1. Trigger `grok-research-engine` skill with topic, modules (trends, stats, experts, social), and depth
   - **Model selection:** Always use the latest available reasoning model. Do NOT hardcode model names — query the /v1/models endpoint first and select the highest-tier reasoning model available. This prevents breakage when xAI updates model names.
2. Search the brand's website for source material
3. Verify all links, statistics, and quotes
4. Cross-reference claims with multiple sources

**For LinkedIn posts (1-3 tool calls):**
1. Verify any statistics or claims cited
2. Check for current context (has anything changed since the source was published?)

**For repurposed content (0-1 tool calls):**
1. Verify links still work
2. Check if new data strengthens the piece

### Source Rules (Universal)

**Always allowed:** Academic journals, international media (Fortune, FT, Bloomberg, Reuters, HBR, MIT Sloan), institutional sources (WEF, OECD, IMF, ILO, Gallup, IFR, IDC), industry associations, government data.

**Consultancy & AI vendor sources (McKinsey, a16z, Anthropic, Gartner, etc.):** Allowed when citing their PRIMARY DATA with large samples (>500), transparent methodology, and own research. NOT allowed: pure opinion/thought leadership blog posts without own data. The data is fine — the editorial framing is not a source.

**Note for Kaizen-branded content:** Competitor consultancies (BCG, Bain, Deloitte, PwC, EY, KPMG, Accenture, Roland Berger, Oliver Wyman, Capgemini) remain excluded as sources per Kaizen brand requirements. Their data may be referenced only when independently verifiable.

**Authority Links (for LinkedIn posts):** Each post should identify ONE high-quality link to include directly in the post body — an academic paper, an original essay by an AI authority (Karpathy, Amodei, Lütke etc.), or a primary data report. This link serves as an authority signal, not as a traffic redirect.

**Grok/NotebookLM results:** Treat as research leads, not sources. Always verify the original source before citing. Never write "according to Grok."

## Step 4: Apply First Principles Filter

Before writing ANY content, run these checks. **This filter runs AUTOMATICALLY at the end of every content production** — not just when explicitly requested. It is a permanent background layer.

1. **What is the one load-bearing truth of this post?** If you can't say it in one sentence, the post isn't ready.
2. **What assumption am I making that I haven't tested?** Check against research data.
3. **What can I delete without losing the core message?** If it's not load-bearing: remove — not simplify.
4. **Am I explaining something that would be better shown through an example?**

## Step 5: Create Content

Follow the brand-specific structure from the loaded reference file. Universal rules apply to all brands:

### Universal Writing Rules

**Hooks:** First 2 sentences determine whether the content gets read. Lead with specific insight, data, or tension — never with corporate announcements or clichés.

**Structure:** Problem → Solution → Proof. Not: "You have a problem → You should do X." The reader sees the solution in action, not a lecture about what to do.

**Paragraphs:** Maximum 3 sentences. Use white space generously. One idea per paragraph.

**Voice:** Active voice. Specific nouns and verbs. Concrete numbers over vague claims ("47% reduction in 12 weeks" beats "significant improvement").

**Evidence:** Pair claims with sources. Include timeframes with metrics. Attribute quotes with full name and title.

**"Du"-Dosierung (MMIND.ai / Hartmut):** Use "Du" sparingly — only in CTAs, direct questions, and personal bridge moments. Main text follows Problem → Solution → Proof structure without constant reader-addressing. SME CEOs want to see solutions, not be coached.

**Test:** Read the text without every "Du"-sentence. Does it still work? Then the "Du"-sentences were filler.

### Piggybacking Strategy (LinkedIn)

When a well-known AI thought leader goes viral and the topic connects to one of the four strategic angles:

1. **Identify** the viral post/trend (Karpathy, Lütke, Dorsey, Altman, Huang, Nadella, Amodei)
2. **Formulate own thesis** — don't retell their post
3. **Connect with own project or experience** — concrete, with numbers
4. **Translate to SME reality** — "What does this mean for a company with 30 employees?"
5. **Visual shows your angle** — not the original poster's point

**Why it works:** The algorithm rewards topic-relevance. The original figure provides authority; you provide practical application. SME decision-makers may not know these figures — you translate.

**Proven results:** Hartmut's top-performing post (67K impressions) piggybacked on Jack Dorsey.

### Metaphor Rules

- **Encouraged:** Context-appropriate metaphors that fit the topic. Sport/performance (cycling, football, relay teams, time trials), industry/trade, craft/Handwerk, engineering, nature — whatever resonates with the specific audience and topic. The metaphor should come FROM the reader's world, not from ours. A construction CEO resonates with building-site metaphors. A manufacturing CEO with production-line metaphors. Match the metaphor to the audience.
- **Forbidden:** Medical metaphors (amnesia, Alzheimer, diagnosis, surgery, therapy, symptoms). Political metaphors (war, battle, enemy, victory, defeat). These can offend or polarize.
- **Principle:** Context-driven selection. Sport metaphors work for agility/speed topics. Production metaphors for process excellence. Nature metaphors for ecosystem thinking. Choose the metaphor family that fits the reader's professional context, not the writer's preference.

### Universal Forbidden Patterns

These apply to ALL brands, ALL formats:

| Pattern | Why | Replace With |
|---------|-----|-------------|
| "Thrilled to announce" | Corporate fluff | Lead with the news itself |
| "Proud to share" | Self-congratulatory | State achievement + impact |
| "Best-in-class" / "Industry-leading" | Empty superlative | Name the specific benchmark |
| "In today's fast-paced world" | Cliché opener | Concrete observation |
| "Delve into" / "Dive into" | Overused, AI-flagged | "Explore," "Examine," "Uncover" |
| "Synergy" / "Leverage" (verb) | Corporate jargon | Plain language: "combine," "use" |
| "Unlock potential" | Abstract | Specific outcome with metric |
| "Paradigm shift" / "Ecosystem" | Dated buzzwords | Describe what actually changed |
| "Journey" (business context) | Overused metaphor | "Program," "transformation," "process" |
| Passive voice as default | Reduces energy | Active: subject + verb + object |
| "eigentlich", "irgendwie" | Qualifiers that weaken | Delete or make specific |
| Generic "KI" / "AI Tools" | Too abstract | Name the specific tool |

### LinkedIn Algorithm Alignment (360Brew 2026 — applies to all brands)

1. **Semantic alignment:** Content must connect to the brand's expertise vector. Drift = algorithmic penalty. 360Brew cross-references your profile, network, engagement patterns, and content for consistency.
2. **Zero-click value:** Deliver full insight within the post. External links reduce reach ~60%.
3. **Save-worthy:** Saves are a TOP signal for 360Brew. Prioritize utility (frameworks, checklists, how-to) over announcements.
4. **Dwell Time:** Posts that hold attention >60 seconds get boosted. Substance > brevity.
5. **Anti-corporate hooks:** No "thrilled to announce" — 360Brew's NLP fluff detector is real.
6. **Anti-engagement-bait:** Keyword-comment CTAs ("Comment 'Framework'"), "Agree or disagree?", "Comment YES" are now PENALIZED. Use substantive questions instead.
7. **Link strategy (3-tier):**
   - **1 Authority Link in post:** Academic paper, original essay, or YouTube from an AI authority. In parentheses after naming the source. Maximum 1 link per post.
   - **Additional links in first comment** OR via **"Edit After Post"** (publish without links, wait 60-90 min, then edit to add). List these separately in the content package as "Links for later insertion."
   - **Promotional links:** Never in post body. Profile featured section or comment only.
8. **Post-engagement obligation:** "Post and ghost" is penalized. After every post: 30-50 minutes of active, substantive commenting on relevant posts in your niche. Grok research delivers weekly "Must-comment" account lists.
9. **Anti-AI-detection:** 360Brew detects and deprioritizes pure AI-generated text. the assistant delivers the draft — the human MUST personally edit: add own anecdotes, specific client situations, unusual formulations. Every post must carry personal voice.
10. **Hashtags:** No longer play a role in distribution. Max 1-3 or omit entirely.
11. **Posting frequency:** Quality > volume. 4-5x/week is sufficient.

## Step 6: Quality Gates

Before presenting ANY content, verify all of these:

### Structure Check
- [ ] Correct number of elements per format
- [ ] All mandatory components present
- [ ] Word counts within specified limits
- [ ] One clear insight per post (not three competing messages)

### Voice Check
- [ ] Matches the loaded brand voice (not generic)
- [ ] No forbidden phrases from either universal or brand-specific lists
- [ ] Active voice throughout
- [ ] Specific outcomes and metrics included
- [ ] "Du"-Dosierung checked (not overused)
- [ ] Perspective: advisor/observer (not affected manager)

### Research Check
- [ ] Statistics verified against original source
- [ ] Links tested (or flagged for user to test)
- [ ] All links full URLs with `https://`
- [ ] Quotes accurately attributed
- [ ] No competitor consultancy content used as source
- [ ] At least one concrete tool named (not generic "AI")

### Algorithm Check (LinkedIn — 360Brew 2026)
- [ ] Hook delivers value in first 2 sentences
- [ ] Maximum 1 authority link in post body (paper, essay, or AI authority video)
- [ ] Additional links listed for first comment or "Edit After Post"
- [ ] No engagement-bait CTAs ("Comment 'X'", "Agree or disagree?")
- [ ] CTA is a substantive question, save-trigger, or newsletter reference
- [ ] Content connects to brand's expertise vector (topic authority)
- [ ] Passes the "Save Test" — would someone reference this again in 30 days?
- [ ] Dwell Time likely >60 seconds (substantial enough)?
- [ ] Post doesn't read as pure AI output (personal voice, specific examples)?
- [ ] Engagement account list included for post-publication commenting?
- [ ] MMIND.ai Company Post included for this week (German, CTA → mmind.space)?

### Critical Thinking Check
- [ ] Assumptions identified and tested (Gate 1)
- [ ] Argument logically valid — no hasty generalization, no survivorship bias (Gate 2)
- [ ] Evidence sufficient and high-quality (Gate 3)
- [ ] Counter-arguments acknowledged where relevant (Gate 4)
- [ ] First Principles filter passed (one load-bearing truth in one sentence)

### CEO Reality Check (FINAL GATE)
This gate runs ALWAYS after all other gates, for every content piece.
- [ ] Would a KMU CEO (10–250 employees) nod or roll their eyes at this?
- [ ] Is every claim backed by a concrete number or named source?
- [ ] Would a CEO forward this to their team?
- [ ] Is the language sober, simple, humble, and condensed enough?
- [ ] Does the post address a REAL, VALIDATED pain point — not an assumed one?
- [ ] Is the perspective always: advisor who observes patterns across organizations — never a lecturer?

### Visual Check
- [ ] Graphic prompt included (correct format, portrait for LinkedIn)
- [ ] Visual style varies (not 3x in a row the same)
- [ ] Visual is surprising, topical, org-level (not generic tool screenshot)
- [ ] Concrete numbers visible in graphic where applicable
- [ ] Format matches current platform trends (check what's performing NOW on LinkedIn before selecting format)

### Visual System Update (April 2026)
- **New formats:** Cheat Sheets (single-image, dense information, save-worthy) for Education/How-To posts
- **Deprecated:** Carousels (April 2026 — almost nobody posts carousels anymore; underperforming). Keep carousel SKILL definition but note it's currently underperforming; use sparingly.
- **Dynamic format sensing:** Before choosing a visual format, check what's currently working on LinkedIn (via Grok social pulse or manual observation). Format trends shift — the system should adapt, not be rigid. The visual format adapts to the topic and current platform trends. What works this month may not work next month. Always check what's performing NOW.

## Step 7: Repurposing Workflow

When repurposing content across formats, follow the brand's repurposing workflow from the reference file. Universal principle: **One insight, multiple expressions, zero copy-paste.** Every format has different constraints — repurposing means re-engineering for each context, not reformatting the same text.

### The "So What?" Test (apply before publishing any repurposed content)
1. Does this deliver value without the original source?
2. Would this feel repetitive to someone who saw the original?
3. Does the format match the platform?
4. Would someone save this?

## Hartmut's Communication Style (HH DNA 2.0)

This style applies when writing as Hartmut Hübner personally or when the content should carry his voice. It also serves as the quality benchmark for all content — even brand content should meet these standards of clarity and actionability.

### Core Principles
- **Peer-to-peer, not lecturer-to-student.** Write as an experienced advisor speaking with equals.
- **Radical pragmatism.** Everything must be immediately usable. Share best knowledge generously.
- **Show, don't explain.** Teach through concrete stories and practice examples, not abstractions.
- **Show your own mistakes.** Vulnerability builds trust faster than polish.
- **First Principles in writing:** Every sentence that isn't load-bearing gets deleted — not simplified.

### Voice Mechanics
- **Perspective:** "Ich" for personal experience, "Du" sparingly for direct engagement, "Wir" for shared insights
- **Sentence length:** 10-15 words ideal. Max 2-3 sentences per paragraph.
- **Numbers over adjectives:** "10 hours per week" not "a lot of time"
- **Swiss spelling:** "ss" not "ß" (Strasse, Schweiss, etc.)
- **Sport metaphors:** Natural fit for teamwork, speed, performance, agility — sport is the method, business concept is the goal. NEVER medical metaphors.
- **Concrete tools always named:** the assistant Cowork, your AI assistant, Lovable, n8n, Gemini, Google AI Studio — never generic "AI"

### Structure (every text)
1. Problem — what's broken, expensive, or surprising
2. Bridge — your experience or observation
3. Solution — concrete application with named tools
4. Proof — numbers, before/after, real case

### Quality Test (after every text)
- Can the reader act immediately?
- Did I show rather than explain?
- Is it easy to scan?
- Would I say it this way in person?
- Is it short enough?
- Is every "Du" earned, not reflexive?

### What to Avoid
- Motivational phrases
- Lecturing formulations ("Du solltest...")
- Passive constructions
- Jargon without explanation
- Medical metaphors (amnesia, Alzheimer, diagnosis, etc.)
- Any sentence that doesn't earn its place

## Reference Files

Load these as needed based on the identified brand:

| File | When to Load | What It Contains |
|------|-------------|-----------------|
| `references/brand-mmind.md` | Any MMIND.ai or Hartmut Hübner content | 7 LinkedIn post types with structures, Flow Factor Newsletter structure, visual system (flat vector SaaS + Nano Banana prompts), CTA library, content calendar logic |

These files contain ALL brand-specific details: mandatory structures, color palettes, typography specs, format specifications, quote libraries, and repurposing workflows.

**Note:** Kaizen Institute content is handled by a separate, dedicated Kaizen skill. Do not load `brand-kaizen.md` from this skill.
