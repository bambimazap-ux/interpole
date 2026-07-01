---
name: interpol-reviewer-packager
description: Local agent skill for expanding the Interpol forensic review portal with new categories from PDF files.
---

# Interpol Reviewer Packager Skill

This local skill documents the standard workflow for expanding the Interpol Forensic Science Reviews portal with new forensic laboratory categories from PDF reports.

## Workflow Overview

To add a new category (e.g., ballistics, documents, drugs) to the portal:
1. **Identify Category Metadata:** Choose a Category ID (lowercase English), user-facing Hebrew name, FontAwesome 6 icon, and HSL accent color scheme.
2. **Translate and Structure PDF:** Translate the English PDF into 5 Hebrew chapters, outputting a structured JSON database in `data/<category>_data.json`.
3. **Extend Portal UI:** Add the category navigation button to `index.html` and define the custom theme class in `style.css`.
4. **Integrate Logic:** Register the new category, add its fallback data, and filter/categorize the glossary rendering in `app.js`.
5. **Verify and Deploy:** Check JSON formatting, test interface responsiveness locally, and push to GitHub Pages.

---

## 1. Category Design Rules

- **Category ID:** Singular lowercase word (e.g., `firearms`, `toxicology`, `documents`).
- **Icon:** Use standard solid FontAwesome 6 icons (e.g., `fa-gun`, `fa-flask`, `fa-file-lines`).
- **Color Palettes (HSL):** Pick a vibrant accent color that stands out from the existing categories:
  - **DNA:** Teal (`hsl(180, 85%, 43%)`)
  - **Fingermarks:** Purple (`hsl(270, 85%, 65%)`)
  - **Firearms:** Bronze/Amber (`hsl(38, 90%, 55%)`)
  - *New categories should pick other unused hues (e.g., Green `hsl(120, ...)` or Crimson Red `hsl(350, ...)`).*

---

## 2. Translation & Content Rules

- **Database Path:** Save the translated data as a JSON array under `data/<category>_data.json`.
- **Chapter Division:** Always divide the report into exactly **5 chapters** to fit the portal layout.
- **Strict Translation Tone (Objective):**
  - **Executive Summary (`summary_he`):** Bulleted list of key findings and scientific conclusions. It must **never** contain operational advice, personal recommendations, or instructions directing Mezap investigators.
  - **Detailed Technical Expansion (`extended_he`):** Thorough scientific description of methodologies, statistics, parameter values, and research outcomes. Use bold headers for organization. It must **never** contain personal recommendations.
  - **Source Pages (`source_pages`):** Always specify the exact pages in the original report corresponding to the chapter (e.g., `"11-15"`).
  - **Key Terms (`key_terms`):** Extract and define key terms. Format:
    ```json
    {
      "term_en": "English Term",
      "term_he": "מונח בעברית",
      "definition_he": "הגדרה תמציתית בעברית"
    }
    ```

---

## 3. Code Integration Checklist

### index.html
Add the button in `#category-nav-section`:
```html
<button class="category-btn" id="btn-cat-<id>" onclick="switchCategory('<id>')">
    <i class="fa-solid fa-<icon> icon-category"></i>
    <span><Hebrew Name></span>
</button>
```

### style.css
Add the HSL variables under category overrides:
```css
body.theme-<id> {
    --accent: hsl(<hue>, <sat>%, <light>%);
    --accent-rgb: <r>, <g>, <b>;
    --accent-hover: hsl(<hue>, <sat>%, <light-10>%);
    --accent-gradient: linear-gradient(135deg, hsl(<hue>, <sat>%, <light>%), hsl(<hue-10>, <sat-5>%, <light-5>%));
    --accent-glow: rgba(<r>, <g>, <b>, 0.35);
}
```

### app.js
1. Declare the data variable `let <category>Data = [...fallback<Category>Data];`.
2. Declare the fallback data array `const fallback<Category>Data = [...]` containing the full JSON payload.
3. Update `loadDataFiles()` to fetch `data/<category>_data.json` and assign it to `<category>Data`.
4. Update `initChapterModes()` to register the new chapters.
5. Modify functions using binary category logic (e.g., `currentCategory === 'dna' ? dnaData : fingermarkData`) to support multiple categories.
6. Modify `buildGlobalGlossary()` to parse terms from all categories, adding the `"category"` tag to each term.
7. Modify `renderGlossary()` to filter terms so that only terms belonging to the active category are rendered.
