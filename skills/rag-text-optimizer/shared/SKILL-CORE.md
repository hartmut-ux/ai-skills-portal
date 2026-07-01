---
name: rag-text-optimizer
description: >
  Full RAG document optimization pipeline. Re-extracts PDFs via Docling/PyMuPDF4LLM with correct tables and layout, fixes multi-column text, cleans OCR artifacts and web scraping garbage, formats as structured Markdown for semantic chunking. Includes Anthropic contextual retrieval and parent-child chunking. Use when user mentions RAG, Dify, knowledge base, vectorization, document cleaning for AI, broken tables, garbled text, chunking, or embedding quality. Triggers on: "prepare for Dify", "fix formatting", "optimize for RAG", "tables are broken", "text is fragmented".
---

# RAG Text Optimizer

Transforms messy, poorly extracted documents into clean, structured Markdown optimized for RAG vectorization and semantic search. Based on peer-reviewed benchmarks from NAACL 2025 (Vectara), Anthropic's contextual retrieval research, Jina AI's late chunking, and 2025/2026 production guides from Chroma, Pinecone, and NVIDIA.

## Why This Matters

RAG systems retrieve document chunks and feed them to LLMs. If those chunks contain navigation menus, broken tables, fragmented multi-column text, or OCR garbage, the LLM retrieves noise instead of signal. Reformatting documents (PDF → clean Markdown + parent-child chunking) routinely yields 20–40% accuracy gains in 2025–2026 benchmarks.

## Target Format: Why Markdown

Markdown is the practical winner for RAG ingestion (Chroma, Pinecone, NVIDIA 2025–2026 benchmarks). It improves retrieval accuracy by up to 35% over raw text while cutting token costs by 20–40%. It mirrors LLM training data (GitHub/docs), provides semantic structure (headings, lists, tables) with minimal overhead, and is natively supported by all major vector DBs.

Note: HtmlRAG (arXiv 2024) showed cleaned HTML can outperform Markdown on web-native QA benchmarks (+3–15% Hit@1). However, for mixed corpora (PDFs, books, research papers, web scrapes) Markdown is more robust and practical.

## The Three-Path Architecture

Every document falls into one of three processing paths, ordered by quality:

### Path A: Docling (best for complex PDFs with tables/multi-column)

IBM's open-source Docling achieves 97.9% table cell accuracy and excellent multi-column/layout preservation — significantly better than PyMuPDF4LLM on complex documents. Use for PDFs with important tables, multi-column layouts, or complex figures.

```bash
pip install docling
```

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("input.pdf")
md_text = result.document.export_to_markdown()
```

Docling advantage: AI-powered layout analysis (DocLayNet) + table structure recognition (TableFormer). Slower than PyMuPDF4LLM but dramatically better on complex layouts.

**Known limitations:** Multi-column text flow has known issues (GitHub #2067, #1203). Docling correctly detects columns but sometimes orders the text incorrectly. For two-column books, apply Docling and manually verify text flow — it's still the best automated option.

**Books:** For large PDFs (>100 pages), process in chapter-sized batches to avoid memory issues. Use `converter.convert()` with page ranges if needed.

**Multi-column workaround:** For two-column layouts:
1. Extract with Docling (best baseline)
2. Review output for text flow errors
3. If still broken: extract page-by-page, use an LLM to reconstruct correct reading order
4. Alternative: LlamaParse (commercial, ~6s/doc) often handles multi-column better

### Path B: PyMuPDF4LLM (fast extraction for clean PDFs)

When speed matters or the PDF has simple layout (single-column, basic tables), PyMuPDF4LLM is the fastest local option with good table preservation.

```python
import pymupdf4llm
md_text = pymupdf4llm.to_markdown("input.pdf")
# For large books (>100 pages), extract in batches
md_text = pymupdf4llm.to_markdown("input.pdf", pages=range(0, 50))
```

**Limitation:** Does not handle two-column layouts. Use Path A for any multi-column document.

### Path C: Text Cleanup (for web scrapes and files without PDFs)

When no original PDF exists, clean the existing text in order:

1. **Remove web scraping artifacts** (navigation, menus, footers, cookie notices, login prompts, sidebars)
2. **Clean HTML entities** (`&#xA0;` → space, `&#x2013;` → –, `&#x2019;` → ', `&lt;` → <, `&gt;` → >, `&amp;` → &)
3. **Fix multi-column fragmentation** — detect alternating short/long lines, reconstruct into flowing paragraphs
4. **Reconstruct broken tables** — detect misaligned pipe characters, rebuild table structure
5. **Reconstruct OCR tables** — see dedicated section below — critical
6. **Remove page-break artifacts** — strip repeated page headers/footers, page numbers, document IDs (`Fassung: 17.09.2016`, `701.01`) that appear mid-content
7. **Apply formatting standards** (see below)

