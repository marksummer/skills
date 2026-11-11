# Framer audit

## Open the target

Use Framer MCP and discover its available tools. Open the selected project and branch with `open_project`, or reuse a session verified for that exact target. Read the returned README, then `context.md` and applicable documentation for trees, styles, tokens, components, variants, code, and rendering.

Verify project and branch identity from session data before traversal or changes. Follow workspace defaults and protected-project restrictions. Recently opened projects do not establish authorization. If the target is unknown, ask for its link while continuing independent work.

Use current MCP documentation for APIs and properties. Do not fall back to `@framer/agent`, its CLI, or its Framer skills. Report missing read capabilities.

## Inventory the project

Use documented read APIs to list pages, reachable layers, breakpoints, components, variants, shared styles and variables, and code components or overrides. Include hidden and conditional layers when readable. Distinguish definitions, instances, and overrides; count each shared definition once.

Batch supported reads, complete pagination, and track stable IDs and visited definitions. Fetch details around suspicious properties and override boundaries instead of repeating full-project dumps. Do not generate or execute writes during an audit.

## Inspect the UI

- Use reference metadata to establish links to shared styles, variables, and components.
- Distinguish allowed property controls from unsupported overrides. Identical-looking standalone layers are duplication candidates; appearance alone does not prove detachment.
- Compare exposed typography, fills, strokes, radii, effects, spacing, layout, and motion with the system.
- Check breakpoint and variant overrides before making cross-state claims.
- Read code components and overrides through MCP when supported. Trace project-owned references and prop overrides using codebase reasoning. Keep access through MCP.
- If only resolved colors or fonts are exposed, mark reference linkage unverified and explain which comparisons remain possible.
- Respect artwork, CMS content, responsive geometry, and exceptions. Inspect CMS templates structurally; claim individual page coverage only for pages enumerated and inspected.

## Verify findings

Locate findings by page and stable node/component ID. Add layer paths and source locations when available. List inaccessible internals, variants, styles, and files.

Use documented MCP rendering and image capabilities. Report the pages, sizes, themes, and states viewed. Canvas images do not prove reference bindings; tree reads do not prove hover, focus, navigation, or mobile behavior.

For requested fixes, use documented mutations and preserve links, bindings, interactions, and property controls. Re-read affected references and render focused checks when possible. Saved edits are unpublished until a publish action. Publish only with explicit authorization.
