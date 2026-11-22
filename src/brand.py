"""Brand page: a press-kit showcase of the user's brand kit
(logos/mallok-brand-kit, copied to assets/brand/)."""

import os

import tokens
from layout import BRAND, T, head

_FONTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'fonts', 'figtree-latin.woff2')
FONT_STATE = (
    ('It is self-hosted from /assets/fonts/ under the SIL Open Font License; no request leaves the site.',
     '字体文件自托管在 /assets/fonts/，采用 SIL Open Font License，不向第三方发请求。')
    if os.path.exists(_FONTS) else
    ('The font files are not in /assets/fonts/ yet, so this build shows the system fallback; no request leaves the site either way.',
     '字体文件尚未放入 /assets/fonts/，所以当前构建显示的是系统回退字体；无论哪种情况都不向第三方发请求。'))

LIGHT_BG = '#FBFAFC'
DARK_BG = '#0D0B14'


def on(hexv):
    """Readable text colour for a swatch."""
    return '#0d0b14' if tokens.contrast(hexv, '#0d0b14') >= tokens.contrast(hexv, '#ffffff') else '#ffffff'


def asset(label, svg, bg, png=None, cls='', alt=''):
    links = f'<a href="{BRAND}/{svg}" download>SVG ↓</a>'
    if png:
        links += f' · <a href="{BRAND}/{png}" download>PNG ↓</a>'
    return (
        f'<figure class="asset"><div class="logo-panel {cls}" style="background:{bg}">'
        f'<img src="{BRAND}/{svg}" alt="{alt or label}" loading="lazy"></div>'
        f'<figcaption><strong>{label}</strong><span>{links}</span></figcaption></figure>'
    )


def logo_assets():
    on_light, on_dark = T('on light', '浅色底'), T('on dark', '深色底')
    logos = [
        (T('Colour', '彩色') + ' · ' + on_light, 'color-light', LIGHT_BG),
        (T('Colour', '彩色') + ' · ' + on_dark, 'color-dark', DARK_BG),
        (T('Accent', '强调色') + ' · ' + on_dark, 'accent-dark', DARK_BG),
        (T('Mono', '单色') + ' · ' + on_light, 'mono-light', LIGHT_BG),
        (T('Mono', '单色') + ' · ' + on_dark, 'mono-dark', DARK_BG),
    ]
    marks = [
        (T('Colour', '彩色'), 'color', LIGHT_BG, 'png/mark/mallok-mark-color-512.png'),
        (T('Accent', '强调色') + ' · ' + on_dark, 'accent-dark', DARK_BG, 'png/mark/mallok-mark-accent-dark-512.png'),
        (T('Mono', '单色') + ' · ' + on_light, 'mono-light', LIGHT_BG, 'png/mark/mallok-mark-mono-light-512.png'),
        (T('Mono', '单色') + ' · ' + on_dark, 'mono-dark', DARK_BG, 'png/mark/mallok-mark-mono-dark-512.png'),
    ]
    words = [
        (T('Colour', '彩色') + ' · ' + on_light, 'light', LIGHT_BG),
        (T('Colour', '彩色') + ' · ' + on_dark, 'dark', DARK_BG),
        (T('Mono', '单色') + ' · ' + on_light, 'mono-light', LIGHT_BG),
        (T('Mono', '单色') + ' · ' + on_dark, 'mono-dark', DARK_BG),
    ]
    a = ''.join(asset(l, f'svg/logo/mallok-logo-{k}.svg', bg, f'png/logo/mallok-logo-{k}.png', alt=f'Mallok logo, {k}') for l, k, bg in logos)
    b = ''.join(asset(l, f'svg/mark/mallok-mark-{k}.svg', bg, png, 'is-mark', alt=f'Mallok mark, {k}') for l, k, bg, png in marks)
    c = ''.join(asset(l, f'svg/wordmark/mallok-wordmark-{k}.svg', bg, alt=f'mallok wordmark, {k}') for l, k, bg in words)
    return f'''<div class="asset-group"><h3>{T("Logo — mark and wordmark", "完整横版标志")}</h3><div class="assets">{a}</div></div>
<div class="asset-group"><h3>{T("Mark — the M alone", "独立图形 M")}</h3><div class="assets">{b}</div></div>
<div class="asset-group"><h3>{T("Wordmark", "独立字标")}</h3><div class="assets">{c}</div></div>'''


