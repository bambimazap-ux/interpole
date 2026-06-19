import re

with open('scripts/full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split("==================== PAGE ")

for p in pages:
    if not p.strip():
        continue
    parts = p.split(" ====================\n", 1)
    page_num = parts[0].strip()
    page_content = parts[1]
    
    # Let's search for headers in page_content.
    # Looking for lines starting with numbers, e.g., "1. Introduction", "2. Standards", "2.1. ...", "3. ...", etc.
    lines = page_content.split("\n")
    for line in lines:
        line_strip = line.strip()
        # Look for section headers (e.g., "1. Introduction", "2. ", "2.1 ", "3.1.2 ", etc.)
        match = re.match(r'^([1-9]\.[0-9]+(?:\.[0-9]+)?|[1-9])\s+([A-Z].*)', line_strip)
        if match:
            print(f"Page {page_num}: {line_strip}")
        elif re.match(r'^[1-9]\s+[A-Z].*', line_strip):
            print(f"Page {page_num}: {line_strip}")
