"""Inline SVG illustrations: theme mockups and diagrams.

The four theme mockups use each theme's real light palette, read from
src/themes/<id>/assets/style.css. They are illustrations, not screenshots,
and every use is labelled as such.
"""

from layout import T

SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif"
SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', 'Songti SC', serif"
MONO = "ui-monospace, Menlo, Consolas, monospace"


def _bars(x, y, widths, color, h=6, gap=13):
    out = ''
    for i, w in enumerate(widths):
        out += f'<rect x="{x}" y="{y + i * gap}" width="{w}" height="{h}" rx="3" fill="{color}"/>'
    return out


def journal():
    label = T('Illustration of the Journal theme: a quiet single-column article list.',
              'Journal 主题示意图：安静的单栏文章列表。')
    entries = ''
    rows = [
        (118, '2026-08-14', 'Notes on a slower release cycle', [330, 300, 210]),
        (214, '2026-07-30', 'What we learned from ten audits', [320, 335, 180]),
        (310, '2026-07-02', 'Writing specifications people read', [335, 290, 240]),
    ]
    for y, date, title, bars in rows:
        entries += (
            f'<text x="150" y="{y}" font-family="{MONO}" font-size="10" fill="#6b7280">{date}</text>'
            f'<text x="150" y="{y + 22}" font-family="{SANS}" font-size="17" font-weight="700" fill="#1f2937">{title}</text>'
            + _bars(150, y + 34, bars, '#e5e7eb')
            + f'<text x="490" y="{y}" text-anchor="end" font-family="{SANS}" font-size="10" fill="#1d4ed8">4 min read</text>'
        )
    return f'''<svg viewBox="0 0 640 420" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">
<rect width="640" height="420" fill="#ffffff"/>
<text x="150" y="52" font-family="{SANS}" font-size="16" font-weight="700" fill="#1f2937">Field Notes</text>
<text x="490" y="52" text-anchor="end" font-family="{SANS}" font-size="11" fill="#6b7280">Articles   About   RSS</text>
<rect x="150" y="72" width="340" height="1" fill="#e5e7eb"/>
{entries}
<rect x="150" y="196" width="340" height="1" fill="#e5e7eb"/>
<rect x="150" y="292" width="340" height="1" fill="#e5e7eb"/>
<rect x="150" y="388" width="340" height="1" fill="#e5e7eb"/>
</svg>'''


def gazette():
    label = T('Illustration of the Gazette theme: serif masthead, lead story with art, a latest rail and a subscribe band.',
              'Gazette 主题示意图：衬线报头、带配图的头条、最新消息栏和订阅横幅。')
    rail = ''
    items = ['Licence quotas tighten', 'Sponge prices steady',
             'New mill capacity', 'Freight index eases']
    for i, title in enumerate(items):
        y = 166 + i * 44
        rail += (
            f'<text x="440" y="{y}" font-family="{MONO}" font-size="9" fill="#5e5e64">0{i + 1}</text>'
            f'<text x="462" y="{y}" font-family="{SERIF}" font-size="12.5" font-weight="700" fill="#16171a">{title}</text>'
            f'<rect x="462" y="{y + 9}" width="{120 - i * 12}" height="5" rx="2.5" fill="#ebebe8"/>'
            f'<rect x="440" y="{y + 24}" width="170" height="1" fill="#ebebe8"/>'
        )
    return f'''<svg viewBox="0 0 640 420" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="gz-art" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2c3e8e"/><stop offset="1" stop-color="#5a6fc9"/></linearGradient></defs>
<rect width="640" height="420" fill="#ffffff"/>
<text x="30" y="26" font-family="{MONO}" font-size="9" fill="#5e5e64">VOL. 12 · TRADE EDITION</text>
<text x="610" y="26" text-anchor="end" font-family="{SANS}" font-size="10" font-weight="700" fill="#a11d33">Subscribe</text>
<text x="320" y="72" text-anchor="middle" font-family="{SERIF}" font-size="36" font-weight="700" fill="#16171a" letter-spacing="-1">The Gazette</text>
<rect x="30" y="90" width="580" height="2" fill="#16171a"/>
<rect x="30" y="95" width="580" height="1" fill="#16171a"/>
<text x="320" y="116" text-anchor="middle" font-family="{SANS}" font-size="10" font-weight="600" fill="#5a5b61" letter-spacing="1.2">MARKETS    POLICY    LOGISTICS    TECHNOLOGY    OPINION</text>
<rect x="30" y="128" width="580" height="1" fill="#ebebe8"/>
<rect x="30" y="146" width="380" height="150" fill="url(#gz-art)"/>
<path d="M30 296l110-70 80 40 90-80 100 62v48z" fill="#ffffff" opacity=".14"/>
<circle cx="350" cy="184" r="20" fill="#ffffff" opacity=".2"/>
<text x="30" y="318" font-family="{SANS}" font-size="9.5" font-weight="700" fill="#a11d33" letter-spacing="1.2">MARKETS</text>
<text x="30" y="343" font-family="{SERIF}" font-size="21" font-weight="700" fill="#16171a">Specialty metals open the week</text>
<text x="30" y="367" font-family="{SERIF}" font-size="21" font-weight="700" fill="#16171a">on firmer footing</text>
<text x="440" y="146" font-family="{SANS}" font-size="9.5" font-weight="700" fill="#a11d33" letter-spacing="1.2">LATEST</text>
{rail}
<rect x="0" y="384" width="640" height="36" fill="#16171a"/>
<text x="30" y="407" font-family="{SERIF}" font-size="13" font-weight="700" fill="#ffffff">The morning wire, 06:30 daily.</text>
<rect x="528" y="392" width="82" height="20" rx="2" fill="#a11d33"/>
<text x="569" y="406" text-anchor="middle" font-family="{SANS}" font-size="10" font-weight="700" fill="#ffffff">Subscribe</text>
</svg>'''


