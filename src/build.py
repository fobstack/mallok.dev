"""Builds the mallok.dev prototype: python3 src/build.py

Writes the HTML pages (English and Simplified Chinese), the logo files and
the favicon, and regenerates the colour-token block in assets/site.css.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import brand  # noqa: E402
import cost  # noqa: E402
import docs  # noqa: E402
import features  # noqa: E402
import home  # noqa: E402
import layout  # noqa: E402
import notfound  # noqa: E402
import themes  # noqa: E402
import tokens  # noqa: E402
from layout import T  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')

PAGES = [
    ('/', home.build,
     lambda: T('Mallok — the Cloudflare-native CMS for multilingual B2B websites', 'Mallok —— 面向多语言 B2B 网站的 Cloudflare 原生 CMS'),
     lambda: T('An open-source WordPress and Ghost alternative that runs in your own Cloudflare account: Markdown content, a web admin, Liquid themes and inquiry forms, with no server and no rebuild to publish.',
               '开源的 WordPress / Ghost 替代方案，运行在你自己的 Cloudflare 账号里：Markdown 内容、网页后台、Liquid 主题和询盘表单，不用服务器，发布内容也不用重新构建。')),
    ('/features/', features.build,
     lambda: T('Features — Mallok', '功能 —— Mallok'),
     lambda: T('What Mallok 0.1 ships: Markdown content, multilingual URLs, Liquid themes, plugins, inquiries, a React admin, a CLI, built-in SEO — and what it deliberately leaves out.',
               'Mallok 0.1 包含的功能：Markdown 内容、多语言 URL、Liquid 主题、插件、询盘、React 后台、CLI、内置 SEO——以及有意不做的事。')),
    ('/themes/', themes.build,
     lambda: T('Themes — Mallok', '主题 —— Mallok'),
     lambda: T('The five Liquid themes bundled with Mallok — Atelier, Journal, Gazette, Manual and Folio — and how switching themes works.',
               'Mallok 内置的五套 Liquid 主题——Atelier、Journal、Gazette、Manual、Folio——以及切换主题的方式。')),
    ('/cost/', cost.build,
     lambda: T('Cost — the Cloudflare cost ladder — Mallok', '成本 —— Cloudflare 成本阶梯 —— Mallok'),
     lambda: T("Mallok is designed to start on Cloudflare's free allowances, with one paid step: Workers Paid at $5 a month per account. The full cost ladder, line by line.",
               'Mallok 以 Cloudflare 免费额度起步为设计目标，付费台阶只有一级：Workers Paid，每账号每月 5 美元。这里是逐项的成本阶梯。')),
    ('/docs/', docs.build,
     lambda: T('Docs — Mallok', '文档 —— Mallok'),
     lambda: T('Quick start for Mallok and a map of the documentation on GitHub: getting started, architecture, theme format, plugin API and CLI.',
               'Mallok 快速上手，以及 GitHub 文档导览：入门指南、架构、主题格式、插件 API 和 CLI。')),
    ('/brand/', brand.build,
     lambda: T('Brand — Mallok', '品牌 —— Mallok'),
     lambda: T("Mallok's brand kit: the Kinetic Thread logo, favicon set, usage rules, colour system and type.",
               'Mallok 品牌资料：“交织引线”标志、favicon 套件、使用规范、色彩体系与字体。')),
]


def write_tokens():
    path = os.path.join(ROOT, 'assets', 'site.css')
    css = open(path, encoding='utf-8').read()
    start = re.search(r'/\* tokens:start[^*]*\*/\n', css)
    end = css.index('/* tokens:end */')
    css = css[:start.end()] + tokens.css() + '\n' + css[end:]
    open(path, 'w', encoding='utf-8').write(css)


FONT_FILES = [
    # (file, unicode-range) — Figtree variable font, subsets as Google Fonts cuts them
    ('figtree-latin-ext.woff2',
     'U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, '
     'U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, '
     'U+2113, U+2C60-2C7F, U+A720-A7FF'),
    ('figtree-latin.woff2',
     'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, '
     'U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, '
     'U+FEFF, U+FFFD'),
]


def write_fonts():
    """Emits @font-face only for font files that exist, so nothing 404s."""
    path = os.path.join(ROOT, 'assets', 'site.css')
    css = open(path, encoding='utf-8').read()
    start = re.search(r'/\* fonts:start[^*]*\*/\n', css)
    end = css.index('/* fonts:end */')
    faces = []
    for name, urange in FONT_FILES:
        if os.path.exists(os.path.join(ROOT, 'assets', 'fonts', name)):
            faces.append(
                '@font-face {\n  font-family: Figtree;\n  font-style: normal;\n'
                '  font-weight: 300 900;\n  font-display: swap;\n'
                f'  src: url("/assets/fonts/{name}") format("woff2");\n'
                f'  unicode-range: {urange};\n}}\n')
    if not faces:
        print('note: assets/fonts/ has no Figtree files; using the system fallback stack')
    css = css[:start.end()] + '\n'.join(faces) + css[end:]
    open(path, 'w', encoding='utf-8').write(css)
    return bool(faces)


def main():
    failures = tokens.check()
    if failures:
        sys.exit(f'Contrast below AA: {failures}')
    write_tokens()
    write_fonts()
    for lang in ('en', 'zh'):
        layout.set_lang(lang)
        for path, build, title, description in PAGES:
            html = layout.page(path, title(), description(), build(), compact_cta=(path == '/'))
            out = os.path.join(ROOT, layout.url(path).strip('/'), 'index.html')
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'w', encoding='utf-8').write(html)
            print('wrote', os.path.relpath(out, ROOT), len(html))
        html = layout.page(
            '/', T('Page not found — Mallok', '页面不存在 —— Mallok'),
            T('This page does not exist on mallok.dev.', 'mallok.dev 上没有这个页面。'),
            notfound.build(), with_cta=False, not_found=True)
        out = os.path.join(ROOT, layout.url('/').strip('/'), '404.html')
        open(out, 'w', encoding='utf-8').write(html)
        print('wrote', os.path.relpath(out, ROOT), len(html))


if __name__ == '__main__':
    main()
