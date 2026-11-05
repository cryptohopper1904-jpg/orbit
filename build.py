#!/usr/bin/env python3
"""Baut index.html (Deutsch) und en/index.html aus src/template.html + src/strings.py. — PiP
Aufruf: python3 build.py   (keine Abhängigkeiten)"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
import strings  # noqa: E402

HTML_KEYS = {'h1', 'lang_switch'}   # dürfen Markup enthalten; alles andere wird escaped


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def render(L):
    tpl = (ROOT / 'src' / 'template.html').read_text(encoding='utf-8')
    data = dict(ui=L['ui'], worlds=L['worlds'], threads=strings.threads(L))
    # </script> im JSON unschädlich machen
    tpl = tpl.replace('{{DATA}}', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))

    def sub(m):
        k = m.group(1)
        if k not in L:
            raise KeyError(f'{L["lang"]}: Schlüssel fehlt: {k}')
        v = L[k]
        return v if k in HTML_KEYS else esc(v)
    out = re.sub(r'\{\{(\w+)\}\}', sub, tpl)
    return out


for L, path in [(strings.DE, ROOT / 'index.html'), (strings.EN, ROOT / 'en' / 'index.html')]:
    path.parent.mkdir(exist_ok=True)
    path.write_text(render(L), encoding='utf-8')
    print('geschrieben:', path.relative_to(ROOT))
