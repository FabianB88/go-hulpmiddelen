# -*- coding: utf-8 -*-
"""Bouwt de hulpmiddelensite uit tools/inhoud.py.

Draaien:  python tools/bouw_site.py

Genereert docs/ opnieuw: een startpagina, een pagina per cluster, het
stijlbestand en een kopie van alles in bestanden/. GitHub Pages serveert docs/
op de main-branch.
"""
import io
import os
import shutil
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.dirname(HIER)
UIT = os.path.join(WORTEL, 'docs')
BESTANDEN = os.path.join(WORTEL, 'bestanden')
sys.path.insert(0, HIER)

import inhoud  # noqa: E402


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def schrijf(naam, tekst):
    pad = os.path.join(UIT, naam)
    io.open(pad, 'w', encoding='utf-8').write(tekst)


def pagina(titel, hoofd, actief=None, terug=False):
    """Zet een complete HTML-pagina in elkaar."""
    nav = ''.join(
        '<a class="nav__link%s" href="%s.html"%s>%s</a>'
        % (' nav__link--actief' if c['id'] == actief else '', c['id'],
           ' aria-current="page"' if c['id'] == actief else '', esc(c['naam']))
        for c in inhoud.CLUSTERS)

    return (
        '<!DOCTYPE html>\n'
        '<html lang="nl">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>%s</title>\n'
        '<link rel="stylesheet" href="stijl.css">\n'
        '</head>\n<body>\n'
        '<a class="overslaan" href="#inhoud">Ga direct naar de inhoud</a>\n'
        '<header class="kop">\n'
        '  <div class="omhulsel">\n'
        '    <a class="kop__titel" href="index.html">%s</a>\n'
        '    <p class="kop__ondertitel">%s</p>\n'
        '  </div>\n'
        '</header>\n'
        '<nav class="nav" aria-label="Clusters">\n'
        '  <div class="omhulsel nav__rij">\n'
        '    <a class="nav__link%s" href="index.html"%s>Overzicht</a>\n'
        '    %s\n'
        '  </div>\n'
        '</nav>\n'
        '<main class="omhulsel" id="inhoud">\n%s</main>\n'
        '<footer class="voet">\n  <div class="omhulsel">%s</div>\n</footer>\n'
        '</body>\n</html>\n'
        % (esc(titel), esc(inhoud.TITEL), esc(inhoud.ONDERTITEL),
           '' if actief else ' nav__link--actief',
           '' if actief else ' aria-current="page"',
           nav, hoofd, voetregel()))


def voetregel():
    items = ''.join(
        '<li><a href="%s">%s</a> — %s</li>'
        % (v['url'], esc(v['naam']), esc(v['omschrijving']))
        for v in inhoud.VERWIJZINGEN)
    return ('<h2 class="voet__kop">Zie ook</h2><ul class="voet__lijst">%s</ul>'
            % items)


def veld(label, waarde):
    """Eén regel in het informatieblok. Leeg = zichtbaar gemarkeerd."""
    if waarde:
        return ('<div class="veld"><dt class="veld__label">%s</dt>'
                '<dd class="veld__waarde">%s</dd></div>'
                % (esc(label), esc(waarde)))
    return ('<div class="veld"><dt class="veld__label">%s</dt>'
            '<dd class="veld__waarde veld__waarde--leeg">Nog in te vullen</dd>'
            '</div>' % esc(label))


def downloads(h):
    knoppen = []
    if h['docx']:
        knoppen.append(
            '<a class="knop" href="bestanden/%s" download>Word-bestand '
            '<span class="knop__bij">om in te vullen</span></a>' % h['docx'])
    if h['pdf']:
        knoppen.append(
            '<a class="knop knop--stil" href="bestanden/%s">Pdf '
            '<span class="knop__bij">om door te lezen</span></a>' % h['pdf'])
    if not knoppen:
        return ('<p class="geenbestand">Het bestand staat er nog niet in. '
                'Zodra het klaar is, verschijnt hier de download.</p>')
    return '<div class="knoppen">%s</div>' % ''.join(knoppen)


def noot(h):
    """Optionele kanttekening bij een hulpmiddel. HTML mag, want de tekst komt
    uit inhoud.py en niet van buiten."""
    tekst = h.get('noot')
    if not tekst:
        return ''
    return '<p class="noot">%s</p>\n  ' % tekst


