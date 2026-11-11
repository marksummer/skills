# Audit

Find where an interface has drifted from the project's shared tokens, components, and design rules. Works with iOS apps, other codebases, and Framer projects.

## Install

Follow the [installation steps](../README.md#install) and choose Audit.

Framer audits require a connected Framer MCP. Visual comparisons use the capture and rendering tools available in your environment; the audit reports any limits.

## Use

```text
Use $audit to audit this project. Keep it read-only.
```

Point it at the project or name the screens and files you want checked. It reads `DESIGN.md` when available and checks the rules against the definitions the project actually uses.

## What you get

A short summary with prioritized findings, exact locations, and existing replacements where supported. Repeated issues are grouped by cause. The report separates confirmed drift from review candidates, system gaps, and approved exceptions.

Supported fixes include a before-and-after preview when tools permit. Coverage states what was inspected in source, viewed, and exercised. A comparable earlier audit can show what is new, resolved, or still present.

Audits leave the project unchanged. Ask explicitly to implement fixes.

## Project setup

Use the [project integration snippets](references/project-integration.md) to add audit guidance to `DESIGN.md` and `AGENTS.md`.

[Instructions](SKILL.md) · [All skills](../README.md)
