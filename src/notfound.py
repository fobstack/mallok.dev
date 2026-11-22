"""The 404 page. Served by Workers Static Assets for any missing path; the
nearest 404.html wins, so /zh-cn/... gets the Chinese one."""

from layout import ARROW, T, head, url

# A thread that comes loose: the ribbon M's stroke, ending in a dropped
# shuttle dot. Decorative only.
ART = '''<svg class="nf-art" viewBox="0 0 320 120" fill="none" aria-hidden="true" focusable="false">
  <defs><linearGradient id="nf-thread" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#A855F7"/><stop offset=".6" stop-color="#7E22CE"/>
    <stop offset="1" stop-color="#7E22CE" stop-opacity="0"/></linearGradient></defs>
  <path class="nf-line" d="M8 92 C 60 92, 70 24, 120 24 S 170 92, 214 70 S 250 40, 272 58"
        stroke="url(#nf-thread)" stroke-width="6" stroke-linecap="round"/>
  <circle class="nf-dot" cx="294" cy="98" r="9" fill="#2DD4BF"/>
</svg>'''


def build():
    links = ''.join(
        f'<li><a href="{url(href)}">{label}{ARROW}</a></li>'
        for href, label in (
            ('/features/', T('Features', '功能')),
            ('/themes/', T('Themes', '主题')),
            ('/cost/', T('Cost', '成本')),
            ('/docs/', T('Docs', '文档')),
        )
    )
    return f'''<section class="hero page-hero nf" aria-labelledby="page-title">
  <div class="wrap">
    {ART}
    {head("404", T("Page not found", "页面不存在"))}
    <h1 id="page-title">{T("This thread leads nowhere.", "这根线没有连到任何页面。")}</h1>
    <p class="lede">{T(
      "The address may be mistyped, or the page may have moved. Everything on this site is a few links from the home page.",
      "可能是网址输错了，也可能页面已经移走。本站的所有内容，从首页出发几步就能找到。")}</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn btn-primary" href="{url("/")}">{T("Back to the home page", "回到首页")}{ARROW}</a>
    </div>
    <ul class="nf-links">{links}</ul>
  </div>
</section>'''
