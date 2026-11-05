# Orbit — Vorstellungsseite

Live: https://cryptohopper1904-jpg.github.io/orbit/ (Deutsch) · `/en/` (Englisch) · `/de/` leitet auf `/` um.

Die Seiten werden **generiert** — `index.html` und `en/index.html` nicht von Hand ändern:

- `src/template.html` — Aufbau, Styles und die klickbare Inbox-Demo (Vanilla JS, keine Abhängigkeiten)
- `src/strings.py` — alle Texte und Demo-Verläufe je Sprache
- `python3 build.py` — schreibt beide Seiten neu

Inhalte an der echten App ausrichten (Repo `message-cockpit`): nur Funktionen zeigen, die dort existieren.
