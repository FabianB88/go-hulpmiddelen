# -*- coding: utf-8 -*-
"""De inhoud van de hulpmiddelensite: clusters en hulpmiddelen, in volgorde.

Dit bestand is de bron. Voeg je een hulpmiddel toe of verplaats je er een, dan
pas je dit bestand aan en draai je `python tools/bouw_site.py` opnieuw.

De teksten bij 'typering', 'wanneer' en 'oplevering' komen uit de kopregel van
de documenten zelf. Wijzigt een document, neem de nieuwe tekst dan hier over,
zodat site en document hetzelfde zeggen. Twee plekken wijken bewust af; die
staan hieronder met een opmerking gemarkeerd.

LET OP — de nummers horen bij de bestanden én bij de verwijzingen in de teksten.
De documenten verwijzen onderling naar elkaar met hun nummer ("zie 09",
"prioriteer met 11"). Hernummeren betekent dus ook: alle documenten opnieuw
nalopen. Komt er een hulpmiddel bij, zet het bij voorkeur achteraan.

Per hulpmiddel:
    nummer      komt overeen met het bestand
    id          anker in de pagina, kleine letters met streepjes
    naam        zoals het op de pagina en in het document staat
    typering    de ondertitel uit het document
    wanneer     wanneer pak je dit erbij
    oplevering  wat heb je als je klaar bent
    noot        optionele kanttekening (HTML mag), verschijnt in een kader
    docx        bestandsnaam in bestanden/, om in te vullen
    pdf         bestandsnaam in bestanden/, om door te lezen (leeg = nog niet)
"""

TITEL = 'Hulpmiddelen'
ONDERTITEL = 'Werkvormen, canvassen en handleidingen voor Green Office'
INLEIDING = (
    'Dit is een databank, geen stappenplan. Veertien hulpmiddelen waaruit je '
    'pakt wat bij jouw project past — de rest laat je staan. Elk hulpmiddel is '
    'een Word-bestand met uitleg en invulbare onderdelen.')

# Kader boven aan de startpagina. Staat los van de inleiding omdat het de
# belangrijkste boodschap is en niet weggelezen mag worden.
KADER = (
    '<b>Niet elk hulpmiddel is voor iedereen nuttig.</b> Werk je zonder '
    'opdrachtgever, dan sla je 04 over. Gaat je vraagstuk niet over een '
    'materiaalstroom, dan heb je 06 en 08 niet nodig. Hoef je niemand te '
    'overtuigen, dan is 09 overbodig. Kijk bij elk hulpmiddel naar '
    '<i>Wanneer pak je dit</i> en beslis zelf of het aan de orde is. Twee tot '
    'vier goed ingevulde hulpmiddelen zeggen meer dan veertien half ingevulde.')

# Eén regel die boven elke clusterpagina komt, als herinnering.
HINT = 'Pak hieruit wat bij je project past; je hoeft niet alles te gebruiken.'

