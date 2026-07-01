#!/usr/bin/env python3
"""
QA Check Script for Branded Visual Factory
Validates HTML files against brand configuration rules.

Usage:
  python qa-check.py <html-file> <brand>

  brand: "mmind" or "flowmomentum"

Returns a score (0-100) and lists all issues found.
"""

import sys
import re
import os

# Brand color palettes
BRAND_COLORS = {
    "mmind": {
        "allowed": ["#CC798E", "#EE876F", "#FAEAE9", "#F2F2F2", "#0D0D0D", "#FFFFFF",
                     "#cc798e", "#ee876f", "#faeae9", "#f2f2f2", "#0d0d0d", "#ffffff"],
        "name": "MMIND.ai",
        "font": "Inter",
        "forbidden_patterns": ["gradient", "box-shadow", "text-shadow", "filter: blur", "backdrop-filter",
                                "rgba", "linear-gradient", "radial-gradient"],
        "required_patterns": ["1080px", "1350px"],  # or 1280x720 for headers
    },
    "flowmomentum": {
        "allowed": ["#D9D9D9", "#96A7FF", "#F3E4C7", "#F5B9A0", "#0066FF", "#99FFBB",
                     "#0A0A0A", "#FFFFFF",
                     "#d9d9d9", "#96a7ff", "#f3e4c7", "#f5b9a0", "#0066ff", "#99ffbb",
                     "#0a0a0a", "#ffffff"],
        "name": "FlowMomentum.ai",
        "font": "Satoshi",
        "forbidden_patterns": ["filter: blur", "backdrop-filter"],  # Gradients allowed!
        "required_patterns": ["1080px", "1350px"],
    }
}


def extract_hex_colors(html_content):
    """Extract all hex color values from HTML/CSS content."""
    # Match #RGB, #RRGGBB, #RRGGBBAA patterns
    pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
    colors = re.findall(pattern, html_content)
    # Normalize to 6-digit hex
    normalized = []
    for c in colors:
        if len(c) == 4:  # #RGB -> #RRGGBB
            c = f"#{c[1]*2}{c[2]*2}{c[3]*2}"
        normalized.append(c.lower())
    return list(set(normalized))


def check_colors(html_content, brand):
    """Check that only brand-approved colors are used."""
    issues = []
    found_colors = extract_hex_colors(html_content)
    allowed = [c.lower() for c in BRAND_COLORS[brand]["allowed"]]

    # Common non-brand colors to ignore (transparent, CSS defaults)
    ignore = ["#e0e0e0", "#000000"]  # body bg for preview, pure black

    for color in found_colors:
        if color.lower() not in allowed and color.lower() not in ignore:
            issues.append(f"Unapproved color: {color}")

    return issues


def check_fonts(html_content, brand):
    """Check that the correct brand font is referenced."""
    issues = []
    expected_font = BRAND_COLORS[brand]["font"]

    if expected_font.lower() not in html_content.lower():
        issues.append(f"Brand font '{expected_font}' not found in HTML")

    return issues


def check_dimensions(html_content, brand):
    """Check canvas dimensions."""
    issues = []

    # Check for either LinkedIn (1080x1350) or Newsletter (1280x720) dimensions
    has_linkedin = "1080px" in html_content and "1350px" in html_content
    has_newsletter = "1280px" in html_content and "720px" in html_content

    if not has_linkedin and not has_newsletter:
        issues.append("Canvas dimensions not found (expected 1080x1350 or 1280x720)")

    return issues


def check_forbidden_patterns(html_content, brand):
    """Check for CSS patterns forbidden by the brand."""
    issues = []
    forbidden = BRAND_COLORS[brand]["forbidden_patterns"]

    for pattern in forbidden:
        if pattern.lower() in html_content.lower():
            # For mmind, check if it's rgba in box-shadow vs rgba in color
            issues.append(f"Forbidden CSS pattern found: '{pattern}'")

    return issues


def check_structure(html_content):
    """Check basic HTML structure requirements."""
    issues = []

    if "<!DOCTYPE html>" not in html_content:
        issues.append("Missing DOCTYPE declaration")

    if "<meta charset=" not in html_content:
        issues.append("Missing charset meta tag")

    if "overflow: hidden" not in html_content and "overflow:hidden" not in html_content:
        issues.append("Canvas should have overflow: hidden")

    return issues


def check_content(html_content):
    """Check for placeholder text that wasn't replaced."""
    issues = []

    placeholders = re.findall(r'\{\{[A-Z_]+\}\}', html_content)
    if placeholders:
        issues.append(f"Unreplaced placeholders found: {', '.join(set(placeholders))}")

    if "lorem ipsum" in html_content.lower():
        issues.append("Lorem ipsum placeholder text found")

    return issues


def check_footer(html_content):
    """Check that footer/branding is present."""
    issues = []

    if "footer" not in html_content.lower():
        issues.append("No footer section found — brand attribution missing")

    return issues


def run_qa(html_file, brand):
    """Run all QA checks and return score + issues."""

    if brand not in BRAND_COLORS:
        print(f"Unknown brand: {brand}. Use 'mmind' or 'flowmomentum'.")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    all_issues = []

    # Run checks
    checks = [
        ("Colors", check_colors(content, brand), 20),
        ("Fonts", check_fonts(content, brand), 15),
        ("Dimensions", check_dimensions(content, brand), 15),
        ("Forbidden Patterns", check_forbidden_patterns(content, brand), 15),
        ("Structure", check_structure(content), 10),
        ("Content", check_content(content), 15),
        ("Footer/Branding", check_footer(content), 10),
    ]

    total_weight = sum(w for _, _, w in checks)
    earned = 0

    print(f"\n{'='*60}")
    print(f"  QA Report — {BRAND_COLORS[brand]['name']}")
    print(f"  File: {os.path.basename(html_file)}")
    print(f"{'='*60}\n")

    for name, issues, weight in checks:
        if not issues:
            earned += weight
            status = "PASS"
            print(f"  [{status}] {name} ({weight}/{weight} pts)")
        else:
            # Partial credit: lose proportionally to number of issues
            deduction = min(weight, len(issues) * (weight // 3))
            earned += (weight - deduction)
            status = "FAIL"
            print(f"  [{status}] {name} ({weight - deduction}/{weight} pts)")
            for issue in issues:
                print(f"         → {issue}")
            all_issues.extend(issues)

    score = round((earned / total_weight) * 100)

    print(f"\n{'─'*60}")
    print(f"  SCORE: {score}/100")
    if score >= 95:
        print(f"  Status: PRODUCTION READY")
    elif score >= 80:
        print(f"  Status: NEEDS MINOR FIXES")
    elif score >= 60:
        print(f"  Status: NEEDS REVISION")
    else:
        print(f"  Status: MAJOR ISSUES — DO NOT PUBLISH")
    print(f"{'─'*60}\n")

    return score, all_issues


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python qa-check.py <html-file> <brand>")
        print("  brand: 'mmind' or 'flowmomentum'")
        sys.exit(1)

    html_file = sys.argv[1]
    brand = sys.argv[2].lower()

    if not os.path.exists(html_file):
        print(f"File not found: {html_file}")
        sys.exit(1)

    score, issues = run_qa(html_file, brand)
    sys.exit(0 if score >= 95 else 1)
