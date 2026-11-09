---
name: tune-motion
description: Preview and tune a described component's animation directly in chat, with live easing, spring and draggable curve controls. Use for trying motion before implementing it in a product.
---

# Tune motion

Turn a component description into one focused, interactive motion preview. Let the user tune it locally, then carry the chosen settings into a later implementation request.

## Use Visualize

This skill depends on the installed `visualize:visualize` skill. Resolve it from the current skill catalog and read its complete `SKILL.md` before producing or updating a preview. Follow its current output contract and applicable mockup guidance; do not hardcode a plugin version. If unavailable, explain that inline previewing needs Visualize rather than claiming a rendered result.

## Establish the component

Use the user's description, supplied component, and conversation to identify the element, its resting/active states and what changes between them. Ask only when a missing detail materially affects the interaction. Otherwise choose a reasonable starting motion and build it.

Show the actual described component, with only enough context to understand its interaction. Do not substitute the stock sliding panel when a component has been described. For example, an expanding accent picker should show a palette expanding and collapsing; a toast should visibly enter and exit. If source is supplied, adapt its meaningful geometry and states without copying application dependencies into the preview.

## Build from the editor

Follow [DESIGN.md](DESIGN.md) for the Linear-inspired editor shell. Keep the preview component faithful to its own design; the editor theme must not recolor or redesign it.

Reuse [assets/editor.html](assets/editor.html) through [scripts/create_preview.py](scripts/create_preview.py). The asset contains the shared motion engine and minimal controls; author only the component markup and its pose renderer. Read [references/component-adapter.md](references/component-adapter.md) for that small interface and an example. Resolve paths relative to this skill directory.

```bash
python3 <skill-dir>/scripts/create_preview.py \
  --name "Accent picker" \
  --description "Expand the palette and rotate the divider; reverse to collapse." \
  --markup <task-dir>/component.html \
  --adapter <task-dir>/component.js \
  --output <writable-visualization-dir>/accent-picker-motion.html
```

Choose a durable writable visualization location using Visualize's current instructions. The helper writes a fragment, not a standalone website. It refuses to overwrite an existing output unless `--force` is supplied. For revisions, keep the output path and component key stable, and retain the chosen settings where available.

Keep the editor minimal: component name, easing, duration, one component preview, Play/Pause/Resume, Loop, Slow and the curve, followed by a live instruction with Copy. Custom numerical values appear only when customizing. Do not add explanatory paragraphs, duplicate state readouts, simultaneous reference previews, transition/direction menus, decorative metrics or new settings panels unless the user needs them.

## Preserve the motion contract

- The renderer receives the same sampled progress as the curve. Use it to set the component's visible pose directly. No independent CSS animation, CSS transition, library spring or second animation clock: those would bypass the controls.
- Let transforms and dimensions show spring overshoot where appropriate; clamp bounded values such as opacity. Record the property mapping in `preview.properties` so the saved settings describe what will be implemented.
- Play runs the full resting → active → resting cycle, starting from rest when replayed. Loop repeats that cycle. Preview component triggers can call `preview.replay()`.
- Slider and curve edits affect a running loop immediately without resetting its phase or stopping it on release. Preserve an explicit Pause. Keep local state and the instruction synchronized; never send a chat message automatically.
- Preserve the included reduced-motion handling, native numeric input alternatives, responsive curve and state persistence. Allow enough room to see overshoot and the component's full expanded state.
- Use the provided practical presets. Published Figma spring parameters are included, but do not claim complete Figma playback parity. Exact matching is separate work only when requested and verifiable.

## Check and hand off

Verify the component at both endpoints, at an intermediate pose and with a bouncy style. Check that changing duration, changing spring values and dragging the curve changes the component itself during a loop. Check full return playback and a narrow conversation width. Keep verification proportional; report any unavailable checks without claiming they passed.

Return the inline preview through Visualize's required content reference. Keep accompanying prose brief. Show a read-only instruction that updates immediately with valid slider, curve, preset and restored-state changes. Display spring values with at most one decimal place in controls and the summary, retaining full internal and exported precision. Keep the summary compact and the complete, read-only specification inspectable under Full specification. Copy includes that full specification without pausing playback. The handoff must contain full-precision current parameters, property mappings, geometry/styles and actual renderer/sampler reference code, opening/closing equations, endpoint/clamping rules, units, interruption and reduced-motion behavior. Distinguish demonstration Loop/Slow/holds/framing from product requirements. Do not substitute preset labels or rounded display values for the selected numeric settings. Verify exported sampler and component poses against the preview, including overshoot and closing. Do not add Draft or Refresh controls. Do not imply that the widget can populate the host chat composer if no such capability exists.

Read available widget state or a copied instruction when the user asks to apply their choice. If the chosen values are unavailable, ask for the instruction rather than guessing from a screenshot. Implement in the product only when requested, following that project's tools and authorization requirements. Creating a preview alone does not edit or publish the product.
