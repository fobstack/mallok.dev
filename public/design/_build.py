#!/usr/bin/env python3
"""Builds the Mallok UI-language design board (index.html + board.css).

Run: python3 public/design/_build.py (sources here are excluded from deploys by public/.assetsignore)
Static output, zero JavaScript. Tokens live here once; the CSS variables and
the contrast tables are both generated from them, and the build prints every
pair that falls below WCAG AA.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).parent

# --------------------------------------------------------------------------
# Tokens
# --------------------------------------------------------------------------
TOKENS = {
    'a': {
        'light': dict(
            bg='#FBFAFC', surface='#FFFFFF', wash='#F4EEFC', washteal='#E6FAF6',
            text='#0D0B14', muted='#55506B', line='#E6E0F0', linestrong='#8A82A3',
            primary='#7E22CE', primaryhover='#6B21A8', onprimary='#FFFFFF',
            link='#7E22CE', teal='#0F766E', tealline='#0D9488',
            thread='#7E22CE', fold='#581C87', focus='#7E22CE',
            codebg='#F6F2FC', codekey='#7E22CE', codestr='#0F766E',
            codecom='#5F5A75',
            warnbg='#FFF6E0', warntext='#6B4300', warnline='#B7791F',
            grad1='#9333EA', grad2='#7E22CE', grad3='#581C87',
            shadow='0 1px 2px rgba(88,28,135,.06), 0 14px 32px -18px rgba(88,28,135,.28)',
            shadowlg='0 2px 4px rgba(88,28,135,.06), 0 28px 56px -24px rgba(88,28,135,.35)',
        ),
        'dark': dict(
            bg='#0D0B14', surface='#17141F', wash='#211A33', washteal='#0E2527',
            text='#FBFAFC', muted='#B4AEC6', line='#2A2538', linestrong='#7A7392',
            primary='#A855F7', primaryhover='#C084FC', onprimary='#0D0B14',
            link='#C99BFB', teal='#2DD4BF', tealline='#2DD4BF',
            thread='#A855F7', fold='#6B21A8', focus='#C99BFB',
            codebg='#14111C', codekey='#C99BFB', codestr='#5EEAD4',
            codecom='#9D97B2',
            warnbg='#2A2010', warntext='#F5C56B', warnline='#D69E2E',
            grad1='#D8B4FE', grad2='#C084FC', grad3='#A855F7',
            shadow='0 1px 0 rgba(255,255,255,.04) inset, 0 14px 32px -18px rgba(0,0,0,.7)',
            shadowlg='0 1px 0 rgba(255,255,255,.05) inset, 0 28px 56px -24px rgba(0,0,0,.8)',
        ),
    },
}

# (foreground token, background token, where it is used, minimum ratio)
PAIRS = [
    ('text', 'bg', '正文 / 标题 → 页面底', 4.5),
    ('text', 'surface', '正文 → 卡片', 4.5),
    ('text', 'wash', '正文 → 淡紫底（徽标、表头、提示）', 4.5),
    ('text', 'washteal', '正文 → 淡青底', 4.5),
    ('muted', 'bg', '次要文字 → 页面底', 4.5),
    ('muted', 'surface', '次要文字 → 卡片', 4.5),
    ('muted', 'wash', '次要文字 → 淡紫底', 4.5),
    ('link', 'bg', '链接 / 幽灵按钮 → 页面底', 4.5),
    ('link', 'surface', '链接 → 卡片', 4.5),
    ('link', 'wash', '链接 → 淡紫底（悬停）', 4.5),
    ('teal', 'bg', '青色文字 → 页面底', 4.5),
    ('teal', 'surface', '青色文字 → 卡片', 4.5),
    ('teal', 'washteal', '青色文字 → 淡青底（状态标签）', 4.5),
    ('onprimary', 'primary', '主按钮文字 → 主按钮', 4.5),
    ('onprimary', 'primaryhover', '主按钮文字 → 主按钮悬停', 4.5),
    ('text', 'codebg', '代码正文 → 代码底', 4.5),
    ('muted', 'codebg', '次要文字 → 代码底', 4.5),
    ('codekey', 'codebg', '代码键名 → 代码底', 4.5),
    ('codestr', 'codebg', '代码字符串 → 代码底', 4.5),
    ('codecom', 'codebg', '代码注释 → 代码底', 4.5),
    ('warntext', 'warnbg', '警告文字 → 警告底', 4.5),
    ('grad1', 'bg', '首屏渐变词最浅端 → 页面底（大字）', 4.5),
    ('linestrong', 'surface', '输入框边线 → 卡片（非文字 ≥3）', 3.0),
    ('tealline', 'bg', '青色线条 → 页面底（非文字 ≥3）', 3.0),
    ('thread', 'bg', '紫色引线 / 编号 → 页面底', 4.5),
    ('focus', 'bg', '焦点环 → 页面底（非文字 ≥3）', 3.0),
]


def lum(hex_):
    h = hex_.lstrip('#')
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


FAILS = []


def token_css():
    out = []
    for d, modes in TOKENS.items():
        for mode, t in modes.items():
            body = ';'.join(f'--{k}:{v}' for k, v in t.items())
            out.append(f'.dir-{d}.{mode}{{{body}}}')
    return '\n'.join(out)


def contrast_table(d, mode):
    t = TOKENS[d][mode]
    rows = []
    for fg, bg, use, need in PAIRS:
        r = ratio(t[fg], t[bg])
        ok = r >= need
        if not ok:
            FAILS.append((d, mode, fg, bg, round(r, 2), need))
        rows.append(
            f'<tr><td><span class="b-chip" style="color:{t[fg]};'
            f'background:{t[bg]}">Aa 文</span></td><td>{use}</td>'
            f'<td><code>{t[fg]}</code></td><td><code>{t[bg]}</code></td>'
            f'<td class="b-num">{r:.2f}:1</td>'
            f'<td>{"通过" if ok else "未通过"} <small>≥{need:g}</small></td></tr>')
    return ('<div class="b-tablewrap"><table class="b-table"><thead><tr>'
            '<th>样例</th><th>用途</th><th>前景</th><th>背景</th><th>对比度</th>'
            '<th>AA</th></tr></thead><tbody>' + ''.join(rows)
            + '</tbody></table></div>')


# --------------------------------------------------------------------------
# Small SVG helpers
# --------------------------------------------------------------------------
_uid = [0]


def uid(prefix):
    _uid[0] += 1
    return f'{prefix}{_uid[0]}'


GH = ('<svg class="m-ico" viewBox="0 0 16 16" width="18" height="18" '
      'aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 '
      '8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49'
      '-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01'
      '-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51'
      '-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02'
      '.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 '
      '1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 '
      '0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 '
      '0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')


def wave(cls='', waves=14, amp=7):
    """A horizontal wavy thread that stretches to its box (stroke unscaled)."""
    w = 1000 / waves
    d = 'M0 12' + ''.join(
        f' q{w / 4:.2f} {-amp if i % 2 == 0 else amp} {w / 2:.2f} 0'
        for i in range(waves * 2))
    return (f'<svg class="m-thread {cls}" viewBox="0 0 1000 24" '
            f'preserveAspectRatio="none" aria-hidden="true"><path d="{d}" '
            'fill="none" stroke="currentColor" stroke-linecap="round" '
            'vector-effect="non-scaling-stroke"/></svg>')


def twin(cls=''):
    """The wordmark's double l: two parallel wavy vertical threads."""
    p = 'c-7 22 7 44 0 66 s7 44 0 66'
    return (f'<svg class="m-twin {cls}" viewBox="0 0 40 150" '
            'aria-hidden="true"><g fill="none" stroke="currentColor" '
            'stroke-width="9" stroke-linecap="round">'
            f'<path d="M12 9{p}"/><path d="M28 9{p}"/></g></svg>')


