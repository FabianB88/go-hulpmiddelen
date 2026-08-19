# -*- coding: utf-8 -*-
"""De inhoud van de hulpmiddelensite: clusters en hulpmiddelen, in volgorde.

Dit bestand is de bron. Voeg je een hulpmiddel toe of verplaats je er een, dan
pas je dit bestand aan en draai je `python tools/bouw_site.py` opnieuw.

De teksten bij 'typering', 'wanneer' en 'oplevering' komen letterlijk uit de
kopregel van de documenten zelf. Wijzigt een document, neem de nieuwe tekst dan
hier over, zodat site en document hetzelfde zeggen.

LET OP — de nummers zijn vast. De documenten verwijzen onderling naar elkaar met
hun nummer ("zie 09", "prioriteer met 10"). Hernummeren breekt die verwijzingen.
Komt er een hulpmiddel bij, geef het dan nummer 14 en zet het achteraan.

Per hulpmiddel:
    nummer      vast, komt overeen met het bestand
    id          anker in de pagina, kleine letters met streepjes
    naam        zoals het op de pagina en in het document staat
    typering    de ondertitel uit het document
    wanneer     wanneer pak je dit erbij
    oplevering  wat heb je als je klaar bent
    docx        bestandsnaam in bestanden/, om in te vullen
    pdf         bestandsnaam in bestanden/, om door te lezen (leeg = nog niet)
"""

TITEL = 'Hulpmiddelen'
ONDERTITEL = 'Werkvormen, canvassen en handleidingen voor Green Office'
INLEIDING = (
    'Dertien hulpmiddelen die je erbij pakt wanneer je ze nodig hebt. Elk '
    'hulpmiddel is een Word-bestand met uitleg en invulbare onderdelen. De '
    'volgorde volgt de fasen van een project, maar je hoeft ze niet op volgorde '
    'te doen en niet allemaal te gebruiken. Door alle dertien loopt dezelfde '
    'voorbeeldcasus: een terugkerende duurzaamheidsweek die losstaat van het '
    'onderwijs.')

