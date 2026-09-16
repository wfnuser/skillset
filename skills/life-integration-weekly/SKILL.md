---
name: life-integration-weekly
description: Use when turning raw weekly notes, Logseq bullets, reading records, research updates, work progress, and life events into a concise first-person Life Integration or PhD Weekly article with the recurring sections 输入、研究、工作、生活.
---

# Life Integration Weekly

Compile one week's scattered records into a short personal weekly article. This skill owns **selection, organization, and weekly-series writing**. The result is a canonical blog Markdown file, not a social-image deck.

## Default series contract

Start from `assets/weekly-template.md` when creating a new issue. Preserve the user's requested order or the established series order. When neither exists, use:

1. `## 输入`
2. `## 研究`
3. `## 工作`
4. `## 生活`

Omit an empty section rather than inventing material. Add `输出` only when the user explicitly wants it or when publishing work is a central part of that week.

Within each major section, use a small number of descriptive `###` subheadings and ordinary paragraphs. Do not reproduce the Logseq tag tree and do not use two levels of nested lists as the article's structure.

## Read the source material

Accept any mixture of:

- Logseq bullets and tags;
- daily notes;
- reading and course records;
- paper lists and research setbacks;
- work updates, meetings, and community progress;
- photos and captions;
- the user's later corrections or additions.

Treat tags such as `#inputs`, `#research`, `#work`, `#life`, `#events`, and project names as routing metadata. They are not prose and normally should not appear verbatim in the article.

Before drafting, read the previous issue when available. Reuse the series conventions, but never copy its incidents, claims, or emotional conclusion into the new week.

## Select before expanding

Make a private four-column ledger:

```text
source item | section | why it matters this week | keep / merge / omit
```

Keep items that do at least one of the following:

- changed the author's understanding;
- moved research or a project forward;
- created a concrete emotional response;
- captures a memorable scene from the week;
- will matter when reread months later.

Merge adjacent course notes, paper notes, or small work updates. Omit empty bullets, duplicates, raw matrices, and details that only make sense inside the original class or task unless a short explanation makes them meaningful.

Do not force every research idea into its own subsection. Mention an idea only when it became a meaningful experiment, decision, discussion, or change of direction.

## Expansion budget

Keep the weekly concise. A useful default is:

- one to four subtopics per major section;
- one to three short paragraphs per subtopic;
- one concrete detail plus one restrained reflection;
- paper reading summarized by the central question or insight, not a miniature literature review;
- courses summarized by the strongest impression or takeaway, not by a syllabus dump;
- work summarized by what changed, who joined, what decision was made, or what happens next.

Expand the user's shorthand only enough to make it readable. Do not turn a week into an inspirational essay.

## Voice

Use the same voice rules as a personal blog:

- candid, first-person, specific, and lightly conversational;
- modest about success and honest about setbacks;
- occasional natural humor or emoji when present in the source;
- concrete observations before abstract lessons;
- no corporate weekly-report language and no synthetic “本周收获颇丰”.

Preserve phrases that carry personality. Repair grammar and transitions, but avoid making the entry sound more solemn or literary than the notes.

## Dates, title, and metadata

Derive the ISO week and date range carefully. Verify that weekdays, dates, issue number, and any displayed date range agree.

Use the existing series title when one exists. A typical canonical file may use:

```yaml
---
type: weekly
period: YYYY-MM-DD/YYYY-MM-DD
series: PhD Weekly
issue: N
status: draft
tags:
  - weekly
---
```

```markdown
# PhD Weekly #N

> 关于作者在 `YYYY-MM-DD` - `YYYY-MM-DD` 期间的人生积分 #N｜PhD Weekly #N
```

Treat this as a series preset, not a universal title. Preserve the user's established wording, pen name, institution suffix, and numbering scheme when known.

## Images

- Prefer zero to three images that record genuinely important moments or evidence.
- Place each image beside the relevant paragraph, not in a detached gallery.
- Correct orientation before use and preserve readable screenshots with `contain`-style presentation in downstream layouts.
- Do not add food, scenery, or meeting photos merely to make the article look busy.
- Use stable project-relative paths in the canonical Markdown.

## Canonical file and derivatives

Save or update the canonical article under the blog's weekly-series folder, for example:

```text
Output/Blog/周记/YYYY-Www - PhD Weekly N.md
```

If the user says they are editing the same file, reread it immediately before applying changes and keep their version primary.

Once approved, the article may be handed to:

- `personal-blog-writing` for a final light polish when needed;
- `xiaohongshu-longform` for continuous-reading image pages;
- a separate social-card skill for claim-based cards.

Publishing, pushing to GitHub, and generating images are separate actions. Perform them only when requested.

## Final checklist

- The four sections reflect the week's actual balance rather than equal quotas.
- Headings are large-topic plus small-topic only; the body is prose, not nested lists.
- Courses and paper reading keep only meaningful points.
- Research setbacks retain factual nuance and do not become self-criticism theater.
- Work updates state concrete progress and next direction without sounding like a status memo.
- Life scenes retain sensory or social details without becoming travel advertising.
- Dates, issue number, links, image orientation, and image paths are correct.
- The entry is short enough to remain a weekly habit.
