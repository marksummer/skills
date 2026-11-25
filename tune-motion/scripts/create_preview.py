#!/usr/bin/env python3
"""Create a focused in-chat motion editor from a component and pose renderer."""
import argparse
import html
import json
import math
import re
from html.parser import HTMLParser
from pathlib import Path

PRESETS = (
    'LINEAR', 'EASE_IN', 'EASE_OUT', 'EASE_IN_AND_OUT',
    'EASE_IN_BACK', 'EASE_OUT_BACK', 'EASE_IN_AND_OUT_BACK',
    'GENTLE', 'QUICK', 'BOUNCY', 'SLOW',
)
SPRINGS = {'GENTLE', 'QUICK', 'BOUNCY', 'SLOW'}


class ComponentMarkup(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag.lower() in {'script', 'iframe', 'object', 'embed', 'html', 'head', 'body'}:
            raise ValueError(f'Component markup must be a passive fragment; remove <{tag}>')
        if any(re.fullmatch(r'on[a-z]+', name.lower()) for name, _ in attrs):
            raise ValueError('Bind component events in the adapter, not inline HTML handlers')


def region(text, name, value, html_marker=False):
    start = f'<!-- motion:{name}:start -->' if html_marker else f'/* motion:{name}:start */'
    end = f'<!-- motion:{name}:end -->' if html_marker else f'/* motion:{name}:end */'
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f'Template has missing or ambiguous {name} region')
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + '\n' + value + '\n' + end + after


def js_json(value):
    # Keep user-provided names/descriptions from terminating an inline script.
    return json.dumps(value, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c').replace('>', '\\u003e')


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--name', required=True, help='Short component name')
    p.add_argument('--description', default='', help='Intended interaction and animated properties')
    p.add_argument('--key', help='Stable component identity for persisted settings')
    p.add_argument('--markup', type=Path, required=True, help='Component HTML/CSS fragment')
    p.add_argument('--adapter', type=Path, required=True, help='JS body returning a pose renderer')
    p.add_argument('--output', type=Path, required=True, help='Writable visualization fragment path')
    motion = p.add_mutually_exclusive_group()
    motion.add_argument('--preset', choices=PRESETS, help='Built-in easing or spring; default EASE_OUT')
    motion.add_argument('--bezier', type=float, nargs=4, metavar=('X1', 'Y1', 'X2', 'Y2'),
                        help='Custom cubic Bézier control points')
    motion.add_argument('--spring', type=float, nargs=3, metavar=('MASS', 'STIFFNESS', 'DAMPING'),
                        help='Custom spring parameters; duration is derived from them')
    p.add_argument('--duration', type=float, help='Bezier duration in ms; default 300')
    p.add_argument('--force', action='store_true', help='Replace an existing generated preview')
    return p


def create(args):
    name = args.name.strip()
    if not name:
        raise ValueError('Component name cannot be empty')
    key = args.key or re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    if not key or len(key) > 100 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', key):
        raise ValueError('Use a nonempty lowercase-hyphenated --key (at most 100 characters)')
    style = args.preset or 'EASE_OUT'
    curve = [0, 0, .58, 1]
    spring = {'mass': 1, 'stiffness': 100, 'damping': 15}
    if args.bezier is not None:
        x1, y1, x2, y2 = args.bezier
        if not (0 <= x1 <= 1 and 0 <= x2 <= 1 and -3 <= y1 <= 4 and -3 <= y2 <= 4):
            raise ValueError('Bézier x values must be between 0 and 1 and y values between -3 and 4')
        style = 'CUSTOM_CUBIC_BEZIER'
        curve = args.bezier
    if args.spring is not None:
        mass, stiffness, damping = args.spring
        if not (.1 <= mass <= 10 and 1 <= stiffness <= 10000 and 1 <= damping <= 1000):
            raise ValueError('Spring mass must be between 0.1 and 10, stiffness between 1 and 10000, and damping between 1 and 1000')
        style = 'CUSTOM_SPRING'
        spring = {'mass': mass, 'stiffness': stiffness, 'damping': damping}
    if (style in SPRINGS or style == 'CUSTOM_SPRING') and args.duration is not None:
        raise ValueError('Spring duration comes from physics; omit --duration')
    duration = 300 if args.duration is None else args.duration
    if not math.isfinite(duration) or not 100 <= duration <= 120000:
        raise ValueError('Duration must be finite and between 100 and 120000 ms')
    output = args.output.expanduser().resolve()
    template = Path(__file__).resolve().parents[1] / 'assets' / 'editor.html'
    if output == template.resolve():
        raise ValueError('Choose a task output path; do not overwrite the installed template')
    if output.exists() and not args.force:
        raise ValueError(f'Output exists: {output}; pass --force to update it')
    markup = args.markup.read_text(encoding='utf-8')
    adapter = args.adapter.read_text(encoding='utf-8')
    if not markup.strip() or not adapter.strip():
        raise ValueError('Component markup and adapter must both contain content')
    check = ComponentMarkup()
    check.feed(markup)
    check.close()
    if re.search(r'</script\b', adapter, re.I):
        raise ValueError('Adapter cannot contain a closing script tag')
    result = template.read_text(encoding='utf-8')
    result = region(result, 'title', html.escape(name), html_marker=True)
    result = region(result, 'scene', markup, html_marker=True)
    result = region(result, 'adapter', adapter)
    subject = {'key': key, 'name': name, 'description': args.description.strip()}
    result = region(result, 'subject', ' const subject=' + js_json(subject) + ';')
    initial = {'style': style, 'duration': duration, 'curve': curve, 'spring': spring}
    result = region(result, 'initial', js_json(initial))
    scene_label = args.description.strip() or f'Animated {name}'
    result = result.replace('aria-label="A large panel moves between start and finish to demonstrate the selected motion curve"',
                            'aria-label="' + html.escape(scene_label, quote=True) + '"', 1)
    if len(result.encode('utf-8')) > 1_000_000:
        raise ValueError('Preview exceeds the inline visualization size limit')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(result, encoding='utf-8')
    return output


def main():
    p = parser()
    args = p.parse_args()
    try:
        output = create(args)
    except (OSError, ValueError) as exc:
        p.exit(2, f'error: {exc}\n')
    print(output)


if __name__ == '__main__':
    main()