def ribbon():
    """Hero ribbon for direction A: one thread, folded, ending in the dot."""
    g = uid('rb')
    return f'''<svg class="m-ribbon" viewBox="0 0 580 440" aria-hidden="true">
<defs>
<linearGradient id="{g}f" x1="40" y1="420" x2="160" y2="60" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6D28D9"/><stop offset=".55" stop-color="#8B3DFF"/><stop offset="1" stop-color="#A855F7"/></linearGradient>
<linearGradient id="{g}g" x1="300" y1="390" x2="460" y2="60" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#7E22CE"/><stop offset=".55" stop-color="#9333EA"/><stop offset="1" stop-color="#B06BFF"/></linearGradient>
<linearGradient id="{g}b" x1="0" y1="60" x2="0" y2="400" gradientUnits="userSpaceOnUse"><stop offset="0" style="stop-color:var(--rb1)"/><stop offset=".45" style="stop-color:var(--rb2)"/><stop offset="1" style="stop-color:var(--rb1)"/></linearGradient>
<linearGradient id="{g}t" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5EEAD4"/><stop offset=".5" stop-color="#2DD4BF"/><stop offset="1" stop-color="#06B6D4"/></linearGradient>
</defs>
<g fill="none" stroke-width="34" stroke-linecap="round" stroke-linejoin="round">
<path d="M150 70c30 0 48 26 62 80l40 172c12 50 30 68 58 68" stroke="url(#{g}b)"/>
<path d="M450 70c28 0 46 26 58 80l22 96" stroke="url(#{g}b)"/>
<path d="M36 430 100 150c12-54 32-80 60-80" stroke="url(#{g}f)"/>
<path d="M300 390c30 0 48-18 60-68l40-172c12-54 32-80 60-80" stroke="url(#{g}g)"/>
</g>
<circle cx="536" cy="278" r="7" fill="url(#{g}t)"/>
<circle class="m-shuttle" cx="540" cy="352" r="30" fill="url(#{g}t)"/>
</svg>'''


# --------------------------------------------------------------------------
# Mockup pieces. d = 'a' | 'b', mode = 'light' | 'dark', zh = Chinese copy.
# --------------------------------------------------------------------------
def T(zh, en, cn):
    return cn if zh else en


def nav(d, mode, zh=False):
    links = [T(zh, 'Features', '功能'), T(zh, 'Themes', '主题'),
             T(zh, 'Cost', '成本'), T(zh, 'Docs', '文档'), T(zh, 'Demo', '演示')]
    items = ''.join(
        f'<a class="m-navlink{" is-active" if i == 0 else ""}">{x}</a>'
        for i, x in enumerate(links))
    en_on, zh_on = ('', ' is-on') if zh else (' is-on', '')
    return f'''<header class="m-nav"><div class="m-wrap m-nav-in">
<a class="m-logo"><img src="assets/logo-{mode}.svg" alt="mallok" width="130" height="36"></a>
<nav class="m-navlinks">{items}</nav>
<div class="m-navend">
<div class="m-seg m-seg--sm" role="group" aria-label="Language"><span class="m-seg-i{en_on}">EN</span><span class="m-seg-i{zh_on}" lang="zh-CN">中文</span></div>
<a class="m-ghlink">{GH}<span>GitHub</span></a>
<span class="m-menu">{T(zh, 'Menu', '菜单')}</span>
</div></div></header>'''


def cmd():
    return ('<div class="m-cmd"><span class="m-cmd-p" aria-hidden="true">$'
            '</span><code>npx mallok create my-site</code></div>')


SAMPLE_NOTE = ('Sample content is illustrative; the company and product are '
               'fictional.')


def md_lines(zh=False, short=False):
    """The sample bundle source, coloured. zh = the zh-CN translation."""
    fm = [('title', '5 级钛棒' if zh else 'Grade 5 titanium bar'),
          ('grade', 'Ti-6Al-4V'), ('standard', 'ASTM B348'),
          ('moq', '500 kg')]
    body = (['5 级钛合金在 400 °C 以内保持强度，', '切削性能稳定。'] if zh else
            ['Grade 5 holds its strength to 400 °C', 'and machines predictably.'])
    out = ['<span class="c">---</span>']
    out += [f'<span class="k">{k}</span>: <span class="s">{v}</span>' for k, v in fm]
    out += ['<span class="c">---</span>'] + body
    if not short:
        out += ['', '<span class="k">[[inquiry]]</span>']
    return '\n'.join(out)


def editor_pane(zh=False, ui_zh=False, short=True):
    name = 'index.zh-CN.md' if zh else 'index.md'
    saved = '已保存' if ui_zh else 'saved'
    lang = ' lang="zh-CN"' if zh else ''
    return f'''<figure class="m-pane m-pane--md"><figcaption class="m-pane-h"><span class="m-pane-f"><bdo dir="ltr">content/product/grade-5-titanium-bar/<b>{name}</b></bdo></span><span class="m-tag m-tag--live"><span class="m-dot"></span>{saved}</span></figcaption>
<pre{lang}><code>{md_lines(zh, short)}</code></pre></figure>'''


def page_pane(zh=False, chips=True):
    url = 'example.com/' + ('zh-CN/' if zh else '') + 'products/grade-5-titanium-bar'
    t = (lambda en, cn: cn) if zh else (lambda en, cn: en)
    en_on, zh_on = ('', ' is-on') if zh else (' is-on', '')
    chip = (f'<span class="m-seg m-seg--sm"><span class="m-seg-i{en_on}">EN</span>'
            f'<span class="m-seg-i{zh_on}" lang="zh-CN">中文</span></span>') if chips else ''
    lang = ' lang="zh-CN"' if zh else ''
    return f'''<figure class="m-pane m-pane--page"><figcaption class="m-pane-h"><span class="m-url">{url}</span></figcaption>
<div class="m-page"{lang}><div class="m-page-top"><span class="m-crumb">{t('Products', '产品')} / {t('Grade 5 titanium bar', '5 级钛棒')}</span>{chip}</div>
<p class="m-page-t">{t('Grade 5 titanium bar', '5 级钛棒')}</p>
<p class="m-page-d">{t('Ti-6Al-4V round bar, 6–160 mm.', 'Ti-6Al-4V 圆棒，6–160 mm。')}</p>
<dl class="m-spec"><dt>{t('Grade', '牌号')}</dt><dd>Ti-6Al-4V</dd><dt>{t('Standard', '标准')}</dt><dd>ASTM B348</dd><dt>{t('Minimum order', '起订量')}</dt><dd>500 kg</dd></dl>
<span class="m-btn m-btn--secondary m-btn--sm">{t('Request a quotation', '索取报价')}</span></div></figure>'''


def weave():
    g = uid('wv')
    grad = (f'<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#A855F7"/><stop offset=".55" stop-color="#7E22CE"/>'
            '<stop offset="1" stop-color="#14B8A6"/></linearGradient>')
    return f'''<div class="m-weave" aria-hidden="true">
<svg class="m-weave-h" width="120" height="200" viewBox="0 0 120 200"><defs>{grad}</defs><path class="m-weave-p" d="M4 100C24 56 42 56 60 100S96 144 116 100" fill="none" stroke="url(#{g})" stroke-width="6" stroke-linecap="round"/></svg>
<svg class="m-weave-v" width="60" height="96" viewBox="0 0 60 96"><defs>{grad.replace(g, g + 'v')}</defs><path class="m-weave-p" d="M30 4C10 22 10 34 30 48S50 74 30 92" fill="none" stroke="url(#{g}v)" stroke-width="6" stroke-linecap="round"/></svg>
<span class="m-travel"></span></div>'''


