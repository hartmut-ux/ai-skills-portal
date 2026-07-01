# DESIGN.md Template

Use this template when creating the visual design system for a new app. Fill in colors, fonts, and component rules based on the project's brand guidelines — or propose a professional default palette.

---

```markdown
# [App Name] — Design System

[Optional: note about brand relationship, e.g. "Based on [Parent Brand] guidelines but runs as independent brand."]

---

## Font

**[Font Name]** (Google Font, Variable Weight)

\```css
@import url('https://fonts.googleapis.com/css2?family=[Font+Name]:wght@300;400;600;700&display=swap');
font-family: '[Font Name]', sans-serif;
\```

### Typography scale (Desktop)

| Level | Size | Weight | Usage |
|-------|------|--------|-------|
| H1 | 48-64px | Bold (700) | Hero headlines |
| H2 | 36-52px | SemiBold (600) | Section headings |
| H3 | 28-48px | SemiBold (600) | Sub-headings |
| B1 | 24-32px | Regular (400) | Large intro text |
| B2 | 20-24px | Regular (400) | Subheadlines |
| B3 | 18-20px | Regular (400) | Large body text |
| B4 | 16px | Regular (400) | Standard body text |
| B5 | 14px | Regular (400) | Small text, labels |
| B6 | 12px | Regular (400) | Captions, footnotes |

### Typography scale (Mobile)
Reduce H1-H3 by ~30%, keep B4-B6 the same. Breakpoint at 768px.

---

## Colors

### Brand colors

| Name | Hex | Usage |
|------|-----|-------|
| **primary** | `#[HEX]` | Primary — headers, buttons, links, active elements |
| **accent** | `#[HEX]` | Accent — CTAs, highlights, badges, hover states |
| **secondary** | `#[HEX]` | Secondary — tags, secondary buttons |

### Neutrals

| Name | Hex | Usage |
|------|-----|-------|
| text | `#2F2F2F` | Body text |
| subtle | `#595959` | Secondary text, placeholders |
| disabled | `#8C8C8C` | Disabled elements |
| border | `#E3E3E3` | Borders, dividers |
| bg-light | `#F2F2F2` | Page background |
| white | `#FFFFFF` | Cards, modals, inputs |

### Alpha variants (for overlays, hover states)

\```css
--primary-10: rgba([R], [G], [B], 0.10);
--primary-30: rgba([R], [G], [B], 0.30);
--primary-50: rgba([R], [G], [B], 0.50);
--accent-10: rgba([R], [G], [B], 0.10);
\```

---

## Gradients (optional)

### Dark gradient (hero sections)
\```css
background: linear-gradient(135deg, #1a1a1a 0%, [mid-tone] 50%, [primary] 100%);
\```

### Light gradient (onboarding, light sections)
\```css
background: linear-gradient(135deg, [primary]20 0%, [accent]20 40%, #FFFFFF 100%);
\```

---

## Tailwind CSS Configuration

\```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#[HEX]',
          10: 'rgba([R], [G], [B], 0.10)',
          30: 'rgba([R], [G], [B], 0.30)',
        },
        accent: {
          DEFAULT: '#[HEX]',
          10: 'rgba([R], [G], [B], 0.10)',
        },
        secondary: '#[HEX]',
        // Add all brand colors here
      },
      fontFamily: {
        sans: ['[Font Name]', 'sans-serif'],
      },
    },
  },
}
\```

---

## shadcn/ui Theme Mapping

\```css
:root {
  --background: 0 0% 100%;
  --foreground: [HSL for text color];
  --primary: [HSL for primary];
  --primary-foreground: 0 0% 100%;
  --secondary: [HSL for secondary];
  --accent: [HSL for accent];
  --muted: 0 0% 95%;
  --muted-foreground: 0 0% 35%;
  --border: [HSL for border];
  --ring: [HSL for primary];
  --radius: 0.75rem;
}
\```

---

## Component Rules

### Buttons
- **Primary:** bg-primary, text-white, hover:bg-secondary
- **Accent:** bg-accent, text-white, hover:opacity-80
- **Outline:** border-primary, text-primary, hover:bg-primary-10
- **Ghost:** text-primary, hover:bg-primary-10
- Border-radius: 12px (rounded-xl)

### Cards
- bg-white, border border-[border-color], rounded-xl, shadow-sm
- Hover: shadow-md transition
- Padding: p-6

### Inputs
- bg-white, border border-[border-color], rounded-lg
- Focus: ring-2 ring-primary
- Height: h-12 (48px)

### Navigation / Sidebar
- bg-primary, text-white
- Active: bg-secondary or bg-primary-80
- Icons: lucide-react, 20px

### Chat interface (if applicable)
- User bubble: bg-primary-10, text-[text-color], rounded-2xl
- Bot bubble: bg-white, border, rounded-2xl
- Input: fixed bottom, bg-white, shadow-lg

### Badges / Tags
- Feature tags: bg-accent-10, text-accent, rounded-full, px-3 py-1
- Status: bg-primary-10 text-primary (active) | bg-[border] text-[subtle] (inactive)

### Tables
- Header: bg-primary, text-white
- Rows: alternating bg-white / bg-[bg-light]
- Borders: border-[border-color]

---

## General Rules

1. Font always [Font Name] — no fallback to system fonts in visible UI.
2. Primary is the lead color — accent only for CTAs and highlights, never large areas.
3. Dark mode: not planned for v1.
4. Responsive: mobile-first. Typography scale switches at 768px breakpoint.
5. Accessibility: contrast ratio minimum 4.5:1 for text.
6. Spacing: Tailwind standard (4px grid). Sections: py-16 (desktop), py-10 (mobile).
```

---

## Default palettes (when no brand guidelines exist)

### Professional Blue
- Primary: `#1E3A5F` (deep blue)
- Accent: `#FF6B35` (warm orange)
- Secondary: `#4A7FB5` (medium blue)

### Modern Purple
- Primary: `#2F1863` (plum)
- Accent: `#FF7D4E` (papaya)
- Secondary: `#694BAD` (orchid)

### Clean Green
- Primary: `#1B4332` (forest)
- Accent: `#F77F00` (amber)
- Secondary: `#2D6A4F` (sage)

### Warm Neutral
- Primary: `#292524` (stone-900)
- Accent: `#DC2626` (red-600)
- Secondary: `#78716C` (stone-500)

Recommended font pairings:
- **Sora** — geometric, modern, excellent readability
- **Inter** — neutral, professional, Google's default
- **Plus Jakarta Sans** — friendly, startup-feeling
- **DM Sans** — clean, geometric, pairs well with anything
