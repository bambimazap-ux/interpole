import pypdf

reader = pypdf.PdfReader('1-s2.0-S2589871X26000483-main.pdf')

with open('scripts/full_text.txt', 'w', encoding='utf-8') as f:
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        f.write(f"\n==================== PAGE {i + 1} ====================\n")
        f.write(text)
        f.write("\n")