def strip(zh=False):
    items = [T(zh, 'Theme pages ship no client JS<a class="m-fn">*</a>', '主题页面不带客户端 JS<a class="m-fn">*</a>'),
             T(zh, 'Multilingual + automatic hreflang', '多语言 + 自动 hreflang'),
             T(zh, "Starts on Cloudflare's free allowances (not unlimited)", '从 Cloudflare 免费额度起步（并非无限）'),
             T(zh, 'Apache-2.0 open source', 'Apache-2.0 开源')]
    fn = T(zh, '* Exceptions: the Turnstile script on the inquiry form and one declared carousel script on Atelier\'s homepage. Cloudflare features you enable may inject their own scripts.',
           '* 例外：询盘表单的 Turnstile 脚本，以及 Atelier 首页声明的一个轮播脚本。你启用的 Cloudflare 功能可能会注入它们自己的脚本。')
    return ('<ul class="m-strip">' + ''.join(f'<li><span class="m-dot"></span>{x}</li>' for x in items)
            + f'</ul><p class="m-note m-strip-fn">{fn}</p>')


def hero(d, mode, zh=False):
    badge = T(zh, '0.1 release candidate — rc.10', '0.1 候选版 —— rc.10')
    h1 = T(zh,
           'The Cloudflare-native CMS for <em>multilingual B2B</em> websites.',
           '为<em>多语言 B2B 网站</em>而生的 Cloudflare 原生 CMS')
    sub = T(zh,
            'Mallok is an open-source alternative to WordPress and Ghost. '
            'Markdown content, a web admin, Liquid themes and inquiry forms — '
            'deployed into your own Cloudflare account, with no server to run '
            'and no rebuild when you publish.',
            'Mallok 是开源的 WordPress / Ghost 替代方案：Markdown 内容、网页后台、'
            'Liquid 主题和询盘表单，一并部署到你自己的 Cloudflare 账号。不用维护服务器，'
            '发布内容也不用重新构建。')
    b1 = T(zh, 'Get started', '开始使用')
    b2 = T(zh, 'View the live demo', '查看在线演示')
    note = T(zh,
             'Needs Node.js 22+ and <code>wrangler login</code>. Creates '
             'resources in, and deploys to, your Cloudflare account.',
             '需要 Node.js 22 及以上，并先执行 <code>wrangler login</code>。'
             '会在你的 Cloudflare 账号里创建资源并完成部署。')
    cap = T(zh,
            '<b>Save → one D1 write + a cache purge by tag → live, with no build.</b> '
            'Purging the edge cache needs a custom domain and a cache-purge token; '
            'without the token, visitors see the previous version until the cache expires. '
            + SAMPLE_NOTE,
            '<b>保存 → 一次 D1 写入 + 一次按标签清缓存 → 上线，不需要构建。</b>'
            '清除边缘缓存需要自定义域名和清缓存令牌；没有令牌时，访客要等缓存过期才能看到新内容。'
            '示例内容仅作演示，企业与产品均为虚构。')
    lang = ' lang="zh-CN"' if zh else ''
    return f'''<section class="m-hero"{lang}><div class="m-wrap">
<div class="m-hero-copy"><p class="m-badge"><span class="m-dot m-dot--pulse"></span>{badge}</p>
<h1 class="m-h1">{h1}</h1><p class="m-lead">{sub}</p>
<div class="m-actions"><a class="m-btn m-btn--primary">{b1}<span class="m-arrow" aria-hidden="true">→</span></a><a class="m-btn m-btn--secondary">{b2}</a></div>
{cmd()}<p class="m-note">{note}</p></div>
<div class="m-duo">{editor_pane(False, zh)}{weave()}{page_pane(False)}</div>
<p class="m-note m-duo-cap">{cap}</p>
{strip(zh)}
</div></section>'''


def i18n_demo(d, mode):
    n = uid('loc')

    def head_tags(zh):
        base = 'https://example.com'
        en_u = base + '/products/grade-5-titanium-bar'
        zh_u = base + '/zh-CN/products/grade-5-titanium-bar'
        rows = [('canonical', None, zh_u if zh else en_u), ('alternate', 'en', en_u),
                ('alternate', 'zh-CN', zh_u), ('alternate', 'x-default', en_u)]
        out = []
        for rel, hl, href in rows:
            h = f' <span class="k">hreflang</span>=<span class="s">"{hl}"</span>' if hl else ''
            out.append(f'<span class="l">&lt;<span class="k">link</span> <span class="k">rel</span>=<span class="s">"{rel}"</span>{h} <span class="k">href</span>=<span class="s">"{href}"</span>&gt;</span>')
        return ('<figure class="m-pane m-pane--md"><figcaption class="m-pane-h"><span class="m-pane-f"><bdo dir="ltr">generated <b>&lt;head&gt;</b></bdo></span></figcaption>'
                '<pre><code>' + ''.join(out) + '</code></pre></figure>')

    def panel(zh):
        return (f'<div class="m-i18n-p m-i18n-p--{"zh" if zh else "en"}">'
                + editor_pane(zh, False, False) + page_pane(zh, False) + head_tags(zh) + '</div>')
    return f'''<section class="m-sec"><div class="m-wrap">
{head('05', 'Multilingual', 'Multilingual is in the content model.', 'Every item has its own locale and belongs to a translation group. URLs are prefixed by language, and the sitemap carries hreflang without a plugin or a setting to remember.')}
<div class="m-i18n">
<input class="m-i18n-r m-i18n-r--en" type="radio" name="{n}" id="{n}-en" checked>
<input class="m-i18n-r m-i18n-r--zh" type="radio" name="{n}" id="{n}-zh">
<div class="m-i18n-bar"><div class="m-seg" role="presentation"><label class="m-seg-i m-seg-i--en" for="{n}-en">EN · en</label><label class="m-seg-i m-seg-i--zh" for="{n}-zh" lang="zh-CN">中文 · zh-CN</label></div>
<p class="m-note">Example site with two locales: <code>en</code> (default, no URL prefix) and <code>zh-CN</code>. <code>x-default</code> points at the default language.</p></div>
{panel(False)}{panel(True)}
</div>
<p class="m-note m-duo-cap">One bundle is one translation group: <code>index.md</code> is the default locale, <code>index.zh-CN.md</code> the translation. {SAMPLE_NOTE}</p>
</div></section>'''


def quickstart(d, mode):
    return f'''<section class="m-sec m-sec--alt"><div class="m-wrap"><div class="m-qs">
<div><h2 class="m-h2">One command. Your account. Your content.</h2>
<p class="m-lead">Mallok creates a Worker, a D1 database and an R2 bucket in your own Cloudflare account and deploys the site there. Nothing is hosted by Mallok, and there is no Mallok account to open.</p></div>
<div class="m-card m-qs-card">{cmd()}
<p class="m-note">Needs Node.js 22+ and <code>wrangler login</code>. Add <code>--no-deploy</code> to generate and check a project locally without creating cloud resources. Currently a 0.1 release candidate.</p>
<ul class="m-qs-links"><li><a class="m-link" href="https://github.com/fobstack/mallok" rel="noopener">github.com/fobstack/mallok</a></li><li><a class="m-link" href="https://www.npmjs.com/package/mallok" rel="noopener">npmjs.com/package/mallok</a></li><li><a class="m-link" href="https://demo.mallok.dev" rel="noopener">demo.mallok.dev</a></li></ul></div>
</div></div></section>'''


def head(num, eyebrow, title, lead=''):
    lead = f'<p class="m-lead">{lead}</p>' if lead else ''
    return (f'<div class="m-head"><p class="m-eyebrow"><span class="m-dot">'
            f'</span><span class="m-idx">{num}</span>{eyebrow}</p>'
            f'<h2 class="m-h2">{title}</h2>{lead}</div>')