### Path D: Image and Infographic Extraction

For documents containing critical infographics, diagrams, or data visualizations:

**Option 1 — Dify v1.11 Multimodal KB (recommended):**
- Dify v1.11+ supports image vectorization alongside text
- Requires multimodal embedding model with VISION badge (Jina CLIP, Google Vertex AI multimodal)
- Images embedded as Markdown links (`![Description](image.png)`) are vectorized with the text
- JPG/PNG/GIF ≤2MB, enables cross-modal retrieval (text query → image result)

**Option 2 — VLM Image Description (works with any embedding model):**
- Extract images from PDF using PyMuPDF
- Send each to a Vision LLM with prompt: "Describe this infographic in detail, including all data points, labels, relationships"
- Insert the text description into the Markdown where the image was located
- Often produces better search results than multimodal embeddings — description is semantically richer

```python
import fitz  # PyMuPDF
doc = fitz.open("input.pdf")
for page_num, page in enumerate(doc):
    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        # Save or send to VLM for description
```

## First-Principles Content Reduction

Not every document should be vectorized in full. Apply BEDROCK/SCAFFOLDING/DECORATION classification:

| Document Type | Strategy | Rationale |
|---|---|---|
| Laws, regulations, standards | **Full text** — keep everything | Must be quotable verbatim |
| Research papers | **Condense** — Abstract + Key Findings + Practical Implications | Methodology details rarely relevant for retrieval |
| Books / frameworks | **Heavily condense** — Core concepts + actionable insights | ~80% is scaffolding |
| Training data (tables, zones, plans) | **Full text** — keep everything | Every number is load-bearing |
| Web articles / blog posts | **Condense** — Key insights only | Strip intro fluff, CTAs, author bios |

Add a metadata tag to track reduction level: `**Reduction:** full | condensed | heavily-condensed`

**Important:** When condensing, always preserve specific statistics, data tables, named frameworks, and direct quotes. Never paraphrase numbers or alter data.

## Optimal Chunk Size: The Research

The Vectara NAACL 2025 peer-reviewed study (Qu et al., "Is Semantic Chunking Worth the Computational Cost?") found that **fixed-size chunking consistently outperforms semantic chunking** across document retrieval, evidence retrieval, and answer generation. The computational overhead of semantic chunking is not justified.

