# Parallel Sub-Agent Review

**When to use this instead of the built-in reviewer:**  
The `academic-paper-reviewer` skill runs agents sequentially in one context window. Use *parallel sub-agents* when you want multiple independent critiques that cannot influence each other — each agent works in its own context, so their outputs stay uncontaminated.

**Key principle**: The purpose of sub-agents is to install walls between critiques. If methodology critique sees argument critique first, it is already colored by it. Parallel sub-agents prevent this.

---

## Use Case 1: Multi-Dimensional Paper Critique

Get 2–4 independent assessments of the same draft simultaneously.

### Setup prompt (run once per project)

```
Create two sub-agents for me:

1. Sub-agent name: ArgumentCritic
   Purpose: Critique the logical structure, argument coherence, and evidence quality of academic drafts in a rigorous, unsparing manner. Focus only on argumentation — ignore methodology, citations, and writing style.

2. Sub-agent name: MethodologyCritic  
   Purpose: Critique the research methodology of academic drafts. Focus only on methodological soundness, research design, sampling, validity, and limitations — ignore the argument structure and writing style.
```

Add more as needed, e.g.:
- `CitationAuditor` — checks all references for accuracy, completeness, format
- `WritingEditor` — copyediting and clarity only
- `EvidenceChecker` — evaluates whether claims are supported by the cited evidence

### Running the agents in parallel

```
Run ArgumentCritic and MethodologyCritic in parallel on drafts/chapter3.docx. 
Give me each critique as a separate section.
```

### Why not just ask one agent to do both?

Because the second critique inherits the context of the first. If argument critique comes first, methodology critique is already shaped by it — and vice versa. Parallel sub-agents give you genuinely independent assessments.

---

## Use Case 2: Dual Independent Screeners for Systematic Reviews

Standard systematic review protocol requires two independent reviewers to screen abstracts, with discrepancies resolved by a third. Sub-agents can replicate this workflow.

### Setup prompt

```
Create two sub-agent reviewers for screening abstracts in my systematic review:

1. Sub-agent name: Reviewer1_Strict
   Purpose: Screen abstracts against inclusion/exclusion criteria. Apply strict interpretation — when in doubt, exclude. For each abstract, output: INCLUDE / EXCLUDE / UNCERTAIN + one-sentence rationale.
   
   Inclusion criteria: [paste your criteria]
   Exclusion criteria: [paste your criteria]

2. Sub-agent name: Reviewer2_Broad
   Purpose: Screen the same abstracts. Apply a more liberal interpretation — when in doubt, include for full-text review. For each abstract, output: INCLUDE / EXCLUDE / UNCERTAIN + one-sentence rationale.
   
   Use the same inclusion/exclusion criteria as Reviewer1_Strict.
```

### Running the screening

```
Run Reviewer1_Strict and Reviewer2_Broad in parallel on this file: literature/abstracts-batch1.txt
Output results as a table: Study | Reviewer1 | Reviewer2 | Agreement (Y/N)
```

### Handling discrepancies

```
For all studies where Reviewer1 and Reviewer2 disagree, give me your own assessment as tiebreaker and flag any that need human judgment.
```

---

## Practical Notes

- Sub-agents are created as `.md` files in your project's `.claude/` folder — Claude Code handles the file creation automatically
- Once created, sub-agents persist across sessions in that project
- Each sub-agent has its own context window — they do not see each other's outputs unless you explicitly show them
- Start with a small test batch (10 abstracts, 2 pages of draft) before running on full documents
- Sub-agents consume more tokens than a single sequential review — useful for critical review stages, not for every minor edit

---

*Part of the academic-research-suite skill. Complements the built-in academic-paper-reviewer for high-stakes independent assessment.*
