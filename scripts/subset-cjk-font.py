#!/usr/bin/env python3
"""Build the CJK subset of the post font.

The site ships TsangerJinKai03 W03 only for Chinese text inside posts. Latin
letters, digits and Latin punctuation are deliberately left out: they fall back
to Inter, which keeps the file small and avoids mixing two Latin designs.

Character set = every CJK character used in src/ + GB2312 level-1 (3755 common
characters, so new posts are covered) + Chinese punctuation.

Usage (needs `fonttools` and `brotli`):
    python scripts/subset-cjk-font.py
    python scripts/subset-cjk-font.py --source localres/fonts/cang-er-03-W03.woff2

The generated file is committed to public/fonts/; CI does not rebuild it.
"""

from __future__ import annotations

import argparse
import os
import sys

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')
DEFAULT_SOURCE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'localres', 'fonts', 'cang-er-03-W03.woff2'
)
DEFAULT_OUTPUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'public', 'fonts', 'TsangerJinKai03-W03-CJK.woff2'
)

# Chinese punctuation that has to travel with the Chinese glyphs, otherwise a
# comma or an em dash would be borrowed from the Latin fallback and look off.
PUNCTUATION_RANGES = [
    (0x00B7, 0x00B7),  # ·
    (0x2010, 0x2027),  # ‐ ‑ ‒ – — ― ‖ ‘ ’ “ ” „ … ‧
    (0x3000, 0x303F),  # CJK symbols and punctuation
    (0xFE10, 0xFE19),  # vertical forms
    (0xFE30, 0xFE4F),  # CJK compatibility forms
    (0xFF01, 0xFF0F),  # ！＂＃＄％＆＇（）＊＋，－．／
    (0xFF1A, 0xFF20),  # ：；＜＝＞？＠
    (0xFF3B, 0xFF40),  # ［＼］＾＿｀
    (0xFF5B, 0xFF60),  # ｛｜｝～
    (0xFFE0, 0xFFE6),  # ￠￡￤￥￦
]


def is_cjk(ch: str) -> bool:
    cp = ord(ch)
    return 0x3400 <= cp <= 0x4DBF or 0x4E00 <= cp <= 0x9FFF or 0xF900 <= cp <= 0xFAFF


def used_in_source() -> set[str]:
    chars: set[str] = set()
    exts = ('.md', '.mdx', '.astro', '.ts', '.json', '.yml', '.yaml')
    for dirpath, _, filenames in os.walk(SRC_DIR):
        for name in filenames:
            if not name.lower().endswith(exts):
                continue
            try:
                text = open(os.path.join(dirpath, name), encoding='utf-8').read()
            except OSError:
                continue
            chars.update(ch for ch in text if is_cjk(ch))
    return chars


def gb2312_level1() -> set[str]:
    chars: set[str] = set()
    for high in range(0xB0, 0xD8):
        for low in range(0xA1, 0xFF):
            try:
                ch = bytes([high, low]).decode('gb2312')
            except UnicodeDecodeError:
                continue
            if is_cjk(ch):
                chars.add(ch)
    return chars


def punctuation() -> set[str]:
    chars: set[str] = set()
    for start, end in PUNCTUATION_RANGES:
        chars.update(chr(cp) for cp in range(start, end + 1))
    return chars


def to_unicode_range(codepoints: list[int]) -> str:
    ranges: list[tuple[int, int]] = []
    for cp in sorted(codepoints):
        if ranges and cp == ranges[-1][1] + 1:
            ranges[-1] = (ranges[-1][0], cp)
        else:
            ranges.append((cp, cp))

    parts = []
    for start, end in ranges:
        parts.append(f'U+{start:X}' if start == end else f'U+{start:X}-{end:X}')
    return ', '.join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default=DEFAULT_SOURCE)
    parser.add_argument('--output', default=DEFAULT_OUTPUT)
    parser.add_argument('--print-range', action='store_true', help='print the unicode-range for fonts.css')
    args = parser.parse_args()

    try:
        from fontTools import subset
        from fontTools.ttLib import TTFont
    except ImportError:
        print('fonttools is missing: pip install fonttools brotli', file=sys.stderr)
        return 1

    if not os.path.exists(args.source):
        print(f'source font not found: {args.source}', file=sys.stderr)
        return 1

    wanted = used_in_source() | gb2312_level1() | punctuation()
    font = TTFont(args.source)
    available = {chr(cp) for cp in font.getBestCmap()}
    charset = sorted(wanted & available)

    text = ''.join(charset)
    options = subset.Options()
    options.flavor = 'woff2'
    options.layout_features = ['*']
    options.name_IDs = ['*']
    options.name_legacy = True
    options.name_languages = ['*']
    options.notdef_outline = True
    options.recalc_bounds = True
    options.drop_tables = ['DSIG']

    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text=text)
    subsetter.subset(font)

    # Guard against Latin leaking back in through a future edit of the charset.
    latin = [ch for ch in charset if ch.isascii()]
    if latin:
        print(f'ASCII characters in subset: {"".join(latin)!r}', file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    font.flavor = 'woff2'
    font.save(args.output)
    font.close()

    source_size = os.path.getsize(args.source)
    output_size = os.path.getsize(args.output)
    print(f'chars     : {len(charset)}')
    print(f'output    : {args.output}')
    print(f'size      : {output_size / 1024:.0f} KB (source {source_size / 1048576:.2f} MB)')

    if args.print_range:
        print('unicode-range:')
        print('  ' + to_unicode_range([ord(ch) for ch in charset]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
