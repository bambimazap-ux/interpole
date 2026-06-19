---
name: forensic-translator
description: Handles processing, translation, page mapping, and structuring of forensic documents for the Interpol review website.
---

# Forensic Literature Translation & Structuring Skill

## Overview
This skill outlines instructions for processing, translating, and structuring forensic scientific reviews into a standardized JSON format. It ensures consistent terminology translation from English to Hebrew, accurate source page mapping, and formatting suitable for ingestion by the web application.

## Terminology Guidelines (English to Hebrew)
Translate technical forensic terms consistently:
- **Fingermarks / Fingerprints:** טביעות אצבע / עקבות אצבע
- **Forensic Biology:** ביולוגיה פורנזית
- **Short Tandem Repeat (STR):** חזרות קצרות רצופות (STR)
- **Forensic Investigative Genetic Genealogy (FIGG):** גניאלוגיה גנטית חקירתית פורנזית (FIGG)
- **Massively Parallel Sequencing (MPS) / Next-Generation Sequencing (NGS):** ריצוף מקבילי עמוק (MPS/NGS)
- **Mixture Interpretation:** פענוח תערובות DNA
- **Likelihood Ratio (LR):** יחס נראות (LR)
- **Rapid DNA:** אנליזת דנ"א מהירה
- **Cyanoacrylate Fuming:** אידוי ציאנואקרילט (אידוי דבק)
- **Vacuum Metal Deposition (VMD):** נידוף מתכות בוואקום (VMD)
- **Physical Developer (PD):** מפתח פיזיקלי (PD)
- **Powder Suspensions (PS):** תרחיפי אבקות
- **Thermal Paper:** נייר תרמי
- **Cartridge Cases:** תרמילי תחמושת
- **Time since deposition:** הזמן שעבר מאז הפקדת העקבה
- **Donor profiling:** פרופיל תורם

## JSON Schema Output
For each document, output a JSON file containing an array of chapter objects. Each chapter object MUST match the following structure:

```json
{
  "chapter_number": 1,
  "title_he": "שם הפרק בעברית",
  "title_en": "English Chapter Title",
  "summary_he": "תקציר מנהלים ממוקד בעברית (נקודות עיקריות, מסקנות והנחיות אופרטיביות למז\"פ)",
  "extended_he": "הרחבה מפורטת בעברית המפרטת את המחקרים, השיטות, התוצאות והמגמות המוצגות בדו\"ח",
  "key_terms": [
    {
      "term_en": "Technical Term in English",
      "term_he": "מונח בעברית",
      "definition_he": "הגדרה או הסבר קצר בעברית"
    }
  ],
  "source_pages": "X-Y",
  "audio_path": "media/category_ch1.mp3",
  "video_path": "media/category_ch1.mp4"
}
```

## Processing Steps
1. **Text Extraction:** Extract text from the specific page range corresponding to each chapter.
2. **Analysis & Translation:**
   - Summarize key findings (bullet points recommended for `summary_he`).
   - Write a detailed Hebrew explanation (`extended_he`) translating the main scientific breakthroughs, compared studies, and methods.
   - Extract key technical terms and map their definitions.
3. **Validation:** Check that no pages are skipped, no scientific terms are mistranslated, and the JSON is valid.
