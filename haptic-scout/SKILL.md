---
name: haptic-scout
description: Audit where tactile feedback would help an app or web interaction. Use for haptic or vibration recommendations. Report the trigger, benefit, feel, and recommendation strength. Default to a read-only audit.
---

# Haptic Scout

Run a read-only audit for the few moments where touch would tell the user something useful. Judge the event the user experiences, such as a drag crossing a snap point. The component that owns the event is where you look for evidence.

## Inspect the current behavior

1. Identify the requested surfaces, runtimes, and input modes. In a mixed repo, distinguish native iOS, native Android, hybrid screens with a native bridge, and browser-only screens by their entry points.
2. Find native controls, direct platform calls, shared haptic helpers, and existing custom patterns such as Apple `.ahap` files. Trace each cue through its callers and check for multiple paths from the same event, such as a gesture handler and a state observer. Note the existing visual, audio, and accessibility feedback.
3. Follow candidate interactions from input to the state change the user would feel. Start with these patterns.

| Look for | Trace to |
|---|---|
| Custom sliders, pickers, scrubbers, and drag-to-reorder | An actual detent, selected value, or reorder position change |
| Swipe actions, hold-to-confirm, and long presses | Entering the armed state, reaching the hold threshold, or opening the affordance |
| Snapping, dropping, and gestures against constraints | Settling at an anchor, accepting a drop, or rejecting it |
| Deliberate actions with meaningful results | The app's real success or failure condition, including cancellation, retries, and rollback where relevant |

## Assess each candidate

- **Purpose.** Name what the user would learn by feeling the cue. Routine taps, hover, scrolling, and background changes rarely justify a pulse.
- **Timing.** Play an arming cue once when the interaction enters its armed state. Repeated updates while armed stay silent. Within a gesture, rearm only when the app's separate reset transition fires. Each new gesture can cue again. Cancellation ends the gesture in silence. For async results, play only when the outcome belongs to the current user-initiated operation and is still relevant in the visible interaction. Canceled, superseded, and stale operations stay silent.
- **Frequency.** Prefer one cue per action. Add another only when it conveys different information at a perceptibly different moment. If fast movement makes detent ticks blur, use coarser milestones.
- **Ownership.** Give each transition one feedback owner per runtime. A gesture callback and a state observer can both see one change and produce two pulses. Reuse the existing owner when it already covers the event. Keep the state visible and accessible with haptics disabled or unavailable. Use accessible state or value for controls and status messages for meaningful outcomes. [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

### Decide what to recommend

| Recommendation | Meaning |
|---|---|
| **Strongly recommended** | The cue would help the user notice an important change or decide what to do next. |
| **Recommended** | The cue would reinforce a meaningful action or result. |
| **Optional** | The interaction is already clear. The cue would mainly make it feel better. |
| **Skip** | The cue would add little, repeat too often, or be hard to understand. |

Judge how much the cue would help, then check where it can be delivered. Recommend an addition or upgrade when it has a clear benefit, a precise trigger, and an appropriate cadence. An existing cue is worth upgrading when a different feel would help the user notice something the current cue misses. If trigger, coverage, or compatibility is uncertain enough to change that decision, record what would resolve it.

## Choose the effect

Start with the closest system effect. A selection tick can mark a snap or newly armed action. If an existing cue already tells the user that the transition happened, skip an additional pulse. Recommend a custom effect only when you can name useful information the system cue would miss and explain how the new feel conveys it.

A soft rise near a snap point can help the user steer if their finger covers the guide and the remaining distance changes how they move. Ease the rise as they back away and stop it on release or cancellation. The snap itself still gets a single tick. A faster landing or a major mark can feel stronger when the distinction helps users judge weight, count steps, or find a target.

Read the applicable section of [runtime checks](references/runtime.md) when checking delivery or building the effect. Code, callback traces, and successful API returns can verify cue routing. Only a supported physical device can verify playback and feel.

## Report

Give a short list of the opportunities worth considering. Apply a recommendation to each cue on its own merits and group related findings by screen or flow. Include an **Optional** finding when it fits the request. Leave **Skip** findings out of the default report. If none are worth adding, say so in one sentence.

Give each finding a short Markdown heading that names the screen, control, or action. Put three bullets underneath, in this order. Use a blank line before the bullets.

- **Why** — Explain what the cue would tell the user or help them do. Use the names people see in the app and keep it to one or two sentences.
- **Haptic** — Say when the cue plays and what it feels like. Name the platform and any fallback when that changes the suggestion.
- Use **Strongly recommended**, **Recommended**, or **Optional** as the final bullet. Show the bold wording by itself.

Put a short source link at the end of **Haptic** when available. Use the file and line for code, or the page, layer, and event for a visual builder. Include a variant or breakpoint if it affects the finding.

If a finding needs testing, say in **Why** what would make the cue worth keeping. Mention platform support or gaps in what you inspected when they change the recommendation. Save API names, device details, replay steps, and rejected ideas for a requested technical breakdown.

Example

### Arming Archive with a swipe

- **Why** — A tick tells you when releasing the swipe will archive the message, even if your finger covers part of the row.
- **Haptic** — On supported iPhones, one short system selection tick when Archive arms. A reverse swipe can rearm the tick only after the row resets. Keep the visible and accessible armed state when web vibration is unavailable.
- **Recommended**

## When asked to build a recommendation

Implement the chosen effect at the event identified in the audit. Define what plays and when, and what cancels or rearms it. For a custom pattern, choose starting timing, intensity, and sharpness or platform equivalents, and connect them to the relevant gesture value if the effect is interactive. Tune the starting values on hardware when available.

Reuse the app's feedback owner and settings. Stop ongoing effects on cancellation, interruption, or when leaving the interaction. On supported hardware, check timing against visible or audio feedback and verify the interaction still works when the cue is off.
