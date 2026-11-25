---
name: wireframe
description: Convert existing UI designs into mid-fi, low-fi, and structural wireframes in a standalone HTML review page with the original images. Use to strip visual polish before reviewing content, hierarchy, or flow. Start from screenshots, design frames, pages, prototypes, or running apps. Not for inventing a new interface.
---

# Wireframe

Preserve an existing design's geometry and meaning while reducing visual detail for review. Draw each screen once with `wf-` primitives; the viewer renders the same board at all three wireframe levels beside the original screenshot.

## Choose the review focus

Identify the supplied screens, their main tasks, and the question the review should answer. Keep the requested screen/flow scope; do not redesign it while translating.

| Level | Preserve | Remove | Use to review |
| --- | --- | --- | --- |
| Design | Original screenshot | Nothing | Finished appearance |
| Mid-fi | Geometry, visible wording, controls, meaningful states | Brand colors/type, photos, decorative icons | Content, wording, and order |
| Low-fi | Same geometry, headings, field names, action labels, decision-critical status | Body detail shown as grey lines | Grouping and arrangement |
| Structure | Labeled regions, user purpose, relative priority | Individual controls and prose | Purpose and importance |

Choose the starting view from the review question; use Mid-fi when none is supplied. Structure suits prioritization; Low-fi suits grouping; Mid-fi suits wording. Keep all levels available in the default deliverable. Audience is a useful hint, not a substitute for the stated question.

At Low-fi, keep text or symbols that tell reviewers what the user can do, what blocks an action, what is selected, or what just happened. Use `data-keep` on body or meta text that carries one of those facts, and a meaningful glyph or label for an icon-only control. If color is the only cue, translate its source-supported meaning into a grayscale cue or flag it in a review note. Reduce other prose to grey lines so grouping is easier to judge without losing the task's meaning.

Paths below are relative to this skill's folder.

## Get the design

Use [capture guidance](references/capture.md) to save an original image per screen and set the board geometry before drawing. A known capture viewport, frame size, or export scale takes precedence over the measurement helper's guess because the same pixel dimensions can come from different devices and scales. Keep the source project unchanged unless the user asks for implementation.

## Map the screen

Give the screen a one-sentence purpose. Map regions top to bottom with a stakeholder-facing name, user purpose, and priority. Give the main job priority 1, supporting content priority 2, and minor content priority 3. A small region can be primary if it explains how to continue the task. Mark uncertain purpose as an open question and ask only when it would change the structure.

## Draw and calibrate one screen

Read [board primitives](references/primitives.md) and follow [the example](assets/example-boards.html). Create one `boards.html` in the work folder.

- Match point width, region positions, heights, side padding, and text hierarchy. Set the status bar's `data-time` from the image. Calibrate recurring measurements on the first screen before copying them.
- Transcribe visible words for Mid-fi. Replace personal names, emails, phone numbers, and addresses in board markup with realistic samples of similar length so anonymization does not change the layout.
- Use one primitive per meaningful element. Omit background art, gradients, and decorative icons. Preserve control states, including disabled actions, in the primitives.
- Give top-level regions `data-zone`, `data-purpose`, and `data-priority`. Do not nest zones: only the outer one renders. Put a single control's zone on its full-width row so its label has room.
- Add `data-note` for supplied decisions or useful open questions. Use neutral descriptions when rationale is unknown; never invent intent or add notes to meet a quota. Attach pins to boxes or rows so they do not cover words.
- Use inline styles only for size, spacing, and position. The levels own color, fonts, shadows, and opacity; hardcoded styling would leak polish across levels.

Build and inspect the first screen:

```bash
python3 <skill-dir>/scripts/build.py <work-dir>/boards.html --out <work-dir>/<flow-name>.html --snap <first-screen-id>
```

Inspect the printed `snap/<id>.png`: Design, Overlay, Mid-fi, Low-fi, and Structure. Correct region edges, status bar, side padding, text sizes, and row heights before drawing the remaining screens. Copy shared regions and change only state-specific content.

## Build and verify

```bash
python3 <skill-dir>/scripts/build.py <work-dir>/boards.html --out <work-dir>/<flow-name>.html --snap
```

The helper embeds screenshots, shrinks large ones, derives board heights, and validates summaries, zones, classes, and inline styles. Fix warnings by correcting markup; do not suppress them to claim a clean result.

Inspect every screen's snapshot:

- Overlay: geometry aligns with the original; note any unavoidable font-width differences.
- Mid-fi: words remain legible without overflow or overlap.
- Low-fi: field names, action labels, and decision-critical states still convey the same task.
- Structure: regions have readable labels and supported priority; pins leave words visible.

Rebuild changed screens with `--snap home new-timesheet` and inspect once more. Snapshot checks need Chrome, Chromium, Edge, or Brave; set `CHROME=/path/to/browser` when needed. Without one, inspect through a browser tool and switch Design/Mid-fi with keys 1 and 2. Report unavailable visual checks.

Open the final HTML and exercise its level switch, screen navigation, notes, and Present/Exit controls, including the narrow viewer layout when possible. These are review-page interactions; static boards do not establish working app navigation or product behavior.

## Deliver and revise

Deliver the self-contained HTML, not just check images. Summarize included screens, the starting review focus, and notes needing input. Use `--start low` (or `design`, `mid`, `struct`) for a chosen starting level.

For presentation order, shortcuts, hosted comments, or feedback summaries, read [review and sharing](references/review-and-sharing.md). Only use artifact-specific tools when available; a standalone file remains usable without them. Before sharing, review original screenshots as well as board text for private content: replacing board names does not redact the original image.

Keep `boards.html`, screen IDs, and the output path stable through revisions so links retain their targets. Rebuild and recheck affected screens; preserve agreed structure unless the user requests changes.
