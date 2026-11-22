"""Mallok's colour system, derived from the brand kit
(logos/mallok-brand-kit, "The Kinetic Thread M").

Single source for the token block in site.css and for the Brand page.
Light is the primary design; dark maps onto the kit's Midnight / Cosmic.
"""

# ---- Kit colours, verbatim ----
KIT = [
    ('Kinetic Purple', '交织紫', '#7E22CE', '--mallok-purple', 'Primary brand: the ribbon, primary buttons, links'),
    ('Ribbon Highlight', '高光紫', '#A855F7', '--mallok-purple-light', 'Brand colour on dark backgrounds'),
    ('Ribbon Fold', '折影紫', '#581C87', '--mallok-purple-deep', 'Gradient end, pressed states'),
    ('Electric Teal', '穿梭青', '#06B6D4', '--mallok-teal', 'The shuttle dot. Graphics only, not text'),
    ('Mint Glow', '穿梭亮青', '#2DD4BF', '--mallok-teal-bright', 'Story accent on dark backgrounds'),
    ('Teal for light backgrounds', '浅底青', '#0D9488', '--mallok-teal-lightbg', 'Large text and graphics on light (3.7:1 on white)'),
    ('Midnight Deep', '暗夜深', '#0D0B14', '--mallok-midnight', 'Ink on light; page background on dark'),
    ('Cosmic Blue', '深邃蓝', '#1E1B4B', '--mallok-cosmic', 'Dark borders and glow'),
    ('Cloud White', '云端白', '#FBFAFC', '--mallok-cloud', 'Page background on light; ink on dark'),
]

# ---- Primitive scales (do not change with the colour scheme) ----
PURPLE = {
    '50': '#faf5ff', '100': '#f3e8ff', '200': '#e9d5ff', '300': '#d8b4fe',
    '400': '#c084fc', '500': '#a855f7', '600': '#9333ea', '700': '#7e22ce',
    '800': '#6b21a8', '900': '#581c87',
}
TEAL = {
    '50': '#f0fdfa', '100': '#ccfbf1', '200': '#99f6e4', '300': '#5eead4',
    '400': '#2dd4bf', '500': '#14b8a6', '600': '#0d9488', '700': '#0f766e',
    '800': '#115e59', '900': '#134e4a',
}
# Violet-tinted greys that run from Cloud White to Midnight.
NEUTRAL = {
    '0': '#ffffff', '50': '#fbfafc', '100': '#f4f2f7', '200': '#e8e5ee',
    '300': '#d3cfdc', '400': '#a8a3b6', '500': '#777189', '600': '#5a546c',
    '700': '#403b52', '800': '#29253a', '900': '#161326', '950': '#0d0b14',
}
GREEN = {'100': '#dcfce7', '400': '#4ade80', '700': '#15803d', '900': '#0f2a1b'}
AMBER = {'100': '#fef3c7', '400': '#fbbf24', '800': '#92400e', '900': '#33260f'}
RED = {'100': '#fee2e2', '300': '#fca5a5', '700': '#b91c1c', '900': '#3b1614'}

# ---- Semantic mapping: token -> (light, dark, note) ----
SEMANTIC = [
    ('paper', NEUTRAL['50'], NEUTRAL['950'], 'Page background (Cloud White / Midnight)'),
    ('paper-2', '#f6f3fa', '#14111c', 'Tinted section'),
    ('surface', NEUTRAL['0'], '#17141f', 'Cards, raised surfaces'),
    ('ink', NEUTRAL['950'], NEUTRAL['50'], 'Headings, primary text'),
    ('ink-2', NEUTRAL['800'], '#d9d5e3', 'Body text on surfaces'),
    ('muted', '#55506b', '#b4aec6', 'Secondary text'),
    ('faint', '#686279', '#9d97b2', 'Labels, captions'),
    ('line', '#e6e0f0', '#2a2538', 'Hairlines'),
    ('line-strong', '#c9c4d4', '#3d3650', 'Control borders'),
    ('accent', PURPLE['700'], '#c99bfb', 'Links, numerals, purple text'),
    ('accent-ink', NEUTRAL['0'], NEUTRAL['950'], 'Text on accent'),
    ('accent-deep', PURPLE['800'], PURPLE['300'], 'Hover / pressed link'),
    ('accent-tint', '#f4eefc', '#211a33', 'Lavender wash: badges, table heads, callouts'),
    ('action', PURPLE['700'], PURPLE['500'], 'Primary button, thread lines (Kinetic Purple / Ribbon Highlight)'),
    ('action-deep', PURPLE['800'], PURPLE['400'], 'Primary button, hover'),
    ('action-ink', NEUTRAL['0'], NEUTRAL['950'], 'Text on the primary button'),
    ('live', TEAL['700'], TEAL['400'], 'Story accent text: live, instant, cache HIT'),
    ('live-line', TEAL['600'], TEAL['400'], 'Teal lines and stops (graphics, 3:1)'),
    ('live-tint', '#e6faf6', '#0e2527', 'Live background'),
    ('code-bg', '#f6f2fc', '#14111c', 'Code panel background'),
    ('code-ink', NEUTRAL['950'], NEUTRAL['50'], 'Code text'),
    ('code-key', PURPLE['700'], '#c99bfb', 'Code keys'),
    ('code-str', TEAL['700'], TEAL['300'], 'Code strings'),
    ('code-dim', '#5f5a75', '#9d97b2', 'Code comments, prompts'),
    ('success', GREEN['700'], GREEN['400'], 'Positive'),
    ('success-tint', GREEN['100'], GREEN['900'], 'Success background'),
    ('warning', AMBER['800'], AMBER['400'], 'Cache MISS, caution'),
    ('warning-tint', AMBER['100'], AMBER['900'], 'Warning background'),
    ('danger', RED['700'], RED['300'], 'Errors, destructive'),
    ('danger-tint', RED['100'], RED['900'], 'Danger background'),
    ('info', PURPLE['700'], '#c99bfb', 'Informational (same as accent)'),
    ('info-tint', '#f4eefc', '#211a33', 'Info background'),
]

