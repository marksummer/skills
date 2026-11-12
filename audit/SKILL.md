---
name: audit
description: Audit UI against DESIGN.md and established tokens, components, variants, and native conventions in codebases or Framer MCP. Use to find design-system drift, hardcoded styles, or detached components. Report evidence, existing replacements, and coverage; implement fixes only when requested. Not a general redesign or design-system creation task.
---

# Audit

Trace the project's established design rules, shared definitions, and uses before judging UI. Similar appearance does not establish equivalent meaning or system membership.

Keep audits read-only unless fixes are explicitly requested. Do not edit source, configuration, assets, dependencies, or Framer state to inspect or illustrate a finding. Save reports and isolated previews only in authorized artifact locations; honor stricter no-write requests. An explicit implementation request authorizes routine fixes within that scope without asking again.

## Set the scope

- Follow user/repository instructions, project and branch restrictions, and required tools. Recent activity alone does not identify the target.
- Identify UI roots, application targets, packages, routes, theme files, and component libraries. Use `rg --files` and batch independent reads when available.
- Read applicable adapters: [iOS](references/ios.md), [other codebases](references/codebases.md), or [Framer MCP](references/framer.md). Mixed projects may need more than one.
- Read root and relevant package/app `DESIGN.md` files and follow their scoped references. If absent or inaccessible, use available owning definitions and state the limit. Do not create missing guidance or bypass Framer MCP to find a local mirror.
- For a full audit, inventory first-party UI definitions and uses. For changed-files requests, trace changed definitions to affected uses and name the narrower scope.
- Exclude generated output, vendor internals, caches, and unrelated code. Inspect third-party UI at its customization boundary. Separate previews, tests, examples, and inactive code from production UI.
- For an every-element request, complete accessible structural coverage. Track inaccessible files, nodes, variants, and computed styles; do not silently substitute a sample.

## Establish authority

Map documented rules, tokens, shared components, variants, themes, aliases, and approved exceptions. Record canonical names, owners, locations, and intended roles. Trace aliases to definitions.

Use this order of authority:

1. Current explicit user and project rules.
2. Designated system definitions and documentation.
3. Established shared implementations.
4. Inferred repeated patterns, which remain candidates.

Verify documentation against owning definitions. Surface unresolved conflicts instead of silently choosing a source or rewriting either side. Repetition does not turn a copied literal into an approved token.

If no established system exists, identify reusable conventions and system gaps. Do not invent tokens, replacements, or a compliance verdict.

## Classify each observation

Inspect shared definitions once, then trace caller overrides and contextual misuse. Check component membership, variants, semantic colors, typography, spacing, layout scales, radii, strokes, shadows, icons, motion, and relevant responsive/theme/platform branches where corresponding rules exist.

Use this decision order:

| Evidence | Classification |
| --- | --- |
| An applicable documented or user-approved exception permits the difference | Approved exception. Record its scope; do not turn it into a global exemption. |
| Missing access, unresolved source conflict, computed values, or runtime context prevents a conclusion | Unverified. Name the evidence needed to decide. |
| An established rule applies and the inspected implementation violates it | Confirmed drift. Cite both the implementation and the rule. |
| A valid reference or approved native convention is used in its intended role | Uses system. |
| A reusable need has no suitable established token or component | System gap. Missing support alone is not noncompliance. |
| Only similarity, repetition, or an inferred convention suggests inconsistency | Review candidate. Do not promote proximity to proof. |

A token can be used in the wrong role: a destructive color on neutral supporting text may violate a semantic rule despite correct reference membership. A literal can be valid for canonical definitions, layout constraints, artwork, image ratios, or computed geometry. Replace it only when an applicable rule supports that change.

Record exact file/line or Framer node/component ID, observed value or reference, rule location, confidence, affected uses, and an existing replacement whose semantics and API fit. Mark unknown replacements explicitly. A gap and an independent violation can coexist; do not count the same observation twice.

## Prioritize supported fixes

Rank confirmed findings by consequence and reach:

1. Misrepresented meaning, missing required state distinctions, or broken theme/accessibility behavior established by evidence.
2. Shared-definition drift affecting many uses.
3. Isolated visual inconsistencies covered by explicit rules.

Within a tier, prefer greater demonstrated reach and the smaller supported correction. Keep confidence separate from priority: a potentially serious candidate still needs evidence. Do not add general UX or accessibility findings without a design-system rule in scope.

Fix at the shared owner when its definition is wrong; fix the caller when an override or role is wrong. Explain which uses a shared correction reaches and which overrides remain. Deduplicate by cause while retaining affected locations.

## Verify and report

Inspect source first. Read existing lint/token validators before running them and verify they are read-only. Skip automatic fixes, snapshot updates, dependency changes, project-local generated output, installers, broad builds, and unrelated execution.

Render when the conclusion depends on appearance or behavior and tools are available; otherwise mark that aspect unverified. Source handling does not prove every runtime combination.

Follow [reporting and baseline comparison](references/reporting.md). Lead with inspected scope, canonical sources, confirmed groups and affected uses where known, then the highest-impact fixes. Keep clean results brief. Report coverage separately:

- Structural: inventoried targets, definitions, uses, exclusions, and unresolved areas.
- Visual: screens, sizes, themes, and states actually viewed, or none.
- Runtime: interactions actually exercised, or none.

Count only inventoried units and name them. Search hits are not an element count; a sample does not establish full coverage. Do not invent compliance percentages.

Include a before-and-after visual for confirmed findings with supported fixes using [visual comparison guidance](references/visual-comparison.md). Distinguish captures, source-based reconstructions, and proposed previews. Keep previews isolated; explain identical-looking semantic changes. Preview checks do not verify product behavior. If tools or no-write constraints prevent a visual, return the audit with that specific limit.

Save a detailed report when locations, later implementation, repeat audits, or the request justify one. Compare a baseline only after verifying comparable project, branch, scope, and rules; label findings not rechecked as unverified. State that an audit applied no fixes.

## Implement requested fixes

Check canonical definitions and APIs before replacing uses. Preserve content, behavior, accessibility, and deliberate exceptions. Implement supported fixes within scope; leave ambiguous candidates for review with reasons. Do not create a system to make the audit pass.

Run focused existing checks and inspect changed UI when possible. Use the available show-work skill for fresh screenshots of visible changes. Report verification and remaining limits. Publishing and deployment require explicit authorization.

For installation or workflow adoption, use [project integration guidance](references/project-integration.md). Edit project guidance only when requested; naming a skill does not install it or guarantee invocation.
