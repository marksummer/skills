<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Skills by Mark Summer — Faster exploration. Deliberate design." src="assets/header-light.svg" width="1200">
</picture>

A growing collection of agent skills for design and development. Starting with **Sketch**: small, interactive wireframes made to accelerate exploration while keeping design decisions deliberate.

[Install](#install) · [Sketch](#sketch) · [Example prompts](#example-prompts) · [About](#about)

## Install

```sh
npx skills add marksummer/skills
```

Run this in your project and choose **Codex**. The installer requires Node.js and lets you choose where to install the skill.

**Interactive previews require the Visualize plugin in Codex.** This command installs Sketch; Visualize is a separate dependency. Without it, the skill provides a concise layout outline.

## Sketch

Quick, interactive interface sketches. Focus on one element by default; expand to screens and flows when requested.

Sketch starts with the decision you need to make. It keeps the context needed to evaluate that decision, with realistic content, clear hierarchy, useful states, and relevant interactions. Its purpose is to reduce the work spent generating surrounding UI while preserving thoughtful design exploration.

### Example: batch reminder entry

**The design question:** Can someone enter and edit several reminders without losing track of them?

<picture>
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/sketch-batch-dark.jpg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/sketch-batch-light.jpg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/sketch-batch-dark.gif">
  <img alt="An eight-second walkthrough showing a reminder being added and typed, Enter creating the next row, a multiline list becoming two reminders, and an entry being removed." src="assets/sketch-batch-light.gif" width="560">
</picture>

An eight-second walkthrough of adding, typing, keyboard entry, multiline paste, and removal.

<details>
<summary>View a still preview</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sketch-batch-dark.jpg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sketch-batch-light.jpg">
  <img alt="A focused reminder-entry sketch with three editable reminder rows, a remove control for each row, and an Add another reminder action." src="assets/sketch-batch-light.jpg" width="560">
</picture>

</details>

This is a demonstration based on an existing feature in **Aside**, using the following prompt:

```text
Use $sketch to explore batch reminder entry: one editable row per reminder,
with adding, removing, and pasting multiple lines.
```

| Design decision | What the sketch makes possible |
| --- | --- |
| One reminder per row | Evaluate whether individual entries are easy to scan and correct. |
| Add, remove, and multiline paste | Try the core task with more than one way to enter reminders. |
| Keyboard behavior | Use Enter to move between rows or create the next one. |
| Focused scope | Keep attention on batch entry before exploring scheduling or navigation. |

**Try the interaction:** [open the standalone example](examples/batch-reminders.html), download the HTML file, and open it in your browser. You can edit rows, add and remove reminders, and paste multiple lines. The example runs locally without accounts or a backend.

### How it works

1. **Find the question.** Identify the element and the decision being explored.
2. **Keep useful context.** Include the labels, sample content, and behavior needed to judge the idea.
3. **Make it tangible.** Generate a low-fidelity sketch with the interactions that matter.
4. **Iterate at the same scope.** Refine that element, or ask to expand into a screen or flow.

Speed and efficiency are the intent. The amount saved depends on the task, scope, and tooling; this reminder example is a demonstration, not a benchmark.

[Read the skill instructions](sketch/SKILL.md) · [View Codex metadata](sketch/agents/openai.yaml)

## Example prompts

**Explore an element**

```text
Use $sketch to explore a compact way to show a reminder’s due date and time.
```

**Compare two approaches**

```text
Use $sketch to compare inline editing and a small edit sheet for a reminder row.
```

**Expand the context**

```text
Use $sketch to show the full reminder creation screen, including scheduling.
```

## About

Created by [Mark Summer](https://marksummer.com), a product designer exploring how reusable guidance can make AI-assisted design work more focused and useful.

Sketch builds on the Visualize plugin for rendering interactive previews. This repository contains the Sketch guidance and Codex metadata; Visualize is provided separately.
