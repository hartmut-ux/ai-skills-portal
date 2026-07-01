# Brand Config: MMIND.ai

## Identity
- **Brand**: MMIND.ai
- **Tagline**: AI-Beratung für KMU
- **Website**: https://mmind.space
- **Logo position**: Bottom-right, small, #0D0D0D on light backgrounds
- **Source line format**: "Quelle · mmind.ai"

## Color Palette (STRICT — only these 5 colors + white)

| Role | Name | Hex | CSS Variable |
|------|------|-----|-------------|
| Primary Accent | Dusty Rose | #CC798E | --color-primary |
| Secondary Accent | Soft Coral | #EE876F | --color-secondary |
| Light Fill | Light Blush | #FAEAE9 | --color-fill-light |
| Neutral Fill | Light Gray | #F2F2F2 | --color-fill-neutral |
| Text & Lines | Near-Black | #0D0D0D | --color-text |
| Background | White | #FFFFFF | --color-bg |

### Color Usage Rules
- Headlines and key data: #CC798E or #EE876F
- Body text and labels: #0D0D0D
- Card backgrounds: #FAEAE9 or #F2F2F2
- Page background: #FFFFFF
- Dividers and outlines: #0D0D0D (1px)
- NO gradients. NO shadows. NO transparency/opacity.

## Typography

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Headline | Inter | 700 (Bold) | 48-56px | #0D0D0D |
| Subheadline | Inter | 400 (Regular) | 24-28px | #0D0D0D |
| Body Text | Inter | 400 (Regular) | 18-22px | #0D0D0D |
| Stats/Callouts | Inter | 700 (Bold) | 36-44px | #CC798E or #EE876F |
| Labels/Small | Inter | 300 (Light) | 12-14px | #0D0D0D |
| Source Line | Inter | 300 (Light) | 12px | #0D0D0D |

### Font Loading
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

Fallback stack: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`

## Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| --space-xs | 8px | Inline gaps, icon padding |
| --space-sm | 16px | Between related elements |
| --space-md | 24px | Between sections |
| --space-lg | 40px | Major section breaks |
| --space-xl | 64px | Top/bottom page margins |

## Cards & Boxes

- Background: #FAEAE9 or #F2F2F2 (fully opaque)
- Border: 1px solid #0D0D0D
- Border-radius: 12-16px
- Padding: 24px
- NO blur, NO transparency, NO shadow, NO gradient

## Visual Style: Flat Vector SaaS

This brand uses a strict flat vector aesthetic inspired by Notion, Linear, and Stripe illustrations.

### Allowed
- Clean geometric shapes
- Flat color fills
- Thin outlines (#0D0D0D, 1-2px)
- Simple flat icons (line-art style)
- Rounded corners (12-16px)

### FORBIDDEN
- Gradients of any kind
- Shadows or drop shadows
- 3D effects or perspective
- Glassmorphism or blur
- Photorealistic elements
- Saturated colors outside palette
- Decorative or handwritten fonts
- More than 5 colors in any single graphic

## Visual Types and Layouts

### Data Card (Stil A)
- One large number center-stage
- Short context line below
- White background, data in accent color

### Infographic (Stil C)
- Process flow or comparison grid
- Light background
- Connection lines in #0D0D0D
- Nodes/sections in accent colors

### Cheat Sheet
- Dense information, grid-based
- Multiple sections with clear headers
- Designed to be saved (bookmark-worthy)

### Comparison (Stil D)
- Two-column or before/after
- "Before" side: #F2F2F2 (muted)
- "After" side: accent colors

### Newsletter Header (Stil F — 16:9)
- Abstract geometric shapes
- White background
- Brand palette shapes and outlines
- NO text in the image
