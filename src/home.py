"""Home page, built from the approved "A · Thread" board (/design/)."""

import art
from layout import ARROW, CMD, DEMO, DOCS, EXT, GH, NPM, T, frame, head, url

SAMPLE = 'grade-5-titanium-bar'
_uid = [0]


def uid(prefix):
    _uid[0] += 1
    return f'{prefix}{_uid[0]}'


def release_href():
    return DOCS + T('RELEASE_STATUS.md', 'zh-CN/RELEASE_STATUS.md')


def wave(waves=14, amp=7):
    """A horizontal wavy thread that stretches to its box (stroke unscaled)."""
    w = 1000 / waves
    d = 'M0 12' + ''.join(
        f' q{w / 4:.2f} {-amp if i % 2 == 0 else amp} {w / 2:.2f} 0'
        for i in range(waves * 2))
    return ('<svg class="m-thread" viewBox="0 0 1000 24" preserveAspectRatio="none" '
            f'aria-hidden="true" focusable="false"><path d="{d}" fill="none" '
            'stroke="currentColor" stroke-linecap="round" '
            'vector-effect="non-scaling-stroke"/></svg>')


def twin():
    """The wordmark's double l: two parallel wavy threads."""
    p = 'c-7 22 7 44 0 66 s7 44 0 66'
    return ('<svg class="m-twin" viewBox="0 0 40 150" aria-hidden="true" focusable="false">'
            '<g fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round">'
            f'<path d="M12 9{p}"/><path d="M28 9{p}"/></g></svg>')


def track(steps, live):
    cls = 'm-track m-track-live' if live else 'm-track'
    return f'<ol class="{cls}">' + ''.join(f'<li>{s}</li>' for s in steps) + '</ol>'


def boundary(dense=False):
    """The two-timeline model. dense=True draws parallel tracks (Features)."""
    live_tag = f'<span class="tag tag-live"><span class="dot"></span>{T("Live immediately", "立即生效")}</span>'
    frame_tag = f'<span class="tag tag-frame">{T("Build + redeploy", "构建并重新部署")}</span>'
    live_h = T("The content timeline", "内容时间线")
    frame_h = T("The frame timeline", "框架时间线")
    live_p = T("Changed in the admin or through the CLI by whoever runs the site day to day. No build, no deployment.", "由日常运营网站的人在后台或通过 CLI 修改。不需要构建，也不需要部署。")
    frame_p = T("Changed in the source tree by someone technical. It travels with the code and takes effect on deployment — never as a one-click switch.", "由技术人员在源码里修改，随代码一起发布，部署后才生效——不会伪装成一键切换。")
    live_ul = f'''<ul>
      <li>{T("Pages, articles, products, media", "页面、文章、产品、媒体")}<span>{T("content", "内容")}</span></li>
      <li>{T("Site name, languages, navigation, SEO defaults", "站点名称、语言、导航、SEO 默认值")}<span>{T("settings", "设置")}</span></li>
      <li>{T("The options a theme exposes", "主题开放的选项")}<span>{T("theme options", "主题选项")}</span></li>
      <li>{T("Plugin on/off switch, settings and secrets", "插件的启用开关、设置与密钥")}<span>{T("plugin settings", "插件设置")}</span></li>
    </ul>'''
    frame_ul = f'''<ul>
      <li>{T("Switching or editing a theme", "切换或修改主题")}<span>{T("themes", "主题")}</span></li>
      <li>{T("Installing or updating a plugin", "安装或更新插件")}<span>{T("plugins", "插件")}</span></li>
      <li>{T("Moving to a new Mallok release", "升级 Mallok 版本")}<span><code>mallok upgrade</code></span></li>
      <li>{T("A theme switch migrates no content and changes no URL", "切换主题不迁移内容，也不改变任何 URL")}<span>{T("guarantee", "保证")}</span></li>
    </ul>'''
    live_track = track([T("save", "保存"), T("D1 write", "写入 D1"), T("purge by tag", "按标签清缓存"), T("live", "上线")], True)
    frame_track = track([T("edit source", "改源码"), T("build", "构建"), T("deploy", "部署"), T("live", "上线")], False)
    if dense:
        return f'''<div class="m-score">
  <div class="m-score-row m-score-row-live"><div>{live_tag}<h3>{live_h}</h3></div>{live_track}</div>
  <div class="m-score-row"><div>{frame_tag}<h3>{frame_h}</h3></div>{frame_track}</div>
</div>
<div class="lanes-flat">
  <div class="lane"><p>{live_p}</p>{live_ul}</div>
  <div class="lane"><p>{frame_p}</p>{frame_ul}</div>
</div>'''
    return f'''<div class="lanes-twin">
  <article class="lane lane-live">{live_tag}<h3>{live_h}</h3><p>{live_p}</p>{live_track}{live_ul}</article>
  {twin()}
  <article class="lane lane-frame">{frame_tag}<h3>{frame_h}</h3><p>{frame_p}</p>{frame_track}{frame_ul}</article>
</div>'''


