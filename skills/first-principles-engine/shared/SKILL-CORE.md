---
name: first-principles-engine
description: Strips any topic down to its fundamental truths using Elon Musk's first principles methodology — deletion, presence at the problem, and relentless speed. Use this skill whenever the user wants to deeply analyze a topic, challenge assumptions, rethink a business model, question conventional wisdom, do a first principles analysis, strip something down to basics, or says things like "break this down", "what's really true here", "challenge my assumptions", "rethink this from scratch", "what am I missing", or "strip this down". Also triggers for strategic analysis, competitive rethinking, innovation brainstorming, or when the user wants to rebuild a concept from the ground up. Do NOT use for simple factual questions, quick summaries, or routine document creation.
---

# First Principles Engine

A structured methodology for stripping any topic down to its load-bearing truths — inspired by Elon Musk's approach of ruthless deletion, direct presence at the problem, and execution speed that forces everything else to reorganize around it.

## Philosophy

Most thinking is inherited. People adopt assumptions from their industry, education, peers, and culture without ever testing whether those assumptions are structurally necessary. This skill systematically identifies and removes every assumption that isn't load-bearing — until only provable, fundamental truths remain. Then it rebuilds from that foundation.

Three operating principles (from Jensen Huang's analysis of Musk):

1. **Deletion** — Question everything to the point where it's at its minimal amount. Every part, process, and assumption that survived because no one had the nerve to kill it gets picked up and tested. If it's not absolutely load-bearing, it's gone. Not simplified. Not optimized. Removed.

2. **Presence** — Go directly to the actual problem. Not the slides about the problem. Not the summary of the problem. The problem itself. Collapse the distance between the failure and the person trying to fix it.

3. **Speed** — Move so fast that everyone else's normal pace feels like standing still. Urgency demonstrated, not demanded.

---

## Workflow: Two Phases

This skill works in two phases. Phase 1 generates research prompts so the user can gather deep source material. Phase 2 (after the user feeds back research results) performs the actual first principles teardown.

---

### PHASE 1: Deep Research Prompt Generation

When the user names a topic, IMMEDIATELY generate two research prompts — one for NotebookLM and one for Grok Deep Research. Do not analyze the topic yet. The goal is to first build a comprehensive evidence base from original sources before stripping anything down.

#### NotebookLM Prompt

Generate a prompt optimized for NotebookLM's source-based analysis. NotebookLM works best when it synthesizes across uploaded documents, so the prompt should instruct the user on what types of sources to upload AND provide analysis instructions.

Use this template (adapt to the specific topic):

```
TOPIC: [topic]

SUGGESTED SOURCES TO UPLOAD:
- [3-5 specific types of sources relevant to this topic: academic papers, industry reports, regulatory documents, financial filings, founding documents, technical specifications, etc.]
- Prioritize PRIMARY sources over commentary
- Include at least one source that CHALLENGES the mainstream view

ANALYSIS INSTRUCTIONS:
Once sources are loaded, analyze the following:

1. ASSUMPTION INVENTORY: What are the 10-15 most commonly held assumptions about [topic]? For each, note which source supports or contradicts it.

2. EVIDENCE MAP: For each assumption, what is the actual empirical evidence? Distinguish between:
   - Proven facts (replicable, measurable)
   - Strong correlations (observed but not causal)
   - Expert opinions (authoritative but not proven)
   - Industry conventions (widely practiced but never tested)
   - Inherited beliefs (accepted without question)

3. CONTRARIAN SOURCES: Which sources challenge the dominant narrative? What specific claims do they make and what evidence do they provide?

4. HISTORICAL CONTEXT: When and why did the current consensus form? What conditions existed then that may no longer exist?

5. STAKEHOLDER MAPPING: Who benefits from the current assumptions staying unchallenged? Who would benefit if they were overturned?

Produce a structured report with citations for every claim.
```

#### Grok Deep Research Prompt

Generate a prompt optimized for Grok's deep research capabilities (real-time web access, X/Twitter integration, broad source scanning). Grok excels at finding current discourse, contrarian voices, and real-time data.

Use this template (adapt to the specific topic):

```
TOPIC: [topic]

Conduct deep research on [topic] with the following specific focus:

1. CURRENT STATE OF PLAY
   - What is the dominant consensus on [topic] right now?
   - What are the 2-3 most influential recent publications, talks, or posts?
   - What data points are most frequently cited?

2. DISSENTING VOICES
   - Who are the most credible people/institutions challenging the mainstream view?
   - What specific arguments and evidence do they present?
   - Find posts/threads on X where experts debate or disagree about [topic]

3. ORIGINAL SOURCES
   - Academic papers (last 5 years) with actual data, not just opinion
   - Industry reports with verifiable metrics
   - Government/regulatory documents
   - Patent filings or technical publications (if relevant)
   - Financial data or market research (if relevant)

4. FAILURE ANALYSIS
   - Where has the conventional approach to [topic] failed?
   - Case studies of companies/projects/policies that went against conventional wisdom — what happened?
   - What predictions about [topic] turned out wrong, and why?

5. FIRST PRINCIPLES CLUES
   - What are the fundamental physics/economics/biology (whichever applies) underlying [topic]?
   - What constraints are actually physical/mathematical vs. merely conventional?
   - Where is the gap between what's theoretically possible and what's currently done?

Provide all sources with links. Prioritize primary sources over secondary commentary. Flag where sources contradict each other.
```

After generating both prompts, tell the user:

> "Here are your research prompts. Feed these into NotebookLM (with the suggested source types uploaded) and Grok Deep Research. Once you have the results, paste them back here and I'll perform the first principles teardown."

**STOP HERE and wait for the user to return with research results.**

---

### PHASE 2: First Principles Teardown

Once the user provides the research results (from NotebookLM, Grok, or any other source), perform the full teardown. Follow these steps in order. Be thorough — this is the core value of the skill.

#### Step 1: Assumption Extraction

From the research material AND your own knowledge, compile the complete list of assumptions people commonly make about this topic. Cast a wide net. Include:

- Industry "best practices" that nobody questions
- "Everyone knows" statements
- Definitions that are treated as fixed
- Metrics that are treated as the right ones to measure
- Historical approaches that persist by inertia
- Expert consensus that lacks recent empirical testing

Present these as a numbered list. For each assumption, note where it comes from (research source, industry convention, cultural norm, etc.).

#### Step 2: Load-Bearing Test

For EACH assumption, apply the Musk deletion test:

**"Is this assumption absolutely load-bearing? If I remove it, does the structure collapse — or does it still stand?"**

Classify every assumption into one of three categories:

| Category | Meaning | Action |
|---|---|---|
| **BEDROCK** | Provably true. Supported by physics, mathematics, verifiable data, or replicated research. The structure collapses without it. | Keep. This is foundation. |
| **SCAFFOLDING** | Was useful when it was built, but the building can stand without it now. Convention, not necessity. | Remove. Examine what opens up. |
| **DECORATION** | Never was structural. Exists because of tradition, comfort, status quo bias, or someone's unexamined preference. | Delete immediately. |

For each classification, provide the reasoning. Reference the research sources where possible. Be direct — don't hedge when the evidence is clear.

#### Step 3: The Skeleton

After deletion, present what remains: the bare load-bearing structure. Only bedrock truths. Write these as clear, declarative statements.

Format:

> **What is fundamentally, provably true about [topic]:**
>
> 1. [Bedrock truth] — *Evidence: [source]*
> 2. [Bedrock truth] — *Evidence: [source]*
> ...

This should feel dramatically simpler than the original topic. If it doesn't feel like a significant reduction, you haven't deleted enough. Go back and be more ruthless.

#### Step 4: Rebuild

Now reconstruct from the skeleton. Ask: if you only knew these bedrock truths and had no inherited thinking, what would you build?

Explore:

- **What becomes possible** that wasn't visible before?
- **What changes** when you remove the scaffolding and decoration?
- **What would you do differently** starting from zero?
- **Where is the gap** between the rebuilt version and current reality?

Be specific and concrete. Reference the research material. This is where the real insight lives.

#### Step 5: Action Map

End with concrete, actionable next steps. For each insight from the rebuild:

- What is one thing the user could do THIS WEEK based on this insight?
- What is the biggest assumption their competitors/peers still hold that creates an opportunity?
- What would "moving at Musk speed" look like for this specific situation?

---

## Output Format

Always structure the final output clearly:

```
## First Principles Analysis: [Topic]

### Assumptions Identified
[Numbered list with sources]

### Load-Bearing Test Results
[Table or structured list: Bedrock / Scaffolding / Decoration]

### The Skeleton — What's Actually True
[Numbered bedrock truths with evidence]

### Rebuilt from Zero
[Concrete insights and alternative approaches]

### Action Map
[Specific next steps]
```

---

## Important Guidelines

- **Be ruthless in deletion.** The natural tendency is to keep too much. Most assumptions are scaffolding or decoration. If you're classifying more than 30% as bedrock, you're probably not questioning hard enough.
- **Use the research.** The whole point of Phase 1 is to have evidence. Don't make claims without grounding them in the sources the user provided.
- **Name the sacred cows.** The most valuable assumptions to challenge are the ones nobody talks about — the ones so deeply embedded they feel like facts rather than choices.
- **Stay concrete.** Abstract philosophy is easy. Specific, actionable insight is hard. Push for the specific.
- **Match the user's context.** If the user is an SME leader, frame insights for SME reality. If they're analyzing a technology, go technical. Adapt the depth and framing to who's asking.
