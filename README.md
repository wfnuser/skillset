# skillset

Personal Agent Skills maintained by [wfnuser](https://github.com/wfnuser). Each Skill is self-contained under `skills/<name>/` and follows the shared `SKILL.md` convention used by Codex, Claude Code, Cursor, OpenCode, and other compatible agents.

## Included Skills

### Writing

| Skill | Purpose |
| --- | --- |
| `personal-blog-writing` | Draft, restructure, or lightly polish a personal Chinese blog article while preserving the author's voice. |
| `life-integration-weekly` | Turn Logseq bullets and weekly fragments into a concise Life Integration / PhD Weekly article. |

### Publishing and artifacts

| Skill | Purpose |
| --- | --- |
| `xiaohongshu-longform` | Compile long-form prose into a continuous-reading Xiaohongshu carousel with natural pagination and recurring series presets. |
| `super-reading` | Produce a fixed three-page paper-reading deck and matching HTML explainer. |
| `storage-analyzer` | Analyze macOS or Windows disk usage and generate a safe, interactive cleanup report. |

The writing Skills produce or refine the canonical article. Presentation Skills consume an approved article or analysis and generate a derivative artifact. Continuous long-form pages belong to `xiaohongshu-longform`; discrete knowledge or promotional cards should use a dedicated social-card Skill such as [`guizang-social-card-skill`](https://github.com/op7418/guizang-social-card-skill) rather than being mixed into the long-form compiler.

## Install

Install every Skill globally for every agent supported by the `skills` CLI:

```bash
npx skills add wfnuser/skillset --skill '*' --agent '*' --global --yes
```

Install only one Skill:

```bash
npx skills add wfnuser/skillset --skill super-reading --agent '*' --global --yes
```

Alternatively, clone the repository and run:

```bash
./scripts/install.sh
```

For local development, link all agents directly to this checkout so edits become visible immediately:

```bash
./scripts/install.sh --local
```

Restart or open a new session after installing so each agent refreshes its Skill catalog.

## Update

For a normal remote installation:

```bash
./scripts/update.sh
```

For a local development checkout, pull the repository; linked agents see the new files immediately:

```bash
git pull --ff-only
```

## Maintain

1. Edit the canonical source under `skills/<name>/`, never an installed copy under an agent's home directory.
2. Keep reusable instructions in `SKILL.md`; move conditional detail into `references/`, deterministic helpers into `scripts/`, and output templates into `assets/`.
3. Run `python3 scripts/validate.py` before committing.
4. Test the affected Skill on a realistic request and inspect its produced artifact.
5. Commit and push. Remote installations can then update with `npx skills update`.

Use Git tags such as `v0.1.0` for known-good snapshots. Keep ordinary installations on the default branch so `skills update` receives the latest maintained version.

Generated artifacts, personal source material, credentials, and machine-specific absolute paths do not belong in this repository.

## Repository Model

This repository intentionally contains only original Skills maintained here. Third-party Skills remain separate dependencies and retain their own upstream repositories and licenses.

## License

[MIT](LICENSE) © 2026 Qinghao Huang