# ---- The sample bundle used by the hero and the multilingual demo ----
def md_source(zh, short):
    fm = [('title', '5 级钛棒' if zh else 'Grade 5 titanium bar'),
          ('grade', 'Ti-6Al-4V'), ('standard', 'ASTM B348'), ('moq', '500 kg')]
    body = (['5 级钛合金在 400 °C 以内保持强度，', '切削性能稳定。'] if zh else
            ['Grade 5 holds its strength to 400 °C', 'and machines predictably.'])
    out = ['<span class="c">---</span>']
    out += [f'<span class="k">{k}</span>: <span class="s">{v}</span>' for k, v in fm]
    out += ['<span class="c">---</span>'] + body
    if not short:
        out += ['', '<span class="k">[[inquiry]]</span>']
    return '\n'.join(out)


def editor_pane(zh=False, short=True):
    name = 'index.zh-CN.md' if zh else 'index.md'
    lang = ' lang="zh-CN"' if zh else ' lang="en"'
    label = T('Markdown source', 'Markdown 源文件')
    return f'''<figure class="m-pane m-pane-md" aria-label="{label}: {name}"><figcaption class="m-pane-h"><span class="m-pane-f"><bdo dir="ltr">content/product/{SAMPLE}/<b>{name}</b></bdo></span><span class="tag tag-live"><span class="dot"></span>{T("saved", "已保存")}</span></figcaption>
<pre{lang} tabindex="0"><code>{md_source(zh, short)}</code></pre></figure>'''


def page_pane(zh=False, chips=True):
    path = ('zh-CN/' if zh else '') + 'products/' + SAMPLE
    t = (lambda en, cn: cn) if zh else (lambda en, cn: en)
    en_on, zh_on = ('', ' class="is-on"') if zh else (' class="is-on"', '')
    chip = (f'<span class="m-chips" aria-hidden="true"><span{en_on}>EN</span>'
            f'<span{zh_on}>中文</span></span>') if chips else ''
    lang = 'zh-CN' if zh else 'en'
    label = T('Rendered page', '渲染后的页面')
    return f'''<figure class="m-pane" aria-label="{label}: example.com/{path}"><figcaption class="m-pane-h"><span class="m-url">example.com/{path}</span></figcaption>
<div class="m-page" lang="{lang}"><div class="m-page-top"><span class="m-crumb">{t('Products', '产品')} / {t('Grade 5 titanium bar', '5 级钛棒')}</span>{chip}</div>
<p class="m-page-t">{t('Grade 5 titanium bar', '5 级钛棒')}</p>
<p class="m-page-d">{t('Ti-6Al-4V round bar, 6–160 mm.', 'Ti-6Al-4V 圆棒，6–160 mm。')}</p>
<dl class="m-spec"><dt>{t('Grade', '牌号')}</dt><dd>Ti-6Al-4V</dd><dt>{t('Standard', '标准')}</dt><dd>ASTM B348</dd><dt>{t('Minimum order', '起订量')}</dt><dd>500 kg</dd></dl>
<span class="m-fakebtn">{t('Request a quotation', '索取报价')}</span></div></figure>'''


def head_pane(zh):
    base = 'https://example.com'
    en_u = f'{base}/products/{SAMPLE}'
    zh_u = f'{base}/zh-CN/products/{SAMPLE}'
    rows = [('canonical', None, zh_u if zh else en_u), ('alternate', 'en', en_u),
            ('alternate', 'zh-CN', zh_u), ('alternate', 'x-default', en_u)]
    out = ''
    for rel, hl, href in rows:
        h = f' <span class="k">hreflang</span>=<span class="s">"{hl}"</span>' if hl else ''
        out += (f'<span class="l">&lt;<span class="k">link</span> <span class="k">rel</span>='
                f'<span class="s">"{rel}"</span>{h} <span class="k">href</span>='
                f'<span class="s">"{href}"</span>&gt;</span>')
    label = T('Generated head tags', '自动生成的 head 标签')
    return (f'<figure class="m-pane m-pane-md" aria-label="{label}"><figcaption class="m-pane-h">'
            f'<span class="m-pane-f"><bdo dir="ltr">{T("generated", "自动生成")} <b>&lt;head&gt;</b></bdo></span></figcaption>'
            f'<pre lang="en" tabindex="0"><code>{out}</code></pre></figure>')


