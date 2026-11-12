# Board primitives

Use one `<template>` per screen and draw it with `wf-` classes. The viewer renders the same board at all three wireframe levels.

## Contents

1. The template element
2. Zones and notes
3. Layout
4. System chrome
5. Text
6. Controls and content
7. Overlays and glyphs
8. How each level treats each primitive
9. Patterns
10. Drawing rules

## 1. The template element

```html
<template data-screen="home" data-name="Home" data-device="phone"
          data-design="shots/home.png"
          data-summary="One sentence: what this screen is for, from the user's side.">
  ...board markup...
</template>
```

| Attribute | Required | Meaning |
|---|---|---|
| `data-name` | yes | Screen name shown in the screen picker and captions. |
| `data-summary` | yes | One sentence on the job of the screen. Shown in the notes rail. |
| `data-design` | yes, when you have it | Path to the screenshot, relative to the boards file. The build inlines it. |
| `data-screen` | no | Short id for links (`#screen=home`). Derived from the name when missing. |
| `data-device` | no | `phone` (390 × 844, default), `tablet` (820 × 1180), `desktop` / `web` (1440 × 900). |
| `data-width` | no | Board width in points when the design is not the device default (an iPhone 17 Pro is 402). |
| `data-height` | no | Set by the build from the image's aspect ratio. Set it yourself only when there is no image. |
| `data-radius` | no | Corner radius of the frame. Defaults to 44 for phones, 24 for tablets, 10 for desktop. |
| `data-present` | no | Present-mode order for this screen, such as `mid,design`. Defaults to `struct,low,mid,design`. |

Optional meta tags at the top of the boards file set the title, summary, starting level, and presentation order:

```html
<meta name="title" content="Clock a Timesheet">
<meta name="summary" content="How a host starts and stops a timesheet from Home">
<meta name="start-level" content="mid">   <!-- design, mid, low or struct -->
<meta name="present" content="struct,low,mid,design">   <!-- Present-mode order for every screen -->
```

The board is a flex column, `position: relative`, with `overflow: hidden`. Children stack top to bottom; give the scrolling middle part `wf-fill` so the tab bar sits at the bottom.

## 2. Zones and notes

Structure shows zones. Add these attributes to each top-level region:

| Attribute | Meaning |
|---|---|
| `data-zone="Today's bookings"` | Name of the part, in the words a stakeholder would use. Not a component name. |
| `data-purpose="Shows who the host meets today and when"` | The job it does, one short sentence, from the user's side. |
| `data-priority="1"` | `1` = the main job of the screen (darker fill, dark outline), `2` = supporting (default, light fill), `3` = minor (white, dashed outline). Aim for one or two `1`s per screen. |

Zones must not nest; only the outer one would show. Together they should cover everything a stakeholder needs to discuss. System chrome (status bar, home indicator) needs no zone.

A zone needs room for its label: about 44pt tall and most of the screen's width. For a single control (one button, one toggle), put the zone on the full-width row or area around it instead of on the control. On a screen with a sheet or dialog, give the dimmed content behind it one priority-3 zone ("Home, behind the card") so the Structure level is not blank there; skip it when only a thin strip shows.

The Structure level tidies zones by itself, so draw them where the regions really are and do not nudge them by hand: a zone within 28pt of a side edge lines up on the shared side margin (16pt, or 24pt on boards 700pt and wider), edges snap to a 4pt grid, every zone is at least 32pt each way, and neighbouring zones keep an 8pt gap. Order and rough position stay, so the blocks still line up with the other levels. A zone on a plain wrapper (no fill, border or shadow of its own, such as a `wf-pad` section) ignores the wrapper's top and bottom padding, so spacing a section with `padding-top` does not stretch its block; a zone on a card or list keeps the card's full edge. Labels sit top left; the purpose line is clamped to the room the block has and is always in the block's hover title.

Notes appear as numbered pins. Add `data-note="..."` where a supplied decision or open question helps the review. Use one sentence per note; do not add notes to meet a quota. Describe an unknown rationale neutrally instead of inventing intent. Keep purely visual details out of notes.

The pin sits just outside the element's top-right corner, so put notes on boxes (a row, card, button, chip group or zone) rather than on a bare line of text, where the pin would cover the end of the line. Pins that would land on top of each other are moved down automatically.