def promises(d, mode):
    cards = [
        ('01', 'No operations', 'No server to run',
         'There is no host to patch and no database server to keep alive. '
         'Mallok is one Worker in your own Cloudflare account. Mallok hosts '
         'nothing, cannot reach your site, and has no account system to sign '
         'up for.',
         'What gets created', 'One Worker, one D1 database, one R2 bucket'),
        ('02', 'No build for content', 'Edits are live immediately',
         'Saving is one D1 write plus a precise cache purge by tag. No CI '
         'run, no build queue, no redeploy. The same goes for settings, theme '
         'options and plugin settings.',
         'What it needs',
         'A custom domain and a cache-purge token. Without the token, '
         'visitors see the previous version until the cache expires.'),
        ('03', 'No lock-in', 'Your content leaves as Markdown',
         'D1 stores standard Markdown with YAML front matter; media sits in '
         'R2. Export produces ordinary bundles — <code>index.md</code> plus '
         '<code>images/</code> — designed to re-import into a fresh Mallok '
         'site byte-identically.',
         'Also exportable', 'Inquiries, as CSV'),
    ]
    html = ''.join(f'''<article class="m-card m-promise"><span class="m-bead" aria-hidden="true"></span>
<p class="m-kicker"><span class="m-idx">{n}</span>{k}</p><h3 class="m-h3">{t}</h3><p>{p}</p>
<dl class="m-fact"><dt>{ft}</dt><dd>{fd}</dd></dl></article>''' for n, k, t, p, ft, fd in cards)
    return f'''<section class="m-sec"><div class="m-wrap">
{head('01', 'What is Mallok?', "A CMS's editing, an edge network's delivery, and content you can take with you.", 'Mallok is built on three promises that refuse both prices.')}
<div class="m-promises">{wave('m-promises-thread', 9, 8) if d == 'a' else ''}{html}</div></div></section>'''


def track(steps, cls):
    return (f'<ol class="m-track {cls}">' + ''.join(
        f'<li{" class=is-end" if i == len(steps) - 1 else ""}><span '
        f'class="m-stop"></span>{s}</li>' for i, s in enumerate(steps))
        + '</ol>')


def timelines(d, mode):
    c_rows = [('Pages, articles, products, media', 'content'),
              ('Site name, languages, navigation, SEO defaults', 'settings'),
              ('The options a theme exposes', 'theme options'),
              ('Plugin on/off switch, settings and secrets', 'plugin settings')]
    f_rows = [('Switching or editing a theme', 'themes'),
              ('Installing or updating a plugin', 'plugins'),
              ('Moving to a new Mallok release', 'mallok upgrade'),
              ('A theme switch migrates no content and changes no URL',
               'guarantee')]

    def rows(rs):
        return '<ul class="m-rows">' + ''.join(
            f'<li><span>{a}</span><code>{b}</code></li>' for a, b in rs) + '</ul>'
    c_track = track(['save', 'D1 write', 'purge by tag', 'live'], 'm-track--teal')
    f_track = track(['edit source', 'build', 'deploy', 'live'], 'm-track--purple')
    c_head = ('<p class="m-tag m-tag--live"><span class="m-dot"></span>Live immediately</p>'
              '<h3 class="m-h3">The content timeline</h3>')
    f_head = ('<p class="m-tag m-tag--frame">Build + redeploy</p>'
              '<h3 class="m-h3">The frame timeline</h3>')
    c_p = ('<p>Changed in the admin or through the CLI by whoever runs the '
           'site day to day. No build, no deployment.</p>')
    f_p = ('<p>Changed in the source tree by someone technical. It travels '
           'with the code and takes effect on deployment — never as a '
           'one-click switch.</p>')
    hd = head('02', 'The boundary', 'Content needs no build. The frame does.',
              'A site has two timelines, and Mallok keeps them visibly apart.')
    if d == 'a':
        body = f'''<div class="m-lines"><article class="m-card m-line m-line--content">{c_head}{c_p}{c_track}{rows(c_rows)}</article>
{twin()}
<article class="m-card m-line m-line--frame">{f_head}{f_p}{f_track}{rows(f_rows)}</article></div>'''
    else:
        body = f'''<div class="m-score">
<div class="m-score-row m-score-row--content"><div class="m-score-l">{c_head}</div><div class="m-score-t">{c_track}</div></div>
<div class="m-score-row m-score-row--frame"><div class="m-score-l">{f_head}</div><div class="m-score-t">{f_track}</div></div>
</div>
<div class="m-lines"><div class="m-line m-line--content">{c_p}{rows(c_rows)}</div><div class="m-line m-line--frame">{f_p}{rows(f_rows)}</div></div>'''
    return f'<section class="m-sec m-sec--alt"><div class="m-wrap">{hd}{body}</div></section>'


def path_row(d, kind, title, nodes, note):
    ns = []
    for i, n in enumerate(nodes):
        a, b = n[0], n[1]
        end = ' is-end' if i == len(nodes) - 1 else ''
        if len(n) > 2:
            allow = f'<span class="m-allow">{n[3]}</span>' if len(n) > 3 else ''
            op = ' open' if len(n) > 4 else ''
            ns.append(f'<li class="m-node{end}"><details{op}><summary><b>{a}</b><small>{b}</small></summary>'
                      f'<div class="m-node-b">{n[2]}{allow}</div></details></li>')
        else:
            ns.append(f'<li class="m-node{end}"><div class="m-node-s"><b>{a}</b><small>{b}</small></div></li>')
    return f'''<div class="m-path m-path--{kind.lower()}">
<div class="m-path-h"><span class="m-tag m-tag--{kind.lower()}">{kind}</span><b>{title}</b></div>
<div class="m-path-r">{wave('', 22, 6)}<ol>{''.join(ns)}</ol><span class="m-dot m-path-dot" aria-hidden="true"></span></div>
<p class="m-note">{note}</p></div>'''


def diagram(d, mode):
    w = 'Workers free tier: 100k requests/day, 10 ms CPU each'
    d1 = 'D1 free tier: 5 GB, 5M rows read/day, 100k rows written/day'
    rows = [
        ('SAVE', 'An edit',
         [('Admin or CLI', 'the same management API',
           'The React admin is served as static files; the CLI publishes folders of Markdown through the same API.',
           'Static Assets: unlimited free requests'),
          ('Markdown → fragment', 'parsed and sanitised once',
           'Markdown becomes a sanitised HTML fragment when you save. The stored Markdown is never modified by sanitising.',
           w, 1),
          ('D1 write', 'content + render_cache',
           'One write stores the Markdown and its fragment. render_cache is derived data and can be rebuilt.',
           d1),
          ('Purge by tag', 'live, with no build',
           'A precise cache purge by tag. It needs a custom domain and a cache-purge token; without the token, visitors see the previous version until the cache expires.',
           'Cache + Purge API: free; 5 tag purges per minute')],
         'Parsing happens once, when you save.'),
        ('HIT', 'Most visitor requests',
         [('Visitor', 'GET /zh-CN/products/…'),
          ('Edge cache', 'cache.match() → HIT'),
          ('Cached page returned', 'no render, no D1 read',
           'CPU measured 0–1 ms across 30 confirmed hits on one rc.5 deployment. Those figures do not certify later candidates.')],
         'No rendering, no database read.'),
        ('MISS', 'A cold render',
         [('Visitor', 'GET'), ('Edge cache', 'MISS'),
          ('Worker reads D1', 'at most 4 round trips',
           'Settings, content with its fragment, and navigation — however much content the site holds. Markdown is not parsed here.',
           d1),
          ('Liquid theme', 'fragment → full page',
           'The theme wraps the fragment into a full page. Templates ship inside the Worker bundle.', w),
          ('cache.put()', 'Cache-Tag: site, c:&lt;id&gt;, …',
           'The page is stored in Cloudflare\'s cache with tags, so a later save can purge exactly the pages it changed.')],
         'Cold renders exceeded the 10 ms free-plan CPU target in 16 of 30 samples on rc.5; none failed. A known limitation of the release candidates.'),
        ('MEDIA', 'Images and files',
         [('Visitor', 'GET image'),
          ('R2', 'served directly',
           'Media is served from an R2 custom domain, or through a /media/* proxy when none is configured.',
           'R2 free tier: 10 GB-month, egress free')],
         'Images are converted to WebP with width variants in the browser on upload.'),
    ]
    return f'''<section class="m-sec"><div class="m-wrap">
{head('03', 'The request path', 'Rendered once, then served from the edge.', 'Open a node to see what it does and which free allowance it draws on.')}
<div class="m-paths">{''.join(path_row(d, *r) for r in rows)}</div>
<p class="m-note m-duo-cap">Free allowances per Cloudflare's documentation, checked 2026-08-28. They may have changed since, and they are allowances, not an unlimited-service promise.</p></div></section>'''


