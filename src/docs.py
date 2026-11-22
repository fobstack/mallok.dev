"""Docs landing page: quick start plus entry points into the GitHub docs."""

from layout import DEMO, DOCS, EXT, GH, NPM, T, head


def doc_list(items, cols=True):
    out = ''
    for href, title, what in items:
        where = href.replace(GH + '/blob/main/', '')
        out += (
            f'<li><a href="{href}"><strong>{title}</strong>'
            f'<span class="where">{where}</span><span class="what">{what}</span></a></li>'
        )
    return f'<ul class="doc-list{" cols" if cols else ""}">{out}</ul>'


def build():
    gs = DOCS + T('GETTING_STARTED.md', 'zh-CN/GETTING_STARTED.md')
    rs = DOCS + T('RELEASE_STATUS.md', 'zh-CN/RELEASE_STATUS.md')
    en = T('', '（英文）')

    start = [
        (gs, T('Create your first site', '创建第一个网站'),
         T('Install, deploy, finish setup, publish a product, configure inquiries, keep an export.', '安装、部署、完成初始化、发布产品、配置询盘、保留一份导出。')),
        (rs, T('Release status and known limitations', '发布状态与已知限制'),
         T('What has been measured, on which candidate, and what is still open.', '哪些内容实测过、在哪个候选版上测的、还有什么没完成。')),
        (DOCS + T('README.md', 'zh-CN/README.md'), T('Documentation index', '中文文档导航'),
         T('Every document, in reading order.', '中文已翻译的内容，以及英文技术参考的入口。')),
        (GH + '/blob/main/' + T('README.md', 'README.zh-CN.md'), T('Project README', '项目介绍'),
         T('Overview, and how to try the framework source locally.', '项目概览，以及如何在本地试用框架源码。')),
    ]
    design = [
        (DOCS + 'PRODUCT_VISION.md', T('Product vision', '产品愿景') + en,
         T('What Mallok is, who it is for, the promises, the cost ladder, the roadmap and the non-goals.', 'Mallok 是什么、给谁用、有哪些承诺、成本阶梯、路线图和不做的事。')),
        (DOCS + 'ARCHITECTURE.md', T('Architecture', '架构') + en,
         T('The request path, two-stage rendering, the three cache layers, the content model, security boundaries.', '请求路径、两阶段渲染、三层缓存、内容模型、安全边界。')),
        (DOCS + 'CONTENT_FORMAT.md', T('Content format', '内容格式') + en,
         T('Content bundles, front-matter fields and the import/export contract.', '内容包、front matter 字段，以及导入导出的约定。')),
        (DOCS + 'DATA_MODEL.md', T('Data model', '数据模型') + en,
         T('The D1 schema, indexes, constraints and migration rules.', 'D1 表结构、索引、约束和迁移规则。')),
        (DOCS + 'CLOUDFLARE_RESOURCES.md', T('Cloudflare resources', 'Cloudflare 资源') + en,
         T('What gets created in your account, quotas, naming, backup and deletion.', '账号里会创建哪些资源，配额、命名、备份与删除。')),
        (DOCS + 'TECH_STACK.md', T('Tech stack', '技术栈') + en,
         T('Runtime, dependency layers and what is deliberately forbidden.', '运行时、依赖分层，以及明确禁止使用的东西。')),
    ]
    build_on = [
        (DOCS + 'THEME_FORMAT.md', T('Theme format', '主题格式') + en,
         T('theme.json, content kinds and fields, the view contract, the restricted Liquid subset, language packs.', 'theme.json、内容类型与字段、视图约定、受限的 Liquid 子集、语言包。')),
        (DOCS + 'PLUGIN_API.md', T('Plugin API', '插件 API') + en,
         T('plugin.json, hooks, capabilities, lifecycle, and the official inquiry plugin.', 'plugin.json、钩子、能力、生命周期，以及官方询盘插件。')),
        (DOCS + 'CLI.md', T('CLI reference', 'CLI 参考') + en,
         T('Commands, arguments, authentication, idempotence, exit codes.', '命令、参数、认证、幂等规则、退出码。')),
        (DOCS + 'ADMIN.md', T('Admin', '后台') + en,
         T('Information architecture, the setup wizard, the editor and the media library.', '信息架构、安装向导、编辑器和媒体库。')),
        (DOCS + 'SEO_PERFORMANCE.md', T('SEO and performance', 'SEO 与性能') + en,
         T('The SEO output built into the core, hreflang, structured data, the performance budget.', '内置的 SEO 输出、hreflang、结构化数据、性能预算。')),
        (DOCS + 'SECURITY.md', T('Security', '安全') + en,
         T('Trust levels, credential handling, sanitisation — and what is deliberately not defended against.', '信任级别、凭据处理、内容净化——以及有意不防御的情形。')),
    ]
    project = [
        (GH + '/blob/main/' + T('CONTRIBUTING.md', 'CONTRIBUTING.zh-CN.md'), T('Contributing', '贡献指南'),
         T('How to set up the repository and what a change is held to.', '如何搭建开发环境，以及一次改动要满足的要求。')),
        (DOCS + 'TESTING.md', T('Testing', '测试') + en,
         T('Test layers, hard-contract checklist and the coverage gate.', '测试分层、硬性约定清单和覆盖率门槛。')),
        (DOCS + 'RELEASE_GATE.md', T('Release runbook', '发布手册') + en,
         T('How a release artifact is verified before it is published.', '发行包在发布前如何验证。')),
        (GH + '/blob/main/SECURITY.md', T('Security reporting', '安全报告') + en,
         T('How to report a vulnerability privately.', '如何私下报告安全漏洞。')),
    ]

    return f'''<section class="hero page-hero" aria-labelledby="page-title">
  <div class="wrap">
    {head("Docs", T("Start here", "从这里开始"))}
    <h1 id="page-title">{T("From an empty folder to a live site.", "从空目录到上线的网站。")}</h1>
    <p class="lede">{T(
      "The quick start below is the short version. The full documentation lives in the repository on GitHub, next to the code it describes; this page is the map.",
      "下面的快速上手是精简版。完整文档放在 GitHub 仓库里，和它描述的代码在一起；这一页是导览。")}</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn btn-primary" href="{gs}">{T("Full getting-started guide", "完整入门指南")}{EXT}</a>
      <a class="btn btn-ghost" href="{DOCS}{T("README.md", "zh-CN/README.md")}">{T("Documentation index", "文档导航")}{EXT}</a>
    </div>
  </div>
</section>

<section class="section" id="quick-start" aria-labelledby="qs-title">
  <div class="wrap">
    <div class="section-head">
      {head("01", T("Quick start", "快速上手"))}
      <h2 id="qs-title">{T("Five steps, one of them a command.", "五步，其中一步只是一条命令。")}</h2>
      <p>{T(
        "You need Node.js 22 or newer with npm, and a Cloudflare account with access to Workers, D1 and R2. The steps target the published 0.1.0-rc.10 candidate.",
        "需要 Node.js 22 或更新版本（含 npm），以及一个能使用 Workers、D1 和 R2 的 Cloudflare 账号。以下步骤针对已发布的 0.1.0-rc.10 候选版。")}</p>
    </div>
    <ol class="steps-list">
      <li>
        <h3>{T("Generate and check a project locally", "在本地生成并检查项目")}</h3>
        <p>{T("This installs dependencies, builds the project and checks the deployment configuration. It creates no cloud resources.", "这一步安装依赖、构建项目并检查部署配置，不会创建任何云资源。")}</p>
        <figure class="code" style="margin:0"><pre tabindex="0"><code>npx mallok create my-site --no-deploy
cd my-site</code></pre></figure>
      </li>
      <li>
        <h3>{T("Sign in to Cloudflare and deploy", "登录 Cloudflare 并部署")}</h3>
        <p>{T("Check that <code>whoami</code> shows the account you intend to use. Creation provisions a Worker, a D1 database and an R2 bucket in it. Add <code>--domain site.example.com</code> to bind a hostname you control from the first deployment.", "先确认 <code>whoami</code> 显示的是你要用的账号。创建过程会在该账号里开通一个 Worker、一个 D1 数据库和一个 R2 存储桶。想在首次部署时就绑定自己的域名，加上 <code>--domain site.example.com</code>。")}</p>
        <figure class="code" style="margin:0"><pre tabindex="0"><code>npx wrangler login
npx wrangler whoami
npx mallok create . --slug my-site</code></pre></figure>
        <p class="fine">{T("Already signed in and happy to do it in one go? <code>npx mallok create my-site</code> generates, verifies and deploys in a single command.", "已经登录，想一步到位？<code>npx mallok create my-site</code> 会一次完成生成、校验和部署。")}</p>
      </li>
      <li>
        <h3>{T("Finish setup in the browser", "在浏览器里完成初始化")}</h3>
        <p>{T("Open the setup URL the CLI prints and enter the one-time setup key. The wizard creates the administrator, sets the site name and languages, and offers example content — placeholders to replace before you present the site as your business.", "打开 CLI 输出的初始化地址，填入一次性的 setup key。向导会创建管理员、设置站点名称和语言，并可导入示例内容——示例只是占位，正式对外之前请替换成你自己的内容。")}</p>
      </li>
      <li>
        <h3>{T("Bind a custom domain", "绑定自定义域名")}</h3>
        <p>{T("Edge caching needs a custom domain; a <code>workers.dev</code> address is for preview only. For edits to appear promptly, also add a cache-purge token (<strong>Zone → Cache Purge → Purge</strong>) and the zone id as Worker secrets. Without them, visitors see the previous version until the cache expires.", "边缘缓存需要自定义域名；<code>workers.dev</code> 地址只用于预览。想让修改及时生效，还要把清缓存令牌（<strong>Zone → Cache Purge → Purge</strong>）和 zone id 配成 Worker secrets。没有它们，访客要等缓存过期才能看到新内容。")}</p>
      </li>
      <li>
        <h3>{T("Publish", "发布内容")}</h3>
        <p>{T("In the admin at <code>/_mallok/app</code>, edit a starter product or create your own, then publish. No rebuild. From a terminal or CI, publish a folder of bundles with a scoped API token instead:", "在 <code>/_mallok/app</code> 后台修改示例产品或新建内容，然后发布，不需要重新构建。也可以在终端或 CI 里，用分权限的 API 令牌直接发布整个内容包目录：")}</p>
        <figure class="code" style="margin:0"><pre tabindex="0"><code>npx mallok publish ./content</code></pre></figure>
      </li>
    </ol>
    <div class="callout" style="margin-top:1.25rem">
      <p><strong>{T("Before you rely on it:", "正式依赖之前：")}</strong> {T(
        "this is a release candidate. There is no “Deploy to Cloudflare” button yet, and real inquiry email delivery has not been accepted end to end.",
        "目前是候选版。还没有“Deploy to Cloudflare”按钮，真实询盘邮件送达也尚未完成端到端验收。")}
        <a href="{rs}">{T("Read the release status", "查看发布状态")}</a></p>
    </div>
  </div>
</section>

<section class="section tinted" aria-labelledby="map-title">
  <div class="wrap">
    <div class="section-head">
      {head("02", T("The map", "文档导览"))}
      <h2 id="map-title">{T("Where to read next.", "接下来读什么。")}</h2>
      <p>{T(
        "Every link below opens the document on GitHub. English is the primary documentation language; a Chinese translation exists for getting started and release status.",
        "下面的链接都会打开 GitHub 上的文档。英文是主要文档语言；入门指南和发布状态有中文翻译，其余技术参考暂为英文。")}</p>
    </div>
    <div class="grid" style="gap:2.5rem">
      <div class="doc-group"><h3>{T("Start here", "从这里开始")}</h3>{doc_list(start)}</div>
      <div class="doc-group"><h3>{T("Understand the design", "理解设计")}</h3>{doc_list(design)}</div>
      <div class="doc-group"><h3>{T("Build on Mallok", "基于 Mallok 开发")}</h3>{doc_list(build_on)}</div>
      <div class="doc-group"><h3>{T("Take part", "参与项目")}</h3>{doc_list(project)}</div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="else-title">
  <div class="wrap">
    <div class="section-head">
      {head("03", T("Elsewhere", "其他入口"))}
      <h2 id="else-title">{T("See it, read it, install it.", "看效果，读源码，装起来。")}</h2>
    </div>
    <div class="grid cols-3">
      <article class="card"><h3>{T("Live demo", "在线演示")}</h3><p>{T("A read-only Atelier site. The sample company and content are fictional; the admin and inquiry collection are not enabled there.", "只读的 Atelier 站点。示例企业与内容均为虚构；演示站不开放后台，也不收集询盘。")}</p><p><a class="link-arrow" href="{DEMO}">demo.mallok.dev</a></p></article>
      <article class="card"><h3>GitHub</h3><p>{T("Source, issues, changelog and the documentation itself, under Apache-2.0.", "源码、issue、更新日志和文档本身，采用 Apache-2.0 许可。")}</p><p><a class="link-arrow" href="{GH}">fobstack/mallok</a></p></article>
      <article class="card"><h3>npm</h3><p>{T("One package, <code>mallok</code>. <code>latest</code> is 0.1.0-rc.10; <code>next</code> is 0.1.0-rc.11.", "只有一个包：<code>mallok</code>。<code>latest</code> 是 0.1.0-rc.10，<code>next</code> 是 0.1.0-rc.11。")}</p><p><a class="link-arrow" href="{NPM}">npmjs.com/package/mallok</a></p></article>
    </div>
  </div>
</section>'''
