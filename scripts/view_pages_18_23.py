with open('scripts/full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split("==================== PAGE ")

with open('scripts/pages_18_23.txt', 'w', encoding='utf-8') as f_out:
    for p in pages:
        if not p.strip():
            continue
        parts = p.split(" ====================\n", 1)
        page_num = parts[0].strip()
        page_content = parts[1]
        
        if page_num in ["18", "19", "20", "21", "22", "23"]:
            f_out.write(f"\n================ PAGE {page_num} ================\n")
            f_out.write(page_content)