def weave():
    g = uid('wv')
    stops = ('<stop offset="0" stop-color="#A855F7"/><stop offset=".55" stop-color="#7E22CE"/>'
             '<stop offset="1" stop-color="#14B8A6"/>')
    return f'''<div class="m-weave" aria-hidden="true">
<svg class="m-weave-h" width="120" height="200" viewBox="0 0 120 200" focusable="false"><defs><linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1">{stops}</linearGradient></defs><path d="M4 100C24 56 42 56 60 100S96 144 116 100" fill="none" stroke="url(#{g})" stroke-width="6" stroke-linecap="round"/></svg>
<svg class="m-weave-v" width="60" height="96" viewBox="0 0 60 96" focusable="false"><defs><linearGradient id="{g}v" x1="0" y1="0" x2="1" y2="1">{stops}</linearGradient></defs><path d="M30 4C10 22 10 34 30 48S50 74 30 92" fill="none" stroke="url(#{g}v)" stroke-width="6" stroke-linecap="round"/></svg>
<span class="m-travel"></span></div>'''


def sample_note():
    return T('Sample content is illustrative; the company and product are fictional.',
             '示例内容仅作演示，企业与产品均为虚构。')


def strip():
    items = [
        T('Theme pages ship no client JS', '主题页面不带客户端 JS') + '<a href="#js-note" aria-describedby="js-note">*</a>',
        T('Multilingual + automatic hreflang', '多语言 + 自动 hreflang'),
        T("Starts on Cloudflare's free allowances (not unlimited)", '从 Cloudflare 免费额度起步（并非无限）'),
        T('Apache-2.0 open source', 'Apache-2.0 开源'),
    ]
    fn = T("* Exceptions: the Turnstile script on the inquiry form and one declared carousel script on Atelier's homepage. Cloudflare features you enable may inject their own scripts.",
           '* 例外：询盘表单的 Turnstile 脚本，以及 Atelier 首页声明的一个轮播脚本。你启用的 Cloudflare 功能可能会注入它们自己的脚本。')
    lis = ''.join(f'<li><span class="dot" aria-hidden="true"></span>{x}</li>' for x in items)
    return (f'<ul class="m-strip" aria-label="{T("At a glance", "概览")}">{lis}</ul>'
            f'<p class="fine m-strip-fn" id="js-note">{fn}</p>')


def i18n_demo():
    n = uid('loc')

    def panel(zh):
        return (f'<div class="m-i18n-p m-i18n-p-{"zh" if zh else "en"}">'
                + editor_pane(zh, False) + page_pane(zh, False) + head_pane(zh) + '</div>')
    return f'''<div class="m-i18n">
  <input class="m-i18n-r m-i18n-r-en" type="radio" name="{n}" id="{n}-en" checked>
  <input class="m-i18n-r m-i18n-r-zh" type="radio" name="{n}" id="{n}-zh">
  <div class="m-i18n-bar">
    <div class="m-seg"><label class="m-seg-en" for="{n}-en" lang="en">EN · en</label><label class="m-seg-zh" for="{n}-zh" lang="zh-CN">中文 · zh-CN</label></div>
    <p class="fine">{T(
      "Example site with two locales: <code>en</code> (default, no URL prefix) and <code>zh-CN</code>. <code>x-default</code> points at the default language.",
      "示例站点有两种语言：<code>en</code>（默认语言，URL 不加前缀）和 <code>zh-CN</code>。<code>x-default</code> 指向默认语言。")}</p>
  </div>
  {panel(False)}{panel(True)}
</div>
<p class="fine m-duo-cap">{T(
  "One bundle is one translation group: <code>index.md</code> is the default locale, <code>index.zh-CN.md</code> the translation. With only one language, no hreflang is emitted.",
  "一个内容包就是一个翻译组：<code>index.md</code> 是默认语言，<code>index.zh-CN.md</code> 是译文。只有一种语言时不会输出 hreflang。")} {sample_note()}</p>'''


def path_row(kind, title, nodes, note):
    """One request path: nodes strung on a thread, ending in the shuttle dot."""
    ns = ''
    for i, n in enumerate(nodes):
        a, b = n[0], n[1]
        if len(n) > 2:
            allow = f'<span class="m-allow">{n[3]}</span>' if len(n) > 3 and n[3] else ''
            op = ' open' if len(n) > 4 else ''
            ns += (f'<li class="m-node"><details{op}><summary><b>{a}</b><small>{b}</small></summary>'
                   f'<div class="m-node-b">{n[2]}{allow}</div></details></li>')
        else:
            ns += f'<li class="m-node"><div class="m-node-s"><b>{a}</b><small>{b}</small></div></li>'
    tag = {'hit': 'tag-live', 'miss': 'tag-miss'}.get(kind.lower(), 'tag-neutral')
    waves = 6 if kind == 'MEDIA' else 22
    return f'''<div class="m-path m-path-{kind.lower()}">
  <div class="m-path-h"><span class="tag {tag}">{kind}</span><h3>{title}</h3></div>
  <div class="m-path-r">{wave(waves, 6)}<ol>{ns}</ol><span class="dot m-path-dot" aria-hidden="true"></span></div>
  <p class="note">{note}</p>
</div>'''


