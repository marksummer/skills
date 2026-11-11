# Visual comparisons

Include a before-and-after comparison when confirmed findings have supported fixes. Keep the audited project read-only unless implementation was explicitly requested. A preview does not authorize changes.

## Choose the states

- Tie each comparison to a finding ID, exact source or node, established rule, and existing replacement. Reuse the audit evidence.
- Show the state that exposes the issue. Match content, viewport or device, state, theme, and accent so only the proposed fix differs.
- Cover confirmed groups with supported replacements. For many groups, use a compact picker or show the highest-impact examples and name the omitted groups. Group repeated instances.
- Preserve exceptions and surrounding layout. Keep redesign and invented content outside the audit.
- Leave unresolved source conflicts and system gaps out of confirmed-fix views. If alternatives are requested, label them as review options.

## Label the evidence

Use visible labels that explain where each view came from:

| Label | Meaning |
| --- | --- |
| Current: captured | A fresh capture of the inspected project state. |
| Current: source-based | A reconstruction from inspected source or properties. Preserve values and identify assumptions. |
| Proposed: preview | An isolated rendering or illustration of a supported change, not applied to the project. |
| Implemented: captured | A fresh capture after explicitly requested implementation. |

Do not present mockups, generated images, reconstructions, or CSS/DOM simulations as product screenshots. A collapsed or idle capture does not verify an expanded or hover state. State rendering limits instead of claiming pixel accuracy. Previews do not establish runtime, accessibility, or device behavior.

## Build without editing the project

For the current view, use running UI and documented read-only capture APIs when available.

In Framer, use documented MCP capture parameters. Do not change preview controls, add nodes, edit code, switch branches, or publish to get an image. For iOS and other codebases, use existing captures or running UI without changing source, configuration, dependencies, or tracked/generated project files.

Build the proposed view in an isolated report preview from minimal copied snippets and inspected design-system values. Do not patch the project's source or DOM, even temporarily. Avoid running arbitrary application code to create an illustration. A copied snippet does not verify the product runtime.

Use the available visualize skill for an inline responsive comparison, following its current instructions. Authorized local rendering or image-presentation tools are alternatives. Preserve project type, colors, and content; avoid AI-generated UI screenshots for precise comparisons. Do not install dependencies, upload project material, or publish solely to meet the visual requirement.

Save report artifacts in an authorized task-owned location. Prefer the chat visualization directory, then the workspace artifact convention. Keep preview components out of the audited app and Framer project.

For a strict no-write request, use available captures or an artifact-free comparison when supported. Otherwise state the limit and return the text audit.

## Show appearances and invisible changes

Show matching light and dark views when supported. An appearance selector may change only the isolated preview. Match the inspected palette and label assumed accent choices. Do not invent an unsupported dark theme. Label source-based dark views as previews; they do not verify the product's theme switcher.

For changes with identical appearance, preserve both views and add a short semantic, binding, or accessibility-tree annotation. For example: `h1` to `p`, same 15px styling. Do not invent a visual difference or claim a screen-reader announcement without testing.

Use side-by-side views when readable and stack them on narrow screens. Keep copy at its actual scale, essential controls available without hover, and labels clear. Include only controls that help assess the finding.

## Check and present

When tools permit, inspect interactions, labels, type, narrow-width fit, and supported appearances. Otherwise use non-mutating markup and state checks and disclose rendering limits. Follow tool and security restrictions.

Embed the visual beside the findings in the final response. Name captured and source-based states and remaining unknowns. Report preview checks separately from product verification. State that no project fixes were applied. If no supported fixes exist, omit the comparison and say so.
