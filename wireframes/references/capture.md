# Capture the design

Save one image per screen in flow order in a `shots/` folder beside the boards file. PNG and JPEG both work. These images provide the Design view for comparison.

Measure the files before drawing:

```bash
python3 <skill-dir>/scripts/build.py --measure shots/*.png
# shots/home.png: 1206 x 2622 px | as phone: 402 pt wide at @3x, board height 874
```

Use the reported point width for the board. Set `data-width` if it differs from 390. Divide pixel measurements by the image scale factor.

## Supplied images

Copy files into `shots/` with short names in flow order, such as `01-home.png` and `02-new-timesheet.png`. If images are pasted in chat and cannot be saved, ask for files or a folder path. The build needs images on disk.

## Figma

With a connected Figma MCP:

1. Get frame node IDs from the URL or metadata tool. `node-id=12-345` corresponds to `12:345`.
2. Capture each frame and save it to `shots/`. If the tool only returns inline images that cannot be saved, ask for PNG exports at 2x.
3. Use design context or metadata for positions, sizes, and text. Figma frames use points, so top-level layer y positions and heights can supply region margins and heights directly.

Without MCP, ask for frame exports at 2x.

## Web pages and HTML

Use a browser tool that can save screenshots. If none is available, use installed headless Chrome:

```bash
# macOS; on Linux use google-chrome or chromium
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --window-size=390,844 --force-device-scale-factor=2 --virtual-time-budget=3000 \
  --screenshot=shots/home.png "https://example.com/page"
```

For desktop, use `--window-size=1440,900`. For a full page, set the height to the page height. If a state needs a click, use Playwright (`npx playwright screenshot ...`) or ask for screenshots.

## Claude artifacts

Read the link with the Artifact tool (`action: read`), save the HTML, and capture the file with headless Chrome. If it contains several screens, size the capture to one screen or crop it.

## Running iOS apps

Navigate to each screen before capturing:

```bash
xcrun simctl io booted screenshot shots/home.png
```

Deep links can use `xcrun simctl openurl booted '<scheme>://...'`. Current iPhone Simulator captures use @3x; an iPhone 17 Pro is 402pt wide.

## Running Android apps

```bash
adb exec-out screencap -p > shots/home.png
```

## Source without a running app

Ask whether the user can run the app or provide screenshots. If neither is possible and they agree, draw from source and omit `data-design`. The Design view will show a placeholder; explain that in the reply.
