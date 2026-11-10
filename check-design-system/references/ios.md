# iOS adapter

## Discover

Identify active application targets, Swift packages, build-conditional UI, and SwiftUI/UIKit entry points. Find theme types, style extensions, reusable views, view modifiers, button/label styles, UIKit subclasses/configurations, appearance proxies, asset catalogs, and typography resources. Read the project's design documentation.

Trace symbols and asset names across packages and call sites. Inspect asset metadata for named colors, appearance/contrast variants, and image roles. Treat generated asset accessors as references to their source assets; do not flag or edit them as literal bypasses.

## Inspect SwiftUI

- Trace fonts, foreground styles, tints, backgrounds, shapes, padding, spacing, frames, shadows, overlays, transitions, and animations to their owning definitions.
- Inspect custom modifiers, styles, environment values, `@ScaledMetric`, and wrapper views before deciding a call bypasses the system.
- Accept semantic native text styles, adaptive colors/materials, standard controls, and default system spacing unless project rules explicitly require alternatives.
- Flag fixed values only with evidence of a system conflict. A fixed icon dimension, hairline, chart coordinate, or image ratio can be intentional.
- Inspect callers' overrides. A shared view can conform internally while a caller applies an unsupported font, tint, frame, or style.
- Include environment-driven themes, control states, size classes, accessibility branches, and platform availability in source inspection. Describe source handling without claiming device behavior.

## Inspect UIKit and mixed apps

- Trace colors, fonts, attributed strings, configurations, constraint constants, layer appearance, nib/storyboard attributes, and appearance customization where relevant.
- Recognize dynamic colors, preferred text styles, `UIFontMetrics`, system configurations, and project-owned bridging wrappers.
- Inspect SwiftUI/UIKit bridges for places where theme propagation breaks.
- Distinguish semantic references from literals with matching resolved colors; inspect appearance variants before suggesting replacement.

## Verify

Use source paths/line numbers or precise asset/nib/storyboard identifiers. Exclude previews from production counts while optionally using them for inspection.

Use existing checks first. Use available Simulator/Xcode tooling and applicable skills when rendering/behavior needs verification. Report the actual simulator, appearance, content-size category, and states exercised. Source inspection or a normal-size screenshot cannot establish Dynamic Type, VoiceOver, physical-device, or full interaction behavior.

Do not replace native controls with custom components merely to increase shared-component usage. Respect the project's chosen balance of native and custom conventions.
