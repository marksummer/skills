# Getting the design as images

The Design level is the anchor: stakeholders flip from it to the wireframes and back. Get one image per screen, in the order the flow runs, and save them in a `shots/` folder next to the boards file. PNG or JPEG both work.

After collecting them, run the measure helper to learn the size to draw each board at:

```bash
python3 <skill-dir>/scripts/build.py --measure shots/*.png
# shots/home.png: 1206 x 2622 px | as phone: 402 pt wide at @3x, board height 874
```

Draw the board at that point width (set `data-width` when it is not 390), and convert any pixel position you read off the image by dividing by the scale factor.

## Image files the user gave you

Copy them into `shots/` with short names in flow order (`01-home.png`, `02-new-timesheet.png`). If they are pasted into the chat rather than saved, ask for the files or a folder path; the build needs files on disk.

## Figma

If a Figma MCP server is connected:

1. Get the frame node ids from the URL (`node-id=12-345` means `12:345`) or with the metadata tool.
2. Use the screenshot tool for each frame and save the image to `shots/`. If the tool only returns the image inline and you cannot save it, ask the user to export the frames at 2x (select frames, Export, PNG 2x) into a folder.
3. Use the design-context or metadata tool for exact positions, sizes and text. Figma frames are already in points: take each top-level layer's y and height and use them directly as the region's margin and height. This replaces most measuring and makes the Design to Mid-fi toggle line up on the first build.

Without the MCP, ask the user to export the frames at 2x.

## A web page, local HTML file or HTML prototype

Use a browser automation tool if your environment has one that can save screenshots. Otherwise headless Chrome works anywhere Chrome is installed:

```bash
# macOS; on Linux use google-chrome or chromium
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --window-size=390,844 --force-device-scale-factor=2 --virtual-time-budget=3000 \
  --screenshot=shots/home.png "https://example.com/page"
```

Use `--window-size=1440,900` for desktop pages. For a full-length page, raise the height to the page height. If the page needs a click to reach a state, use Playwright (`npx playwright screenshot ...`) or ask the user for screenshots.

## A Claude artifact link

Read it with the Artifact tool (`action: read`), save the HTML to a file, then screenshot that file with headless Chrome as above. If the artifact draws several screens on one page, screenshot at a size that shows one screen, or crop.

## A running iOS app

```bash
xcrun simctl io booted screenshot shots/home.png
```

Navigate to each screen first (deep links: `xcrun simctl openurl booted '<scheme>://...'`). Simulator screenshots are @3x on current iPhones (402 pt wide on an iPhone 17 Pro).

## A running Android app

```bash
adb exec-out screencap -p > shots/home.png
```

## Only code, no running app

Ask whether the user can run it or share screenshots. If neither is possible and they accept it, draw the boards from the code and leave out `data-design`; the Design level then shows a placeholder. Say so in your reply.