Add `data-keep` to retain real text at Low-fi, where body text normally becomes grey lines. Use it for essential words, such as a status that changes the screen's meaning.

## 3. Layout

| Class | What it is | Tuning (inline custom properties) |
|---|---|---|
| `wf-stack` | Vertical flex column | `--gap` (12px) |
| `wf-hstack` | Horizontal row, items centered | `--gap` (12px) |
| `wf-grid` | Equal columns | `--cols` (2), `--gap` |
| `wf-pad` | Padding on all sides | `--pad` (16px) |
| `wf-fill` | Takes the remaining height; use for the scrolling body | |
| `wf-spacer` | Pushes siblings apart in a stack or row | |
| `wf-carousel` | Horizontal row that runs off the edge | `--gap` |
| `wf-divider` | 1px rule | |
| `wf-sidebar` | Desktop side navigation column | `--w` (240px) |

You may also use inline `style` for size and position: `width`, `height`, `padding`, `margin`, `gap`, `flex`, `font-size`, `position`/`top`/`left`, `align-self`.

Some primitives have a minimum height so they look right without sizing: `wf-item` 56pt, `wf-btn` 50pt (`is-small` 34pt), `wf-input` and `wf-nav` 44pt, `wf-img` 40pt, `wf-chip` 32pt. An inline `height` overrides the minimum, so a 44pt row is just `style="height:44px"`.

## 4. System chrome

| Class | Notes |
|---|---|
| `wf-statusbar` | Phone status bar, 54pt. Empty element; draws "9:41" and signal glyphs itself. Add `data-time="4:06"` to match the screenshot's clock. iPhones with the Dynamic Island at 402 or 440pt wide (iPhone 16 Pro and 17 Pro) need `style="height:62px"`. |
| `wf-home` | Home indicator strip, 34pt. Put it last. Under a floating tab bar the visible gap is smaller; set `style="height:22px"` or whatever lines the tab bar up with the design. |
| `wf-nav` | Top bar row. Put `wf-title` inside for an inline title, and `wf-icon` or `wf-btn is-text` for bar buttons. |
| `wf-title` | Centered inline nav title. |
| `wf-tabbar` | Bottom tab bar. Children are `wf-tab`; mark the current one `is-active`. Add `is-floating` for a floating, rounded bar (iOS 26 style). |
| `wf-tab` | One tab; its text is the label. The icon is drawn for you. |

## 5. Text

| Class | Use | Low-fi |
|---|---|---|
| `wf-h1` | Large screen title (30pt) | kept |
| `wf-h2` | Section or sheet title (21pt) | kept |
| `wf-h3` | Card title (17pt) | kept |
| `wf-label` | Small uppercase section label | kept |
| `wf-text` | Body text (15pt) | grey lines |
| `wf-meta` | Secondary, smaller text (13pt) | lighter grey lines |
| `wf-display` | Large number or short figure, such as a timer or total (48pt, tabular digits) | kept |
| `wf-link` | Inline link inside text | follows its parent |

Set a different size with inline `font-size` when the design's text is clearly larger or smaller. `<b>` inside text is fine. Add `wf-truncate` to any text that the design cuts off with an ellipsis.

Field names in form and settings rows ("Starts", "Service Type") are structure, not content: give them `data-keep` so Low-fi still says which fields exist.

## 6. Controls and content