def favicon_assets():
    f = BRAND + '/favicon'
    sizes = ''.join(
        f'<img src="{f}/{name}" width="{s}" height="{s}" alt="favicon {s}px" loading="lazy">'
        for name, s in (('favicon-16x16.png', 16), ('favicon-32x32.png', 32), ('favicon-48x48.png', 48)))
    files = ['favicon.ico', 'favicon.svg', 'favicon-16x16.png', 'favicon-32x32.png', 'favicon-48x48.png',
             'apple-touch-icon.png', 'android-chrome-192x192.png', 'android-chrome-512x512.png',
             'mstile-150x150.png', 'safari-pinned-tab.svg', 'site.webmanifest']
    links = ''.join(f'<li><a href="{f}/{n}">{n}</a></li>' for n in files)
    return f'''<div class="assets">
  <figure class="asset"><div class="logo-panel is-small is-row" style="background:#ffffff">{sizes}</div>
    <figcaption><strong>16 · 32 · 48 px</strong><span>{T("small-size artwork", "小尺寸专用版本")}</span></figcaption></figure>
  <figure class="asset"><div class="logo-panel is-small is-row" style="background:{DARK_BG}">{sizes}</div>
    <figcaption><strong>16 · 32 · 48 px</strong><span>{T("on dark", "深色底")}</span></figcaption></figure>
  <figure class="asset"><div class="logo-panel is-mark" style="background:#ffffff"><img src="{f}/apple-touch-icon.png" width="180" height="180" alt="Apple touch icon" loading="lazy"></div>
    <figcaption><strong>{T("App icon", "App 图标")}</strong><span>180 px</span></figcaption></figure>
  <figure class="asset"><div class="logo-panel" style="background:#ffffff;padding:.5rem"><img src="{BRAND}/social/og-image.png" width="1200" height="630" alt="{T("Open Graph share image", "Open Graph 分享图")}" loading="lazy" style="width:100%"></div>
    <figcaption><strong>{T("Share image", "分享图")}</strong><span><a href="{BRAND}/social/og-image.png" download>1200×630 ↓</a></span></figcaption></figure>
</div>
<ul class="chips" style="margin-top:1.25rem" aria-label="{T("Favicon files", "favicon 文件")}">{links}</ul>'''


def kit_colours():
    out = ''
    for en, zh, hexv, var, role in tokens.KIT:
        w, m = tokens.contrast(hexv, '#ffffff'), tokens.contrast(hexv, '#0D0B14')
        out += (
            f'<div class="kit-colour"><i style="background:{hexv}"></i><div>'
            f'<strong>{T(en, zh)}</strong><code>{hexv}</code><code>{var}</code>'
            f'<span>{T("on white", "对白色")} {w:.1f}:1 · {T("on Midnight", "对暗夜深")} {m:.1f}:1</span></div></div>'
        )
    return f'<div class="kit-colours">{out}</div>'


def ramp(prefix, values):
    cells = ''.join(
        f'<div class="ramp-cell" style="background:{v};color:{on(v)}"><b>{k}</b><span>{v}</span></div>'
        for k, v in values.items())
    return f'<div class="ramp" role="img" aria-label="{prefix} ramp">{cells}</div><p class="fine" style="margin-top:.4rem"><code>--{prefix}-&lt;step&gt;</code></p>'


