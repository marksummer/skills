# Tune Motion — Linear-inspired UI

A small, precise motion editor. The component is the subject; the controls are quiet tools around it.

Inspired by [Linear's approach to a cohesive, neutral interface](https://linear.app/now/how-we-redesigned-the-linear-ui). This is a local design specification, not an official Linear theme or a reproduction of its private tokens.

## Surface and color

Use the theme-aware `--mp-` tokens in `assets/editor.html`. No gradients, glass, shadows, ornamental icons or extra cards.

| Token | Light | Dark |
| --- | --- | --- |
| Paper | `#ffffff` | `#17181c` |
| Preview ground | `#f7f7f9` | `#1d1e23` |
| Field | `#ffffff` | `#202127` |
| Primary text | `#22232a` | `#ececf0` |
| Secondary text | `#62646f` | `#a2a4af` |
| Divider | `#e4e5e9` | `#303138` |
| Motion accent | `#5e63cc` | `#a5a9ff` |

Keep the motion accent on curve strokes, handles, native range/checkbox states and focus. Play uses a neutral ink fill. Preserve the depicted component's own colors; selecting an accent in a component must not recolor the editor.

## Type and geometry

Use Inter when available, then the platform sans-serif. Do not add a font download for this small editor. Title: 14px, 500 weight, 20px line height. Fields: 13px. Labels, buttons, graph annotations: 12px. Numeric inputs use tabular figures. Spring controls and summary values show at most one decimal place, without trailing .0; retain full precision internally and in the full copied specification. Keep labels readable; never shrink them to make an overcrowded row fit.

Use an 18px desktop inset and 14px narrow inset. Main vertical groups use 12–16px spacing; related field parts use 6–8px. Outer radius: 10px. Preview and controls: 6px. Borders are 1px; depth comes from neutral surface differences, not shadows.

## Composition

- Header: component name.
- Settings: Easing plus a compact Duration row containing the numeric value, ms unit and live slider.
- One generous preview, then Play at left and Loop/Slow at right.
- One directly editable curve below a subtle divider. Custom values appear only while customizing.
- A compact instruction updates live below the curve and custom values. One Copy button copies the complete specification, including reference code. Keep that read-only text inspectable under Full specification; no Draft or Refresh action. Let expanded text grow to fit without internal scrolling.

Do not add subtitles, repeated preset headings, phase/progress readouts, direction menus, comparisons, explanatory copy, metrics or extra settings panels by default.

## Responsive and interactive details

Stack the settings below 400px. Let custom Bézier values form two columns on narrow widths. Keep three spring columns on fine pointers; on narrow touch surfaces use labelled rows with a value and slider. Touch controls retain 44px targets and 16px editable text. Avoid horizontal scrolling and clipped numbers.

Use native controls and visible focus rings. Hover may strengthen a field border or neutral fill. Preserve disabled states, text selection, native keyboard entry and copy feedback. Appearance follows the host.

Styling must not change the animation sampler, live editing, loop phase, explicit pause, reduced-motion handling, saved component identity or property mapping. A restyle should preserve the user's selected motion. Keep any changes to the example component separate from editor styling.
