# mallok.dev prototype — notes

Static HTML/CSS plus one small script (see "Theme toggle and language menu" below), no external requests.
Serve with `python3 -m http.server 4400 --directory .tmp/website`.
Nothing was committed, pushed, deployed or published.

## Thread redesign (fourth round) — read this first

The site now uses the approved design board, "A · 引线 (final candidate)",
at `/design/` (`design/_build.py`; not touched in this round). Sections below
that describe the earlier look are kept for history; where they disagree
with this section, this section is current.

### What changed

- **Tokens** (`src/tokens.py`): values moved to the board's. New tokens:
  `--action` / `--action-deep` / `--action-ink` (primary button and thread
  lines: `#7E22CE` light, `#A855F7` with Midnight text dark), `--live-line`
  (teal graphics), `--code-bg` / `--code-ink` / `--code-key` / `--code-str` /
  `--code-dim` (code panels are light in light mode — no dark slabs),
  `--shadow-lg`. In dark, `--accent` (text links) is `#C99BFB`. The hero and
  CTA glows and the grid are gone. 38 text pairs are checked at build; all
  pass AA in both modes.
- **`assets/site.css`**: radius 20 / 12 px, pills for buttons, badge and
  command, 800-weight headings, and a new section 11, "Thread design system",
  that restyles the existing components and adds the home page's pieces
  (classes prefixed `m-`, the same names as on the board). 80 / 15 / 5:
  neutral / Kinetic Purple / Electric Teal; teal is only the shuttle dot,
  "live" tags, the content timeline and the cache-HIT thread. The frame
  timeline and MISS are purple now, not amber. Motion (dot pulse, the dot
  travelling the hero thread, hover lift) sits inside
  `prefers-reduced-motion: no-preference`.
- **Home** (`src/home.py`, rewritten): hero with the editor → thread → live
  page visual; capability strip with its footnote; three promises strung on a
  thread; two timelines with the twin threads; multilingual demo (radio
  inputs + labels, arrow keys switch, no script); request path as
  `<details>` nodes with free allowances; the rc.5 measurements and note
  (numbers and wording unchanged); themes; release status; quick start; a
  compact closing CTA (`layout.cta_compact`) so the command is not shown
  three times. The old "product page is a Markdown file" split, the bento
  and the cost teaser left the home page; their content is on Features and
  Cost.
- **Dense variant**: all `table.data` tables and the docs link lists are
  hairline (2 px ink rule on top, no card). Features draws the two timelines
  as parallel tracks (`home.boundary(dense=True)`).
- **Brand**: new "UI language" section (ratio bar, component samples, link
  to `/design/`); the Type section now describes Figtree.
- **Locale examples** use `zh-CN` everywhere: `index.zh-CN.md`,
  `/zh-CN/products/…`, `hreflang="zh-CN"`. The default language is
  unprefixed (`docs/SEO_PERFORMANCE.md` §4). The site's own Chinese pages
  stay under `/zh-cn/` with `hreflang="zh-CN"`.
- **Sample content** in the hero and the demo is taken from the repo's own
  `content/product/grade-5-titanium-bar/index.md` (shortened) and labelled
  as illustrative.
- `src/check.py` (new): lang, canonical, hreflang, OG, skip link, one `h1`,
  no `<script>`, duplicate ids, internal links and fragments, image and CSS
  file references. Run after `build.py`.

### Font: Figtree — NOT downloaded yet

Figtree is licensed under the SIL Open Font License 1.1. The stylesheet
names it first and the build writes `@font-face` rules **only for files that
exist** in `assets/fonts/`, so nothing 404s. The files are not there:
downloading them needs the user's own go-ahead, which I did not have. Until
then every page renders in the system sans stack and requests no font at
all (no Google Fonts request either).

To finish: `python3 src/fetch_fonts.py && python3 src/build.py`. That
fetches the variable woff2 (latin and latin-ext subsets) from Google Fonts
and `OFL.txt` from the google/fonts repository into `assets/fonts/`. The
script has not been run, so it is untested. After it runs, re-check the
hero at 375 px: Figtree is wider than the fallback.

### Cache-hit claim: verified, and reworded

The old copy said a cache hit does "no rendering, no database read". Traced
in the repo at HEAD:

- `src/runtime/cloudflare/index.ts` (`createPageHandler`): the cache lookup
  is the first thing the page handler does and a hit returns before locals,
  page code or the theme run. **"No rendering" is true.**
- `src/worker/handler.ts`: before the page handler, every non-`/media/`
  request awaits `boot(env)` (`src/worker/bootstrap.ts`). It is memoised per
  isolate, but the first request a new isolate handles runs the migration
  check, reads the site row and ensures plugin rows — several D1 round
  trips, even when the page is then served from cache.