CLUSTERS = [
    {
        'id': 'aanpak',
        'naam': 'Aanpak',
        'intro': 'Waarmee je bepaalt hoe je werkt: welke route je volgt, hoe je '
                 'richting houdt en in welk ritme je stappen zet.',
        'hulpmiddelen': [
            {'nummer': 1, 'id': 'projectaanpak', 'naam': 'Projectaanpak',
             'typering': 'Het Double Diamond als kaart voor projecten waarvan '
                         'de vraag nog niet vaststaat.',
             'wanneer': 'Aan de start van een project, en daarna als je niet '
                        'weet waar je staat.',
             'oplevering': 'Geen eigen product. Dit model bepaalt de volgorde '
                           'van je andere werk.',
             'docx': '01_Projectaanpak.docx', 'pdf': ''},
            {'nummer': 2, 'id': 'aanpakplan', 'naam': 'Aanpakplan',
             'typering': 'Richting kiezen en in beweging blijven, zonder alles '
                         'vooraf dicht te timmeren.',
             'wanneer': 'Aan het begin, daarna bijwerken bij elk '
                        'voortgangsoverleg.',
             'oplevering': 'Een levend aanpakplan dat je meeneemt naar je '
                           'overleg.',
             'noot': 'Dit hulpmiddel is mogelijk aanvullend op het '
                     'PVA-werkboek, dat nog volgt. <b>Het PVA-werkboek is '
                     'leidend</b> — wijken de twee van elkaar af, houd dan het '
                     'werkboek aan.',
             'docx': '02_Aanpakplan.docx', 'pdf': ''},
            {'nummer': 3, 'id': 'scrum-en-kanban', 'naam': 'Scrum & kanban',
             'typering': 'Ritme, kleine stappen en overzicht in je project.',
             'wanneer': 'Vanaf de eerste week, het hele project door.',
             'oplevering': 'Een bijgewerkt bord, een sprintplanning per sprint '
                           'en jullie werkafspraken.',
             'docx': '03_Scrum-en-kanban.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'verkennen',
        'naam': 'Verkennen',
        'intro': 'Waarmee je uitzoekt wat de vraag werkelijk is, wie erbij '
                 'betrokken zijn en waar je mee te maken hebt.',
        'hulpmiddelen': [
            {'nummer': 4, 'id': 'opdrachtgever-afspraken',
             'naam': 'Opdrachtgever-afspraken',
             'typering': 'De vraag scherp krijgen en een ritme afspreken voor '
                         'goed contact.',
             'wanneer': 'Meteen aan het begin. Het ritme houd je het hele '
                        'project aan.',
             'oplevering': 'Ingevulde intake, vastgelegde afspraken en een '
                           'afstemmingsritme dat je deelt.',
             'noot': 'Alleen aan de orde als er iemand is die de opdracht '
                     'geeft — een externe opdrachtgever, of je clusterlead. '
                     'Pak je iets op dat je zelf hebt bedacht en waar niemand '
                     'anders over gaat, sla dit dan over.',
             'docx': '04_Opdrachtgever-afspraken.docx', 'pdf': ''},
            {'nummer': 5, 'id': 'stakeholderanalyse',
             'naam': 'Stakeholderanalyse',
             'typering': 'In kaart brengen wie belang heeft bij je project en '
                         'wie er invloed op heeft.',
             'wanneer': 'Aan de start, zodra je de vraag kent. Bijwerken als er '
                        'partijen bij komen.',
             'oplevering': 'Een ingevuld grid en een lijst met per partij je '
                           'aanpak.',
             'docx': '05_Stakeholderanalyse.docx', 'pdf': ''},
            {'nummer': 6, 'id': 'ketenschets', 'naam': 'Ketenschets',
             'typering': 'In beeld brengen waar materiaal, geld en informatie '
                         'langsgaan.',
             'wanneer': 'Aan de start, zodra je weet welke stroom je '
                        'onderzoekt.',
             'oplevering': 'Een getekende ketenschets met drie gemarkeerde '
                           'hotspots, plus je aannames.',
             'docx': '06_Ketenschets.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'scherpstellen',
        'naam': 'Scherpstellen',
        'intro': 'Waarmee je van een vage vraag naar een scherp probleem gaat, '
                 'en dat onderbouwd op tafel legt.',
        'hulpmiddelen': [
            {'nummer': 7, 'id': 'probleemdefinitie',
             'naam': 'Probleemdefinitie',
             'typering': 'Van de gevraagde oplossing naar het echte probleem.',
             'wanneer': 'Nadat je de intake en je eerste verkenning hebt '
                        'gedaan.',
             # Afwijking van het document: dat zegt alleen 'opdrachtgever'.
             # Bij het Green Office is dat vaak de clusterlead.
             'oplevering': 'Eén scherpe probleemdefinitie en één kansvraag, '
                           'getoetst bij je opdrachtgever en/of clusterlead.',
             'docx': '07_Probleemdefinitie.docx', 'pdf': ''},
            {'nummer': 8, 'id': 'circulaire-denkmodellen',
             'naam': 'Circulaire denkmodellen',
             'typering': 'Drie modellen om je vraagstuk circulair scherp te '
                         'krijgen.',
             'wanneer': 'Zodra je probleem scherp is, bij het uitwerken van '
                        'richtingen.',
             'oplevering': 'Per model een ingevuld werkblad, dat je gebruikt in '
                           'je projectvoorstel.',
             'docx': '08_Circulaire-denkmodellen.docx', 'pdf': ''},
            {'nummer': 9, 'id': 'projectvoorstel', 'naam': 'Projectvoorstel',
             'typering': 'Je project onderbouwen rond waarom, hoe en wat.',
             'wanneer': 'Nadat je probleemdefinitie staat, en bijwerken tot de '
                        'oplevering.',
             'oplevering': 'Een voorstel waarmee je intern draagvlak, tijd of '
                           'middelen krijgt.',
             'docx': '09_Projectvoorstel.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'ontwikkelen',
        'naam': 'Ontwikkelen',
        'intro': 'Waarmee je van veel mogelijkheden naar één onderbouwde keuze '
                 'gaat.',
        'hulpmiddelen': [
            {'nummer': 10, 'id': 'brainstorm', 'naam': 'Brainstorm',
             'typering': 'Eerst breed denken, dan kiezen.',
             'wanneer': 'Zodra je kansvraag staat en je richtingen zoekt.',
             # Afwijking van het document: dat zegt hier nog 'met 10'. Onder de
             # nieuwe nummering is Prioriteren nummer 11.
             'oplevering': 'Een gevulde ideeënlijst en een gekozen richting, '
                           'die je prioriteert met 11.',
             'docx': '10_Brainstorm.docx', 'pdf': ''},
            {'nummer': 11, 'id': 'prioriteren', 'naam': 'Prioriteren',
             'typering': 'Kiezen waar je je tijd en energie op zet.',
             'wanneer': 'Na elke brainstorm, en elke keer dat je je planning '
                        'bijstelt.',
             'oplevering': 'Een ingevulde MoSCoW en matrix, vertaald naar je '
                           'aanpakplan.',
             'docx': '11_Prioriteren.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'doorlopend',
        'naam': 'Doorlopend',
        'intro': 'Hulpmiddelen die niet bij één fase horen maar door je hele '
                 'project heen meelopen. Voor je AI-werk is de e-learning '
                 '<i>AI leren gebruiken</i> het volledige verhaal; dit zijn de '
                 'korte werkvormen.',
        'hulpmiddelen': [
            {'nummer': 12, 'id': 'ai-naar-website', 'naam': 'AI naar website',
             'typering': 'Van een schets naar een werkende pagina, zonder te '
                         'coderen.',
             'wanneer': 'Zodra je iets hebt om te tonen: een concept, een '
                        'overzicht of een resultaat.',
             'oplevering': 'Een werkende pagina of prototype, plus je ingevulde '
                           'briefing.',
             'docx': '12_AI-naar-website.docx', 'pdf': ''},
            {'nummer': 13, 'id': 'slim-ai-gebruiken',
             'naam': 'Slim AI gebruiken',
             'typering': 'Eerst denken, dan schetsen, dan prompten.',
             'wanneer': 'Elke keer dat je AI inzet voor werk dat je oplevert.',
             'oplevering': 'Geen los product. Je AI-gebruik wordt zichtbaar in '
                           'je verantwoording.',
             'docx': '13_Slim-AI-gebruiken.docx', 'pdf': ''},
            {'nummer': 14, 'id': 'reflectie', 'naam': 'Reflectie',
             'typering': 'Terugkijken op je werk met STARR.',
             'wanneer': 'Na een project of een moment dat de moeite waard is om '
                        'op terug te kijken.',
             'oplevering': 'Een uitgewerkte reflectie die je gebruikt in je '
                           'voortgangsgesprek of teamevaluatie.',
             'docx': '14_Reflectie.docx', 'pdf': ''},
        ],
    },
]

# Oude adressen die naar een nieuwe pagina moeten wijzen.
# De clusters heetten eerst anders; bookmarks, links vanuit de app en pagina's
# in iemands browsercache verwijzen nog naar de oude namen. Laat deze staan.
OMLEIDINGEN = {
    'aanpak-kiezen': 'aanpak',
    'bedenken-en-kiezen': 'ontwikkelen',
    'onderbouwen': 'scherpstellen',
    'ai-inzetten': 'doorlopend',
}

# Verwijzingen onderaan de site
VERWIJZINGEN = [
    {'naam': 'AI leren gebruiken',
     'omschrijving': 'De e-learning over AI inzetten in je werk. Het volledige '
                     'verhaal achter hulpmiddel 12 en 13.',
     'url': 'https://fabianb88.github.io/ai-gebruiken-elearning/'},
]
