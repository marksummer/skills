# Runtime checks

Use the section that matches the audited interaction. Pick a matching system effect or silence when custom playback is unavailable.

## iOS

Use the app's helper or a SwiftUI or UIKit effect for familiar cues. Check deployment and hardware support before recommending Core Haptics, including `CHHapticEngine.capabilitiesForHardware().supportsHaptics`. Use a transient for a click, a continuous event for a rise, and dynamic intensity or sharpness when the feel follows a gesture. An AHAP file can hold a fixed reusable pattern. Reuse the engine and recover from stops and resets when implementing a custom cue. [Apple haptics guidance](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) · [Apple engine setup](https://developer.apple.com/documentation/corehaptics/preparing-your-app-to-play-haptics) · [Apple real-time haptic parameters](https://developer.apple.com/documentation/corehaptics/updating-continuous-and-transient-haptic-parameters-in-real-time)

## Android

Start with action-based system feedback. For a custom effect, check the app's available composition or envelope APIs and device support for each required effect. [Android custom haptic effects](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects)

## Hybrid

Trace the wrapper to the registered plugin and native implementation on each platform. Check the installed plugin version and deployment targets. Apply the web checks when the same screen runs outside the app.

## Web

Treat `navigator.vibrate()` as optional basic vibration. Check device and browser support, API presence, document visibility, and prior user activation in the actual frame. Exercise the intended trigger on a fresh page and after activation. A first touch drag can cross the threshold before release grants activation. Skip the pulse if playback is unavailable at the trigger and preserve visible and accessible state. [W3C Vibration API](https://www.w3.org/TR/vibration/) · [HTML activation events](https://html.spec.whatwg.org/multipage/interaction.html#activation-triggering-input-event)
