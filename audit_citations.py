import csv
import re
import os
import sys
from pathlib import Path

CS_REVIEW_DIR = Path("/mnt/Space/Projects/PhD/Latex/cs-review")
CONTENTS_DIR = CS_REVIEW_DIR / "contents"
BIB_FILE = CS_REVIEW_DIR / "references.bib"
BIB_MAP_FILE = CS_REVIEW_DIR / "revision_notes" / "phase4" / "paper_bibkey_map.csv"
V3_NOT_V4_FILE = CS_REVIEW_DIR.parent / "review_scripts" / "data" / "V4" / "Stim" / "V3_2025_selected_not_in_V4.csv"

cited_keys = set()
cite_pattern = re.compile(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}')
for tex_file in CONTENTS_DIR.rglob("*.tex"):
    with open(tex_file, "r", encoding="utf-8") as f:
        text = f.read()
        for match in cite_pattern.finditer(text):
            keys = match.group(1).split(",")
            for key in keys:
                cited_keys.add(key.strip())

with open(CS_REVIEW_DIR / "review_bci_cs.tex", "r", encoding="utf-8") as f:
    text = f.read()
    for match in cite_pattern.finditer(text):
        keys = match.group(1).split(",")
        for key in keys:
            cited_keys.add(key.strip())

bib_entries = set()
bib_pattern = re.compile(r'@\w+\s*\{\s*([^,]+),')
with open(BIB_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    for match in bib_pattern.finditer(text):
        bib_entries.add(match.group(1).strip())

corpus_keys = []
with open(BIB_MAP_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        bib_key = row["bib_key"].strip()
        if bib_key:
            corpus_keys.append(bib_key)

print("--- corpus-papers-without-bib-entry ---")
for key in corpus_keys:
    if key not in bib_entries:
        print(f"Missing in bib: {key}")

print("\n--- corpus-papers-not-cited-in-prose ---")
for key in corpus_keys:
    if key not in cited_keys:
        print(f"Not cited: {key}")

bib_titles = {}
title_pattern = re.compile(r'title\s*=\s*[\{"]([^}"]+)[\}"]', re.IGNORECASE)
entry_blocks = re.split(r'\n@', '\n' + open(BIB_FILE, "r", encoding="utf-8").read())
for block in entry_blocks:
    if not block.strip(): continue
    m_key = re.search(r'^\w+\s*\{\s*([^,]+),', block)
    m_title = title_pattern.search(block)
    if m_key and m_title:
        # keep alphanumeric only for matching
        clean_title = re.sub(r'[^a-z0-9]', '', m_title.group(1).lower())
        bib_titles[m_key.group(1).strip()] = clean_title

print("\n--- v3-not-v4-papers-still-cited ---")
try:
    with open(V3_NOT_V4_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = re.sub(r'[^a-z0-9]', '', row.get("Title", "").lower())
            for key in cited_keys:
                if key in bib_titles:
                    bib_title = bib_titles[key]
                    if title == bib_title:
                        print(f"Still cited: {key}")
except Exception as e:
    print(e)
