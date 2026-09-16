# Repository guidance

- Treat `skills/` as the canonical source of every published Skill in this repository.
- Do not edit installed copies under `~/.codex/skills`, `~/.claude/skills`, or `~/.agents/skills` and then forget to port the change back here.
- Keep each Skill self-contained and make its directory name match the `name` field in `SKILL.md`.
- Keep generated media, test artifacts, personal documents, tokens, and machine-specific paths out of Git.
- Run `python3 scripts/validate.py` after modifying any Skill.
- Preserve user intent and existing behavior when refining a Skill; test meaningful output rather than matching prose mechanically.
- Do not vendor third-party Skills into this repository. Link to their upstream installation instructions instead.
