---
name: check-design-system
description: Audit design-system use against DESIGN.md when present and canonical project definitions across iOS apps (SwiftUI/UIKit), other codebases, and Framer projects through Framer MCP. Use to check every UI element, find hardcoded styles or detached components, audit tokens and variants, or detect design-system drift. Report a concise summary, prioritized findings, a before-and-after visual preview, existing replacements, exceptions, coverage, and changes since a comparable prior audit; fix only when requested. Not a general redesign or a request to invent a design system.
---

# Check Design System

Trace shared definitions and their usages to audit quickly. Establish the project's actual design system before judging UI. Keep every audit read-only unless the user explicitly asks to implement fixes. Do not edit source, configuration, assets, dependencies, or Framer state during an audit. Audit reports, captures, and isolated visual previews are output artifacts only; save them in authorized artifact locations without editing the audited project. Honor stricter no-write requests. Honor explicit implementation requests without asking again for routine authorized changes.

## 1. Establish target and inventory

- Follow user and repository instructions, project/branch restrictions, and tool requirements. Never select a project from recent activity alone.
- Identify UI roots, application targets, source packages, pages/routes, theme files, component libraries, and relevant documentation. Use `rg --files` and batch independent source reads when available.
- Load only applicable adapters: [iOS](references/ios.md), [other codebases](references/codebases.md), [Framer MCP](references/framer.md). Load multiple adapters for mixed projects.
- Read `DESIGN.md` when present at the selected project root or within relevant application/package directories before inferring design rules. Respect each document's stated scope and follow applicable references to canonical tokens/components. Use the platform's permitted project tools; do not bypass Framer MCP restrictions to find a local mirror. If the document is absent or inaccessible, continue with available documentation/definitions and state the limitation without inventing its contents or creating it.
- Default to a full first-party structural scan: enumerate UI definitions and usages, then investigate shared causes. For changed-files requests, trace changed definitions to affected usages and label the narrower scope.
- Exclude generated output, vendor internals, build caches, and unrelated code. Inspect third-party components at the project's usage/customization boundary. Separate previews, tests, examples, and inactive code from production UI.
- Do not silently substitute a sample for an every-element request. Complete accessible structural coverage and track inaccessible or unresolved files, nodes, variants, and computed styles.

## 2. Build the system map

Find explicit documentation, token definitions, shared components, styles, variants, theme mappings, and approved exceptions. Record canonical names, locations, intended roles, and aliases. Trace aliases to their owners.

Use authority in this order: current explicit user/project rules; designated system definitions and documentation; established shared implementations; inferred repeated patterns. Surface conflicts between authoritative sources. Treat inferred patterns as candidates, never binding rules. A frequently copied literal is not proof of an approved token.

Treat `DESIGN.md` as design guidance, and verify its claims against the owning definitions. Report discrepancies between the document and actual tokens/components as source-of-truth conflicts; do not silently rewrite either side or assume a copied literal is approved. Follow explicit user/repository precedence and surface unresolved conflicts between scoped design documents.

If no established system exists, say so. Identify reusable conventions and consolidation candidates, but do not invent tokens, components, or a compliance verdict.

## 3. Inspect definitions and usages

Check these where corresponding rules exist:

- Component membership, variants, wrappers, detached copies, and per-instance overrides.
- Semantic colors, typography, spacing, layout scales, radii, strokes, shadows, icon families/sizes, motion, and interactive states.
- Responsive, appearance, accessibility, and platform-specific source branches.
- Correct role as well as provenance: an approved destructive color used for neutral supporting text can still violate documented rules.

Inspect shared definitions once; trace usages for overrides and contextual misuse. Group repeated instances by root cause and retain affected locations. Inspect conditional branches and variant definitions without claiming every runtime combination was exercised.

Classify outcomes:

| Outcome | Evidence |
| --- | --- |
| Uses system | Reference or approved native convention matches its intended role |
| Confirmed drift | Established rule is violated or a required shared definition is bypassed |
| Review candidate | Possible duplicate, near match, inferred inconsistency, or unclear role |
| System gap | A needed reusable pattern has no suitable established component/token; not itself a violation |
| Approved exception | Applicable documented/user-approved reason permits the difference |
| Unverified | Access, dynamic values, missing definitions, or runtime context prevents a conclusion |

Do not flag every literal. Layout constraints, image ratios, computed geometry, and unique artwork may be legitimate. Do not round to the nearest scale value without a project rule supporting that relationship. Visual equality does not establish reference membership or interchangeable semantics. Respect projects that explicitly allow literal values from a documented scale.

For each finding, capture the precise file/line or Framer node/component ID, observed implementation, applicable system rule and its location, confidence, affected usages, and a concrete existing replacement when supported. Mark the replacement unknown when none can be established. Distinguish confirmed drift from missing system support; never invent a replacement or count a system gap as noncompliance. Identify whether the smallest supported fix belongs in a shared definition or at individual usage sites, and explain its reach without counting overlapping usages twice.

## 4. Verify and report

Use relevant existing lint/token validators only in a verified read-only mode. Read scripts before running them; skip mutating checks, automatic fixes, snapshot updates, dependency changes, and project-local generated output during an audit. Avoid installers, new dependencies, broad builds, and execution unrelated to the audit. Use static inspection first. Render when diagnosis depends on appearance/behavior and tooling is available; otherwise mark that aspect unverified.

Report coverage separately:

- Structural: targets/files/pages included and excluded, definitions/usages inspected, and unresolved areas.
- Visual: exact screens, sizes, themes, and states actually viewed, or explicitly none.
- Runtime: interactions actually exercised, or explicitly none.

Count only inventoried units and name the unit: source occurrences, component usages, or Framer nodes. Never turn grep hits into an element count, infer full coverage from a sample, or invent a compliance percentage. Keep grouped locations in a workspace-local artifact if needed; do not write outside the authorized workspace.

Use [the report format and comparison rules](references/reporting.md). Lead with a concise summary of inspected scope, grouped issue counts and affected usages where known, and the highest-impact fixes. Include exact locations behind each finding; distinguish shared-source fixes, per-usage fixes, and system gaps. Separate candidates, exceptions, and unknowns from confirmed issues. Report structural, visual, and runtime coverage and state that no fixes were applied.

Include a before-and-after visual comparison by default for confirmed findings with supported fixes. Follow [visual comparison guidance](references/visual-comparison.md): distinguish captured current UI from source-based reconstructions and proposed previews, show light/dark appearances when supported, and explain semantic changes that look identical. Never alter the audited project, even temporarily, to produce an after view. Keep preview coverage separate from verified product behavior.

Save a detailed local report when useful for numerous locations, a later implementation pass, user-requested reporting, or repeat audits. Follow the workspace's artifact convention and link the result. Do not save an artifact for a strict no-write request. Compare against a prior report only when the project/branch identity and scope are comparable; show new, resolved, and remaining findings, with unverified status for anything not rechecked. If no usable baseline exists, say so. Never fabricate a trend, compliance score, or percentage.

Keep clean results brief rather than listing every passing element. Prioritize shared causes and semantic misuse over isolated cosmetic differences.

## 5. Fix within the requested scope

When requested, use established tokens/components and preserve content, behavior, accessibility, and deliberate exceptions. Verify canonical definitions and component APIs before replacing usages. Apply supported changes; leave ambiguous candidates for review with reasons. Do not create a design system to make the audit pass.

Run focused existing checks appropriate to the changes and inspect changed UI where tooling permits. Use the available show-work skill for fresh screenshots of visible changes. Report changes, verification, and remaining limits. Never publish or deploy without explicit authorization.

## Project integration

For installation, adoption, or requests to make this audit part of a project's workflow, provide the ready-to-paste [DESIGN.md and AGENTS.md snippets](references/project-integration.md). Keep integration guidance separate from routine audit findings. Do not edit project guidance files during an audit or add these snippets automatically; modify them only when the user requests that project change. Referencing the skill does not install it or guarantee invocation by every agent.