| Class | Modifiers | Notes |
|---|---|---|
| `wf-btn` | `is-secondary`, `is-text`, `is-small`, `is-pill`, `is-block` | Primary is solid ink. Use exactly one primary per screen where the design has one. The label is always kept. |
| `wf-icon` | `is-round` | Placeholder square for a meaningful icon. Size with `--size` (24px). Add `data-glyph` when the icon is a control whose symbol matters (see below). |
| `wf-avatar` | | Circle; put initials inside. Size with `--size` (44px). |
| `wf-img` | | Image, map, chart, video or illustration placeholder. Give it a height and `data-label="Map"`. Corner radius with `--radius`. |
| `wf-card` | `is-filled`, `is-row` | Bordered (or filled) container, a column by default; `is-row` lays its children out in a row. `--pad`, `--gap`, `--radius`. Do not combine with `wf-hstack` on the same element. |
| `wf-list` | `is-inset` | Wraps `wf-item` rows and draws separators. `is-inset` gives a grouped, filled background. |
| `wf-item` | | List row: leading `wf-icon`/`wf-avatar`, a `wf-item-body` with `wf-text` + `wf-meta`, trailing `wf-meta`, `wf-badge`, `wf-toggle` or `wf-chevron`. |
| `wf-item-body` | | Flexible text column inside a row. |
| `wf-chevron` | `is-down`, `is-updown` | Disclosure arrow; `is-down` for menus, `is-updown` for pickers. |
| `wf-input` | `is-search` | Text field; its text is the placeholder or value. |
| `wf-toggle` | `is-on` | Switch. |
| `wf-check` | `is-on`, `is-round` | Checkbox; `is-round` for a round selection marker. |
| `wf-chip` | `is-selected` | Filter or choice chip. |
| `wf-badge` | | Count badge. |
| `wf-tag` | | Small status label ("Now", "Draft", "Overdue"). Text is kept at Low-fi. |
| `wf-dot` | | Status dot (`--size`). |
| `wf-segmented` | children `is-selected` | Segmented control; each child is one segment. |
| `wf-progress` | | Progress bar; set `--value:40%`. |
| `wf-bubble` | `is-mine` | Chat bubble; put plain text inside. |

## 7. Overlays and glyphs

| Class | Notes |
|---|---|
| `wf-scrim` | Dims the screen behind a sheet or dialog. Place it after the screen content. |
| `wf-sheet` | Bottom sheet with a grabber, pinned to the bottom. Put it after the scrim. Add `no-grabber` when the design has none, and inline `top:` for a tall sheet. |
| `wf-overlay` | Full-screen absolute layer whose children sit at the bottom; use for custom floating panels. |
| `wf-fab` | Floating round action button; position with `--x` and `--y` (from right and bottom), size with `--size` (56px). |

For anything else that floats (a floating timer bar, a toast, a card that is not a bottom sheet), use a normal primitive with inline `position:absolute; left; right; top` or `bottom`. Cards, inset lists, inputs and bubbles stay opaque at every level, so a floating card covers the content behind it; draw the content behind it in full, as it is in the design.

### Glyphs

Icons default to blank placeholders. For controls whose symbol carries meaning, such as play, stop, or close, add `data-glyph` to the `wf-icon`, `wf-fab` or `wf-avatar`:

`play` `pause` `stop` `close` `down` `back` `plus` `check` `more` `search` `chat` `edit`

```html
<span class="wf-icon is-round" style="--size:44px" data-glyph="stop"></span>
<span class="wf-fab" style="--size:61px;--x:20px;--y:91px" data-glyph="play"></span>
```

Glyphs show at Mid-fi and Low-fi. Use them sparingly; most icons should stay blank.

## 8. How each level treats each primitive

| | Mid-fi | Low-fi | Structure |
|---|---|---|---|
| Layout and sizes | as drawn | identical | identical (zones keep their real size) |
| Headings, labels, buttons, tabs, chips | real text | real text | hidden |
| Body and meta text | real text | grey lines that follow each line's length | hidden |
| Fills (cards, icons, avatars, images) | light greys | outlines only | hidden |
| Primary button | solid ink | solid ink | hidden |
| Status bar, home indicator | drawn | blank | hidden |
| Zones | invisible | invisible | tidied labeled blocks, shaded by priority |
| Notes | pins | pins | pins |

Shared geometry keeps the screens aligned when switching levels.

## 9. Patterns

### Large-title screen with a list and tab bar

```html
<div class="wf-statusbar"></div>
<header class="wf-pad wf-stack" style="--gap:4px;padding-top:8px"
        data-zone="Header" data-purpose="Says where you are" data-priority="3">
  <p class="wf-meta">Tuesday, Oct 20</p>
  <h1 class="wf-h1">Clients</h1>
</header>
<div class="wf-pad" style="padding-block:0 8px" data-zone="Search" data-purpose="Finds a client by name" data-priority="2">
  <div class="wf-input is-search">Search clients</div>
</div>
<section class="wf-fill" data-zone="Client list" data-purpose="Every client the host works with" data-priority="1">
  <div class="wf-list">
    <div class="wf-item">
      <span class="wf-avatar">AL</span>
      <div class="wf-item-body"><p class="wf-text">Alex Lee</p><p class="wf-meta">Arrives Oct 28</p></div>
      <span class="wf-chevron"></span>
    </div>
  </div>
</section>
<nav class="wf-tabbar is-floating" data-zone="Tabs" data-purpose="Moves between the main areas" data-priority="3">
  <span class="wf-tab is-active">Home</span><span class="wf-tab">Clients</span><span class="wf-tab">Phone</span><span class="wf-tab">Profile</span>
</nav>
<div class="wf-home"></div>
```

