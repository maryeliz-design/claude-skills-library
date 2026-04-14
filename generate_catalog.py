#!/usr/bin/env python3
"""
generate_catalog.py

Reads YAML front-matter from every .md file under skills/
and regenerates the catalog tables in README.md.

Run locally:  python scripts/generate_catalog.py
Run in CI:    called by .github/workflows/update-catalog.yml
"""

import os
import re
import yaml

SKILLS_DIR = "skills"
README_PATH = "README.md"

CATEGORY_ORDER = ["admin", "ux", "design", "requirements", "content"]
CATEGORY_LABELS = {
    "admin":        "🗂️ Admin",
    "ux":           "🖥️ UX",
    "admin":        "🗂️ Admin",
    "ux":           "🖥️ UX",
    "design":       "🎨 Design",
    "content":      "📝 Content",
    "requirements": "📋 Requirements",
    "brand":        "🏢 Brand",
}

def parse_frontmatter(filepath):
    """Extract YAML front-matter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

def build_catalog_tables():
    """Walk skills/ and build a dict of category -> list of skill rows."""
    categories = {cat: [] for cat in CATEGORY_ORDER}

    for category in CATEGORY_ORDER:
        cat_dir = os.path.join(SKILLS_DIR, category)
        if not os.path.isdir(cat_dir):
            continue

        for filename in sorted(os.listdir(cat_dir)):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(cat_dir, filename)
            meta = parse_frontmatter(filepath)
            if not meta:
                print(f"  ⚠️  Skipping {filepath} — no valid front-matter")
                continue

            name        = meta.get("name", filename.replace(".md", ""))
            description = str(meta.get("description", "")).strip().replace("\n", " ")
            roles       = meta.get("relevant_roles", [])
            owner       = meta.get("owner", "—")
            rel_path    = f"./{filepath}"

            if isinstance(roles, list):
                roles_str = " ".join(f"#{r}" for r in roles)
            else:
                roles_str = str(roles)

            categories[category].append(
                f"| [{name}]({rel_path}) | {description} | {roles_str} | {owner} |"
            )

    return categories

def build_catalog_markdown(categories):
    """Render category tables as a markdown string."""
    lines = []
    for cat in CATEGORY_ORDER:
        rows = categories.get(cat, [])
        if not rows:
            continue
        label = CATEGORY_LABELS[cat]
        lines.append(f"### {label}\n")
        lines.append("| Skill | Description | Relevant Roles | Owner |")
        lines.append("|-------|-------------|---------------|-------|")
        lines.extend(rows)
        lines.append("")
    return "\n".join(lines)

def update_readme(new_catalog_md):
    """Replace the catalog section in README.md between sentinel comments."""
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    start_marker = "<!-- CATALOG_START -->"
    end_marker   = "<!-- CATALOG_END -->"

    if start_marker not in readme or end_marker not in readme:
        print(
            "⚠️  README.md is missing <!-- CATALOG_START --> and <!-- CATALOG_END --> markers.\n"
            "   Add them around the catalog section to enable auto-updates."
        )
        return False

    new_section = f"{start_marker}\n{new_catalog_md}\n{end_marker}"
    updated = re.sub(
        re.escape(start_marker) + ".*?" + re.escape(end_marker),
        new_section,
        readme,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print("✅  README.md catalog updated.")
    return True

if __name__ == "__main__":
    print("🔍  Scanning skills/...")
    categories = build_catalog_tables()

    total = sum(len(v) for v in categories.values())
    print(f"   Found {total} skills across {len(CATEGORY_ORDER)} categories.")

    catalog_md = build_catalog_markdown(categories)
    update_readme(catalog_md)
