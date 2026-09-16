# Series Presets

Presets provide defaults, not restrictions. User instructions and the canonical article always win.

## Monthly Reflection / 月度随笔

- Mode: `continuous-essay`
- Series identifier: `monthly-reflection`
- Cover: month or date, article title, one restrained subtitle, left-swipe cue.
- Body: preserve essay order and original section headings; do not turn each experience into a separate card.
- Images: anchor travel, event, or person photos to their paragraphs; distribute only truly unanchored atmosphere images.
- Emphasis: a few key phrases per long section, never a whole paragraph by default.
- Typical ending: preserve the original final cadence without adding a platform CTA.

## Life Integration (Weekly)

- Mode: `continuous-essay`
- Series identifier: `life-integration-weekly`
- Display label: `Life Integration (Weekly)` by default; allow issue-specific overrides such as `PhD Weekly #1`.
- Cover: series label and issue, exact date range, a compact subtitle beginning with “关于……”, and an optional recurring formula or integral when supplied by the author.
- Stable integral-cover variant: record `cover_variant: weekly-integral-v1` in `source.md`, add `weekly-cover` to the cover section, and add `cover-formula` to the formula heading. Use the following values unchanged across issues:
  - **NON-NEGOTIABLE RENDERING INVARIANT — follow the fuller/bolder approved cover:** set both `-webkit-font-smoothing: auto` and `-moz-osx-font-smoothing: auto` directly on `.weekly-cover`. This local rule must override any global or legacy `antialiased` / `grayscale` declaration. Do not treat matching `font-weight` values as sufficient: before delivery, inspect the computed smoothing value on the rendered cover and confirm it is `auto` for every issue.
  - Canvas and safe area: `1080×1440`; cover content padding `96px 88px 87px`, giving a `904px` usable width.
  - Series line: system sans, `500 22px/1`, letter spacing `.12em`.
  - Integral: `400 78px/1.18 "Times New Roman", serif`, letter spacing `-.025em`, top margin `210px`, fixed title-box height `296px`, `max-width: 904px`, and `white-space: nowrap`. The fixed height prevents different MathJax/date glyphs from moving later elements onto different subpixels across issues.
  - Subtitle: Songti/serif, `400 38px/1.65`, top margin `52px`, `max-width: 904px`, and keep it on one line for the standard weekly wording. A `.cover-date` span may identify the date semantically, but it must inherit the subtitle's exact font, size, weight, line height, letter spacing, and baseline; never enlarge or vertically shift the date independently.
  - Footer: left-swipe cue `42px/500` with `.04em` letter spacing; page number `17px/1`; count the cover as page `01`.
  - TeX wording: keep `\mathrm{d}(\mathrm{Week})` with ASCII half-width `(` and `)`. Never substitute Chinese full-width `（` or `）`.
  - Render check: the MathJax container must remain on one line, start at the `88px` left safe edge, and fit inside the `904px` content width. Do not resize one issue independently; revise the shared variant only if the recurring formula itself changes.
- Body: follow the canonical order—commonly input, research, work, life, and output—but never reorder merely to balance pages.
- Section headings appear only where the source reaches them. Body pages share one equal-height reading area.
- Images: screenshots or weekly evidence may stay inline with centered captions.
- Keep the voice personal, concise, and lightly humorous; do not inflate a weekly log into a manifesto.

## Annual Review / 年度总结

- Mode: `continuous-essay`
- Series identifier: `annual-review`
- Cover: year, annual title or theme, optional one-line subtitle.
- Body: allow larger chapter transitions than weekly or monthly posts, but still paginate as one continuous document.
- Structure: retain chronology or the author's thematic order. Do not manufacture “ten lessons” unless the source uses that structure.
- Images: select fewer, stronger images that represent turning points; avoid a dense photo album.
- Ending: preserve the author's retrospective conclusion and forward-looking note.