### Inset grouped list (iOS settings style)

```html
<div class="wf-pad wf-stack" style="--gap:8px">
  <p class="wf-label">Details</p>
  <div class="wf-list is-inset">
    <div class="wf-item"><p class="wf-text wf-spacer">Starts</p><p class="wf-meta">Now</p><span class="wf-chevron"></span></div>
    <div class="wf-item"><p class="wf-text wf-spacer">End time</p><span class="wf-toggle"></span></div>
  </div>
</div>
```

### Modal sheet over a dimmed screen

```html
<div class="wf-statusbar"></div>
<div class="wf-fill"></div>
<div class="wf-scrim"></div>
<div class="wf-sheet" style="top:60px">
  <div class="wf-nav" style="padding:0"><span class="wf-icon is-round" style="--size:36px"></span><span class="wf-title">New Timesheet</span><span style="width:36px"></span></div>
  ...
</div>
```

### Chat

```html
<section class="wf-fill wf-stack wf-pad" style="--gap:8px;justify-content:flex-end" data-zone="Conversation" data-purpose="Messages with the client" data-priority="1">
  <div class="wf-bubble">Can we move the tour to Thursday?</div>
  <div class="wf-bubble is-mine">Yes, Thursday at 10 works.</div>
</section>
<div class="wf-pad wf-hstack" style="--gap:8px" data-zone="Reply" data-purpose="Writes back" data-priority="2">
  <div class="wf-input" style="flex:1">Message</div><span class="wf-icon is-round" style="--size:36px"></span>
</div>
```

### Floating button with its own zone

Place a floating button inside a full-width, absolutely positioned row at the button's height. Put the zone on that row to leave room for its label:

```html
<div style="position:absolute;left:0;right:0;bottom:91px;height:61px"
     data-zone="Start the clock" data-purpose="Opens New Timesheet" data-priority="1">
  <span class="wf-fab" style="--size:61px;--x:20px;--y:0px" data-glyph="play"></span>
</div>
```

### Carousel that runs off the edge of a card or sheet

Give the carousel a negative side margin equal to the container's padding, and the same padding inside, so chips scroll under the edge as in the design: `style="margin:0 -16px;padding:0 16px"`.

### Desktop page with a sidebar

```html
<template data-name="Dashboard" data-device="desktop" data-design="shots/dashboard.png" data-summary="...">
  <div class="wf-hstack" style="align-items:stretch;gap:0;height:100%">
    <aside class="wf-sidebar" data-zone="Navigation" data-purpose="Moves between sections" data-priority="3">
      <p class="wf-h3">Acme</p><p class="wf-text">Overview</p><p class="wf-text">Reports</p>
    </aside>
    <main class="wf-fill wf-stack wf-pad" style="--pad:32px;--gap:24px">
      <div data-zone="Key numbers" data-purpose="Shows this month's totals at a glance" data-priority="1" class="wf-grid" style="--cols:4">
        <div class="wf-card"><p class="wf-meta">Active moves</p><p class="wf-h2">128</p></div>
      </div>
      <div class="wf-img" style="height:320px" data-label="Chart" data-zone="Trend" data-purpose="Shows whether volume is rising" data-priority="2"></div>
    </main>
  </div>
</template>
```

## 10. Drawing rules

- Inline styles only for size, spacing and position. Never set color, background, font family, weight, shadow or opacity: the levels own those, and a hard-coded color leaks into every level.
- Use the primitives instead of inventing classes. The build warns about any unknown `wf-` class because it would render unstyled.
- Simplify while you draw. One primitive per thing that matters; drop decoration (background art, gradients, purely decorative icons and dividers).
- Use the design's words at Mid-fi. Replace every person's name, email, phone number, and address with sample values such as "Alex Morgan" or "Jordan Ellis". Replace distracting QA names such as "Qa Tester 12" too. Keep place, service, and product names.
