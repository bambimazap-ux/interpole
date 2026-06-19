import pypdf
import re

reader = pypdf.PdfReader('1-s2.0-S2589871X26000483-main.pdf')

header_pattern = re.compile(r'^\s*([1-9]\.[0-9]?\.?\s+[A-Z].*|[1-9]\s+[A-Z].*)')

with open('scripts/headers_output.txt', 'w', encoding='utf-8') as f:
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        f.write(f"\n--- Page {i + 1} ---\n")
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            # print lines that start with numbers followed by uppercase words or look like section titles
            if header_pattern.match(line) or "Introduction" in line or "Standards" in line or "fluid" in line.lower() or "mixture" in line.lower() or "sequencing" in line.lower() or "genealogy" in line.lower():
                f.write(f"  {line}\n")
