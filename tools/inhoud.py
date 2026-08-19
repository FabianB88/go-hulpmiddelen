# -*- coding: utf-8 -*-
"""De inhoud van de hulpmiddelensite: clusters en hulpmiddelen, in volgorde.

Dit bestand is de bron. Voeg je een hulpmiddel toe of verplaats je er een, dan
pas je dit bestand aan en draai je `python tools/bouw_site.py` opnieuw.

Per hulpmiddel:
    id          bestandsnaam van de pagina-anker, kleine letters met streepjes
    naam        zoals het op de pagina staat
    typering    één zin: wat is dit
    wanneer     wanneer pak je dit erbij   (leeg = nog in te vullen)
    oplevering  wat heb je als je klaar bent (leeg = nog in te vullen)
    tijd        ruwe tijdsindicatie          (leeg = nog in te vullen)
    docx        bestandsnaam in bestanden/, om in te vullen
    pdf         bestandsnaam in bestanden/, om in de app te lezen

Lege velden worden op de site zichtbaar gemarkeerd als 'nog in te vullen', zodat
er nooit iets verzonnen op de pagina belandt.
"""

TITEL = 'Hulpmiddelen'
ONDERTITEL = 'Werkvormen, canvassen en handleidingen voor Green Office'
INLEIDING = (
    'Losse hulpmiddelen die je erbij pakt wanneer je ze nodig hebt. Elk '
    'hulpmiddel is een Word-bestand dat je invult, met een pdf ernaast om snel '
    'door te lezen. Je hoeft ze niet op volgorde te doen en niet allemaal te '
    'gebruiken.')

CLUSTERS = [
    {
        'id': 'aanpak-kiezen',
        'naam': 'Aanpak kiezen',
        'intro': 'Waarmee je bepaalt hoe je een klus aanvliegt en hoe je '
                 'onderweg bijstuurt.',
        'hulpmiddelen': [
            {'id': 'design-thinking', 'naam': 'Design thinking',
             'typering': 'Een manier van werken waarin je eerst de behoefte '
                         'scherp krijgt en pas daarna een oplossing bedenkt.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'scrum-kanban', 'naam': 'Scrum en kanban',
             'typering': 'Twee manieren om werk in korte rondes te verdelen en '
                         'zichtbaar te houden wie waarmee bezig is.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'reflectie', 'naam': 'Reflectie',
             'typering': 'Terugkijken op wat er gebeurde en daar een volgende '
                         'stap uit halen, in plaats van alleen constateren.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
        ],
    },
    {
        'id': 'verkennen',
        'naam': 'Verkennen',
        'intro': 'Waarmee je in beeld brengt waar je mee te maken hebt voordat '
                 'je iets bedenkt.',
        'hulpmiddelen': [
            {'id': 'stakeholderanalyse', 'naam': 'Stakeholderanalyse',
             'typering': 'In kaart brengen wie er belang bij heeft, hoeveel '
                         'invloed ze hebben en wat dat betekent voor je aanpak.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'ketenschets', 'naam': 'Ketenschets',
             'typering': 'Een schets van de keten of stroom waar je iets in '
                         'wil veranderen, van begin tot eind.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'probleemdefinitie', 'naam': 'Probleemdefinitie',
             'typering': 'Van een vaag ongemak naar een probleem dat je kunt '
                         'aanpakken en waarvan je kunt zien of het opgelost is.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
        ],
    },
    {
        'id': 'bedenken-en-kiezen',
        'naam': 'Bedenken en kiezen',
        'intro': 'Waarmee je van veel mogelijkheden naar één onderbouwde keuze '
                 'gaat.',
        'hulpmiddelen': [
            {'id': 'brainstorm', 'naam': 'Brainstorm',
             'typering': 'Gestructureerd veel ideeën ophalen, zonder ze meteen '
                         'af te schieten.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'prioriteren', 'naam': 'Prioriteren',
             'typering': 'Ideeën of taken tegen elkaar afwegen op criteria die '
                         'je vooraf zelf kiest.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'ce-modellen', 'naam': 'CE-modellen',
             'typering': 'Modellen uit de circulaire economie om een oplossing '
                         'langs te leggen en scherper te krijgen.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
        ],
    },
    {
        'id': 'onderbouwen',
        'naam': 'Onderbouwen',
        'intro': 'Waarmee je aantoont dat je keuze klopt, in plaats van dat je '
                 'hem alleen toelicht.',
        'hulpmiddelen': [
            {'id': 'onderbouwen', 'naam': 'Onderbouwen',
             'typering': 'Vastleggen waarop je je keuzes baseert en welke '
                         'bronnen daaronder liggen.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'testen-en-valideren', 'naam': 'Testen en valideren',
             'typering': 'Je aanname voorleggen aan de werkelijkheid en '
                         'opschrijven wat je eruit leert.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
        ],
    },
    {
        'id': 'ai-inzetten',
        'naam': 'AI inzetten',
        'intro': 'Praktische hulpmiddelen naast de e-learning <i>AI leren '
                 'gebruiken</i>. Die cursus is het volledige verhaal; dit zijn '
                 'de losse werkvormen.',
        'hulpmiddelen': [
            {'id': 'slim-ai-gebruiken', 'naam': 'Slim AI gebruiken',
             'typering': 'Een beknopte werkwijze om AI in je dagelijkse werk in '
                         'te zetten zonder de bekende valkuilen.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
            {'id': 'ai-naar-website', 'naam': 'AI naar website',
             'typering': 'Stap voor stap van een idee naar een werkende '
                         'website, met AI als bouwer.',
             'wanneer': '', 'oplevering': '', 'tijd': '',
             'docx': '', 'pdf': ''},
        ],
    },
]

# Verwijzingen onderaan de site
VERWIJZINGEN = [
    {'naam': 'AI leren gebruiken',
     'omschrijving': 'De e-learning over AI inzetten in je werk. Het volledige '
                     'verhaal achter de twee AI-hulpmiddelen hiernaast.',
     'url': 'https://fabianb88.github.io/ai-gebruiken-elearning/'},
]
