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

## Een bestand toevoegen of bijwerken

1. Zet de `.docx` (en de `.pdf` zodra die er is) in `bestanden/`.
2. Vul in `tools/inhoud.py` bij het hulpmiddel de velden `docx` en `pdf` met de
   bestandsnamen.
3. `python tools/bouw_site.py`, daarna committen en pushen.

De teksten bij **typering**, **wanneer** en **oplevering** komen letterlijk uit
de kopregel van het document zelf. Wijzig je een document, neem de nieuwe tekst
dan over in `tools/inhoud.py`, zodat site en document hetzelfde zeggen.

De generator meldt na afloop wat er nog ontbreekt: hulpmiddelen zonder
download, lege velden, en documenten waar nog geen pdf bij zit. Op de site
verschijnt daar niets van — wat er niet is, wordt gewoon niet getoond.

## Publiceren

De site staat in `docs/` en GitHub Pages serveert die map op de `main`-branch.
Na `bouw_site.py` dus gewoon:

```bash
git add -A && git commit -m "update" && git push
```

## Waarom downloads en geen webpagina's

De meeste hulpmiddelen zijn canvassen en werkbladen die je **invult** — daar is
het Word-bestand het product, niet een leespagina. De clusterpagina's zijn er om
te kiezen: wat is het, wanneer pak je het, wat levert het op.

Er komt een **pdf naast elke `.docx`**, want een webview toont een pdf inline en
een Word-bestand niet. Dat dekt het doorlezen binnen de app af zonder dat er één
webpagina per hulpmiddel gebouwd hoeft te worden. Die pdf's zijn er nog niet;
tot die tijd staat er alleen de Word-knop.

Blijkt één hulpmiddel puur leesmateriaal dat niemand invult, maak van dát ene
een echte pagina. Behandel dat als uitzondering, niet als beleid.

## Nummering — niet aanpassen

De nummers 01 tot en met 14 horen bij de bestanden én bij de
verwijzingen in de teksten. De documenten verwijzen onderling
naar elkaar met hun nummer: *"prioriteer met 10"*, *"zie 09"*, *"terugleggen in
je projectvoorstel (zie 08)"*. Hernummeren breekt die verwijzingen stuk, en dat
merk je pas als iemand erop klikt.

Komt er een hulpmiddel bij, geef het dan nummer 14 en zet het achteraan — ook
als het inhoudelijk ergens in het midden hoort. De clustering op deze site
bepaalt de plek op de pagina; het nummer blijft de identiteit van het document.

## Nog te leveren

- **De pdf's** bij alle veertien documenten. Zolang die er niet zijn, staat er
  alleen de Word-knop; er verschijnt geen "volgt nog" op de site.

## Openstaand in de documenten

Bij het invoegen van Scrum op plek 03 is alles vanaf 04 opgeschoven. De
verwijzingen in de teksten zijn grotendeels meegegaan, maar **drie zijn blijven
staan op het oude nummer**:

| Document | Staat er | Moet zijn |
|---|---|---|
| 09 Projectvoorstel | "Werk uit in 04 Stakeholderanalyse" | 05 Stakeholderanalyse |
| 10 Brainstorm | "de rest prioriteren met 10 Prioriteren" | 11 Prioriteren |
| 10 Brainstorm (kopregel) | "die je prioriteert met 10" | met 11 |

Op de site staat de juiste versie; in de Word-bestanden nog niet. Laat dit bij
de volgende ronde in de bron corrigeren.

Verder wijkt de site op één punt bewust af: bij **07 Probleemdefinitie** staat
op de site "getoetst bij je opdrachtgever en/of clusterlead", terwijl het
document alleen "opdrachtgever" zegt.

**Controleren na een hernummering:** lees de documenten uit met `python-docx`,
zoek op patronen als `zie \d\d` en `\d\d Naam`, en toets elk nummer tegen de
lijst in `tools/inhoud.py`. Zo vind je stille fouten voordat iemand erop klikt.

## Verhouding tot de e-learning## Verhouding tot de e-learning

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
