---
name: tune-motion
description: Preview and tune a described component's animation directly in chat, with live easing, spring and draggable curve controls. Use for trying motion before implementing it in a product.
---

# Tune motion

Build one interactive preview of the described component. Let the user adjust its motion, then use the chosen settings when they ask for implementation.

## Set the scope

Use the description, supplied source, and conversation to identify the component, its resting and active states, and what changes between them. Ask only when a missing detail would affect the interaction. Otherwise choose a reasonable starting motion and build it.

Show the requested component with enough context to understand it. An expanding accent picker should show the palette opening and closing; a toast should enter and exit. Use supplied geometry and states without copying application dependencies into the preview. Use the stock sliding panel only when it fits the request.

## Choose the starting motion

Preserve supplied endpoints and chosen values. When starting from a description, identify what the motion should communicate, then use the first applicable case:

| Interaction | Starting choice and reason |
| --- | --- |
| Direct dragging or a release that should feel physical | Start with a spring such as `GENTLE`; keep the visible pose tied to the gesture when implementing. A timed curve should not lag behind direct input. |
| An element enters or exits | Use `EASE_OUT` so feedback begins promptly and settles into place. |
| An existing element moves or changes shape | Use `EASE_IN_AND_OUT` to ease between established states. |
| Progress that must represent constant change | Use `LINEAR`; easing would distort the apparent rate. |

For timed UI transitions without supplied timing, start at 200ms for a small control and 280ms for a larger panel. Larger travel needs more time to remain legible. These are tuning defaults, not limits on user choices or spring settling time. Distinguish Slow playback from product duration.

For a new dialog/popover scale entrance, start near full size (around 0.95), because growing from a point implies a different physical origin. Preserve a real expansion from its trigger when the supplied geometry calls for one. Do not add overshoot to bounded properties such as opacity.

If motion delays repeated keyboard actions or obscures functional data, explain the concern and offer an immediate or reduced-motion implementation. Keep a specifically requested motion experiment in scope; do not turn it into a broad animation audit.

## Use Visualize

Find the installed `visualize:visualize` skill in the current catalog and read its full `SKILL.md` before creating or revising a preview. Follow its current output contract and relevant mockup guidance. Do not hardcode a plugin version.

If Visualize is unavailable, explain that inline previews need it. Only claim a rendered result when one exists.

## Build the preview

Follow [DESIGN.md](DESIGN.md) for the Linear-inspired editor. Preserve the component's own design and colors.

Use [scripts/create_preview.py](scripts/create_preview.py) to reuse [assets/editor.html](assets/editor.html), which contains the motion engine and controls. Write the component markup and pose renderer using [references/component-adapter.md](references/component-adapter.md). Resolve paths from this skill's directory.

```bash
python3 <skill-dir>/scripts/create_preview.py \
  --name "Accent picker" \
  --description "Expand the palette and rotate the divider; reverse to collapse." \
  --markup <task-dir>/component.html \
  --adapter <task-dir>/component.js \
  --output <writable-visualization-dir>/accent-picker-motion.html
```

Choose a durable, writable location using Visualize's current instructions. The helper writes a fragment and requires `--force` to replace an existing output. For revisions, keep the output path and component key stable and retain chosen settings when available.

Keep one component preview and the controls specified in DESIGN.md. Add comparison views or extra panels only when they help answer the user's motion question.

## Keep the motion consistent

- Drive the visible pose with the same sampled progress as the curve. Independent CSS animations, transitions, library springs, and timers must not drive it: they make the controls and exported specification describe different motion.
- Allow spring overshoot in transforms and dimensions where appropriate. Clamp bounded values such as opacity. Record mappings in `preview.properties` so exported settings describe the implementation.
- Play runs from rest to active and back to rest; replay starts from rest. Loop repeats that cycle. Component triggers can call `preview.replay()`.
- Apply slider and curve edits immediately during a loop. Keep its phase and preserve an explicit Pause. Releasing a control must not stop playback. Keep local state and the instruction synchronized; never send a chat message automatically.
- Preserve reduced-motion handling, native numeric alternatives, a responsive curve, and state persistence. Leave room for overshoot and the full expanded component.
- Use the supplied presets. Published Figma spring parameters are included, but they do not establish full Figma playback parity. Exact matching needs a separate request and verification.

## Check and present

Check both endpoints, an intermediate pose, and a bouncy style. While a loop runs, verify that duration, spring values, and curve dragging change the component itself. Check the complete return cycle and a narrow chat width. Report any checks you could not complete.

Return the inline preview using Visualize's required content reference, with brief accompanying prose.

The read-only instruction must update immediately after valid slider, curve, preset, and restored-state changes. Show spring values to at most one decimal place in controls and the summary; retain full precision internally and in exports. Keep the summary short and the full read-only specification inspectable under Full specification. Copy must include the full specification without pausing playback.

The specification must contain:

- Current parameters at full precision, property mappings, and geometry/styles.
- Actual renderer and sampler reference code.
- Opening and closing equations, endpoint and clamping rules, and units.
- Interruption and reduced-motion behavior.

Separate demonstration controls such as Loop, Slow, holds, and framing from product requirements. Use selected numeric values, not just preset labels or rounded displays. Verify the exported sampler and poses against the preview, including overshoot and closing. Do not add Draft or Refresh controls, or claim the widget can fill the host chat composer without that capability.

When the user asks to apply the motion, read available widget state or their copied instruction. If chosen values are unavailable, ask for the instruction; a screenshot is not enough to recover them. Follow the product's tools and authorization requirements. A preview alone does not authorize product changes or publication.
