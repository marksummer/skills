---
name: check-design-system
description: Audit design-system use against DESIGN.md when present and canonical project definitions across iOS apps (SwiftUI/UIKit), other codebases, and Framer projects through Framer MCP. Use to check every UI element, find hardcoded styles or detached components, audit tokens and variants, or detect design-system drift. Report a concise summary, prioritized findings, a before-and-after visual preview, existing replacements, exceptions, coverage, and changes since a comparable prior audit; fix only when requested. Not a general redesign or a request to invent a design system.
---

# Check design system

Check UI against the project's established design system. Trace shared definitions and their uses before judging an element.

Keep audits read-only unless the user explicitly requests fixes. Do not change source, configuration, assets, dependencies, or Framer state. Save reports, captures, and isolated previews only in authorized artifact locations, outside the audited project code. Follow stricter no-write requests. An explicit implementation request authorizes routine changes within that scope without asking again.

## Set the scope

- Follow user and repository instructions, project and branch restrictions, and required tools. Recent activity alone does not identify the target.
- Identify UI roots, application targets, packages, routes, theme files, component libraries, and relevant documentation. Use `rg --files` and batch independent reads when available.
- Read the relevant adapters: [iOS](references/ios.md), [other codebases](references/codebases.md), or [Framer MCP](references/framer.md). Mixed projects may need more than one.
- Read `DESIGN.md` at the project root and in relevant app or package directories. Follow its scope and references to canonical definitions. Use permitted project tools; do not bypass Framer MCP to find a local mirror. If documentation is absent or inaccessible, use available definitions and state the limit. Do not invent or create the missing document.
- For a full audit, inventory first-party UI definitions and uses, then investigate shared causes. For a changed-files request, trace changed definitions to affected uses and name that narrower scope.
- Exclude generated output, vendor internals, caches, and unrelated code. Inspect third-party components at the project's customization boundary. Keep previews, tests, examples, and inactive code separate from production UI.
- For an every-element request, complete accessible structural coverage. Track inaccessible files, nodes, variants, and computed styles instead of silently substituting a sample.

## Establish the design system

Map the documented rules, tokens, shared components, styles, variants, themes, aliases, and approved exceptions. Record canonical names, owners, locations, and intended roles. Trace aliases to their definitions.

Use this order of authority:

1. Current explicit user and project rules.
2. Designated system definitions and documentation.
3. Established shared implementations.
4. Inferred repeated patterns.

Report conflicts between authoritative sources. Repetition alone does not make a literal an approved token, and inferred conventions remain candidates.

Check `DESIGN.md` against the owning definitions. Report disagreements as source-of-truth conflicts; do not silently rewrite either source. Follow explicit precedence rules and surface unresolved conflicts between scoped documents.

If no established system exists, say so. Identify reusable conventions and consolidation candidates without inventing tokens, components, or a compliance verdict.

## Inspect definitions and uses

Where project rules exist, check:

- Component membership, variants, wrappers, detached copies, and instance overrides.
- Semantic colors, type, spacing, layout scales, radii, strokes, shadows, icon families and sizes, motion, and interaction states.
- Responsive, appearance, accessibility, and platform-specific source branches.
- Intended roles. An approved destructive color can still be wrong for neutral supporting text.

Inspect shared definitions once, then trace overrides and contextual misuse. Group instances by cause and retain affected locations. Inspect conditions and variants without claiming to have exercised every runtime combination.

| Outcome | Evidence |
| --- | --- |
| Uses system | A reference or approved native convention matches its intended role. |
| Confirmed drift | An established rule is violated or a required shared definition is bypassed. |
| Review candidate | A possible duplicate, near match, inferred inconsistency, or unclear role needs review. |
| System gap | A reusable pattern has no suitable established component or token. This alone is not a violation. |
| Approved exception | A documented or user-approved reason permits the difference. |
| Unverified | Access, dynamic values, missing definitions, or runtime context prevents a conclusion. |

Literal values can be valid for layout constraints, image ratios, computed geometry, or artwork. Round to a scale only when project rules support it. Matching appearance does not prove reference membership or equivalent semantics. Respect documented permission to use literal scale values.

For each finding, record the exact file and line or Framer node/component ID, observed implementation, applicable rule and its location, confidence, affected uses, and an existing replacement where supported. Mark unknown replacements explicitly. Keep gaps separate from noncompliance.

Identify the smallest supported fix: a shared definition or individual uses. Explain its reach and avoid counting overlapping uses twice.

## Verify and report

Inspect source first. Read existing lint or token-validator scripts before using them and verify that they are read-only. Skip mutating checks, automatic fixes, snapshot updates, dependency changes, and project-local generated output. Avoid installers, new dependencies, broad builds, and unrelated execution.

Render when a finding depends on appearance or behavior and tools are available. Otherwise mark that aspect unverified.

Report coverage separately:

- Structural: included and excluded targets, files, or pages; definitions and uses inspected; unresolved areas.
- Visual: the screens, sizes, themes, and states actually viewed, or none.
- Runtime: the interactions actually exercised, or none.

Count inventoried units and name them, such as source occurrences, component uses, or Framer nodes. Search hits are not an element count. A sample does not establish full coverage. Do not invent compliance percentages. Keep grouped locations in an authorized workspace artifact when needed.

Follow [the report and comparison guidance](references/reporting.md). Lead with scope, grouped issue counts and affected uses where known, and the highest-impact fixes. Give exact locations. Separate shared fixes, individual fixes, gaps, candidates, exceptions, and unknowns. State that the audit applied no fixes.

Include a before-and-after visual for confirmed findings with supported fixes, following [visual comparison guidance](references/visual-comparison.md). Label actual captures, source-based reconstructions, and proposed previews. Show supported light and dark appearances, and explain changes that look identical. Never alter the audited project, even temporarily, to create an after view. Preview coverage does not verify product behavior.

Save a detailed report when locations, later implementation, repeat audits, or the user's request justify one. Follow the workspace artifact convention and link it. Honor strict no-write requests.

Compare a previous audit only when project, branch, and scope are comparable. Report new, resolved, and remaining findings; mark anything not rechecked as unverified. If no usable baseline exists, say so. Do not invent trends or scores.

Keep clean results brief. Prioritize shared causes and semantic misuse over isolated cosmetic differences.

## Implement requested fixes

When asked, use established tokens and components while preserving content, behavior, accessibility, and deliberate exceptions. Check canonical definitions and component APIs before replacements. Apply supported fixes and leave ambiguous candidates for review with reasons. Do not create a design system to make an audit pass.

Run focused existing checks and inspect changed UI when tools permit. Use the available show-work skill for fresh screenshots of visible changes. Report changes, verification, and remaining limits. Publishing and deployment require explicit authorization.

## Project setup

For installation or workflow adoption, provide the [DESIGN.md and AGENTS.md snippets](references/project-integration.md). Keep setup advice separate from routine findings. Edit project guidance only when requested. Naming the skill does not install it or guarantee invocation by every agent.
