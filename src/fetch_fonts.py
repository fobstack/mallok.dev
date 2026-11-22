"""Downloads Figtree (SIL Open Font License 1.1) into assets/fonts/.

Run once, by hand: python3 src/fetch_fonts.py
The build then emits @font-face rules for whatever is present; without the
files the site falls back to the system sans stack and requests nothing.

Sources: the Google Fonts CSS API (variable woff2, latin + latin-ext subsets)
and the licence text from the google/fonts repository.
"""

import os
import re
import urllib.request

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')
OUT = os.path.join(ROOT, 'assets', 'fonts')
CSS = 'https://fonts.googleapis.com/css2?family=Figtree:wght@300..900&display=swap'
OFL = 'https://raw.githubusercontent.com/google/fonts/main/ofl/figtree/OFL.txt'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return urllib.request.urlopen(req, timeout=30).read()


def main():
    os.makedirs(OUT, exist_ok=True)
    css = get(CSS).decode('utf-8')
    for subset, url in re.findall(r'/\* ([a-z-]+) \*/\s*@font-face\s*{[^}]*?url\((https://[^)]+\.woff2)\)', css):
        if subset in ('latin', 'latin-ext'):
            data = get(url)
            open(os.path.join(OUT, f'figtree-{subset}.woff2'), 'wb').write(data)
            print(f'figtree-{subset}.woff2', len(data), 'bytes')
    open(os.path.join(OUT, 'OFL.txt'), 'wb').write(get(OFL))
    print('OFL.txt written; now run python3 src/build.py')


if __name__ == '__main__':
    main()