- Same file: if any compiled-in plugin declares an `onRequest` hook,
  `runOnRequest` reads site data from D1 on every public request, before the
  cache lookup. No bundled plugin declares one (`src/plugins/`), so this
  only applies to custom plugins.

So the home page now says: "returned before any page code runs: no
rendering, and no database read on a warm Worker", and the node's detail
adds that a newly started Worker's first request runs a start-up check
against D1. The `onRequest` case is not mentioned on the site.

### Checks done this round

- `python3 src/build.py`: AA check green. `python3 src/check.py`: 12
  pages, 0 problems.
- Browser: all 12 pages at 1440 and 375, in light and dark — no horizontal
  overflow, no broken image (measured by script in iframes).
- Looked at: home (1440 light and dark, 375 light in Chinese), Features
  (Chinese, dark), Cost, Docs, Themes and Brand (1440 light). Other
  combinations were measured but not looked at.
- Keyboard: the EN / 中文 control and the `<details>` nodes were exercised
  on the board, which uses the same markup and CSS pattern; not re-tested on
  the site itself.

## Files

Pages (12: six pages × en / zh-CN):

| Page | English | Chinese |
| --- | --- | --- |
| Home | `index.html` | `zh-cn/index.html` |
| Features | `features/index.html` | `zh-cn/features/index.html` |
| Themes | `themes/index.html` | `zh-cn/themes/index.html` |
| Cost | `cost/index.html` | `zh-cn/cost/index.html` |
| Docs | `docs/index.html` | `zh-cn/docs/index.html` |
| Brand (footer link only) | `brand/index.html` | `zh-cn/brand/index.html` |

Assets:

- `assets/site.css` — the one stylesheet.
- `assets/atelier-desktop.jpg` — supplied screenshot (unchanged).
- `assets/brand/` — a copy of the user's brand kit
  (`logos/mallok-brand-kit/`: `svg/`, `png/`, `favicon/`, `social/`, `gif/`).
  The kit itself was not modified. One copied file was edited: the icon
  paths in `assets/brand/favicon/site.webmanifest`.
- My earlier logo concepts (`assets/logo/`, `assets/favicon.svg`,
  `src/logos.py`) are deleted.

Source (the HTML is generated so the 12 pages cannot drift apart):

- `src/build.py` — run `python3 src/build.py` to rebuild everything.
- `src/layout.py` (head, header, footer, CTA), `home.py`, `features.py`,
  `themes.py`, `cost.py`, `docs.py`, `brand.py` — one module per page; every
  string is `T(english, chinese)`.
- `src/tokens.py` — the colour system (single source; writes the token block
  in `site.css` and the contrast table on the Brand page; the build fails if a
  listed pair drops below AA).
- `src/art.py` — theme mockups and the rendering diagram (inline SVG).

Every page has: `lang`, canonical, `hreflang` en / zh-CN / x-default, a
language switcher to its counterpart, skip link, one `h1`, landmarks, OG tags.

## Checks done

- Structure: tag balance, one `h1`, no duplicate ids, all internal links and
  fragments resolve, all images have `alt` (script, all 12 pages).
- 375 px: `scrollWidth == 375` on all 12 pages (tables, the diagram and code
  scroll inside their own containers).
- Looked at in a browser at 1440 and 375, light and dark: home, themes (zh),
  features, cost (zh, mobile menu open), brand. Not every page was viewed in
  every combination. After the logo revision: Brand page re-viewed at 1440
  light, 375 px overflow and AA contrast re-run on all 12 pages; the new
  Brand sections were not viewed in dark or at 375.

## Brand kit applied (third round)

The user's kit, "The Kinetic Thread M", replaces my logo concepts and colour
system entirely. The site is now light-first.

- **Logo**: header and footer use `svg/logo/mallok-logo-color-light.svg`,
  swapped to `…-color-dark.svg` by `<picture>` + `prefers-color-scheme` (no
  JS). Rendered 32 px tall = 116 px wide (kit minimum 96 px). No tile.
- **Head**: the kit's favicon snippet with paths under
  `/assets/brand/favicon/`; `theme-color` `#FBFAFC` (light) and `#0D0B14`
  (dark); `og:image` → `social/og-image.png`.
- **Brand page**: concept story (README, en + zh), logo / mark / wordmark
  variants with SVG and PNG downloads, favicon set and share image, usage
  rules from the README, kit colours with contrast, derived scales, semantic
  tokens, contrast table, type. The three-concept chooser and the
  "personality idea" section are gone.
