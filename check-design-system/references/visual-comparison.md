# Default before-and-after comparison

Include a useful visual comparison with the audit summary whenever confirmed findings have supported proposed fixes. Keep the audited project read-only unless the user explicitly asks to implement fixes. The preview is part of the report, not permission to apply it.

## Choose representative states

- Map each comparison to a finding ID, exact source/node location, established rule, and existing replacement. Reuse the audit's evidence instead of rescanning unrelated UI.
- Show the actual state that exposes the issue: feedback text, expanded prose, an overridden component, or the affected breakpoint. Match content, viewport/device, state, theme, and accent across both sides so only the proposed fix differs.
- Cover the confirmed groups with supported replacements. For many groups, use a compact picker or show the highest-impact examples and explicitly identify groups omitted from the visual. Group repeated instances rather than drawing the same issue repeatedly.
- Preserve intentional exceptions and surrounding layout. Do not turn a token/component audit into a redesign or invent missing content to fill a screen.
- Keep unresolved source-of-truth conflicts and system gaps out of the proposed-fix view. If the user asks to compare alternatives for them, label those views as review options, not confirmed corrections.

## Label evidence honestly

Distinguish these views visibly:

- **Current — captured:** a fresh capture of the actual inspected project state.
- **Current — source-based:** a reconstruction from inspected source/properties when the relevant state cannot be captured read-only. Preserve actual values and identify assumptions.
- **Proposed — preview:** an isolated rendering or illustration of the supported change; it has not been applied to the project.
- **Implemented — captured:** use only after an explicit implementation request and a fresh capture of the changed product.

Never present a mockup, generated image, reconstructed state, or CSS/DOM simulation as a product screenshot. A capture of the collapsed or idle state is not evidence of the expanded or hover state. If exact rendering cannot be established, say so instead of implying pixel accuracy. Do not claim runtime, accessibility, or device validation from a preview.

## Produce the comparison without project edits

Prefer existing running UI and documented read-only screenshot APIs for the current side. For Framer, use MCP capture parameters where documented; do not change instance preview controls, add nodes, edit code, switch branches, or publish merely to obtain a visual. For iOS and codebases, use available existing captures or running UI without modifying sources, configuration, dependencies, or tracked/generated project files.

Create the proposed side in an isolated report preview using copied, minimal UI snippets and the inspected design-system values. Do not patch the real project's source or DOM, even temporarily or with an intent to revert. Avoid executing arbitrary application code merely to make an illustration. Reading project code into a separate illustrative snippet does not verify that product's runtime.

Use the available visualize skill for an inline, responsive comparison and follow its current instructions. Use authorized local rendering or image-presentation tools as an alternative when appropriate. Keep project typography, colors, and content inside the preview; avoid AI-generated text/UI screenshots for precise comparisons. Do not install dependencies, upload project material, or publish a preview just to satisfy this output requirement.

Save only report artifacts in an explicitly authorized task-owned location: prefer the thread visualization directory for inline previews, otherwise the workspace's artifact convention. Do not place preview components inside the audited app or Framer project. Respect a stricter request for no filesystem writes: use already available captures or an artifact-free comparison if supported; otherwise explain the limitation without blocking the textual audit.

## Show appearances and invisible changes

Show matching light and dark views when the project supports them. A local appearance selector may switch only the isolated preview. Match the inspected palette; if an accent choice is assumed, label it. Do not invent a dark theme for a single-appearance product. Source-based dark previews must be labeled as previews, not proof that the product's theme switcher works.

For semantic or structural fixes with identical appearance, preserve the visible design on both sides and add a concise document-role, component-binding, or accessibility-tree annotation. For example: `h1` to `p`, same 15px styling. Do not manufacture a visual difference or claim a particular screen-reader announcement without testing it.

Use side-by-side views where readable and stack them on narrow screens. Keep copy at its actual scale, essential controls accessible without hover, and labels clear. Include only comparison controls that help evaluate the finding; avoid a new dashboard or decorative scorecards.

## Verify and deliver

Inspect the generated comparison when rendering tools are available. Check primary interactions, labels, typography, narrow-width fit, and supported appearances. Verify markup/state logic with non-mutating checks when rendering is unavailable; disclose material rendering limits rather than claiming visual verification. Do not bypass tool/security restrictions to obtain a capture.

Embed the visual in the final response alongside the concise findings. Identify which states were actually captured, which are source-based, and what remains unverified. Keep product verification separate from preview checks in coverage. State that no project fixes were applied. If there are no supported proposed fixes, report that directly rather than fabricating before-and-after panels.
