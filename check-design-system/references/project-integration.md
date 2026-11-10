# Ready-to-paste project integration

Use these snippets when the user asks how to adopt the audit in a project. Keep the reusable audit workflow in the installed skill, the project's design rules in `DESIGN.md`, and routing guidance in the agent's recognized instruction file. Provide the snippets without modifying project files unless the user requests those edits.

## Add to DESIGN.md

Place this section alongside the project's existing design rules. Preserve its token/component links and scoped exceptions.

```markdown
## Design-system verification

For UI reviews and before completing UI changes, use the
check-design-system skill to audit the affected UI against this
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

## Add to AGENTS.md for Codex

Use a path relative to the instruction file; adjust it for a monorepo or a nested design document. Preserve existing instructions and project restrictions.

```markdown
Before UI work, read DESIGN.md when it exists.
Follow its Design-system verification section before finishing.
Use the installed check-design-system skill for the audit.
If the skill is unavailable, report that limitation; do not claim
to have run it. Do not implement audit findings unless requested.
```

For another agent, put equivalent routing in its documented instruction mechanism; do not promise that every tool automatically reads `DESIGN.md` or recognizes Codex's invocation syntax.

## Availability and scope

Install the skill before relying on its name. A reference in `DESIGN.md` does not install/register the skill. For a Codex team repository, a project-owned skill may live at `.agents/skills/check-design-system/SKILL.md`, with its sibling `references/` and `agents/` files retained. A personal installation can serve multiple projects. Use the host's current skill installation/discovery guidance when giving setup instructions.

Keep everyday checks scoped to affected UI and relevant shared definitions; request a full-project audit explicitly when needed. The skill's full-project audit default still applies to a standalone request to audit the project. An instruction to audit before finishing does not authorize fixes discovered by that audit.

For Framer projects, use the project's documented MCP guidance mechanism and permitted documentation access. Do not create an unsupported `DESIGN.md` code file or a local mirror to simulate integration. If project guidance cannot expose the snippet, provide it for the user to add through an appropriate supported mechanism.

If the user asks for a self-contained workflow inside `DESIGN.md`, adapt the skill's procedure explicitly rather than claiming the short reference contains the full workflow. Keep the canonical skill and any embedded copy synchronized when both are maintained.