def cost(d, mode):
    rows = [
        ('Rendering, admin, API', 'Workers',
         '100k requests/day, 10 ms CPU each',
         'Workers Paid at $5/month: 10M requests, 30M CPU-ms'),
        ('Content, inquiries', 'D1',
         '5 GB total, 5M rows read/day, 100k rows written/day',
         'With Paid: 25B rows read/month, 50M written/month'),
        ('Images, attachments', 'R2',
         '10 GB-month, egress free', '$0.015/GB-month'),
        ('Scheduled publishing, email retries', 'Cron Triggers',
         '5 per account', '250 with Paid'),
        ('Form abuse protection', 'Turnstile',
         'Free, 20 widgets, 10 hostnames each', 'Enterprise'),
    ]
    trs = ''.join(
        f'<tr><th scope="row">{a}<small>{b}</small></th><td>{c}</td><td>{e}</td></tr>'
        for a, b, c, e in rows)
    return f'''<section class="m-sec m-sec--alt"><div class="m-wrap">
{head('07', 'Cost', "Designed to start on Cloudflare's free allowances.", 'There is exactly one paid step — Workers Paid, at $5 a month per account — and taking it changes no architecture and moves no data.')}
<div class="m-steps">
<article class="m-card m-step"><p class="m-kicker"><span class="m-idx">Step 0</span></p><p class="m-price">$0</p><h3 class="m-h3">Free allowances</h3><p>Workers, D1, R2, Static Assets, cache, cron and Turnstile free tiers.</p></article>
<span class="m-steps-link" aria-hidden="true"></span>
<article class="m-card m-step"><p class="m-kicker"><span class="m-idx">Step 1</span></p><p class="m-price">$5<small> / month / account</small></p><h3 class="m-h3">Workers Paid</h3><p>Higher request, CPU, D1 and cron limits. Same Worker, same data.</p></article>
</div>
<div class="m-tablewrap"><table class="m-table"><thead><tr><th>Purpose · product</th><th>Free tier</th><th>Beyond it</th></tr></thead><tbody>{trs}</tbody></table></div>
<p class="m-note">Figures from Cloudflare's official documentation, checked 2026-08-28. They may have changed since; confirm against the provider's current pricing pages.</p>
</div></section>'''


def code_block():
    lines = [
        ('c', '---'),
        ('k', 'title', 'Grade 5 titanium bar'),
        ('k', 'kind', 'product'),
        ('k', 'grade', 'Gr5 (Ti-6Al-4V)'),
        ('k', 'standard', 'ASTM B348'),
        ('k', 'moq', '50 kg'),
        ('k', 'cover', 'images/bar.jpg'),
        ('c', '---'),
        ('t', 'Annealed round bar, supplied with'),
        ('t', 'mill test certificates.'),
        ('t', ''),
        ('s', '[[inquiry]]'),
    ]
    out = []
    for ln in lines:
        if ln[0] == 'k':
            out.append(f'<span class="k">{ln[1]}</span>: <span class="s">{ln[2]}</span>')
        elif ln[0] == 'c':
            out.append(f'<span class="c">{ln[1]}</span>')
        elif ln[0] == 's':
            out.append(f'<span class="k">{ln[1]}</span>')
        else:
            out.append(ln[1])
    return ('<figure class="m-code"><figcaption><span class="m-dot"></span>'
            'titanium-bar-gr5/index.md<small>what D1 stores</small>'
            '</figcaption><pre><code>' + '\n'.join(out)
            + '</code></pre></figure>')


def theme_card():
    return '''<article class="m-card m-theme"><div class="m-theme-img"><img src="assets/atelier-desktop.jpg" alt="Atelier theme, desktop screenshot" width="1425" height="990"></div>
<div class="m-theme-b"><h3 class="m-h3">Atelier <span class="m-tag m-tag--live"><span class="m-dot"></span>default</span></h3>
<p>A material-first industrial catalogue: products, families, cases, FAQs and notes.</p>
<a class="m-link">demo.mallok.dev <span aria-hidden="true">→</span></a></div></article>'''


def content_sec(d, mode):
    return f'''<section class="m-sec"><div class="m-wrap">
{head('04', 'Content', 'A product page is a Markdown file.')}
<div class="m-two">{code_block()}{theme_card()}</div></div></section>'''


def footer(d, mode):
    cols = [
        ('Product', ['Features', 'Themes', 'Cost ladder', 'Roadmap', 'Live demo']),
        ('Documentation', ['Docs home', 'Getting started', 'Architecture',
                           'Theme format', 'CLI reference']),
        ('Project', ['GitHub', 'npm', 'Release status', 'Contributing',
                     'Apache-2.0 licence']),
    ]
    cs = ''.join(
        f'<div><h4>{h}</h4><ul>' + ''.join(f'<li><a>{x}</a></li>' for x in xs)
        + '</ul></div>' for h, xs in cols)
    return f'''<footer class="m-foot"><div class="m-wrap">
<div class="m-foot-in"><div class="m-foot-brand"><img src="assets/logo-{mode}.svg" alt="mallok" width="130" height="36">
<p>The Cloudflare-native CMS and website builder for multilingual B2B websites. Open source under Apache-2.0.</p>
<div class="m-seg m-seg--sm"><span class="m-seg-i is-on">EN</span><span class="m-seg-i" lang="zh-CN">简体中文</span></div></div>
{cs}</div>
<p class="m-foot-legal"><span class="m-dot"></span>Mallok is an independent open-source project and is not affiliated with Cloudflare, Resend, WordPress or Ghost.</p>
</div></footer>'''


