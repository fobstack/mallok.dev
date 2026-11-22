"""Cost page: the Cloudflare cost ladder (PRODUCT_VISION §7)."""

from layout import DOCS, T, head


def ladder_table():
    rows = [
        (T('Rendering, admin, API', '渲染、后台、API'), 'Workers',
         T('100k requests/day, 10 ms CPU each; a script up to 64 MiB uncompressed', '每天 10 万次请求，每次 10 ms CPU；脚本未压缩上限 64 MiB'),
         T('Workers Paid at $5/month: 10M requests, 30M CPU-ms, 30 s CPU by default; the same 64 MiB script limit', 'Workers Paid 每月 5 美元：1000 万次请求、3000 万 CPU 毫秒，默认单次 30 秒 CPU；脚本上限同为 64 MiB')),
        (T('Content, inquiries', '内容、询盘'), 'D1',
         T('5 GB total, 5M rows read/day, 100k rows written/day; exceeding it makes D1 unavailable for the day', '总计 5 GB，每天读 500 万行、写 10 万行；超出后当天不可用'),
         T('With Paid: 25B rows read/month, 50M written/month, $0.75/GB past 5 GB', '开通 Paid 后：每月读 250 亿行、写 5000 万行，超过 5 GB 部分每 GB 0.75 美元')),
        (T('Images, attachments', '图片、附件'), 'R2',
         T('10 GB-month, 1M writes and 10M reads/month, egress free', '10 GB·月，每月 100 万次写、1000 万次读，出站流量免费'),
         T('$0.015/GB-month', '每 GB·月 0.015 美元')),
        (T('The admin app', '后台应用'), 'Workers Static Assets',
         T('Unlimited free requests, 20k files, 25 MiB each', '请求免费且不限量，2 万个文件，单个 25 MiB'),
         T('With Paid, up to 100k files', '开通 Paid 后最多 10 万个文件')),
        (T('Page caching and purging', '页面缓存与清除'), 'Cache API + Purge API',
         T('Free; ample single-file purge quota, 5 tag/host/everything purges per minute', '免费；单文件清除额度充足，按标签/主机/全站清除每分钟 5 次'),
         T('Higher on Pro and Business', 'Pro 与 Business 套餐更高')),
        (T('Scheduled publishing, email retries', '定时发布、邮件重试'), 'Cron Triggers',
         T('<strong>5 per account</strong>', '<strong>每个账号 5 个</strong>'),
         T('250 with Paid', '开通 Paid 后 250 个')),
        (T('Form abuse protection', '表单防刷'), 'Turnstile',
         T('Free, 20 widgets, 10 hostnames each', '免费，20 个组件，每个 10 个主机名'),
         'Enterprise'),
        (T('Domain and DNS', '域名与 DNS'), 'Registrar + DNS',
         T('Domains at cost, DNS free', '域名按成本价，DNS 免费'), '—'),
        (T('Visitor analytics', '访客统计'), T('Cloudflare site analytics', 'Cloudflare 站点分析'),
         T('Free', '免费'), '—'),
        (T('Sending email', '发送邮件'), 'Resend',
         T('3,000/month, 100/day, 3 domains', '每月 3000 封，每天 100 封，3 个域名'),
         T('Pro at $20/month for 50,000', 'Pro 每月 20 美元，5 万封')),
    ]
    body = ''.join(
        f'<tr><th scope="row">{a}<small>{b}</small></th><td>{c}</td><td>{d}</td></tr>'
        for a, b, c, d in rows)
    return f'''<div class="table-wrap" tabindex="0" role="region" aria-labelledby="ladder-caption">
<table class="data">
<caption id="ladder-caption">{T(
  "Figures from Cloudflare's and Resend's official documentation, checked 2026-08-28. They may have changed since; confirm against the providers' current pricing pages before you rely on them.",
  "数据来自 Cloudflare 与 Resend 官方文档，核对日期为 2026-08-28。之后可能有变化，使用前请以服务商当前的定价页面为准。")}</caption>
<thead><tr><th scope="col">{T("Purpose · product", "用途 · 产品")}</th><th scope="col">{T("Free tier", "免费额度")}</th><th scope="col">{T("Beyond it", "超出之后")}</th></tr></thead>
<tbody>{body}</tbody>
</table></div>'''


