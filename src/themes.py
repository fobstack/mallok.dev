"""Themes page."""

import art
from layout import DEMO, DOCS, EXT, T, frame, head


def swatches(colors):
    return '<div class="swatches">' + ''.join(
        f'<span><i style="--sw:{c}"></i>{c}</span>' for c in colors) + '</div>'


def detail(ident, name, tag, visual, lede, rows, colors, extra=''):
    t = f'<span class="tag tag-accent">{tag}</span>' if tag else ''
    dl = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    dl += f'<div><dt>{T("Palette", "配色")}</dt><dd>{swatches(colors)}</dd></div>'
    return f'''<article class="theme-detail" id="{ident}" aria-labelledby="{ident}-title">
  <div class="theme-art">{visual}</div>
  <div>
    <h3 id="{ident}-title">{name}{t}</h3>
    <p class="lede">{lede}</p>
    <dl class="spec">{dl}</dl>
    {extra}
  </div>
</article>'''


def build():
    illus = T('Illustration, not a screenshot', '示意图，非截图')
    shot = '<img class="frame-shot" src="/assets/atelier-desktop.jpg" width="1425" height="990" alt="{}">'.format(
        T("Screenshot of the Atelier theme on the demo site: the homepage of a fictional titanium supplier, with a hero carousel, product navigation and a quotation button.",
          "Atelier 主题在演示站上的截图：一家虚构钛材供应商的首页，包含首屏轮播、产品导航和询价按钮。"))
    kinds = T('Content kinds', '内容类型')
    best = T('Made for', '适合')
    opts = T('Options in the admin', '后台可调选项')
    js = T('Client script', '客户端脚本')
    none = T('None', '无')
    both = T('Light and dark; English and Chinese language packs', '浅色与深色；英文、中文语言包')
    modes = T('Ships with', '自带')

    atelier = detail(
        'atelier', 'Atelier', T('default', '默认'), frame('demo.mallok.dev', shot),
        T('A material-first industrial catalogue. The theme a B2B site starts on: product families, specification cards, case studies, FAQs and a quotation call to action on every product.',
          '以材料为中心的工业产品目录，B2B 站点的默认起点：产品系列、规格卡片、案例、FAQ，每个产品页都有询价入口。'),
        [
            (best, T('Manufacturers, suppliers and trading companies with a product catalogue', '有产品目录的制造商、供应商和贸易公司')),
            (kinds, T('Page, Product, Product family, Case study, FAQ, Note', '页面、产品、产品系列、案例、FAQ、资讯')),
            (opts, T('Hero headline, paragraph and badge, stats, certifications and more', '首屏标题、段落与徽标、数据亮点、资质认证等')),
            (js, T('One declared, dependency-free carousel script on the homepage only (about 4 KB). Every other page is script-free.', '仅首页有一个已声明、零依赖的轮播脚本（约 4 KB），其余页面都没有脚本。')),
            (modes, both),
        ],
        ['#152b40', '#1748bd', '#dce4eb', '#f0f4f8'],
        f'<p style="margin-top:1.25rem"><a class="btn btn-ghost" href="{DEMO}">{T("Open the Atelier demo", "打开 Atelier 演示站")}{EXT}</a></p>'
        f'<p class="fine" style="margin-top:.6rem">{T("The demo is read-only; its company and content are fictional, and it collects no inquiries.", "演示站为只读；其中的企业与内容均为虚构，也不收集询盘。")}</p>')

    journal = detail(
        'journal', 'Journal', '', frame('journal', art.journal(), illus),
        T('A quiet theme for articles and pages: one comfortable reading column, dates, optional reading time, and nothing else competing for attention.',
          '安静的文章与页面主题：一栏舒适的阅读宽度、日期、可选的阅读时长，没有任何多余的干扰。'),
        [
            (best, T('Blogs, notes, company news', '博客、随笔、企业动态')),
            (kinds, T('Page, Article', '页面、文章')),
            (opts, T('Accent colour, show reading time', '强调色、是否显示阅读时长')),
            (js, none), (modes, both),
        ],
        ['#1f2937', '#1d4ed8', '#e5e7eb', '#ffffff'])

    gazette = detail(
        'gazette', 'Gazette', '', frame('gazette', art.gazette(), illus),
        T('A trade-news magazine: serif masthead, a lead story with art, a rail of the latest stories and a subscribe band that points at the site feed by default.',
          '行业新闻杂志：衬线报头、带配图的头条、最新报道栏，以及默认指向站点 RSS 的订阅横幅。'),
        [
            (best, T('Industry news, market reports, editorial sites', '行业新闻、市场报告、媒体类站点')),
            (kinds, T('Page, Story', '页面、报道')),
            (opts, T('Masthead link, subscribe band title, text and link', '报头链接，订阅横幅的标题、文字和链接')),
            (js, none), (modes, both),
        ],
        ['#16171a', '#a11d33', '#ebebe8', '#ffffff'])

    manual = detail(
        'manual', 'Manual', '', frame('manual', art.manual(), illus),
        T('Documentation done properly: a centred hero, quick-start cards, guide rows and numbered sections in every article.',
          '认真做文档的主题：居中的首屏、快速上手卡片、指南列表，每篇文章的章节都带编号。'),
        [
            (best, T('Product manuals, handbooks, help centres', '产品手册、操作指南、帮助中心')),
            (kinds, T('Page, Guide', '页面、指南')),
            (opts, T('Hero badge and headline, help box title, text and link', '首屏徽标与标题，帮助框的标题、文字和链接')),
            (js, none), (modes, both),
        ],
        ['#1a1c1e', '#c2410c', '#ffedd5', '#fdf7f2'])

    folio = detail(
        'folio', 'Folio', '', frame('folio', art.folio(), illus),
        T('A light gallery portfolio: an oversized serif introduction, a full-bleed featured project and an editorial grid for the rest.',
          '浅色画廊式作品集：超大衬线引言、通栏的精选项目，其余作品以编辑式网格排列。'),
        [
            (best, T('Studios, designers, project showcases', '工作室、设计师、项目展示')),
            (kinds, T('Page, Project, Writing', '页面、项目、文章')),
            (opts, T('Intro paragraph, meta line, enquire link', '引言段落、说明行、咨询链接')),
            (js, none), (modes, both),
        ],
        ['#1c1a17', '#7a2b33', '#e3ddd2', '#faf8f4'])

    return f'''<section class="hero page-hero" aria-labelledby="page-title">
  <div class="wrap">
    {head("Themes", T("Five bundled designs", "内置五套设计"))}
    <h1 id="page-title">{T("Themes decide how it looks. Your content stays put.", "主题决定外观，内容原地不动。")}</h1>
    <p class="lede">{T(
      "Mallok ships five Liquid themes. Each one is a directory of templates and one stylesheet in your project, bundled into the Worker when you deploy. Pick one, adjust its options in the admin, or write your own.",
      "Mallok 自带五套 Liquid 主题。每套主题就是项目里的一个模板目录加一份样式表，部署时打包进 Worker。选一套，在后台调整它的选项，或者自己写一套。")}</p>
    <ul class="toc" aria-label="{T("Themes", "主题")}">
      <li><a href="#atelier">Atelier</a></li><li><a href="#journal">Journal</a></li><li><a href="#gazette">Gazette</a></li><li><a href="#manual">Manual</a></li><li><a href="#folio">Folio</a></li><li><a href="#switching">{T("Switching themes", "切换主题")}</a></li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="gallery-title" style="padding-bottom:0">
  <div class="wrap">
    <div class="section-head" style="margin-bottom:1.5rem">
      {head("01", T("The gallery", "主题一览"))}
      <h2 id="gallery-title">{T("One real screenshot, four honest illustrations.", "一张真实截图，四张如实标注的示意图。")}</h2>
      <p>{T(
        "Atelier is shown as it runs on the demo site. The other four are drawn here from each theme's own palette and layout description, and are labelled as illustrations.",
        "Atelier 展示的是演示站上的真实效果。另外四套是按各主题自己的配色和布局描述绘制的，并标注为示意图。")}</p>
    </div>
    {atelier}
    {journal}
    {gazette}
    {manual}
    {folio}
  </div>
</section>

<section class="section tinted" id="switching" aria-labelledby="switching-title">
  <div class="wrap">
    <div class="feature">
      <div>
        {head("02", T("Switching themes", "切换主题"))}
        <h2 id="switching-title">{T("One line of source, one redeploy. Not one click.", "改一行源码，重新部署一次。不是点一下就行。")}</h2>
        <p class="lede">{T(
          "The theme is a build-time choice in your site's Worker entry. Changing it means editing that line, building and deploying — and Mallok's admin says so rather than offering a switch that pretends otherwise.",
          "主题是站点 Worker 入口里的构建期选择。更换主题就是改这一行，然后构建、部署——Mallok 的后台会如实告知，而不是放一个假装能热切换的开关。")}</p>
        <ul class="ticks">
          <li>{T("No content is migrated, no content id changes, and by default no public URL changes.", "不迁移内容，不改内容 id，默认也不改任何公开 URL。")}</li>
          <li>{T("A content kind the new theme does not declare is rendered through its page layout; the content and its URLs stay.", "新主题没有声明的内容类型，会用它的页面布局渲染；内容和 URL 都保留。")}</li>
          <li>{T("The options a theme exposes — headlines, colours, links — are edited in the admin and are live immediately.", "主题开放的选项——标题、颜色、链接——在后台修改，立即生效。")}</li>
          <li>{T("Templates ship inside the Worker and assets go to Static Assets; a theme is never stored in D1 or R2.", "模板随 Worker 打包，静态资源交给 Static Assets；主题不会存进 D1 或 R2。")}</li>
        </ul>
      </div>
      <div>
        <figure class="code" style="margin:0">
          <figcaption class="code-bar"><span>src/worker/index.ts</span><span>{T("your generated site", "你生成的站点项目")}</span></figcaption>
          <pre tabindex="0"><code><span class="k">import</span> {{ atelier, createMallok, inquiry }} <span class="k">from</span> <span class="s">'mallok/worker'</span>;

<span class="k">export default</span> createMallok({{
  <span class="c">// One of: atelier, folio, gazette, journal, manual.</span>
  <span class="c">// Or your own, built with defineTheme.</span>
  theme: atelier,
  plugins: [inquiry],
}});</code></pre>
        </figure>
        <div class="track" aria-hidden="true" style="margin-top:1rem"><span>{T("edit this line", "改这一行")}</span><i></i><span>{T("build", "构建")}</span><i></i><span>{T("deploy", "部署")}</span><i></i><span>{T("new look, same URLs", "新外观，URL 不变")}</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="own-title">
  <div class="wrap">
    <div class="section-head">
      {head("03", T("Writing a theme", "编写主题"))}
      <h2 id="own-title">{T("Declarative by design, checkable at build time.", "声明式设计，构建时即可校验。")}</h2>
      <p>{T(
        "Third-party themes use the same documented contract as the bundled ones. There is no private interface only official themes can reach.",
        "第三方主题和内置主题用的是同一份公开的约定，不存在只有官方主题才能用的私有接口。")}</p>
    </div>
    <div class="grid cols-3">
      <article class="card"><h3>theme.json</h3><p>{T("Declares the theme's content kinds, their fields, the options it exposes to the admin, its language packs and any client script.", "声明主题的内容类型及其字段、开放给后台的选项、语言包，以及用到的客户端脚本。")}</p></article>
      <article class="card"><h3>{T("Restricted Liquid", "受限的 Liquid")}</h3><p>{T("Layouts and partials in a restricted Liquid subset, rendering a documented view object. No arbitrary JavaScript runs in a theme.", "布局和局部模板使用受限的 Liquid 子集，渲染一份有文档的视图对象。主题里不会运行任意 JavaScript。")}</p></article>
      <article class="card"><h3>{T("Distributed as source", "以源码分发")}</h3><p>{T("Copy a theme directory into your project or start from a starter. It enters your build artifact, so review it as you would any code you ship.", "把主题目录复制进项目，或从 starter 开始。它会进入你的构建产物，所以请像审查其他上线代码一样审查它。")}</p></article>
    </div>
    <p style="margin-top:1.5rem"><a class="link-arrow" href="{DOCS}THEME_FORMAT.md">{T("Read the theme format", "阅读主题格式文档（英文）")}</a></p>
  </div>
</section>'''
