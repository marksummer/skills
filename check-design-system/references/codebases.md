# Codebase audit

## Find the system

Identify the language, framework, UI roots, workspace boundaries, routes, theme providers, and shared component APIs. Read manifests and local instructions. Treat monorepo applications separately when their systems differ.

Find style sources such as CSS variables, Sass maps, token JSON, theme objects, utility-framework configuration, CSS-in-JS, component libraries, and native resource dictionaries. Trace aliases, imports, re-exports, inheritance, and overrides as access permits.

For unfamiliar frameworks, use project conventions and available primary documentation. Apply each stack's rules and report limits on framework coverage.

## Inspect the UI

- For web UI, inspect relevant templates/JSX, CSS modules, stylesheets, inline styles, utility classes, pseudo-elements, state selectors, responsive queries, and portal roots.
- Check utility-framework values and approved arbitrary-value exceptions against project rules. `text-sm` may reference the system; `text-[#777]` needs context.
- For React Native, inspect theme hooks and providers, stylesheets, inline overrides, dynamic colors, platform branches, and shared primitives. Accept documented native defaults.
- For other native stacks, trace themes, resources, controls, inheritance, and layouts in their own formats.
- Treat copied components as candidates until source evidence establishes equivalent meaning and behavior. Appearance alone does not justify a replacement.
- Check per-instance props, styles, and context as well as base definitions. Compare variants and states with the public component API.
- Accept literals in canonical token definitions; those definitions need concrete values.

Use search to inventory candidates, then read their context before confirming findings. Record unresolved imports, computed styles, server data, and generated templates as coverage limits.

## Verify findings

Use relevant existing lint rules, type checks, and token validators. A routine audit does not need a new scanner dependency. Give source locations and the canonical definition behind each recommendation.

Inspect representative rendered states when appearance determines the finding. Report visual checks separately from source coverage.

For authorized fixes, check APIs and preserve events, focus, accessible names, layout intent, and responsive behavior. Numeric or color proximity alone does not justify replacing a value with a token.
