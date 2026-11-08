---
name: sketch
description: "Quick, interactive interface sketches. Focus on one element by default; expand to screens and flows when requested."
---

# Sketch

Turn the user's idea into the smallest sketch that helps them make a design decision. Default to focused mode; use fuller mode when the user asks for a screen or flow.

## Use Visualize

This skill depends on the installed `visualize:visualize` skill from the Visualize plugin. Find it in the current skill catalog and read its complete `SKILL.md` before creating or changing a sketch. Follow its current output contract and UI mockup guidance; read its referenced mockup and variant guidance when applicable. Resolve its location from the catalog rather than hardcoding a plugin version or copying its runtime instructions here.

If Visualize is unavailable, explain the missing dependency and provide a concise layout outline; do not claim to have rendered an interactive sketch.

## Choose the scope

### Focused mode — default

- Identify the one element and design question being refined. Render one direction with only the surrounding context needed to judge it.
- Keep relevant labels, sample content, platform conventions, and selection or feedback states. Add interaction only when it helps answer the question.
- Omit unrelated app chrome, navigation, preview panels, settings pages, dismissal/reopening flows, and extra states unless they affect that decision. Reduce the scope of the sketch, without implying those features should be removed from the product.
- Do not automatically generate alternatives or a complete journey. A comparison request authorizes the requested alternatives at the same focused scope.
- For example, exploring an accent picker's choice layout needs the color options and selected-state feedback. Include an app preview only when evaluating how the accent looks in context.

### Fuller mode — when requested

- Use this mode for requests such as "show the full screen," "include the surrounding settings," or "sketch the onboarding flow." An explicit screen or flow request is enough; no mode keyword is required.
- Show the requested screen or journey, with the navigation, adjacent actions, and states needed to try its main task. Keep unrelated screens out of scope.

Carry the chosen scope through revisions. Expand it when the user asks for more context or a fuller screen or flow.

## Establish the brief

- Use the request and conversation to identify the intended user, platform, and design question.
- Ask one focused question only if missing information would materially change the structure. Otherwise make reasonable assumptions and briefly state consequential assumptions in the response.
- Use product context and supplied references already available. Follow Visualize's guidance on using existing context instead of searching the project just to produce a mockup.
- A sketch request alone does not authorize implementation in the product or publication. Follow an explicit request for another deliverable format when given.

## Build the sketch

- Keep fidelity low: a restrained neutral palette, simple boundaries, readable labels, and clear spacing. Preserve platform conventions that affect navigation or behavior. Skip decorative illustrations, gradients, and branding work unless requested.
- Use plausible sample content and real action labels. Reserve placeholders for images and genuinely unknown content; avoid filling every region with lorem ipsum or blank boxes.
- Make included controls locally interactive when relevant: selection changes the visible state and forms provide plausible feedback. In fuller mode, navigation should connect the requested screens with a clear way back. Keep simulated actions local and do not imply real data was saved or sent.
- Include empty, loading, error, or confirmation states only when they affect the design question. Do not build a state catalogue by default.
- Follow the chosen scope for alternatives. When comparing, use meaningfully different structures with the same task and sample content, following Visualize's variant carousel guidance.
- Use Visualize's product-specific mockup styling rules inside the depicted interface. Keep any presentation controls outside the product UI and limited to useful layout decisions.
- Support the requested platform and narrow conversation widths. Keep labels readable, controls keyboard accessible, and essential actions usable without hover.

## Check and present

Read back the generated fragment and check its primary interaction and narrow layout using Visualize's checks and preview workflow where available. Check navigation only when included. Keep verification proportional to the sketch; fix broken controls, clipped content, and unreadable states, and report checks that could not be completed.

Return the inline visualization through Visualize's required final-response content reference. Add at most a short explanation of the key layout decision or a consequential assumption. Keep implementation details out of the sketch and surrounding explanation.

For revisions, preserve the agreed structure and fidelity unless the user changes direction. Update the existing sketch where practical and include the updated visualization reference in that turn's final response. Carry forward explicit layout choices; move to polished design or product implementation when the user requests it.

## Example requests

- Focused: "Show an alternative accent picker."
- Focused comparison: "Compare two ways to show the selected color."
- Fuller screen: "Show the complete iPhone reminder creation screen."
- Fuller flow: "Sketch onboarding with working next and back buttons."