def semantic_table():
    rows = ''
    for name, light, dark, note in tokens.SEMANTIC:
        rows += (
            f'<tr><th scope="row"><code>--{name}</code></th>'
            f'<td><span class="sw" style="background:{light}"></span><code>{light}</code></td>'
            f'<td><span class="sw" style="background:{dark}"></span><code>{dark}</code></td>'
            f'<td>{note}</td></tr>'
        )
    return f'''<div class="table-wrap" tabindex="0" role="region" aria-label="{T("Semantic colour tokens", "语义色令牌")}">
<table class="data">
<thead><tr><th scope="col">Token</th><th scope="col">{T("Light", "浅色")}</th><th scope="col">{T("Dark", "深色")}</th><th scope="col">{T("Role", "用途")}</th></tr></thead>
<tbody>{rows}</tbody></table></div>'''


def grade(r):
    return 'AAA' if r >= 7 else ('AA' if r >= 4.5 else 'FAIL')


def contrast_table():
    rows = ''
    for fg, bg in tokens.PAIRS:
        cells = ''
        for mode in ('light', 'dark'):
            f, b = tokens.value(fg, mode), tokens.value(bg, mode)
            r = tokens.contrast(f, b)
            cells += (
                f'<td><span class="pair" style="background:{b};color:{f}">Aa 文</span>'
                f'<code>{r:.2f}:1</code> <span class="fine">{grade(r)}</span></td>'
            )
        rows += f'<tr><th scope="row"><code>--{fg}</code> <span class="fine">{T("on", "于")}</span> <code>--{bg}</code></th>{cells}</tr>'
    return f'''<div class="table-wrap" tabindex="0" role="region" aria-label="{T("Contrast ratios", "对比度")}">
<table class="data narrow">
<thead><tr><th scope="col">{T("Text on background", "文字 / 背景")}</th><th scope="col">{T("Light", "浅色")}</th><th scope="col">{T("Dark", "深色")}</th></tr></thead>
<tbody>{rows}</tbody></table></div>'''


