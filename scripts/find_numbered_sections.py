import re

with open('scripts/full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split("==================== PAGE ")

# Match things like "2. ", "2.1. ", "3.5 ", "4.2.1. ", etc. at the start of a line
# Note: we will look for lines that start with digits and a dot, or a sub-section number.
section_pattern = re.compile(r'^\s*([0-9]+\.[0-9]+(?:\.[0-9]+)*|[0-9]+)\.?\s+([A-Z].*)')

with open('scripts/numbered_sections.txt', 'w', encoding='utf-8') as f_out:
    for p in pages:
        if not p.strip():
            continue
        parts = p.split(" ====================\n", 1)
        page_num = parts[0].strip()
        page_content = parts[1]
        
        lines = page_content.split("\n")
        for idx, line in enumerate(lines):
            line_strip = line.strip()
            # If the line starts with a number and a dot, or just a number, let's see
            match = section_pattern.match(line_strip)
            if match:
                f_out.write(f"Page {page_num} (Line {idx+1}): {line_strip}\n")
            elif line_strip.isupper() and len(line_strip) < 60:
                # Some section headers might be all uppercase
                f_out.write(f"Page {page_num} (Line {idx+1}) [UPPERCASE]: {line_strip}\n")