def manual():
    label = T('Illustration of the Manual theme: centred hero, three quick-start cards and guide rows.',
              'Manual 主题示意图：居中的首屏、三张快速上手卡片和指南列表。')
    cards = ''
    for i, (title, w) in enumerate([('Install', 110), ('Configure', 96), ('Maintain', 120)]):
        x = 60 + i * 180
        cards += (
            f'<rect x="{x}" y="176" width="160" height="92" rx="8" fill="#ffffff" stroke="#e2e2df"/>'
            f'<rect x="{x + 14}" y="190" width="26" height="18" rx="4" fill="#ffedd5"/>'
            f'<text x="{x + 27}" y="203" text-anchor="middle" font-family="{MONO}" font-size="9.5" font-weight="700" fill="#9a3412">0{i + 1}</text>'
            f'<text x="{x + 14}" y="230" font-family="{SANS}" font-size="13.5" font-weight="700" fill="#1a1c1e">{title}</text>'
            + _bars(x + 14, 241, [w, w - 28], '#ececea', h=5, gap=10)
        )
    rows = ''
    for i, title in enumerate(['Commissioning checklist', 'Routine inspection', 'Troubleshooting faults']):
        y = 300 + i * 36
        rows += (
            f'<rect x="60" y="{y}" width="520" height="1" fill="#ececea"/>'
            f'<text x="60" y="{y + 23}" font-family="{MONO}" font-size="10" fill="#c2410c">{i + 1}.0</text>'
            f'<text x="96" y="{y + 23}" font-family="{SANS}" font-size="12.5" font-weight="600" fill="#1a1c1e">{title}</text>'
            f'<path d="M570 {y + 14}l5 5-5 5" fill="none" stroke="#666a6f" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
        )
    return f'''<svg viewBox="0 0 640 420" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">
<rect width="640" height="420" fill="#ffffff"/>
<rect width="640" height="160" fill="#fdf7f2"/>
<rect x="60" y="20" width="14" height="14" rx="3" fill="#c2410c"/>
<text x="82" y="32" font-family="{SANS}" font-size="13" font-weight="700" fill="#1a1c1e">Handbook</text>
<text x="580" y="32" text-anchor="end" font-family="{SANS}" font-size="10.5" fill="#565a5e">Guides    Reference    Changelog</text>
<rect x="268" y="62" width="104" height="20" rx="10" fill="#ffedd5"/>
<text x="320" y="76" text-anchor="middle" font-family="{SANS}" font-size="10" font-weight="700" fill="#9a3412">Documentation</text>
<text x="320" y="114" text-anchor="middle" font-family="{SANS}" font-size="27" font-weight="700" fill="#1a1c1e" letter-spacing="-0.8">Operator handbook</text>
<rect x="210" y="128" width="220" height="6" rx="3" fill="#e2e2df"/>
<rect x="250" y="141" width="140" height="6" rx="3" fill="#e2e2df"/>
{cards}
{rows}
<rect x="60" y="408" width="520" height="1" fill="#ececea"/>
</svg>'''


