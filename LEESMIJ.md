# Hulpmiddelen — Green Office

Losse werkvormen, canvassen en handleidingen voor Green Office-medewerkers,
gebundeld per cluster. Elk hulpmiddel is een Word-bestand om in te vullen, met
een pdf ernaast om snel door te lezen.

Draait als statische site op GitHub Pages en is bedoeld om **embedded in de
Green Office-app** getoond te worden. Het palet komt daarom uit
`green-office-flutter/lib/theme.dart`, zodat het naadloos aansluit.

## Bijwerken

De inhoud staat in **`tools/inhoud.py`** — clusters, hulpmiddelen, en per
hulpmiddel de teksten en de bestandsnamen. De HTML in `docs/` wordt
gegenereerd en overschreven; bewerk die dus nooit met de hand.

```bash
python tools/bouw_site.py
```

De generator meldt na afloop welke hulpmiddelen nog geen download hebben en
welke velden nog leeg zijn.

## Een bestand toevoegen

1. Zet de `.docx` en de `.pdf` in `bestanden/`.
2. Vul in `tools/inhoud.py` bij het betreffende hulpmiddel de velden `docx` en
   `pdf` met de bestandsnamen.
3. Vul ook `wanneer`, `oplevering` en `tijd` in.
4. `python tools/bouw_site.py`, daarna committen en pushen.

Lege velden verschijnen op de site als **Nog in te vullen**, en een hulpmiddel
zonder bestand krijgt een blokje dat zegt dat de download nog komt. Er belandt
dus nooit verzonnen tekst op de pagina — wat ontbreekt, is zichtbaar.

## Publiceren

De site staat in `docs/` en GitHub Pages serveert die map op de `main`-branch.
Na `bouw_site.py` dus gewoon:

```bash
git add -A && git commit -m "update" && git push
```

## Waarom downloads en geen webpagina's

De meeste hulpmiddelen zijn canvassen en werkbladen die je **invult** — daar is
het Word-bestand het product, niet een leespagina. De clusterpagina's zijn er om
te kiezen: wat is het, wanneer pak je het, wat levert het op. De pdf ernaast
dekt het doorlezen af, ook binnen de app, want een webview toont een pdf inline
en een Word-bestand niet.

Blijkt één hulpmiddel puur leesmateriaal dat niemand invult, maak van dát ene
een echte pagina. Behandel dat als uitzondering, niet als beleid.

## Nummering

De nummers op de site zijn **weergavevolgorde**, niet de identiteit van een
hulpmiddel. Verwijs in de documenten naar de **naam** van een hulpmiddel, nooit
naar het nummer — bij de minorhandleidingen is die nummering al eens uit de pas
gaan lopen, en na een herindeling klopt hij opnieuw niet.

## Verhouding tot de e-learning

De e-learning [AI leren gebruiken](https://fabianb88.github.io/ai-gebruiken-elearning/)
is primair. *Slim AI gebruiken* en *AI naar website* zijn losse hulpmiddelen die
daarmee overlappen; dat is bewust. Zet in die twee documenten wel een regel
bovenaan die naar de e-learning verwijst als het volledige verhaal.

## Toegankelijkheid

Als bekostigde onderwijsinstelling val je onder het Tijdelijk besluit digitale
toegankelijkheid: WCAG 2.1 AA. Wat in deze site al geregeld is: een
overslaan-link, zichtbare focusstates, semantische koppen, `aria-current` op de
actieve navigatie, en een palet dat is nagerekend — `#5C7A5A` haalt 4,79:1 op
wit en `#7A6E66` haalt 4,61:1. `#B0A49A` haalt AA **niet** en wordt daarom
alleen decoratief gebruikt.

Wat je zelf moet bewaken: de documenten zelf. Een pdf met koppenstructuur en
alt-teksten is toegankelijk, een gescande pdf niet.
