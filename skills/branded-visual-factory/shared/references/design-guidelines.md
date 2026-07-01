# Design Guidelines — Branded Visual Factory

Universelle Regeln für alle Brands. Brand-spezifische Regeln stehen in `brands/*.md`.

## Canvas Dimensions

| Format | Width | Height | Ratio | Use |
|--------|-------|--------|-------|-----|
| LinkedIn Single Image | 1080px | 1350px | 4:5 | Posts, Infographics, Cheat Sheets |
| LinkedIn Carousel Slide | 1080px | 1350px | 4:5 | Per slide |
| Newsletter Header | 1280px | 720px | 16:9 | Beehiiv, Blog headers |

## Visual Hierarchy

Every visual follows this hierarchy (top to bottom):

1. **Eyebrow** (optional) — Category, topic tag, or brand marker. Small, uppercase, accent color.
2. **Headline** — The main message. Bold, large, max 10 words.
3. **Body** — The content (steps, grid, data). 60-70% of canvas height.
4. **Callout** (optional) — Key takeaway, pro-tip, or pull-quote.
5. **Footer** — Source attribution + brand logo. Always present.

## Text Rules

- Max 7 items in any list or grid
- Max 40 words per section/card
- Headlines: max 10 words
- Subheadlines: max 20 words
- No orphaned words (single word on last line)
- Swiss spelling: "ss" not "ß"
- Numbers over words: "47%" not "fast die Hälfte"

## Spacing Principles

- **Consistent rhythm**: Use the spacing scale from the brand config. Don't invent custom values.
- **Breathing room**: Minimum 40px padding on all canvas edges.
- **Grouping**: Related items closer together (8-16px), unrelated items further apart (24-40px).
- **Vertical flow**: Content reads top-to-bottom. No Z-patterns or complex layouts.

## Color Application

### Contrast Requirements (WCAG AA)
- Body text on white: minimum 4.5:1 ratio
- Large text (24px+) on white: minimum 3:1 ratio
- Text on colored backgrounds: always check contrast

### Color Distribution Rule
- **60%** — Background/neutral (white, light fills)
- **30%** — Supporting elements (cards, sections, dividers)
- **10%** — Accent/highlight (headlines, stats, CTAs)

## Grid Systems

### 2-Column Grid (Cheat Sheets, Comparisons)
```
| 40px | ====== col 1 ====== | 16px | ====== col 2 ====== | 40px |
```

### 1-Column Flow (Infographics, Data Cards)
```
| 40px | ==================== content ==================== | 40px |
```

### 2x2 Grid (Cheat Sheets with 4 sections)
```
| section 1 | section 2 |
| section 3 | section 4 |
```

### 2x3 Grid (Cheat Sheets with 6 sections)
```
| section 1 | section 2 |
| section 3 | section 4 |
| section 5 | section 6 |
```

## Icon Usage

- Use simple, line-art style icons only
- Consistent stroke width (1.5-2px)
- Same color as text or primary accent
- Size: 20-32px for inline, 40-48px for section headers
- Source: Unicode symbols, SVG paths, or CSS-drawn shapes
- NO emoji (unless explicitly requested)

## Production Checklist

Before any visual is considered done:

1. [ ] Correct canvas dimensions (check width AND height)
2. [ ] Only brand-approved colors (run qa-check.py)
3. [ ] Correct font loaded and rendering
4. [ ] All placeholder text replaced
5. [ ] Footer with source + brand present
6. [ ] No overflow or clipping
7. [ ] Text contrast passes WCAG AA
8. [ ] Content scannable in 3 seconds (headline test)
9. [ ] Swiss spelling checked
10. [ ] File saves as valid, self-contained HTML