def components(d, mode):
    return f'''<div class="m-sheet">
<div class="m-sheet-g"><h5>Buttons · default / hover / focus</h5>
<div class="m-sheet-r"><a class="m-btn m-btn--primary">Get started<span class="m-arrow">→</span></a><a class="m-btn m-btn--primary is-hover">Get started<span class="m-arrow">→</span></a><a class="m-btn m-btn--primary is-focus">Get started<span class="m-arrow">→</span></a></div>
<div class="m-sheet-r"><a class="m-btn m-btn--secondary">View the live demo</a><a class="m-btn m-btn--secondary is-hover">View the live demo</a><a class="m-btn m-btn--secondary is-focus">View the live demo</a></div>
<div class="m-sheet-r"><a class="m-btn m-btn--ghost">Read the quick start →</a><a class="m-btn m-btn--ghost is-hover">Read the quick start →</a><a class="m-btn m-btn--ghost is-focus">Read the quick start →</a></div>
<div class="m-sheet-r"><a class="m-btn m-btn--primary m-btn--sm">Small</a><a class="m-btn m-btn--secondary m-btn--sm">{GH}GitHub</a></div></div>

<div class="m-sheet-g"><h5>Links</h5>
<p>Body text with <a class="m-link">an inline link</a>, a <a class="m-link is-hover">hovered link</a> and a <a class="m-link is-focus">focused link</a>. <a class="m-link">Full release status <span aria-hidden="true">→</span></a></p></div>

<div class="m-sheet-g"><h5>Badges &amp; tags</h5>
<div class="m-sheet-r"><span class="m-badge"><span class="m-dot"></span>0.1 release candidate — rc.10</span><span class="m-tag m-tag--live"><span class="m-dot"></span>Live immediately</span><span class="m-tag m-tag--frame">Build + redeploy</span><span class="m-tag">Apache-2.0</span><span class="m-tag m-tag--warn">in progress</span><code class="m-kbd">theme.json</code></div></div>

<div class="m-sheet-g"><h5>Nav · active state</h5>
<div class="m-sheet-r m-navlinks m-navlinks--demo"><a class="m-navlink is-active">Features</a><a class="m-navlink">Themes</a><a class="m-navlink is-hover">Cost</a><a class="m-navlink">Docs</a></div></div>

<div class="m-sheet-g"><h5>Segmented control</h5>
<div class="m-sheet-r"><div class="m-seg"><span class="m-seg-i is-on">npm</span><span class="m-seg-i">pnpm</span><span class="m-seg-i">yarn</span></div><div class="m-seg m-seg--sm"><span class="m-seg-i is-on">EN</span><span class="m-seg-i" lang="zh-CN">中文</span></div></div></div>

<div class="m-sheet-g"><h5>Card</h5>
<article class="m-card m-promise"><span class="m-bead" aria-hidden="true"></span><p class="m-kicker"><span class="m-idx">02</span>No build for content</p><h3 class="m-h3">Edits are live immediately</h3><p>Saving is one D1 write plus a precise cache purge by tag.</p><dl class="m-fact"><dt>What it needs</dt><dd>A custom domain and a cache-purge token.</dd></dl></article></div>

<div class="m-sheet-g"><h5>Form input · default / focus</h5>
<div class="m-form"><label class="m-field"><span>Company email</span><input class="m-input" type="email" value="" placeholder="you@company.com" tabindex="-1"><small>Used only to reply to this inquiry.</small></label>
<label class="m-field"><span>Message</span><input class="m-input is-focus" type="text" value="Gr5 bar, 50 kg, h9" tabindex="-1"><small>Focus: thread-coloured ring.</small></label></div></div>

<div class="m-sheet-g"><h5>Callouts</h5>
<div class="m-callout"><span class="m-dot"></span><div><b>Read these numbers for what they are.</b> They come from one isolated deployment of 0.1.0-rc.5 on a custom domain.</div></div>
<div class="m-callout m-callout--warn"><span class="m-dot"></span><div><b>Themes need a redeploy.</b> Switching theme changes the frame timeline; it migrates no content and changes no URL.</div></div></div>

<div class="m-sheet-g"><h5>Table</h5>
<div class="m-tablewrap"><table class="m-table"><thead><tr><th>Surface</th><th>Client JavaScript</th></tr></thead><tbody>
<tr><th scope="row">Content pages, lists, navigation</th><td>no script</td></tr>
<tr><th scope="row">Inquiry form</th><td>Turnstile script</td></tr>
<tr><th scope="row">Atelier homepage</th><td>one declared carousel script</td></tr></tbody></table></div></div>

<div class="m-sheet-g"><h5>Command</h5>{cmd()}</div>
</div>'''


def type_specimen(d):
    rows_a = [('Display', 'm-h1', 'multilingual B2B', '60 / 1.06 · 800 · -0.025em'),
              ('H2', 'm-h2', 'Content needs no build.', '40 / 1.12 · 800 · -0.02em'),
              ('H3', 'm-h3', 'Edits are live immediately', '22 / 1.3 · 700'),
              ('Body', 'm-body', 'Saving is one D1 write plus a precise cache purge by tag.', '17 / 1.6 · 400'),
              ('Small', 'm-note', 'Needs Node.js 22+ and wrangler login.', '14 / 1.5 · 400'),
              ('Label', 'm-kicker', 'No build for content', '13 / 1.2 · 700 · +0.06em · 大写'),
              ('中文标题', 'm-h2', '内容不需要构建，框架需要。', 'PingFang SC Semibold · 字距 0 · 行高 1.3'),
              ('Mono', 'm-mono', 'npx mallok create my-site', '15 / 1.6 · 系统等宽')]
    rows_b = [('Display', 'm-h1', 'multilingual B2B', '84 / 0.98 · 900 · -0.04em'),
              ('H2', 'm-h2', 'Content needs no build.', '48 / 1.04 · 900 · -0.03em'),
              ('H3', 'm-h3', 'Edits are live immediately', '22 / 1.25 · 800 · -0.01em'),
              ('Body', 'm-body', 'Saving is one D1 write plus a precise cache purge by tag.', '17 / 1.6 · 400'),
              ('Small', 'm-note', 'Needs Node.js 22+ and wrangler login.', '14 / 1.5 · 400'),
              ('Label', 'm-kicker', 'No build for content', '12 / 1.2 · 等宽 · +0.08em · 大写'),
              ('中文标题', 'm-h2', '内容不需要构建，框架需要。', 'PingFang SC Semibold · 字距 0 · 行高 1.25'),
              ('Mono', 'm-mono', 'npx mallok create my-site', '15 / 1.6 · 系统等宽')]
    rows = rows_a if d == 'a' else rows_b
    return '<div class="m-type">' + ''.join(
        f'<div class="m-type-r"><span class="m-type-l">{l}<small>{s}</small>'
        f'</span><span class="{c}"{" lang=zh-CN" if "中文" in l else ""}>{t}</span></div>'
        for l, c, t, s in rows) + '</div>'


def swatches(d, mode):
    t = TOKENS[d][mode]
    names = [('bg', '页面底'), ('surface', '卡片'), ('wash', '淡紫底'),
             ('washteal', '淡青底'), ('text', '正文'), ('muted', '次要文字'),
             ('line', '细线'), ('linestrong', '强边线'), ('primary', '主按钮'),
             ('primaryhover', '主按钮悬停'), ('link', '链接'),
             ('thread', '引线紫'), ('teal', '青色文字'), ('tealline', '青色线')]
    return '<div class="b-sw">' + ''.join(
        f'<div class="b-sw-i"><span style="background:{t[k]}"></span>'
        f'<b>{n}</b><code>{t[k]}</code></div>' for k, n in names) + '</div>'


def shape_tokens(d):
    if d == 'a':
        radii = [('8', '标签内代码'), ('14', '输入框'), ('24', '卡片'),
                 ('999', '按钮 / 徽标 / 命令条')]
        shadow = ('<p>两级柔和紫调投影，卡片底部带一道淡紫渐变，对应 Logo 的折叠阴影。'
                  '深色下改为顶部 1px 高光加黑色投影。</p>')
    else:
        radii = [('0', '表格 / 分栏'), ('4', '卡片 / 代码块'), ('8', '按钮 / 输入框'),
                 ('999', '仅用于圆点和线端')]
        shadow = ('<p>默认没有投影，层次靠 2px 墨线和发丝线。只有主题卡、悬停状态用'
                  '一块 8px 的实色错位（折角），对应 Logo 丝带压叠的那一面。</p>')
    r = ''.join(
        f'<div class="b-rad"><span style="border-radius:{v if v != "999" else "999"}px"></span>'
        f'<b>{v}px</b><small>{n}</small></div>' for v, n in radii)
    sp = ''.join(f'<div class="b-sp"><span style="width:{v}px"></span>'
                 f'<small>{v}</small></div>' for v in (4, 8, 12, 16, 24, 32, 48, 64, 96))
    return f'''<div class="b-shape"><div><h5>圆角</h5><div class="b-rads">{r}</div></div>
<div><h5>间距（4 的倍数）</h5><div class="b-sps">{sp}</div><p>区块上下留白：桌面 96，手机 56。内容最大宽 1200，手机两侧 16。</p></div>
<div><h5>层次</h5>{shadow}<div class="mk dir-{d} light b-depth"><div class="m-card">card</div><div class="m-card m-card--lg">card · raised</div></div></div></div>'''


