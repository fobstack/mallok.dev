"""Structural checks for the built pages: python3 src/check.py"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')
PAGES = ['', 'features/', 'themes/', 'cost/', 'docs/', 'brand/']
PAGES = PAGES + ['zh-cn/' + p for p in PAGES]


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.imgs, self.h1, self.tags = [], [], [], 0, []
        self.html_lang = None
        self.head = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'html':
            self.html_lang = a.get('lang')
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        if tag in ('img', 'source'):
            self.imgs.append((a.get('src') or a.get('srcset'), a.get('alt'), tag))
        if tag == 'script':
            self.scripts.append(a.get('src'))
        if tag == 'h1':
            self.h1 += 1
        if tag in ('link', 'meta'):
            self.head.append(a)


def load(page):
    p = P()
    p.feed(open(os.path.join(ROOT, page, 'index.html'), encoding='utf-8').read())
    return p


def main():
    parsed = {pg: load(pg) for pg in PAGES}
    bad = []
    for pg, p in parsed.items():
        zh = pg.startswith('zh-cn/')
        want = 'zh-CN' if zh else 'en'
        if p.html_lang != want:
            bad.append((pg, 'lang', p.html_lang))
        if p.h1 != 1:
            bad.append((pg, 'h1 count', p.h1))
        # Only the pre-paint theme snippet and the header script are allowed.
        if sorted(p.scripts, key=str) != sorted([None, '/assets/site.js'], key=str):
            bad.append((pg, 'unexpected scripts', p.scripts))
        dup = {i for i in p.ids if p.ids.count(i) > 1}
        if dup:
            bad.append((pg, 'duplicate ids', sorted(dup)))
        rels = [(h.get('rel'), h.get('hreflang')) for h in p.head]
        for need in [('canonical', None), ('alternate', 'en'), ('alternate', 'zh-CN'), ('alternate', 'x-default')]:
            if need not in rels:
                bad.append((pg, 'missing link', need))
        props = [h.get('property') for h in p.head]
        for need in ('og:title', 'og:description', 'og:url', 'og:image'):
            if need not in props:
                bad.append((pg, 'missing', need))
        if '#main' not in p.links or 'main' not in p.ids:
            bad.append((pg, 'skip link'))
        for src, alt, tag in p.imgs:
            if tag == 'img' and alt is None:
                bad.append((pg, 'img without alt', src))
            if src and src.startswith('/') and not os.path.exists(os.path.join(ROOT, src.lstrip('/'))):
                bad.append((pg, 'missing file', src))
        for href in p.links:
            if href.startswith(('http://', 'https://', 'mailto:')):
                continue
            path, _, frag = href.partition('#')
            target = pg if path == '' else path.lstrip('/')
            if target.endswith('/') or target == '':
                if target not in parsed and not os.path.exists(os.path.join(ROOT, target, 'index.html')):
                    bad.append((pg, 'broken link', href))
                    continue
                if frag and target in parsed and frag not in parsed[target].ids:
                    bad.append((pg, 'broken fragment', href))
            elif not os.path.exists(os.path.join(ROOT, target)):
                bad.append((pg, 'broken link', href))
    for nf, want in (('404.html', 'en'), ('zh-cn/404.html', 'zh-CN')):
        p = P()
        p.feed(open(os.path.join(ROOT, nf), encoding='utf-8').read())
        robots = [h.get('content') for h in p.head if h.get('name') == 'robots']
        if p.html_lang != want or p.h1 != 1 or robots != ['noindex']:
            bad.append((nf, 'lang/h1/noindex', p.html_lang, p.h1, robots))
        if any(h.get('rel') == 'canonical' for h in p.head):
            bad.append((nf, 'canonical on a 404'))
        # Served at any URL, so every internal link must be absolute.
        for href in p.links + [src for src, _, _ in p.imgs]:
            if href and not href.startswith(('/', '#', 'http')):
                bad.append((nf, 'relative link', href))
    css = open(os.path.join(ROOT, 'assets', 'site.css'), encoding='utf-8').read()
    for u in re.findall(r'url\("?(/[^")]+)"?\)', css):
        if not os.path.exists(os.path.join(ROOT, u.lstrip('/'))):
            bad.append(('site.css', 'missing file', u))
    if re.search(r'https?://', re.sub(r'/\*.*?\*/', '', css, flags=re.S)):
        bad.append(('site.css', 'external URL in CSS'))
    for b in bad:
        print('FAIL', b)
    print(len(PAGES), 'pages checked;', len(bad), 'problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
