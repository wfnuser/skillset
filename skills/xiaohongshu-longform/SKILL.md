---
name: xiaohongshu-longform
description: Compile a finished long-form Markdown article into a continuous-reading Xiaohongshu image carousel with natural pagination, restrained typography, inline images, recurring series presets, and traceable source metadata. Use for weekly reflections, monthly essays, annual reviews, travel writing, diaries, and other prose whose order and cadence should remain intact. Do not use for one-idea-per-page knowledge cards, product teardowns, or paper lists.
---

# Xiaohongshu Longform

Compile one canonical article into a readable Xiaohongshu carousel without creating a second drifting draft. Treat the carousel as one continuous article viewed through equal-height page windows, not as a deck of independent cards.

## Start here

1. Read the complete canonical article and its front matter.
2. If the article belongs to a recurring series, read `references/series-presets.md` and apply the matching preset.
3. Record the canonical source and chosen series in `source.md`.
4. Copy `assets/continuous-essay.html` and `assets/render.cjs` into the derivative project instead of starting from blank files.
5. Preserve article order and paginate naturally.

## Canonical-source rule

- Treat the selected Markdown article as the single source of truth.
- Do not silently rewrite, shorten, reorder, or correct it while compiling.
- Keep the derivative carousel in a separate project folder.
- Copy only images actually used into the derivative project's `assets/` folder.
- Reference project-local relative image paths from the rendered HTML.
- Keep platform captions and promotional copy separate from the canonical article.

## Project contract

Each derivative folder should contain:

```text
<slug>/
├── source.md
├── index.html
├── render.cjs
├── assets/
├── output/
└── preview-contact-sheet.png
```

Record at least the following in `source.md`:

```yaml
source: path or wiki link to the canonical article
mode: continuous-essay
series: monthly-reflection | life-integration-weekly | annual-review | custom
issue: optional
date_range: optional
cover: final cover copy
images: semantic anchor or unanchored
page_plan: ordered page roles
```

## Continuous-reading composition

- Mount one article stream and reveal successive equal-height windows from it.
- Use one consistent body area, type size, line height, margins, running header, and footer across body pages.
- Preserve headings only where the source reaches them; never repeat a title because a new image begins.
- Allow paragraphs and, when necessary, sentences to cross page boundaries.
- Keep true headings with the first lines that follow them without reserving a new page for every heading.
- Count inline images by the vertical space they occupy, then continue the article normally.
- Prefer full pages. Fix sparse pages by changing page count or flow boundaries, not by inventing copy or decoration.
- Preserve a few meaningful bold phrases; do not bold whole paragraphs by default.

## Image rules

- Keep semantically anchored images beside the paragraph they illustrate.
- Treat screenshots as evidence: use `object-fit: contain` and do not crop important UI or labels.
- Distribute unanchored images only when they support nearby prose; omit weak filler images.
- Keep captions short, quiet, and centered beneath the image.
- Do not invent stock imagery for a text-first article unless the user asks.

## Cover rules

- Use one primary visual idea: title, formula, quotation, date range, or recurring series mark.
- Keep the series name, issue number, and subtitle subordinate to that idea.
- Reuse a preset's class names and numeric tokens verbatim across issues instead of eyeballing an older image.
- For `life-integration-weekly`, the font-smoothing invariant in the preset is part of the fixed cover contract.
- Include a clear left-swipe cue and count the cover in page numbering.
- Keep the cover legible at thumbnail size and avoid decorative devices that compete with the article identity.

## Build and verification

1. Update `--body-pages`, the mounting script's page count, total counters, article content, and image anchors together.
2. Render numbered `1080×1440` PNG files plus a contact sheet.
3. Adjust the body-page count until the final page is comfortably filled without clipping.
4. Verify text clipping, image cropping, page order, repeated headings, and accidental blank lower bands.
5. Show the cover and contact sheet before optional visual critique or publication.

External publishing requires an explicit user request.