def hulpmiddelblok(nummer, h):
    return (
        '<article class="kaart hulpmiddel" id="%s">\n'
        '  <div class="hulpmiddel__kop">\n'
        '    <span class="nummer" aria-hidden="true">%02d</span>\n'
        '    <h2 class="hulpmiddel__naam">%s</h2>\n'
        '  </div>\n'
        '  <p class="hulpmiddel__typering">%s</p>\n'
        '  %s'
        '  <dl class="velden">%s%s</dl>\n'
        '  %s\n'
        '</article>\n'
        % (h['id'], nummer, esc(h['naam']), esc(h['typering']),
           noot(h),
           veld('Wanneer pak je dit', h['wanneer']),
           veld('Wat lever je op', h['oplevering']),
           downloads(h)))


def bouw():
    if os.path.isdir(UIT):
        shutil.rmtree(UIT)
    os.makedirs(UIT)

    # ---------------------------------------------------------- startpagina
    kaarten = []
    nummer = 0
    for c in inhoud.CLUSTERS:
        namen = ''.join('<li>%s</li>' % esc(h['naam']) for h in c['hulpmiddelen'])
        aantal = len(c['hulpmiddelen'])
        kaarten.append(
            '<a class="kaart cluster" href="%s.html">\n'
            '  <h2 class="cluster__naam">%s</h2>\n'
            '  <p class="cluster__intro">%s</p>\n'
            '  <ul class="cluster__lijst">%s</ul>\n'
            '  <span class="cluster__meer">%d hulpmiddel%s bekijken</span>\n'
            '</a>\n'
            % (c['id'], esc(c['naam']), c['intro'], namen,
               aantal, '' if aantal == 1 else 'en'))
        nummer += aantal

    start = ('<p class="inleiding">%s</p>\n'
             '<aside class="kader">%s</aside>\n'
             '<div class="raster">%s</div>\n'
             % (esc(inhoud.INLEIDING), inhoud.KADER, ''.join(kaarten)))
    schrijf('index.html', pagina(inhoud.TITEL, start))

    # ------------------------------------------------------- clusterpagina's
    teller = 0
    for c in inhoud.CLUSTERS:
        blokken = []
        for h in c['hulpmiddelen']:
            teller += 1
            blokken.append(hulpmiddelblok(h['nummer'], h))
        hoofd = ('<p class="kruimel"><a href="index.html">Overzicht</a> '
                 '<span aria-hidden="true">›</span> %s</p>\n'
                 '<h1 class="titel">%s</h1>\n'
                 '<p class="inleiding">%s</p>\n'
                 '<p class="hint">%s</p>\n%s'
                 % (esc(c['naam']), esc(c['naam']), c['intro'],
                    esc(inhoud.HINT), ''.join(blokken)))
        schrijf('%s.html' % c['id'],
                pagina('%s — %s' % (c['naam'], inhoud.TITEL), hoofd,
                       actief=c['id']))

    # ------------------------------------------------------------ omleidingen
    # Oude clusternamen blijven werken. Zonder deze stubs krijgt iedereen met
    # een bookmark of een pagina in zijn cache een 404 van GitHub Pages.
    for oud, nieuw in sorted(getattr(inhoud, 'OMLEIDINGEN', {}).items()):
        schrijf('%s.html' % oud,
                '<!DOCTYPE html>\n<html lang="nl">\n<head>\n'
                '<meta charset="utf-8">\n'
                '<meta http-equiv="refresh" content="0; url=%s.html">\n'
                '<link rel="canonical" href="%s.html">\n'
                '<title>Verplaatst — %s</title>\n'
                '</head>\n<body>\n'
                '<p>Deze pagina is verplaatst. '
                '<a href="%s.html">Ga verder naar de nieuwe pagina</a>.</p>\n'
                '</body>\n</html>\n' % (nieuw, nieuw, inhoud.TITEL, nieuw))

    schrijf('stijl.css', STIJL)
    io.open(os.path.join(UIT, '.nojekyll'), 'w').write('')

    # ----------------------------------------------------------- bestanden
    doel = os.path.join(UIT, 'bestanden')
    os.makedirs(doel)
    gekopieerd = 0
    if os.path.isdir(BESTANDEN):
        for naam in sorted(os.listdir(BESTANDEN)):
            if naam.startswith('.'):
                continue
            shutil.copy2(os.path.join(BESTANDEN, naam),
                         os.path.join(doel, naam))
            gekopieerd += 1

    # ------------------------------------------------- controle op ontbreken
    ontbreekt = [h['naam'] for c in inhoud.CLUSTERS for h in c['hulpmiddelen']
                 if not h['docx']]
    leeg = [h['naam'] for c in inhoud.CLUSTERS for h in c['hulpmiddelen']
            if not (h['wanneer'] and h['oplevering'])]
    geenpdf = [h['naam'] for c in inhoud.CLUSTERS for h in c['hulpmiddelen']
               if h['docx'] and not h['pdf']]

    print('%d clusters, %d hulpmiddelen, %d bestanden gekopieerd'
          % (len(inhoud.CLUSTERS), teller, gekopieerd))
    if ontbreekt:
        print('  nog geen download: %s' % ', '.join(ontbreekt))
    if leeg:
        print('  nog in te vullen velden: %s' % ', '.join(leeg))
    if geenpdf:
        print('  nog geen pdf: %s' % ', '.join(geenpdf))


