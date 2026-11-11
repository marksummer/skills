# Tune motion editor

Keep the component central and the controls simple.

The editor takes direction from [Linear's neutral interface](https://linear.app/now/how-we-redesigned-the-linear-ui). These are local design rules, not official Linear tokens or a reproduction of its private theme.

## Color and surfaces

Use the theme-aware `--mp-` tokens in `assets/editor.html`. Leave out gradients, glass, shadows, decorative icons, and extra cards.

| Token | Light | Dark |
| --- | --- | --- |
| Paper | `#ffffff` | `#17181c` |
| Preview ground | `#f7f7f9` | `#1d1e23` |
| Field | `#ffffff` | `#202127` |
| Primary text | `#22232a` | `#ececf0` |
| Secondary text | `#62646f` | `#a2a4af` |
| Divider | `#e4e5e9` | `#303138` |
| Motion accent | `#5e63cc` | `#a5a9ff` |

Use the motion accent for curve strokes, handles, native range and checkbox states, and focus. Give Play a neutral ink fill. Preserve the component's colors; changing an accent inside it must not recolor the editor.

## Type and spacing

Use Inter when available, then the platform sans-serif. Do not download a font for the editor.

| Element | Size |
| --- | --- |
| Title | 14px, 500 weight, 20px line height |
| Fields | 13px |
| Labels, buttons, and graph annotations | 12px |

Use tabular figures in numeric inputs. Show spring controls and summary values to at most one decimal place, without trailing .0. Keep full precision internally and in the copied specification. Rearrange crowded rows instead of shrinking labels.

Use 18px outer padding on desktop and 14px at narrow widths. Space main groups 12 to 16px apart and related field parts 6 to 8px apart. Use a 10px outer radius, 6px for the preview and controls, and 1px borders. Separate surfaces with neutral color differences.

## Layout

- Header: component name.
- Settings: Easing and a compact Duration row with the value, ms unit, and live slider.
- One roomy preview, followed by Play on the left and Loop/Slow on the right.
- One editable curve below a subtle divider. Show custom values only while customizing.
- A compact live instruction below the curve and custom values. Copy exports the complete specification and reference code. Keep that read-only text inspectable under Full specification and let it expand without internal scrolling. Do not add Draft or Refresh.

Leave out subtitles, repeated preset headings, progress displays, direction menus, comparisons, explanatory copy, metrics, and extra settings panels unless requested.

## Responsive behavior

Stack settings below 400px. Use two columns for custom Bézier values at narrow widths. Keep three spring columns with fine pointers. On narrow touch screens, use labeled rows with a value and slider. Keep touch targets at 44px and editable text at 16px. Prevent horizontal scrolling and clipped numbers.

Use native controls and visible focus rings. Hover can strengthen a border or neutral fill. Preserve disabled states, selection, keyboard entry, and copy feedback. Follow the host appearance.

Styling changes must preserve the sampler, live editing, loop phase, explicit pause, reduced-motion handling, saved component identity, property mapping, and selected motion. Keep example-component changes separate from editor styling.
