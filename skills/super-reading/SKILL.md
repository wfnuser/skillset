---
name: super-reading
description: Create a fixed three-page paper-reading deck and a matching HTML explainer for research group meetings.
---

# Super Reading

Use this skill when the user asks for a Super Reading, paper速读、组会论文 slides, or a compact paper walkthrough.

## Fixed deliverable

Super Reading is **exactly three pages total**. “Three pages” is a fixed count, not a 3–5 page range. Do not add a cover, table of contents, thank-you page, or standalone benchmark page.

The three pages have fixed narrative jobs:

1. **问题 + 思路**：论文解决的具体问题、现有方法的关键矛盾、作者的核心 insight。
2. **具体解决方案和亮点**：方法数据流/算法路径，以及真正新增的机制；最多保留 3–4 个步骤。
3. **实验结果**：最能支持主张的结果、必要的消融或对照、局限和结果含义。

## Content rules

- Each page has one clear takeaway and a direct title.
- Use only claims, numbers, formulas, and figures supported by the paper or clearly label an inference.
- Prefer one main diagram or evidence block per page; do not turn the deck into a literature survey.
- Keep formulas readable and explain what each variable means; remove equations that do not change the audience’s understanding.
- Page 3 must explain what the reported numbers measure, not merely reproduce a table.
- Separate “论文做了什么” from “对我们项目的启发”. Project implications may appear as a short callout on page 3, but must not be presented as paper results.

## Output convention

Store deliverables under:

```text
Obsidian/TheVault/Output/Presentations/Super Reading - <Paper>/
├── slides.html
├── index.html                 # optional long-form explainer
├── <Paper> - Qinghao Huang.pptx  # when PPTX is requested
└── assets/
```

`slides.html` is the canonical visual source for the three-page deck. The optional `index.html` is a separate long-form reading aid and may contain more detail, but it must not change the three-page structure.

Workflow: build and revise `slides.html` first. Only generate or update the PPTX after the user approves the HTML version. For PPTX requests, use the installed presentations skill and validate the final deck by rendering all three slides. Keep the slide count exactly three and preserve the information hierarchy of `slides.html`.

## Default visual and writing style

- 16:10 white canvas, black/gray text, thin rules, compact footer, and **one accent color only**. Use the accent for progress bars, tags, callouts, section labels, and emphasis; do not assign separate colors to different mechanisms or metrics. Original paper figures may retain their own colors when reused.
- Keep container styling consistent: highlighted insight, training, and takeaway boxes should share the same light accent fill, thin border, accent left rule, and square corners; neutral metric/table cards should share a separate gray treatment.
- Check the vertical composition at the final 16:10 export size. Do not let a `flex: 1` spacer push the mechanism cards and training strip to the bottom while leaving a large empty middle; figures inside a flexible region must grow to use that region, or the region must use explicit compact sizing.
- For image-backed PPTX export, render the approved HTML at a viewport close to the intended presentation preview (typically 1600×1000 for this 16:10 layout), keep the custom 16:10 ratio, and place the screenshot edge-to-edge on the slide. Do not inflate the viewport width solely for “高清”, because fixed CSS text then becomes visually too small after slide fitting.
- Avoid slogans, vague section labels, filler subtitles, and presenter narration on slides.
- Footer convention on **all three pages**: bottom left = `Paper authors · Main affiliations · Venue Year`; bottom right = lecturer/presenter name when requested. **REQUIRED: include the authors’ main affiliations (主要机构：公司、学校或研究机构)**, not just author names and venue.
- Verify affiliations against the paper's author affiliations for the version being presented, not the authors' current employers. For multi-institution work, include the principal contributing institutions; use recognizable abbreviations if needed for a compact footer. If affiliations cannot be verified, flag this to the user instead of guessing. Keep the footer content and alignment consistent across all three pages and carry the same affiliations into any later PPTX export.
- On page 1, use the paper title as the main title. Put the paper's motivating problem in the subtitle. Do not use a self-authored question as the main title when the paper title is available.
- Prefer the paper's original figures, tables, and diagrams over redrawing them. Crop or reuse the source figure with a small source label when it materially improves fidelity; redraw only when the paper has no suitable visual or when the edit is necessary to explain a derived comparison.
