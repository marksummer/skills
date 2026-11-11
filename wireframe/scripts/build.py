#!/usr/bin/env python3
"""Build a self-contained wireframe viewer from a boards file.

    python3 build.py BOARDS.html [--out FILE.html] [--title T] [--summary S] [--start mid] [--open]
    python3 build.py BOARDS.html --snap [SCREEN_ID ...]
    python3 build.py --measure IMAGE [IMAGE ...]

The boards file holds one <template> per screen (see references/primitives.md).
This script inlines each screen's design image, sets each board's height from
the image's aspect ratio, checks the boards for common mistakes, and writes one
HTML file that opens in any browser and can be published as-is.

--snap also renders one check image per screen with headless Chrome (or
Chromium, Edge, Brave; set CHROME=/path to choose): Design | Overlay | Mid-fi |
Low-fi | Structure, side by side, saved in a snap/ folder next to the page.

Only the Python 3 standard library is used. On macOS, `sips` shrinks large
screenshots; elsewhere Pillow is used when installed.
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import html
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import time
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.normpath(os.path.join(HERE, "..", "assets", "viewer.html"))
DEVICE_WIDTH = {"phone": 390, "tablet": 820, "desktop": 1440, "web": 1440}
DEVICE_HEIGHT = {"phone": 844, "tablet": 1180, "desktop": 900, "web": 900}
LEVELS = {"design", "mid", "low", "struct", "structure"}
MAX_TOTAL = 15 * 1024 * 1024
STYLE_FORBIDDEN = re.compile(r"(^|;)\s*(color|background(-color|-image)?|font-family|font-weight|box-shadow|border(-[a-z]+)?-color|opacity|filter)\s*:", re.I)
ATTR_RE = re.compile(r'([^\s=/>]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+)))?')
TEMPLATE_RE = re.compile(r"<template\b([^>]*)>(.*?)</template>", re.S | re.I)
META_RE = re.compile(r'<meta\s+name="(title|summary|start-level|present)"\s+content="([^"]*)"\s*/?>\s*', re.I)


def warn(msg: str) -> None:
    print("  ! " + msg)


# ---------- images ----------

def image_size(data: bytes):
    """Return (width, height) for PNG, JPEG, GIF or WebP bytes, else None."""
    if data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) >= 24:
        return struct.unpack(">II", data[16:24])
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return struct.unpack("<HH", data[6:10])
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        chunk = data[12:16]
        if chunk == b"VP8X":
            w = 1 + int.from_bytes(data[24:27], "little")
            h = 1 + int.from_bytes(data[27:30], "little")
            return w, h
        if chunk == b"VP8 ":
            w, h = struct.unpack("<HH", data[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if chunk == b"VP8L":
            b = data[21:25]
            w = 1 + (((b[1] & 0x3F) << 8) | b[0])
            h = 1 + (((b[3] & 0x0F) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
            return w, h
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


def mime_for(data: bytes) -> str:
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if data[:2] == b"\xff\xd8":
        return "image/jpeg"
    if data[:4] == b"RIFF":
        return "image/webp"
    if data[:3] == b"GIF":
        return "image/gif"
    return "application/octet-stream"


def guess_points(px_w: int, device: str):
    """Guess the point width and scale factor of a screenshot."""
    ranges = {"phone": (320, 440), "tablet": (700, 1100)}
    lo, hi = ranges.get(device, (900, 2000))
    for scale in (3, 2, 1):
        w = px_w / scale
        if lo <= w <= hi and abs(w - round(w)) < 0.01:
            return int(round(w)), scale
    for scale in (3, 2, 1):
        w = px_w / scale
        if lo <= w <= hi:
            return int(round(w)), scale
    return None, None


def shrink(path: str, data: bytes, max_w: int):
    """Return smaller image bytes when the image is wider than max_w, else the original."""
    size = image_size(data)
    if not size or size[0] <= max_w:
        return data
    tmpdir = tempfile.mkdtemp(prefix="wf-")
    out = os.path.join(tmpdir, "shot.jpg")
    try:
        if shutil.which("sips"):
            subprocess.run(["sips", "--resampleWidth", str(max_w), "-s", "format", "jpeg",
                            "-s", "formatOptions", "86", path, "--out", out],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            with open(out, "rb") as f:
                return f.read()
        try:
            from PIL import Image  # type: ignore
        except ImportError:
            return data
        im = Image.open(path).convert("RGB")
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        im.save(out, "JPEG", quality=86)
        with open(out, "rb") as f:
            return f.read()
    except Exception as exc:  # keep the original on any failure
        warn("could not shrink %s (%s); embedding it at full size" % (path, exc))
        return data
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# ---------- board checks ----------

class BoardCheck(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self, known):
        super().__init__(convert_charrefs=True)
        self.known = known
        self.stack = []  # bool per open element: is a zone
        self.zones = 0
        self.nested = []
        self.notes = 0
        self.unknown = set()
        self.styles = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for cls in (a.get("class") or "").split():
            if cls.startswith("wf-") and cls not in self.known:
                self.unknown.add(cls)
        style = a.get("style") or ""
        if STYLE_FORBIDDEN.search(style):
            self.styles.append(style.strip())
        is_zone = "data-zone" in a
        if is_zone:
            if any(self.stack):
                self.nested.append(a.get("data-zone"))
            else:
                self.zones += 1
        if "data-note" in a:
            self.notes += 1
        if tag not in self.VOID:
            self.stack.append(is_zone)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID and self.stack:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag not in self.VOID and self.stack:
            self.stack.pop()


def parse_attrs(raw: str):
    attrs = []
    for m in ATTR_RE.finditer(raw):
        name = m.group(1)
        val = m.group(2) if m.group(2) is not None else m.group(3) if m.group(3) is not None else m.group(4)
        attrs.append([name, val])
    return attrs


def render_attrs(attrs) -> str:
    out = []
    for name, val in attrs:
        out.append(name if val is None else '%s="%s"' % (name, val.replace('"', "&quot;")))
    return (" " + " ".join(out)) if out else ""


def get(attrs, name):
    for k, v in attrs:
        if k == name:
            return v
    return None


def put(attrs, name, value):
    for pair in attrs:
        if pair[0] == name:
            pair[1] = value
            return
    attrs.append([name, value])


# ---------- snapshots ----------

def find_chrome():
    cands = [os.environ.get("CHROME")]
    cands += [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    ]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "brave-browser", "chrome"):
        cands.append(shutil.which(name))
    for c in cands:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


def snap(out: str, boards, only) -> None:
    """Render Design | Overlay | Mid-fi | Low-fi | Structure for each screen into snap/<id>.png."""
    chrome = find_chrome()
    if not chrome:
        warn("--snap needs Chrome, Chromium, Edge or Brave (or CHROME=/path/to/browser). Check the page in a browser instead, using the Overlay view.")
        return
    todo = [b for b in boards if not only or b[0] in only]
    missing = sorted(set(only or []) - {b[0] for b in boards})
    if missing:
        warn("no screen with id %s (ids: %s)" % (", ".join(missing), ", ".join(b[0] for b in boards)))
    if not todo:
        return
    snap_dir = os.path.join(os.path.dirname(out), "snap")
    os.makedirs(snap_dir, exist_ok=True)
    uri = Path(out).as_uri()
    started = time.time()

    def one(board):
        sid, w, h = board
        cols, gap = 5, 32
        row_w = cols * w + gap * (cols - 1)
        scale = min(1.0, 2400.0 / row_w)
        width = int(row_w * scale) + 48 + 16
        height = int(h * scale) + 16 + 32 + 30 + 20 + 16
        png = os.path.join(snap_dir, sid + ".png")
        profile = tempfile.mkdtemp(prefix="wf-chrome-")
        cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
               "--no-default-browser-check", "--force-device-scale-factor=1",
               "--blink-settings=preferredColorScheme=1", "--user-data-dir=" + profile,
               "--window-size=%d,%d" % (width, height), "--virtual-time-budget=4000",
               "--screenshot=" + png, "%s#screen=%s&snap=1&snapscale=%.3f" % (uri, sid, scale)]
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        except subprocess.TimeoutExpired:
            pass
        finally:
            shutil.rmtree(profile, ignore_errors=True)
        return png if os.path.isfile(png) else None

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(one, todo))
    print("Snapshots, %.0fs (each: Design | Overlay | Mid-fi | Low-fi | Structure):" % (time.time() - started))
    for board, png in zip(todo, results):
        print("  " + (png or "! %s failed to render" % board[0]))


# ---------- commands ----------

def measure(paths) -> int:
    for p in paths:
        try:
            with open(p, "rb") as f:
                data = f.read()
        except OSError as exc:
            print("%s: cannot read (%s)" % (p, exc))
            continue
        size = image_size(data)
        if not size:
            print("%s: unknown image format" % p)
            continue
        w, h = size
        line = "%s: %d x %d px" % (p, w, h)
        for device in ("phone", "tablet"):
            pts, scale = guess_points(w, device)
            if pts:
                line += " | as %s: %d pt wide at @%dx, board height %d" % (device, pts, scale, round(h / scale))
                break
        print(line)
    return 0


def build(args) -> int:
    boards_path = os.path.abspath(args.boards)
    base = os.path.dirname(boards_path)
    with open(boards_path, encoding="utf-8") as f:
        src = f.read()
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()

    style_block = tpl.split("</style>", 1)[0]
    known = set(re.findall(r"\.(wf-[a-z0-9-]+)", style_block)) | {"wf-item-body"}

    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    meta = {k.lower(): v for k, v in META_RE.findall(src)}
    src = META_RE.sub("", src)
    title = args.title or meta.get("title") or "Wireframes"
    summary = args.summary if args.summary is not None else meta.get("summary", "")
    start = (args.start or meta.get("start-level") or "mid").lower()
    if start not in LEVELS:
        warn("unknown start level %r; using mid" % start)
        start = "mid"

    print("Building %s" % title)
    total_img = 0
    screens = 0
    snap_boards = []

    def fix_template(m):
        nonlocal total_img, screens
        screens += 1
        attrs = parse_attrs(m.group(1))
        body = m.group(2)
        name = get(attrs, "data-name") or ("screen %d" % screens)
        device = get(attrs, "data-device") or "phone"
        if device not in DEVICE_WIDTH:
            warn("%s: unknown data-device %r (use phone, tablet, desktop or web)" % (name, device))
            device = "phone"
        if not get(attrs, "data-screen"):
            put(attrs, "data-screen", re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "screen-%d" % screens)
        if not get(attrs, "data-name"):
            warn("screen %d has no data-name" % screens)
        width = get(attrs, "data-width")
        board_w = int(float(width)) if width else DEVICE_WIDTH[device]

        design = get(attrs, "data-design")
        if not design:
            warn("%s: no data-design image, so the Design level shows a placeholder" % name)
        elif design.startswith(("http://", "https://")):
            warn("%s: data-design is a web address. Download the image and point to the file; published pages block remote images" % name)
        elif not design.startswith("data:"):
            path = design if os.path.isabs(design) else os.path.join(base, design)
            if not os.path.isfile(path):
                warn("%s: design image not found: %s" % (name, design))
            else:
                with open(path, "rb") as f:
                    data = f.read()
                size = image_size(data)
                if size and not width:
                    pts, scale = guess_points(size[0], device)
                    if pts and pts != board_w:
                        warn("%s: the image looks %d pt wide (@%dx). Set data-width=\"%d\" if the board was drawn at that width" % (name, pts, scale, pts))
                if size and not get(attrs, "data-height"):
                    put(attrs, "data-height", str(round(board_w * size[1] / size[0])))
                data = shrink(path, data, board_w * 2)
                total_img += len(data)
                put(attrs, "data-design", "data:%s;base64,%s" % (mime_for(data), base64.b64encode(data).decode("ascii")))
        if not get(attrs, "data-height") and device in DEVICE_HEIGHT:
            put(attrs, "data-height", str(DEVICE_HEIGHT[device]))
        snap_boards.append((get(attrs, "data-screen"), board_w, int(float(get(attrs, "data-height")))))

        check = BoardCheck(known)
        check.feed(body)
        if not get(attrs, "data-summary"):
            warn("%s: add data-summary, one sentence on what this screen is for" % name)
        if check.zones == 0:
            warn("%s: no data-zone regions, so the Structure level will be blank" % name)
        if check.nested:
            warn("%s: zones inside zones (%s); only the outer zone shows in Structure" % (name, ", ".join(check.nested)))
        if check.notes > 7:
            warn("%s: %d notes; keep it to the few that matter (2 to 6)" % (name, check.notes))
        for cls in sorted(check.unknown):
            warn("%s: unknown class %s (typo, or not a primitive; it will have no styling)" % (name, cls))
        for st in check.styles[:5]:
            warn("%s: inline style sets color, font or effects (%s); keep inline styles to size and spacing so every level stays clean" % (name, st))
        return "<template%s>%s</template>" % (render_attrs(attrs), body)

    boards = TEMPLATE_RE.sub(fix_template, src)
    if screens == 0:
        warn("no <template> boards found in %s" % args.boards)

    out_html = (tpl
                .replace("{{TITLE}}", html.escape(title, quote=False))
                .replace("{{TITLE_ATTR}}", html.escape(title))
                .replace("{{SUMMARY_ATTR}}", html.escape(summary))
                .replace("{{DATE_ATTR}}", _dt.date.today().isoformat())
                .replace("{{START_ATTR}}", html.escape(start))
                .replace("{{PRESENT_ATTR}}", html.escape(args.present or meta.get("present", "")))
                .replace("<!--WF:BOARDS-->", boards.strip()))

    out = os.path.abspath(args.out or os.path.join(base, re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-").lower() + ".html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(out_html)
    size = os.path.getsize(out)
    print("  %d screen%s, %.1f MB (images %.1f MB)" % (screens, "" if screens == 1 else "s", size / 1e6, total_img / 1e6))
    if size > MAX_TOTAL:
        warn("the file is over 15 MB; drop or crop the largest screenshots before publishing")
    print("Wrote " + out)
    if args.snap is not None:
        snap(out, snap_boards, args.snap)
    if args.open:
        webbrowser.open("file://" + out)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build a wireframe viewer from a boards file.")
    ap.add_argument("boards", nargs="?", help="boards file with one <template> per screen")
    ap.add_argument("--out", help="output HTML path (default: next to the boards file)")
    ap.add_argument("--title", help="page title (default: <meta name=\"title\"> in the boards file)")
    ap.add_argument("--summary", help="one line under the title")
    ap.add_argument("--start", help="level the page opens on: design, mid, low or struct (default mid)")
    ap.add_argument("--present", help="Present mode order per screen, e.g. struct,low,mid,design (the default)")
    ap.add_argument("--open", action="store_true", help="open the result in the default browser")
    ap.add_argument("--snap", nargs="*", metavar="SCREEN_ID", help="also render a check image per screen (all screens, or only the ids given) into snap/")
    ap.add_argument("--measure", nargs="+", metavar="IMAGE", help="print screenshot sizes and the board size to draw at")
    args = ap.parse_args(argv)
    if args.measure:
        return measure(args.measure)
    if not args.boards:
        ap.error("give a boards file, or --measure IMAGE")
    return build(args)


if __name__ == "__main__":
    sys.exit(main())
