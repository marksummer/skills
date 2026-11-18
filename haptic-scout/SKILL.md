---
name: haptic-scout
description: Audit an app or website for places where standard or custom haptics would help. Use when asked where to add a haptic or where richer feedback would improve an interaction. Give a short, read-only report with where the cue goes, why it helps, what it should feel like on the target platform, and how strongly you recommend it.
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
- **Timing.** Name the exact state transition, when it rearms, and which paths should stay silent. For an async result, trace the final outcome and confirm it still belongs to the current user-initiated operation and is relevant in the visible interaction. A canceled, superseded, or stale operation should stay silent.
- **Frequency.** Judge the cadence within a gesture and across a session. Prefer one cue per action unless multiple cues convey distinct information at perceptibly different moments. If fast movement makes detent ticks blur, consider coarser milestones. At a gesture boundary, use an existing separate reset threshold where appropriate or fire once per gesture.
- **Existing feedback.** Identify who owns the cue on each runtime and avoid duplicate tactile feedback. The state should remain visible and accessible with haptics disabled or unavailable. Use accessible state or value for controls and status messages for meaningful outcomes. [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

### Decide what to recommend

| Recommendation | Meaning |
|---|---|
| **Strongly recommended** | The cue would help the user notice an important change or decide what to do next. |
| **Recommended** | The cue would reinforce a meaningful action or result. |
| **Optional** | The interaction is already clear. The cue would mainly make it feel better. |
| **Skip** | The cue would add little, repeat too often, or be hard to understand. |

Judge how much the cue would help, then check where it can be delivered. Recommend an addition or upgrade when it has a clear benefit, a precise trigger, and an appropriate cadence. An existing cue is worth upgrading when a different feel would help the user notice something the current cue misses. If trigger, coverage, or compatibility is uncertain enough to change that decision, record what would resolve it.

## Look for a richer feel

Actively look for moments where a custom effect could give an interaction a distinctive feel or make a physical change easier to read. Compare it with the closest system effect. A familiar selection or success cue often fits. A custom effect earns its place when the interaction benefits from a noticeable change in texture, strength, or timing.

- **Pulling into a snap point.** Let a soft sensation build near the actual snap point. End the rise with one crisp click when the object locks in. Ease the rise as the finger backs away and stop it when the drag ends or is canceled.
- **Landing a moving object.** Use one short impact as the object settles. Vary the strength with the landing speed within a subtle range.
- **Crossing fine steps and major marks.** Make some marks feel different so the user can count or find an important value. Keep the smaller steps light and drop intermediate ticks when the user moves quickly.

## Recommend the effect by runtime

- **iOS.** Use an existing helper or a SwiftUI or UIKit effect when it can deliver the intended feel. For custom effects, consider Core Haptics on supported devices. Use a short transient for a click, a continuous event for a texture or rise, and dynamic intensity or sharpness when the feel follows a gesture. An AHAP file can hold a reusable, fixed pattern. Check deployment and hardware support, including `CHHapticEngine.capabilitiesForHardware().supportsHaptics`. Choose a matching system effect or silence as the fallback. [Apple haptics guidance](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) · [Core Haptics](https://developer.apple.com/documentation/corehaptics)
- **Android.** Start with action-based system feedback for familiar controls. For custom feel, check which composition or envelope APIs the app can use and whether the device supports the required effects. Choose a matching system effect or silence as the fallback. [Android custom haptic effects](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects)
- **Hybrid apps.** Trace the wrapper to the registered plugin and the implementation on each platform. Check the installed dependency version and deployment targets. A resolved bridge call alone leaves physical playback unverified. Apply the browser checks when the same screen runs outside the app.
- **Web.** Treat `navigator.vibrate()` as optional basic vibration. For a richer effect a browser cannot reproduce, use the visible or accessible cue without vibration. Verify current browser and device support, API presence, document visibility, and prior user activation (sticky activation) in the actual frame. Check the exact trigger on a fresh page and after activation. The first touch drag can reach a threshold before release grants activation. If vibration is unavailable at that moment, keep the visible and accessible cue and skip the pulse. API presence or a successful return value leaves physical playback unverified. [W3C Vibration API](https://www.w3.org/TR/vibration/) · [HTML activation events](https://html.spec.whatwg.org/multipage/interaction.html#activation-triggering-input-event)

## Report

Give a short list of the opportunities worth considering. Apply a recommendation to each cue on its own merits and group related findings by screen or flow. Include an **Optional** finding when it fits the request. Leave **Skip** findings out of the default report. If none are worth adding, say so in one sentence.

Give each finding a short Markdown heading that names the screen, control, or action. Put three bullets underneath, in this order. Use a blank line before the bullets.

- **Why** — Explain what the cue would tell the user or help them do. Use the names people see in the app and keep it to one or two sentences.
- **Haptic** — Say when the cue plays and what it feels like. Name the platform and any fallback when that changes the suggestion.
- Use **Strongly recommended**, **Recommended**, or **Optional** as the final bullet. Show the bold wording by itself.

Put a short source link at the end of **Haptic** when available. Use the file and line for code, or the page, layer, and event for a visual builder. Include a variant or breakpoint if it affects the finding.

If a finding needs testing, say in **Why** what would make the cue worth keeping. Mention platform support or gaps in what you inspected when they change the recommendation. Save API names, device details, replay steps, and rejected ideas for a requested technical breakdown.

Example

### Dragging a card into a grid slot

- **Why** — You can feel the card lock into place even if your finger covers the outline.
- **Haptic** — On supported iPhones, a soft rise as the card nears the slot and one crisp click as it snaps in.
- **Strongly recommended**

## When asked to build a recommendation

Implement the chosen effect at the event identified in the audit. Define what plays and when, and what cancels or rearms it. For a custom pattern, choose starting timing, intensity, and sharpness or platform equivalents, and connect them to the relevant gesture value if the effect is interactive. Tune the starting values on hardware when available.

Reuse the app's feedback owner and settings so the new effect replaces any cue on that same event. For Core Haptics, reuse the engine and stop ongoing effects on cancellation, interruption, or when leaving the interaction. Recover from engine stops and resets for the next eligible event. Check that supported hardware plays the intended effect in sync with the visual or audio feedback. Verify that turning haptics off suppresses the cue while the interaction still works. [Apple engine setup](https://developer.apple.com/documentation/corehaptics/preparing-your-app-to-play-haptics) · [Apple real-time haptic parameters](https://developer.apple.com/documentation/corehaptics/updating-continuous-and-transient-haptic-parameters-in-real-time)