STIJL = """/* Green Office — palet uit de Flutter-app (lib/theme.dart, GOColors) */
:root {
  --achtergrond: #F7F4F0;
  --kaart: #FFFFFF;
  --vlak: #F2EEE9;
  --rand: #E4DDD6;
  --rand-zacht: #EDE8E3;
  --tekst: #1C1713;
  --tekst-secundair: #7A6E66;
  --tekst-gedimd: #B0A49A;
  --accent: #5C7A5A;
  --accent-donker: #3D5C3B;
  --accent-licht: #EFF4EE;
  --accent-medium: #D0E3CF;
  --schaduw: 0 2px 12px rgba(0, 0, 0, .08);
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--achtergrond);
  color: var(--tekst);
  font-family: Inter, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 17px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.omhulsel { max-width: 880px; margin: 0 auto; padding: 0 1.25rem; }

.overslaan {
  position: absolute; left: -9999px;
  background: var(--accent); color: #fff;
  padding: .75rem 1.25rem; border-radius: 0 0 10px 0;
}
.overslaan:focus { left: 0; top: 0; z-index: 10; }

/* Kop */
.kop { background: var(--kaart); border-bottom: 1px solid var(--rand); padding: 2rem 0 1.5rem; }
.kop__titel {
  display: inline-block; font-size: 1.6rem; font-weight: 700;
  color: var(--tekst); text-decoration: none; letter-spacing: -.01em;
}
.kop__titel:hover { color: var(--accent-donker); }
.kop__ondertitel { margin: .35rem 0 0; color: var(--tekst-secundair); }

/* Navigatie */
.nav { background: var(--kaart); border-bottom: 1px solid var(--rand); position: sticky; top: 0; z-index: 5; }
.nav__rij { display: flex; flex-wrap: wrap; gap: .25rem; padding-top: .5rem; padding-bottom: .5rem; }
.nav__link {
  padding: .5rem .85rem; border-radius: 10px; text-decoration: none;
  color: var(--tekst-secundair); font-size: .95rem; font-weight: 600;
}
.nav__link:hover { background: var(--vlak); color: var(--tekst); }
.nav__link--actief { background: var(--accent-licht); color: var(--accent-donker); }

/* Inhoud */
main { padding: 2rem 1.25rem 3rem; }
.titel { font-size: 1.9rem; margin: .25rem 0 .5rem; letter-spacing: -.02em; }
.inleiding { color: var(--tekst-secundair); max-width: 60ch; margin-top: 0; }
.kruimel { font-size: .9rem; color: var(--tekst-secundair); margin: 0 0 .5rem; }
.kruimel a { color: var(--tekst-secundair); }

.kaart {
  background: var(--kaart); border: 1px solid var(--rand);
  border-radius: 14px; box-shadow: var(--schaduw); padding: 1.5rem;
}

.kader {
  margin: 1.25rem 0 0; padding: 1.1rem 1.25rem;
  background: var(--accent-licht); border: 1px solid var(--accent-medium);
  border-radius: 14px; max-width: 68ch;
}
.hint {
  margin: -.25rem 0 1.5rem; padding: .5rem .85rem;
  background: var(--vlak); border-left: 3px solid var(--accent-medium);
  border-radius: 0 8px 8px 0;
  font-size: .95rem; color: var(--tekst-secundair); max-width: 62ch;
}

/* Startpagina */
.raster { display: grid; gap: 1rem; grid-template-columns: 1fr; margin-top: 1.5rem; }
@media (min-width: 640px) { .raster { grid-template-columns: 1fr 1fr; } }
.cluster { display: block; text-decoration: none; color: inherit; }
.cluster:hover { border-color: var(--accent-medium); }
.cluster__naam { margin: 0 0 .35rem; font-size: 1.2rem; color: var(--accent-donker); }
.cluster__intro { margin: 0 0 .75rem; color: var(--tekst-secundair); font-size: .95rem; }
.cluster__lijst { margin: 0 0 1rem; padding-left: 1.1rem; font-size: .95rem; }
.cluster__lijst li { margin-bottom: .15rem; }
.cluster__meer { font-weight: 600; color: var(--accent); font-size: .95rem; }

/* Hulpmiddel */
.hulpmiddel { margin-bottom: 1.25rem; }
.hulpmiddel__kop { display: flex; align-items: baseline; gap: .75rem; }
.nummer {
  font-variant-numeric: tabular-nums; font-weight: 700; font-size: .95rem;
  color: #fff; background: var(--accent); border-radius: 8px;
  padding: .15rem .5rem; flex: none;
}
.hulpmiddel__naam { margin: 0; font-size: 1.25rem; }
.hulpmiddel__typering { margin: .6rem 0 1rem; max-width: 62ch; }

.velden { margin: 0 0 1.25rem; padding: 1rem 1.1rem; background: var(--vlak); border-radius: 10px; }
.veld { display: grid; gap: .1rem; padding: .4rem 0; border-bottom: 1px solid var(--rand-zacht); }
.veld:last-child { border-bottom: 0; }
@media (min-width: 560px) { .veld { grid-template-columns: 12rem 1fr; gap: 1rem; align-items: baseline; } }
.veld__label { font-weight: 600; font-size: .9rem; color: var(--tekst-secundair); }
.veld__waarde { margin: 0; }
.veld__waarde--leeg { color: var(--tekst-secundair); font-style: italic; }

.noot {
  margin: 0 0 1.1rem; padding: .8rem 1rem;
  background: var(--accent-licht); border-left: 3px solid var(--accent);
  border-radius: 0 10px 10px 0; font-size: .95rem; max-width: 62ch;
}

/* Knoppen */
.knoppen { display: flex; flex-wrap: wrap; gap: .6rem; }
.knop {
  display: inline-flex; flex-direction: column; gap: .1rem;
  background: var(--accent); color: #fff; text-decoration: none;
  padding: 13px 20px; border-radius: 10px; font-weight: 600;
}
.knop:hover { background: var(--accent-donker); }
.knop--stil { background: var(--kaart); color: var(--accent-donker); border: 1px solid var(--rand); }
.knop--stil:hover { background: var(--accent-licht); border-color: var(--accent-medium); }
.knop__bij { font-weight: 400; font-size: .85rem; opacity: .9; }
.geenbestand {
  margin: 0; padding: .85rem 1rem; border-radius: 10px;
  background: var(--vlak); color: var(--tekst-secundair);
  font-size: .95rem; border-left: 3px solid var(--rand);
}

/* Voet */
.voet { border-top: 1px solid var(--rand); background: var(--kaart); padding: 2rem 0 2.5rem; margin-top: 1rem; }
.voet__kop { font-size: 1rem; margin: 0 0 .5rem; }
.voet__lijst { margin: 0; padding-left: 1.1rem; color: var(--tekst-secundair); font-size: .95rem; }
.voet__lijst a { color: var(--accent-donker); font-weight: 600; }

a:focus-visible, .knop:focus-visible, .cluster:focus-visible {
  outline: 2px solid var(--accent-donker); outline-offset: 2px;
}
"""


if __name__ == '__main__':
    bouw()
