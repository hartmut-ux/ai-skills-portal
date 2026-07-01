# Scholar Evaluator Sub-Agent

Build a sub-agent that embodies the critical perspective of a specific scholar or theoretical framework — then use it to get targeted feedback on your work.

**Why this is powerful**: Generic peer review asks "is this good research?" A scholar evaluator asks "does this adequately engage with Venuti's theory of domestication?" or "would a Foucauldian analysis accept this framing?" These are the questions that matter most for field-specific work.

---

## Concept

You gather the scholar's canonical texts (papers, book chapters, key passages) → put them in a folder → ask Claude to build a sub-agent that reasons from within that framework → use the sub-agent to critique your drafts.

The result: critique that is calibrated to a specific intellectual tradition rather than generic methodology.

---

## Setup (step by step)

### Step 1: Gather the source texts

Create a subfolder in your project:
```
[project]/
  theory-sources/
    venuti-translators-invisibility-ch1.pdf
    venuti-translation-changes-everything.pdf
    venuti-1998-scandals-translation.pdf
```

Tip: 3–5 key texts are sufficient. More is not always better — focus on the texts that define the framework you're working within.

### Step 2: Create the sub-agent

```
I want to create a sub-agent called [ScholarName]Evaluator. 
Its purpose is to evaluate my academic drafts from the perspective of [Scholar Name]'s theoretical framework. 

Base it on these documents in theory-sources/:
- [list the files]

The sub-agent should:
- Assess how rigorously I have engaged with [Scholar's] key concepts
- Identify missed opportunities to apply the theory
- Flag where my argument contradicts or oversimplifies the framework
- Suggest specific passages from the source texts I should engage with more deeply

Name the sub-agent: [ScholarName]Evaluator
```

### Step 3: Use the sub-agent

```
Run VenutiEvaluator on drafts/chapter2.docx
```

or, in parallel with a general critic:

```
Run VenutiEvaluator and ArgumentCritic in parallel on drafts/chapter2.docx
```

---

## Example Evaluators for Different Fields

| Field | Evaluator idea | Source texts |
|-------|---------------|--------------|
| Translation Studies | VenutiEvaluator | Venuti's canonical chapters |
| Postcolonial Studies | BhabhaEvaluator | Homi Bhabha's key essays |
| Sociology | BourdieuEvaluator | Bourdieu on field, capital, habitus |
| Critical Theory | FoucaultEvaluator | Foucault on discourse and power |
| Nursing/Medicine | EBPEvaluator | Evidence-based practice standards |
| Systematic Review | PRISMAEvaluator | PRISMA 2020 checklist + explanation |

---

## Using Your Own Writing as a Style Evaluator

A variation: build an evaluator that critiques drafts against your own *best* writing.

```
Create a sub-agent called MyStyleEvaluator. 
Base it on the samples in mywritingstyle.md.
Its purpose is to identify passages in my new drafts that drift from my established voice and suggest rewrites that match my style.
```

---

## Important Caveats

- The sub-agent reasons from the texts you provide, not from a live or authoritative understanding of the scholar's full body of work
- Treat output as a structured prompt for your own thinking, not as a definitive scholarly judgment
- For humanities work especially: always verify the sub-agent's claims against the source texts yourself

---

*Part of the academic-research-suite skill. Works best in combination with parallel-review-guide.md.*