- **Page impression**: Cloud White page, white cards, soft purple/teal glow
  in the hero and closing CTA. The closing CTA was a dark slab and is now
  light. Code blocks and the hero's small response-headers card stay dark.

### Colour tokens (`src/tokens.py` → `:root` in `site.css`)

- Kit colours verbatim: `--mallok-purple` `#7E22CE`, `--mallok-purple-light`
  `#A855F7`, `--mallok-purple-deep` `#581C87`, `--mallok-teal` `#06B6D4`,
  `--mallok-teal-bright` `#2DD4BF`, `--mallok-teal-lightbg` `#0D9488`,
  `--mallok-midnight` `#0D0B14`, `--mallok-cosmic` `#1E1B4B`,
  `--mallok-cloud` `#FBFAFC`, plus `--mallok-gradient-thread` / `-shuttle`.
- Derived scales: `--purple-50…900` (700 = Kinetic Purple, 500 = highlight,
  900 = fold), `--teal-50…900` (400 = Mint Glow, 600 = the kit's light-bg
  teal), `--neutral-0…950` (violet-tinted; 50 = Cloud White, 900 = the kit's
  dark surface `#161326`, 950 = Midnight), `--green-*`, `--amber-*`, `--red-*`.
- Semantic, light → dark: `--paper` `#fbfafc` → `#0d0b14`; `--paper-2`
  `#f4f2f7` → `#131022`; `--surface` `#ffffff` → `#161326`; `--ink` `#0d0b14`
  → `#fbfafc`; `--ink-2`, `--muted`, `--faint`, `--line`, `--line-strong`;
  `--accent` `#7e22ce` → `#a855f7` (text on it: white → Midnight);
  `--accent-deep`, `--accent-tint`; `--live` `#0f766e` → `#2dd4bf` (teal, the
  "live immediately" / cache HIT colour) and `--live-tint`; `--success`
  (green), `--warning` (amber, "needs redeploy" / MISS), `--danger`, `--info`
  and their tints.
- Dark is emitted twice: `@media (prefers-color-scheme: dark)` on
  `:root:not([data-theme="light"])`, and `[data-theme="dark"]` for
  compatibility with the kit's tokens. `[data-theme="light"]` forces light.
- All 27 listed text/background pairs pass AA in both modes; the build fails
  otherwise. Lowest: light `--success` on its tint 4.57, dark `--accent` on
  `--surface` 4.59.
- Removed: ember accent, the navy/titanium neutrals, `--logo-accent`.
- Hard-coded colours that remain on purpose: the four theme mockups and the
  Atelier product-page illustration use those *themes'* own palettes (Atelier
  is blue).
- Type: `--sans` now starts `Inter, "Noto Sans", …system`, `--mono` starts
  `"JetBrains Mono", ui-monospace, …`. No web fonts are requested.

### What in the kit could not be used as-is

1. **`#0D9488` as text on light** — the kit recommends it for light
   backgrounds, but it is 3.7:1 on white (AA needs 4.5:1). The site uses
   teal-700 `#0f766e` (5.5:1) for teal text; `#0D9488` is kept as a token
   and documented as "large text and graphics only".
2. **`#A855F7` as a button colour in dark mode** — white text on it is below
   AA, so dark-mode primary buttons use Midnight text on `#A855F7`.
3. **`site.webmanifest`** — icon paths are root-absolute; edited in the copy
   only. The pages use per-scheme `theme-color` metas instead of the
   snippet's single dark one.
4. **`--border-subtle: #1E1B4B` (Cosmic) in dark** — as a hairline on
   Midnight it reads strongly blue; dark hairlines use `#262245`.
5. **Logo swap and `[data-theme]`** — the `<picture>` swap follows the system
   scheme only; forcing `data-theme="dark"` changes colours but not the logo
   file. Needs two images toggled by CSS if a manual switch is ever added.
6. **GIFs** — linked from the Brand page, not embedded, so no page animates
   on its own. `safari-pinned-tab.svg`, `mstile` and the manifest are linked
   but not tested in those browsers.
7. **Kit version** — README says v0.2, `brand-tokens.css/json` say v0.1; the
   Brand page shows v0.2.
8. The README recommends the dark logo on a dark hero as the main
   presentation; per the brief the site is light-first, so light is default.

Checked after this round: AA build check green; no overflow at 375 px and no
broken images on all 12 pages (script, with lazy images forced to load);
viewed home (light and dark, 1440) and Brand (zh, light, 1440). Other pages
were not re-viewed individually after the recolour.

## Astro patterns

