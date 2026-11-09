# Component adapter

Create two small files. The helper injects both into a copy of the editor; do not rebuild its controls or motion engine. No frontend framework or build step is needed.

## Markup

`--markup` is passive HTML and root-scoped CSS placed inside the preview scene. Scope styles under `#motion-playground [data-motion-component]`. Do not include document wrappers, scripts, inline event handlers or dependencies. Leave the editor's `mp-` IDs alone; use component-specific attributes for queries.

## Renderer

`--adapter` is a JavaScript function body, executed once inside the editor's closure. It must **return a function** `(progress, context) => { ... }` that sets the visible pose.

`preview` provides:

- `scene`: the scene element; measure it for responsive positioning.
- `query(selector)`: query inside that scene.
- `replay()`: replay the complete interaction from rest.
- `properties`: set this to a JSON-serializable mapping of animated properties and endpoints. It is included in saved/exported motion settings.

`progress` is the component's absolute pose: 0 is resting, 1 is active. It may be below 0 or above 1 with Back curves or springs; on the return leg it moves from 1 to 0. Use it for geometry, not just an unrelated diagnostic marker.

`context` contains `phase` (`opening`, `open`, `closing`, `closed`), `elapsedMs` within the passage, `durationMs`, `reducedMotion`, and `sample(ms)`, the same forward easing function used by the graph. Elapsed time is pinned to the completed passage during either endpoint hold. Prefer the simple absolute progress for a single transition. If choreography is necessary, fit offsets within this controlled duration and invert sampled poses on return; do not start another timer.

Set up listeners once outside the returned function. Set styles, attributes and text inside it; do not replace interactive DOM every frame. Native custom value fields are the keyboard alternative to graph dragging.

## Example: expandable card

Markup:

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

Use realistic content from the actual brief instead of this example copy. Adjust the scene height when the described component needs more room; change the copied preview, not the installed template.

## Generation options

`--preset` accepts any built-in easing or spring enum in the editor, such as `EASE_OUT` or `BOUNCY`. Default is `EASE_OUT`. `--duration` sets a Bézier duration in milliseconds (default 300); spring duration is derived from its physical parameters, so do not supply both a spring preset and `--duration`. Users can customize every value in the resulting editor.

`--key` sets a stable component identity for persisted settings; it defaults to the name's slug. Reuse it when revising the same component. A saved snapshot from a different component key is ignored. `--force` explicitly replaces an existing generated output.

The compact instruction summarizes the component and current motion. Copy includes the complete inspectable specification, with full-precision parameters, property mapping, initial scene markup/styles, the actual adapter factory, its layout helper and the actual analytic spring/inverse-Bezier sampler source. Keep the adapter self-contained: use preview and the supplied context; the included layout/q helper is available for the template. Do not depend on other outer editor variables, external assets or independent clocks. Record any additional constants inside the adapter and give the component explicit geometry/transform origins. The saved model state also includes component identity and the full property mapping. The demo's layout, hold pauses and Slow/Loop choices are preview controls, not implementation requirements.
