# Brand Config: FlowMomentum.ai

## Identity
- **Brand**: FlowMomentum.ai
- **Tagline**: Leadership Performance Platform
- **Website**: https://flowmomentum.ai
- **Logo**: "flow momentum®" wordmark + connected wave symbol
- **Logo position**: Bottom-right or bottom-center, small
- **Logo colors**: White on dark backgrounds, #0A0A0A on light backgrounds
- **Source line format**: "flowmomentum.ai"

## Color Palette (6 colors + black/white)

| Role | Name | Hex | CSS Variable |
|------|------|-----|-------------|
| Neutral | Light Gray | #D9D9D9 | --color-neutral |
| Accent 1 | Lilac | #96A7FF | --color-lilac |
| Accent 2 | Sand | #F3E4C7 | --color-sand |
| Accent 3 | Peach | #F5B9A0 | --color-peach |
| Accent 4 | Electric Blue | #0066FF | --color-blue |
| Accent 5 | Mint | #99FFBB | --color-mint |
| Text Dark | Near-Black | #0A0A0A | --color-text |
| Background | White | #FFFFFF | --color-bg |

### Color Usage Rules
- Headlines: #0A0A0A or white (on dark/gradient backgrounds)
- Body text: #0A0A0A
- Primary accent elements: #96A7FF (Lilac) or #0066FF (Electric Blue)
- Secondary fills: #F3E4C7 (Sand), #F5B9A0 (Peach)
- Highlight/success: #99FFBB (Mint)
- Card backgrounds: #F3E4C7, #F5B9A0, or #D9D9D9

### Gradient System (UNIQUE to FlowMomentum)

Unlike MMIND.ai, this brand USES gradients as a core design element.

**Warm Gradient** — for wellness, coaching, personal topics:
```css
background: linear-gradient(135deg, #F3E4C7 0%, #F5B9A0 40%, #D9D9D9 70%, #96A7FF 100%);
```

**Cool Gradient** — for tech, performance, data topics:
```css
background: linear-gradient(135deg, #0066FF 0%, #96A7FF 30%, #F3E4C7 70%, #F3E4C7 100%);
```

**Usage**: Gradients are used for full-page backgrounds or hero sections. Text on gradients must be #0A0A0A or white with sufficient contrast. Cards on gradient backgrounds use white (#FFFFFF) with slight opacity or solid white.

## Typography

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Headline | Satoshi | 700 (Bold) | 48-56px | #0A0A0A |
| Subheadline | Satoshi | 500 (Medium) | 24-28px | #0A0A0A |
| Body Text | Satoshi | 400 (Regular) | 18-22px | #0A0A0A |
| Stats/Callouts | Satoshi | 900 (Black) | 36-48px | #0066FF or #96A7FF |
| Labels/Small | Satoshi | 300 (Light) | 12-14px | #0A0A0A |
| Source Line | Satoshi | 300 (Light) | 12px | #0A0A0A |

### Font Loading

**Option 1 — Fontshare CDN (preferred):**
```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap" rel="stylesheet">
```

**Option 2 — Local woff2 (base64 embedded):**
Font files in `assets/fonts/Satoshi-*.woff2`

Fallback stack: `'Satoshi', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`

## Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| --space-xs | 8px | Inline gaps, icon padding |
| --space-sm | 16px | Between related elements |
| --space-md | 24px | Between sections |
| --space-lg | 40px | Major section breaks |
| --space-xl | 64px | Top/bottom page margins |

## Cards & Boxes

- Background: #FFFFFF (on gradient bg) or #F3E4C7 / #D9D9D9 (on white bg)
- Border: none (soft edges) or 1px solid #D9D9D9
- Border-radius: 16-20px
- Padding: 24-32px
- Box-shadow: `0 2px 12px rgba(0,0,0,0.06)` — subtle allowed (unlike MMIND.ai)
- Backdrop-filter: none (no glassmorphism)

## Visual Style: Modern Gradient SaaS

This brand uses a premium, modern aesthetic with gradients as signature element. Think: Calm, Headspace, Whoop meets Linear.

### Allowed
- Soft gradients (warm and cool palettes)
- Subtle shadows (very light, max 6% opacity)
- Rounded shapes and corners (16-20px)
- Clean geometric elements
- Bold typography as design element
- Color blocking with palette colors
- Organic flowing shapes (echoing the wave logo)

### FORBIDDEN
- 3D effects or perspective
- Glassmorphism or heavy blur
- Photorealistic elements
- Neon or saturated colors outside palette
- Handwritten or decorative fonts
- More than 3 gradient colors in a single gradient
- Heavy drop shadows

## Visual Types and Layouts

### Data Card
- Large stat number in #0066FF or #96A7FF
- Warm gradient background
- White card overlay with stat

### Infographic
- Process flow with numbered steps
- Cool gradient header section
- White body with color-coded sections

### Cheat Sheet
- Grid layout with color-coded categories
- Each category uses a different palette color as accent
- Dense but breathable spacing

### Comparison
- Side-by-side with contrasting gradient halves
- Left: warm gradient (before/challenge)
- Right: cool gradient (after/solution)

### Newsletter Header (16:9)
- Full gradient background (warm or cool based on topic)
- Minimal — wave shapes or geometric elements only
- NO text in the image