Empirically optimal parameters (consensus across Pinecone, Weaviate, Chroma, NVIDIA 2025–2026):
- **Chunk size:** 400–512 tokens (~150–350 words, ~800–1200 characters)
- **Overlap:** 10–20% (50–100 tokens) — diminishing returns above 20–30%
- **Split strategy:** Structure-based at heading boundaries (## / ###), then recursive within sections

Factoid queries favor smaller chunks (256–512 tokens), analytical queries benefit from larger ones (512–1024). The 512-token default achieved 69% end-to-end accuracy in the 2026 Firecrawl benchmark.

## Contextual Retrieval (Anthropic Technique)

Anthropic's September 2024 research showed that prepending a short LLM-generated context summary to each chunk before embedding reduces top-20 retrieval failures by:
- 35% (embeddings alone)
- 49% (with contextual BM25)
- 67% (with reranking)

Implementation: After chunking, use an LLM to generate a 1–2 sentence prefix for each chunk explaining how it fits the overall document. Prepend this to the chunk before embedding.

```
Example chunk prefix:
"This section from 'Interval Training for Cycling' by Rønnestad et al. describes
the power output differences between CAT.1 and CAT.2 professional cyclists
after varying levels of energy expenditure."
```

This is the single highest-impact optimization after getting the base formatting right.

## Formatting Standards for RAG-Optimized Markdown

### File Header (always present)

```markdown
# [Descriptive Title]

**Source:** [URL or filename]
**Authors:** [Names only, no affiliations/addresses/emails]
**Topic:** [Primary knowledge domain]
**Relevance:** [Why this matters for the platform's use case]
**Reduction:** [full | condensed | heavily-condensed]

---
```

### Content Body

Use ## for major sections and ### for subsections. Each ## section should be a **self-contained knowledge unit** — most important formatting principle. Target 150–350 words per ## section (~400–512 tokens).

Research papers:
```markdown
## Abstract
[Clean abstract text]

## Key Findings
[Most important results with specific numbers/statistics]

## Methodology Summary
[Brief methods — only what's needed to understand findings]

## Practical Implications
[What this means for practitioners/coaches/leaders]
```

Books / long-form:
```markdown
## [Chapter/Section Title]
### [Key Concept 1]
[Explanation with actionable takeaways]
```

### Table Formatting

Tables are critical for training data (zones, plans). 2025 benchmark: **Markdown-KV format** = highest LLM accuracy (60.7%) vs JSON (52.3%), HTML (53.6%), CSV (44.3%). GitHub-compatible pipe tables are the practical standard.

```markdown
| Zone | % FTP    | HR Range   | Duration   |
|------|----------|------------|------------|
| Z1   | < 55%    | < 68% max  | 30-90 min  |
| Z2   | 56-75%   | 69-83% max | 60-300 min |
```

Rules:
- Every row same number of pipe characters
- Header separator row uses `|---|`
- One blank line before/after every table
- No `<br>` tags inside cells — split into separate rows
- > 8 columns → split tables or Markdown-KV
- Tables intact within a single chunk — never split across chunk boundaries

### OCR Table Reconstruction (CRITICAL)

PDF extractors often render tables from scanned/image-based PDFs as OCR text blocks (`picture text` blocks or `<br>`-separated lines). These look like flowing text but contain tabular data with implicit column structure. **The single most common source of RAG retrieval errors.**

**Detection:** Look for:
- `**----- Start of picture text -----**` / `**----- End of picture text -----**` blocks with aligned values
- Multiple `<br>` tags separating what should be table rows
- Values separated only by whitespace with implicit column alignment
- Table content split across consecutive OCR blocks or page breaks
- Column headers only in the first block, separated from data rows in later blocks

**Reconstruction rules:**
1. Identify all columns from the header row.
2. Merge all OCR blocks belonging to the same table. Remove injected page artifacts.
3. Reconstruct each row with explicit pipe-separated columns.
4. Rejoin wrapped cell text.
5. Preserve all column values independently — never merge identical-looking columns.
6. Add a context line before the table explaining columns.
7. Move explanatory notes after the table as "Zusatzregeln" or "Anmerkungen".

**Before (broken OCR):**
```
**----- Start of picture text -----**
Einstellplätze Freistellplätze
1. Wohnbauten
1.1 Einfamilienhäuser 1 je Wohneinheit 1 je Wohneinheit
**----- End of picture text -----**
```

**After (clean Markdown):**
```markdown
Die folgende Tabelle gibt die Mindestanzahl an Einstell- und Freistellplätzen je Nutzungsart an. Beide Spalten sind separat zu lesen.

| Nr. | Nutzung | Einstellplätze | Freistellplätze |
|-----|---------|---------------|----------------|
| 1.1 | Einfamilienhäuser | 1 je Wohneinheit | 1 je Wohneinheit |
| 3 | Dienstleistungsbetriebe | 1 je 60 m² BGF | 1 je 60 m² BGF |
```

**Verification:** Count pipe characters per row — must be identical. Read each column top-to-bottom against the original PDF.

### Image References

```markdown
### [Diagram Title]
![Description of what the image shows](filename.png)

**Image Summary:** [Detailed text description: data points, labels, relationships, key takeaways. This is what gets vectorized.]
```

The `**Image Summary:**` block is essential — ensures image content is searchable even without multimodal embedding.

### What to Remove (DECORATION — never load-bearing)

- Navigation menus, breadcrumbs, sidebars
- "Skip to Main Content", "Login", "Register", cookie notices
- Journal article count lists ("JMIR mHealth 3028 articles")
- Author institutional addresses, phone numbers, emails
- Full reference/bibliography sections (keep in-text citations)
- "Article Processing Fees", "Browse Journal", "Submit Article"
- Newsletter signup forms, social media buttons
- "Related Articles", "You May Also Like"
- Country/region dropdowns
- Excessive whitespace (max 1 blank line between sections)
- Copyright/license boilerplate
- PDF page headers/footers
- OCR garbage from cover images
- `**==> picture ... intentionally omitted <==**` markers — remove. But always check the accompanying `picture text` block for tabular data.

### What to Keep (BEDROCK — always load-bearing)

- All substantive content (findings, methods, conclusions, frameworks)
- Author names (without contact details)
- Specific statistics, numbers, percentages
- Tables with data
- Key quotes and definitions
- Actionable recommendations
- Source URLs and DOIs

### What to Condense (SCAFFOLDING — useful but compressible)

- Verbose methodology → brief summary
- Long literature review → key citations only
- Repetitive examples → representative examples
- Full book chapters → key frameworks + actionable insights

## Tools / Scripts

This skill ships with two scripts in `scripts/`:

### 1. PDF Processor (`scripts/pdf_processor.py`) — All-in-One PDF → Markdown

Converts any PDF to clean, Dify-ready Markdown. Handles text, tables, and images in one pipeline.

**Usage:**
```bash
# Basic
python scripts/pdf_processor.py "document.pdf"

# Specific output folder
python scripts/pdf_processor.py "document.pdf" --output "output_folder/"

# Batch
python scripts/pdf_processor.py --batch "folder_with_pdfs/" --output "output_folder/"

# Force Docling for complex PDFs
python scripts/pdf_processor.py "complex.pdf" --force-path A

# Image descriptions via the assistant Vision
python scripts/pdf_processor.py "document.pdf" --anthropic-key "sk-ant-..."

# Content reduction (condenses research papers, books)
python scripts/pdf_processor.py "paper.pdf" --anthropic-key "sk-ant-..." --reduce --doc-type research
```

**Document types for `--doc-type`:**

| Type | Behavior |
|---|---|
| research | Keeps Abstract, Key Findings, Practical Implications. Condenses methods. |
| book | Condenses to ~30%. Keeps frameworks, data, tables. |
| standard | Keeps EVERYTHING. Only cleans formatting. |
| training | Keeps all zones, tables, protocols. Removes filler. |
| web | Strips intro fluff, CTAs, author bios, newsletter signups. |

**What the tool does (5 steps):**
1. Analyzes the PDF: page count, multi-column detection, table detection, image count
2. Extracts text: PyMuPDF4LLM (fast) or Docling (AI-powered)
3. Extracts images: significant images as PNG/JPEG, optionally describes via the assistant Vision
4. Cleans: HTML entities, OCR garbage, scraping artifacts, table formatting
5. Structures: adds metadata header, inserts image descriptions, applies content reduction

**Requirements:**
- Python 3.10+
- `pip install pymupdf4llm`
- Optional: `pip install docling` (~2GB)
- Optional: Anthropic API key (image descriptions + reduction)

### 2. KB Batch Cleaner (`scripts/process_kb.py`)

For cleaning already-extracted .md files in a knowledge base.

```bash
# Single file
python scripts/process_kb.py --file "file.md" --pdf-dir "pdfs/"

# Entire KB folder
python scripts/process_kb.py --kb-dir "kb/" --pdf-dir "pdfs/"
```

## Quality Validation Checklist

Every file should pass:
- [ ] Starts with `# Title` and metadata block (including Reduction tag)
- [ ] No HTML entities remain
- [ ] No navigation/menu artifacts
- [ ] Tables have consistent pipe counts per row
- [ ] No multi-column text fragmentation
- [ ] Each ## section is 150–350 words
- [ ] No empty sections
- [ ] Source attribution present
- [ ] No OCR garbage
- [ ] Signal-to-noise ratio: boilerplate < 5%
- [ ] Images described in text (Image Summary blocks)

For comprehensive validation use RAGAS or Vectara's HHEM-2.1. Target > 85% recall + coherence.

## Dify-Specific Configuration

Recommended settings (Dify 0.15+):
- **Chunk mode:** Parent-Child (strongly recommended)
- **Child chunk strategy:** Paragraph mode (splits on `\n\n`)
- **Max chunk size:** 800–1200 characters (~400–512 tokens)
- **Chunk overlap:** 10–20% (80–200 characters)
- **Cleaning:** Enable "remove extra spaces and blank lines"
- **Index mode:** High Quality (embedding-based)
- **Embedding model:** text-embedding-3-large (text-only). For multimodal: model with VISION badge.
- **Retrieval mode:** Hybrid (keyword + semantic)
- **Rerank model:** jina-reranker-v3 or similar
- **Top K:** 5 (8-10 for broad analytical queries)
- **Score threshold:** 0.5 (0.3 exploratory, 0.7 factual)
- **Plugin:** Advanced Markdown Chunker — https://github.com/asukhodko/dify-markdown-chunker

For FAQ-style KBs use Q&A mode. For research/books/frameworks use standard mode.

## Image Pipeline for Vision-Enabled Dify KBs

Dify KB upload only accepts text files. For documents with data-relevant images:

### Step 1: Extract images during PDF processing
`pdf_processor.py` extracts significant images (>15 KB) into an `images/` subfolder.

### Step 2: Host images on public storage
Images need public HTTPS URLs.

**Option A — Google Cloud Storage:**
```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/path/to/service-account.json
gsutil -m cp "output/images/*.jpeg" gs://YOUR-BUCKET/
```
Public URL: `https://storage.googleapis.com/YOUR-BUCKET/img_pXX_Y.jpeg`

**Org Policy notes:** Workspace orgs often block `iam.disableServiceAccountKeyCreation` and `iam.allowedPolicyMemberDomains` — override at org level.

**Option B — GitHub Public Repo:**
```bash
cd output/images/
git init && git add *.jpeg && git commit -m "KB images"
gh repo create kb-assets --public --push
```
URL: `https://raw.githubusercontent.com/USERNAME/kb-assets/main/img_pXX_Y.jpeg`

**Option C:** Any static hosting (Hostinger, Cloudflare R2, Netlify).

### Step 3: Update Markdown with public URLs
```python
import re
with open('document_dify.md', 'r') as f:
    content = f.read()
GCS_BASE = 'https://storage.googleapis.com/YOUR-BUCKET'
content = re.sub(r'images/(img_p\d+_\d+\.\w+)', GCS_BASE + '/\\1', content)
with open('document_dify.md', 'w') as f:
    f.write(content)
```

### Step 4: Embedding model selection

| KB Content | Model | Reason |
|---|---|---|
| Text only | `text-embedding-3-large` or `text-embedding-005` (Vertex AI) | Best text retrieval |
| Text + data images | `multimodalembedding@001` (Vertex AI) or `jina-clip-v2` | Unified text+image space |
| Multilingual | `text-multilingual-embedding-002` (Vertex AI) | Non-English optimized |

**Critical:** KB embedding model is fixed after creation. Choose before uploading.

### Step 5: Automated GCS Upload from Cowork (no terminal)
For users with service account JSON in the workspace folder, the assistant can upload images directly during PDF processing.

**One-time setup:**
1. Place service account JSON in `the assistant Cowork/`
2. Grant the SA `Storage Object Admin` on the bucket
3. Grant `allUsers` `Storage Object Viewer` (public read)

**Standard output folder:** All finished `_dify.md` files save to `the assistant Cowork/Dify uploads/` automatically.

```python
from google.cloud import storage
import os, glob

workspace = "<your-cowork-mount>"
dify_output = os.path.join(workspace, "Dify uploads")
os.makedirs(dify_output, exist_ok=True)

key_files = glob.glob(os.path.join(workspace, "*.json"))
key_path = key_files[0]

images = sorted(glob.glob(os.path.join(workspace, f"{doc_name}_images/*.jpeg")))
if images:
    client = storage.Client.from_service_account_json(key_path)
    bucket = client.bucket("dify-kb-assets")
    for img_path in images:
        filename = os.path.basename(img_path)
        blob = bucket.blob(filename)
        blob.upload_from_filename(img_path, content_type="image/jpeg")

GCS_BASE = "https://storage.googleapis.com/dify-kb-assets"
src_path = os.path.join(workspace, f"{doc_name}_dify.md")
dst_path = os.path.join(dify_output, f"{doc_name}_dify.md")
with open(src_path, "r") as f:
    content = f.read()
if images:
    content = re.sub(r'[a-zA-Z0-9_]+_images/(img_p\d+_\d+\.\w+)', GCS_BASE + '/\\1', content)
with open(dst_path, "w") as f:
    f.write(content)
```

### Step 6: Verify before uploading
```bash
curl -s -o /dev/null -w "%{http_code}" "https://storage.googleapis.com/YOUR-BUCKET/img_p1_0.jpeg"
# 200 = public, 403 = public access not set, 404 = not uploaded yet
```

## Key Sources

- Qu et al. NAACL 2025 — Fixed vs semantic chunking: https://arxiv.org/abs/2410.13070
- HtmlRAG (arXiv 2024) — HTML vs Markdown for RAG: https://arxiv.org/abs/2411.02959
- Jina AI Late Chunking (2024): https://arxiv.org/abs/2409.04701
- Anthropic Contextual Retrieval (Sep 2024): https://www.anthropic.com/news/contextual-retrieval
- Docling PDF benchmark (Mar 2025) — 97.9% table accuracy: https://procycons.com/en/blogs/pdf-data-extraction-benchmark/
- Dify chunk configuration: https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text
- Advanced Markdown Chunker for Dify: https://github.com/asukhodko/dify-markdown-chunker
- Firecrawl 2026 Chunking Benchmark: https://www.firecrawl.dev/blog/best-chunking-strategies-rag
- PyMuPDF4LLM: https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/