Adopted: slim top nav with GitHub icon; version badge in the hero (linking to
release status); one-line value proposition + one sentence + primary button +
the `npx` command; three pillars under "What is Mallok?"; a data-backed
performance block (rc.5 numbers only, labelled); code beside its rendered
result (`index.md` beside a product page); bento feature grid with small
inline illustrations; theme gallery; closing CTA repeating the command; docs
entry points; rich footer.

Adapted: the logo wall became a four-fact strip (licence, what runs, themes,
no Mallok account). The copy button became a select-on-click command
(`user-select: all`), because a copy button needs JavaScript.

Skipped: customer logos, testimonials, stars/download counts, sponsors,
partner/agency band (Mallok has none and none were invented); a blog and
community links (do not exist); theme-gallery category tabs (five themes do
not need them); Astro's look, gradient and wording.

## Copy claims I was unsure about

1. **"Round-trip fidelity is covered by tests"** (Features → Content). Tests
   mentioning round trips exist (`test/core/bundle.test.ts`,
   `frontmatter.test.ts`); I did not read them to confirm they cover a full
   export → import. The home pillar says "designed to re-import
   byte-identically" and both note the second-deployment restore is open.
2. **"No rendering, no database read" on a cache hit** (home flow). Based on
   `src/runtime/cloudflare/index.ts` returning before the page runs and on
   ARCHITECTURE §4; I did not trace whether the Worker entry touches D1
   before the page handler.
3. **Purge-failure wording** (Features → Rendering): says failed purges are
   recorded on `main` but released candidates up to rc.11 can report success.
   Taken from RELEASE_STATUS; correct it when a release ships the fix.
4. **"Live immediately"** is qualified everywhere with "needs a custom domain
   and a cache-purge token". ARCHITECTURE cites a ≈20 s purge round trip and
   "within a minute"; the site does not quote a latency figure.
5. **Workers Paid "covers every site in that account" and "usage beyond the
   included amounts is billed by Cloudflare"** (Cost) — my reading of "$5 per
   account", not a sentence from the docs. The table itself is §7 verbatim.
6. **D1 daily cap**: I state that cold renders, saves and inquiries stop;
   I do not claim cached pages keep being served.
7. **Atelier carousel "about 4 KB"** — from `theme.json` (4,010 bytes) in the
   repo at HEAD, not necessarily the rc.10 package.
8. **Theme "light and dark; English and Chinese language packs"** — from each
   theme's CSS and `locales` at HEAD.
9. **Admin "English and Simplified Chinese"** and **"inquiries read like an
   inbox"** — from CLAUDE.md and recent commits on `main`; may be newer than
   rc.10.
10. **Roadmap** omits the 0.2 revision-history UI, 0.3 CRM webhooks and the
    1.0 storefront plugin to match the brief's list; "Excel" was dropped from
    product import for the same reason.
11. **Quick start** shows the guide's two-step path (`--no-deploy`, then
    `create . --slug`) and mentions the one-command form; `npx mallok publish
    ./content` is shown without its `--site`/token arguments.
12. The footer disclaimer ("not affiliated with Cloudflare, Resend, WordPress
    or Ghost") is my addition.
13. The home product sample (Grade 5 titanium bar, ASTM B348, MOQ, lead time)
    is invented sample content and is labelled as such.

## Known rough edges

- Chinese headings use `text-wrap: balance`; a few break mid-phrase at 375 px.
- The Brand page's type specimen depends on installed fonts (Inter and
  JetBrains Mono are not downloaded).
- Theme mockups are drawn with system fonts, not the themes' own typefaces.
- The four non-Atelier themes have no real screenshots; replace the
  illustrations when screenshots exist.

## Theme toggle and language menu (2026-11-22)

- Dark is the default: every page ships `<html data-theme="dark">`; tokens
  key only on `[data-theme]` (no `prefers-color-scheme` anymore).
- A pre-paint inline snippet in `<head>` applies a stored choice
  (`localStorage['mallok-theme']`) so light never flashes dark.
- `assets/site.js` (deferred): the sun/moon toggle with a circular reveal
  from the button (View Transitions API), a colour cross-fade where that API
  is missing, and no animation under `prefers-reduced-motion`. It also closes
  header menus on outside click / Escape and keeps one open at a time.
- The language switch is a `<details>` dropdown (globe, current language,
  chevron; list with a check on the current one). Without JS it still works.
- The logo swap is two `<img>` toggled by `[data-theme]` instead of
  `<picture>`, which could only follow the system setting.
- `check.py` now allows exactly the inline theme snippet and `/assets/site.js`.
- This marketing site's script is separate from Mallok's own rule that visitor
  pages of Mallok sites ship no client JS; the site's copy does not claim the
  marketing site itself is JS-free.