# --------------------------------------------------------------------------
# Board assembly
# --------------------------------------------------------------------------
def mk(d, mode, inner, extra=''):
    return f'<div class="mk dir-{d} {mode} {extra}">{inner}</div>'


def desk(d, title, note, fn, anchor=''):
    """A desktop-width segment: light frame above, dark frame below."""
    frames = ''.join(
        f'<div class="b-frame"><span class="b-mode b-mode--{m}">{"浅色" if m == "light" else "深色"}</span>'
        f'<div class="b-scroll" tabindex="0">{mk(d, m, fn(d, m), "w-desk")}</div></div>'
        for m in ('light', 'dark'))
    return (f'<div class="b-seg"><h3 class="b-h3">{title}</h3>'
            f'<p class="b-note">{note}</p>{frames}</div>')


def pair(d, title, note, fn):
    """A narrow segment: light and dark side by side."""
    frames = ''.join(
        f'<div class="b-frame"><span class="b-mode b-mode--{m}">{"浅色" if m == "light" else "深色"}</span>'
        f'<div class="b-scroll" tabindex="0">{mk(d, m, fn(d, m), "w-fluid")}</div></div>'
        for m in ('light', 'dark'))
    return (f'<div class="b-seg"><h3 class="b-h3">{title}</h3>'
            f'<p class="b-note">{note}</p><div class="b-pair">{frames}</div></div>')


def phones(d):
    items = [('light', False, '浅色 · EN'), ('dark', False, '深色 · EN'),
             ('light', True, '浅色 · 中文')]
    fr = ''.join(
        f'<div class="b-phone"><span class="b-mode b-mode--{m}">{lab} · 375</span>'
        f'<div class="b-scroll" tabindex="0">{mk(d, m, nav(d, m, z) + hero(d, m, z), "w-phone")}</div></div>'
        for m, z, lab in items)
    return ('<div class="b-seg"><h3 class="b-h3">2 · 首屏（手机 375px）</h3>'
            '<p class="b-note">同一套标记，用容器查询在 375px 画框里换成单列：两个面板上下叠放，引线变成竖向。'
            '导航收成「Menu」，正式站用 <code>&lt;details&gt;</code> 实现，不需要脚本。'
            f'第三个是中文首屏。</p><div class="b-phones">{fr}</div></div>')


RATIONALE = {
    'a': ('最终候选', 'A · 引线 Thread', '轻、亮、圆；一条线把内容从 Markdown 串到上线的页面',
          ['<b>丝带 → 线</b>：一条波浪线把卡片、流程节点串起来；首屏里它连接「编辑器」和「上线的页面」，从紫渐变到青。',
           '<b>圆头线端 → 圆角</b>：按钮、徽标、命令条全是胶囊形，卡片 20–24px 圆角。',
           '<b>穿梭圆点 → 标记</b>：状态点、列表符号、当前导航、流程终点，都是同一颗青色圆点；首屏里它沿着引线移动。',
           '<b>双 l → 成对</b>：两条时间线之间一对青色竖波纹；EN / 中文是一对胶囊，多语言演示就是这一对的放大。',
           '<b>折叠阴影 → 层次</b>：卡片底部一道很淡的紫色渐变加柔和紫调投影。',
           '<b>粗几何小写 → 标题</b>：Figtree 800，负字距。'],
          ['颜色按 80 / 15 / 5 分配：中性色为主，紫色只做动作和线，青色只讲「即时上线」。',
           '原来的方向 B 不再单独展示。它的两样东西并进了 A，用在信息密集的页面：平行轨道的时间线、只有发丝线的表格（见第 10 节）。',
           '代价：圆角和投影多，信息密度偏低，所以成本页、文档页改用密集变体。',
           '所有文案都对照文档核对过；没有对比表、没有速度数字、没有「一键部署」。']),
}


def dense(d, mode):
    c_track = track(['save', 'D1 write', 'purge by tag', 'live'], 'm-track--teal')
    f_track = track(['edit source', 'build', 'deploy', 'live'], 'm-track--purple')
    rows = [('Rendering, admin, API', 'Workers', '100k requests/day, 10 ms CPU each', 'Workers Paid at $5/month: 10M requests, 30M CPU-ms'),
            ('Content, inquiries', 'D1', '5 GB total, 5M rows read/day, 100k rows written/day', 'With Paid: 25B rows read/month, 50M written/month'),
            ('Images, attachments', 'R2', '10 GB-month, egress free', '$0.015/GB-month'),
            ('The admin app', 'Workers Static Assets', 'Unlimited free requests, 20k files, 25 MiB each', 'With Paid, up to 100k files')]
    trs = ''.join(f'<tr><th scope="row">{a}<small>{b}</small></th><td>{c}</td><td>{e}</td></tr>' for a, b, c, e in rows)
    return f'''<section class="m-sec"><div class="m-wrap">
<div class="m-score">
<div class="m-score-row m-score-row--content"><div class="m-score-l"><p class="m-tag m-tag--live"><span class="m-dot"></span>Live immediately</p><h3 class="m-h3">The content timeline</h3></div><div class="m-score-t">{c_track}</div></div>
<div class="m-score-row m-score-row--frame"><div class="m-score-l"><p class="m-tag m-tag--frame">Build + redeploy</p><h3 class="m-h3">The frame timeline</h3></div><div class="m-score-t">{f_track}</div></div>
</div>
<div class="m-tablewrap m-tablewrap--hair"><table class="m-table"><thead><tr><th>Purpose · product</th><th>Free tier</th><th>Beyond it</th></tr></thead><tbody>{trs}</tbody></table></div>
<p class="m-note">Figures from Cloudflare's official documentation, checked 2026-08-28. They may have changed since.</p>
</div></section>'''


def ratio_bar():
    return '''<div class="b-ratio" role="img" aria-label="80% 中性色，15% 交织紫，5% 穿梭青"><span class="b-ratio-n">80% 中性 · Cloud White / Midnight</span><span class="b-ratio-p">15% 交织紫</span><span class="b-ratio-t"></span></div>
<ul class="b-ratio-l"><li><b>80% 中性</b>：Cloud White 页面底、白色卡片、Midnight 文字。浅色模式里没有大面积深色块。</li><li><b>15% 交织紫</b>：主按钮、链接、引线、编号、淡紫底。每屏只有一个实心紫按钮。</li><li><b>5% 穿梭青</b>：只讲「即时 / 已上线」这一个故事 —— 状态点、终点圆点、内容时间线、缓存命中线。不用来做装饰，也不做第二种按钮色。</li></ul>'''


