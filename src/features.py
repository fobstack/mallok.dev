"""Features page."""

import art
import home
from layout import DOCS, T, head, url


def feature(num, ident, label, title, lede, ticks, side, flip=False, tinted=False):
    items = ''.join(f'<li>{t}</li>' for t in ticks)
    return f'''<section class="section{" tinted" if tinted else ""}" id="{ident}" aria-labelledby="{ident}-title">
  <div class="wrap">
    <div class="feature{" flip" if flip else ""}">
      <div>
        {head(num, label)}
        <h2 id="{ident}-title">{title}</h2>
        <p class="lede">{lede}</p>
        <ul class="ticks">{items}</ul>
      </div>
      <div>{side}</div>
    </div>
  </div>
</section>'''


def cli_table():
    rows = [
        ('mallok create &lt;dir&gt;', T('Create a project, verify it, then deploy it to your Cloudflare account. <code>--no-deploy</code> stops before any cloud resource is created.', '创建项目、校验，然后部署到你的 Cloudflare 账号。加 <code>--no-deploy</code> 则不创建任何云资源。')),
        ('mallok publish &lt;dir&gt;', T('Publish one or more content bundles, images included.', '发布一个或多个内容包，连同图片。')),
        ('mallok import &lt;dir&gt;', T('Import bundles, keeping the status their front matter says.', '导入内容包，状态以 front matter 为准。')),
        ('mallok export &lt;dir&gt;', T('Export the whole site to a directory of bundles.', '把整个站点导出为内容包目录。')),
        ('mallok build &lt;dir&gt;', T('Compile a local directory into a static site, touching neither D1 nor the network.', '把本地目录编译成静态网站，不碰 D1，也不联网。')),
        ('mallok upgrade --to &lt;version&gt;', T('Move a project onto another Mallok release. Takes effect when you redeploy.', '把项目切换到另一个 Mallok 版本，重新部署后生效。')),
        ('mallok preview &lt;dir&gt;', T('Render bundles locally, offline.', '在本地离线渲染内容包。')),
    ]
    body = ''.join(f'<tr><th scope="row"><code>{c}</code></th><td>{d}</td></tr>' for c, d in rows)
    return f'''<div class="table-wrap" tabindex="0" role="region" aria-label="{T("CLI commands", "CLI 命令")}">
<table class="data narrow">
<thead><tr><th scope="col">{T("Command", "命令")}</th><th scope="col">{T("What it does", "作用")}</th></tr></thead>
<tbody>{body}</tbody>
</table></div>
<p class="fine" style="margin-top:.75rem">{T(
  'Also: <code>media push</code>, <code>setup-key</code>, <code>repair</code>, <code>destroy</code>. Every site command accepts <code>--dry-run</code> and <code>--json</code>. See the <a href="' + DOCS + 'CLI.md">CLI reference</a>.',
  '此外还有 <code>media push</code>、<code>setup-key</code>、<code>repair</code>、<code>destroy</code>。站点类命令都支持 <code>--dry-run</code> 和 <code>--json</code>。详见 <a href="' + DOCS + 'CLI.md">CLI 参考（英文）</a>。')}</p>'''


def cache_table():
    rows = [
        (T('Edge cache', '边缘缓存'), 'Cache API', T('The request URL', '请求 URL'), T('Visitor requests never reach rendering', '访客请求不会走到渲染')),
        (T('Fragment cache', '片段缓存'), 'D1 <code>render_cache</code>', T('Markdown hash + pipeline version + plugin hash', 'Markdown 哈希 + 管线版本 + 插件哈希'), T('A cold render never parses Markdown', '冷渲染不解析 Markdown')),
        (T('Template cache', '模板缓存'), T('Isolate module scope', 'isolate 模块作用域'), T('Theme id + version', '主题 id + 版本'), T('Liquid is never parsed twice in one isolate', '同一个 isolate 里 Liquid 只解析一次')),
    ]
    body = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in rows)
    return f'''<div class="table-wrap" tabindex="0" role="region" aria-label="{T("The three cache layers", "三层缓存")}">
<table class="data">
<thead><tr><th scope="col">{T("Layer", "层")}</th><th scope="col">{T("Where", "位置")}</th><th scope="col">{T("Key", "键")}</th><th scope="col">{T("What it solves", "解决什么")}</th></tr></thead>
<tbody>{body}</tbody>
</table></div>'''


