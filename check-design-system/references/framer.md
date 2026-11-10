# Framer MCP adapter

## Open the authorized target

Use Framer MCP. Discover its currently available tools. Open the explicitly selected project/branch with `open_project`, or reuse a session already verified for that exact target. Read the returned README, then `context.md` and listed documentation applicable to tree traversal, styles/tokens, components/variants, code files, and any needed rendering capability.

Verify project identity and branch from session/project data before traversal or changes. Follow user/workspace defaults and protected-project restrictions; never infer authorization from recently opened projects. If no target is established, ask for the project link while continuing independent work.

Do not use `@framer/agent`, its CLI, or its Framer skills as a fallback. Do not guess APIs or property names; use current MCP documentation. Report access limits if a required read capability is unavailable.

## Inventory

Use documented read APIs to inventory pages, reachable layer trees, breakpoints, components, variants, shared styles/variables, and code components/overrides. Include hidden/conditional layers where readable. Distinguish definitions, instances, and overrides. Do not count a shared component's internal definition repeatedly as separate definitions.

Batch reads where supported and complete pagination. Track stable IDs and visited definitions. Avoid repeated full-project dumps; retrieve details at suspicious properties and override boundaries. Do not generate or execute writes during an audit.

## Inspect

- Establish linkage to shared styles, variables, and components from reference metadata where available.
- Distinguish allowed property controls from unsupported overrides. Treat identical-looking standalone layers as duplication candidates, not proof of detachment.
- Compare typography, fills, strokes, radii, effects, spacing, layout, and motion against the system when exposed.
- Inspect breakpoint and variant overrides before claiming cross-state conformance.
- Read code components/overrides through MCP where supported. Trace project-owned references and prop overrides using codebase reasoning; do not switch to a separate Framer CLI.
- Never infer reference membership from resolved colors/fonts alone. If MCP exposes resolved values only, mark linkage unverified and state what can still be compared.
- Respect unique artwork, CMS-bound content, responsive geometry, and exceptions. Inspect CMS templates structurally; claim individual CMS-page coverage only for pages actually enumerated and inspected.

## Verify

Locate findings with page names and stable node/component IDs, adding layer paths/source locations where supported. List inaccessible internals, variants, styles, and files.

Use MCP rendering/image capabilities only as documented. Report the exact pages, sizes, themes, and states viewed. Canvas images cannot prove shared-reference binding; tree reads cannot prove hover, focus, navigation, or mobile behavior.

For requested fixes, use documented MCP mutations and preserve links, bindings, interactions, and property controls. Re-read affected references and render focused checks where possible. Saved edits are not publication; publish only with explicit user authorization.
