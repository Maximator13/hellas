import type { HistoricalEvent } from './schema.ts'

const HERODOTE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0126'
const THUCYDIDE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0200'
const XENOPHON = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0206'
const PAUSANIAS = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0160'
const DIODORE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0084'
const STRABON = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0198'
const PLUTARQUE = 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives'
const DION = 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio'

export const events: HistoricalEvent[] = [
  {
    "id": "premiers-palais-minoens",
    "title": "Premiers palais de Crète",
    "start": -1949,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique : les premiers palais apparaissent au minoen moyen, vers 1950 à 1900 selon les chronologies.",
    "era": "bronze",
    "track": "minoens",
    "category": "building",
    "importance": 2,
    "placeId": "cnossos",
    "summary": "Vers 1950, de grands palais s'élèvent en Crète, à Cnossos, Phaistos et Malia : autour d'une vaste cour centrale, ils regroupent magasins, ateliers, lieux de culte et archives. Ils marquent la naissance d'une société dirigée par une administration qui écrit, mais dont les textes restent indéchiffrés.",
    "body": "**Des palais autour d'une cour.** Au début du IIe millénaire, les Crétois bâtissent à Cnossos, Phaistos et Malia des ensembles monumentaux organisés autour d'une grande cour centrale. On les appelle « palais » d'après le vocabulaire d'Arthur Evans, qui fouilla Cnossos à partir de 1900 : ce sont à la fois des centres de stockage (grandes jarres, les pithoi), des ateliers, des lieux de culte et de cérémonie.\n\n**Une administration qui écrit.** Les scribes utilisent le hiéroglyphique crétois puis le linéaire A, sur des tablettes d'argile et des scellés. Ces écritures ne sont pas déchiffrées : on reconnaît des chiffres et des signes de denrées, mais ni la langue ni le nom d'un souverain. Le roi Minos des légendes grecques, dont Evans a tiré le mot « minoen », n'est attesté par aucun document.\n\n**Une chronologie relative.** Ces premiers palais sont détruits vers 1700, sans doute par des séismes, puis reconstruits plus vastes. Leurs dates absolues sont tirées de la céramique, d'objets échangés avec l'Égypte et du radiocarbone, avec une marge de plusieurs décennies.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "XIX, 178 et 179 (Minos roi de Cnossos)"
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 4 (la flotte de Minos)",
        "url": `${THUCYDIDE}:book=1:chapter=4`
      },
      {
        "kind": "modern",
        "author": "Cynthia W. Shelmerdine (dir.)",
        "work": "The Cambridge Companion to the Aegean Bronze Age, Cambridge, Cambridge University Press, 2008"
      },
      {
        "kind": "modern",
        "author": "Eric H. Cline (dir.)",
        "work": "The Oxford Handbook of the Bronze Age Aegean, Oxford, Oxford University Press, 2010"
      }
    ]
  },
  {
    "id": "eruption-de-thera",
    "title": "Éruption de Théra",
    "start": -1599,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Date discutée : le radiocarbone donne de 1630 à 1600 environ, la chronologie archéologique (céramique et liens avec l'Égypte) de 1530 à 1500 environ ; les recalibrations récentes rendent possible le XVIe siècle.",
    "era": "bronze",
    "track": "minoens",
    "category": "nature",
    "importance": 1,
    "placeId": "akrotiri",
    "summary": "L'île de Théra (Santorin) explose dans l'une des plus grandes éruptions volcaniques des derniers millénaires et ensevelit la ville d'Akrotiri sous des mètres de ponces et de cendres. Ses habitants avaient fui à temps. La date, vers 1600 ou un siècle plus tard, reste l'un des grands débats de l'archéologie égéenne.",
    "body": "**Une ville sous la cendre.** Akrotiri, port prospère de l'île, vivait en contact étroit avec la Crète minoenne. Des séismes précurseurs ont poussé ses habitants à partir : les fouilles, commencées en 1967 par Spyridon Marinatos, n'ont retrouvé ni victimes ni objets précieux. Les maisons à étages et leurs fresques (le pêcheur, la flottille, les singes bleus) sont conservées sous les dépôts volcaniques.\n\n**Une éruption géante.** L'éruption dite « minoenne » a projeté plusieurs dizaines de kilomètres cubes de roches et agrandi la caldeira de l'île. Ses cendres se retrouvent en Crète, dans le Dodécanèse et en Anatolie, et un tsunami a frappé la côte nord de la Crète.\n\n**La date en débat.** Le radiocarbone d'une branche d'olivier enfouie vivante par l'éruption donne de 1627 à 1600 environ ; la chronologie archéologique, qui rattache la céramique égéenne aux règnes égyptiens, place l'éruption vers 1530 à 1500. Les nouvelles courbes de calibration ont rapproché les deux camps sans trancher. L'éruption n'est plus tenue pour la cause directe du déclin minoen, survenu plusieurs générations plus tard, et rien ne la relie à l'Atlantide de Platon.",
    "sources": [
      {
        "kind": "modern",
        "author": "Walter L. Friedrich et al.",
        "work": "Santorini Eruption Radiocarbon Dated to 1627-1600 B.C., Science, 312, 2006",
        "locus": "p. 548"
      },
      {
        "kind": "modern",
        "author": "Sturt W. Manning",
        "work": "A Test of Time and A Test of Time Revisited: The Volcano of Thera and the Chronology and History of the Aegean and East Mediterranean in the Mid Second Millennium BC, Oxford, Oxbow, 2014"
      },
      {
        "kind": "modern",
        "author": "Charlotte L. Pearson et al.",
        "work": "Annual radiocarbon record indicates 16th century BCE date for the Thera eruption, Science Advances, 4, 8, 2018"
      },
      {
        "kind": "modern",
        "author": "Christos G. Doumas",
        "work": "Thera, Pompeii of the Ancient Aegean, Londres, Thames and Hudson, 1983"
      }
    ]
  },
  {
    "id": "tombes-a-fosse-de-mycenes",
    "title": "Tombes à fosse de Mycènes",
    "start": -1599,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique : cercle B de 1650 à 1550 environ, cercle A de 1600 à 1500 environ ; les noms des défunts sont inconnus.",
    "era": "bronze",
    "track": "myceniens",
    "category": "society",
    "importance": 2,
    "placeId": "cercle-a-de-mycenes",
    "summary": "Au XVIe siècle, des chefs de Mycènes se font enterrer dans des tombes creusées dans le roc, regroupées dans deux enclos circulaires, avec des armes, des vases et des masques d'or. Ces sépultures annoncent la puissance des royaumes mycéniens, les premiers États de langue grecque.",
    "body": "**Deux cercles de tombes.** Le cercle B, hors de la future enceinte, réunit des tombes de 1650 à 1550 environ ; le cercle A, fouillé par Heinrich Schliemann en 1876, des tombes de 1600 à 1500 environ. Chaque tombe est un puits creusé dans le roc où plusieurs défunts ont été déposés au fil du temps. Le cercle A a livré une masse d'objets d'or sans équivalent en Grèce à cette époque : masques funéraires, coupes, bijoux, épées et poignards incrustés.\n\n**Le « masque d'Agamemnon ».** Schliemann crut avoir trouvé le visage du roi de l'*Iliade*. Les tombes sont en réalité plus anciennes d'environ trois siècles que la date donnée par les Grecs à la guerre de Troie. L'authenticité du masque a été contestée, mais la plupart des spécialistes la tiennent pour assurée.\n\n**Pourquoi c'est important.** Ces richesses, souvent faites de matières importées comme l'ambre de la Baltique, montrent une élite guerrière qui s'enrichit vite. Ses successeurs bâtiront, à partir du XIVe siècle, les palais et les murs cyclopéens de Mycènes. Les noms de ces chefs restent inconnus : les tablettes en linéaire B sont plus tardives.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Iliade",
        "locus": "II, 569 à 580 (le contingent de Mycènes)"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 16, 6 et 7 (les tombes d'Atrée et d'Agamemnon)",
        "url": `${PAUSANIAS}:book=2:chapter=16`
      },
      {
        "kind": "modern",
        "author": "Oliver Dickinson",
        "work": "The Aegean Bronze Age, Cambridge, Cambridge University Press, 1994"
      },
      {
        "kind": "modern",
        "author": "Cynthia W. Shelmerdine (dir.)",
        "work": "The Cambridge Companion to the Aegean Bronze Age, Cambridge, Cambridge University Press, 2008"
      }
    ]
  },
  {
    "id": "dispute-d-athena-et-de-poseidon",
    "title": "Athéna et Poséidon se disputent l'Attique",
    "start": -1581,
    "precision": "century",
    "certainty": "legendary",
    "certaintyNote": "Récit légendaire, placé sous le règne de Cécrops, que le Marbre de Paros (entrée A 1) fait commencer en 1582/1 ; le Marbre date aussi de 1532/1 (entrée A 3) le premier procès de l'Aréopage, entre Arès et Poséidon.",
    "era": "bronze",
    "track": "mythes",
    "category": "religion",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "cecrops"
    ],
    "summary": "Sous Cécrops, premier roi d'Athènes, Athéna et Poséidon se disputent l'Attique. Poséidon frappe le rocher de l'Acropole et fait jaillir une source d'eau salée ; Athéna fait pousser le premier olivier. L'olivier est jugé le plus beau présent : la déesse devient la protectrice de la cité, qui porte son nom.",
    "body": "**Le mythe.** Selon Apollodore, Poséidon arrive le premier sur l'Acropole et, d'un coup de trident, fait jaillir une « mer » d'eau salée ; Athéna plante un olivier, en prenant Cécrops à témoin. Les douze dieux, ou selon d'autres Cécrops lui-même, attribuent le pays à Athéna. Furieux, Poséidon inonde la plaine de Thria.\n\n**Un mythe civique.** À l'époque classique, les Athéniens montraient encore dans l'Érechthéion l'olivier sacré et l'eau de mer laissée par le dieu, que mentionne Hérodote : brûlé par les Perses en 480, l'olivier aurait aussitôt repoussé. Le fronton ouest du Parthénon, sculpté entre 438 et 432, représentait la dispute face à ceux qui montaient à l'Acropole ; ses figures, très mutilées, sont connues par des fragments et par des dessins faits en 1674, avant l'explosion de 1687.\n\n**Ce que montre l'archéologie.** L'Acropole était bien habitée et fortifiée à l'âge du bronze : un rempart cyclopéen y est élevé au XIIIe siècle, et un palais mycénien y a sans doute existé, mais ses traces sont maigres. Le mythe explique des noms et des cultes de la cité (Athéna Poliade, Poséidon Érechthée), il ne garde le souvenir d'aucun événement ; la date de Cécrops est un calcul des chronographes, qui comptaient les générations de rois légendaires.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VIII, 55",
        "url": `${HERODOTE}:book=8:chapter=55`
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "III, 14, 1"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 24, 5 (le fronton ouest du Parthénon)",
        "url": `${PAUSANIAS}:book=1:chapter=24`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 1 et 3"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      },
      {
        "kind": "modern",
        "author": "Jeffrey M. Hurwit",
        "work": "The Athenian Acropolis: History, Mythology, and Archaeology from the Neolithic Era to the Present, Cambridge, Cambridge University Press, 1999"
      }
    ]
  },
  {
    "id": "deluge-de-deucalion",
    "title": "Le déluge de Deucalion",
    "start": -1528,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date du Marbre de Paros, entrée A 4 (1529/8), selon laquelle Deucalion fuit les pluies de Lycoréia pour se réfugier à Athènes ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "nature",
    "importance": 2,
    "placeId": "parnasse",
    "people": [
      "deucalion"
    ],
    "summary": "Zeus veut anéantir les hommes de l'âge de bronze et noie la Grèce sous un déluge. Prévenu par son père Prométhée, Deucalion se sauve avec sa femme Pyrrha dans un coffre qui flotte neuf jours avant d'aborder au Parnasse. Le couple repeuple la terre en jetant des pierres par-dessus son épaule : elles deviennent des hommes et des femmes.",
    "body": "**Le mythe.** Selon Apollodore, Deucalion, fils de Prométhée et roi de Phthie, construit un coffre (larnax) sur le conseil de son père. Après neuf jours et neuf nuits, il aborde au Parnasse et sacrifie à Zeus, puis, sur l'ordre des dieux, jette avec Pyrrha des pierres derrière lui : celles de Deucalion deviennent des hommes, celles de Pyrrha des femmes. Leur fils Hellen donne son nom aux Hellènes.\n\n**Un ancêtre commun.** Le récit ouvre les généalogies grecques : par Hellen et ses fils Doros, Éolos et Xouthos, père d'Ion, tous les peuples grecs descendent de Deucalion. Les Athéniens montraient dans l'enceinte de Zeus Olympien une fissure où les eaux se seraient écoulées, et le Marbre de Paros attribue à Deucalion, réfugié à Athènes, la fondation de ce sanctuaire. Lycoréia, sur le Parnasse, se disait fondée par des rescapés guidés par des hurlements de loups.\n\n**Ce qu'on peut en dire.** Le motif rappelle les récits mésopotamiens du déluge (Atrahasis, l'épopée de Gilgamesh), bien plus anciens, dont il dérive sans doute en partie ; il ne renvoie à aucune catastrophe identifiable, et les rapprochements avec l'éruption de Théra restent des hypothèses sans preuve. Le Marbre de Paros, gravé en 264/3, en fait pourtant un événement daté, pour mettre en ordre le passé grec.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "I, 7, 2"
      },
      {
        "kind": "ancient",
        "author": "Pindare",
        "work": "Olympiques",
        "locus": "IX, 41 à 53"
      },
      {
        "kind": "ancient",
        "author": "Ovide",
        "work": "Métamorphoses",
        "locus": "I, 253 à 415"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 18, 7 et X, 6, 2",
        "url": `${PAUSANIAS}:book=1:chapter=18`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 2 et 4"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      },
      {
        "kind": "modern",
        "author": "Martin L. West",
        "work": "The East Face of Helicon: West Asiatic Elements in Greek Poetry and Myth, Oxford, Clarendon Press, 1997"
      }
    ]
  },
  {
    "id": "cadmos-fonde-thebes",
    "title": "Cadmos fonde Thèbes",
    "start": -1518,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date du Marbre de Paros, entrée A 7 (1519/8) ; la Chronique d'Eusèbe, dans la version de Jérôme, place Cadmos un siècle plus tard, entre 1430 et 1400 environ ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "politics",
    "importance": 2,
    "placeId": "thebes",
    "people": [
      "cadmos"
    ],
    "summary": "Parti de Phénicie à la recherche de sa sœur Europe, enlevée par Zeus, Cadmos suit une vache jusqu'en Béotie et fonde là où elle se couche la citadelle de Thèbes, la Cadmée. Il tue le dragon d'Arès, dont les dents semées font naître les Spartes, ancêtres des Thébains. Hérodote lui attribue l'introduction en Grèce des lettres phéniciennes.",
    "body": "**Le mythe.** Fils d'Agénor, roi de Tyr ou de Sidon, Cadmos cherche Europe en vain ; l'oracle de Delphes lui ordonne de suivre une vache et de fonder une ville à l'endroit où elle se couchera. Il y tue le dragon qui garde une source et sème ses dents sur le conseil d'Athéna : des guerriers armés en sortent et s'entretuent, et les cinq survivants, les Spartes (« hommes semés »), sont les ancêtres des grandes familles thébaines. Cadmos épouse Harmonie, fille d'Arès et d'Aphrodite.\n\n**Les usages.** Les Thébains se disaient « Cadméens » et montraient la maison de Cadmos sur leur acropole. Hérodote affirme que les Phéniciens venus avec lui apprirent l'alphabet aux Grecs, et dit avoir vu à Thèbes des inscriptions en « lettres cadméennes ». La tragédie athénienne (Euripide, *Les Bacchantes* et *Les Phéniciennes*) fait de sa descendance une suite de malheurs, de Penthée à Œdipe.\n\n**Ce que montre l'archéologie.** La Cadmée porte bien un palais mycénien : on y a trouvé des tablettes en linéaire B et, en 1963 et 1964, un lot de sceaux-cylindres orientaux en lapis-lazuli, venus de Mésopotamie et du Levant. Ils prouvent des contacts avec l'Orient, pas une colonie phénicienne. L'alphabet grec n'est adopté qu'au VIIIe siècle, bien après la date des chronographes : la tradition a prêté à un fondateur unique un emprunt beaucoup plus tardif.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 57 à 61",
        "url": `${HERODOTE}:book=5:chapter=58`
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "III, 4, 1 et 2"
      },
      {
        "kind": "ancient",
        "author": "Euripide",
        "work": "Les Phéniciennes",
        "locus": "638 à 675"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "IX, 5, 1 à 3",
        "url": `${PAUSANIAS}:book=9:chapter=5`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 7"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      },
      {
        "kind": "modern",
        "author": "Vassilis L. Aravantinos, Louis Godart et Anna Sacconi",
        "work": "Thèbes. Fouilles de la Cadmée I. Les tablettes en linéaire B de la odos Pelopidou, Pise et Rome, 2001"
      }
    ]
  },
  {
    "id": "danaos-arrive-a-argos",
    "title": "Danaos et les Danaïdes arrivent à Argos",
    "start": -1510,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date du Marbre de Paros, entrée A 9 (1511/0), qui mentionne le premier navire à cinquante rames venu d'Égypte ; Eusèbe et Jérôme placent le règne de Danaos à Argos vers 1475 ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "politics",
    "importance": 3,
    "placeId": "argos",
    "people": [
      "danaos"
    ],
    "summary": "Fuyant son frère Égyptos, Danaos quitte l'Égypte avec ses cinquante filles sur le premier navire à cinquante rames et devient roi d'Argos. Forcées d'épouser les cinquante fils d'Égyptos, les Danaïdes les tuent la nuit des noces, sauf Hypermnestre, qui épargne Lyncée. Chez Homère, les Grecs sont souvent appelés « Danaens ».",
    "body": "**Le mythe.** Danaos et Égyptos sont deux frères, descendants d'Io. Menacé, Danaos s'enfuit avec ses filles, fait escale à Lindos, à Rhodes, où les Danaïdes fondent un temple d'Athéna, puis aborde en Argolide ; les Argiens lui donnent le trône. Les fils d'Égyptos le poursuivent et exigent le mariage : quarante-neuf épouses tuent leur mari. Lyncée, épargné, succède à Danaos, et de lui descendent Acrisios, Danaé et Persée.\n\n**Les usages.** Eschyle consacre aux Danaïdes une trilogie, dont seules *Les Suppliantes* sont conservées. Les Argiens attribuaient à Danaos le temple d'Apollon Lycien de leur ville et rattachaient à ses filles leurs sources : Amymone, l'une d'elles, aurait obtenu de Poséidon les eaux de Lerne. Une tradition plus tardive montre les Danaïdes, aux Enfers, condamnées à remplir un tonneau percé.\n\n**Ce que montre l'archéologie.** Argos est habitée à l'époque mycénienne (colline de l'Aspis, Larissa, tombes de la Deiras), mais les grands centres de l'Argolide sont alors Mycènes et Tirynthe. Une liste égyptienne du temps d'Amenhotep III (vers 1370) mentionne un pays « Tanaja », que certains rapprochent des Danaens ; l'hypothèse est discutée. Le mythe dit surtout comment les Grecs pensaient leurs liens anciens avec l'Égypte.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Eschyle",
        "work": "Les Suppliantes"
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "II, 1, 4 et 5"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 19, 3 à 6",
        "url": `${PAUSANIAS}:book=2:chapter=19`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 182 (le temple de Lindos)",
        "url": `${HERODOTE}:book=2:chapter=182`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 9"
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 66 à 69"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "thesee-et-le-minotaure",
    "title": "Thésée et le Minotaure",
    "start": -1294,
    "end": -1258,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Dates du Marbre de Paros : entrée A 19 (1295/4), où Athènes, frappée par la famine, doit accepter le châtiment exigé par Minos, et entrée A 20 (1259/8), avènement de Thésée ; Eusèbe et Jérôme placent le Minotaure vers 1232 ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "politics",
    "importance": 1,
    "placeId": "cnossos",
    "people": [
      "minos",
      "thesee",
      "ariane"
    ],
    "summary": "Pour venger son fils Androgée, tué en Attique, Minos, roi de Cnossos, impose à Athènes un tribut de sept jeunes gens et sept jeunes filles, livrés au Minotaure, monstre à tête de taureau enfermé dans le Labyrinthe construit par Dédale. Thésée part avec eux, tue le monstre et ressort grâce au fil d'Ariane ; à son retour, il devient roi d'Athènes.",
    "body": "**Le mythe.** Pasiphaé, épouse de Minos, s'est unie au taureau envoyé par Poséidon et a donné naissance au Minotaure. Quand Athènes doit livrer son tribut, Thésée, fils du roi Égée, se joint aux victimes. Ariane, fille de Minos, lui donne une pelote de fil pour retrouver la sortie, puis s'enfuit avec lui ; il l'abandonne à Naxos. Au retour, il oublie de hisser la voile blanche convenue : Égée, se croyant privé de son fils, se jette dans la mer, et Thésée devient roi.\n\n**Un héros pour Athènes.** À partir de la fin du VIe siècle, Thésée devient le héros national d'Athènes, rival d'Héraclès : on lui attribue la réunion des villages de l'Attique en une seule cité. En 476/5, Cimon rapporte de Skyros des ossements présentés comme les siens, et les Athéniens conservèrent jusqu'à l'époque hellénistique un navire dit de Thésée, sans cesse réparé.\n\n**Ce que montre l'archéologie.** Le palais de Cnossos, fouillé par Arthur Evans à partir de 1900, frappe par son plan complexe, ses fresques de sauts par-dessus le taureau et ses cornes de consécration. Une tablette en linéaire B de Cnossos (KN Gg 702) note une offrande de miel à la « Maîtresse du labyrinthe » : le mot existait donc à l'âge du bronze. Le lien avec la labrys, la double hache, est une hypothèse ancienne et discutée, et rien n'atteste un tribut athénien ; Thucydide voyait dans Minos le souvenir d'une puissance maritime crétoise.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "XI, 321 à 325 (Ariane)"
      },
      {
        "kind": "ancient",
        "author": "Bacchylide",
        "work": "Dithyrambes",
        "locus": "17"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Thésée",
        "locus": "15 à 23 et 36",
        "url": `${PLUTARQUE}/Theseus*.html`
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "III, 15, 7 et 8 ; Épitomé, I, 7 à 11"
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 4 et II, 15",
        "url": `${THUCYDIDE}:book=2:chapter=15`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 19 et 20"
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 92"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      },
      {
        "kind": "modern",
        "author": "Henry J. Walker",
        "work": "Theseus and Athens, Oxford, Oxford University Press, 1995"
      }
    ]
  },
  {
    "id": "persee-fonde-mycenes",
    "title": "Persée tue la Gorgone et fonde Mycènes",
    "start": -1306,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date de la Chronique d'Eusèbe dans la version latine de Jérôme, qui place vers 1307 le règne de Persée après la mort accidentelle d'Acrisios, et ses exploits vers 1347 à 1330 ; les parties conservées du Marbre de Paros ne le mentionnent pas ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "politics",
    "importance": 2,
    "placeId": "mycenes",
    "people": [
      "persee"
    ],
    "summary": "Fils de Zeus et de Danaé, Persée tranche la tête de la Gorgone Méduse, dont le regard change les hommes en pierre, puis sauve Andromède d'un monstre marin. Il tue ensuite par accident son grand-père Acrisios, roi d'Argos ; honteux d'hériter de sa victime, il échange Argos contre Tirynthe et, selon Pausanias, fonde Mycènes.",
    "body": "**Le mythe.** Un oracle a prédit à Acrisios que son petit-fils le tuerait : il enferme sa fille Danaé, que Zeus rejoint sous forme d'une pluie d'or, puis jette la mère et l'enfant à la mer dans un coffre. Devenu adulte à Sériphos, Persée part chercher la tête de Méduse, avec l'aide d'Athéna et d'Hermès ; du cou tranché naissent Pégase et Chrysaor. Lors de jeux à Larissa, son disque tue Acrisios, accomplissant l'oracle.\n\n**Les usages.** Persée est l'ancêtre des rois de Mycènes et de Tirynthe, et le bisaïeul d'Héraclès. Pausanias rapporte deux explications du nom de Mycènes : le bout du fourreau (mykès) de Persée y serait tombé, ou il y aurait cueilli un champignon pour boire l'eau d'une source, la Perseia. Hérodote dit que les rois perses se réclamaient de Persée, dont le fils Persès aurait donné son nom à leur peuple ; Méduse est un sujet favori des peintres de vases et des frontons archaïques.\n\n**Ce que montre l'archéologie.** Mycènes est occupée bien avant la date de Jérôme : ses tombes à fosse remontent au XVIe siècle. Le rempart cyclopéen et la porte des Lions datent du milieu du XIIIe siècle, et une citerne souterraine creusée à la fin du même siècle était alimentée par une source extérieure, peut-être la Perseia de Pausanias. Aucun document de l'époque ne nomme un fondateur.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hésiode",
        "work": "Théogonie",
        "locus": "270 à 283"
      },
      {
        "kind": "ancient",
        "author": "Pindare",
        "work": "Pythiques",
        "locus": "XII, 6 à 26"
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "II, 4, 1 à 5"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 16, 3 à 6",
        "url": `${PAUSANIAS}:book=2:chapter=16`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VII, 61 et 150",
        "url": `${HERODOTE}:book=7:chapter=150`
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 80 à 85"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "expedition-des-argonautes",
    "title": "L'expédition des Argonautes",
    "start": -1266,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date de la Chronique d'Eusèbe dans la version latine de Jérôme, qui place le voyage des Argonautes vers 1267 ; les parties conservées du Marbre de Paros ne le datent pas ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "culture",
    "importance": 1,
    "placeId": "iolcos",
    "people": [
      "jason",
      "medee",
      "heracles"
    ],
    "summary": "Pour reprendre le trône d'Iolcos, Jason doit rapporter la Toison d'or de Colchide, au bout de la mer Noire. Avec les héros de sa génération, dont Héraclès, Orphée et les Dioscures, il embarque sur l'Argo, franchit les Roches qui s'entrechoquent et, grâce à la magicienne Médée, fille du roi Aiétès, s'empare de la Toison.",
    "body": "**Le mythe.** Pélias, qui a usurpé le trône d'Iolcos, envoie son neveu Jason chercher la toison du bélier d'or. Le navire passe par Lemnos, Cyzique et le Bosphore, où le devin Phinée, délivré des Harpies, indique la route entre les Roches Cyanées. En Colchide, Jason doit atteler des taureaux qui crachent le feu et semer des dents de dragon ; Médée, éprise de lui, l'aide par ses drogues, endort le serpent gardien et s'enfuit avec lui. De retour, elle fait périr Pélias par ses propres filles.\n\n**Les usages.** L'*Odyssée* parle déjà de l'Argo « que tous chantent ». Pindare raconte le voyage en 462 pour un roi de Cyrène, cité dont la fondation est rattachée à un Argonaute ; Euripide fait de Médée, abandonnée à Corinthe, la meurtrière de ses enfants (431). Au IIIe siècle, à Alexandrie, Apollonios de Rhodes en tire une épopée savante, les *Argonautiques*. Les Grecs installés au bord de la mer Noire à partir du VIIe siècle retrouvaient dans ce récit la route de leurs colonies.\n\n**Ce que montre l'archéologie.** Autour de Volos, en Thessalie, la colline du Kastro et le site voisin de Dimini, avec ses grands bâtiments mycéniens, sont des candidats pour Iolcos ; l'identification reste débattue. La Colchide correspond à l'ouest de la Géorgie, riche en or : Strabon explique la toison par des peaux de mouton qui servaient à recueillir les paillettes des torrents, une rationalisation antique plutôt qu'une preuve.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "XII, 69 à 72"
      },
      {
        "kind": "ancient",
        "author": "Pindare",
        "work": "Pythiques",
        "locus": "IV"
      },
      {
        "kind": "ancient",
        "author": "Euripide",
        "work": "Médée"
      },
      {
        "kind": "ancient",
        "author": "Apollonios de Rhodes",
        "work": "Argonautiques",
        "locus": "I à IV"
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "I, 9, 16 à 28"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XI, 2, 19",
        "url": `${STRABON}:book=11:chapter=2:section=19`
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 88"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "travaux-d-heracles",
    "title": "Les travaux d'Héraclès",
    "start": -1244,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date de la Chronique d'Eusèbe dans la version latine de Jérôme, qui place vers 1245 la fin des travaux d'Héraclès et sa mort vers 1196 ; la liste canonique des douze travaux n'est fixée qu'au Ve siècle ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "culture",
    "importance": 1,
    "placeId": "tirynthe",
    "people": [
      "heracles",
      "eurysthee"
    ],
    "summary": "Fils de Zeus et d'Alcmène, Héraclès est poursuivi par la haine d'Héra. Frappé de folie, il tue ses enfants et doit, pour expier, servir son cousin Eurysthée, roi de Mycènes et de Tirynthe, qui lui impose une série d'épreuves : le lion de Némée, l'hydre de Lerne, les écuries d'Augias, les oiseaux du lac Stymphale, jusqu'à la capture de Cerbère aux Enfers.",
    "body": "**Le mythe.** Dans l'*Iliade*, Héra retarde la naissance d'Héraclès pour qu'Eurysthée, né avant lui, obtienne la royauté promise par Zeus. Selon Apollodore, la Pythie ordonne au héros de servir Eurysthée à Tirynthe pendant douze ans : aux dix travaux prévus s'en ajoutent deux, le roi refusant d'en compter deux. Les douze sont le lion de Némée, l'hydre, la biche de Cérynie, le sanglier d'Érymanthe, Augias, les oiseaux du Stymphale, le taureau de Crète, les juments de Diomède, la ceinture de l'Amazone, les bœufs de Géryon, les pommes des Hespérides et Cerbère. Mort sur un bûcher au mont Œta, Héraclès est accueilli parmi les dieux.\n\n**Le héros de tous les Grecs.** C'est le héros le plus représenté de l'art grec ; les métopes du temple de Zeus à Olympie, vers 460, montrent la plus ancienne série complète des douze travaux. On lui attribuait la fondation des jeux Olympiques, et les rois de Sparte comme ceux de Macédoine, jusqu'à Alexandre, se disaient ses descendants. Il recevait à la fois un culte de héros et un culte de dieu, ce qui intriguait déjà Hérodote.\n\n**Ce que montre l'archéologie.** Les murailles de Tirynthe, faites de blocs énormes que Pausanias attribuait aux Cyclopes, et son palais datent pour l'essentiel du XIIIe siècle. Plusieurs travaux s'attachent à des paysages réels du Péloponnèse (Némée, le marais de Lerne, le lac Stymphale). Rien, en revanche, ne permet de remonter à un personnage réel derrière ce héros composite.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Iliade",
        "locus": "XIX, 95 à 133"
      },
      {
        "kind": "ancient",
        "author": "Hésiode",
        "work": "Théogonie",
        "locus": "313 à 332"
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "II, 4, 8 à II, 7, 7"
      },
      {
        "kind": "ancient",
        "author": "Sophocle",
        "work": "Les Trachiniennes"
      },
      {
        "kind": "ancient",
        "author": "Euripide",
        "work": "Héraclès"
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 44",
        "url": `${HERODOTE}:book=2:chapter=44`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 25, 8 et V, 10, 9",
        "url": `${PAUSANIAS}:book=5:chapter=10`
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 90 et 96"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "oedipe-et-les-sept-contre-thebes",
    "title": "Œdipe et les Sept contre Thèbes",
    "start": -1260,
    "end": -1250,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Dates antiques : Eusèbe et Jérôme placent le Sphinx et Œdipe vers 1261 ; le Marbre de Paros (entrée A 22) date de 1251/0 l'expédition d'Adraste contre Thèbes et la fondation des jeux Néméens, que Jérôme met vers 1234 ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "war",
    "importance": 1,
    "placeId": "thebes",
    "people": [
      "oedipe",
      "polynice",
      "adraste"
    ],
    "summary": "Abandonné à sa naissance parce qu'un oracle annonçait qu'il tuerait son père, Œdipe tue sans le savoir le roi Laïos, délivre Thèbes du Sphinx et épouse la reine Jocaste, sa mère. La vérité découverte, il se crève les yeux. Ses fils se disputent le trône : Polynice revient avec six chefs menés par Adraste, roi d'Argos, et les deux frères s'entretuent devant les portes de Thèbes.",
    "body": "**Le mythe.** Exposé sur le Cithéron, Œdipe est élevé à Corinthe. Sur la route de Delphes, il tue un inconnu, Laïos ; à Thèbes, il résout l'énigme du Sphinx et reçoit la main de la reine. Après sa chute, Étéocle refuse de céder le pouvoir à son frère. Les Sept (Adraste, Polynice, Tydée, Capanée, Amphiaraos, Hippomédon, Parthénopée) attaquent chacun une des sept portes et périssent tous, sauf Adraste ; Antigone ensevelit Polynice malgré l'interdiction de Créon. Dix ans plus tard, leurs fils, les Épigones, prennent la ville.\n\n**Une matière pour la tragédie.** Homère connaît déjà la mère et épouse d'Œdipe, qu'il nomme Épicaste, et l'expédition de Tydée. Des épopées perdues, l'*Œdipodie* et la *Thébaïde*, ont nourri les tragiques : Eschyle (*Les Sept contre Thèbes*, 467), Sophocle (*Antigone*, *Œdipe roi*, *Œdipe à Colone*), Euripide (*Les Phéniciennes*). Aristote prend *Œdipe roi* pour modèle de la tragédie. Les Athéniens se flattaient que Thésée eût obtenu la sépulture des Sept, dont ils montraient les tombes à Éleusis.\n\n**Ce que montre l'archéologie.** Le palais mycénien de la Cadmée, riche en tablettes en linéaire B, est détruit par un incendie au XIIIe siècle, à une date discutée. Certains y ont vu le souvenir de la guerre des Sept ou des Épigones ; rien ne permet de le confirmer. Les sept portes que décrit Pausanias sont celles de la ville classique, et leur nombre semble autant poétique que topographique.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "XI, 271 à 280"
      },
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Iliade",
        "locus": "IV, 376 à 398"
      },
      {
        "kind": "ancient",
        "author": "Eschyle",
        "work": "Les Sept contre Thèbes"
      },
      {
        "kind": "ancient",
        "author": "Sophocle",
        "work": "Œdipe roi ; Antigone"
      },
      {
        "kind": "ancient",
        "author": "Euripide",
        "work": "Les Phéniciennes"
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "III, 5, 7 à III, 7, 2"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "IX, 5, 10 à 12 et IX, 8, 4 à 7",
        "url": `${PAUSANIAS}:book=9:chapter=8`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 22"
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 88 et 90"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "destruction-des-palais-myceniens",
    "title": "Destruction des palais mycéniens",
    "start": -1199,
    "end": -1179,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Destructions attestées par l'archéologie, mais étalées selon les sites et datées à quelques décennies près ; leurs causes restent débattues.",
    "era": "bronze",
    "track": "myceniens",
    "category": "society",
    "importance": 1,
    "placeId": "mycenes",
    "summary": "Vers 1200, les palais mycéniens (Mycènes, Tirynthe, Pylos, Thèbes) sont incendiés ou abandonnés en quelques décennies, comme d'autres grands centres de la Méditerranée orientale. Le système palatial et l'écriture linéaire B disparaissent. Les causes de cet effondrement (séismes, raids, révoltes, rupture des échanges) restent discutées.",
    "body": "**Ce que montrent les fouilles.** Pylos brûle, et l'incendie cuit les tablettes d'argile de ses archives, qui nous sont ainsi parvenues ; Mycènes et Tirynthe subissent des destructions répétées, Thèbes est incendiée. Les archéologues datent ces niveaux de la fin de l'helladique récent IIIB, de 1200 à 1180 environ, avec des écarts de plusieurs décennies d'un site à l'autre. À la même époque, Ougarit, en Syrie, est détruite et l'empire hittite s'effondre.\n\n**Des causes multiples.** Les hypothèses se combinent : séismes (traces à Mycènes et à Tirynthe), attaques venues de la mer (les « Peuples de la mer » des inscriptions de Ramsès III en Égypte), révoltes contre des palais très centralisés, sécheresses, rupture des circuits qui apportaient le cuivre et l'étain. Aucune n'explique tout à elle seule.\n\n**La suite.** La vie continue sur plusieurs sites pendant l'helladique récent IIIC (la ville basse de Tirynthe est même agrandie), mais sans palais ni écriture, et la population baisse fortement. Les Grecs plus tardifs ont gardé le souvenir d'un âge héroïque, suivi d'un « retour des Héraclides » et d'une migration dorienne dont l'archéologie ne trouve pas de trace nette.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 12 (migrations après la guerre de Troie)",
        "url": `${THUCYDIDE}:book=1:chapter=12`
      },
      {
        "kind": "ancient",
        "author": "Ramsès III",
        "work": "Inscription de l'an 8, temple de Médinet Habou (les Peuples de la mer)"
      },
      {
        "kind": "modern",
        "author": "Cynthia W. Shelmerdine (dir.)",
        "work": "The Cambridge Companion to the Aegean Bronze Age, Cambridge, Cambridge University Press, 2008"
      },
      {
        "kind": "modern",
        "author": "Eric H. Cline",
        "work": "1177 avant J.-C. Le jour où la civilisation s'est effondrée, Paris, La Découverte, 2015"
      }
    ]
  },
  {
    "id": "jugement-de-paris-et-enlevement-d-helene",
    "title": "Le jugement de Pâris et l'enlèvement d'Hélène",
    "start": -1194,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date déduite : peu avant les dix ans de guerre comptés à partir de la prise de Troie selon Ératosthène (1184/3), date suivie par ce site. Eusèbe et Jérôme placent l'enlèvement vers 1191, le Marbre de Paros (entrée A 23) le départ des Grecs en 1218/7 ; dans l'Iliade, Hélène dit être partie depuis vingt ans ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "war",
    "importance": 2,
    "placeId": "sparte",
    "people": [
      "paris",
      "helene",
      "menelas"
    ],
    "summary": "Aux noces de Pélée et de Thétis, Éris, la Discorde, lance une pomme d'or destinée à la plus belle. Choisi pour juger entre Héra, Athéna et Aphrodite, le prince troyen Pâris donne la pomme à Aphrodite, qui lui promet la plus belle des femmes : Hélène, épouse de Ménélas, roi de Sparte. Pâris l'emmène à Troie, et les princes grecs, liés par un serment, partent la reprendre.",
    "body": "**Le mythe.** Le récit était celui des *Chants cypriens*, une épopée perdue connue par un résumé antique ; l'*Iliade* n'y fait qu'une allusion. Les anciens prétendants d'Hélène avaient juré de défendre son époux. Reçu en hôte à Sparte, Pâris profite d'un voyage de Ménélas en Crète pour partir avec Hélène et des trésors ; Ménélas et son frère Agamemnon rassemblent alors l'armée grecque à Aulis.\n\n**Coupable ou victime ?** Les Grecs ont beaucoup discuté de la responsabilité d'Hélène. Le poète Stésichore, selon la légende, perdit la vue pour l'avoir accusée et la retrouva en se rétractant ; Euripide, dans *Hélène* (412), et Hérodote rapportent une version où la vraie Hélène reste en Égypte pendant que les Grecs se battent pour un fantôme. Le jugement de Pâris est l'un des sujets favoris des peintres de vases. À Sparte, Hélène était honorée comme une déesse.\n\n**Ce que montre l'archéologie.** Au Ménélaion de Thérapné, près de Sparte, un sanctuaire d'Hélène et de Ménélas, actif à partir de 700 environ, a livré des dédicaces à Hélène ; il domine les restes d'une grande demeure mycénienne. Depuis 2009, les fouilles d'Ayios Vasileios, au sud de Sparte, ont mis au jour un palais avec des tablettes en linéaire B, centre de la Laconie mycénienne. Aucun de ces textes ne nomme Ménélas ou Hélène.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Iliade",
        "locus": "XXIV, 25 à 30 et 765 et 766"
      },
      {
        "kind": "ancient",
        "author": "Proclos",
        "work": "Chrestomathie (résumé des Chants cypriens)"
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "III, 10, 9 ; Épitomé, III, 1 à 6"
      },
      {
        "kind": "ancient",
        "author": "Euripide",
        "work": "Hélène"
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 112 à 120 et VI, 61",
        "url": `${HERODOTE}:book=2:chapter=112`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 23"
      },
      {
        "kind": "ancient",
        "author": "Eusèbe de Césarée et Jérôme",
        "work": "Chronique, version latine de Jérôme (éd. R. Helm)",
        "locus": "p. 96"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "guerre-de-troie",
    "title": "Guerre de Troie",
    "start": -1193,
    "end": -1183,
    "precision": "year",
    "certainty": "legendary",
    "certaintyNote": "Récit légendaire. Les Anciens proposaient des dates allant de 1334 (Douris de Samos) à 1184/1183 (Ératosthène) ; le site suit Ératosthène, avec dix ans de siège.",
    "era": "bronze",
    "track": "mythes",
    "category": "war",
    "importance": 2,
    "placeId": "troie",
    "people": [
      "agamemnon",
      "homere"
    ],
    "summary": "Selon l'Iliade et la tradition, une coalition de rois grecs menée par Agamemnon, roi de Mycènes, assiège Troie pendant dix ans pour reprendre Hélène, puis prend la ville par la ruse du cheval de bois. Le récit est légendaire ; la date retenue ici est celle que calcula Ératosthène au IIIe siècle av. J.-C.",
    "body": "**Le récit.** L'*Iliade*, composée vers le VIIIe ou le VIIe siècle, raconte quelques semaines de la dixième année du siège ; la chute de la ville, avec le cheval de bois, est évoquée dans l'*Odyssée* et contée dans des poèmes aujourd'hui perdus. Pour les Grecs, cette guerre était un fait historique et le point de départ de leur chronologie.\n\n**Les dates antiques.** Faute de documents, les savants grecs l'ont datée en comptant les générations : Douris de Samos proposait 1334, Hérodote un peu plus de huit siècles avant son temps, soit vers 1250, le Marbre de Paros 1209/1208. Ératosthène retint 1184/1183, date devenue canonique ; le site la suit, avec dix ans de siège.\n\n**Ce que dit l'archéologie.** Le site d'Hisarlik, fouillé à partir de 1870 par Heinrich Schliemann, montre une grande ville de l'âge du bronze (Troie VI et VIIa), détruite vers 1300 puis vers 1180. Des textes hittites mentionnent une Wilusa (Ilios ?) et des Ahhiyawa (Achéens ?) actifs en Anatolie occidentale. Ces indices rendent plausibles des conflits dans la région, mais aucun ne prouve la guerre racontée par Homère.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "VIII, 492 à 520 (le cheval de bois)"
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 145",
        "url": `${HERODOTE}:book=2:chapter=145`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 24"
      },
      {
        "kind": "ancient",
        "author": "Clément d'Alexandrie",
        "work": "Stromates",
        "locus": "I, 21, 138 et 139 (dates d'Ératosthène et de Douris)"
      },
      {
        "kind": "modern",
        "author": "Joachim Latacz",
        "work": "Troy and Homer: Towards a Solution of an Old Mystery, Oxford, Oxford University Press, 2004"
      },
      {
        "kind": "modern",
        "author": "Eric H. Cline",
        "work": "The Trojan War: A Very Short Introduction, Oxford, Oxford University Press, 2013"
      }
    ]
  },
  {
    "id": "meurtre-d-agamemnon-et-vengeance-d-oreste",
    "title": "Le meurtre d'Agamemnon et la vengeance d'Oreste",
    "start": -1183,
    "end": -1175,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Dates déduites de la prise de Troie selon Ératosthène (1184/3) et de l'Odyssée, qui fait régner Égisthe sept ans sur Mycènes avant le retour d'Oreste la huitième année ; le Marbre de Paros (entrée A 25) date de 1208/7 l'acquittement d'Oreste devant l'Aréopage, un an après sa propre date de la prise de Troie ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "politics",
    "importance": 2,
    "placeId": "mycenes",
    "people": [
      "agamemnon",
      "clytemnestre",
      "oreste"
    ],
    "summary": "Revenu vainqueur de Troie, Agamemnon, roi de Mycènes, est assassiné par sa femme Clytemnestre et par son amant Égisthe. Sept ans plus tard, son fils Oreste revient le venger en tuant Égisthe et sa propre mère ; poursuivi par les Érinyes, il est jugé et acquitté à Athènes. Ce meurtre clôt la sanglante histoire de la maison d'Atrée.",
    "body": "**Une maison maudite.** Les crimes se succèdent dans la famille depuis Tantale et Pélops : Atrée sert à son frère Thyeste la chair de ses propres enfants, et Égisthe, fils de Thyeste, venge son père. Agamemnon, fils d'Atrée, a sacrifié sa fille Iphigénie à Aulis pour obtenir des vents favorables, ce que Clytemnestre ne lui pardonne pas.\n\n**Des récits concurrents.** Dans l'*Odyssée*, Égisthe est le principal meurtrier et la vengeance d'Oreste sert de modèle à Télémaque. L'*Orestie* d'Eschyle (458) fait de Clytemnestre la meurtrière, qui frappe son mari dans son bain, et fonde à Athènes le tribunal de l'Aréopage pour juger Oreste, quelques années après la réforme qui avait réduit ses pouvoirs. Sophocle et Euripide ont chacun écrit une *Électre*. Vers 550, les Spartiates rapportèrent de Tégée de prétendus ossements d'Oreste, pour s'approprier le héros.\n\n**Ce que montre l'archéologie.** Le masque d'or trouvé par Schliemann en 1876 dans le cercle A de Mycènes, qu'il croyait celui d'Agamemnon, date du XVIe siècle, trois siècles trop tôt. Le « trésor d'Atrée » et la « tombe de Clytemnestre » sont des tombes à coupole du XIVe ou du XIIIe siècle, nommées par les voyageurs et les archéologues à partir de Pausanias, qui vit à Mycènes des tombes attribuées aux Atrides. La citadelle subit des destructions vers 1200 puis décline.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "I, 29 à 43 ; III, 193 à 200 et 303 à 310 ; XI, 405 à 434"
      },
      {
        "kind": "ancient",
        "author": "Eschyle",
        "work": "Orestie (Agamemnon, Les Choéphores, Les Euménides)"
      },
      {
        "kind": "ancient",
        "author": "Sophocle",
        "work": "Électre"
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 67 et 68",
        "url": `${HERODOTE}:book=1:chapter=67`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 16, 6 et 7",
        "url": `${PAUSANIAS}:book=2:chapter=16`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 24 et 25"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "errances-d-ulysse",
    "title": "Les errances d'Ulysse",
    "start": -1183,
    "end": -1173,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Dates déduites de la prise de Troie selon Ératosthène (1184/3) et des dix ans de voyage que l'Odyssée prête à Ulysse, rentré à Ithaque la vingtième année après son départ ; récit légendaire.",
    "era": "bronze",
    "track": "mythes",
    "category": "culture",
    "importance": 1,
    "placeId": "ithaque",
    "people": [
      "ulysse",
      "penelope"
    ],
    "summary": "Après la chute de Troie, Ulysse, roi d'Ithaque, met dix ans à rentrer chez lui. Poursuivi par la colère de Poséidon, dont il a aveuglé le fils, le Cyclope Polyphème, il perd tous ses compagnons et reste sept ans chez la nymphe Calypso, avant que les Phéaciens le ramènent à Ithaque. Il y massacre les prétendants qui pressaient sa femme Pénélope de se remarier.",
    "body": "**Le récit.** L'*Odyssée*, composée vers la fin du VIIIe ou au VIIe siècle, entrelace le voyage de Télémaque, parti chercher des nouvelles de son père à Pylos et à Sparte, et le récit qu'Ulysse fait de ses aventures chez les Phéaciens : les Lotophages, le Cyclope, Éole et l'outre des vents, les Lestrygons, Circé, la descente aux Enfers, les Sirènes, Charybde et Scylla, les vaches du Soleil. De retour sous les traits d'un mendiant, il se fait reconnaître et reprend sa maison.\n\n**Une géographie disputée.** Les Anciens ont cherché les escales d'Ulysse : Thucydide place les Phéaciens à Corcyre, et la tradition met les Cyclopes et Scylla en Sicile ou près du détroit de Messine. Ératosthène s'en moquait déjà, estimant qu'on trouverait la route d'Ulysse le jour où l'on trouverait le cordonnier qui avait cousu l'outre des vents. Ulysse, l'homme rusé, est admiré ou critiqué selon les auteurs, jusqu'à devenir chez Sophocle un politique sans scrupules.\n\n**Ce que montre l'archéologie.** À Ithaque, aucun palais mycénien n'a été identifié avec certitude ; la grotte de la baie de Polis a livré des trépieds du IXe et du VIIIe siècle et un masque d'époque hellénistique portant une dédicace à Ulysse, signe d'un culte du héros. Certains chercheurs placent l'Ithaque d'Homère sur une autre île, hypothèse non démontrée. À Pylos, où Télémaque rend visite à Nestor, le « palais de Nestor », fouillé à partir de 1939, a livré plus d'un millier de tablettes en linéaire B ; il est détruit par le feu vers 1180.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "I, 1 à 21 ; IX à XII ; XXII et XXIII"
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 25, 4",
        "url": `${THUCYDIDE}:book=1:chapter=25`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "I, 2, 15 (le mot d'Ératosthène)",
        "url": `${STRABON}:book=1:chapter=2:section=15`
      },
      {
        "kind": "ancient",
        "author": "Sophocle",
        "work": "Philoctète"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      },
      {
        "kind": "modern",
        "author": "Irad Malkin",
        "work": "The Returns of Odysseus: Colonization and Ethnicity, Berkeley, University of California Press, 1998"
      }
    ]
  },
  {
    "id": "retour-des-heraclides",
    "title": "Le retour des Héraclides",
    "start": -1103,
    "precision": "decade",
    "certainty": "legendary",
    "certaintyNote": "Date d'Ératosthène, qui compte quatre-vingts ans entre la prise de Troie (1184/3) et le retour des Héraclides (1104/3), comme Thucydide (I, 12) ; récit légendaire, que les Anciens tenaient pour l'histoire de l'arrivée des Doriens.",
    "era": "bronze",
    "track": "mythes",
    "category": "war",
    "importance": 2,
    "placeId": "sparte",
    "people": [
      "heracles"
    ],
    "summary": "Quatre-vingts ans après la prise de Troie, selon Thucydide, les descendants d'Héraclès, chassés du Péloponnèse après sa mort, y reviennent à la tête des Doriens. Ils se partagent le pays par tirage au sort : Téménos reçoit Argos, Cresphontès la Messénie, et les fils jumeaux d'Aristodèmos, Eurysthénès et Proclès, la Laconie, d'où descendent les deux familles royales de Sparte.",
    "body": "**Le mythe.** Après la mort d'Héraclès, ses fils, persécutés par Eurysthée, se réfugient à Athènes. Plusieurs tentatives de retour échouent, car l'oracle parlait de la « troisième récolte », c'est-à-dire de la troisième génération. Les arrière-petits-fils du héros franchissent enfin le golfe de Corinthe à Naupacte, guidés par l'Étolien Oxylos, qui reçoit l'Élide ; Cresphontès obtient la Messénie par une ruse lors du tirage au sort.\n\n**Une charte politique.** Le récit justifiait la domination des Doriens dans le Péloponnèse : les deux dynasties royales de Sparte, les Agiades et les Eurypontides, remontaient à Héraclès, comme les rois d'Argos, et les rois de Macédoine se disaient issus de Téménos. Le poète spartiate Tyrtée rappelait que Zeus avait donné la cité aux Héraclides, et Euripide, dans *Les Héraclides*, rappelait aux Spartiates ce qu'ils devaient à Athènes.\n\n**Ce que dit l'archéologie.** Au XIXe siècle, on a lu dans ce mythe le souvenir d'une « invasion dorienne » qui aurait détruit les palais mycéniens. La plupart des archéologues en doutent aujourd'hui : aucune culture matérielle propre à des nouveaux venus n'a été identifiée, les destructions de 1200 environ s'étalent sur plusieurs décennies et ont des causes variées, et la date antique tombe un siècle plus tard. La répartition des dialectes doriens reste le principal indice d'un déplacement de populations, dont l'ampleur et la date sont discutées.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 12",
        "url": `${THUCYDIDE}:book=1:chapter=12`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VI, 52 et VIII, 137",
        "url": `${HERODOTE}:book=6:chapter=52`
      },
      {
        "kind": "ancient",
        "author": "Apollodore",
        "work": "Bibliothèque",
        "locus": "II, 8, 2 à 5"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 18, 7 à 9",
        "url": `${PAUSANIAS}:book=2:chapter=18`
      },
      {
        "kind": "ancient",
        "author": "Clément d'Alexandrie",
        "work": "Stromates",
        "locus": "I, 21, 138 (dates d'Ératosthène)"
      },
      {
        "kind": "ancient",
        "author": "Tyrtée",
        "work": "Fragments",
        "locus": "fr. 2 West"
      },
      {
        "kind": "modern",
        "author": "Jonathan M. Hall",
        "work": "Ethnic Identity in Greek Antiquity, Cambridge, Cambridge University Press, 1997"
      },
      {
        "kind": "modern",
        "author": "Timothy Gantz",
        "work": "Early Greek Myth: A Guide to Literary and Artistic Sources, Baltimore, Johns Hopkins University Press, 1993"
      }
    ]
  },
  {
    "id": "migration-ionienne",
    "title": "Migration ionienne",
    "start": -1043,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Date traditionnelle : 1044/1043 selon Ératosthène, 1077/1076 selon le Marbre de Paros. L'archéologie montre une installation progressive, du XIe au IXe siècle.",
    "era": "ages-obscurs",
    "track": "monde-grec",
    "category": "society",
    "importance": 1,
    "placeId": "milet",
    "people": [
      "nelee"
    ],
    "summary": "Selon la tradition, des Grecs partis d'Athènes, menés par Nélée et d'autres fils du roi Codros, fondent les cités d'Ionie sur la côte d'Asie Mineure, Milet en tête. L'archéologie confirme une installation grecque sur cette côte aux XIe et Xe siècles, mais progressive et moins organisée que le récit.",
    "body": "**Le récit traditionnel.** Les auteurs grecs racontent qu'après le retour des Héraclides, des familles chassées du Péloponnèse se réfugient en Attique, puis passent la mer sous la conduite des fils de Codros, dernier roi d'Athènes. Nélée fonde Milet, Androclos Éphèse ; douze cités forment la ligue ionienne, autour du sanctuaire commun du Panionion. Athènes s'en servira pour se présenter comme la métropole de tous les Ioniens.\n\n**Les dates.** Ératosthène place la migration soixante ans après le retour des Héraclides, soit en 1044/1043 ; le Marbre de Paros la place en 1077/1076. Ce sont des calculs par générations, sans document contemporain.\n\n**Ce que montrent les fouilles.** Milet abritait déjà des Minoens puis des Mycéniens. La céramique protogéométrique apparaît à Milet, Éphèse, Smyrne ou Clazomènes à partir de la fin du XIe siècle et au Xe siècle, ce qui suggère des arrivées échelonnées plutôt qu'une expédition unique. Hérodote remarquait déjà que les Ioniens d'Asie étaient un peuple mêlé, dont les ancêtres avaient épousé des femmes cariennes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 142 à 148",
        "url": `${HERODOTE}:book=1:chapter=142`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "VII, 2, 1 à 9",
        "url": `${PAUSANIAS}:book=7:chapter=2`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIV, 1, 3",
        "url": `${STRABON}:book=14:chapter=1:section=3`
      },
      {
        "kind": "ancient",
        "author": "Clément d'Alexandrie",
        "work": "Stromates",
        "locus": "I, 21, 138 (chronologie d'Ératosthène)"
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros (FGrHist 239)",
        "locus": "A, 27"
      },
      {
        "kind": "modern",
        "author": "Alan M. Greaves",
        "work": "The Land of Ionia: Society and Economy in the Archaic Period, Chichester, Wiley-Blackwell, 2010"
      },
      {
        "kind": "modern",
        "author": "Jonathan M. Hall",
        "work": "A History of the Archaic Greek World, ca. 1200-479 BCE, 2e éd., Chichester, Wiley-Blackwell, 2014"
      }
    ]
  },
  {
    "id": "style-protogeometrique-a-athenes",
    "title": "Le style protogéométrique à Athènes",
    "start": -1049,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique, à quelques décennies près : le style apparaît vers 1050 selon la chronologie classique, un peu plus tard selon d'autres.",
    "era": "ages-obscurs",
    "track": "monde-grec",
    "category": "culture",
    "importance": 3,
    "placeId": "ceramique",
    "summary": "Vers 1050, les potiers d'Athènes inventent un style nouveau : vases mieux galbés, tournés plus vite, décorés de cercles et de demi-cercles tracés au compas. Ce style protogéométrique, connu surtout par les tombes du Céramique, se répand dans une grande partie de l'Égée et sert aux archéologues d'horloge pour dater les âges obscurs.",
    "body": "**Un nouvel artisanat.** Après la fin des palais, la céramique dite submycénienne est pauvre et répétitive. Vers 1050, des ateliers athéniens adoptent un tour plus rapide et un outil nouveau, un compas muni de plusieurs pinceaux, qui trace des cercles concentriques réguliers sur des amphores et des cratères aux formes plus tendues.\n\n**Ce que disent les tombes.** Les nécropoles du Céramique, au nord-ouest de l'Acropole, livrent la séquence la plus complète : les adultes sont incinérés, leurs cendres placées dans une amphore choisie selon le sexe (anses sur le col pour les hommes, sur la panse pour les femmes), et des armes de fer accompagnent les hommes. Le fer devient alors courant pour les armes et les outils.\n\n**Une horloge relative.** Le protogéométrique (de 1050 à 900 environ), puis le géométrique (de 900 à 700 environ), servent à dater les couches des sites de tout le monde grec. Les dates absolues restent approximatives, car elles reposent sur peu d'objets datés par ailleurs au Proche-Orient et sur le radiocarbone.",
    "sources": [
      {
        "kind": "modern",
        "author": "Vincent R. d'A. Desborough",
        "work": "Protogeometric Pottery, Oxford, Clarendon Press, 1952"
      },
      {
        "kind": "modern",
        "author": "Irene S. Lemos",
        "work": "The Protogeometric Aegean: The Archaeology of the Late Eleventh and Tenth Centuries BC, Oxford, Oxford University Press, 2002"
      },
      {
        "kind": "modern",
        "author": "J. N. Coldstream",
        "work": "Geometric Greece, 900-700 BC, 2e éd., Londres, Routledge, 2003"
      }
    ]
  },
  {
    "id": "grand-edifice-de-lefkandi",
    "title": "Grand édifice de Lefkandi",
    "start": -949,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Bâtiment daté vers 950 par la céramique ; sa fonction (monument funéraire ou demeure de chef) reste discutée.",
    "era": "ages-obscurs",
    "track": "monde-grec",
    "category": "society",
    "importance": 2,
    "placeId": "lefkandi",
    "summary": "Vers 950, à Lefkandi en Eubée, un bâtiment absidal de près de 50 mètres de long abrite deux sépultures : un homme incinéré, dont les cendres reposent dans une amphore de bronze venue de Chypre, et une femme parée d'or ; quatre chevaux sont enterrés à côté. Cette découverte nuance l'image d'âges obscurs appauvris et coupés du monde.",
    "body": "**La découverte.** En 1980, des fouilles de sauvetage menées par l'École britannique d'Athènes et le service archéologique grec dégagent sur la colline de Toumba un édifice de près de 50 mètres sur une dizaine, aux murs de briques crues sur un socle de pierre, entouré d'une rangée de poteaux de bois. Sous le sol, une double sépulture : les cendres d'un homme, enveloppées d'un tissu, dans une amphore de bronze chypriote déjà ancienne, avec une épée et une lance de fer ; à côté, une femme inhumée avec des bijoux d'or, dont un pendentif d'origine orientale ; dans une fosse voisine, quatre chevaux.\n\n**Monument ou demeure ?** Le bâtiment a été démoli peu après les funérailles et recouvert d'un tertre. Les fouilleurs y ont vu un hérôon, un monument élevé en l'honneur du défunt ; d'autres pensent à la maison d'un chef, transformée en tombeau à sa mort. La question reste ouverte.\n\n**Pourquoi c'est important.** La nécropole qui se développe ensuite autour du tertre est riche en objets venus du Levant, de Chypre et d'Égypte. Lefkandi montre qu'au Xe siècle certaines communautés grecques avaient des chefs puissants et des échanges lointains, bien avant la reprise générale du VIIIe siècle.",
    "sources": [
      {
        "kind": "modern",
        "author": "Mervyn R. Popham, Petros G. Calligas, L. Hugh Sackett (dir.)",
        "work": "Lefkandi II. The Protogeometric Building at Toumba, part 2, The Excavation, Architecture and Finds, Londres, British School at Athens, 1993"
      },
      {
        "kind": "modern",
        "author": "Irene S. Lemos",
        "work": "The Protogeometric Aegean: The Archaeology of the Late Eleventh and Tenth Centuries BC, Oxford, Oxford University Press, 2002"
      }
    ]
  },
  {
    "id": "premiers-jeux-olympiques",
    "title": "Premiers Jeux olympiques",
    "start": -775,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Date tirée de la liste des vainqueurs établie vers 400 par Hippias d'Élis, que Plutarque jugeait déjà peu sûre ; l'archéologie suggère un essor des concours plutôt vers 700.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "religion",
    "importance": 1,
    "placeId": "olympie",
    "people": [
      "corebe"
    ],
    "summary": "Selon la tradition, les premiers Jeux olympiques se tiennent en 776 au sanctuaire de Zeus à Olympie, avec une seule épreuve, la course du stade, remportée par Corèbe d'Élis. Les Grecs dateront ensuite les années par olympiades, mais cette date de départ est une reconstruction tardive.",
    "body": "**Le récit.** Pausanias raconte que les Jeux, plus anciens selon la légende, furent rétablis par Iphitos, roi d'Élis, et que la liste des vainqueurs commence avec Corèbe, vainqueur du stade, une course d'environ 192 mètres. D'autres épreuves s'ajoutent au fil des olympiades : double stade, course de fond, lutte, pentathlon, pugilat, courses de chars.\n\n**Une date calculée.** La liste des vainqueurs fut établie vers 400 par le sophiste Hippias d'Élis, puis reprise par Aristote et Ératosthène. Plutarque note déjà que Hippias ne s'appuyait sur aucune preuve sûre. L'année 776 est devenue le point de départ du comput par olympiades, généralisé par les historiens à partir de Timée, au IIIe siècle av. J.-C.\n\n**Ce que dit l'archéologie.** Des offrandes (figurines de terre cuite et de bronze, trépieds) montrent un culte à Olympie dès le Xe siècle. Les puits creusés pour les visiteurs se multiplient vers 700, ce qui suggère que les concours prennent de l'ampleur à ce moment, plus tard que la date traditionnelle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "V, 8, 5 et 6",
        "url": `${PAUSANIAS}:book=5:chapter=8`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Numa",
        "locus": "1",
        "url": `${PLUTARQUE}/Numa*.html`
      },
      {
        "kind": "modern",
        "author": "Alfred Mallwitz",
        "work": "Cult and Competition Locations at Olympia, dans W. J. Raschke (dir.), The Archaeology of the Olympics, Madison, University of Wisconsin Press, 1988"
      },
      {
        "kind": "modern",
        "author": "Paul Christesen",
        "work": "Olympic Victor Lists and Ancient Greek History, Cambridge, Cambridge University Press, 2007"
      }
    ]
  },
  {
    "id": "adoption-de-l-alphabet",
    "title": "Adoption de l'alphabet",
    "start": -799,
    "end": -749,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Les premières inscriptions grecques datent de 775 à 725 environ ; l'emprunt lui-même est placé selon les auteurs entre la fin du IXe et le début du VIIIe siècle, en un lieu inconnu.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "people": [
      "cadmos"
    ],
    "summary": "Au VIIIe siècle, les Grecs empruntent l'alphabet des Phéniciens et l'adaptent en notant aussi les voyelles. Les premières inscriptions, gravées ou peintes sur des vases vers 775 à 725, sont des vers, des noms et des dédicaces. L'écriture, disparue depuis la fin des palais, revient sous une forme bien plus simple que le linéaire B.",
    "body": "**Un emprunt phénicien.** Les Grecs eux-mêmes appelaient leurs lettres *phoinikeia grammata*, « lettres phéniciennes », et Hérodote attribue leur introduction aux Phéniciens venus avec Cadmos. La forme et l'ordre des lettres (alpha, bêta, gamma, d'après *aleph*, *beth*, *gimel*) le confirment. L'innovation grecque est d'avoir employé des signes de consonnes inutiles en grec pour noter les voyelles.\n\n**Les premières inscriptions.** Parmi les plus anciennes : quelques lettres sur un vase de Gabii, dans le Latium (vers 770, lecture discutée), l'œnochoé du Dipylon à Athènes (vers 740), promise au danseur le plus gracieux, et la « coupe de Nestor » de Pithécusses, dans la baie de Naples (vers 725), qui porte trois vers. Ces textes montrent un usage privé et poétique avant l'usage administratif.\n\n**Où et quand ?** Le lieu de l'emprunt (Eubée, Crète, Chypre, comptoir d'Al Mina en Syrie) et sa date restent discutés : la plupart des spécialistes le placent au début du VIIIe siècle, certains plus tôt. Chaque région développe ensuite son alphabet local, jusqu'à l'adoption officielle de l'alphabet ionien par Athènes en 403/402.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 58",
        "url": `${HERODOTE}:book=5:chapter=58`
      },
      {
        "kind": "modern",
        "author": "Lilian H. Jeffery",
        "work": "The Local Scripts of Archaic Greece, 2e éd. revue par A. W. Johnston, Oxford, Clarendon Press, 1990"
      },
      {
        "kind": "modern",
        "author": "Barry B. Powell",
        "work": "Homer and the Origin of the Greek Alphabet, Cambridge, Cambridge University Press, 1991"
      }
    ]
  },
  {
    "id": "fondation-de-syracuse",
    "title": "Fondation de Syracuse",
    "start": -732,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Thucydide ne donne pas d'année absolue : on la déduit des intervalles qu'il indique entre les fondations siciliennes, ce qui donne 733 ou 734. La céramique la plus ancienne du site s'accorde avec la seconde moitié du VIIIe siècle.",
    "era": "archaique",
    "track": "occident",
    "category": "politics",
    "importance": 2,
    "placeId": "syracuse",
    "people": [
      "archias"
    ],
    "summary": "Selon Thucydide, des colons de Corinthe menés par Archias, de la famille aristocratique des Bacchiades, s'installent sur l'île d'Ortygie un an après la fondation de Naxos de Sicile, et en chassent les Sicules. Syracuse devient la plus puissante des cités grecques d'Occident.",
    "body": "**Le récit.** Thucydide, au début de son récit de l'expédition athénienne en Sicile, énumère les fondations grecques de l'île : Naxos par des Chalcidiens, puis, l'année suivante, Syracuse par Archias, un Héraclide de Corinthe, qui chasse les Sicules de l'île d'Ortygie. Ortygie, reliée plus tard à la terre ferme, reste le cœur de la ville, avec la source Aréthuse.\n\n**La date.** Thucydide compte en intervalles (Camarine, par exemple, est fondée 135 ans après Syracuse) ; les modernes les raccrochent à des dates transmises par d'autres auteurs, et obtiennent 733 ou 734. La céramique corinthienne trouvée sur place s'accorde avec la seconde moitié du VIIIe siècle.\n\n**Une colonie conquérante.** Riche de la plaine qui l'entoure et de deux ports, Syracuse fonde à son tour Akrai, Kasménai et Camarine, et domine au Ve siècle une grande partie de la Sicile. Une tradition rapportée par Plutarque explique le départ d'Archias par un meurtre commis à Corinthe : comme souvent, le récit de fondation mêle souvenirs et légendes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI, 3, 2 et VI, 5, 2 et 3",
        "url": `${THUCYDIDE}:book=6:chapter=3`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VI, 2, 4",
        "url": `${STRABON}:book=6:chapter=2:section=4`
      },
      {
        "kind": "modern",
        "author": "Adolfo J. Domínguez",
        "work": "Greeks in Sicily, dans G. R. Tsetskhladze (dir.), Greek Colonisation, vol. 1, Leyde, Brill, 2006"
      },
      {
        "kind": "modern",
        "author": "Franco De Angelis",
        "work": "Archaic and Classical Greek Sicily: A Social and Economic History, Oxford, Oxford University Press, 2016"
      }
    ]
  },
  {
    "id": "fondation-de-marseille",
    "title": "Fondation de Marseille",
    "start": -599,
    "precision": "decade",
    "certainty": "traditional",
    "certaintyNote": "Timée place la fondation 120 ans avant Salamine, soit vers 600 ; la céramique grecque la plus ancienne des fouilles de Marseille s'accorde avec cette date.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "politics",
    "importance": 2,
    "placeId": "marseille",
    "people": [
      "protis"
    ],
    "summary": "Vers 600, des Grecs de Phocée, cité d'Ionie, fondent Massalia près de l'embouchure du Rhône. Selon la légende, leur chef épouse la fille du roi indigène, qui le choisit au cours d'un banquet. Massalia devient le principal port grec de l'Occident et fonde à son tour des comptoirs en Gaule et en Espagne.",
    "body": "**La légende de fondation.** Aristote, cité par Athénée, et Justin, qui abrège l'historien Trogue Pompée, racontent qu'un Phocéen (Euxène chez Aristote, Protis chez Justin) arrive chez le roi indigène Nannos le jour où sa fille doit choisir un époux au cours d'un banquet. Elle tend la coupe au Grec, et le couple reçoit le terrain de la future ville. Le récit présente l'installation comme une alliance plutôt qu'une conquête.\n\n**La date.** Thucydide rapporte seulement que les Phocéens, en fondant Massalia, battirent les Carthaginois sur mer. Timée, dont le calcul est transmis par le Pseudo-Scymnos, place la fondation 120 ans avant la bataille de Salamine, soit vers 600. Les fouilles de Marseille ont livré de la céramique grecque du tout début du VIe siècle, qui s'accorde avec cette date.\n\n**Un port d'Occident.** Massalia contrôle l'accès à la vallée du Rhône, voie du commerce avec la Gaule intérieure. Elle fonde ou contrôle Agde, Nice, Antibes et Emporion en Catalogne. Alliée de Rome, elle reste une cité grecque indépendante jusqu'à sa prise par César en 49.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 13, 6",
        "url": `${THUCYDIDE}:book=1:chapter=13`
      },
      {
        "kind": "ancient",
        "author": "Athénée",
        "work": "Deipnosophistes",
        "locus": "XIII, 576a (citant Aristote, Constitution des Massaliotes)"
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XLIII, 3 et 4"
      },
      {
        "kind": "ancient",
        "author": "Pseudo-Scymnos",
        "work": "Circuit de la Terre",
        "locus": "v. 211 à 214 (d'après Timée)"
      },
      {
        "kind": "modern",
        "author": "Antoine Hermary, Antoinette Hesnard, Henri Tréziny",
        "work": "Marseille grecque, 600-49 av. J.-C. La cité phocéenne, Paris, Errance, 1999"
      }
    ]
  },
  {
    "id": "revolte-de-l-ionie",
    "title": "Révolte de l'Ionie",
    "start": -498,
    "end": -493,
    "precision": "year",
    "certainty": "attested",
    "era": "archaique",
    "track": "ionie",
    "category": "war",
    "importance": 2,
    "placeId": "milet",
    "people": [
      "aristagoras",
      "histiee",
      "darius-ier"
    ],
    "summary": "En 499, Aristagoras, tyran de Milet, soulève les cités grecques d'Asie contre la domination perse ; Athènes et Érétrie envoient des navires, et les révoltés incendient Sardes. La Perse reprend l'avantage, écrase la flotte ionienne à Ladé en 494 et prend Milet. L'aide athénienne servira de motif aux expéditions perses contre la Grèce.",
    "body": "**Les causes.** Selon Hérodote, Aristagoras, qui gouverne Milet à la place de son beau-père Histiée, retenu à la cour de Darius, a échoué dans une expédition contre Naxos promise aux Perses. Menacé, il renonce à la tyrannie, proclame l'égalité des droits (*isonomia*) et pousse les cités ioniennes à chasser leurs tyrans, soutenus par la Perse. Les historiens ajoutent des raisons plus profondes : poids du tribut, appui perse aux tyrans, concurrence commerciale.\n\n**La guerre.** Sparte refuse son aide ; Athènes envoie 20 navires et Érétrie 5. En 498, les révoltés prennent et incendient Sardes, capitale de la satrapie, temple de Cybèbè compris, puis la révolte gagne l'Hellespont, la Carie et Chypre. Les Perses reprennent ces régions une à une.\n\n**La fin.** En 494, devant l'île de Ladé, la flotte ionienne (353 trières selon Hérodote) est battue par une flotte perse et phénicienne de 600 navires selon lui, après la défection des Samiens. Milet est prise, une partie de ses habitants déportée près de l'embouchure du Tigre. Darius, raconte Hérodote, avait juré de punir Athènes : c'est l'origine de l'expédition de Marathon.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 28 à 38 et 97 à 126",
        "url": `${HERODOTE}:book=5:chapter=28`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VI, 1 à 32",
        "url": `${HERODOTE}:book=6:chapter=1`
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      },
      {
        "kind": "modern",
        "author": "Oswyn Murray",
        "work": "The Ionian Revolt, dans The Cambridge Ancient History, 2e éd., vol. IV, 1988"
      }
    ]
  },
  {
    "id": "reformes-de-clisthene",
    "title": "Réformes de Clisthène",
    "start": -507,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Réformes engagées pendant l'année archontale 508/507 (archontat d'Isagoras), qui chevauche deux de nos années ; leur mise en place a pris plusieurs années.",
    "era": "archaique",
    "track": "athenes",
    "category": "politics",
    "importance": 1,
    "placeId": "athenes",
    "people": [
      "clisthene",
      "isagoras"
    ],
    "summary": "À Athènes, l'Alcméonide Clisthène l'emporte sur son rival Isagoras, soutenu par Sparte, en s'appuyant sur le peuple. Il répartit les citoyens en dix tribus nouvelles, formées de dèmes de toute l'Attique, et crée un Conseil de 500 membres : ces réformes fondent la démocratie athénienne.",
    "body": "**Le contexte.** Après la chute du tyran Hippias (510), deux aristocrates se disputent le pouvoir. Isagoras, archonte en 508/507, appelle le roi de Sparte Cléomène, qui chasse 700 familles ; mais le peuple se soulève, assiège les Spartiates sur l'Acropole et rappelle Clisthène. Hérodote résume : Clisthène avait fait du peuple son allié.\n\n**La réforme.** L'Attique est découpée en environ 140 dèmes, groupés en trente trittyes (dix de la ville, dix de la côte, dix de l'intérieur) ; chaque tribu réunit une trittye de chaque région. Ce brassage casse les clientèles locales des grandes familles. Chaque tribu fournit 50 membres au nouveau Conseil des Cinq-Cents, qui prépare les décisions de l'Assemblée.\n\n**Ce qui reste discuté.** Les Athéniens appelaient ce régime *isonomia*, l'égalité devant la loi ; le mot *dêmokratia* n'apparaît que plus tard. L'ostracisme, attribué à Clisthène par Aristote, n'est utilisé pour la première fois qu'en 488/487. Les intentions de Clisthène, idéaliste ou habile chef de faction, sont débattues.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 66 et 69 à 73",
        "url": `${HERODOTE}:book=5:chapter=66`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Constitution des Athéniens",
        "locus": "20 à 22"
      },
      {
        "kind": "modern",
        "author": "Pierre Lévêque et Pierre Vidal-Naquet",
        "work": "Clisthène l'Athénien, Paris, Les Belles Lettres, 1964"
      },
      {
        "kind": "modern",
        "author": "P. J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "bataille-de-marathon",
    "title": "Bataille de Marathon",
    "start": -489,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée en août ou en septembre 490 : le jour dépend de la reconstitution des calendriers athénien et spartiate (12 septembre selon Boeckh, mi-août selon d'autres calculs).",
    "era": "archaique",
    "track": "athenes",
    "category": "war",
    "importance": 1,
    "placeId": "marathon",
    "people": [
      "miltiade",
      "callimaque",
      "datis",
      "darius-ier"
    ],
    "summary": "En 490, une armée perse commandée par Datis et Artapherne débarque dans la plaine de Marathon, après avoir détruit Érétrie. Les hoplites d'Athènes et de Platées, menés par Miltiade et le polémarque Callimaque, chargent et la rejettent à la mer. Hérodote compte 6 400 morts perses et 192 Athéniens.",
    "body": "**L'expédition.** Pour punir Athènes et Érétrie de leur aide à la révolte de l'Ionie, Darius envoie une flotte sous les ordres du Mède Datis et d'Artapherne. Érétrie est prise par trahison, puis l'armée débarque à Marathon, sur la côte nord-est de l'Attique, guidée par Hippias, l'ancien tyran d'Athènes. Le coureur Philippidès va demander l'aide de Sparte, mais les Spartiates attendent la pleine lune pour partir.\n\n**La bataille.** Les Athéniens, de 9 000 à 10 000 hoplites selon des auteurs plus tardifs, avec environ 1 000 Platéens, hésitent plusieurs jours. Sur l'avis de Miltiade, ils attaquent : leur centre, volontairement affaibli, recule, tandis que les ailes enfoncent les Perses puis se referment sur eux. Les Perses regagnent leurs navires en en perdant sept. Hérodote ne donne pas leur nombre ; Cornélius Népos parle de 200 000 fantassins et 10 000 cavaliers, mais les historiens modernes estiment le plus souvent l'armée perse entre 20 000 et 30 000 hommes environ.\n\n**Ce qui reste discuté.** La date exacte, le rôle de la cavalerie perse, peut-être absente du champ de bataille, et la course de Marathon à Athènes, qui n'apparaît que chez Plutarque et Lucien, des siècles après Hérodote. Le marathon des Jeux de 1896 s'inspire de cette légende tardive.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VI, 94 à 120",
        "url": `${HERODOTE}:book=6:chapter=94`
      },
      {
        "kind": "ancient",
        "author": "Cornélius Népos",
        "work": "Vie de Miltiade",
        "locus": "4 et 5"
      },
      {
        "kind": "modern",
        "author": "Peter Krentz",
        "work": "The Battle of Marathon, New Haven, Yale University Press, 2010"
      },
      {
        "kind": "modern",
        "author": "Donald W. Olson et al.",
        "work": "The Moon and the Marathon, Sky and Telescope, septembre 2004"
      }
    ]
  },
  {
    "id": "bataille-des-thermopyles",
    "title": "Bataille des Thermopyles",
    "start": -479,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée à la fin de l'été 480 ; le jour est discuté (fin juillet, fin août ou début septembre selon les calculs), car il dépend des Jeux olympiques et de la fête spartiate des Carneia.",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 2,
    "placeId": "thermopyles",
    "people": [
      "leonidas",
      "xerxes",
      "ephialte"
    ],
    "summary": "À la fin de l'été 480, au défilé des Thermopyles, quelques milliers de Grecs commandés par Léonidas, roi de Sparte, arrêtent pendant deux jours l'immense armée de Xerxès. Tournés par un sentier de montagne, ils sont anéantis le troisième jour : Léonidas et ses 300 Spartiates meurent avec les Thespiens restés à leurs côtés.",
    "body": "**Un défilé à tenir.** Pour arrêter l'invasion de Xerxès, les Grecs coalisés occupent le passage étroit entre la montagne et le golfe Maliaque, tandis que leur flotte tient le cap Artémision. Hérodote (VII, 202 et 203) compte 3 100 hoplites du Péloponnèse, dont 300 Spartiates, puis 700 Thespiens et 400 Thébains, soit 4 200 hommes, auxquels s'ajoutent 1 000 Phocidiens et les Locriens d'Oponte venus en masse, qu'il ne chiffre pas : plus de 5 200 hommes au total. Diodore (XI, 4), qui compte les Locriens, arrive à environ 7 400 hommes, et les historiens modernes retiennent le plus souvent environ 7 000. Les « 300 » ne sont donc qu'une partie de l'armée grecque.\n\n**Trois jours.** Pendant deux jours, les assauts perses, y compris ceux des Immortels, échouent dans le défilé. Un homme de la région, Éphialte, révèle alors le sentier de l'Anopée, qui contourne la position. Léonidas renvoie la plus grande partie des troupes et reste avec les Spartiates, 700 Thespiens et 400 Thébains ; ils sont encerclés et tués le troisième jour, sauf des Thébains qui se rendent.\n\n**Les chiffres.** Hérodote attribue à Xerxès plus de 5 millions d'hommes en comptant les non-combattants ; les historiens modernes estiment son armée de terre entre 100 000 et 300 000 hommes environ. Il compte 20 000 morts perses aux Thermopyles, chiffre invérifiable. L'épitaphe attribuée à Simonide (« Étranger, va dire aux Lacédémoniens que nous gisons ici, obéissant à leurs ordres ») a fait de cette défaite un symbole.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VII, 175 à 177 et 201 à 233",
        "url": `${HERODOTE}:book=7:chapter=201`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XI, 4 à 11",
        "url": `${DIODORE}:book=11:chapter=4`
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Thermopylae: The Battle That Changed the World, Londres, Macmillan, 2006"
      },
      {
        "kind": "modern",
        "author": "J. F. Lazenby",
        "work": "The Defence of Greece, 490-479 BC, Warminster, Aris and Phillips, 1993"
      }
    ]
  },
  {
    "id": "bataille-de-salamine",
    "title": "Bataille de Salamine",
    "start": -479,
    "month": 9,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Mois probable : Plutarque place la bataille vers le 20 Boédromion, et elle précède l'éclipse de soleil du 2 octobre 480 ; les propositions vont du 20 au 29 septembre.",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 1,
    "placeId": "salamine",
    "people": [
      "themistocle",
      "eurybiade",
      "xerxes"
    ],
    "summary": "Fin septembre 480, dans le détroit entre l'île de Salamine et l'Attique, la flotte grecque, en majorité athénienne, attire la flotte perse dans un passage étroit où son nombre devient un handicap, et la met en déroute sous les yeux de Xerxès. Cette victoire, voulue par Thémistocle, sauve la Grèce de la conquête.",
    "body": "**Avant la bataille.** Après les Thermopyles, les Perses occupent l'Attique et incendient l'Acropole, évacuée. La flotte grecque, rassemblée à Salamine sous le commandement du Spartiate Eurybiade, hésite à se replier vers l'isthme de Corinthe. Selon Hérodote, Thémistocle fait alors porter à Xerxès un faux message annonçant la fuite des Grecs, pour pousser les Perses à attaquer dans le détroit.\n\n**La bataille.** À l'aube, les navires perses entrent dans le détroit et s'y gênent les uns les autres ; les trières grecques, plus lourdes, les éperonnent. Le combat dure toute la journée. Xerxès, assis au pied du mont Aigaléos, assiste à la défaite. Eschyle, qui a peut-être combattu, en fait le sujet de sa tragédie *Les Perses*, jouée en 472.\n\n**Les chiffres.** Hérodote compte 378 navires grecs, dont 180 athéniens, et 1 207 navires perses au départ de l'expédition ; Eschyle donne 310 navires grecs. Les historiens modernes estiment la flotte perse présente à Salamine entre 600 et 800 navires environ. Après la défaite, Xerxès rentre en Asie et laisse Mardonios en Grèce : il sera battu à Platées l'année suivante.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VIII, 40 à 96",
        "url": `${HERODOTE}:book=8:chapter=40`
      },
      {
        "kind": "ancient",
        "author": "Eschyle",
        "work": "Les Perses",
        "locus": "v. 337 à 432"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Thémistocle",
        "locus": "11 à 15",
        "url": `${PLUTARQUE}/Themistocles*.html`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Camille",
        "locus": "19",
        "url": `${PLUTARQUE}/Camillus*.html`
      },
      {
        "kind": "modern",
        "author": "Barry Strauss",
        "work": "The Battle of Salamis: The Naval Encounter That Saved Greece and Western Civilization, New York, Simon and Schuster, 2004"
      },
      {
        "kind": "modern",
        "author": "J. F. Lazenby",
        "work": "The Defence of Greece, 490-479 BC, Warminster, Aris and Phillips, 1993"
      }
    ]
  },
  {
    "id": "construction-du-parthenon",
    "title": "Construction du Parthénon",
    "start": -446,
    "end": -431,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Dates assurées par les comptes du chantier, gravés sur pierre ; la statue d'Athéna Parthénos est consacrée en 438/437.",
    "era": "classique",
    "track": "athenes",
    "category": "building",
    "importance": 2,
    "placeId": "parthenon",
    "people": [
      "pericles",
      "phidias",
      "ictinos",
      "callicrates"
    ],
    "summary": "De 447 à 432, sur l'Acropole incendiée par les Perses, Athènes construit le Parthénon, temple d'Athéna en marbre du Pentélique, conçu par les architectes Ictinos et Callicratès, sous la direction artistique de Phidias. Financé en partie par le trésor de la ligue de Délos, il affiche la puissance de l'Athènes de Périclès.",
    "body": "**Le chantier.** Les comptes du chantier, gravés sur des stèles exposées sur l'Acropole, couvrent quinze années, de 447/446 à 433/432. La statue d'or et d'ivoire d'Athéna Parthénos, haute d'environ 12 mètres, est consacrée en 438/437, sans doute aux Panathénées de l'été 438 ; les sculptures des frontons sont achevées vers 432. Le temple, dorique mais doté d'une frise continue à la manière ionique, mesure environ 31 mètres sur 70.\n\n**Un monument politique.** Plutarque rapporte les critiques des adversaires de Périclès : Athènes aurait paré la ville comme une coquette avec l'argent versé par les alliés pour la guerre contre les Perses. Le trésor de la ligue de Délos, transféré à Athènes en 454, a bien financé une partie des travaux. La frise montre une procession, sans doute celle des Panathénées.\n\n**La suite.** Le Parthénon devient église, puis mosquée. En 1687, pendant un siège vénitien, un boulet fait exploser la poudre qu'y stockaient les Ottomans et détruit le centre de l'édifice. Une grande partie des sculptures a été emportée à Londres par lord Elgin au début du XIXe siècle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Comptes du Parthénon",
        "locus": "IG I³ 436 à 451"
      },
      {
        "kind": "ancient",
        "author": "Philochore",
        "work": "Atthis",
        "locus": "FGrHist 328 F 121"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Périclès",
        "locus": "12 et 13",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "modern",
        "author": "Bernard Holtzmann",
        "work": "L'Acropole d'Athènes. Monuments, cultes et histoire du sanctuaire d'Athèna Polias, Paris, Picard, 2003"
      },
      {
        "kind": "modern",
        "author": "Jenifer Neils (dir.)",
        "work": "The Parthenon: From Antiquity to the Present, Cambridge, Cambridge University Press, 2005"
      }
    ]
  },
  {
    "id": "guerre-du-peloponnese",
    "title": "Guerre du Péloponnèse",
    "start": -430,
    "end": -403,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 1,
    "placeId": "athenes",
    "people": [
      "pericles",
      "archidamos-ii",
      "alcibiade",
      "lysandre",
      "thucydide"
    ],
    "summary": "De 431 à 404, Athènes et son empire maritime affrontent Sparte et la ligue du Péloponnèse. Après une épidémie qui emporte Périclès, une paix fragile (421) et le désastre de l'expédition de Sicile (de 415 à 413), Sparte, financée par la Perse, détruit la flotte athénienne à Aigos Potamos (405). Athènes, assiégée et affamée, capitule au printemps 404.",
    "body": "**Les causes.** Thucydide, qui a vécu la guerre et en a écrit l'histoire, distingue les griefs immédiats (Corcyre, Potidée, le décret contre Mégare) de la cause la plus vraie : la crainte que la croissance de la puissance athénienne inspirait aux Spartiates. Au printemps 431, les Thébains attaquent Platées, alliée d'Athènes ; quatre-vingts jours plus tard, le roi Archidamos II envahit l'Attique.\n\n**Trois guerres en une.** Pendant la guerre d'Archidamos (de 431 à 421), les Spartiates ravagent l'Attique presque chaque année, tandis que la population s'entasse derrière les Longs Murs ; l'épidémie de 430 à 426, la « peste », tue peut-être un quart à un tiers des habitants, dont Périclès en 429. La paix de Nicias (421) ne règle rien. L'expédition de Sicile, poussée par Alcibiade, s'achève en 413 par la perte de deux flottes. La dernière phase (de 413 à 404) se joue sur mer, avec l'or perse du côté de Sparte.\n\n**La fin.** En 405, Lysandre capture la flotte athénienne à Aigos Potamos, dans l'Hellespont. Athènes, bloquée, capitule au printemps 404 : elle doit abattre les Longs Murs et livrer sa flotte, puis subit le gouvernement oligarchique des Trente. Le conflit a ruiné une grande partie de la Grèce et rendu la Perse arbitre de ses affaires.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 23, 6 ; II, 2, 1 ; II, 19, 1 ; V, 26",
        "url": `${THUCYDIDE}:book=1:chapter=23`
      },
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "II, 1, 21 à 32 et II, 2, 20 à 23",
        "url": `${XENOPHON}:book=2:chapter=2`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Peloponnesian War, New York, Viking, 2003"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": "Le Monde grec et l'Orient, t. I, Le Ve siècle (510-403), Paris, PUF, 1972"
      }
    ]
  },
  {
    "id": "bataille-de-leuctres",
    "title": "Bataille de Leuctres",
    "start": -370,
    "month": 7,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Plutarque date la bataille du 5 Hécatombéon ; la conversion en calendrier julien (début juillet 371) est incertaine d'environ un mois.",
    "era": "classique",
    "track": "thebes",
    "category": "war",
    "importance": 2,
    "placeId": "leuctres",
    "people": [
      "epaminondas",
      "pelopidas",
      "cleombrote-ier"
    ],
    "summary": "En juillet 371, dans la plaine de Leuctres en Béotie, l'armée thébaine d'Épaminondas écrase l'armée spartiate du roi Cléombrote. Pour la première fois, des hoplites spartiates sont battus en bataille rangée par des forces moins nombreuses. Sparte perd sa suprématie, et Thèbes devient pour une dizaine d'années la première puissance de la Grèce.",
    "body": "**Le contexte.** Thèbes refuse de signer la paix générale de 371 au nom des seuls Thébains plutôt que de toute la Béotie. Le roi Cléombrote envahit la Béotie avec 10 000 hoplites et 1 000 cavaliers selon Plutarque ; les Béotiens, 6 000 hommes environ selon Diodore, sont nettement moins nombreux.\n\n**Une aile renforcée.** Épaminondas masse son aile gauche, face aux Spartiates, sur une profondeur d'au moins cinquante rangs, contre douze au plus en face, et retient le reste de sa ligne. Le Bataillon sacré de Pélopidas, 300 hommes d'élite, appuie l'attaque. La cavalerie thébaine bouscule celle de Sparte, puis la colonne thébaine enfonce l'aile droite spartiate : Cléombrote et environ 400 des 700 Spartiates présents sont tués.\n\n**Les conséquences.** Le mythe de l'invincibilité spartiate s'effondre. Épaminondas envahit ensuite le Péloponnèse, libère la Messénie et fonde Messène en 369, privant Sparte des hilotes qui la faisaient vivre. Plutarque date la bataille du 5 Hécatombéon, ce qui correspond à début juillet 371, à un mois près.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "VI, 4, 4 à 15",
        "url": `${XENOPHON}:book=6:chapter=4`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Pélopidas",
        "locus": "20 à 23",
        "url": `${PLUTARQUE}/Pelopidas*.html`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Camille",
        "locus": "19",
        "url": `${PLUTARQUE}/Camillus*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XV, 51 à 56",
        "url": `${DIODORE}:book=15:chapter=51`
      },
      {
        "kind": "modern",
        "author": "John Buckler",
        "work": "The Theban Hegemony, 371-362 BC, Cambridge (Massachusetts), Harvard University Press, 1980"
      },
      {
        "kind": "modern",
        "author": "Victor Davis Hanson",
        "work": "Epameinondas, the Battle of Leuktra (371 B.C.), and the Revolution in Greek Battle Tactics, Classical Antiquity, 7, 2, 1988"
      }
    ]
  },
  {
    "id": "bataille-de-cheronee",
    "title": "Bataille de Chéronée",
    "start": -337,
    "month": 8,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Plutarque donne le 7 Métageitnion, souvent converti en 2 août 338 ; la conversion est incertaine d'environ un mois.",
    "era": "classique",
    "track": "macedoine",
    "category": "war",
    "importance": 2,
    "placeId": "cheronee",
    "people": [
      "philippe-ii",
      "alexandre-le-grand",
      "demosthene"
    ],
    "summary": "En août 338, à Chéronée en Béotie, Philippe II de Macédoine bat l'armée coalisée d'Athènes et de Thèbes, que Démosthène avait poussées à s'unir contre lui. Le jeune Alexandre, 18 ans, commande la cavalerie. Philippe impose ensuite aux cités la ligue de Corinthe, sous son autorité : les grandes cités perdent leur indépendance de fait.",
    "body": "**L'affrontement.** Depuis vingt ans, Philippe étend son pouvoir en Thrace et en Grèce centrale. Démosthène, à Athènes, réussit en 339 à rallier Thèbes contre lui. Selon Diodore, Philippe dispose de plus de 30 000 fantassins et de 2 000 cavaliers ; les Grecs, venus aussi d'autres cités, alignent des effectifs comparables. Les deux armées se rencontrent dans la plaine du Céphise.\n\n**La bataille.** Les récits sont brefs et tardifs. Philippe, à l'aile droite face aux Athéniens, aurait reculé pour les attirer, tandis qu'Alexandre, à l'aile gauche, enfonçait les Thébains et leur Bataillon sacré. Plus de 1 000 Athéniens sont tués et au moins 2 000 faits prisonniers selon Diodore. Le lion de Chéronée se dresse au-dessus d'une fosse où l'on a retrouvé 254 squelettes, souvent attribués au Bataillon sacré.\n\n**Les conséquences.** Philippe traite Athènes avec ménagement mais met une garnison à Thèbes. En 337, il réunit les cités grecques, sauf Sparte, dans la ligue de Corinthe, dont il prend la tête pour une guerre contre la Perse. Assassiné en 336, il laisse ce projet à Alexandre.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 84 à 88",
        "url": `${DIODORE}:book=16:chapter=84`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "9",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Camille",
        "locus": "19",
        "url": `${PLUTARQUE}/Camillus*.html`
      },
      {
        "kind": "ancient",
        "author": "Polyen",
        "work": "Stratagèmes",
        "locus": "IV, 2, 2"
      },
      {
        "kind": "modern",
        "author": "N. G. L. Hammond et G. T. Griffith",
        "work": "A History of Macedonia, vol. II, 550-336 B.C., Oxford, Clarendon Press, 1979"
      },
      {
        "kind": "modern",
        "author": "Pierre Carlier",
        "work": "Démosthène, Paris, Fayard, 1990"
      }
    ]
  },
  {
    "id": "bataille-de-gaugameles",
    "title": "Bataille de Gaugamèles",
    "start": -330,
    "month": 10,
    "day": 1,
    "precision": "day",
    "certainty": "attested",
    "certaintyNote": "Date assurée par l'éclipse de lune du 20 septembre 331, survenue onze jours avant la bataille selon Plutarque, et par un journal astronomique babylonien.",
    "era": "classique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "gaugameles",
    "people": [
      "alexandre-le-grand",
      "darius-iii",
      "parmenion"
    ],
    "summary": "Le 1er octobre 331, dans la plaine de Gaugamèles, au nord de la Mésopotamie, Alexandre affronte la grande armée de Darius III. Une charge de la cavalerie macédonienne, menée par Alexandre lui-même, perce le centre perse et met Darius en fuite. L'empire achéménide est perdu : Babylone, Suse et Persépolis tombent dans les mois suivants.",
    "body": "**Le terrain choisi par Darius.** Après sa défaite d'Issos (333), Darius III rassemble les contingents des provinces orientales et choisit une vaste plaine, aplanie pour ses chars à faux. Arrien lui prête 40 000 cavaliers et un million de fantassins, chiffres très exagérés ; les historiens modernes pensent à une armée de 50 000 à 100 000 hommes, parfois davantage. Alexandre dispose d'environ 40 000 fantassins et 7 000 cavaliers selon Arrien.\n\n**La bataille.** Alexandre progresse en oblique vers sa droite pour quitter le terrain préparé ; les chars perses sont neutralisés par l'infanterie légère. Quand la cavalerie perse ouvre une brèche dans sa propre ligne en cherchant à déborder la droite macédonienne, Alexandre s'y engouffre avec les Compagnons et fonce vers Darius, qui s'enfuit. À gauche, Parménion, durement pressé, tient bon.\n\n**Une date sûre.** Une éclipse de lune, que Plutarque place onze jours avant la bataille, est celle du 20 septembre 331. Un journal astronomique babylonien, rédigé au jour le jour, note la défaite de l'armée du roi face au « roi du monde », Alexandre, à la date correspondant au 1er octobre. Darius, en fuite, sera assassiné par ses satrapes en juillet 330.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "III, 7 à 15"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "31 à 33",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 53 à 61",
        "url": `${DIODORE}:book=17:chapter=53`
      },
      {
        "kind": "ancient",
        "author": "Journal astronomique babylonien",
        "work": "A. J. Sachs et H. Hunger, Astronomical Diaries and Related Texts from Babylonia, vol. I, Vienne, 1988",
        "locus": "n° -330"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Alexandre le Grand, Paris, PUF, coll. Que sais-je ?, 1974, nombreuses rééditions"
      }
    ]
  },
  {
    "id": "mort-d-alexandre",
    "title": "Mort d'Alexandre le Grand",
    "start": -322,
    "month": 6,
    "day": 11,
    "precision": "day",
    "certainty": "attested",
    "certaintyNote": "Date établie par un journal astronomique babylonien (29 Aiaru, du soir du 10 au soir du 11 juin 323) ; Plutarque donne le 28 Daisios. Les causes de la mort restent discutées.",
    "era": "hellenistique",
    "track": "alexandre",
    "category": "politics",
    "importance": 1,
    "placeId": "babylone",
    "people": [
      "alexandre-le-grand",
      "perdiccas"
    ],
    "summary": "Le 11 juin 323, Alexandre meurt à Babylone, à 32 ans, après une dizaine de jours de fièvre, sans successeur désigné. Ses généraux confient le pouvoir à son demi-frère Philippe III Arrhidée et à son fils à naître, Alexandre IV, sous la régence de Perdiccas : c'est le début des guerres des Diadoques et de l'époque hellénistique.",
    "body": "**Les derniers jours.** De retour d'Inde, Alexandre prépare à Babylone une expédition vers l'Arabie. Après un banquet, il est pris de fièvre ; les *Éphémérides royales*, citées par Arrien et Plutarque, décrivent une aggravation progressive, la perte de la parole, puis la mort. Un journal astronomique babylonien note sobrement : « le roi mourut ».\n\n**Pourquoi ?** Les Anciens évoquaient déjà un empoisonnement par l'entourage d'Antipatros, rumeur que la plupart des historiens rejettent. Les hypothèses modernes vont du paludisme à la fièvre typhoïde, en passant par l'alcool et l'épuisement dû aux blessures ; aucune ne peut être prouvée.\n\n**Un empire sans maître.** Selon la tradition, Alexandre, interrogé sur son successeur, aurait répondu : « au plus fort ». Ses généraux se partagent le gouvernement des provinces (accords de Babylone) : Ptolémée reçoit l'Égypte, Antigone garde la Phrygie, Lysimaque reçoit la Thrace. Perdiccas, régent, est tué en 321 ou 320, et l'unité de l'empire ne survit pas aux guerres qui suivent.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Journal astronomique babylonien",
        "work": "BM 45962, dans A. J. Sachs et H. Hunger, Astronomical Diaries and Related Texts from Babylonia, vol. I, Vienne, 1988",
        "locus": "n° -322 B"
      },
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "VII, 24 à 28"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "75 à 77",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 117",
        "url": `${DIODORE}:book=17:chapter=117`
      },
      {
        "kind": "modern",
        "author": "Leo Depuydt",
        "work": "The Time of Death of Alexander the Great: 11 June 323 B.C. (-322), ca. 4:00-5:00 PM, Die Welt des Orients, 28, 1997",
        "locus": "p. 117 à 135"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "bataille-d-ipsos",
    "title": "Bataille d'Ipsos",
    "start": -300,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée, sans doute en été 301 d'après le déroulement des campagnes ; l'emplacement exact, en Phrygie, reste approximatif.",
    "era": "hellenistique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "ipsos",
    "people": [
      "antigone-le-borgne",
      "demetrios-poliorcete",
      "seleucos-ier",
      "lysimaque",
      "cassandre"
    ],
    "summary": "En 301, à Ipsos en Phrygie, Séleucos et Lysimaque, alliés de Cassandre et de Ptolémée, battent Antigone le Borgne et son fils Démétrios, qui voulaient reconstituer l'empire d'Alexandre. Antigone, âgé de plus de 80 ans, est tué. Le partage du monde hellénistique entre royaumes rivaux devient définitif.",
    "body": "**Le dernier rêve d'unité.** Depuis la mort d'Alexandre, Antigone le Borgne, maître de l'Asie Mineure et de la Syrie, s'est proclamé roi avec son fils Démétrios en 306. Contre eux, Cassandre (Macédoine), Lysimaque (Thrace), Séleucos (Babylonie et provinces orientales) et Ptolémée (Égypte) forment une coalition.\n\n**La bataille.** Selon Plutarque, Antigone aligne plus de 70 000 fantassins, 10 000 cavaliers et 75 éléphants, ses adversaires 64 000 fantassins, 10 500 cavaliers, 400 éléphants et 120 chars. Ces éléphants viennent du roi indien Chandragupta, qui en avait cédé 500 à Séleucos. Démétrios, à la tête de la cavalerie, met en fuite celle d'en face mais la poursuit trop loin ; les éléphants de Séleucos l'empêchent de revenir. L'infanterie d'Antigone, isolée, se débande ou passe à l'ennemi, et le vieux roi meurt sous les javelots en attendant son fils.\n\n**Le partage.** Lysimaque prend l'essentiel de l'Asie Mineure, Séleucos la Syrie du Nord, où il fonde Antioche ; Ptolémée, absent de la bataille, occupe la Syrie du Sud, objet de six guerres entre Lagides et Séleucides. Démétrios, qui garde sa flotte, prendra la Macédoine en 294.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Démétrios",
        "locus": "28 à 30",
        "url": `${PLUTARQUE}/Demetrius*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XX, 113 et XXI, 1"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XV, 2, 9 (les éléphants de Chandragupta)"
      },
      {
        "kind": "modern",
        "author": "Richard A. Billows",
        "work": "Antigonos the One-Eyed and the Creation of the Hellenistic State, Berkeley, University of California Press, 1990"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": "Histoire politique du monde hellénistique, t. I, 2e éd., Nancy, Presses universitaires de Nancy, 1979"
      }
    ]
  },
  {
    "id": "sac-de-corinthe",
    "title": "Sac de Corinthe",
    "start": -145,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Le sac est attesté ; l'archéologie nuance l'ampleur de la destruction et montre une occupation réduite du site jusqu'à la colonie romaine de 44.",
    "era": "hellenistique",
    "track": "corinthe",
    "category": "war",
    "importance": 1,
    "placeId": "corinthe",
    "people": [
      "mummius",
      "diaios"
    ],
    "summary": "En 146, après la défaite de la ligue achéenne, le consul Lucius Mummius prend Corinthe, fait tuer les hommes, vendre les femmes et les enfants, emporter les œuvres d'art et raser la ville. La même année, Rome détruit Carthage. La Grèce passe sous la surveillance du gouverneur romain de Macédoine.",
    "body": "**La guerre d'Achaïe.** La ligue achéenne, dont Corinthe est le principal centre, entre en conflit avec Rome à propos de Sparte, qui veut la quitter. Ses stratèges, Critolaos puis Diaios, mobilisent jusqu'à des esclaves affranchis. Battue à Scarphée puis à Leucopétra, sur l'isthme, l'armée achéenne se disperse ; Diaios se donne la mort.\n\n**Le sac.** Mummius entre dans Corinthe, que beaucoup d'habitants ont fuie. Selon Pausanias, les hommes restés sur place sont tués, les femmes et les enfants vendus ; statues et tableaux sont envoyés à Rome, et Polybe, témoin, a vu des soldats jouer aux dés sur des tableaux célèbres. Les murs sont abattus et la ville incendiée.\n\n**Après 146.** La ligue est dissoute et les cités grecques passent sous la surveillance du gouverneur de Macédoine, ce qui marque pour beaucoup d'historiens la fin de la Grèce indépendante. Les fouilles montrent toutefois une occupation réduite du site jusqu'à la fondation d'une colonie romaine par César en 44.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "VII, 14 à 16 (en particulier VII, 16, 7 à 10)",
        "url": `${PAUSANIAS}:book=7:chapter=16`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VIII, 6, 23 (citant Polybe)",
        "url": `${STRABON}:book=8:chapter=6:section=23`
      },
      {
        "kind": "modern",
        "author": "Erich S. Gruen",
        "work": "The Hellenistic World and the Coming of Rome, Berkeley, University of California Press, 1984"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": "Histoire politique du monde hellénistique, t. II, 2e éd., Nancy, Presses universitaires de Nancy, 1982"
      }
    ]
  },
  {
    "id": "actium-et-mort-de-cleopatre",
    "title": "Actium et mort de Cléopâtre VII",
    "start": -30,
    "end": -29,
    "month": 9,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Actium a lieu le 2 septembre 31 ; la date de la mort de Cléopâtre (10 ou 12 août 30) est discutée.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "war",
    "importance": 1,
    "placeId": "actium",
    "people": [
      "cleopatre-vii",
      "marc-antoine",
      "octavien",
      "agrippa"
    ],
    "summary": "Le 2 septembre 31, devant Actium, la flotte d'Octavien commandée par Agrippa bat celle de Marc Antoine et de Cléopâtre VII. Un an plus tard, Octavien entre dans Alexandrie : Antoine puis Cléopâtre se donnent la mort, en août 30. L'Égypte passe sous l'autorité de Rome, et le dernier royaume issu de l'empire d'Alexandre disparaît.",
    "body": "**La dernière reine.** Cléopâtre VII, reine depuis 51, est la dernière souveraine de la dynastie fondée par Ptolémée, fils de Lagos ; c'est aussi, selon Plutarque, la première de sa famille à parler égyptien. Alliée puis épouse de Marc Antoine, maître de l'Orient romain, elle reçoit de lui des territoires qui rappellent l'empire lagide d'autrefois (donations d'Alexandrie, 34).\n\n**Actium.** Octavien fait déclarer la guerre à Cléopâtre en 32. Bloquée dans le golfe d'Ambracie, la flotte d'Antoine tente une sortie le 2 septembre 31 ; Cléopâtre prend le large avec soixante navires, Antoine la suit, et le reste de sa flotte se rend. Plutarque donne à Antoine au moins 500 navires de guerre au début de la campagne, et 250 à Octavien ; le nombre réellement engagé reste discuté.\n\n**Alexandrie.** Le 1er août 30, Octavien entre dans Alexandrie et Antoine se tue. Cléopâtre, qui refuse de figurer au triomphe d'Octavien, se donne la mort quelques jours plus tard, le 10 ou le 12 août selon les calculs, par la morsure d'un aspic selon la tradition ; Plutarque reconnaît que personne ne connaît la vérité. Son fils Césarion est exécuté, et l'Égypte est confiée à un préfet d'Octavien.\n\nLa suite de l'histoire, avec Rome devenue empire, se lit sur [Roma, de Romulus à Constantin XI](https://maximator13.github.io/roma/#/evenement/auguste-princeps).",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Antoine",
        "locus": "27, 61 à 68 et 74 à 86",
        "url": `${PLUTARQUE}/Antony*.html`
      },
      {
        "kind": "ancient",
        "author": "Dion Cassius",
        "work": "Histoire romaine",
        "locus": "L, 31 à 35",
        "url": `${DION}/50*.html`
      },
      {
        "kind": "ancient",
        "author": "Dion Cassius",
        "work": "Histoire romaine",
        "locus": "LI, 1, 1 et 10 à 15",
        "url": `${DION}/51*.html`
      },
      {
        "kind": "modern",
        "author": "Christopher Pelling",
        "work": "The triumviral period, dans The Cambridge Ancient History, 2e éd., vol. X, 1996",
        "locus": "chap. 1"
      },
      {
        "kind": "modern",
        "author": "Duane W. Roller",
        "work": "Cleopatra: A Biography, Oxford, Oxford University Press, 2010"
      }
    ]
  }
]
