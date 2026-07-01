---
name: branded-visual-factory
description: "Generates on-brand HTML/CSS infographics, cheat sheets, data cards, and carousel slides as code — fully editable, pixel-perfect, PNG-exportable. Supports multiple brands (MMIND.ai, FlowMomentum.ai). Use whenever the user wants to create a branded infographic, cheat sheet, visual content card, social media graphic, data visualization, carousel, or any visual content piece that should follow brand guidelines. Also triggers on: 'erstelle eine Infografik', 'Cheat Sheet', 'Visual erstellen', 'branded graphic', 'LinkedIn Visual', 'Daten-Karte', 'Social Media Grafik', 'Infographic', 'visuellen Content erstellen', or when content-engine requests a visual deliverable. Do NOT use for generative art or p5.js sketches (use programmatic-infographics instead) or for AI image generation prompts (use brand-guardian instead)."
---

# Branded Visual Factory

Generates production-ready, on-brand visuals as HTML/CSS code. Every output is a self-contained HTML file that renders at exact social media dimensions, follows strict brand rules, and exports to PNG.

This is NOT an AI image generator. This is code-based design — every pixel is editable, every color is a hex value, every element is a CSS rule.

## How This Skill Works

1. Identify which brand the visual is for
2. Load the brand config from `brands/`
3. Select the right template from `templates/`
4. Generate the HTML/CSS with brand-specific values
5. Run QA validation
6. Export to PNG if requested

## Step 1: Identify the Brand

Determine the brand from context or ask explicitly.

| Signal | Brand | Config File |
|--------|-------|-------------|
| MMIND.ai, AI-Beratung, KMU, Flow Factor, Hartmut LinkedIn | MMIND.ai | `brands/mmind.md` |
| FlowMomentum, Cycling, Leadership Performance, Garmin, Corporate Wellness | FlowMomentum.ai | `brands/flowmomentum.md` |
| Unclear or new brand | Ask the user | — |

Read the relevant brand config file before generating any visual.

## Step 2: Select the Visual Type

| User Request | Template | Dimensions |
|-------------|----------|------------|
| "Infographic", "Prozess zeigen", "Ablauf darstellen" | `templates/infographic.html` | 1080 x 1350 (4:5) |
| "Cheat Sheet", "Zusammenfassung", "Spickzettel" | `templates/cheat-sheet.html` | 1080 x 1350 (4:5) |
| "Data Card", "Zahl hervorheben", "Statistik" | `templates/data-card.html` | 1080 x 1350 (4:5) |
| "Carousel Slide" | `templates/carousel-slide.html` | 1080 x 1350 (4:5) |
| "Newsletter Header" | `templates/newsletter-header.html` | 1280 x 720 (16:9) |

Read the template file to understand its structure before generating.

## Step 3: Generate the Visual

Use the template as structural foundation. Replace ALL placeholder values with brand-specific values from the loaded config:

1. **Colors**: Use ONLY the colors defined in the brand config. No additional colors.
2. **Typography**: Use the exact font families and weights from the brand config. Embed fonts via base64 @font-face or use Google Fonts/CDN fallbacks.
3. **Spacing**: Follow the spacing scale from the brand config.
4. **Logo**: Include the brand logo in the position specified by the config.
5. **Content**: Fill in the actual content from the user's request.

### Critical HTML/CSS Rules

- **Dimensions**: Set the root container to exact pixel dimensions (e.g., `width: 1080px; height: 1350px`)
- **No viewport units**: Use px only — this must render identically at any zoom level
- **Inline everything**: All CSS inline in a `<style>` tag. No external stylesheets except font CDNs.
- **Self-contained**: The HTML file must work when opened directly in a browser
- **No JavaScript required**: Pure HTML/CSS for the visual. JS only for optional interactivity.
- **Print-quality text**: All text must be crisp, properly anti-aliased, correctly sized
- **Overflow hidden**: Nothing should bleed outside the canvas dimensions

### Font Embedding Strategy

For each brand, use this fallback chain:
1. **First choice**: Google Fonts CDN link (if the font is on Google Fonts)
2. **Second choice**: Base64-encoded @font-face from `assets/fonts/`
3. **Fallback**: System font stack specified in brand config

For FlowMomentum.ai (Satoshi font): Satoshi is NOT on Google Fonts. Use the woff2 files from `assets/fonts/` via base64 @font-face, or reference the CDN at `https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,900&display=swap`.

For MMIND.ai (Inter): Available on Google Fonts. Use `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap`.

## Step 4: QA Validation

Before presenting any visual, run these checks mentally (or via `scripts/qa-check.py` if available):

### Color Check
- [ ] Only brand-palette colors used (check every hex value in the CSS)
- [ ] Background color matches brand spec
- [ ] Text contrast ratio meets WCAG AA (4.5:1 for body text)

### Typography Check
- [ ] Correct font family loaded and applied
- [ ] Font weights match brand spec (headlines bold, body regular)
- [ ] Font sizes within brand spec ranges
- [ ] Line heights appropriate (1.3-1.5 for body, 1.1-1.2 for headlines)

### Layout Check
- [ ] Canvas dimensions exact (1080x1350 or 1280x720)
- [ ] No content overflow or clipping
- [ ] Spacing consistent with brand grid
- [ ] Visual hierarchy clear (headline > subheadline > body > footer)
- [ ] Logo present, correct size, correct position

### Content Check
- [ ] All text proofread (Swiss spelling: ss not ß)
- [ ] Source attribution present where needed
- [ ] No lorem ipsum or placeholder text remaining
- [ ] Content is scannable — max 7 items in any list, max 40 words per section

### Brand-Specific Check
- [ ] MMIND.ai: Flat vector style, no gradients, no shadows, no 3D
- [ ] FlowMomentum.ai: Gradient usage matches warm/cool specs, modern aesthetic

If any check fails, fix it before presenting the output.

## Step 5: Export to PNG

When the user wants a PNG file, use Playwright or Puppeteer to screenshot the HTML:

```bash
# Install if needed
pip install playwright --break-system-packages
playwright install chromium

# Export
python scripts/export-png.py <input.html> <output.png>
```

Alternative: The user can open the HTML in Chrome and use DevTools → Capture screenshot at the correct dimensions.

## Integration with Other Skills

### With content-engine
When content-engine produces a content package (LinkedIn post, newsletter, etc.), it can request a visual from this skill. The content-engine provides: topic, key data points, visual type. This skill returns: HTML file + optional PNG.

### With brand-guardian
Brand Guardian defines the rules. This skill executes them in code. If brand-guardian updates its color palette or typography, update the corresponding brand config file here.

### With programmatic-infographics
Different use cases. `programmatic-infographics` creates generative art with p5.js. This skill creates structured content visuals with HTML/CSS. They don't overlap.

## Reference Files

| File | Purpose |
|------|---------|
| `brands/mmind.md` | Complete MMIND.ai brand configuration |
| `brands/flowmomentum.md` | Complete FlowMomentum.ai brand configuration |
| `references/design-guidelines.md` | Universal spacing, grid, and composition rules |
| `templates/*.html` | Starting-point templates for each visual type |
| `scripts/qa-check.py` | Automated QA validation script |
| `assets/fonts/` | Satoshi font files (woff2) for FlowMomentum.ai |
| `assets/logos/` | Brand logos (SVG/PNG) |