def request_flow():
    w = T('Workers free tier: 100k requests/day, 10 ms CPU each', 'Workers 免费额度：每天 10 万次请求，每次 10 ms CPU')
    d1 = T('D1 free tier: 5 GB, 5M rows read/day, 100k rows written/day', 'D1 免费额度：5 GB，每天读 500 万行、写 10 万行')
    rows = [
        ('SAVE', T('An edit', '一次编辑'), [
            (T('Admin or CLI', '后台或 CLI'), T('the same management API', '同一套管理 API'),
             T('The React admin is served as static files; the CLI publishes folders of Markdown through the same API.',
               'React 后台以静态文件提供；CLI 通过同一套 API 发布 Markdown 目录。'),
             T('Static Assets: unlimited free requests', 'Static Assets：请求免费且不限量')),
            (T('Markdown → fragment', 'Markdown → 片段'), T('parsed and sanitised once', '解析并净化一次'),
             T('Markdown becomes a sanitised HTML fragment when you save. The stored Markdown is never modified by sanitising.',
               '保存时，Markdown 被转成净化过的 HTML 片段。净化不会改动存储的 Markdown 原文。'), w, 1),
            (T('D1 write', '写入 D1'), 'content + render_cache',
             T('One write stores the Markdown and its fragment. The fragment table is derived data and can be rebuilt.',
               '一次写入同时保存 Markdown 和它的片段。片段表是派生数据，可以重建。'), d1),
            (T('Purge by tag', '按标签清除缓存'), T('live, with no build', '上线，不需要构建'),
             T('A precise cache purge by tag. It needs a custom domain and a cache-purge token; without the token, visitors see the previous version until the cache expires.',
               '按标签精确清除缓存。需要自定义域名和清缓存令牌；没有令牌时，访客要等缓存过期才能看到新内容。'),
             T('Cache + Purge API: free; 5 tag purges per minute', 'Cache 与 Purge API：免费；按标签清除每分钟 5 次')),
        ], T('Parsing happens once, when you save.', '解析只在保存时做一次。')),
        ('HIT', T('Most visitor requests', '绝大多数访客请求'), [
            (T('Visitor', '访客'), 'GET /zh-CN/products/…'),
            (T('Edge cache', '边缘缓存'), 'cache.match() → HIT'),
            (T('Cached page returned', '直接返回缓存页面'), T('before any page code runs', '页面代码还没开始运行'),
             T('The cached page is returned before any page code runs: no rendering, and no database read on a warm Worker. The first request a newly started Worker handles also runs a start-up check against D1. CPU measured 0–1 ms across 30 confirmed hits on one rc.5 deployment; that sample does not certify later candidates.',
               '缓存页面在任何页面代码运行之前就被返回：不渲染；Worker 已启动时也不读数据库。新启动的 Worker 处理的第一个请求还会对 D1 做一次启动检查。rc.5 一次部署的 30 次确认命中里，CPU 实测为 0–1 ms；这组样本不能代表之后的候选版。')),
        ], T('No rendering, and no database read on a warm Worker.', '不渲染；Worker 已启动时也不读数据库。')),
        ('MISS', T('A cold render', '冷渲染'), [
            (T('Visitor', '访客'), 'GET'),
            (T('Edge cache', '边缘缓存'), 'MISS'),
            (T('Worker reads D1', 'Worker 读取 D1'), T('at most 4 round trips', '最多 4 次往返'),
             T('Settings, content with its fragment, and navigation — however much content the site holds. Markdown is not parsed here.',
               '设置、内容及其片段、导航——无论站点有多少内容。这一步不解析 Markdown。'), d1),
            (T('Liquid theme', 'Liquid 主题'), T('fragment → full page', '片段 → 完整页面'),
             T('The theme wraps the fragment into a full page. Templates ship inside the Worker bundle.',
               '主题把片段套成完整页面。模板随 Worker 一起打包。'), w),
            ('cache.put()', 'Cache-Tag: site, c:&lt;id&gt;, …',
             T("The page is stored in Cloudflare's cache with tags, so a later save can purge exactly the pages it changed.",
               '页面带着标签写进 Cloudflare 缓存，之后的保存就能只清除它改动过的页面。')),
        ], T('At most four D1 round trips, however much content the site holds. Markdown is not parsed here.',
             '无论站点有多少内容，最多 4 次 D1 往返。这一步不解析 Markdown。')),
        ('MEDIA', T('Images and files', '图片与文件'), [
            (T('Visitor', '访客'), T('GET image', 'GET 图片')),
            ('R2', T('served directly', '直接提供'),
             T('Media is served from an R2 custom domain, or through a <code>/media/*</code> proxy when none is configured.',
               '媒体由 R2 自定义域名直接提供；没有配置时走 <code>/media/*</code> 代理。'),
             T('R2 free tier: 10 GB-month, egress free', 'R2 免费额度：每月 10 GB，出口流量免费')),
        ], T('Images are converted to WebP with width variants in the browser on upload.',
             '图片在上传时由浏览器转成 WebP，并生成多种宽度。')),
    ]
    return ('<div class="m-paths">' + ''.join(path_row(*r) for r in rows) + '</div>'
            + '<p class="fine m-duo-cap">' + T(
                "Free allowances per Cloudflare's documentation, checked 2026-08-28. They may have changed since, and they are allowances, not an unlimited-service promise.",
                '免费额度依据 Cloudflare 官方文档，核对于 2026-08-28，之后可能有变化；它们是额度，不是无限使用的承诺。')
            + f' <a href="{url("/cost/")}">{T("The cost ladder", "成本阶梯")}</a></p>')


