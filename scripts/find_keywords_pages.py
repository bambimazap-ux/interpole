import re

with open('scripts/full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split("==================== PAGE ")

keywords = [
    "Introduction", 
    "Guidance", 
    "Standards", 
    "Body fluid", 
    "Sperm", 
    "Extraction", 
    "Quantification", 
    "Amplification", 
    "STR typing", 
    "Electrophoresis", 
    "Mixture", 
    "Statistics", 
    "Likelihood Ratio", 
    "Massively Parallel Sequencing", 
    "MPS", 
    "NGS", 
    "Phenotyping", 
    "Genealogy", 
    "Kinship", 
    "Wildlife",
    "References"
]

with open('scripts/keywords_output.txt', 'w', encoding='utf-8') as f_out:
    for p in pages:
        if not p.strip():
            continue
        parts = p.split(" ====================\n", 1)
        page_num = parts[0].strip()
        page_content = parts[1]
        
        lines = page_content.split("\n")
        for idx, line in enumerate(lines):
            for kw in keywords:
                if re.search(r'\b' + re.escape(kw) + r'\b', line, re.IGNORECASE):
                    if len(line.strip()) < 100:
                        f_out.write(f"Page {page_num} (Line {idx+1}): {line.strip()} [Match: {kw}]\n")
                        break
