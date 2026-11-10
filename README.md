<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Skills by Mark Summer — Faster exploration. Deliberate design." src="assets/header-light.svg" width="1200">
</picture>

## Sketch

Quick, interactive wireframes for faster design exploration. Focus on one element while keeping the content, hierarchy, and interactions needed to make thoughtful decisions. Ask for a full screen or flow when needed.

## Clean Up

Remove unnecessary UI, tighten copy, and improve layout while preserving useful behavior and the existing visual identity. Uses Impeccable when available and also works independently.

[Usage and before/after example](clean-up/README.md) · [Skill instructions](clean-up/SKILL.md)

## Check Design System

Audit iOS apps, other codebases, and Framer projects against `DESIGN.md` when present and the project's shared tokens and components. Find drift, group repeated issues, and get exact locations, existing replacements, coverage, and a before-and-after visual preview where tooling permits.

Audits stay read-only unless you explicitly ask to implement fixes.

```sh
npx skills add marksummer/skills --skill check-design-system
```

```text
Use $check-design-system to audit this project. Keep it read-only.
```

[Skill instructions](check-design-system/SKILL.md) · [Add verification to DESIGN.md and AGENTS.md](check-design-system/references/project-integration.md)

## Install

```sh
npx skills add marksummer/skills
```

Requires Node.js. Run in your project and choose **Codex** and the skills you want. Tune Motion’s preview generator also requires Python 3.

**Interactive previews require the Visualize plugin in Codex, installed separately.** Without it, Sketch provides a layout outline; Tune Motion needs the plugin for its interactive editor.

Check Design System uses the available capture and rendering tools for comparisons. If a preview cannot be produced, it reports that limitation alongside the audit. Framer audits require a connected Framer MCP.

## Example: batch reminder entry

Can someone add and edit several reminders without losing track? This demo, based on **Aside**, explores editable rows, keyboard entry, and multiline paste.

<picture>
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/sketch-batch-dark.jpg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/sketch-batch-light.jpg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/sketch-batch-dark.gif">
  <img alt="An eight-second walkthrough showing a reminder being added and typed, Enter creating the next row, a multiline list becoming two reminders, and an entry being removed." src="assets/sketch-batch-light.gif" width="560">
</picture>

<details>
<summary>View a still preview</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sketch-batch-dark.jpg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sketch-batch-light.jpg">
  <img alt="A focused reminder-entry sketch with three editable reminder rows, a remove control for each row, and an Add another reminder action." src="assets/sketch-batch-light.jpg" width="560">
</picture>

</details>

```text
Use $sketch to explore batch reminder entry: one editable row per reminder,
with adding, removing, and pasting multiple lines.
```

[Download the example](https://raw.githubusercontent.com/marksummer/skills/main/examples/batch-reminders.html) and open it in your browser. It runs locally without a backend.

To iterate, ask to refine an element, compare approaches, or expand into a full screen.

## Tune Motion

Describe a component and tune its animation in chat before implementing it. Try easing and spring presets, drag the curve, and adjust values while the interaction loops. Copy the complete specification, including property mappings and reference code, into your AI tool.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/tune-motion-dark.jpg">
  <img alt="Tune Motion showing the accent picker, draggable motion curve, spring controls, and a live instruction with Copy." src="assets/tune-motion-light.jpg" width="560">
</picture>

```text
Use $tune-motion to show the accent picker expanding and collapsing
so I can tune its animation.
```

[Download the example](https://raw.githubusercontent.com/marksummer/skills/main/examples/accent-picker.html) and open it in your browser. [Skill instructions](tune-motion/SKILL.md).



---

Created by [Mark Summer](https://marksummer.com) · [Sketch instructions](sketch/SKILL.md) · [Clean Up instructions](clean-up/SKILL.md) · [Tune Motion instructions](tune-motion/SKILL.md) · [Check Design System instructions](check-design-system/SKILL.md)
