---
name: life-integration-writing
description: Use when the user provides diaries, Logseq notes, photos, reading, research, work, or life records and asks for a personal retrospective, weekly journal, monthly reflection, annual review, milestone summary, or transition narrative.
---

# Life Integration Writing

Turn scattered traces of a life into a durable personal record. The essential task is not “write a weekly report”; it is to select, connect, and summarize what happened during a meaningful period without making the result sound like a performance review.

This skill owns **source synthesis and life-review structure**. It may hand a completed draft to `personal-blog-writing` for deeper editorial polish, but it does not render social images or publish the result unless the user separately asks.

## Choose the scale

Choose the period before choosing headings:

- `weekly`: concise and close to the original events.
- `monthly`: recurring themes and meaningful changes, not four weekly reports joined together.
- `annual`: longer arcs, turning points, unfinished work, and changes in perspective.
- `milestone`: a transition such as graduation, moving, starting a PhD, finishing a project, or completing a journey.
- `open-period`: use the exact date range or life stage supplied by the user.

Read `references/format-presets.md` for the selected scale. Do not load every preset when only one applies.

## Work from life traces

Accept daily notes, diaries, Logseq bullets and tags, reading, courses, papers, experiments, work updates, relationships, health, hobbies, travel, photos, screenshots, and later corrections.

Treat tags such as `#inputs`, `#research`, `#work`, `#life`, `#events`, and project names as routing metadata rather than prose.

When a previous entry in the same series exists, read it to recover naming, numbering, metadata, rhythm, and level of detail. Do not carry its incidents or conclusions into the new period.

## Synthesis workflow

1. Build a private ledger:

   ```text
   source item | date or phase | domain | why it matters | keep / merge / omit
   ```

2. Keep items that changed the author's understanding, direction, relationship, routine, research, work, or project; preserve scenes the author will want to remember.
3. Merge duplicates. Omit empty bullets, raw matrices, administrative noise, and details that only mattered momentarily.
4. Choose chronology for a journey or transition; choose themes when several life domains developed in parallel.
5. Draft from concrete events, scenes, and decisions toward restrained reflection.

The familiar domains—输入、研究、工作、生活—are useful lenses, not mandatory quotas or universal headings. Preserve them when the series uses them; otherwise let the selected period determine the sections.

## Interpretation and voice

- Write in a candid, first-person, concrete, lightly conversational voice.
- Preserve uncertainty with language such as “可能”“感觉”“某种程度上”.
- Do not force unrelated events into one grand theme.
- Do not convert setbacks into self-criticism theater or ordinary progress into a success narrative.
- Let contradictions remain when they are honest: excitement and fatigue, freedom and responsibility, ambition and doubt can coexist.
- Distinguish what happened then from what the author understands now.
- Expand shorthand only enough to make it readable; keep telling details rather than every log entry.
- Avoid corporate language, motivational clichés, inflated lessons, and artificial literary flourishes.

If the user asks only to “梳理重点”, return a compact outline, likely themes, useful images, and genuinely missing facts. If they explicitly ask for a plan before drafting, treat it as an approval checkpoint when their wording implies review; otherwise present the plan first and continue into the draft.

## Accuracy and images

- Verify that the date range, week or month number, issue number, and filename agree.
- Mark conflicting dates or memories instead of silently choosing one.
- Do not invent distances, names, publication status, research results, motivations, or emotional certainty.
- Place a semantically anchored image after the passage it illustrates.
- Correct orientation, keep screenshots readable, and do not infer a photo's date, people, or meaning without evidence.
- For public writing, flag private names, relationships, locations, or images that may need consent or anonymization; do not silently rewrite them.
- Use stable project-relative image paths in canonical Markdown unless the user explicitly requests an absolute-path handoff copy.

## Canonical output

Store one canonical record under the appropriate blog or personal-output series:

```text
Output/Blog/<series>/<period-and-title>.md
```

Keep platform captions and rendered derivatives in the media output area. If the user is editing the same file, reread it before applying changes and keep their latest wording primary.

After approval:

- use `personal-blog-writing` when the draft needs structural or language polish;
- use `xiaohongshu-longform` when it should become continuous-reading image pages;
- use a dedicated social-card skill when the content should be decomposed into one claim per card.

Publishing, pushing to GitHub, and generating derivatives are separate actions and require an explicit request.

## Final check

Confirm that the record fits the selected period rather than an arbitrary template; facts and scenes survive while noise does not; reflections come from concrete experience; the author's uncertainty and mixed feelings remain recognizable; metadata and image paths are correct; and the length matches the chosen time scale.