def roadmap():
    return f'''<ol class="roadmap">
  <li><h3>0.2</h3><ul>
    <li>{T("A visual editor", "可视化编辑器")}</li>
    <li>{T("Product import from CSV", "从 CSV 批量导入产品")}</li>
    <li>{T("An AI translation plugin", "AI 翻译插件")}</li>
    <li>{T("An inquiry cart: several products in one request for quotation", "询盘车：多个产品合并成一份询价")}</li>
    <li>{T("A WordPress importer", "WordPress 导入工具")}</li>
  </ul></li>
  <li><h3>0.3</h3><ul>
    <li>{T("Payment for samples and small orders through a hosted checkout page", "通过第三方托管的收银页面，支付样品和小额订单")}</li>
  </ul></li>
  <li><h3>1.0</h3><ul>
    <li>{T("A hosted setup assistant for non-technical owners", "面向非技术用户的托管安装助手")}</li>
    <li>{T("Marketplaces for themes, starters and plugins", "主题、starter 和插件市场")}</li>
  </ul></li>
</ol>'''


def build():
    toc = [
        ('content', T('Content', '内容')), ('multilingual', T('Multilingual', '多语言')),
        ('themes', T('Themes', '主题')), ('inquiry', T('Inquiries', '询盘')),
        ('admin', T('Admin', '后台')), ('cli', 'CLI'),
        ('rendering', T('Rendering & caching', '渲染与缓存')), ('seo', 'SEO'),
        ('static', T('Static build', '静态构建')), ('boundary', T('The boundary', '边界')),
        ('limits', T('What it is not', '不做什么')), ('roadmap', T('Roadmap', '路线图')),
    ]
    toc_html = ''.join(f'<li><a href="#{i}">{l}</a></li>' for i, l in toc)

    md_side = f'''<figure class="code" style="margin:0">
  <figcaption class="code-bar"><span>{T("a content bundle", "一个内容包")}</span><span>{T("import / export format", "导入 / 导出格式")}</span></figcaption>
  <pre tabindex="0"><code>titanium-price-2026-08/
├── index.md        <span class="c"># {T("the default locale", "默认语言")}</span>
├── index.zh-CN.md  <span class="c"># {T("other locales, by filename", "其他语言，写在文件名里")}</span>
├── index.de.md
├── images/         <span class="c"># {T("shared by every locale", "各语言共用")}</span>
│   ├── hero.jpg
│   └── chart.png
└── files/
    └── datasheet.pdf</code></pre>
</figure>'''

    ml_side = f'''<div class="mini">
  <div class="mini-row"><span>/products/titanium-bar</span><span>en · {T("main language, no prefix", "主语言，无前缀")}</span></div>
  <div class="mini-row"><span>/zh-CN/products/titanium-bar</span><span>zh-CN</span></div>
  <div class="mini-row"><span>/de/products/titanium-bar</span><span>de</span></div>
</div>
<figure class="code" style="margin:1rem 0 0">
  <figcaption class="code-bar"><span>sitemap.xml</span><span>{T("generated", "自动生成")}</span></figcaption>
  <pre tabindex="0"><code>&lt;<span class="k">url</span>&gt;
  &lt;<span class="k">loc</span>&gt;https://example.com/products/titanium-bar&lt;/<span class="k">loc</span>&gt;
  &lt;<span class="k">xhtml:link</span> rel=<span class="s">"alternate"</span> hreflang=<span class="s">"en"</span> href=<span class="s">"…/products/titanium-bar"</span>/&gt;
  &lt;<span class="k">xhtml:link</span> rel=<span class="s">"alternate"</span> hreflang=<span class="s">"zh-CN"</span> href=<span class="s">"…/zh-CN/products/titanium-bar"</span>/&gt;
  &lt;<span class="k">xhtml:link</span> rel=<span class="s">"alternate"</span> hreflang=<span class="s">"de"</span> href=<span class="s">"…/de/products/titanium-bar"</span>/&gt;
&lt;/<span class="k">url</span>&gt;</code></pre>
</figure>
<p class="fine" style="margin-top:.6rem">{T("Simplified illustration of the sitemap output.", "sitemap 输出的简化示意。")}</p>'''

    theme_side = f'''<figure class="code" style="margin:0">
  <figcaption class="code-bar"><span>src/themes/atelier/theme.json</span><span>{T("excerpt", "节选")}</span></figcaption>
  <pre tabindex="0"><code>{{
  <span class="k">"id"</span>: <span class="s">"atelier"</span>,
  <span class="k">"kinds"</span>: {{
    <span class="k">"product"</span>: {{
      <span class="k">"layout"</span>: <span class="s">"layouts/product.liquid"</span>,
      <span class="k">"listLayout"</span>: <span class="s">"layouts/list.liquid"</span>,
      <span class="k">"base"</span>: <span class="s">"products"</span>,
      <span class="k">"fields"</span>: {{
        <span class="k">"grade"</span>: {{ <span class="k">"type"</span>: <span class="s">"string"</span>, <span class="k">"label"</span>: <span class="s">"Grade"</span> }},
        <span class="k">"specs"</span>: {{ <span class="k">"type"</span>: <span class="s">"keyvalue"</span>, <span class="k">"label"</span>: <span class="s">"Properties"</span> }},
        <span class="k">"gallery"</span>: {{ <span class="k">"type"</span>: <span class="s">"image[]"</span>, <span class="k">"label"</span>: <span class="s">"Gallery"</span> }},
        <span class="k">"datasheet"</span>: {{ <span class="k">"type"</span>: <span class="s">"file"</span>, <span class="k">"accept"</span>: [<span class="s">".pdf"</span>] }}
      }}
    }}
  }},
  <span class="k">"clientScripts"</span>: [ <span class="c">/* {T("declared, never implicit", "必须显式声明")} */</span> ]
}}</code></pre>
</figure>'''

    inquiry_side = f'''<div class="flow">
  <div class="flow-row" style="grid-template-columns:minmax(0,1fr)">
    <ol class="steps">
      <li><span class="step">{T("Buyer submits the form", "买家提交表单")}<small>[[inquiry]]</small></span></li>
      <li><span class="step">Turnstile<small>{T("spam check", "防刷校验")}</small></span></li>
      <li><span class="step">{T("Stored in D1", "存入 D1")}</span></li>
      <li><span class="step">Resend<small>{T("email to you, optional confirmation to the buyer", "发给你，可选自动回复买家")}</small></span></li>
      <li><span class="step">{T("Admin inbox", "后台收件箱")}<small>{T("CSV export", "CSV 导出")}</small></span></li>
    </ol>
  </div>
</div>
<div class="callout" style="margin-top:1rem">
  <p><strong>{T("In progress:", "进行中：")}</strong> {T(
    "real Turnstile and Resend delivery has not yet been accepted end to end for the current release candidates. Test with addresses you control before relying on it.",
    "当前候选版尚未完成真实 Turnstile 与 Resend 送达的端到端验收。正式依赖之前，请先用自己掌握的邮箱测试。")}</p>
</div>'''

    admin_side = f'''<div class="mini">
  <div class="mini-row"><span>{T("Content", "内容")}</span><span>{T("Markdown editor + fields from the kind's schema", "Markdown 编辑器 + 按类型 schema 生成的字段")}</span></div>
  <div class="mini-row"><span>{T("Media", "媒体")}</span><span>{T("upload, WebP variants, picker", "上传、WebP 多宽度、选择器")}</span></div>
  <div class="mini-row"><span>{T("Inquiries", "询盘")}</span><span>{T("read like an inbox, export CSV", "像收件箱一样查看，可导出 CSV")}</span></div>
  <div class="mini-row"><span>{T("Settings", "设置")}</span><span>{T("site, languages, navigation, SEO, email, cache", "站点、语言、导航、SEO、邮件、缓存")}</span></div>
  <div class="mini-row"><span>{T("Plugins", "插件")}</span><span>{T("enable switch + settings, live", "启用开关与设置，立即生效")}</span></div>
  <div class="mini-row"><span>{T("Themes, plugin install", "主题、插件安装")}</span><span class="warn">{T("needs a redeploy — and says so", "需要重新部署——界面会明说")}</span></div>
</div>'''

    seo_side = f'''<ul class="chips" aria-label="{T("SEO output", "SEO 输出")}">
  <li>sitemap.xml + hreflang</li><li>RSS</li><li>rel=canonical</li><li>Open Graph</li>
  <li>JSON-LD · Organization</li><li>JSON-LD · Article</li><li>JSON-LD · Product</li><li>JSON-LD · FAQ</li>
  <li>{T("301 on slug change", "改 slug 自动 301")}</li><li>{T("signed draft preview links", "带签名的草稿预览链接")}</li>
</ul>
<p class="fine" style="margin-top:1rem">{T(
  "Deliberately absent: automatic language detection and redirection. Visitors and crawlers get the URL they asked for.",
  "有意不做：自动识别语言并跳转。访客和爬虫请求哪个 URL，就得到哪个 URL。")}</p>'''

    static_side = f'''<figure class="code" style="margin:0">
  <figcaption class="code-bar"><span>{T("terminal", "终端")}</span><span>{T("the path without D1", "不用 D1 的那条路")}</span></figcaption>
  <pre tabindex="0"><code>mallok build ./my-site \\
  --theme ./src/themes/atelier \\
  --origin https://example.com</code></pre>
</figure>
<div class="mini" style="margin-top:1rem">
  <div class="mini-row"><span>{T("Inquiry form", "询盘表单")}</span><span class="warn">{T("not available — removed and reported", "不可用——构建时移除并提示")}</span></div>
  <div class="mini-row"><span>{T("Admin editor", "后台编辑")}</span><span class="warn">{T("not available", "不可用")}</span></div>
  <div class="mini-row"><span>{T("Instant and scheduled publishing", "即时发布与定时发布")}</span><span class="warn">{T("rebuild and redeploy instead", "改为重新构建并部署")}</span></div>
</div>'''

    return f'''<section class="hero page-hero" aria-labelledby="page-title">
  <div class="wrap">
    {head("Features", T("What ships in 0.1", "0.1 包含什么"))}
    <h1 id="page-title">{T("Everything a multilingual company site needs, and a clear line around the rest.", "多语言企业官网需要的都有，其余的边界也讲清楚。")}</h1>
    <p class="lede">{T(
      "Mallok is a complete CMS — content, themes, an admin, a CLI, inquiries and SEO — published as one npm package and running as one Worker. This page lists what it does, how it does it, and what it deliberately leaves out.",
      "Mallok 是一套完整的 CMS——内容、主题、后台、CLI、询盘和 SEO——以一个 npm 包发布，以一个 Worker 运行。这一页列出它做什么、怎么做，以及有意不做什么。")}</p>
    <nav aria-label="{T("On this page", "本页目录")}"><ul class="toc">{toc_html}</ul></nav>
  </div>
</section>

{feature("01", "content", T("Content", "内容"),
  T("Standard Markdown, stored as written.", "标准 Markdown，原样存储。"),
  T("Content is CommonMark with GFM and a YAML front-matter block. D1 holds the complete text of each file; images and attachments are referenced by relative path and live in R2.",
    "内容是 CommonMark + GFM，外加一段 YAML front matter。D1 保存每个文件的完整文本；图片和附件用相对路径引用，文件存放在 R2。"),
  [
    T("Draft, published and scheduled states.", "草稿、已发布、定时发布三种状态。"),
    T("Content kinds beyond page and article are declared by the theme — the B2B starter brings products, categories, cases, FAQs and news.", "页面和文章之外的内容类型由主题声明——B2B starter 自带产品、分类、案例、FAQ 和新闻。"),
    T("Content is always treated as untrusted: HTML is sanitised against an allow-list when the fragment is generated, and the stored Markdown is never modified.", "内容一律视为不可信：生成片段时按白名单净化 HTML，存储的 Markdown 原文不会被改动。"),
    T("Export produces the same bundles import accepts. Round-trip fidelity is covered by tests; a full restore into a second live deployment is still on the acceptance list.", "导出得到的内容包，就是导入接受的格式。往返一致性有测试覆盖；完整恢复到第二个线上部署仍在验收清单上。"),
  ], md_side)}

{feature("02", "multilingual", T("Multilingual", "多语言"),
  T("Languages are a property of content, not a plugin.", "语言是内容的属性，不是插件。"),
  T("Each item carries a locale and a translation group. The main language has no URL prefix; every other language is served under its own.",
    "每条内容都带语言和翻译组。主语言的 URL 不加前缀，其他语言各自有前缀。"),
  [
    T("hreflang in the sitemap and canonical links are generated automatically.", "sitemap 里的 hreflang 和 canonical 链接自动生成。"),
    T("A bundle holds every translation of one item and shares its images between them.", "一个内容包包含同一条内容的全部译文，并共用图片。"),
    T("Theme interface strings follow the site's language through language packs.", "主题的界面文字通过语言包跟随站点语言。"),
    T("0.1 delivers the model, the URL rules and simple translation management. Machine translation is a roadmap item, not a current feature.", "0.1 提供内容模型、URL 规则和基础的翻译管理。机器翻译在路线图里，目前还没有。"),
  ], ml_side, flip=True, tinted=True)}

{feature("03", "themes", T("Themes and plugins", "主题与插件"),
  T("Declarative themes. Real plugins. Both honest about deployment.", "声明式主题，真正的插件，部署这件事都不含糊。"),
  T("A theme is a directory of restricted Liquid templates plus a theme.json. A plugin is real JavaScript with its own tables, routes, settings and scheduled work. Both live in your project's source and are bundled at build time.",
    "主题是一个目录：受限的 Liquid 模板加一份 theme.json。插件是真正的 JavaScript，有自己的数据表、路由、设置和定时任务。两者都放在项目源码里，构建时打包。"),
  [
    T("Themes contain no arbitrary JavaScript; any client script must be declared in theme.json.", "主题里没有任意 JavaScript；需要的客户端脚本必须在 theme.json 里声明。"),
    T("Switching a theme changes no content id and no public URL. A kind the new theme does not know renders through its page layout.", "切换主题不改内容 id，也不改公开 URL。新主题不认识的类型，会用它的页面布局渲染。"),
    T("Official and third-party plugins take the same path: source in the repository, bundled at build.", "官方插件和第三方插件走同一条路：源码进仓库，构建时打包。"),
    T("<strong>Installing or changing a theme or plugin needs a build and a redeploy.</strong> Once deployed, a plugin's enable switch, settings and secrets are live from the admin.", "<strong>安装或更换主题、插件都需要构建并重新部署。</strong>部署之后，插件的启用开关、设置和密钥可以在后台即时修改。"),
    T("A plugin runs with real access inside your own account — the same trust boundary as a WordPress plugin. Review it like any other code you ship.", "插件在你自己的账号里真实运行——信任边界和 WordPress 插件一样。请像审查其他上线代码那样审查它。"),
  ], theme_side)}

{feature("04", "inquiry", T("Inquiries", "询盘"),
  T("One form, from product page to inbox.", "一张表单，从产品页到收件箱。"),
  T("The official inquiry plugin is what turns a catalogue into a sales channel. Put <code>[[inquiry]]</code> in a page and the form renders when the plugin is enabled.",
    "官方询盘插件把产品目录变成获客渠道。在页面里写上 <code>[[inquiry]]</code>，启用插件后表单就会出现。"),
  [
    T("Cloudflare Turnstile against spam.", "Cloudflare Turnstile 防刷。"),
    T("Email to you through Resend, with an optional automatic confirmation to the buyer.", "通过 Resend 给你发信，可选自动回复买家。"),
    T("Every inquiry is stored in D1, readable in the admin like an inbox, exportable as CSV.", "每条询盘都存进 D1，在后台像收件箱一样查看，可导出 CSV。"),
    T("Third-party keys are encrypted (AES-GCM) before they are stored in D1; they never go into content or source.", "第三方密钥以 AES-GCM 加密后才写入 D1，不会出现在内容或源码里。"),
  ], inquiry_side, flip=True, tinted=True)}

{feature("05", "admin", T("Admin", "后台"),
  T("An admin that only shows what you can actually change.", "后台只展示你真正能改的东西。"),
  T("A React single-page admin served from the same Worker, in English and Simplified Chinese. Nobody using it needs to know what a Worker, D1 or a cache tag is.",
    "React 单页后台，由同一个 Worker 提供，支持英文和简体中文。使用它的人不需要知道 Worker、D1 或缓存标签是什么。"),
  [
    T("A Markdown source editor beside a field form generated from the content kind's schema.", "Markdown 源码编辑器，配上按内容类型 schema 生成的字段表单。"),
    T("A media library; uploads are converted to WebP with width variants in the browser.", "媒体库；上传时由浏览器转成 WebP 并生成多种宽度。"),
    T("A setup wizard for the administrator, site name, languages, example content and domain.", "安装向导：管理员、站点名称、语言、示例内容和域名。"),
    T("Scoped API tokens for the CLI and for content pipelines.", "给 CLI 和内容流水线使用的分权限 API 令牌。"),
  ], admin_side)}

<section class="section tinted" id="cli" aria-labelledby="cli-title">
  <div class="wrap">
    <div class="section-head">
      {head("06", "CLI")}
      <h2 id="cli-title">{T("The same data path, from a terminal.", "同一条数据通路，在终端里走。")}</h2>
      <p>{T("The CLI talks to the same management API as the admin, so a folder published from CI and an article saved in the browser are stored, rendered and purged the same way.",
            "CLI 调用的是后台同一套管理 API，所以 CI 里发布的目录和浏览器里保存的文章，存储、渲染和清缓存的方式完全一样。")}</p>
    </div>
    {cli_table()}
  </div>
</section>

<section class="section" id="rendering" aria-labelledby="rendering-title">
  <div class="wrap">
    <div class="section-head">
      {head("07", T("Rendering and caching", "渲染与缓存"))}
      <h2 id="rendering-title">{T("Two stages, three caches, one deterministic core.", "两个阶段，三层缓存，一个确定性的渲染核心。")}</h2>
      <p>{T("The render core has no platform dependencies, so the CLI's local preview, the admin's live preview and the Worker in production run the same function and produce the same bytes.",
            "渲染核心不依赖任何平台 API，所以 CLI 的本地预览、后台的实时预览和线上的 Worker 跑的是同一个函数，输出同样的字节。")}</p>
    </div>
    <div class="diagram" tabindex="0" role="region" aria-label="{T("Two-stage rendering diagram", "两阶段渲染示意图")}">{art.pipeline()}</div>
    <div style="margin-top:1.25rem">{cache_table()}</div>
    <div class="grid cols-3" style="margin-top:1.25rem">
      <article class="card"><h3>{T("Bounded cold renders", "有界的冷渲染")}</h3><p>{T("A cold render makes at most four D1 round trips regardless of how much content the site holds. List pages never parse body Markdown and never query per item.", "无论站点有多少内容，一次冷渲染最多 4 次 D1 往返。列表页从不解析正文 Markdown，也不会逐条查询。")}</p></article>
      <article class="card"><h3>{T("Purge by tag", "按标签清除")}</h3><p>{T("Every page carries Cache-Tags for the site, its content, its kind and its locale. A save purges exactly the pages that show the item. A failed purge is recorded and shown in the admin on <code>main</code>; released candidates up to rc.11 can report a failed purge as success.", "每个页面都带站点、内容、类型和语言的 Cache-Tag。保存时只清除展示了该内容的页面。在 <code>main</code> 分支上，清除失败会被记录并显示在后台；已发布的候选版（到 rc.11）可能把失败的清除显示为成功。")}</p></article>
      <article class="card"><h3>{T("The edge keeps it, the browser revalidates", "边缘缓存长存，浏览器每次校验")}</h3><p>{T("Pages are cached at the edge for an hour by default (adjustable) and browsers are told to revalidate, so a purge is not defeated by a copy sitting in someone's browser.", "页面默认在边缘缓存一小时（可调），同时要求浏览器每次重新校验，这样清除缓存不会被访客浏览器里的旧副本抵消。")}</p></article>
    </div>
    <h3 style="margin-top:2.5rem;font-size:1.2rem">{T("Measured on rc.5, one deployment", "rc.5 单次部署的实测数据")}</h3>
    {home.measurements()}
    {home.measure_note()}
  </div>
</section>

{feature("08", "seo", "SEO",
  T("Structured output, built into the core.", "结构化输出，内置在核心里。"),
  T("Search output is not left to a plugin or to each theme author. Every Mallok site produces the same set.",
    "搜索相关的输出不交给插件，也不交给各个主题作者。每个 Mallok 站点的输出都是同一套。"),
  [
    T("Sitemap with hreflang, RSS feeds, canonical links and Open Graph tags.", "带 hreflang 的 sitemap、RSS、canonical 链接和 Open Graph 标签。"),
    T("JSON-LD for Organization, Article, Product and FAQ.", "Organization、Article、Product、FAQ 四类 JSON-LD。"),
    T("Changing a slug writes a 301 redirect automatically.", "修改 slug 会自动写入 301 跳转。"),
    T("Semantic HTML and no theme JavaScript on content pages. Cloudflare features you turn on, such as analytics, can still inject their own script.", "内容页是语义化 HTML，主题不输出 JavaScript。你在 Cloudflare 启用的功能（如统计分析）仍可能注入它自己的脚本。"),
  ], seo_side, tinted=True)}

{feature("09", "static", T("Static build", "静态构建"),
  T("Prefer plain files? There is a second path.", "更想要纯静态文件？还有第二条路。"),
  T("<code>mallok build</code> compiles a local directory — the same layout <code>mallok export</code> produces — into a complete static site: kinds, tags, several languages and the SEO endpoints, through the same render functions.",
    "<code>mallok build</code> 把本地目录（与 <code>mallok export</code> 的导出结构相同）编译成完整的静态站点：内容类型、标签、多语言和 SEO 端点，用的是同一套渲染函数。"),
  [
    T("It touches neither D1 nor the network.", "不碰 D1，也不联网。"),
    T("Broken references are reported as errors instead of silently dropped.", "失效的引用会报错，而不是悄悄丢掉。"),
    T("It is a second path beside the Worker, not a replacement: the costs on the right are the price.", "它是 Worker 之外的另一条路，不是替代品：右边列出的就是代价。"),
  ], static_side, flip=True)}

<section class="section tinted" id="boundary" aria-labelledby="boundary-title">
  <div class="wrap">
    <div class="section-head">
      {head("10", T("The boundary", "边界"))}
      <h2 id="boundary-title">{T("What is live immediately, and what needs a redeploy.", "哪些立即生效，哪些需要重新部署。")}</h2>
      <p>{T("This is the single most important line in the product, so it is drawn in the interface as well as here.", "这是产品里最重要的一条线，所以不只写在这里，界面上也画得清清楚楚。")}</p>
    </div>
    {home.boundary(dense=True)}
  </div>
</section>

<section class="section" id="limits" aria-labelledby="limits-title">
  <div class="wrap">
    <div class="section-head">
      {head("11", T("What it is not", "不做什么"))}
      <h2 id="limits-title">{T("Deliberately out of scope for 0.1.", "0.1 有意不做的事。")}</h2>
      <p>{T("Knowing where a tool stops is part of trusting it.", "知道一个工具的边界在哪里，才谈得上信任它。")}</p>
    </div>
    <div class="grid cols-3">
      <article class="card"><h3>{T("Not a hosting service", "不是托管服务")}</h3><p>{T("No Mallok accounts, billing or multi-tenant control plane. Your site runs in your Cloudflare account and nowhere else.", "没有 Mallok 账号、计费或多租户控制台。你的网站只运行在你自己的 Cloudflare 账号里。")}</p></article>
      <article class="card"><h3>{T("Not a shop — yet", "暂时不是商城")}</h3><p>{T("0.1 goes as far as inquiries: no cart, payment, membership or comments. Commerce is a later direction, as plugins.", "0.1 做到询盘为止：没有购物车、支付、会员和评论。电商是后续方向，以插件形式提供。")}</p></article>
      <article class="card"><h3>{T("Not a compatibility layer", "不是兼容层")}</h3><p>{T("It does not run PHP, WordPress themes or plugins, or Astro or Next.js projects. A WordPress importer is on the roadmap.", "不运行 PHP，不兼容 WordPress 主题和插件，也不运行 Astro 或 Next.js 项目。WordPress 导入工具在路线图里。")}</p></article>
      <article class="card"><h3>{T("Not for application logic", "不适合写业务应用")}</h3><p>{T("Sites that need freely written server-side business logic, permission systems or complex form flows are a poor fit.", "需要自由编写服务端业务逻辑、权限体系或复杂表单流程的站点，并不适合用它。")}</p></article>
      <article class="card"><h3>{T("Not collaborative editing", "没有协同编辑")}</h3><p>{T("There is no real-time co-editing in 0.1.", "0.1 没有实时多人协作编辑。")}</p></article>
      <article class="card"><h3>{T("Not multi-cloud", "不是多云")}</h3><p>{T("One cloud vendor and one email provider, stated rather than disguised. The mitigation is that content and inquiries export at any time.", "只依赖一家云厂商和一家邮件服务商，我们直说而不掩饰。对策是内容和询盘随时可以导出。")}</p></article>
    </div>
  </div>
</section>

<section class="section tinted" id="roadmap" aria-labelledby="roadmap-title">
  <div class="wrap">
    <div class="section-head">
      {head("12", T("Roadmap", "路线图"))}
      <h2 id="roadmap-title">{T("Directions, not commitments.", "是方向，不是承诺。")}</h2>
      <p>{T("None of this is in the current release candidates, and none of it has a date.", "下面这些都不在当前候选版里，也都没有排期。")}</p>
    </div>
    {roadmap()}
    <p class="fine" style="margin-top:1rem">{T(
      'Source: <a href="' + DOCS + 'PRODUCT_VISION.md">the product vision</a>, section 9. A “Deploy to Cloudflare” button is also planned and is not available yet.',
      '来源：<a href="' + DOCS + 'PRODUCT_VISION.md">产品愿景（英文）</a>第 9 节。“Deploy to Cloudflare” 按钮也在计划中，目前尚不可用。')}</p>
  </div>
</section>'''
