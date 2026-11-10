# Codebase adapter

## Discover

Identify the language/framework, UI roots, workspace boundaries, route/screen definitions, theme providers, and shared component interfaces. Read manifests and local instructions. Treat monorepo applications separately when their systems differ.

Find CSS variables, Sass maps, token JSON, theme objects, utility-framework configuration, CSS-in-JS, component libraries, native resource dictionaries, and other framework-specific style sources. Trace aliases, imports, re-exports, inheritance, and overrides as source access permits.

For unfamiliar frameworks, follow project conventions and available primary documentation. Do not apply web rules to every stack or claim exhaustive framework support.

## Inspect

- For web UI, include templates/JSX, CSS modules, stylesheets, inline styles, utility classes, pseudo-elements, state selectors, responsive queries, and portal roots where relevant.
- Distinguish configured utility-framework values and approved arbitrary-value exceptions. A class such as `text-sm` may be a system reference; `text-[#777]` needs evidence about project rules and intent.
- For React Native, inspect theme hooks/providers, stylesheets, inline overrides, dynamic colors, platform branches, and shared primitives. Accept documented native defaults.
- For other native stacks, trace themes/resources, controls, style inheritance, and layout resources in their actual formats.
- Treat possible copied components as candidates until source evidence supports equivalent semantics and behavior. Matching appearance alone is insufficient for replacement.
- Trace per-instance props/styles and context as well as base definitions. Check variants and states against the public component contract.
- Do not flag literal values inside canonical token definitions merely because they are literals; concrete values must originate somewhere.

Use search to inventory candidates, then read context to confirm findings. Identify unresolved imports, computed styles, server data, or generated templates as coverage boundaries.

## Verify

Prefer relevant existing lint rules, type checks, and token validators. Do not introduce a scanner dependency for a routine audit. Cite source locations and the canonical definition supporting each recommendation.

Inspect representative rendered states when appearance determines the finding. Report visual verification separately from source-wide coverage.

For authorized fixes, check APIs and preserve events, focus, accessible names, layout intent, and responsive behavior. Do not replace values solely because their numeric/color distance to a token is small.
