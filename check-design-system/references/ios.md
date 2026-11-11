# iOS audit

## Find the system

Identify active app targets, Swift packages, build-conditional UI, and SwiftUI/UIKit entry points. Read project design guidance. Find theme types, style extensions, reusable views, modifiers, button and label styles, UIKit subclasses and configurations, appearance proxies, asset catalogs, and type resources.

Trace symbols and asset names across packages and call sites. Inspect named colors, appearance and contrast variants, and image roles. Generated asset accessors reference their source assets; do not flag or edit them as literal bypasses.

## Inspect SwiftUI

- Trace fonts, foreground styles, tints, backgrounds, shapes, padding, spacing, frames, shadows, overlays, transitions, and animations to their definitions.
- Read custom modifiers, styles, environment values, `@ScaledMetric`, and wrapper views before deciding that a call bypasses the system.
- Accept semantic native text styles, adaptive colors and materials, standard controls, and default spacing unless project rules require alternatives.
- Flag fixed values when they conflict with an established rule. Fixed icon dimensions, hairlines, chart coordinates, and image ratios can be deliberate.
- Inspect caller overrides. A shared view can conform internally while its caller applies an unsupported font, tint, frame, or style.
- Inspect environment-driven themes, control states, size classes, accessibility branches, and platform availability. Source handling alone does not establish device behavior.

## Inspect UIKit and mixed apps

- Trace colors, fonts, attributed strings, configurations, constraints, layer appearance, nib and storyboard attributes, and appearance customization.
- Recognize dynamic colors, preferred text styles, `UIFontMetrics`, system configurations, and project-owned bridging wrappers.
- Check whether SwiftUI/UIKit bridges preserve theme propagation.
- Distinguish semantic references from matching literal colors. Check appearance variants before proposing a replacement.

## Verify findings

Use file paths and line numbers or precise asset, nib, and storyboard identifiers. Keep previews out of production counts, even when they help inspection.

Use existing checks first. Use available Simulator/Xcode tools and relevant skills when rendering or behavior needs verification. Report the simulator, appearance, content-size category, and states actually exercised. Source inspection or a normal-size screenshot does not establish Dynamic Type, VoiceOver, physical-device, or full interaction behavior.

Respect the project's balance of native and custom conventions. Keep native controls when they serve the design; shared-component counts do not justify replacing them.
