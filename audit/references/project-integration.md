# Project setup

Use these snippets when the user asks to adopt the audit. Keep the workflow in the installed skill, project design rules in `DESIGN.md`, and routing in the agent's instruction file. Provide the snippets; edit project files only when requested.

## DESIGN.md

Add this beside the existing design rules. Preserve token and component links and scoped exceptions.

```markdown
## Design-system verification

For UI reviews and before completing UI changes, use the
audit skill to audit the affected UI against this
document and the project's canonical tokens and components.

Report:
- Confirmed deviations and exact locations.
- Existing replacements and shared-source fixes.
- Exceptions, missing system support, and uncertainties.
- A before-and-after visual showing supported proposed fixes.
- What was inspected and what remains unverified.

Keep the audit read-only. Implement findings only when explicitly
requested. Clearly label proposed previews as unapplied.

If this document and the implementation disagree, report the
conflict rather than silently changing either one.
```

## AGENTS.md for Codex

Use paths relative to the instruction file, adjusting for monorepos and nested design documents. Preserve existing instructions and restrictions.

```markdown
Before UI work, read DESIGN.md when it exists.
Follow its Design-system verification section before finishing.
Use the installed audit skill for the audit.
If the skill is unavailable, report that limitation; do not claim
to have run it. Do not implement audit findings unless requested.
```

For other agents, use their documented instruction mechanism. Do not assume every tool reads `DESIGN.md` or understands Codex invocation syntax.

## Installation and scope

Install the skill before relying on its name. A mention in `DESIGN.md` does not install or register it.

In a Codex team repository, the skill can live at `.agents/skills/audit/SKILL.md`, with its sibling `references/` and `agents/` files. A personal installation can serve several projects. Follow the host's current installation and discovery guidance.

Keep routine checks scoped to affected UI and relevant shared definitions. Request a full-project audit when needed. A standalone project-audit request still uses the skill's full-project default. An instruction to audit before finishing does not authorize the fixes it finds.

For Framer, use the project's documented MCP guidance mechanism and permitted documentation access. Do not create an unsupported `DESIGN.md` code file or local mirror. If project guidance cannot expose the snippet, provide it for the user to add through a supported route.

If the user wants the complete workflow inside `DESIGN.md`, adapt the procedure into it. A short skill reference does not contain that workflow. Keep the installed skill and any maintained embedded copy synchronized.