def build():
    specimen = f'''<div class="specimen">
  <div>
    <p class="fine"><code>--sans</code> · {T("headings and body", "标题与正文")}</p>
    <p style="font-size:var(--step-4);font-weight:750;letter-spacing:-.035em;line-height:1.02;color:var(--ink)">{T("Content needs no build.", "内容不需要构建。")}</p>
    <p style="font-size:var(--step-3);font-weight:700;letter-spacing:-.022em;line-height:1.12;margin-top:.75rem;color:var(--ink)">{T("The frame does.", "框架需要。")}</p>
    <p class="lede" style="margin-top:.75rem;max-width:40rem">{T("Mallok is the Cloudflare-native CMS and website builder for multilingual B2B websites. 多语言 B2B 网站的建站工具。", "Mallok 是面向多语言 B2B 网站的 Cloudflare 原生 CMS 与建站工具。Markdown content, Liquid themes.")}</p>
  </div>
  <div>
    <p class="fine"><code>--mono</code> · {T("labels, code, catalogue numbers", "标签、代码、目录编号")}</p>
    <p style="font-family:var(--mono);font-size:1.25rem;color:var(--ink)">npx mallok create my-site</p>
    <p class="eyebrow" style="margin-top:.75rem"><b>01</b>{T("Section label", "栏目标签")}</p>
  </div>
  <div>
    <p class="fine"><code>--serif</code> · {T("reserved for quotations and long-form accents; not used in the interface", "保留给引文和长文点缀；界面中不使用")}</p>
    <p style="font-family:var(--serif);font-size:1.5rem;font-style:italic;color:var(--ink)">{T("Publish at the edge, keep the Markdown.", "在边缘发布，把 Markdown 留在自己手里。")}</p>
  </div>
</div>'''

    scale = ''.join(
        f'<div class="mini-row"><span><code>--step-{n}</code></span><span>{d}</span></div>'
        for n, d in [('-1', '13px · ' + T('fine print', '小字')), ('0', '16px · ' + T('body', '正文')),
                     ('1', '18px · ' + T('lede', '导语')), ('2', '20–24px · ' + T('card titles', '卡片标题')),
                     ('3', '26–38px · ' + T('section titles', '栏目标题')), ('4', '34–60px · ' + T('hero', '首屏标题'))])

    return f'''<section class="hero page-hero" aria-labelledby="page-title">
  <div class="wrap">
    {head("Brand", T("Brand kit v0.2", "品牌资料 v0.2"))}
    <h1 id="page-title">{T("The Kinetic Thread M.", "「交织引线」M")}</h1>
    <p class="lede">{T(
      "Mallok's logo, favicon set, colours and type, with the rules for using them. Every file on this page is a copy from the brand kit and can be downloaded as it is.",
      "Mallok 的标志、favicon 套件、色彩与字体，以及它们的使用规范。本页的每个文件都是品牌资料包的副本，可以直接下载使用。")}</p>
    <ul class="toc"><li><a href="#story">{T("Concept", "品牌概念")}</a></li><li><a href="#logo">{T("Logo files", "标志文件")}</a></li><li><a href="#icons">{T("Favicon and social", "Favicon 与社交")}</a></li><li><a href="#usage">{T("Usage", "使用规范")}</a></li><li><a href="#colour">{T("Colour", "色彩")}</a></li><li><a href="#contrast">{T("Contrast", "对比度")}</a></li><li><a href="#type">{T("Type", "字体")}</a></li></ul>
  </div>
</section>

<section class="section" id="story" aria-labelledby="story-title">
  <div class="wrap">
    <div class="feature">
      <div>
        {head("01", T("Concept", "品牌概念"))}
        <h2 id="story-title">{T("One unbroken thread, and one dot that travels.", "一条不间断的引线，一个穿梭的圆点。")}</h2>
        <p class="lede">{T(
          "The initial M is drawn as a single continuous thread, standing for the seamless serverless flow of a site that runs on Cloudflare Workers, D1 and R2. The only teal element, the shuttle dot at the lower right, answers the two flowing l's in the wordmark.",
          "首字母 M 由一条连续不间断的交织引线构成，象征运行于 Cloudflare Workers + D1 + R2 上的无服务器无缝流转。右下角唯一的「穿梭青」圆点，与字标中双轨流线的 ll 遥相呼应。")}</p>
        <p class="lede" style="margin-top:.9rem">{T(
          "Together they tell the product's story: no operations, content woven live the moment it is saved, and Markdown that is free to leave.",
          "它们合在一起，讲的就是产品的故事：不用运维、内容即时编织上线、Markdown 自由不锁定。")}</p>
      </div>
      <div class="logo-panel" style="background:{LIGHT_BG};min-height:16rem">
        <img src="{BRAND}/svg/mark/mallok-mark-color.svg" width="256" height="256" alt="{T("The Mallok mark: a purple ribbon M with a teal dot", "Mallok 图形标记：紫色丝带 M 与青色圆点")}" style="width:auto;height:12rem">
      </div>
    </div>
  </div>
</section>

<section class="section tinted" id="logo" aria-labelledby="logo-title">
  <div class="wrap">
    <div class="section-head">
      {head("02", T("Logo files", "标志文件"))}
      <h2 id="logo-title">{T("Logo, mark and wordmark.", "完整标志、图形与字标。")}</h2>
      <p>{T(
        "All SVGs are pure vector paths with no font dependency. Use the colour logo wherever you can: the light version on light pages, the dark version on dark ones. The mono versions are for print, white papers and partner walls.",
        "所有 SVG 都是纯矢量路径，不依赖字体。能用彩色版就用彩色版：浅色页面用浅色版，深色页面用深色版。单色版用于印刷、白皮书和合作伙伴墙。")}</p>
    </div>
    {logo_assets()}
  </div>
</section>

<section class="section" id="icons" aria-labelledby="icons-title">
  <div class="wrap">
    <div class="section-head">
      {head("03", T("Favicon and social", "Favicon 与社交"))}
      <h2 id="icons-title">{T("The small sizes have their own artwork.", "小尺寸有专门优化的版本。")}</h2>
      <p>{T(
        "Between 16 and 32 pixels, always use the files from the favicon set rather than scaling the mark down. This site uses the set as supplied.",
        "16 到 32 像素之间，务必使用 favicon 套件里的文件，而不是把图形标记直接缩小。本站使用的就是这套文件。")}</p>
    </div>
    {favicon_assets()}
    <p class="fine" style="margin-top:1rem">{T(
      'Also in the kit: a 512 px avatar (<a href="' + BRAND + '/social/github-avatar-512.png">PNG</a>), README headers for light and dark (<a href="' + BRAND + '/social/readme-header-light.svg">light</a>, <a href="' + BRAND + '/social/readme-header-dark.svg">dark</a>) and four looping GIFs (<a href="' + BRAND + '/gif/mallok-logo-light.gif">logo light</a>, <a href="' + BRAND + '/gif/mallok-logo-dark.gif">logo dark</a>, <a href="' + BRAND + '/gif/mallok-mark-dark.gif">mark</a>, <a href="' + BRAND + '/gif/mallok-loader.gif">loader</a>). The GIFs are linked rather than shown, so nothing on this page moves on its own.',
      '资料包里还有：512 px 头像（<a href="' + BRAND + '/social/github-avatar-512.png">PNG</a>）、明暗两版 README 横幅（<a href="' + BRAND + '/social/readme-header-light.svg">浅色</a>、<a href="' + BRAND + '/social/readme-header-dark.svg">深色</a>）和四个循环 GIF（<a href="' + BRAND + '/gif/mallok-logo-light.gif">浅色标志</a>、<a href="' + BRAND + '/gif/mallok-logo-dark.gif">深色标志</a>、<a href="' + BRAND + '/gif/mallok-mark-dark.gif">图形</a>、<a href="' + BRAND + '/gif/mallok-loader.gif">加载动效</a>）。GIF 只提供链接而不直接展示，所以本页不会有任何自动播放的动画。')}</p>
  </div>
</section>

<section class="section tinted" id="usage" aria-labelledby="usage-title">
  <div class="wrap">
    <div class="section-head">
      {head("04", T("Usage", "使用规范"))}
      <h2 id="usage-title">{T("How to use it, and the red lines.", "怎么用，以及不能碰的红线。")}</h2>
    </div>
    <div class="do-dont">
      <div class="do">
        <h3>{T("How to use", "正确用法")}</h3>
        <ul>
          <li>{T("<strong>Clear space:</strong> keep at least one shuttle-dot diameter free on every side of the logo.", "<strong>安全留白：</strong>标志四周的最小安全间距，不小于「穿梭圆点」的 1 倍直径。")}</li>
          <li>{T("<strong>Minimum size:</strong> the full logo at least 96 px wide on screen; the mark at least 16 × 16 px.", "<strong>最小尺寸：</strong>完整横版标志在屏幕上最小宽度 96 px；独立图形最小 16×16 px。")}</li>
          <li>{T("From 16 to 32 px, use the versions in the favicon set, which are drawn for small sizes.", "16–32 px 务必使用 favicon 套件中针对小尺寸优化的版本。")}</li>
          <li>{T("Pick the file for the background: colour-light or mono-light on light; colour-dark, accent-dark or mono-dark on dark.", "按背景选文件：浅色底用彩色浅底版或单色浅底版；深色底用彩色深底版、强调色版或单色深底版。")}</li>
          <li>{T("Teal is the one story accent: the shuttle dot, the double l, and “instant” status. Use it sparingly.", "穿梭青是唯一的故事强调色：只用于穿梭圆点、双 l 亮点和“即时”状态提示，克制使用。")}</li>
        </ul>
      </div>
      <div class="dont">
        <h3>{T("Things to avoid", "禁止操作")}</h3>
        <ul>
          <li>{T("Do not put the M on a rounded tile or any other container. The only exception is the iOS and Android app icons.", "不要给独立 M 图形加圆角方框或其他底托。仅 iOS / Android App 图标除外。")}</li>
          <li>{T("Do not stretch or distort the logo.", "不要拉伸、变形。")}</li>
          <li>{T("Do not change the balance of teal and purple, or recolour either.", "不要自行更改穿梭青与交织紫的配色比例，也不要改色。")}</li>
          <li>{T("Do not use Electric Teal (#06B6D4) or #0D9488 for small text on light backgrounds; they are below 4.5:1 there. This site uses <code>--live</code> (#0f766e) for teal text.", "不要在浅色背景上用穿梭青（#06B6D4）或 #0D9488 写小字，它们在浅底上的对比度不到 4.5:1。本站的青色文字使用 <code>--live</code>（#0f766e）。")}</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="colour" aria-labelledby="colour-title">
  <div class="wrap">
    <div class="section-head">
      {head("05", T("Colour", "色彩"))}
      <h2 id="colour-title">{T("Cloud White, Midnight ink, purple to act, teal for live.", "云端白打底，暗夜深为墨，紫色行动，青色表示“已上线”。")}</h2>
      <p>{T(
        "The site is light first. Purple is the brand and action colour. Teal appears only where something is live or instant; amber marks what needs a redeploy. The scales below are derived from the kit's colours, and pages use the semantic tokens only.",
        "网站以浅色为主。紫色是品牌色和行动色。青色只出现在“已上线”或“即时”的地方；琥珀色标记需要重新部署的内容。下面的色阶由资料包的颜色推导而来，页面只使用语义令牌。")}</p>
    </div>
    <h3 class="ramp-title">{T("The kit's colours", "资料包中的颜色")}</h3>
    {kit_colours()}
    <div class="grid cols-2" style="margin-top:1.5rem">
      <div><h3 class="ramp-title">{T("Thread gradient", "引线渐变")}</h3><div class="gradient-bar" style="background:var(--mallok-gradient-thread)"></div><p class="fine" style="margin-top:.4rem"><code>--mallok-gradient-thread</code></p></div>
      <div><h3 class="ramp-title">{T("Shuttle gradient", "穿梭渐变")}</h3><div class="gradient-bar" style="background:var(--mallok-gradient-shuttle)"></div><p class="fine" style="margin-top:.4rem"><code>--mallok-gradient-shuttle</code></p></div>
    </div>
    <div class="stack" style="--gap:1.5rem;margin-top:2.5rem">
      <div><h3 class="ramp-title">{T("Purple — 700 is Kinetic Purple, 500 the highlight, 900 the fold", "紫 —— 700 为交织紫，500 为高光，900 为折影")}</h3>{ramp("purple", tokens.PURPLE)}</div>
      <div><h3 class="ramp-title">{T("Teal — 400 is Mint Glow, 600 the kit's light-background teal, 700 is used for text", "青 —— 400 为穿梭亮青，600 为资料包的浅底青，文字使用 700")}</h3>{ramp("teal", tokens.TEAL)}</div>
      <div><h3 class="ramp-title">{T("Neutral — violet-tinted, from Cloud White to Midnight", "中性色 —— 带紫调，从云端白到暗夜深")}</h3>{ramp("neutral", tokens.NEUTRAL)}</div>
      <div class="grid cols-3">
        <div><h3 class="ramp-title">{T("Green — success", "绿 —— 成功")}</h3>{ramp("green", tokens.GREEN)}</div>
        <div><h3 class="ramp-title">{T("Amber — warning", "琥珀 —— 警示")}</h3>{ramp("amber", tokens.AMBER)}</div>
        <div><h3 class="ramp-title">{T("Red — danger", "红 —— 危险")}</h3>{ramp("red", tokens.RED)}</div>
      </div>
    </div>
    <h3 style="margin:2.5rem 0 1rem;font-size:1.2rem">{T("Semantic tokens and their light and dark values", "语义令牌及其浅色、深色取值")}</h3>
    {semantic_table()}
  </div>
</section>

<section class="section tinted" id="contrast" aria-labelledby="contrast-title">
  <div class="wrap">
    <div class="section-head">
      {head("06", T("Contrast", "对比度"))}
      <h2 id="contrast-title">{T("Every text pair the site uses, measured.", "网站用到的每一组文字配色，都算过。")}</h2>
      <p>{T(
        "WCAG 2 contrast ratios, computed from the token values when this page is built. AA for normal text needs 4.5:1; AAA needs 7:1.",
        "WCAG 2 对比度，在构建本页时由令牌数值直接计算。普通文字 AA 需要 4.5:1，AAA 需要 7:1。")}</p>
    </div>
    {contrast_table()}
  </div>
</section>

<section class="section" id="ui" aria-labelledby="ui-title">
  <div class="wrap">
    <div class="section-head">
      {head("07", T("UI language", "界面语言"))}
      <h2 id="ui-title">{T("How the logo becomes an interface.", "Logo 怎样变成界面。")}</h2>
      <p>{T(
        "The ribbon becomes the threads that connect cards and diagram nodes. Its rounded ends become pill buttons and rounded cards. The shuttle dot marks status, list items and the current page. The wordmark's twin l becomes paired things: the two timelines, EN and 中文.",
        "丝带变成连接卡片和流程节点的引线；圆头线端变成胶囊按钮和圆角卡片；穿梭圆点用来标记状态、列表项和当前页面；字标里的双 l 变成成对的东西：两条时间线、EN 与中文。")}</p>
    </div>
    <div class="stack">
      <div class="ratio-bar" role="img" aria-label="{T("80% neutral, 15% Kinetic Purple, 5% Electric Teal", "80% 中性色，15% 交织紫，5% 穿梭青")}"><span class="ratio-n">{T("80% neutral · Cloud White / Midnight", "80% 中性 · 云端白 / 暗夜深")}</span><span class="ratio-p">{T("15% purple", "15% 紫")}</span><span class="ratio-t"></span></div>
      <p class="note">{T(
        "80% neutral, 15% Kinetic Purple for actions and threads, 5% Electric Teal for one story only: live, instant, arrived. Teal is never a second button colour.",
        "80% 中性色；15% 交织紫，用于动作和引线；5% 穿梭青，只讲一个故事：即时、已上线、已到达。青色不做第二种按钮色。")}</p>
      <div class="kit-demo">
        <span class="btn btn-primary">{T("Primary", "主按钮")}</span>
        <span class="btn btn-ghost">{T("Secondary", "次按钮")}</span>
        <span class="badge"><span class="dot" aria-hidden="true"></span>{T("0.1 release candidate", "0.1 候选版")}</span>
        <span class="tag tag-live"><span class="dot" aria-hidden="true"></span>{T("Live immediately", "立即生效")}</span>
        <span class="tag tag-frame">{T("Build + redeploy", "构建并重新部署")}</span>
        <div class="cmd"><code>npx mallok create my-site</code></div>
      </div>
      <p><a class="link-arrow" href="/design/">{T("The full design board: components, states and tokens", "完整设计画板：组件、状态与变量（中文）")}</a></p>
    </div>
  </div>
</section>

<section class="section tinted" id="type" aria-labelledby="type-title">
  <div class="wrap">
    <div class="section-head">
      {head("08", T("Type", "字体"))}
      <h2 id="type-title">{T("Figtree for Latin text, system fonts for Chinese and code.", "西文用 Figtree，中文和代码用系统字体。")}</h2>
      <p>{T(
        "Figtree's 800 weight is the closest match to the wordmark's heavy geometric lowercase, and its 400 reads well as body text. " + FONT_STATE[0] + " Chinese uses PingFang SC, Microsoft YaHei and Noto Sans SC; code uses each platform's monospace. Neither loads a web font.",
        "Figtree 的 800 字重和字标那种很粗的几何小写最接近，400 字重读正文也舒服。" + FONT_STATE[1] + "中文使用苹方、微软雅黑和思源黑体，代码使用各平台自带的等宽字体，两者都不加载网络字体。")}</p>
    </div>
    <div class="feature">
      {specimen}
      <div class="mini">{scale}</div>
    </div>
  </div>
</section>'''