def direction(d):
    tag, name, strap, derive, trade = RATIONALE[d]
    li = ''.join(f'<li>{x}</li>' for x in derive)
    tr = ''.join(f'<li>{x}</li>' for x in trade)
    segs = [
        desk(d, '1 · 导航 + 首屏（桌面）',
             '首屏主视觉是「左边写 Markdown，右边就是上线的页面」，中间一条紫到青的引线，圆点沿线移动（纯 CSS，'
             '系统设置为减少动效时静止在终点）。下面是四枚能力标签。画框宽度固定为桌面尺寸；浅色在上，深色在下。',
             lambda dd, mm: nav(dd, mm) + hero(dd, mm)),
        phones(d),
        desk(d, '3 · 功能区：三个承诺', '', promises),
        desk(d, '4 · 两条时间线', '「ll 双线」的用法：内容线用青色（即时），框架线用紫色（要部署）。', timelines),
        desk(d, '5 · 多语言演示（纯 CSS 切换）',
             '用单选按钮加 <code>&lt;label&gt;</code> 做的分段开关，没有脚本：Tab 聚焦，左右方向键切换。'
             '每个状态显示 Markdown 源文件、渲染后的页面，以及核心自动生成的 canonical 和 hreflang 标签。', i18n_demo),
        desk(d, '6 · 可展开的请求路径图',
             '节点穿在引线上，带「+」的节点是 <code>&lt;details&gt;</code>，点开（或聚焦后按回车 / 空格）显示一两句说明和对应的免费额度。'
             '第一行默认展开了一个作为示例。', diagram),
        desk(d, '7 · 成本表', '', cost),
        desk(d, '8 · 代码块 + 主题卡', '浅色模式下代码块也是浅色的，不做深色大色块。', content_sec),
        desk(d, '9 · 快速开始 + 页脚', '只有一条真实命令和三个真实链接，没有「一键部署」按钮。',
             lambda dd, mm: quickstart(dd, mm) + footer(dd, mm)),
        desk(d, '10 · 密集页面变体（成本页、文档页用）',
             '从原来的方向 B 吸收两样东西：两条时间线画成上下平行的轨道；表格去掉卡片外框，只留发丝线。圆角、颜色、字体仍是 A。', dense),
        pair(d, '11 · 组件表', '悬停、焦点状态是静态画出来的（<code>.is-hover</code> / <code>.is-focus</code>）。', components),
    ]
    tokens = f'''<div class="b-seg"><h3 class="b-h3">12 · 设计变量</h3>
<h4 class="b-h4">配色比例：80 / 15 / 5</h4>{ratio_bar()}
<h4 class="b-h4">颜色 · 浅色</h4>{swatches(d, 'light')}{contrast_table(d, 'light')}
<h4 class="b-h4">颜色 · 深色</h4>{swatches(d, 'dark')}{contrast_table(d, 'dark')}
<h4 class="b-h4">字体与字号</h4>
<div class="b-frame"><div class="b-scroll" tabindex="0">{mk(d, 'light', type_specimen(d), 'w-fluid')}</div></div>
<h4 class="b-h4">圆角 · 间距 · 层次</h4>{shape_tokens(d)}
</div>'''
    return f'''<section class="b-dir" id="dir-{d}">
<header class="b-dirhead"><p class="b-kicker">{tag}</p><h2 class="b-h2">{name}</h2><p class="b-strap">{strap}</p>
<div class="b-rat"><div><h4>怎么从 Logo 来的</h4><ul>{li}</ul></div><div><h4>取舍</h4><ul>{tr}</ul></div></div></header>
{''.join(segs)}{tokens}</section>'''


FONT_NOTE = '''<section class="b-dir" id="shared"><header class="b-dirhead"><p class="b-kicker">补充</p><h2 class="b-h2">字体与动效</h2>
<div class="b-rat"><div><h4>字体：Figtree（只加载这一个家族）</h4><ul>
<li>字标是很粗的几何小写，圆润、开口大、a 是双层。Figtree 的 800 / 900 字重和它的骨架最接近，400 字重读正文也舒服，一个可变字体文件就覆盖全部字重。</li>
<li>画板从 Google Fonts 加载；<b>正式站应当自托管 woff2</b>（只子集拉丁字符，约 30 KB 以内），不向第三方发请求。</li>
<li>回退栈：<code>Figtree, ui-sans-serif, system-ui, -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif</code>。</li>
<li>中文不加载网页字体，直接用 PingFang SC / Microsoft YaHei / Noto Sans SC。中文标题用系统最粗的一档（PingFang Semibold），字距归零，行高放到 1.25–1.3。</li>
<li>等宽：<code>ui-monospace, "SF Mono", Menlo, Consolas, monospace</code>，系统字体，不加载。</li></ul></div>
<div><h4>动效（纯 CSS，正式站不带 JS）</h4><ul>
<li><b>圆点呼吸</b>：徽标前的状态点 2.4s 一次的光晕扩散（画板里已实现）。</li>
<li><b>圆点穿梭</b>：首屏引线上的圆点用 <code>offset-path</code> 从编辑器走到页面，3.6s 一次（画板里已实现）。</li>
<li><b>引线描画</b>：流程图的线用 <code>stroke-dashoffset</code> 在载入时从左画到右，600ms，一次（正式站再做）。</li>
<li><b>按钮</b>：悬停 150ms 换色，箭头右移 3px；按下回弹 1px。</li>
<li><b>卡片</b>：悬停上浮 2px，投影加深。</li>
<li><b>分段开关、展开节点</b>：单选按钮和 <code>&lt;details&gt;</code>，状态切换不加动画，保证键盘操作即时。</li>
<li><b>命令条</b>：<code>user-select: all</code>，点一下全选，不需要「复制」脚本。</li>
<li>全部包在 <code>prefers-reduced-motion: no-preference</code> 里；减少动效时一律静止。时长 150 / 240 / 600ms，缓动 <code>cubic-bezier(.2,.7,.2,1)</code>。</li></ul></div></div></header></section>'''


def page():
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Mallok 官网 UI 语言 · 设计画板</title>
<link rel="icon" href="assets/mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400..900&amp;display=swap">
<link rel="stylesheet" href="board.css">
</head>
<body>
<header class="b-top">
<img src="assets/logo-light.svg" class="b-logo b-logo--l" alt="mallok" width="173" height="48"><img src="assets/logo-dark.svg" class="b-logo b-logo--d" alt="mallok" width="173" height="48">
<h1 class="b-h1">官网 UI 语言 · 最终候选</h1>
<p class="b-intro">方向 <b>A · 引线</b>，加上首屏双面板、多语言演示、可展开的架构图、配色比例和能力标签这五处改进。<b>浅色为主</b>，深色是它的映射。画板不含 JavaScript，现有网站页面没有改动，文案都对照文档核对过。</p>
<nav class="b-toc"><a href="#dir-a"><b>A · 引线（最终候选）</b><span>12 节：页面、组件、变量</span></a><a href="#shared"><b>字体与动效</b><span>Figtree · 纯 CSS</span></a></nav>
<div class="b-logo-map"><img src="assets/mark.svg" alt="" width="96" height="96">
<ul><li><i class="b-k b-k--ribbon"></i><b>丝带</b>连接线、分隔线、图表路径</li><li><i class="b-k b-k--cap"></i><b>圆头线端</b>按钮与圆角</li><li><i class="b-k b-k--dot"></i><b>穿梭圆点</b>状态、列表符号、当前导航</li><li><i class="b-k b-k--ll"></i><b>双 l</b>成对的东西：两条时间线、EN / 中文</li><li><i class="b-k b-k--fold"></i><b>折叠阴影</b>卡片层次</li></ul></div>
</header>
{direction('a')}
{FONT_NOTE}
<footer class="b-end">设计画板 · 未提交、未发布。由 <code>design/_build.py</code> 生成，颜色变量和对比度表出自同一份数据。</footer>
</body>
</html>
'''


CSS = (HERE / '_board.src.css').read_text()

if __name__ == '__main__':
    html = page()
    (HERE / 'index.html').write_text(html)
    (HERE / 'board.css').write_text(
        '/* Generated by _build.py from _board.src.css + tokens. */\n'
        + token_css() + '\n' + CSS)
    if '<script' in html:
        sys.exit('script found')
    for f in FAILS:
        print('CONTRAST FAIL', f)
    print('ok', len(html), 'bytes;', len(FAILS), 'contrast failures')