def measurements():
    return f'''<dl class="measure">
  <div class="stat">
    <dt>{T("Cache hit · CPU", "缓存命中 · CPU")}</dt>
    <dd><span class="big">0<small> ms p50 / p95</small></span>
    <p>{T("Maximum 1 ms across 30 confirmed hits. Zero is the value the platform recorded, not a claim of zero computation.", "30 次确认命中里最大值为 1 ms。0 是平台记录的数值，并不表示没有任何计算。")}</p></dd>
  </div>
  <div class="stat span-2">
    <dt>{T("Cold render · CPU, 30 confirmed misses", "冷渲染 · CPU，30 次确认未命中")}</dt>
    <dd>
      <div class="bars" role="img" aria-label="{T("Cold render CPU: p50 11 milliseconds, p95 35 milliseconds, maximum 44 milliseconds.", "冷渲染 CPU：p50 为 11 毫秒，p95 为 35 毫秒，最大 44 毫秒。")}">
        <div class="bar"><span>p50</span><i style="--w:25%"></i><b>11 ms</b></div>
        <div class="bar"><span>p95</span><i style="--w:79.5%;--c:var(--miss)"></i><b>35 ms</b></div>
        <div class="bar"><span>max</span><i style="--w:100%;--c:var(--miss)"></i><b>44 ms</b></div>
      </div>
      <p class="target-note">{T("Free-plan target: 10 ms. Exceeded in 16 of 30 cold samples; none failed.", "免费套餐目标：10 ms。30 次冷渲染里有 16 次超出，全部请求成功。")}</p>
    </dd>
  </div>
  <div class="stat">
    <dt>{T("Mobile Lighthouse", "移动端 Lighthouse")}</dt>
    <dd><span class="big">95–97<small> {T("performance", "性能")}</small></span>
    <p>{T("Accessibility, best practices and SEO scored 100 in all six runs (home and article).", "首页与文章页共六次测试，无障碍、最佳实践和 SEO 均为 100。")}</p></dd>
  </div>
</dl>'''


def measure_note():
    return f'''<div class="callout" style="margin-top:1rem">
  <p><strong>{T("Read these numbers for what they are.", "请按实际含义看待这些数字。")}</strong> {T(
    "They come from one isolated deployment of 0.1.0-rc.5 on a custom domain. No CPU sample has been taken for rc.6 to rc.11, which add work to cold renders, so these figures do not certify the current candidates. Cold renders above 10 ms CPU are a known, accepted limitation of the release candidates.",
    "它们来自 0.1.0-rc.5 在自定义域名上的一次隔离部署。rc.6 到 rc.11 没有重新采样，而且这些版本给冷渲染增加了开销，所以这些数字不能代表当前候选版。冷渲染超过 10 ms CPU 是候选版已知并已接受的限制。")}
    <a href="{release_href()}">{T("Full release status", "完整发布状态")}</a></p>
</div>'''


