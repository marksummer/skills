# Wireframes skill

An agent skill that turns a polished UI design into wireframes for stakeholder reviews, so feedback stays on content, flow and structure instead of colors and fonts.

The agent draws each screen once and packages everything as one self-contained HTML page that switches between four levels:

| Level | What it shows |
|---|---|
| Design | The original screenshot |
| Mid-fi | Real words and layout, with color, type and imagery removed |
| Low-fi | Boxes and labels; body text becomes grey lines |
| Structure | Each part of the screen as a labeled block, shaded by priority |

The page has a Screen view and an All screens view, numbered note pins, a full-screen Present mode, and keyboard shortcuts. When it is published as a Claude artifact, reviewers can also pin comments on any spot.

It works from screenshots, Figma frames, web pages, HTML prototypes, Claude artifacts or a running app.

## Install

The skill is the `wireframes/` folder in [marksummer/skills](https://github.com/marksummer/skills). Run the commands below from the repository root. Clone this repository once, then link that folder where each tool looks for skills.

```bash
git clone https://github.com/marksummer/skills.git ~/code/wireframes-skill
```

**Codex and Cursor** read `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills
ln -s ~/code/wireframes-skill/wireframes ~/.agents/skills/wireframes
```

**Claude Code** reads `~/.claude/skills` (Cursor reads it too):

```bash
mkdir -p ~/.claude/skills
ln -s ~/code/wireframes-skill/wireframes ~/.claude/skills/wireframes
```

**Claude apps (claude.ai, desktop):** zip the `wireframes/` folder and upload the zip as a custom skill.

```bash
cd ~/code/wireframes-skill && zip -r wireframes.zip wireframes
```

Pull the repository to update; the links pick up the changes.

## Requirements

- Python 3.9 or later (standard library only).
- Chrome, Chromium, Edge or Brave for the check snapshots (`--snap`). Set `CHROME=/path/to/browser` if it is not found.
- Optional: `sips` (macOS) or Pillow to shrink large screenshots.

## Use

Ask your agent in plain words, for example: "Turn these four screenshots of our sign-up flow into wireframes for a stakeholder review." The skill describes the full workflow in `wireframes/SKILL.md`.

To try the build on its own:

```bash
python3 wireframes/scripts/build.py wireframes/assets/example-boards.html --out example.html --open
```

## Layout

```
wireframes/
  SKILL.md                 workflow the agent follows
  references/primitives.md board vocabulary (wf- classes, zones, notes, patterns)
  references/capture.md    getting screenshots from each kind of source
  assets/viewer.html       page template
  assets/example-boards.html
  scripts/build.py         builds the page, lints boards, renders check snapshots
```

## License

[MIT License](../LICENSE), shared with the rest of this repository.
