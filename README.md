# Skills by Mark Summer

Reusable agent skills for design and development.

## Install

```sh
npx skills add marksummer/skills
```

Run the command in your project and choose Codex. The installer requires Node.js and lets you choose the installation scope.

## Sketch

Quick, interactive interface sketches. Focus on one element by default; expand to screens and flows when requested.

Sketch starts with a design question and generates only the interface needed to explore it. Its guidance keeps hierarchy, realistic content, meaningful feedback, and keyboard behavior central to the exploration.

### Requirement

Sketch is designed for Codex with the **Visualize plugin** enabled. The command installs Sketch; it does not install Visualize. Without Visualize, Sketch provides a concise layout outline instead of an interactive preview.

### Try it

```text
Use $sketch to explore batch reminder entry: one editable row per reminder,
with adding, removing, and pasting multiple lines.
```

Focused exploration is the default. Ask for a full screen or flow when you need more context:

```text
Use $sketch to show the complete reminder creation screen.
```

### Files

- [Skill instructions](sketch/SKILL.md)
- [Codex metadata](sketch/agents/openai.yaml)

## About

Created by [Mark Summer](https://marksummer.com).
