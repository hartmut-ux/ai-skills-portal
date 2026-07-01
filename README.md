# Multi-Platform AI Skills Portal

A template repository for publishing **AI skills** that work across **Kimi Code CLI**, **Claude Code**, and **Codex CLI**.

An AI skill is a reusable instruction pack that teaches your assistant how to do a specific job — write content, run research, create visuals, check arguments, or build apps — with consistent quality.

**Live page:** https://hartmut-ux.github.io/ai-skills-portal

## How it works

Each skill lives in `skills/<skill-name>/` and contains:

- `shared/SKILL-CORE.md` — the platform-agnostic skill definition.
- `.kimi/skills/<skill-name>/SKILL.md` — thin Kimi wrapper.
- `.claude/skills/<skill-name>/SKILL.md` — thin Claude wrapper.
- `.codex/skills/<skill-name>/SKILL.md` — thin Codex wrapper.

You edit the skill once in `shared/SKILL-CORE.md`. The wrappers only add platform-specific invocation hints and frontmatter.

## Push this repository to GitHub

```bash
cd /Users/hartmut/Documents/ai-skills-portal
git remote add origin https://github.com/hartmut-ux/ai-skills-portal.git
git branch -M main
git push -u origin main
```

Create a release tag to trigger the ZIP build:

```bash
git tag -a v0.1.0 -m "Initial release"
git push origin v0.1.0
```

## Enable GitHub Pages

1. Open `https://github.com/hartmut-ux/ai-skills-portal/settings/pages`.
2. Under **Source**, select **Deploy from a branch**.
3. Choose `main` and `/ (root)`.
4. Save. The page will be available at `https://hartmut-ux.github.io/ai-skills-portal`.

> Already done for this repo. The page is live.

## Where to store Claude skills for conversion

Place every skill you want to convert in its own folder under `skills/`:

```text
skills/
├── example-skill/
│   ├── README.md
│   ├── shared/
│   │   └── SKILL-CORE.md
│   ├── .kimi/skills/example-skill/SKILL.md
│   ├── .claude/skills/example-skill/SKILL.md
│   └── .codex/skills/example-skill/SKILL.md
├── your-claude-skill-1/
│   ├── README.md
│   ├── shared/
│   │   └── SKILL-CORE.md
│   ├── .kimi/skills/your-claude-skill-1/SKILL.md
│   ├── .claude/skills/your-claude-skill-1/SKILL.md
│   └── .codex/skills/your-claude-skill-1/SKILL.md
└── your-claude-skill-2/
    └── ...
```

### Migration checklist for each Claude skill

1. Unzip the original Claude skill.
2. Create `skills/<skill-name>/`.
3. Copy the original Claude `SKILL.md` content into `shared/SKILL-CORE.md`.
4. Remove platform-specific phrasing or replace "Claude" with neutral terms where possible.
5. Create the three thin wrappers under `.kimi/`, `.claude/`, `.codex/`.
6. Move shared assets (prompts, templates, code) into `shared/`.
7. Update the skill table in `index.md`.
8. Run `python scripts/package-skill.py <skill-name>` to test the ZIP output.

## Add a new skill

1. Copy the `skills/example-skill/` folder and rename it.
2. Replace the content in `shared/SKILL-CORE.md`.
3. Update the frontmatter in each wrapper `SKILL.md`.
4. Run the packaging script:

   ```bash
   python scripts/package-skill.py example-skill
   ```

5. Commit and push. GitHub Actions will attach the ZIP files to your next release automatically.

## Download structure

For each skill the following ZIP files are produced:

- `<skill>-all.zip` — wrappers for Kimi, Claude and Codex.
- `<skill>-kimi.zip` — Kimi wrapper only.
- `<skill>-claude.zip` — Claude wrapper only.
- `<skill>-codex.zip` — Codex wrapper only.

## License

MIT — reuse, resell or embed into your own tooling.
