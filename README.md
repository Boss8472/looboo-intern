# looboo (privat)

Arbeitsrepo für looboo.de: Rohdaten, Kontext, Entwürfe und Tools. **Nichts hiervon wird veröffentlicht.**

| Pfad | Inhalt |
|---|---|
| `looboo/` | **Submodule** → `github.com/Boss8472/looboo`: das htdocs-Repo, wird automatisch auf looboo.de deployed |
| `entwuerfe/` | 10 Designentwürfe, Übersicht in `entwuerfe/index.html` |
| `tools/make_icons.py` | erzeugt Favicons, App-Icons und das OG-Bild ins Submodule (`python3 tools/make_icons.py`, benötigt Pillow) |

## Submodule-Workflow

```sh
# Klonen inkl. htdocs
git clone --recurse-submodules <url-dieses-repos>

# Änderung an der Website
cd looboo
git add -A && git commit -m "…" && git push      # 1. zuerst htdocs pushen (geht live)
cd ..
git add looboo && git commit -m "htdocs aktualisiert" && git push   # 2. Zeiger im äußeren Repo nachziehen
```

Immer zuerst das innere Repo pushen, dann das äußere. Sonst zeigt der Submodule-Zeiger auf einen Commit, den es auf GitHub nicht gibt.

## Remote für dieses Repo einrichten

```sh
git remote add origin git@github.com:Boss8472/<privates-repo>.git
git push -u origin main
```