def folio():
    label = T('Illustration of the Folio theme: oversized serif intro, full-bleed featured project and an editorial grid.',
              'Folio 主题示意图：超大衬线引言、通栏精选项目和编辑式网格。')
    grid = ''
    fills = ['#d9cfc0', '#c9b9a6', '#e3ddd2']
    names = ['Reading room', 'Courtyard house', 'Oak series']
    for i in range(3):
        x = 34 + i * 194
        grid += (
            f'<rect x="{x}" y="318" width="184" height="66" fill="{fills[i]}"/>'
            f'<text x="{x}" y="402" font-family="{SERIF}" font-size="12.5" fill="#1c1a17">{names[i]}</text>'
            f'<text x="{x + 184}" y="402" text-anchor="end" font-family="{MONO}" font-size="9" fill="#6b665e">0{i + 2}</text>'
        )
    return f'''<svg viewBox="0 0 640 420" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="fo-art" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7a2b33"/><stop offset="1" stop-color="#5e1f26"/></linearGradient></defs>
<rect width="640" height="420" fill="#faf8f4"/>
<text x="34" y="34" font-family="{SANS}" font-size="12" font-weight="600" fill="#1c1a17">Studio</text>
<text x="606" y="34" text-anchor="end" font-family="{SANS}" font-size="11" fill="#6f6a62">Work    Journal    <tspan fill="#7a2b33" font-weight="600">Enquire</tspan></text>
<text x="606" y="74" text-anchor="end" font-family="{MONO}" font-size="9" fill="#6b665e">SELECTED WORK · 2024–2026</text>
<text x="34" y="98" font-family="{SERIF}" font-size="34" fill="#1c1a17" letter-spacing="-0.8">Objects, interiors and</text>
<text x="34" y="136" font-family="{SERIF}" font-size="34" font-style="italic" fill="#1c1a17" letter-spacing="-0.8">considered spaces.</text>
<rect x="0" y="160" width="640" height="138" fill="url(#fo-art)"/>
<rect x="392" y="182" width="150" height="116" fill="#faf8f4" opacity=".12"/>
<circle cx="470" cy="214" r="34" fill="#faf8f4" opacity=".16"/>
<text x="34" y="262" font-family="{MONO}" font-size="9" fill="#faf8f4" opacity=".85">01 — FEATURED</text>
<text x="34" y="284" font-family="{SERIF}" font-size="20" fill="#faf8f4">Harbour pavilion</text>
{grid}
</svg>'''


def pipeline():
    """Two-stage rendering diagram for the Features page."""
    label = T(
        'Diagram of two-stage rendering. Stage one runs on save: Markdown is parsed, sanitised and stored as an HTML fragment in D1. Stage two runs on a cache miss: the fragment and the Liquid theme produce the full page, which is stored in the edge cache.',
        '两阶段渲染示意图。第一阶段在保存时执行：解析 Markdown、净化并把 HTML 片段写入 D1。第二阶段在缓存未命中时执行：片段加 Liquid 主题生成完整页面，并写入边缘缓存。')
    s1 = T('STAGE ONE · ON SAVE', '第一阶段 · 保存时')
    s2 = T('STAGE TWO · ON REQUEST (CACHE MISS)', '第二阶段 · 请求时（缓存未命中）')
    b = [
        (T('Markdown', 'Markdown'), T('+ YAML front matter', '+ YAML front matter')),
        (T('Parse + sanitise', '解析 + 净化'), T('remark / rehype, allow-list', 'remark / rehype，白名单')),
        (T('Resolve media', '解析媒体路径'), T('images/ → R2 URLs, srcset', 'images/ → R2 地址、srcset')),
        (T('HTML fragment', 'HTML 片段'), T('D1 render_cache (derived)', 'D1 render_cache（派生数据）')),
    ]
    c = [
        (T('Fragment + data', '片段 + 数据'), T('bounded D1 batches', '有界的 D1 批量查询')),
        (T('Liquid theme', 'Liquid 主题'), T('templates ship in the Worker', '模板随 Worker 打包')),
        (T('Full page', '完整页面'), T('Cache-Control + Cache-Tag', 'Cache-Control + Cache-Tag')),
        (T('Edge cache', '边缘缓存'), T('cache.put(), purge by tag', 'cache.put()，按标签清除')),
    ]

    def row(items, y, cls):
        out = ''
        for i, (title, sub) in enumerate(items):
            x = 24 + i * 232
            last = i == len(items) - 1
            out += (
                f'<rect x="{x}" y="{y}" width="196" height="62" rx="8" class="{cls if last else "f-paper"}" stroke-width="1" style="stroke:var(--line-strong)"/>'
                f'<text x="{x + 14}" y="{y + 26}" class="t-sans f-ink">{title}</text>'
                f'<text x="{x + 14}" y="{y + 45}" class="t-mono f-muted" style="font-size:10.5px">{sub}</text>'
            )
            if not last:
                out += (
                    f'<path d="M{x + 200} {y + 31}h26" class="s-line" stroke-width="1.4"/>'
                    f'<path d="M{x + 222} {y + 27}l5 4-5 4" class="s-line" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>'
                )
        return out

    return f'''<svg viewBox="0 0 940 300" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">
<text x="24" y="34" class="t-mono f-hit" style="font-weight:600;letter-spacing:.06em">{s1}</text>
{row(b, 48, "f-hit-tint")}
<path d="M818 110v36H122v32" class="s-line" stroke-width="1.4" stroke-dasharray="4 4"/>
<path d="M118 174l4 5 4-5" class="s-line" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
<text x="24" y="170" class="t-mono f-accent" style="font-weight:600;letter-spacing:.06em" dx="120">{s2}</text>
{row(c, 190, "f-accent-tint")}
<text x="24" y="282" class="t-mono f-faint" style="font-size:10.5px">{T("Same Markdown + pipeline version + theme version → byte-identical HTML. No clock, randomness or request data in the render core.", "相同的 Markdown + 管线版本 + 主题版本 → 逐字节一致的 HTML。渲染核心不读取时钟、随机数或请求数据。")}</text>
</svg>'''
