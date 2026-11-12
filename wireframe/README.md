# Wireframe

Turn an existing design into wireframes for review. Switch between the original screen and three levels of detail to discuss content, flow, and structure.

## Install

Follow the [installation steps](../README.md#install) and choose Wireframe.

Requires Python 3.9 or later, using only the standard library. Snapshot checks (`--snap`) also need Chrome, Chromium, Edge, or Brave. Set `CHROME=/path/to/browser` if the browser is not found. To shrink large screenshots, use `sips` on macOS or Pillow.

## Use

```text
Use $wireframe to turn these four sign-up screens into wireframes for review.
```

Provide screenshots, Figma frames, a web page, an HTML prototype, a Claude artifact, or a running app.

## What you get

One self-contained HTML page with four views of each screen:

| Level | What it shows |
| --- | --- |
| Design | The original screenshot. |
| Mid-fi | Real words and layout with color, brand type, and imagery removed. |
| Low-fi | Boxes and labels, with body text shown as grey lines. |
| Structure | Labeled regions shaded by priority. |

The page includes Screen and All screens views, numbered notes, keyboard shortcuts, and a full-screen Present mode. It embeds screenshots and uses local system fonts, so you can review it offline.

Publishing as a Claude artifact adds comment pins through the Claude service. Those comments require a connection.

## Example

Run this from the repository root to try the build:

```bash
python3 wireframe/scripts/build.py wireframe/assets/example-boards.html --out example.html --open
```

## Manual setup

Clone the repository once, then link the skill folder where your tool looks for skills.

```bash
git clone https://github.com/marksummer/skills.git ~/code/wireframes-skill
```

Codex and Cursor read `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills
ln -s ~/code/wireframes-skill/wireframe ~/.agents/skills/wireframe
```

Claude Code reads `~/.claude/skills` (Cursor reads it too):

```bash
mkdir -p ~/.claude/skills
ln -s ~/code/wireframes-skill/wireframe ~/.claude/skills/wireframe
```

Claude apps (claude.ai, desktop): zip the `wireframe/` folder and upload the zip as a custom skill.

```bash
cd ~/code/wireframes-skill && zip -r wireframe.zip wireframe
```

Pull the repository to update the linked skill.


## Files

```
wireframe/
  SKILL.md                 workflow the agent follows
  references/primitives.md board vocabulary (wf- classes, zones, notes, patterns)
  references/capture.md    getting screenshots from each kind of source
  references/review-and-sharing.md presentation and optional hosted feedback
  assets/viewer.html       page template
  assets/example-boards.html
  scripts/build.py         builds the page, lints boards, renders check snapshots
```

[Instructions](SKILL.md) · [MIT License](../LICENSE) · [All skills](../README.md)