def theme_cards():
    shot = '<img class="frame-shot" src="/assets/atelier-desktop.jpg" width="1425" height="990" loading="lazy" alt="{}">'.format(
        T("Screenshot of the Atelier theme's homepage on the demo site: a fictional titanium supplier with a hero image, product navigation and a quotation button.",
          "Atelier 主题在演示站上的首页截图：虚构的钛材供应商，包含首屏大图、产品导航和询价按钮。"))
    illus = T('Illustration', '示意图')
    cards = [
        ('lead', 'Atelier', frame('demo.mallok.dev', shot), T('default', '默认'),
         T('A material-first industrial catalogue: products, families, cases, FAQs and notes.', '以材料为中心的工业产品目录：产品、产品系列、案例、FAQ 和资讯。')),
        ('', 'Journal', frame('journal', art.journal(), illus), '',
         T('A quiet theme for articles and pages.', '安静的文章与页面主题。')),
        ('', 'Gazette', frame('gazette', art.gazette(), illus), '',
         T('A trade-news magazine with a serif masthead.', '衬线报头的行业新闻杂志。')),
        ('', 'Manual', frame('manual', art.manual(), illus), '',
         T('Documentation with quick-start cards and numbered sections.', '带快速上手卡片和编号章节的文档主题。')),
        ('', 'Folio', frame('folio', art.folio(), illus), '',
         T('A light gallery portfolio with an editorial grid.', '浅色画廊式作品集，编辑式网格。')),
    ]
    out = ''
    for cls, name, fig, tag, desc in cards:
        t = f'<span class="tag tag-accent">{tag}</span>' if tag else ''
        out += (
            f'<figure class="theme-card {cls}">{fig}<figcaption>'
            f'<h3><a href="{url("/themes/")}#{name.lower()}" style="color:inherit;text-decoration:none">{name}</a>{t}</h3>'
            f'<p>{desc}</p></figcaption></figure>'
        )
    return f'<div class="themes">{out}</div>'



def pillars():
    cards = [
        ('01', T('No operations', '免运维'), T('No server to run', '不用维护服务器'),
         T('There is no host to patch and no database server to keep alive. Mallok is one Worker in your own Cloudflare account. Mallok hosts nothing, cannot reach your site, and has no account system to sign up for.',
           '没有要打补丁的主机，也没有要守着的数据库服务器。Mallok 就是你自己 Cloudflare 账号里的一个 Worker。Mallok 不托管任何东西，接触不到你的网站，也没有需要注册的账号体系。'),
         T('What gets created', '会创建什么'), T('One Worker, one D1 database, one R2 bucket', '一个 Worker、一个 D1 数据库、一个 R2 存储桶')),
        ('02', T('No build for content', '内容免构建'), T('Edits are live immediately', '改完立即生效'),
         T('Saving is one D1 write plus a precise cache purge by tag. No CI run, no build queue, no redeploy. The same goes for settings, theme options and plugin settings.',
           '保存就是一次 D1 写入，加一次按标签的精确缓存清除。没有 CI，没有构建队列，也不用重新部署。站点设置、主题选项和插件设置同样如此。'),
         T('What it needs', '前提条件'), T('A custom domain and a cache-purge token. Without the token, visitors see the previous version until the cache expires.', '一个自定义域名和一个清缓存令牌。没有令牌时，访客要等缓存过期才能看到新内容。')),
        ('03', T('No lock-in', '不锁定'), T('Your content leaves as Markdown', '内容以 Markdown 带走'),
         T('D1 stores standard Markdown with YAML front matter; media sits in R2. Export produces ordinary bundles — <code>index.md</code> plus <code>images/</code> — designed to re-import into a fresh Mallok site byte-identically.',
           'D1 里存的是带 YAML front matter 的标准 Markdown，媒体放在 R2。导出得到普通的内容包——<code>index.md</code> 加 <code>images/</code>——设计目标是能逐字节一致地重新导入另一个全新的 Mallok 站点。'),
         T('Also exportable', '同样可以导出'), T('Inquiries, as CSV', '询盘记录，CSV 格式')),
    ]
    out = ''.join(f'''<article class="card pillar"><span class="m-bead" aria-hidden="true"></span>
        <span class="num">{n} / {k.upper()}</span><h3>{t}</h3><p>{p}</p>
        <dl><dt>{dt}</dt><dd>{dd}</dd></dl></article>''' for n, k, t, p, dt, dd in cards)
    return f'<div class="m-strung">{wave(9, 8)}<div class="grid cols-3">{out}</div></div>'