# Component tokens that also change with the scheme (not text pairs).
COMPONENT = [
    ('code-line', '#e6e0f0', '#2a2538'),
    ('ribbon-back-1', '#3b0764', '#4c1d95'),
    ('ribbon-back-2', '#6b21a8', '#7e22ce'),
    ('shadow', '0 1px 2px rgba(88, 28, 135, 0.06), 0 14px 32px -18px rgba(88, 28, 135, 0.28)',
     '0 1px 0 rgba(255, 255, 255, 0.04) inset, 0 14px 32px -18px rgba(0, 0, 0, 0.7)'),
    ('shadow-lg', '0 2px 4px rgba(88, 28, 135, 0.06), 0 28px 56px -24px rgba(88, 28, 135, 0.35)',
     '0 1px 0 rgba(255, 255, 255, 0.05) inset, 0 28px 56px -24px rgba(0, 0, 0, 0.8)'),
]

# Text/background pairs used on the site; all must pass AA (4.5:1).
PAIRS = [
    ('ink', 'paper'), ('ink', 'surface'), ('ink-2', 'surface'), ('ink-2', 'paper-2'),
    ('ink', 'accent-tint'), ('ink', 'live-tint'), ('ink-2', 'accent-tint'),
    ('muted', 'paper'), ('muted', 'surface'), ('muted', 'paper-2'), ('muted', 'accent-tint'),
    ('faint', 'paper'), ('faint', 'surface'), ('faint', 'paper-2'),
    ('accent', 'paper'), ('accent', 'surface'), ('accent', 'paper-2'),
    ('accent-ink', 'accent'), ('accent', 'accent-tint'),
    ('action-ink', 'action'), ('action-ink', 'action-deep'),
    ('live', 'paper'), ('live', 'surface'), ('live', 'paper-2'), ('live', 'live-tint'),
    ('code-ink', 'code-bg'), ('code-key', 'code-bg'), ('code-str', 'code-bg'),
    ('code-dim', 'code-bg'), ('muted', 'code-bg'),
    ('success', 'surface'), ('success', 'success-tint'),
    ('warning', 'surface'), ('warning', 'warning-tint'),
    ('danger', 'surface'), ('danger', 'danger-tint'),
    ('info', 'info-tint'), ('paper', 'ink'),
]


def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexv):
    h = hexv.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a, b):
    """WCAG 2 contrast ratio between two hex colours."""
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def value(token, mode):
    for name, light, dark, _ in SEMANTIC:
        if name == token:
            return light if mode == 'light' else dark
    raise KeyError(token)


def check():
    """Returns the pairs that fail AA, as (mode, fg, bg, ratio)."""
    bad = []
    for mode in ('light', 'dark'):
        for fg, bg in PAIRS:
            r = contrast(value(fg, mode), value(bg, mode))
            if r < 4.5:
                bad.append((mode, fg, bg, round(r, 2)))
    return bad


def _dark(indent):
    lines = [f'{indent}--{name}: {dark};' for name, _, dark, _ in SEMANTIC]
    lines += [f'{indent}--{name}: {dark};' for name, _, dark in COMPONENT]
    return lines


def css():
    """The generated token block for site.css."""
    out = [':root {', '  color-scheme: light;', '', '  /* Brand kit colours, verbatim */']
    for _, _, hexv, var, _ in KIT:
        out.append(f'  {var}: {hexv};')
    out += [
        '  --mallok-gradient-thread: linear-gradient(135deg, #A855F7 0%, #7E22CE 55%, #581C87 100%);',
        '  --mallok-gradient-shuttle: linear-gradient(180deg, #5EEAD4 0%, #2DD4BF 48%, #06B6D4 100%);',
        '', '  /* Primitive scales */',
    ]
    for prefix, ramp in (('purple', PURPLE), ('teal', TEAL), ('neutral', NEUTRAL),
                         ('green', GREEN), ('amber', AMBER), ('red', RED)):
        for k, v in ramp.items():
            out.append(f'  --{prefix}-{k}: {v};')
    out += ['', '  /* Semantic, light (the primary design) */']
    for name, light, _, note in SEMANTIC:
        out.append(f'  --{name}: {light}; /* {note} */')
    for name, light, _ in COMPONENT:
        out.append(f'  --{name}: {light};')
    out += ['}', '', '/* Dark is the default: <html data-theme="dark"> ships in',
            '   every page, and the toggle stores "light" or "dark". */',
            '[data-theme="dark"] {', '  color-scheme: dark;']
    out += _dark('  ')
    out += ['}', '', '[data-theme="light"] {', '  color-scheme: light;', '}']
    return '\n'.join(out)


if __name__ == '__main__':
    for row in check():
        print('FAIL', row)
    for mode in ('light', 'dark'):
        for fg, bg in PAIRS:
            print(mode, fg, bg, round(contrast(value(fg, mode), value(bg, mode)), 2))
