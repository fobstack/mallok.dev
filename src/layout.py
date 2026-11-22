"""Shared page chrome for the mallok.dev prototype (header, footer, head)."""

import html

ORIGIN = 'https://mallok.dev'
GH = 'https://github.com/fobstack/mallok'
DOCS = GH + '/blob/main/docs/'
NPM = 'https://www.npmjs.com/package/mallok'
DEMO = 'https://demo.mallok.dev/'
CMD = 'npx mallok create my-site'

LANG = 'en'


def set_lang(lang):
    """Selects the language every T() call resolves to."""
    global LANG
    LANG = lang


def T(en, zh):
    """Returns the string for the language being built."""
    return en if LANG == 'en' else zh


def url(path):
    """Root-absolute URL of a page in the language being built."""
    return path if LANG == 'en' else '/zh-cn' + path


def esc(text):
    return html.escape(text, quote=True)


BRAND = '/assets/brand'


def brand_logo():
    """The kit's colour logo; CSS shows the artwork for the active theme."""
    return (
        f'<img class="logo-light" src="{BRAND}/svg/logo/mallok-logo-color-light.svg" width="924" height="256" alt="Mallok">'
        f'<img class="logo-dark" src="{BRAND}/svg/logo/mallok-logo-color-dark.svg" width="924" height="256" alt="Mallok">'
    )


GH_ICON = (
    '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 '
    '0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
    '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-'
    '.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-'
    '.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-'
    '.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 '
    '.27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 '
    '0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 '
    '.21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>'
)