def build():
    return f'''<section class="hero hero-home" aria-labelledby="hero-title">
  <div class="wrap">
    <div class="hero-copy">
      <div class="hero-logo" aria-hidden="true"></div>
      <a class="badge" href="{release_href()}"><span class="dot dot-pulse" aria-hidden="true"></span>{T("0.1 release candidate — rc.10 on npm", "0.1 候选版 —— npm 上为 rc.10")}<span aria-hidden="true">→</span></a>
      <h1 id="hero-title">{T("The Cloudflare-native CMS for <em>multilingual B2B</em> websites.", "为<em>多语言 B2B 网站</em>而生的 Cloudflare 原生 CMS")}</h1>
      <p class="lede">{T(
        "Mallok is an open-source alternative to WordPress and Ghost. Markdown content, a web admin, Liquid themes and inquiry forms — deployed into your own Cloudflare account, with no server to run and no rebuild when you publish.",
        "Mallok 是开源的 WordPress / Ghost 替代方案：Markdown 内容、网页后台、Liquid 主题和询盘表单，一并部署到你自己的 Cloudflare 账号。不用维护服务器，发布内容也不用重新构建。")}</p>
      <div class="actions">
        <a class="btn btn-primary" href="{url("/docs/")}#quick-start">{T("Get started", "开始使用")}{ARROW}</a>
        <a class="btn btn-ghost" href="{DEMO}">{T("View the live demo", "查看在线演示")}{EXT}</a>
      </div>
      <div class="cmd" role="group" aria-label="{T("Create command", "创建命令")}"><code>{CMD}</code></div>
      <p class="fine cmd-hint">{T(
        "Needs Node.js 22+ and <code>wrangler login</code>. Creates resources in, and deploys to, your Cloudflare account.",
        "需要 Node.js 22 及以上，并先执行 <code>wrangler login</code>。会在你的 Cloudflare 账号里创建资源并完成部署。")}</p>
    </div>
    <figure class="m-duo-fig">
      <div class="m-duo">{editor_pane()}{weave()}{page_pane()}</div>
      <figcaption class="fine m-duo-cap"><b>{T(
        "Save → one D1 write + a cache purge by tag → live, with no build.",
        "保存 → 一次 D1 写入 + 一次按标签清缓存 → 上线，不需要构建。")}</b> {T(
        "Purging the edge cache needs a custom domain and a cache-purge token; without the token, visitors see the previous version until the cache expires.",
        "清除边缘缓存需要自定义域名和清缓存令牌；没有令牌时，访客要等缓存过期才能看到新内容。")} {sample_note()}</figcaption>
    </figure>
    {strip()}
  </div>
</section>

<section class="section" aria-labelledby="what-title">
  <div class="wrap">
    <div class="section-head">
      {head("01", T("What is Mallok?", "Mallok 是什么"))}
      <h2 id="what-title">{T("A CMS's editing, an edge network's delivery, and content you can take with you.", "CMS 的编辑体验，边缘网络的交付速度，随时带得走的内容。")}</h2>
      <p>{T(
        "A traditional CMS gives you instant edits and charges you a server, a database and a stream of security updates. A static generator gives you fast pages and charges you a commit and a build for every typo. Mallok is built on three promises that refuse both prices.",
        "传统 CMS 改了就能上线，代价是一台服务器、一个数据库和没完没了的安全更新。静态生成器页面够快，代价是改个错别字也要提交、构建、再部署。Mallok 的三个承诺，就是这两种代价都不付。")}</p>
    </div>
    {pillars()}
  </div>
</section>

<section class="section tinted" aria-labelledby="boundary-title">
  <div class="wrap">
    <div class="section-head">
      {head("02", T("The boundary", "边界"))}
      <h2 id="boundary-title">{T("Content needs no build. The frame does.", "内容不需要构建，框架需要。")}</h2>
      <p>{T(
        "A site has two timelines, and Mallok keeps them visibly apart. Day-to-day work only touches the first; the second belongs to deployment, and the interface says so instead of pretending a theme switch is one click.",
        "一个网站有两条时间线，Mallok 把它们分得清清楚楚。日常运营只碰第一条；第二条属于部署，界面会如实说明，而不是把换主题包装成一键操作。")}</p>
    </div>
    {boundary()}
  </div>
</section>

<section class="section" aria-labelledby="i18n-title">
  <div class="wrap">
    <div class="section-head">
      {head("03", T("Multilingual", "多语言"))}
      <h2 id="i18n-title">{T("Multilingual is in the content model.", "多语言是内容模型的一部分。")}</h2>
      <p>{T(
        "Every item has its own locale and belongs to a translation group. URLs are prefixed by language, and the sitemap carries hreflang without a plugin or a setting to remember.",
        "每条内容都有自己的语言，并归属一个翻译组。URL 按语言加前缀，sitemap 自动带上 hreflang，不需要插件，也没有容易忘的开关。")}</p>
    </div>
    {i18n_demo()}
  </div>
</section>

<section class="section tinted" aria-labelledby="path-title">
  <div class="wrap">
    <div class="section-head">
      {head("04", T("The request path", "请求路径"))}
      <h2 id="path-title">{T("Rendered once, then served from the edge.", "渲染一次，之后由边缘直接返回。")}</h2>
      <p>{T(
        "Markdown is turned into a sanitised HTML fragment when you save. A visitor's first request applies the theme and stores the page in Cloudflare's cache; later requests never reach rendering. Open a node to see what it does and which free allowance it draws on.",
        "保存时，Markdown 就被转成净化过的 HTML 片段。访客的第一次请求套上主题，并把页面写进 Cloudflare 缓存；之后的请求根本不会走到渲染。点开节点，可以看到它做什么、用的是哪一项免费额度。")}</p>
    </div>
    {request_flow()}
    <h3 style="margin-top:2.5rem;font-size:1.3rem">{T("Measured on rc.5, one deployment", "rc.5 单次部署的实测数据")}</h3>
    {measurements()}
    {measure_note()}
  </div>
</section>

<section class="section" aria-labelledby="themes-title">
  <div class="wrap">
    <div class="section-head">
      {head("05", T("Themes", "主题"))}
      <h2 id="themes-title">{T("Five bundled themes, one content model.", "内置五套主题，共用一个内容模型。")}</h2>
      <p>{T(
        "Themes are declarative Liquid templates in your project's source tree. Changing theme means a redeploy — and moves no content and no URL.",
        "主题是项目源码里的声明式 Liquid 模板。更换主题需要重新部署——但不会动任何内容，也不会改任何 URL。")}</p>
    </div>
    {theme_cards()}
    <p style="margin-top:1.5rem"><a class="link-arrow" href="{url("/themes/")}">{T("See all five themes", "查看全部五套主题")}</a></p>
  </div>
</section>

<section class="section tinted" aria-labelledby="status-title">
  <div class="wrap">
    <div class="feature">
      <div>
        {head("06", T("Release status", "发布状态"))}
        <h2 id="status-title">{T("A release candidate, described honestly.", "这是候选版，我们如实说明。")}</h2>
        <p class="lede">{T(
          "<code>0.1.0-rc.10</code> is what <code>npx mallok create</code> installs today; <code>rc.11</code> is on npm's <code>next</code> tag. Both are public release candidates, not the stable 0.1.",
          "目前 <code>npx mallok create</code> 安装的是 <code>0.1.0-rc.10</code>；<code>rc.11</code> 在 npm 的 <code>next</code> 标签下。两者都是公开候选版，不是 0.1 稳定版。")}</p>
        <div class="actions" style="margin-top:1.5rem">
          <a class="btn btn-ghost" href="{release_href()}">{T("Release status and known limitations", "发布状态与已知限制")}{EXT}</a>
        </div>
      </div>
      <div class="callout">
        <h3>{T("Still open before a stable 0.1", "稳定版 0.1 之前仍未完成的事")}</h3>
        <ul>
          <li>{T("Real inquiry email delivery through Turnstile and Resend has not been verified end to end.", "通过 Turnstile 和 Resend 的真实询盘邮件送达，尚未完成端到端验证。")}</li>
          <li>{T("Cold renders exceeded the 10 ms free-plan CPU target in 16 of 30 samples on rc.5. None failed; the limitation is known and accepted for the candidates.", "rc.5 的 30 次冷渲染样本中有 16 次超过免费套餐 10 ms 的 CPU 目标。没有请求失败；这是候选版已知并接受的限制。")}</li>
          <li>{T("A full export and restore into a second deployment, and a production upgrade and rollback, are still to be accepted.", "完整导出并恢复到第二个部署，以及生产环境的升级与回滚，仍待验收。")}</li>
          <li>{T("There is no “Deploy to Cloudflare” button yet. The CLI is the way in.", "目前还没有“Deploy to Cloudflare”按钮，入口是 CLI。")}</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="start" aria-labelledby="qs-title">
  <div class="wrap">
    <div class="m-qs">
      <div>
        {head("07", T("Quick start", "快速开始"))}
        <h2 id="qs-title" style="margin-top:.9rem">{T("One command. Your account. Your content.", "一条命令，部署到你自己的账号。")}</h2>
        <p class="lede">{T(
          "Mallok creates a Worker, a D1 database and an R2 bucket in your own Cloudflare account and deploys the site there. Nothing is hosted by Mallok, and there is no Mallok account to open.",
          "Mallok 会在你自己的 Cloudflare 账号里创建 Worker、D1 数据库和 R2 存储桶，并把网站部署上去。Mallok 不托管任何东西，也不需要注册 Mallok 账号。")}</p>
      </div>
      <div class="card m-qs-card">
        <div class="cmd" role="group" aria-label="{T("Create command", "创建命令")}"><code>{CMD}</code></div>
        <p class="fine">{T(
          "Needs Node.js 22+ and <code>wrangler login</code>. Add <code>--no-deploy</code> to generate and check a project locally without creating cloud resources. Currently a 0.1 release candidate.",
          "需要 Node.js 22 及以上，并先执行 <code>wrangler login</code>。加上 <code>--no-deploy</code> 只在本地生成并检查项目，不创建云资源。当前为 0.1 候选版。")}</p>
        <ul class="m-qs-links">
          <li><a href="{url("/docs/")}#quick-start">{T("Quick start guide", "快速上手指南")}</a></li>
          <li><a href="{GH}">github.com/fobstack/mallok</a></li>
          <li><a href="{NPM}">npmjs.com/package/mallok</a></li>
          <li><a href="{DEMO}">demo.mallok.dev</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>'''
