# Component adapter

Write a markup file and an adapter file. The helper inserts them into a copy of the editor, reusing its controls and motion engine. No frontend framework or build step is required.

## Markup

`--markup` accepts passive HTML and root-scoped CSS for the preview scene. Scope styles under `#motion-playground [data-motion-component]`. Omit document wrappers, scripts, inline event handlers, and dependencies. Leave `mp-` IDs for the editor and use component-specific attributes for queries.

## Renderer

`--adapter` is a JavaScript function body that runs once inside the editor's closure. Return a function `(progress, context) => { ... }` that sets the visible pose.

The `preview` interface provides:

| Member | Purpose |
| --- | --- |
| `scene` | Scene element, available for responsive measurements. |
| `query(selector)` | Query within the scene. |
| `replay()` | Replay the full interaction from rest. |
| `properties` | JSON-serializable property and endpoint mappings included in saved and exported settings. |

`progress` is the absolute pose: 0 at rest and 1 active. Back curves and springs can go below 0 or above 1. The return leg moves from 1 to 0. Use it to drive the component geometry.

`context` contains `phase` (`opening`, `open`, `closing`, `closed`), `elapsedMs` within the passage, `durationMs`, `reducedMotion`, and `sample(ms)`, the graph's forward easing function. Endpoint holds pin elapsed time to the completed passage.

For a single transition, use absolute progress. If choreography is needed, fit offsets within the controlled duration and invert sampled poses on return. Do not start another timer.

Set up listeners once outside the returned function. Update styles, attributes, and text inside it without replacing interactive DOM each frame. Native custom-value fields provide a keyboard alternative to curve dragging.

## Example

Expandable-card markup:

```html
<div data-motion-component>
  <button type="button" data-disclosure aria-expanded="false">Details</button>
  <div data-content><p>Animation settings update this expansion live.</p></div>
</div>
<style>
#motion-playground [data-motion-component] {width:min(320px,calc(100% - 32px));margin:24px auto;color:var(--mp-ink)}
#motion-playground [data-disclosure] {display:block;width:100%;height:44px;text-align:left;padding:0 14px;border:1px solid var(--mp-border);border-radius:8px;background:var(--mp-paper)}
#motion-playground [data-content] {overflow:hidden;height:0}
#motion-playground [data-content] p {margin:0;padding:14px;font-size:14px}
</style>
```

Adapter:

```javascript
const button = preview.query('[data-disclosure]');
const content = preview.query('[data-content]');
preview.properties = { contentHeightPx: [0, 72], contentOpacity: [0, 1] };
button.addEventListener('click', preview.replay);
return progress => {
  content.style.height = Math.max(0, 72 * progress) + 'px';
  content.style.opacity = Math.max(0, Math.min(1, progress));
  button.setAttribute('aria-expanded', String(progress > 0));
};
```

Replace the sample content with the brief's actual content. Allow enough scene height for the component. Change the generated copy, leaving the installed template intact.

## Generator options

`--preset` accepts a built-in easing or spring enum, such as `EASE_OUT` or `BOUNCY`; the default is `EASE_OUT`.

`--duration` sets Bézier duration in milliseconds, defaulting to 300. Spring duration comes from its physical parameters, so do not combine a spring preset with `--duration`. The editor lets users customize all values.

`--key` sets the component identity used for persistence. It defaults to the name's slug. Reuse it for revisions; snapshots from another key are ignored.

`--force` replaces an existing generated output.

## Export

The compact instruction describes the component and current motion. Copy includes the inspectable full specification with:

- Parameters at full precision, property mappings, and initial scene markup/styles.
- The actual adapter factory and layout helper.
- The actual analytic spring/inverse-Bezier sampler source.

Keep the adapter self-contained with `preview` and the supplied context. The template's included layout/q helper is also available. Avoid other outer editor variables, external assets, and independent clocks. Put additional constants inside the adapter and define geometry and transform origins explicitly.

Saved model state includes the component identity and full property mapping. Layout, endpoint holds, and Slow/Loop choices belong to the preview and do not become product requirements.