def build():
    return f'''<section class="hero page-hero" aria-labelledby="page-title">
  <div class="wrap">
    {head("Cost", T("The Cloudflare cost ladder", "Cloudflare 成本阶梯"))}
    <h1 id="page-title">{T("Start on the free allowances. One paid step, and it changes nothing else.", "从免费额度起步。只有一级付费台阶，而且别的都不用改。")}</h1>
    <p class="lede">{T(
      "Mallok itself is free and open source, and it hosts nothing: what you pay, you pay to Cloudflare (and to Resend if you send email) from your own accounts. Mallok is designed to start on Cloudflare's free allowances. That is a design target — not a promise of unlimited free service.",
      "Mallok 本身免费、开源，也不托管任何东西：所有费用都由你自己的账号直接付给 Cloudflare（如果发邮件，还有 Resend）。Mallok 以 Cloudflare 免费额度起步为设计目标——这是设计目标，不是无限免费的承诺。")}</p>
  </div>
</section>

<section class="section" aria-labelledby="steps-title">
  <div class="wrap">
    <div class="section-head">
      {head("01", T("The two rungs", "两级台阶"))}
      <h2 id="steps-title">{T("Free at first; $5 a month per account when there is volume.", "先免费；有量之后，每个账号每月 5 美元。")}</h2>
      <p>{T(
        "Every Cloudflare product Mallok depends on has a free tier. The one paid step is Workers Paid. It raises limits on the same Worker, the same D1 database and the same R2 bucket — no migration, no architecture change.",
        "Mallok 依赖的每一项 Cloudflare 产品都有免费额度。唯一的付费台阶是 Workers Paid：它只是提高同一个 Worker、同一个 D1 数据库、同一个 R2 存储桶的上限——不迁移数据，也不改架构。")}</p>
    </div>
    <div class="ladder">
      <div class="rung">
        <span class="tag tag-live">{T("STEP 0", "第 0 级")}</span>
        <span class="price">$0<small> {T("to Cloudflare", "付给 Cloudflare")}</small></span>
        <h3>{T("Free allowances", "免费额度")}</h3>
        <p>{T(
          "100k Worker requests a day at 10 ms CPU each, 5 GB of D1, 10 GB of R2, free caching and purging, five cron triggers per account, Turnstile and DNS. You still need a domain, which is not free.",
          "每天 10 万次 Worker 请求（每次 10 ms CPU）、5 GB D1、10 GB R2、免费的缓存与清除、每账号 5 个定时触发器、Turnstile 和 DNS。域名仍然需要，而域名不是免费的。")}</p>
      </div>
      <div class="rung rung-paid">
        <span class="tag tag-accent">{T("STEP 1", "第 1 级")}</span>
        <span class="price">$5<small> {T("/ month / account", "/ 月 / 账号")}</small></span>
        <h3>Workers Paid</h3>
        <p>{T(
          "10M requests and 30M CPU-milliseconds a month, 30 s of CPU per invocation by default, far higher D1 limits and 250 cron triggers. Charged per Cloudflare account, so it covers every site in that account. Usage beyond the included amounts is billed by Cloudflare.",
          "每月 1000 万次请求、3000 万 CPU 毫秒，单次调用默认 30 秒 CPU，D1 上限大幅提高，定时触发器增至 250 个。按 Cloudflare 账号计费，账号下的所有站点共用。超出包含额度的用量由 Cloudflare 另行计费。")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section tinted" aria-labelledby="table-title">
  <div class="wrap">
    <div class="section-head">
      {head("02", T("The ladder, line by line", "逐项明细"))}
      <h2 id="table-title">{T("What each dependency gives you free, and what comes after.", "每项依赖免费给多少，之后怎么算。")}</h2>
    </div>
    {ladder_table()}
    <p class="fine" style="margin-top:.9rem">{T(
      'Source: <a href="' + DOCS + 'PRODUCT_VISION.md">product vision</a>, section 7, and <a href="' + DOCS + 'CLOUDFLARE_RESOURCES.md">Cloudflare resources</a>. Mallok is not affiliated with Cloudflare or Resend and does not set these prices.',
      '来源：<a href="' + DOCS + 'PRODUCT_VISION.md">产品愿景（英文）</a>第 7 节与 <a href="' + DOCS + 'CLOUDFLARE_RESOURCES.md">Cloudflare 资源说明（英文）</a>。Mallok 与 Cloudflare、Resend 没有隶属关系，这些价格也不由 Mallok 决定。')}</p>
  </div>
</section>

<section class="section" aria-labelledby="limits-title">
  <div class="wrap">
    <div class="section-head">
      {head("03", T("Limits that shape the product", "影响产品设计的几条限制"))}
      <h2 id="limits-title">{T("The free tier has edges. Here is where they are.", "免费额度有边界，位置在这里。")}</h2>
    </div>
    <div class="grid cols-2">
      <div class="callout">
        <h3>{T("Five cron triggers per account", "每个账号 5 个定时触发器")}</h3>
        <p>{T(
          "Each Mallok site uses one cron trigger for scheduled publishing and email retries. One free Cloudflare account therefore carries scheduled work for at most five sites; a larger portfolio needs Workers Paid.",
          "每个 Mallok 站点用一个定时触发器来处理定时发布和邮件重试。所以一个免费 Cloudflare 账号最多支撑 5 个站点的定时任务；站点更多就需要 Workers Paid。")}</p>
      </div>
      <div class="callout">
        <h3>{T("D1's daily cap is a hard stop", "D1 的每日上限是硬限制")}</h3>
        <p>{T(
          "Exceeding D1's free daily rows makes the database unavailable for the rest of that day, and with it everything that needs D1: cold renders, saves and inquiries. Watch usage as a site grows.",
          "超过 D1 免费的每日行数后，数据库当天剩余时间都不可用，所有依赖 D1 的事情——冷渲染、保存、询盘——也随之停摆。站点长大后要留意用量。")}</p>
      </div>
      <div class="callout">
        <h3>{T("10 ms of CPU on the free plan", "免费套餐的 10 ms CPU")}</h3>
        <p>{T(
          "Cache hits measured 0–1 ms of CPU on rc.5. Cold renders measured p50 11 ms and p95 35 ms, above the 10 ms target in 16 of 30 samples; none failed in that sample. This is the release candidates' known limitation, and those rc.5 figures do not certify later candidates.",
          "rc.5 实测缓存命中为 0–1 ms CPU；冷渲染 p50 为 11 ms、p95 为 35 ms，30 个样本里有 16 个超过 10 ms 目标，该样本中没有请求失败。这是候选版的已知限制，而且 rc.5 的数据不能代表之后的候选版。")}
          <a href="{DOCS}{T("RELEASE_STATUS.md", "zh-CN/RELEASE_STATUS.md")}">{T("Release status", "发布状态")}</a></p>
      </div>
      <div class="callout info">
        <h3>{T("A custom domain is required for caching", "缓存需要自定义域名")}</h3>
        <p>{T(
          "Edge caching — the thing that keeps nearly every request off the Worker's CPU budget — works on a custom domain. A <code>workers.dev</code> address is for preview only. Budget for a domain; Cloudflare Registrar sells them at cost.",
          "边缘缓存——也就是让绝大多数请求不占用 Worker CPU 额度的关键——需要自定义域名才能工作。<code>workers.dev</code> 地址只用于预览。请把域名算进预算；Cloudflare Registrar 按成本价出售域名。")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section tinted" aria-labelledby="unused-title">
  <div class="wrap">
    <div class="feature">
      <div>
        {head("04", T("Deliberately unused", "有意不用的服务"))}
        <h2 id="unused-title">{T("What Mallok leaves out to keep the ladder short.", "为了让台阶少一些，Mallok 不用这些。")}</h2>
        <p class="lede">{T(
          "A dependency with a tight free tier or no free tier would add a second paid step. So the Worker uses D1, R2, Static Assets, the Cache API and one cron trigger — and nothing else.",
          "免费额度太紧或没有免费额度的依赖，都会多出一级付费台阶。所以 Worker 只用 D1、R2、Static Assets、Cache API 和一个定时触发器，别的都不用。")}</p>
      </div>
      <div class="mini">
        <div class="mini-row"><span>Workers KV</span><span>{T("1,000 writes a day on the free tier", "免费额度每天只有 1000 次写入")}</span></div>
        <div class="mini-row"><span>Cloudflare Images</span><span>{T("paid — images are resized in the browser instead", "付费——改为在浏览器里处理图片")}</span></div>
        <div class="mini-row"><span>Email Workers send</span><span>{T("Paid-only, verified addresses only", "仅 Paid 可用，且只能发到已验证地址")}</span></div>
        <div class="mini-row"><span>Queues</span><span>{T("not needed — cron covers email retries", "不需要——定时任务已覆盖邮件重试")}</span></div>
        <div class="mini-row"><span>Durable Objects</span><span>{T("not used", "不使用")}</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="notfree-title">
  <div class="wrap">
    <div class="section-head">
      {head("05", T("What is not free", "哪些不免费"))}
      <h2 id="notfree-title">{T("The honest total.", "把账算清楚。")}</h2>
    </div>
    <div class="grid cols-3">
      <article class="card"><h3>{T("Your domain", "域名")}</h3><p>{T("Needed for caching and for a credible company site. Priced by your registrar.", "缓存需要它，一个像样的企业官网也需要它。价格由注册商决定。")}</p></article>
      <article class="card"><h3>{T("Email at volume", "大量邮件")}</h3><p>{T("Inquiry email goes through Resend. Its free tier covers 3,000 emails a month and 100 a day; beyond that is Resend's paid plan.", "询盘邮件通过 Resend 发送。免费额度每月 3000 封、每天 100 封，超出需要 Resend 的付费套餐。")}</p></article>
      <article class="card"><h3>{T("Your time", "你的时间")}</h3><p>{T("Setup needs someone comfortable with Node and a terminal. Themes, plugins and upgrades need a redeploy by that same person.", "安装需要一个会用 Node 和终端的人。主题、插件和升级的重新部署，也要这个人来做。")}</p></article>
    </div>
  </div>
</section>'''
