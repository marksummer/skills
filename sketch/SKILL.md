---
name: sketch
description: "Explore an interface decision with a quick, interactive sketch. Use to try or compare layouts, interactions, or visual choices at the requested element, screen, or flow scope."
---

# Sketch

Build the smallest interactive sketch that helps the user make a design decision. Start with one element. Include a full screen or flow when requested.

## Set the scope

Use the request and conversation to identify the user, platform, and design question. Use the product context and references already available. Ask one focused question if a missing detail would change the structure; otherwise proceed and state any consequential assumptions.

Before building, complete internally: "This sketch helps decide ___." Include an element or interaction only when it helps answer that question or makes the example understandable. This keeps surrounding UI from competing with the decision.

Keep the chosen scope through revisions:

- For one element, show one direction with enough context to judge it. Keep relevant labels, sample content, platform conventions, and selection or feedback states.
- For a comparison, show the requested alternatives at the same scope.
- For a screen or flow, include the navigation, adjacent actions, and states needed to try the main task. An explicit request is enough; the user does not need to name a mode.

Leave out unrelated app chrome, settings, preview panels, and dismissal or reopening flows. Add them when they affect the decision. Omitting them from a sketch does not mean removing them from the product. An accent-picker layout usually needs color choices and selection feedback; an app preview helps when the question is how the accent looks in context.

A sketch request alone does not authorize product implementation or publication. Follow any requested deliverable format.

## Use Visualize

Find the installed `visualize:visualize` skill in the current catalog. Read its full instructions and UI mockup guidance before building or revising. Use its current product styling, checks, and inline response format. Keep presentation controls outside the depicted product.

If Visualize is unavailable, explain the dependency and provide a short outline. Only claim an interactive result when one was rendered.

## Compare what the user wants to decide

- Vary the property or set of choices named in the request. Keep the task, sample content, and other choices stable so the user can tell what caused the difference.
- For layout or interaction comparisons, change the relevant grouping, control placement, information visibility, or sequence. Use Visualize's variant carousel for structurally distinct alternatives unless the user requests simultaneous views.
- For a visual comparison on the same layout, keep one sketch and its interaction state. Switch between the requested values locally, or show paired swatches when context is unnecessary. For two accent palettes on a reminder picker, change the colors while keeping the labels, positions, and current selection fixed.

## Build the sketch

Use the product context already available. Avoid searching the project solely to make a mockup.

- Keep fidelity low so feedback stays on hierarchy and behavior. Use neutral colors and simple boundaries, while preserving distinctions needed to understand selection, errors, disabled controls, and focus. Keep color or imagery when it is part of the decision. Add decorative branding only when requested.
- Use plausible sample content and real action labels. Use placeholders for images and unknown content.
- Keep repeated editable items in a consistent row structure so people can scan and compare them. Place item actions beside the item they affect. Put information required for the current decision beside its control; reveal optional detail when requested. Adapt these defaults to explicit user choices and platform conventions.
- Make controls work locally when they help answer the question. Selection should change the visible state; forms should give plausible feedback. For flows, connect the requested screens and provide a way back. Keep simulated actions local and make their limits clear.
- Include empty, loading, error, or confirmation states when they affect the decision.
- Support the requested platform and narrow chat widths. Keep labels readable, controls keyboard accessible, and essential actions available without hover.

## Check and present

Read back the generated fragment. Perform the main action and confirm its visible result. For a comparison, switch alternatives and check that the shared choices and content still match. Exercise included navigation or recovery. Check keyboard access and narrow layouts. Fix broken controls, clipping, and unreadable states. Report checks you could not exercise.

Return the sketch with a short explanation only when a decision or consequential assumption needs it.

For revisions, preserve agreed choices and fidelity unless the user changes direction. Update the existing sketch when practical and return its updated visualization reference. Move to polished design or product implementation when requested.

## Example requests

- "Show an alternative accent picker."
- "Compare two ways to show the selected color."
- "Show two accent palettes on the same reminder picker. Keep the layout and behavior identical."
- "Show the complete iPhone reminder creation screen."
- "Sketch onboarding with working next and back buttons."