CLUSTERS = [
    {
        'id': 'aanpak',
        'naam': 'Aanpak',
        'intro': 'Waarmee je bepaalt hoe je een klus aanvliegt, richting houdt '
                 'en afspraken maakt met je opdrachtgever.',
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
             'docx': '02_Aanpakplan.docx', 'pdf': ''},
            {'nummer': 3, 'id': 'opdrachtgever-afspraken',
             'naam': 'Opdrachtgever-afspraken',
             'typering': 'De vraag scherp krijgen en een ritme afspreken voor '
                         'goed contact.',
             'wanneer': 'Meteen aan het begin. Het ritme houd je het hele '
                        'project aan.',
             'oplevering': 'Ingevulde intake, vastgelegde afspraken en een '
                           'afstemmingsritme dat je deelt.',
             'docx': '03_Opdrachtgever-afspraken.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'verkennen',
        'naam': 'Verkennen',
        'intro': 'Waarmee je in beeld brengt waar je mee te maken hebt, '
                 'voordat je iets bedenkt.',
        'hulpmiddelen': [
            {'nummer': 4, 'id': 'stakeholderanalyse',
             'naam': 'Stakeholderanalyse',
             'typering': 'In kaart brengen wie belang heeft bij je project en '
                         'wie er invloed op heeft.',
             'wanneer': 'Aan de start, zodra je de vraag kent. Bijwerken als er '
                        'partijen bij komen.',
             'oplevering': 'Een ingevuld grid en een lijst met per partij je '
                           'aanpak.',
             'docx': '04_Stakeholderanalyse.docx', 'pdf': ''},
            {'nummer': 5, 'id': 'ketenschets', 'naam': 'Ketenschets',
             'typering': 'In beeld brengen waar materiaal, geld en informatie '
                         'langsgaan.',
             'wanneer': 'Aan de start, zodra je weet welke stroom je '
                        'onderzoekt.',
             'oplevering': 'Een getekende ketenschets met drie gemarkeerde '
                           'hotspots, plus je aannames.',
             'docx': '05_Ketenschets.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'scherpstellen',
        'naam': 'Scherpstellen',
        'intro': 'Waarmee je van een vage vraag naar een scherp probleem gaat, '
                 'en dat onderbouwd op tafel legt.',
        'hulpmiddelen': [
            {'nummer': 6, 'id': 'probleemdefinitie',
             'naam': 'Probleemdefinitie',
             'typering': 'Van de gevraagde oplossing naar het echte probleem.',
             'wanneer': 'Nadat je de intake en je eerste verkenning hebt '
                        'gedaan.',
             'oplevering': 'Eén scherpe probleemdefinitie en één kansvraag, '
                           'getoetst bij je opdrachtgever.',
             'docx': '06_Probleemdefinitie.docx', 'pdf': ''},
            {'nummer': 7, 'id': 'circulaire-denkmodellen',
             'naam': 'Circulaire denkmodellen',
             'typering': 'Drie modellen om je vraagstuk circulair scherp te '
                         'krijgen.',
             'wanneer': 'Zodra je probleem scherp is, bij het uitwerken van '
                        'richtingen.',
             'oplevering': 'Per model een ingevuld werkblad, dat je gebruikt in '
                           'je projectvoorstel.',
             'docx': '07_Circulaire-denkmodellen.docx', 'pdf': ''},
            {'nummer': 8, 'id': 'projectvoorstel', 'naam': 'Projectvoorstel',
             'typering': 'Je project onderbouwen rond waarom, hoe en wat.',
             'wanneer': 'Nadat je probleemdefinitie staat, en bijwerken tot de '
                        'oplevering.',
             'oplevering': 'Een voorstel waarmee je intern draagvlak, tijd of '
                           'middelen krijgt.',
             'docx': '08_Projectvoorstel.docx', 'pdf': ''},
        ],
    },
    {
        'id': 'ontwikkelen',
        'naam': 'Ontwikkelen',
        'intro': 'Waarmee je van veel mogelijkheden naar één onderbouwde keuze '
                 'gaat.',
        'hulpmiddelen': [
            {'nummer': 9, 'id': 'brainstorm', 'naam': 'Brainstorm',
             'typering': 'Eerst breed denken, dan kiezen.',
             'wanneer': 'Zodra je kansvraag staat en je richtingen zoekt.',
             'oplevering': 'Een gevulde ideeënlijst en een gekozen richting, '
                           'die je prioriteert met 10.',
             'docx': '09_Brainstorm.docx', 'pdf': ''},
            {'nummer': 10, 'id': 'prioriteren', 'naam': 'Prioriteren',
             'typering': 'Kiezen waar je je tijd en energie op zet.',
             'wanneer': 'Na elke brainstorm, en elke keer dat je je planning '
                        'bijstelt.',
             'oplevering': 'Een ingevulde MoSCoW en matrix, vertaald naar je '
                           'aanpakplan.',
             'docx': '10_Prioriteren.docx', 'pdf': ''},
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
            {'nummer': 11, 'id': 'ai-naar-website', 'naam': 'AI naar website',
             'typering': 'Van een schets naar een werkende pagina, zonder te '
                         'coderen.',
             'wanneer': 'Zodra je iets hebt om te tonen: een concept, een '
                        'overzicht of een resultaat.',
             'oplevering': 'Een werkende pagina of prototype, plus je ingevulde '
                           'briefing.',
             'docx': '11_AI-naar-website.docx', 'pdf': ''},
            {'nummer': 12, 'id': 'slim-ai-gebruiken',
             'naam': 'Slim AI gebruiken',
             'typering': 'Eerst denken, dan schetsen, dan prompten.',
             'wanneer': 'Elke keer dat je AI inzet voor werk dat je oplevert.',
             'oplevering': 'Geen los product. Je AI-gebruik wordt zichtbaar in '
                           'je verantwoording.',
             'docx': '12_Slim-AI-gebruiken.docx', 'pdf': ''},
            {'nummer': 13, 'id': 'reflectie', 'naam': 'Reflectie',
             'typering': 'Terugkijken op je werk met STARR.',
             'wanneer': 'Na een project of een moment dat de moeite waard is om '
                        'op terug te kijken.',
             'oplevering': 'Een uitgewerkte reflectie die je gebruikt in je '
                           'voortgangsgesprek of teamevaluatie.',
             'docx': '13_Reflectie.docx', 'pdf': ''},
        ],
    },
]

# Verwijzingen onderaan de site
VERWIJZINGEN = [
    {'naam': 'AI leren gebruiken',
     'omschrijving': 'De e-learning over AI inzetten in je werk. Het volledige '
                     'verhaal achter hulpmiddel 11 en 12.',
     'url': 'https://fabianb88.github.io/ai-gebruiken-elearning/'},
]
