# SEO & GEO Optimization Checklist

Complete checklist for landing page optimization. Apply to every production app landing page.

---

## Technical SEO — Must Have

### Meta Tags (in `<head>`)

```html
<!-- Title: primary keyword + brand, max 60 chars -->
<title>[Primary Keyword] — [App Name] | [Value Proposition]</title>

<!-- Description: what + for whom + CTA, max 155 chars -->
<meta name="description" content="[App Name] hilft [Zielgruppe] bei [Problem]. [Kernfeature]. Jetzt kostenlos starten.">

<!-- Canonical URL -->
<link rel="canonical" href="https://[domain.tld]/">

<!-- Language -->
<html lang="[de-CH / de-DE / en]">
```

### Open Graph (Social Sharing)

```html
<meta property="og:title" content="[Same as title or shorter]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:image" content="https://[domain.tld]/og-image.png">
<meta property="og:url" content="https://[domain.tld]/">
<meta property="og:type" content="website">
<meta property="og:locale" content="[de_CH / de_DE / en_US]">
```

### Twitter Card

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Title]">
<meta name="twitter:description" content="[Description]">
<meta name="twitter:image" content="https://[domain.tld]/og-image.png">
```

### OG Image specifications
- Size: 1200 x 630 px
- Format: PNG or JPG
- Include: logo, tagline, visual element
- Text must be readable at thumbnail size

---

## robots.txt

```
User-agent: *
Allow: /
Disallow: /dashboard/
Disallow: /api/
Sitemap: https://[domain.tld]/sitemap.xml
```

## sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://[domain.tld]/</loc>
    <lastmod>[YYYY-MM-DD]</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://[domain.tld]/features</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://[domain.tld]/pricing</loc>
    <priority>0.8</priority>
  </url>
  <!-- Add all public pages -->
</urlset>
```

---

## Schema.org Structured Data

### For SaaS / Web App

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[App Name]",
  "description": "[Description]",
  "url": "https://[domain.tld]",
  "applicationCategory": "[BusinessApplication / FinanceApplication / etc.]",
  "operatingSystem": "Web",
  "offers": {
    "@type": "Offer",
    "price": "[0 / price]",
    "priceCurrency": "[CHF / EUR / USD]"
  },
  "author": {
    "@type": "Organization",
    "name": "[Company Name]",
    "url": "https://[company-domain]"
  }
}
```

### For Local Business (regional apps)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "https://[domain.tld]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "postalCode": "[PLZ]",
    "addressCountry": "[LI / CH / AT / DE]"
  },
  "areaServed": [
    {
      "@type": "Place",
      "name": "[Region 1]"
    },
    {
      "@type": "Place",
      "name": "[Region 2]"
    }
  ]
}
```

---

## Content SEO

### Page structure
- One H1 per page with primary keyword
- H2 for section headings
- H3 for subsections
- At least 300 words unique content per page
- Alt text on all images (descriptive, include keyword if natural)
- Internal links between pages

### Landing page sections (recommended order)
1. **Hero** — H1 + subheadline + CTA + hero image
2. **Social proof** — logos, testimonials, numbers
3. **Problem** — what pain point the app solves
4. **Solution** — how the app solves it (features)
5. **How it works** — 3-step visual guide
6. **Features** — detailed feature cards
7. **Pricing** — plans or pricing model
8. **FAQ** — common questions (also helps SEO)
9. **CTA** — final call to action

---

## GEO Optimization (Regional Apps)

### When targeting a specific region (e.g., Liechtenstein, Eastern Switzerland)

**hreflang tags** (if multiple languages):
```html
<link rel="alternate" hreflang="de-CH" href="https://[domain.tld]/">
<link rel="alternate" hreflang="de-LI" href="https://[domain.tld]/">
<link rel="alternate" hreflang="x-default" href="https://[domain.tld]/">
```

**Regional keywords** to include naturally:
- City/region names in title, H1, and body text
- "in Liechtenstein", "für die Ostschweiz", "im Rheintal"
- Local currency (CHF, not EUR)
- Local terms and conventions

**Local directories** (register where applicable):
- Google Business Profile
- local.ch (Switzerland)
- Gelbe Seiten / directories for the target country
- Industry-specific directories

**Swiss German conventions:**
- No ß (use ss instead)
- Guillemets «...» for quotes (optional, but authentic)
- CHF for currency
- Swiss date format: DD.MM.YYYY
- Formal "Sie" or informal "du" — be consistent

---

## Performance (affects SEO ranking)

- Largest Contentful Paint (LCP): < 2.5 seconds
- First Input Delay (FID): < 100ms
- Cumulative Layout Shift (CLS): < 0.1

### Quick wins:
- Compress images (WebP format, max 200kb for hero images)
- Lazy load below-the-fold images
- Preload critical fonts
- Minimize JavaScript bundle
- Use CDN (Railway/Lovable handle this automatically)

---

## Post-Launch SEO Tasks

```
[ ] Submit sitemap to Google Search Console
[ ] Submit sitemap to Bing Webmaster Tools
[ ] Verify OG tags with https://developers.facebook.com/tools/debug/
[ ] Test structured data with https://search.google.com/test/rich-results
[ ] Check mobile-friendliness with Google Mobile Test
[ ] Set up Google Analytics or Plausible
[ ] Monitor Core Web Vitals in Search Console
```