ARROW = (
    '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path d="M3 8h10M9 4l4 4-4 4" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)

EXT = (
    '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path d="M6 3H3v10h10v-3M9 3h4v4M13 3 7.5 8.5" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)


GLOBE = (
    '<svg class="ico" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false">'
    '<circle cx="8" cy="8" r="6.2" stroke-width="1.4"/>'
    '<path d="M1.8 8h12.4M8 1.8c1.7 1.8 2.5 3.9 2.5 6.2S9.7 12.4 8 14.2'
    'M8 1.8C6.3 3.6 5.5 5.7 5.5 8s.8 4.4 2.5 6.2" stroke-width="1.4"/></svg>'
)

CHEVRON = (
    '<svg class="chev" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false">'
    '<path d="M4 6l4 4 4-4" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

CHECK = (
    '<svg class="check" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false">'
    '<path d="M3.5 8.5l3 3 6-7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

SUN = (
    '<svg class="sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">'
    '<circle cx="12" cy="12" r="4.2" stroke-width="1.8"/>'
    '<path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.5 1.5'
    'M17.2 17.2l1.5 1.5M5.3 18.7l1.5-1.5M17.2 6.8l1.5-1.5" stroke-width="1.8" '
    'stroke-linecap="round"/></svg>'
)

MOON = (
    '<svg class="moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">'
    '<path d="M20 14.6A8 8 0 0 1 9.4 4a8 8 0 1 0 10.6 10.6Z" stroke-width="1.8" '
    'stroke-linejoin="round"/></svg>'
)

# Runs before first paint so a stored "light" choice never flashes dark.
HEAD_SCRIPT = (
    "<script>try{var t=localStorage.getItem('mallok-theme');"
    "if(t==='light'||t==='dark'){document.documentElement.dataset.theme=t;"
    "document.querySelector('meta[name=theme-color]')"
    ".content=t==='light'?'#FBFAFC':'#0D0B14'}}catch(e){}</script>"
)


def nav_items():
    return [
        ('/features/', T('Features', '功能')),
        ('/themes/', T('Themes', '主题')),
        ('/cost/', T('Cost', '成本')),
        ('/docs/', T('Docs', '文档')),
    ]


def header(path):
    links = ''
    mobile = ''
    for href, label in nav_items():
        cur = ' aria-current="page"' if href == path else ''
        links += f'<li><a href="{url(href)}"{cur}>{label}</a></li>'
        mobile += f'<li><a href="{url(href)}"{cur}>{label}</a></li>'
    links += f'<li><a href="{DEMO}">{T("Demo", "演示")}</a></li>'
    mobile += (
        f'<li><a href="{DEMO}">{T("Live demo", "在线演示")}'
        '<span>demo.mallok.dev</span></a></li>'
        f'<li><a href="{GH}">GitHub<span>fobstack/mallok</span></a></li>'
        f'<li><a href="{NPM}">npm<span>mallok</span></a></li>'
    )
    en_href = path
    zh_href = '/zh-cn' + path
    options = ''
    for code, href, name, short in (('en', en_href, 'English', 'EN'),
                                    ('zh-CN', zh_href, '简体中文', '中文')):
        here = (code == 'en') == (LANG == 'en')
        cur = ' aria-current="true"' if here else ''
        options += (
            f'<li><a href="{href}" lang="{code}" hreflang="{code}"{cur}>'
            f'<span>{name}</span>{CHECK if here else ""}</a></li>'
        )
    short = T('EN', '中文')
    lang = f'''<details class="lang-menu">
        <summary aria-label="{T("Language: English", "语言：简体中文")}">{GLOBE}<span>{short}</span>{CHEVRON}</summary>
        <ul class="lang-list">{options}</ul>
      </details>'''
    theme = (
        '<button class="theme-toggle" type="button" '
        f'data-label-light="{T("Switch to light mode", "切换到浅色模式")}" '
        f'data-label-dark="{T("Switch to dark mode", "切换到深色模式")}" '
        f'aria-label="{T("Switch to light mode", "切换到浅色模式")}">'
        f'{SUN}{MOON}</button>'
    )
    return f'''<a class="skip" href="#main">{T("Skip to content", "跳到正文")}</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{url("/")}" aria-label="{T("Mallok home", "Mallok 首页")}">{brand_logo()}</a>
    <nav class="nav-desktop" aria-label="{T("Primary", "主导航")}">
      <ul>{links}</ul>
    </nav>
    <div class="head-tools">
      {lang}
      {theme}
      <a class="icon-link" href="{GH}" aria-label="{T("Mallok on GitHub", "Mallok 的 GitHub 仓库")}">{GH_ICON}</a>
      <details class="nav-mobile">
        <summary>
          <svg class="ico-open" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 4.5h12M2 8h12M2 11.5h12" stroke-width="1.6" stroke-linecap="round"/></svg>
          <svg class="ico-close" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 3.5l9 9M12.5 3.5l-9 9" stroke-width="1.6" stroke-linecap="round"/></svg>
          {T("Menu", "菜单")}
        </summary>
        <nav aria-label="{T("Menu", "菜单")}">
          <ul>{mobile}</ul>
        </nav>
      </details>
    </div>
  </div>
</header>'''


def cta_compact():
    """Closing call to action for pages that already show the command."""
    return f'''<section class="cta cta-compact" aria-labelledby="cta-title">
  <div class="wrap">
    <h2 id="cta-title">{T("See it running before you install anything.", "先看它跑起来，再决定要不要装。")}</h2>
    <p>{T(
      "The live demo is a read-only Mallok site on Atelier, the default theme. Its company and content are fictional.",
      "在线演示是一个只读的 Mallok 站点，使用默认主题 Atelier。其中的企业与内容均为虚构。")}</p>
    <div class="actions">
      <a class="btn btn-primary" href="{DEMO}">{T("Open the live demo", "打开在线演示")}{EXT}</a>
      <a class="btn btn-ghost" href="{url("/docs/")}#quick-start">{T("Read the quick start", "阅读快速上手")}{ARROW}</a>
    </div>
  </div>
</section>'''


def cta():
    return f'''<section class="cta" aria-labelledby="cta-title">
  <div class="wrap">
    <div class="cta-main">
      <h2 id="cta-title">{T("One command. Your account. Your content.", "一条命令，部署到你自己的账号。")}</h2>
      <p>{T(
        "Mallok creates a Worker, a D1 database and an R2 bucket in your own Cloudflare account and deploys the site there. Nothing is hosted by Mallok, and there is no Mallok account to open.",
        "Mallok 会在你自己的 Cloudflare 账号里创建 Worker、D1 数据库和 R2 存储桶，并把网站部署上去。Mallok 不托管任何东西，也不需要注册 Mallok 账号。")}</p>
    </div>
    <div class="cta-side">
      <div class="cmd" role="group" aria-label="{T("Create command", "创建命令")}"><code>{CMD}</code></div>
      <p class="fine">{T(
        "Needs Node.js 22+ and <code>wrangler login</code>. Add <code>--no-deploy</code> to generate and check a project locally without creating cloud resources. Currently a 0.1 release candidate.",
        "需要 Node.js 22 及以上，并先执行 <code>wrangler login</code>。加上 <code>--no-deploy</code> 只在本地生成并检查项目，不创建云资源。当前为 0.1 候选版。")}</p>
      <div class="actions">
        <a class="btn btn-ghost" href="{url("/docs/")}#quick-start">{T("Read the quick start", "阅读快速上手")}{ARROW}</a>
        <a class="btn btn-ghost" href="{DEMO}">{T("Open the live demo", "打开在线演示")}{EXT}</a>
      </div>
    </div>
  </div>
</section>'''


def footer(path):
    gs = T('GETTING_STARTED.md', 'zh-CN/GETTING_STARTED.md')
    rs = T('RELEASE_STATUS.md', 'zh-CN/RELEASE_STATUS.md')
    contributing = T('CONTRIBUTING.md', 'CONTRIBUTING.zh-CN.md')
    other = (
        f'<a href="/zh-cn{path}" lang="zh-CN" hreflang="zh-CN">简体中文</a>'
        if LANG == 'en'
        else f'<a href="{path}" lang="en" hreflang="en">English</a>'
    )
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="brand" href="{url("/")}" aria-label="{T("Mallok home", "Mallok 首页")}">{brand_logo()}</a>
        <p>{T(
          "The Cloudflare-native CMS and website builder for multilingual B2B websites. Open source under Apache-2.0.",
          "面向多语言 B2B 网站的 Cloudflare 原生 CMS 与建站工具。基于 Apache-2.0 开源。")}</p>
      </div>
      <nav aria-label="{T("Product", "产品")}">
        <h2>{T("Product", "产品")}</h2>
        <ul>
          <li><a href="{url("/features/")}">{T("Features", "功能")}</a></li>
          <li><a href="{url("/themes/")}">{T("Themes", "主题")}</a></li>
          <li><a href="{url("/cost/")}">{T("Cost ladder", "成本阶梯")}</a></li>
          <li><a href="{url("/features/")}#roadmap">{T("Roadmap", "路线图")}</a></li>
          <li><a href="{DEMO}">{T("Live demo", "在线演示")}</a></li>
        </ul>
      </nav>
      <nav aria-label="{T("Documentation", "文档")}">
        <h2>{T("Documentation", "文档")}</h2>
        <ul>
          <li><a href="{url("/docs/")}">{T("Docs home", "文档入口")}</a></li>
          <li><a href="{DOCS}{gs}">{T("Getting started", "入门指南")}</a></li>
          <li><a href="{DOCS}ARCHITECTURE.md">{T("Architecture", "架构（英文）")}</a></li>
          <li><a href="{DOCS}THEME_FORMAT.md">{T("Theme format", "主题格式（英文）")}</a></li>
          <li><a href="{DOCS}PLUGIN_API.md">{T("Plugin API", "插件 API（英文）")}</a></li>
          <li><a href="{DOCS}CLI.md">{T("CLI reference", "CLI 参考（英文）")}</a></li>
        </ul>
      </nav>
      <nav aria-label="{T("Project", "项目")}">
        <h2>{T("Project", "项目")}</h2>
        <ul>
          <li><a href="{GH}">GitHub</a></li>
          <li><a href="{NPM}">npm</a></li>
          <li><a href="{DOCS}{rs}">{T("Release status", "发布状态")}</a></li>
          <li><a href="{GH}/blob/main/{contributing}">{T("Contributing", "贡献指南")}</a></li>
          <li><a href="{GH}/blob/main/SECURITY.md">{T("Security reporting", "安全报告")}</a></li>
          <li><a href="{GH}/blob/main/LICENSE">{T("Apache-2.0 licence", "Apache-2.0 许可证")}</a></li>
          <li><a href="{url("/brand/")}">{T("Brand", "品牌")}</a></li>
        </ul>
      </nav>
    </div>
    <div class="foot-base">
      <span>{T(
        "Mallok is an independent open-source project and is not affiliated with Cloudflare, Resend, WordPress or Ghost.",
        "Mallok 是独立的开源项目，与 Cloudflare、Resend、WordPress、Ghost 均无隶属关系。")}</span>
      <span>{other}</span>
    </div>
  </div>
</footer>'''


def page(path, title, description, body, with_cta=True, compact_cta=False):
    """Wraps a page body in the full document."""
    lang = T('en', 'zh-CN')
    canonical = ORIGIN + url(path)
    return f'''<!doctype html>
<html lang="{lang}" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{ORIGIN}{path}">
<link rel="alternate" hreflang="zh-CN" href="{ORIGIN}/zh-cn{path}">
<link rel="alternate" hreflang="x-default" href="{ORIGIN}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mallok">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ORIGIN}{BRAND}/social/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{T("en_US", "zh_CN")}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0D0B14">
{HEAD_SCRIPT}
<link rel="icon" href="{BRAND}/favicon/favicon.ico" sizes="48x48">
<link rel="icon" href="{BRAND}/favicon/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="{BRAND}/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{BRAND}/favicon/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{BRAND}/favicon/apple-touch-icon.png">
<link rel="mask-icon" href="{BRAND}/favicon/safari-pinned-tab.svg" color="#7E22CE">
<link rel="manifest" href="{BRAND}/favicon/site.webmanifest">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
{header(path)}
<main id="main">
{body}
</main>
{(cta_compact() if compact_cta else cta()) if with_cta else ""}
{footer(path)}
</body>
</html>
'''


def head(num, label):
    """A numbered catalogue-style eyebrow."""
    return f'<p class="eyebrow"><b>{num}</b>{label}</p>'


def frame(url_text, inner, label=None):
    """A browser-window frame around a screenshot or an illustration."""
    tag = f'<span class="illus-label">{label}</span>' if label else ''
    return (
        '<div class="frame"><div class="frame-bar" aria-hidden="true">'
        '<span class="frame-dots"><i></i><i></i><i></i></span>'
        f'<span class="frame-url">{url_text}</span></div>{inner}{tag}</div>'
    )
