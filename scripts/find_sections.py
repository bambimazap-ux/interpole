import pypdf
import re
import sys

reader = pypdf.PdfReader('1-s2.0-S2589871X26000483-main.pdf')

keywords = {
    "SWGDAM": "swgdam",
    "OSAC": "osac",
    "NIST": "nist",
    "ENFSI": "enfsi",
    "UK FSR": "fsr",
    "Body fluid": "body fluid",
    "RNA": "rna",
    "Raman": "raman",
    "Extraction": "extraction",
    "qPCR / Quantification": "quantification",
    "STR typing": "str typing",
    "Direct PCR": "direct pcr",
    "Electrophoresis / Artifacts": "electrophoresis",
    "Mixture / DNAmix": "mixture",
    "Likelihood Ratio / LR": "likelihood",
    "MPS / NGS": "mps",
    "Phenotyping / FDP": "phenotyping",
    "FIGG / Genealogy": "genealogy",
    "Single-cell": "single-cell"
}

with open('scripts/sections_output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total Pages: {len(reader.pages)}\n")
    f.write("=" * 60 + "\n")

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        first_lines = "\n".join([line.strip() for line in text.split("\n")[:10] if line.strip()])
        f.write(f"\n--- Page {i + 1} ---\n")
        f.write(f"First few lines:\n{first_lines}\n")
        
        found_kw = []
        text_lower = text.lower()
        for kw, pattern in keywords.items():
            if re.search(pattern, text_lower):
                found_kw.append(kw)
        if found_kw:
            f.write(f"Keywords found: {', '.join(found_kw)}\n")
