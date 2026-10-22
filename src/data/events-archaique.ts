import type { HistoricalEvent } from './schema.ts'

const HERODOTE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0126'
const THUCYDIDE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0200'
const PAUSANIAS = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0160'
const DIODORE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0084'
const STRABON = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0198'
const PLUTARQUE = 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives'

export const events: HistoricalEvent[] = [
  {
    "id": "lycurgue-legislateur-de-sparte",
    "title": "Lycurgue, législateur de Sparte",
    "start": -799,
    "precision": "century",
    "certainty": "legendary",
    "certaintyNote": "Les Anciens plaçaient Lycurgue du XIe au VIIIe siècle ; Thucydide dit seulement que Sparte avait le même régime depuis un peu plus de 400 ans en 404, soit vers 800. Son existence même est douteuse.",
    "era": "archaique",
    "track": "sparte",
    "category": "politics",
    "importance": 2,
    "placeId": "sparte",
    "people": [
      "lycurgue"
    ],
    "summary": "Les Spartiates attribuaient toutes leurs institutions à un législateur, Lycurgue, inspiré par l'oracle de Delphes : les deux rois, le conseil des Anciens, l'assemblée, l'éducation collective des garçons et les repas en commun. Les historiens y voient plutôt un ensemble de réformes étalées sur les VIIIe, VIIe et VIe siècles.",
    "body": "**Un personnage insaisissable.** Plutarque ouvre sa Vie de Lycurgue en avouant qu'on ne peut rien dire de lui qui ne soit contesté. Hérodote rapporte que Sparte avait d'abord les pires lois de la Grèce, puis que Lycurgue établit le bon ordre (*eunomia*), selon les uns sur l'ordre de la Pythie, selon les Spartiates eux-mêmes sur le modèle de la Crète.\n\n**La Grande Rhètra.** Plutarque cite un oracle, la Grande Rhètra, qui organise le peuple en tribus et en *obai*, crée un conseil de trente membres avec les deux rois et réunit l'assemblée à dates fixes ; un amendement attribué aux rois Théopompe et Polydore permet au conseil de casser les décisions « tordues » du peuple. Le poète Tyrtée, au VIIe siècle, en paraphrase déjà le contenu.\n\n**Ce que pensent les historiens.** L'éducation spartiate, les repas en commun et le partage égal des terres que Plutarque attribue à Lycurgue se sont formés progressivement, et une partie de cette image idéale a été construite plus tard, au IVe siècle et à l'époque hellénistique.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 65 et 66",
        "url": `${HERODOTE}:book=1:chapter=65`
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 18, 1",
        "url": `${THUCYDIDE}:book=1:chapter=18`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Lycurgue",
        "locus": "1 et 6",
        "url": `${PLUTARQUE}/Lycurgus*.html`
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Sparta and Lakonia: A Regional History 1300-362 BC, 2e éd., Londres, Routledge, 2002"
      }
    ]
  },
  {
    "id": "fondation-de-pithecusses",
    "title": "Les Eubéens s'installent à Pithécusses",
    "start": -769,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Date archéologique : les tombes et les ateliers les plus anciens remontent au deuxième quart du VIIIe siècle, vers 770 à 750, à quelques décennies près.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "society",
    "importance": 2,
    "placeId": "pithecusses",
    "summary": "Vers 770 à 750, des Grecs d'Érétrie et de Chalcis, en Eubée, s'installent sur l'île d'Ischia, dans la baie de Naples. Pithécusses, le plus ancien établissement grec durable d'Occident, est un comptoir où se côtoient Grecs, Phéniciens et indigènes, tourné vers le minerai de fer de l'île d'Elbe et vers les Étrusques.",
    "body": "**Le récit et les fouilles.** Strabon rapporte que des Érétriens et des Chalcidiens fondèrent Pithécusses et y prospérèrent, avant d'en partir à cause de querelles, puis de séismes et d'éruptions. Les fouilles de Giorgio Buchner, à partir de 1952, ont dégagé la nécropole de San Montano et un quartier de métallurgistes à Mazzola, où l'on travaillait le fer venu de l'île d'Elbe.\n\n**Un comptoir plus qu'une cité.** Les objets trouvés dans les tombes viennent de Corinthe, d'Eubée, de Phénicie, d'Égypte et d'Étrurie, et des inscriptions sémitiques montrent que des Phéniciens vivaient sur place. On y a trouvé la « coupe de Nestor », vers 725, qui porte l'un des plus anciens textes grecs en vers.\n\n**Ce qui reste discuté.** Le statut du site (simple comptoir ou véritable colonie) et sa population, estimée à quelques milliers d'habitants à la fin du VIIIe siècle, font débat. Pithécusses précède de peu Cumes, fondée en face, sur le continent.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "V, 4, 9",
        "url": `${STRABON}:book=5:chapter=4:section=9`
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "VIII, 22, 5 et 6"
      },
      {
        "kind": "modern",
        "author": "David Ridgway",
        "work": "The First Western Greeks, Cambridge, Cambridge University Press, 1992"
      },
      {
        "kind": "modern",
        "author": "Giorgio Buchner et David Ridgway",
        "work": "Pithekoussai I. La necropoli : tombe 1-723 scavate dal 1952 al 1961, Rome, Giorgio Bretschneider, 1993"
      }
    ]
  },
  {
    "id": "poemes-homeriques",
    "title": "Composition de l'Iliade et de l'Odyssée",
    "start": -749,
    "end": -669,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Aucune date antique sûre : Hérodote place Homère environ 400 ans avant lui, soit vers 850. Les modernes datent l'Iliade de 750 à 700 environ, l'Odyssée un peu après ; d'autres descendent jusqu'au milieu du VIIe siècle.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 1,
    "people": [
      "homere"
    ],
    "summary": "Dans la seconde moitié du VIIIe siècle ou au début du VIIe, les deux grandes épopées attribuées à Homère prennent la forme sous laquelle nous les lisons : l'Iliade, sur un épisode de la guerre de Troie, et l'Odyssée, sur le retour d'Ulysse. Elles deviennent le texte commun de tous les Grecs.",
    "body": "**Une poésie orale.** L'Iliade (environ 15 700 vers) et l'Odyssée (environ 12 100 vers) sont composées en hexamètres dans une langue artificielle qui mêle plusieurs dialectes. Leurs formules répétées (« Achille aux pieds rapides », « l'Aurore aux doigts de rose ») trahissent un long héritage de chanteurs, les aèdes, qui improvisaient à partir d'un stock d'expressions toutes faites.\n\n**Quand et comment ?** Les épopées décrivent un monde héroïque imaginé, qui mêle des souvenirs de l'âge du bronze (le casque en défenses de sanglier, le grand bouclier) et des réalités du VIIIe siècle. Le passage à l'écrit, rendu possible par l'alphabet, reste discuté ; une tradition tardive attribue à Pisistrate la fixation du texte à Athènes, au VIe siècle.\n\n**Un poète discuté.** Les Grecs plaçaient Homère en Ionie, à Smyrne ou à Chios, sans rien savoir de sûr de sa vie. Les modernes se demandent encore si un même auteur a composé les deux poèmes, et ce que doit chacun d'eux à la tradition orale.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 53",
        "url": `${HERODOTE}:book=2:chapter=53`
      },
      {
        "kind": "modern",
        "author": "Pierre Carlier",
        "work": "Homère, Paris, Fayard, 1999"
      },
      {
        "kind": "modern",
        "author": "Martin L. West",
        "work": "The Making of the Iliad: Disquisition and Analytical Commentary, Oxford, Oxford University Press, 2011"
      }
    ]
  },
  {
    "id": "premiere-guerre-de-messenie",
    "title": "Première guerre de Messénie",
    "start": -742,
    "end": -723,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Dates de Pausanias (de 743 à 724), calculées par olympiades à partir de sources hellénistiques ; Tyrtée, plus proche des faits, confirme seulement une guerre de vingt ans sous le roi Théopompe.",
    "era": "archaique",
    "track": "sparte",
    "category": "war",
    "importance": 2,
    "placeId": "ithome",
    "people": [
      "theopompe"
    ],
    "summary": "Selon la tradition, Sparte mène pendant vingt ans une guerre contre ses voisins de Messénie, retranchés sur le mont Ithôme, et finit par conquérir leur riche plaine. Les Messéniens deviennent des hilotes, qui cultivent la terre pour les Spartiates : ce travail forcé fonde le mode de vie spartiate.",
    "body": "**Le témoignage de Tyrtée.** Le poète spartiate Tyrtée, au VIIe siècle, chante le roi Théopompe, « par qui nous avons pris la vaste Messène », et dit que les pères de leurs pères combattirent dix-neuf ans avant que les Messéniens n'abandonnent l'Ithôme la vingtième année. C'est le seul témoignage proche des faits.\n\n**Le récit de Pausanias.** Pausanias raconte la guerre en détail, de 743 à 724, mais il suit des auteurs hellénistiques (Myron de Priène, le poète Rhianos) dont il reconnaît lui-même les invraisemblances. Ses épisodes héroïques sont en partie des inventions de l'époque où la Messénie, libérée en 369, se cherchait un passé.\n\n**Les conséquences.** La conquête double le territoire de Sparte. Les Messéniens soumis deviennent hilotes et livrent une partie de leurs récoltes ; la crainte de leurs révoltes pèse ensuite sur toute la politique spartiate.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Tyrtée",
        "work": "Fragments élégiaques",
        "locus": "fr. 5 West"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "IV, 5 à 13",
        "url": `${PAUSANIAS}:book=4:chapter=5`
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Sparta and Lakonia: A Regional History 1300-362 BC, 2e éd., Londres, Routledge, 2002"
      }
    ]
  },
  {
    "id": "fondation-de-cumes",
    "title": "Fondation de Cumes",
    "start": -739,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Les auteurs antiques en font la plus ancienne colonie d'Italie, sans date fiable ; les tombes grecques les plus anciennes du site datent de 740 à 720 environ.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "politics",
    "importance": 2,
    "placeId": "cumes",
    "summary": "Vers 740 à 730, des Grecs de Chalcis, en Eubée, venus de Pithécusses, fondent Cumes sur la côte de Campanie. C'est la première colonie grecque du continent italien ; par elle, l'alphabet eubéen passe aux Étrusques puis aux Latins.",
    "body": "**Le récit.** Strabon tient Cumes pour la plus ancienne des cités grecques de Sicile et d'Italie, fondée par des Chalcidiens et des gens de Kymè, sous deux chefs, Hippoclès et Mégasthène. Tite-Live précise que les colons, partis de Chalcis, avaient d'abord abordé à Pithécusses avant de passer sur le continent.\n\n**Une cité ouverte sur l'Italie.** Installée sur une acropole qui domine la mer, plus tard célèbre pour sa Sibylle, Cumes contrôle la plaine fertile de Campanie et commerce avec les Étrusques et les Latins. L'alphabet de type eubéen qu'on y utilise est à l'origine de l'alphabet étrusque, puis de l'alphabet latin.\n\n**Ce qui reste incertain.** La date exacte et le lien avec Pithécusses (fondation distincte ou déplacement d'une partie des habitants) sont discutés. La céramique place les premières tombes grecques dans le dernier tiers du VIIIe siècle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "V, 4, 4",
        "url": `${STRABON}:book=5:chapter=4:section=4`
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "VIII, 22, 5 et 6"
      },
      {
        "kind": "modern",
        "author": "David Ridgway",
        "work": "The First Western Greeks, Cambridge, Cambridge University Press, 1992"
      },
      {
        "kind": "modern",
        "author": "Mogens Herman Hansen et Thomas Heine Nielsen (dir.)",
        "work": "An Inventory of Archaic and Classical Poleis, Oxford, Oxford University Press, 2004"
      }
    ]
  },
  {
    "id": "fondation-de-naxos-de-sicile",
    "title": "Fondation de Naxos, première colonie grecque de Sicile",
    "start": -733,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Date déduite de Thucydide, qui place Naxos un an avant Syracuse, soit 734 ; la céramique du site s'accorde avec le dernier tiers du VIIIe siècle.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "politics",
    "importance": 2,
    "placeId": "naxos-de-sicile",
    "people": [
      "thoucles"
    ],
    "summary": "Selon Thucydide, des Chalcidiens d'Eubée conduits par Thouclès fondent Naxos sur la côte orientale de la Sicile, un an avant Syracuse. Leur autel d'Apollon Archégète devient le lieu où tous les Grecs de Sicile sacrifient avant de partir en ambassade vers les sanctuaires de Grèce.",
    "body": "**Le récit.** Thucydide ouvre la liste des fondations grecques de Sicile par Naxos, créée par des Chalcidiens sous la conduite de Thouclès. Il précise que l'autel d'Apollon Archégète (« le fondateur ») se trouve hors de la ville, et que les ambassadeurs des cités siciliennes y sacrifient avant de s'embarquer. Strabon, d'après Éphore, fait de Thouclès un Athénien poussé en Sicile par les vents.\n\n**Une métropole à son tour.** Cinq ans après Syracuse, Thouclès et les Chalcidiens de Naxos fondent Léontinoi, puis Catane, dans les plaines de l'intérieur. Naxos reste une petite cité ; elle est détruite par Denys l'Ancien en 403.\n\n**La date.** Thucydide donne des intervalles plutôt que des années ; les modernes en tirent 734 pour Naxos et 733 pour Syracuse. Les fouilles du cap Schisò ont livré une céramique compatible avec cette chronologie.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI, 3, 1 et 3",
        "url": `${THUCYDIDE}:book=6:chapter=3`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VI, 2, 2",
        "url": `${STRABON}:book=6:chapter=2:section=2`
      },
      {
        "kind": "modern",
        "author": "Franco De Angelis",
        "work": "Archaic and Classical Greek Sicily: A Social and Economic History, Oxford, Oxford University Press, 2016"
      }
    ]
  },
  {
    "id": "fondation-de-megara-hyblaea",
    "title": "Fondation de Mégara Hyblaea",
    "start": -727,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Date déduite de Thucydide : les Mégariens vécurent 245 ans dans leur cité avant d'en être chassés par Gélon vers 483, d'où 728 environ.",
    "era": "archaique",
    "track": "occident",
    "category": "politics",
    "importance": 3,
    "placeId": "megara-hyblaea",
    "summary": "Après plusieurs essais malheureux sur la côte orientale de la Sicile, des colons de Mégare reçoivent d'un roi sicule, Hyblon, un territoire au nord de Syracuse. Leur cité, Mégara Hyblaea, possède très tôt un plan régulier, l'un des plus anciens du monde grec.",
    "body": "**Une installation difficile.** Thucydide raconte que Lamis, venu de Mégare, s'établit d'abord à Trotilon, puis chez les Chalcidiens de Léontinoi, qui le chassent, et enfin à Thapsos, où il meurt. Ses compagnons reçoivent alors du roi sicule Hyblon un territoire où ils fondent Mégara, dite Hyblaea en son honneur.\n\n**Un urbanisme précoce.** Les fouilles françaises menées depuis 1949 ont montré qu'au VIIe siècle la ville est divisée en lots par des rues rectilignes, autour d'une agora trapézoïdale laissée libre dès l'origine. C'est l'un des meilleurs témoignages du partage des terres entre colons.\n\n**Une fin brutale.** Cent ans après sa fondation, Mégara fonde à son tour Sélinonte, à l'ouest de l'île. Vers 483, Gélon de Syracuse prend la ville, installe les riches à Syracuse et vend le peuple comme esclave.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI, 4, 1 et 2",
        "url": `${THUCYDIDE}:book=6:chapter=4`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VII, 156",
        "url": `${HERODOTE}:book=7:chapter=156`
      },
      {
        "kind": "modern",
        "author": "Michel Gras, Henri Tréziny et Henri Broise",
        "work": "Mégara Hyblaea 5. La ville archaïque, Rome, École française de Rome, 2004"
      }
    ]
  },
  {
    "id": "fondation-de-tarente",
    "title": "Fondation de Tarente",
    "start": -705,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Date traditionnelle de 706, transmise par la chronique d'Eusèbe ; la céramique la plus ancienne du site date de la fin du VIIIe siècle.",
    "era": "archaique",
    "track": "occident",
    "category": "politics",
    "importance": 3,
    "placeId": "tarente",
    "people": [
      "phalanthos"
    ],
    "summary": "Selon la tradition, des Spartiates exclus de la citoyenneté, les Parthénies, menés par Phalanthos, fondent Tarente sur le golfe du même nom, en Italie du Sud. C'est la seule colonie fondée par Sparte, et l'une des cités les plus riches de la Grande-Grèce.",
    "body": "**La légende des Parthénies.** Antiochos de Syracuse, cité par Strabon, raconte que les fils nés pendant la guerre de Messénie de Spartiates restés à l'arrière furent privés de droits et appelés Parthénies, « fils de vierges ». Leur complot découvert, ils partent sous la conduite de Phalanthos, sur l'ordre de Delphes, et s'installent à Satyrion puis à Tarente. Éphore, toujours chez Strabon, donne une version un peu différente.\n\n**Une grande cité.** Tarente occupe une presqu'île entre une lagune, la « petite mer », et la haute mer, avec le meilleur port de la côte. Elle devient au IVe siècle la principale cité grecque d'Italie, avant d'appeler Pyrrhos contre Rome en 281.\n\n**Ce qui est sûr.** Le récit des Parthénies est une légende qui explique l'origine des colons ; les objets laconiens trouvés à Tarente confirment toutefois des liens étroits avec Sparte dès la fin du VIIIe siècle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VI, 3, 2 et 3 (d'après Antiochos et Éphore)",
        "url": `${STRABON}:book=6:chapter=3:section=2`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "X, 10, 6 à 8",
        "url": `${PAUSANIAS}:book=10:chapter=10`
      },
      {
        "kind": "modern",
        "author": "Irad Malkin",
        "work": "Myth and Territory in the Spartan Mediterranean, Cambridge, Cambridge University Press, 1994"
      }
    ]
  },
  {
    "id": "hesiode",
    "title": "Hésiode compose la Théogonie et les Travaux et les Jours",
    "start": -699,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Date déduite des poèmes eux-mêmes et de leur langue : vers 700, à une génération près ; certains placent Hésiode avant Homère.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "ascra",
    "people": [
      "hesiode"
    ],
    "summary": "Vers 700, un paysan-poète d'Ascra, en Béotie, compose la Théogonie, qui raconte la naissance des dieux et le règne de Zeus, et les Travaux et les Jours, poème sur le travail de la terre et la justice. Hésiode est le premier poète grec qui parle de lui-même.",
    "body": "**Un poète qui se raconte.** Hésiode dit que son père, parti de Kymè en Éolide pour fuir la pauvreté, s'installa à Ascra, « village misérable, dur l'hiver, pénible l'été, jamais agréable ». Il raconte aussi que les Muses lui apparurent sur l'Hélicon pendant qu'il gardait ses moutons, et qu'il gagna un trépied à Chalcis aux jeux funèbres d'Amphidamas.\n\n**Deux poèmes fondateurs.** La Théogonie ordonne les générations divines, du Chaos à Zeus, en passant par Ouranos et Cronos ; elle s'inspire en partie de mythes du Proche-Orient. Les Travaux et les Jours, adressés à son frère Persès, donnent un calendrier agricole, le mythe des races et celui de Pandore, et un éloge de la justice contre les « rois mangeurs de présents ».\n\n**Ce qui reste discuté.** Hérodote fait d'Hésiode un contemporain d'Homère. Les modernes hésitent sur l'ordre des deux poètes et sur la part du poète dans l'œuvre qu'on lui attribue ; l'existence d'un Hésiode historique est généralement admise.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hésiode",
        "work": "Les Travaux et les Jours",
        "locus": "v. 633 à 640 et 650 à 659"
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 53",
        "url": `${HERODOTE}:book=2:chapter=53`
      },
      {
        "kind": "modern",
        "author": "Martin L. West (éd.)",
        "work": "Hesiod, Theogony, Oxford, Clarendon Press, 1966"
      }
    ]
  },
  {
    "id": "pheidon-d-argos",
    "title": "Pheidon d'Argos",
    "start": -667,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Pausanias le place lors de la 8e olympiade (748), que beaucoup de modernes corrigent en 28e (668) ; Hérodote en fait le père d'un prétendant des années 570. Sa date flotte donc sur plus d'un siècle.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "politics",
    "importance": 3,
    "placeId": "argos",
    "people": [
      "pheidon"
    ],
    "summary": "Pheidon, roi d'Argos, impose la puissance de sa cité dans le Péloponnèse, s'empare de la présidence des Jeux d'Olympie et laisse son nom à un système de poids et mesures. Il est souvent daté vers 670, mais sa chronologie est l'une des plus discutées de l'époque archaïque.",
    "body": "**Ce que disent les sources.** Hérodote parle de Pheidon, « tyran des Argiens », qui fixa des mesures pour les Péloponnésiens, chassa les organisateurs éléens et présida lui-même les Jeux olympiques. Pausanias date cette usurpation de la 8e olympiade, avec l'appui des Pisates. Aristote cite Pheidon comme exemple de roi devenu tyran.\n\n**Les mesures et la monnaie.** Éphore, cité par Strabon, lui attribue les mesures « pheidoniennes » et la première monnaie d'argent, frappée à Égine. Cette dernière attribution est impossible : les premières monnaies d'Égine datent du VIe siècle.\n\n**La date.** Beaucoup d'historiens corrigent la date de Pausanias en 668 et rapprochent Pheidon de la victoire d'Argos sur Sparte à Hysiai, que Pausanias place en 669. D'autres préfèrent le VIIIe siècle ou suivent Hérodote. Rien ne permet de trancher.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VI, 127, 3",
        "url": `${HERODOTE}:book=6:chapter=127`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "VI, 22, 2 et II, 24, 7",
        "url": `${PAUSANIAS}:book=6:chapter=22`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VIII, 3, 33",
        "url": `${STRABON}:book=8:chapter=3:section=33`
      },
      {
        "kind": "modern",
        "author": "Thomas Kelly",
        "work": "A History of Argos to 500 B.C., Minneapolis, University of Minnesota Press, 1976"
      }
    ]
  },
  {
    "id": "fondation-de-byzance",
    "title": "Fondation de Byzance",
    "start": -659,
    "precision": "decade",
    "certainty": "traditional",
    "certaintyNote": "Date des chronographes (vers 660 selon la chronique d'Eusèbe) ; Hérodote dit seulement que Chalcédoine fut fondée dix-sept ans plus tôt. Les plus anciens objets grecs du site datent du VIIe siècle.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "politics",
    "importance": 2,
    "placeId": "byzance",
    "people": [
      "byzas"
    ],
    "summary": "Vers 660, des colons de Mégare s'installent à l'entrée du Bosphore, sur le promontoire qui deviendra Constantinople puis Istanbul. Byzance contrôle le passage entre la mer Égée et la mer Noire, ses blés et ses pêcheries de thon.",
    "body": "**« La ville des aveugles ».** Hérodote raconte que le Perse Mégabaze traita d'aveugles les habitants de Chalcédoine, sur la rive d'Asie : fondée dix-sept ans avant Byzance, leur cité avait négligé le meilleur emplacement, juste en face. Tacite rapporte qu'Apollon avait ordonné aux fondateurs de Byzance de s'établir « en face du pays des aveugles ».\n\n**Un site exceptionnel.** Le promontoire est bordé par la Corne d'Or, un port naturel profond, et par le Bosphore, où les bancs de thons venus de la mer Noire assurent une pêche abondante. Byzance prélève aussi des droits sur les navires qui franchissent le détroit, ce qui en fait un enjeu constant entre Athènes, Sparte et la Perse.\n\n**Les fondateurs.** La colonie est mégarienne, peut-être avec d'autres Grecs. Le héros Byzas, qui aurait donné son nom à la ville, n'apparaît que dans des récits tardifs.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "IV, 144",
        "url": `${HERODOTE}:book=4:chapter=144`
      },
      {
        "kind": "ancient",
        "author": "Tacite",
        "work": "Annales",
        "locus": "XII, 63"
      },
      {
        "kind": "modern",
        "author": "Mogens Herman Hansen et Thomas Heine Nielsen (dir.)",
        "work": "An Inventory of Archaic and Classical Poleis, Oxford, Oxford University Press, 2004"
      }
    ]
  },
  {
    "id": "tyrannie-de-cypselos",
    "title": "Cypsélos, tyran de Corinthe",
    "start": -656,
    "end": -582,
    "precision": "decade",
    "certainty": "traditional",
    "certaintyNote": "Dates traditionnelles (de 657 à 583) reconstruites à partir des durées de règne données par Aristote ; une chronologie basse, défendue par certains, descend d'une quarantaine d'années.",
    "era": "archaique",
    "track": "corinthe",
    "category": "politics",
    "importance": 2,
    "placeId": "corinthe",
    "people": [
      "cypselos",
      "periandre"
    ],
    "summary": "Vers 657, Cypsélos renverse les Bacchiades, l'aristocratie qui gouvernait Corinthe, et devient tyran. Son fils Périandre lui succède : sous leur dynastie, Corinthe fonde des colonies sur la mer Ionienne et domine le commerce entre la Grèce et l'Occident.",
    "body": "**Le récit d'Hérodote.** Les Bacchiades se mariaient entre eux. L'une de leurs filles, Labda, boiteuse, épouse un homme d'un autre clan ; un oracle annonce que son fils renversera les Bacchiades. Ceux-ci envoient des hommes pour tuer l'enfant, mais sa mère le cache dans un coffre (*kypselê*), d'où son nom. Devenu adulte, Cypsélos prend le pouvoir et règne trente ans.\n\n**Périandre.** Son fils Périandre, plus dur selon Hérodote, entretient des liens avec le tyran Thrasybule de Milet et avec l'Égypte. Corinthe fonde alors Leucade, Anactorion, Ambracie et Potidée. Le *diolkos*, chaussée dallée qui permettait de tirer les navires à travers l'isthme, date de la même époque. Aristote compte 73 ans et demi pour toute la dynastie.\n\n**Ce qui reste discuté.** Le récit de la naissance est un conte ; les dates reposent sur des calculs antiques. Pour Hérodote, qui écrit pour un public hostile aux tyrans, Périandre est le modèle du despote ; d'autres le comptaient parmi les Sept Sages.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 92",
        "url": `${HERODOTE}:book=5:chapter=92`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Politique",
        "locus": "V, 12, 1315b"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": "Korinthiaka. Recherches sur l'histoire et la civilisation de Corinthe des origines aux guerres médiques, Paris, De Boccard, 1955"
      }
    ]
  },
  {
    "id": "seconde-guerre-de-messenie",
    "title": "Seconde guerre de Messénie",
    "start": -649,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Pausanias la date de 685 à 668 ; Tyrtée, qui y prit part, la situe deux générations après la première, ce qui conduit les modernes vers le milieu du VIIe siècle ou plus tard.",
    "era": "archaique",
    "track": "sparte",
    "category": "war",
    "importance": 3,
    "placeId": "eira",
    "people": [
      "tyrtee",
      "aristomene"
    ],
    "summary": "Au VIIe siècle, les Messéniens se révoltent contre Sparte. La guerre est longue et dure ; le poète Tyrtée exhorte les Spartiates à tenir leur rang dans la ligne de bataille. Sparte l'emporte et resserre son emprise sur les hilotes de Messénie.",
    "body": "**Tyrtée, poète de la guerre.** Les élégies de Tyrtée, en partie conservées, appellent les jeunes Spartiates à combattre au premier rang, bouclier contre bouclier, et à préférer une belle mort à la fuite. Elles décrivent une guerre d'hoplites en rangs serrés et témoignent d'une crise intérieure : Aristote rapporte que, selon Tyrtée, certains réclamaient un nouveau partage des terres.\n\n**Le récit de Pausanias.** Pausanias fait d'Aristomène le héros de la révolte et raconte un siège de onze ans de la place forte d'Eira, au nord de la Messénie. Ce récit, tiré du poète hellénistique Rhianos, relève largement de la légende.\n\n**Les conséquences.** Après cette guerre, Sparte organise la société des égaux, entraînés au combat et nourris par le travail des hilotes. La date et même l'existence d'une guerre unique et bien délimitée restent discutées.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Tyrtée",
        "work": "Fragments élégiaques",
        "locus": "fr. 5, 10, 11 et 12 West"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "IV, 14 à 24",
        "url": `${PAUSANIAS}:book=4:chapter=14`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Politique",
        "locus": "V, 7, 1306b-1307a"
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Sparta and Lakonia: A Regional History 1300-362 BC, 2e éd., Londres, Routledge, 2002"
      }
    ]
  },
  {
    "id": "tentative-de-cylon",
    "title": "Tentative de tyrannie de Cylon à Athènes",
    "start": -631,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Le coup eut lieu une année olympique après la victoire de Cylon à Olympie (640 selon la tradition), donc en 636 ou en 632, plus probablement 632.",
    "era": "archaique",
    "track": "athenes",
    "category": "politics",
    "importance": 3,
    "placeId": "athenes",
    "people": [
      "cylon",
      "megacles"
    ],
    "summary": "Vers 632, l'aristocrate Cylon, vainqueur olympique et gendre du tyran de Mégare, s'empare de l'Acropole pour devenir tyran d'Athènes. Le peuple ne le suit pas ; ses partisans, réfugiés auprès des autels, sont massacrés malgré la promesse qu'on leur avait faite, et cette souillure poursuit pendant deux siècles la famille des Alcméonides.",
    "body": "**Le coup manqué.** Thucydide raconte que Cylon, sur la foi d'un oracle de Delphes qui lui conseillait d'agir « pendant la plus grande fête de Zeus », occupa l'Acropole pendant les Jeux olympiques, avec l'aide de soldats envoyés par son beau-père Théagène. Les Athéniens accoururent des champs et l'assiégèrent ; Cylon et son frère s'enfuirent.\n\n**Le sacrilège.** Ses partisans, affamés, s'assirent en suppliants près de l'autel. Les magistrats leur promirent la vie sauve, puis les mirent à mort, certains jusque sur les autels des Euménides. Les responsables, dont l'archonte Mégaclès, de la famille des Alcméonides, furent déclarés maudits.\n\n**Une malédiction politique.** Cette souillure sert d'argument contre les descendants de Mégaclès : Sparte l'invoque contre Clisthène en 508, puis contre Périclès en 432. L'épisode montre aussi que la tyrannie n'avait pas encore d'appuis dans le peuple athénien.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 126, 3 à 12",
        "url": `${THUCYDIDE}:book=1:chapter=126`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 71",
        "url": `${HERODOTE}:book=5:chapter=71`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Solon",
        "locus": "12",
        "url": `${PLUTARQUE}/Solon*.html`
      },
      {
        "kind": "modern",
        "author": "P. J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "fondation-de-cyrene",
    "title": "Fondation de Cyrène",
    "start": -630,
    "precision": "decade",
    "certainty": "traditional",
    "certaintyNote": "Date traditionnelle de 631, transmise par les chronographes ; la céramique la plus ancienne du site date du dernier tiers du VIIe siècle.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "politics",
    "importance": 2,
    "placeId": "cyrene",
    "people": [
      "battos-ier"
    ],
    "summary": "Vers 631, sur l'ordre de l'oracle de Delphes, des colons de l'île de Théra menés par Battos s'installent en Libye, d'abord sur une île côtière, puis sur un plateau fertile près d'une source consacrée à Apollon. Cyrène devient une riche cité de blé, de chevaux et de silphion, gouvernée par les rois Battiades.",
    "body": "**Deux récits.** Hérodote donne une version des Théréens et une version des Cyrénéens. Dans les deux, la Pythie ordonne de fonder une ville en Libye ; les Théréens, qui ignorent où se trouve ce pays, n'obéissent qu'après une sécheresse de sept ans. Les colons passent deux ans sur l'île de Platéa, six ans à Aziris, puis des Libyens les conduisent à la source d'Apollon.\n\n**Un document exceptionnel.** Une inscription de Cyrène du IVe siècle prétend reproduire le « serment des fondateurs » : chaque famille de Théra doit fournir un fils, et quiconque refuse de partir est puni de mort. Son authenticité est discutée, mais elle montre comment une colonie pouvait être imposée par la cité mère.\n\n**Une royauté grecque en Afrique.** Huit rois, alternativement nommés Battos et Arcésilas, règnent sur Cyrène jusqu'au milieu du Ve siècle. La cité exporte le silphion, une plante médicinale et condimentaire aujourd'hui disparue.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "IV, 150 à 159",
        "url": `${HERODOTE}:book=4:chapter=150`
      },
      {
        "kind": "ancient",
        "author": "Inscription",
        "work": "Décret des Théréens et serment des fondateurs (SEG IX, 3)",
        "locus": "R. Meiggs et D. Lewis, A Selection of Greek Historical Inscriptions, n° 5"
      },
      {
        "kind": "modern",
        "author": "François Chamoux",
        "work": "Cyrène sous la monarchie des Battiades, Paris, De Boccard, 1953"
      }
    ]
  },
  {
    "id": "premieres-monnaies-lydiennes",
    "title": "Premières monnaies, en Lydie et en Ionie",
    "start": -629,
    "end": -599,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Date tirée surtout du dépôt de fondation de l'Artémision d'Éphèse, daté selon les fouilleurs entre 650 et 600 environ ; les premières frappes elles-mêmes ne sont pas datées avec précision.",
    "era": "archaique",
    "track": "ionie",
    "category": "society",
    "importance": 1,
    "placeId": "sardes",
    "summary": "Dans le dernier tiers du VIIe siècle, en Lydie et dans les cités grecques voisines, on frappe les premières monnaies : de petits lingots d'électrum, alliage naturel d'or et d'argent, de poids fixe et marqués d'un poinçon. L'invention se répand ensuite dans tout le monde grec.",
    "body": "**Ce que dit Hérodote.** Selon Hérodote, les Lydiens furent les premiers à frapper et à utiliser des monnaies d'or et d'argent, et les premiers aussi à faire du commerce de détail. L'électrum venait des sables du Pactole, la rivière qui traverse Sardes, la capitale lydienne.\n\n**Ce que montrent les fouilles.** Les plus anciennes monnaies datées par leur contexte ont été trouvées dans le dépôt de fondation du temple d'Artémis à Éphèse : des pièces d'électrum, certaines lisses, d'autres frappées d'une tête de lion, l'emblème royal lydien. Une pièce de la même époque, trouvée en Carie, porte l'inscription « je suis l'emblème de Phanès ».\n\n**Ce qui reste discuté.** L'usage premier de ces pièces (paiement de mercenaires, offrandes, taxes, échanges) est débattu, de même que la date exacte, entre 650 et 600 environ. Les premières monnaies d'or et d'argent purs, attribuées à Crésus, pourraient dater du début de la domination perse.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 94, 1",
        "url": `${HERODOTE}:book=1:chapter=94`
      },
      {
        "kind": "modern",
        "author": "Colin M. Kraay",
        "work": "Archaic and Classical Greek Coins, Londres, Methuen, 1976"
      },
      {
        "kind": "modern",
        "author": "William E. Metcalf (dir.)",
        "work": "The Oxford Handbook of Greek and Roman Coinage, Oxford, Oxford University Press, 2012"
      }
    ]
  },
  {
    "id": "lois-de-dracon",
    "title": "Lois de Dracon",
    "start": -620,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Année archontale 621/620 (archontat d'Aristaichmos) selon la Constitution des Athéniens, qui chevauche deux de nos années ; la « constitution de Dracon » décrite par le même texte est jugée inventée.",
    "era": "archaique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "dracon"
    ],
    "summary": "En 621/620, Dracon donne aux Athéniens leurs premières lois écrites. Leur sévérité est restée proverbiale, mais leur apport durable est la loi sur l'homicide, qui distingue le meurtre volontaire de l'homicide involontaire et retire la vengeance aux familles pour la confier aux tribunaux.",
    "body": "**Des lois écrites.** Mettre les lois par écrit limite l'arbitraire des aristocrates qui rendaient la justice. La Constitution des Athéniens date ces lois de l'archontat d'Aristaichmos ; elle prête aussi à Dracon une constitution complète, que les historiens tiennent pour une invention de la fin du Ve siècle.\n\n**La loi sur l'homicide.** En 409/408, les Athéniens font regraver la loi de Dracon sur l'homicide, et cette copie sur pierre nous est parvenue en partie. Elle prévoit l'exil pour l'homicide involontaire et permet à la famille de la victime d'accorder le pardon. Solon abolit les autres lois de Dracon, mais conserve celle-ci.\n\n**« Écrites avec du sang ».** Plutarque rapporte que la mort punissait presque tous les délits, même le vol de légumes, et cite le mot de l'orateur Démade : Dracon avait écrit ses lois avec du sang et non avec de l'encre. D'où l'adjectif « draconien ».",
    "sources": [
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Constitution des Athéniens",
        "locus": "4, 1 et 7, 1"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Solon",
        "locus": "17",
        "url": `${PLUTARQUE}/Solon*.html`
      },
      {
        "kind": "ancient",
        "author": "Inscription",
        "work": "Loi de Dracon sur l'homicide, regravée en 409/408",
        "locus": "IG I³ 104"
      },
      {
        "kind": "modern",
        "author": "Ronald S. Stroud",
        "work": "Drakon's Law on Homicide, Berkeley, University of California Press, 1968"
      }
    ]
  },
  {
    "id": "sappho-et-alcee",
    "title": "Sappho et Alcée à Lesbos",
    "start": -599,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Les deux poètes sont contemporains de Pittacos, au pouvoir à Mytilène vers 590 à 580 ; leurs dates de naissance et de mort sont inconnues.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "mytilene",
    "people": [
      "sappho",
      "alcee",
      "pittacos"
    ],
    "summary": "Vers 600, à Mytilène, sur l'île de Lesbos, Sappho et Alcée composent des poèmes lyriques chantés à la lyre : chants d'amour, hymnes et chants de noces chez Sappho, poèmes de banquet et de combat politique chez Alcée. Ils comptent parmi les premières voix personnelles de la littérature européenne.",
    "body": "**Sappho.** Ses poèmes, réunis plus tard en neuf livres, ne nous sont parvenus que par fragments : citations d'auteurs anciens et papyrus d'Égypte. L'hymne à Aphrodite, conservé en entier, et le poème qui décrit les effets du désir (« ma langue se brise ») font partie des textes les plus célèbres de l'Antiquité. Hérodote rapporte qu'elle se moqua de son frère Charaxos, qui avait racheté une courtisane à Naucratis.\n\n**Alcée.** Aristocrate engagé dans les luttes de Mytilène, il combat les tyrans, puis Pittacos, que la cité élit pour dix ans comme arbitre ; Aristote cite les vers où il s'en plaint. Hérodote raconte qu'il abandonna ses armes en fuyant lors d'une guerre contre Athènes à Sigée.\n\n**Ce qui reste incertain.** On ignore presque tout de la vie de Sappho. Les récits anciens (son exil en Sicile, son saut de la falaise de Leucade par amour) sont tardifs ou légendaires.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIII, 2, 3",
        "url": `${STRABON}:book=13:chapter=2:section=3`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "II, 135 et V, 95",
        "url": `${HERODOTE}:book=2:chapter=135`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Politique",
        "locus": "III, 14, 1285a"
      },
      {
        "kind": "modern",
        "author": "Denys Page",
        "work": "Sappho and Alcaeus: An Introduction to the Study of Ancient Lesbian Poetry, Oxford, Clarendon Press, 1955"
      }
    ]
  },
  {
    "id": "temple-d-hera-a-olympie",
    "title": "Temple d'Héra à Olympie et premiers temples doriques",
    "start": -599,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Le temple d'Héra est daté vers 600 par la plupart des archéologues, entre 650 et 590 selon les études ; ses colonnes de bois ont été remplacées une à une par des colonnes de pierre.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "building",
    "importance": 2,
    "placeId": "olympie",
    "summary": "Vers 600, les Éléens élèvent à Olympie un temple d'Héra entouré de colonnes, d'abord en bois, que l'on remplace peu à peu par des colonnes de pierre. Au même moment, à Corcyre et à Syracuse, apparaissent les premiers temples doriques entièrement en pierre : l'ordre dorique est né.",
    "body": "**Un temple en transition.** Pausanias décrit le temple d'Héra comme dorique, entouré de colonnes, et note que l'une des deux colonnes de l'opisthodome (la pièce arrière) est encore en bois de chêne. Les fouilles montrent un soubassement de pierre, des murs de briques crues et des colonnes de pierre de styles et d'époques différents : elles ont remplacé, au fil des siècles, des colonnes de bois.\n\n**Les premiers temples de pierre.** Au VIIe siècle, le temple d'Apollon à Thermon, en Étolie, garde une structure de bois, mais porte déjà des métopes de terre cuite peintes. Vers 580, le temple d'Artémis à Corcyre, avec sa grande Gorgone au fronton, et le temple d'Apollon à Syracuse sont entièrement en pierre.\n\n**Pourquoi c'est important.** L'ordre dorique (colonnes sans base, chapiteau simple, frise de triglyphes et de métopes) fixe pour des siècles l'image du temple grec. Plusieurs de ses détails semblent transposer dans la pierre une ancienne charpente de bois.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "V, 16, 1",
        "url": `${PAUSANIAS}:book=5:chapter=16`
      },
      {
        "kind": "modern",
        "author": "Alfred Mallwitz",
        "work": "Olympia und seine Bauten, Munich, Prestel, 1972"
      },
      {
        "kind": "modern",
        "author": "Marie-Christine Hellmann",
        "work": "L'architecture grecque, 2. Architecture religieuse et funéraire, Paris, Picard, 2006"
      }
    ]
  },
  {
    "id": "premiers-kouroi-de-marbre",
    "title": "Premiers kouroi de marbre",
    "start": -599,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Datation stylistique : les plus anciens grands kouroi de marbre, comme ceux du cap Sounion, sont placés vers 600 à 580, à une ou deux décennies près.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "sounion",
    "summary": "Vers 600, les sculpteurs grecs taillent dans le marbre des Cyclades de grandes statues de jeunes hommes nus, debout, une jambe en avant : les kouroi. Inspirés de la statuaire égyptienne, ils servent d'offrandes dans les sanctuaires ou de monuments sur les tombes, et marquent le début de la grande sculpture grecque.",
    "body": "**Un modèle égyptien.** Depuis le milieu du VIIe siècle, des Grecs fréquentent l'Égypte comme mercenaires et marchands. Diodore rapporte que deux sculpteurs de Samos, Téléclès et Théodoros, réalisèrent chacun une moitié d'une statue d'Apollon, l'un à Samos, l'autre à Éphèse, selon les proportions égyptiennes, et que les deux moitiés s'ajustèrent parfaitement.\n\n**Les premiers grands kouroi.** Les kouroi du sanctuaire de Poséidon au cap Sounion, hauts de plus de trois mètres, le kouros dit de New York et les jumeaux d'Argos dédiés à Delphes, que l'on identifie souvent à Cléobis et Biton dont Hérodote raconte l'histoire, datent du début du VIe siècle. Contrairement aux statues égyptiennes, ils sont nus et détachés de tout pilier.\n\n**Un siècle d'évolution.** Des premiers kouroi à ceux de la fin du VIe siècle (Kroïsos d'Anavyssos, Aristodikos), l'anatomie devient de plus en plus naturelle. Les historiens de l'art s'en servent comme d'une échelle pour dater la sculpture archaïque, avec une marge de quelques décennies.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "I, 98, 5 à 9",
        "url": `${DIODORE}:book=1:chapter=98`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 31",
        "url": `${HERODOTE}:book=1:chapter=31`
      },
      {
        "kind": "modern",
        "author": "Gisela M. A. Richter",
        "work": "Kouroi: Archaic Greek Youths, 3e éd., Londres, Phaidon, 1970"
      }
    ]
  },
  {
    "id": "reformes-de-solon",
    "title": "Réformes de Solon",
    "start": -593,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Solon est archonte en 594/593, année archontale qui chevauche deux de nos années ; quelques historiens placent ses lois une vingtaine d'années plus tard.",
    "era": "archaique",
    "track": "athenes",
    "category": "politics",
    "importance": 1,
    "placeId": "athenes",
    "people": [
      "solon"
    ],
    "summary": "En 594/593, alors qu'Athènes est déchirée entre riches et pauvres endettés, Solon est nommé archonte et arbitre. Il annule les dettes qui pesaient sur les terres et les personnes, interdit l'esclavage pour dettes, classe les citoyens selon leurs revenus et donne à tous un accès aux tribunaux : ses lois préparent la démocratie athénienne.",
    "body": "**La crise.** Selon la Constitution des Athéniens, les pauvres travaillaient les terres des riches et, s'ils ne payaient pas leur part, pouvaient être vendus comme esclaves avec leur famille. Solon, aristocrate et poète, est choisi pour réconcilier les deux camps.\n\n**La « levée du fardeau ».** Par la *seisachtheia*, il annule les dettes, fait arracher les bornes qui marquaient les terres engagées et rachète des Athéniens vendus à l'étranger, comme il le dit lui-même dans un poème. Il répartit les citoyens en quatre classes selon la production de leurs terres (pentacosiomédimnes, cavaliers, zeugites et thètes) : les charges dépendent désormais de la richesse, non plus de la naissance. Tout citoyen peut faire appel devant un tribunal populaire et poursuivre un délit au nom d'une victime. Ses lois sont affichées sur des panneaux de bois pivotants, les *axones*.\n\n**Ce qui reste discuté.** La création d'un Conseil de 400 membres, que lui prête Aristote, est discutée. Solon quitte Athènes pour dix ans afin de ne pas modifier ses lois ; les conflits reprennent après son départ et ouvrent la voie à la tyrannie de Pisistrate.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Constitution des Athéniens",
        "locus": "5 à 12"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Solon",
        "locus": "14 à 25",
        "url": `${PLUTARQUE}/Solon*.html`
      },
      {
        "kind": "ancient",
        "author": "Solon",
        "work": "Fragments",
        "locus": "fr. 36 West (cité par Aristote, Constitution des Athéniens, 12, 4)"
      },
      {
        "kind": "modern",
        "author": "P. J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      },
      {
        "kind": "modern",
        "author": "Josine H. Blok et André P. M. H. Lardinois (dir.)",
        "work": "Solon of Athens: New Historical and Philological Approaches, Leyde, Brill, 2006"
      }
    ]
  },
  {
    "id": "eclipse-de-thales",
    "title": "Éclipse de Thalès",
    "start": -584,
    "month": 5,
    "day": 28,
    "precision": "day",
    "certainty": "debated",
    "certaintyNote": "L'éclipse totale du 28 mai 585 (calendrier julien) est certaine, et on l'identifie en général à celle d'Hérodote ; que Thalès l'ait vraiment prédite est très discuté.",
    "era": "archaique",
    "track": "ionie",
    "category": "culture",
    "importance": 2,
    "placeId": "milet",
    "people": [
      "thales",
      "alyatte"
    ],
    "summary": "Pendant une bataille entre les Lydiens d'Alyatte et les Mèdes, le jour se change soudain en nuit ; effrayés, les deux camps font la paix. Hérodote affirme que Thalès de Milet avait annoncé l'année de ce phénomène, une éclipse de soleil que les astronomes datent du 28 mai 585.",
    "body": "**Le récit d'Hérodote.** Lydiens et Mèdes se battaient depuis cinq ans quand, la sixième année, au milieu d'une bataille, le jour devint nuit. Thalès avait prédit ce changement, en fixant l'année où il se produirait. Les rois de Cilicie et de Babylone négocient la paix, scellée par un mariage, et le fleuve Halys devient la frontière entre les deux royaumes.\n\n**Thalès, premier savant grec.** Aristote voit en Thalès le premier des philosophes de la nature, pour qui l'eau est le principe de toutes choses. Les Grecs lui attribuaient aussi des théorèmes de géométrie, la mesure de la hauteur des pyramides par leur ombre et des conseils politiques aux Ioniens.\n\n**Une prédiction possible ?** L'éclipse du 28 mai 585, totale en Asie Mineure, correspond bien au récit. Mais prévoir le lieu d'une éclipse de soleil dépassait les connaissances de l'époque : au mieux, Thalès aurait pu connaître des cycles observés par les astronomes babyloniens. Beaucoup d'historiens doutent de la prédiction elle-même.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 74",
        "url": `${HERODOTE}:book=1:chapter=74`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Métaphysique",
        "locus": "A, 3, 983b"
      },
      {
        "kind": "modern",
        "author": "Geoffrey S. Kirk, John E. Raven et Malcolm Schofield",
        "work": "The Presocratic Philosophers, 2e éd., Cambridge, Cambridge University Press, 1983"
      },
      {
        "kind": "modern",
        "author": "F. Richard Stephenson",
        "work": "Historical Eclipses and Earth's Rotation, Cambridge, Cambridge University Press, 1997"
      }
    ]
  },
  {
    "id": "jeux-pythiques",
    "title": "Les Jeux pythiques deviennent panhelléniques",
    "start": -581,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Pausanias place les premiers concours à prix en 586 et les premiers concours à couronne quatre ans plus tard ; 582 sert de point de départ au comput des pythiades, mais certains historiens proposent d'autres dates.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "religion",
    "importance": 2,
    "placeId": "delphes",
    "summary": "Après la première guerre sacrée, qui détruit la cité de Kirrha, les Amphictyons réorganisent les concours de Delphes en l'honneur d'Apollon : en 582, les vainqueurs reçoivent pour la première fois une couronne de laurier. Les Jeux pythiques, tous les quatre ans, deviennent les deuxièmes en prestige après ceux d'Olympie.",
    "body": "**D'un concours de chant à des jeux complets.** Pausanias rapporte que le plus ancien concours de Delphes était un hymne chanté au dieu. Lors de la 48e olympiade, en 586, les Amphictyons (le conseil des peuples voisins qui gère le sanctuaire) ajoutent des concours de flûte et des épreuves athlétiques, avec des prix ; à la pythiade suivante, les prix sont remplacés par des couronnes.\n\n**La guerre sacrée.** Cette réorganisation suit la guerre menée par les Amphictyons contre Kirrha, accusée de rançonner les pèlerins qui montaient à Delphes. La plaine de Kirrha est consacrée au dieu et ne doit plus être cultivée.\n\n**Le circuit des grands jeux.** Avec les Jeux isthmiques et néméens, créés ou réorganisés dans les années qui suivent, se forme la *periodos*, le circuit des quatre grands jeux panhelléniques. Les épreuves musicales restent la marque propre des Jeux pythiques.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "X, 7, 2 à 5 et X, 37, 5 à 7",
        "url": `${PAUSANIAS}:book=10:chapter=7`
      },
      {
        "kind": "modern",
        "author": "Stephen G. Miller",
        "work": "Ancient Greek Athletics, New Haven, Yale University Press, 2004"
      }
    ]
  },
  {
    "id": "jeux-isthmiques",
    "title": "Les Jeux isthmiques deviennent panhelléniques",
    "start": -580,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Les chronographes placent la première fête panhellénique en 582 ou 581 ; les fouilles montrent un culte bien plus ancien et un premier stade au VIe siècle.",
    "era": "archaique",
    "track": "corinthe",
    "category": "religion",
    "importance": 3,
    "placeId": "isthmia",
    "summary": "Vers 581, Corinthe ouvre à tous les Grecs les concours célébrés tous les deux ans au sanctuaire de Poséidon, sur l'isthme. Les vainqueurs y reçoivent une couronne de pin ou de céleri sauvage, et les Jeux isthmiques prennent place dans le circuit des grands jeux.",
    "body": "**Des origines mythiques.** Pausanias rapporte que les jeux furent fondés par Sisyphe, roi légendaire de Corinthe, en l'honneur de l'enfant Mélicerte, dont un dauphin avait porté le corps sur l'isthme. Les Athéniens, selon Plutarque, en attribuaient la fondation à Thésée.\n\n**Un sanctuaire très ancien.** Le temple archaïque de Poséidon, du VIIe siècle, est l'un des premiers temples grecs à murs de pierre et à toit de tuiles. Les fouilles ont dégagé un premier stade aménagé au VIe siècle.\n\n**Des jeux tous les deux ans.** Placés au carrefour des routes et des mers, les Jeux isthmiques attirent une grande foule. C'est là, en 196, que le Romain Flamininus proclamera la « liberté des Grecs ».",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 1, 3",
        "url": `${PAUSANIAS}:book=2:chapter=1`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Thésée",
        "locus": "25",
        "url": `${PLUTARQUE}/Theseus*.html`
      },
      {
        "kind": "modern",
        "author": "Stephen G. Miller",
        "work": "Ancient Greek Athletics, New Haven, Yale University Press, 2004"
      }
    ]
  },
  {
    "id": "jeux-nemeens",
    "title": "Premiers Jeux néméens panhelléniques",
    "start": -572,
    "precision": "year",
    "certainty": "traditional",
    "certaintyNote": "Date traditionnelle de 573, transmise par les chronographes ; elle s'accorde avec l'aménagement du sanctuaire au VIe siècle.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "religion",
    "importance": 3,
    "placeId": "nemee",
    "summary": "En 573 selon la tradition, les concours célébrés au sanctuaire de Zeus à Némée, entre Corinthe et Argos, s'ouvrent à tous les Grecs. Tous les deux ans, les vainqueurs y reçoivent une couronne de céleri sauvage ; le circuit des quatre grands jeux panhelléniques est désormais complet.",
    "body": "**Des jeux funèbres.** Selon le mythe rapporté par Pausanias, les Sept, en marche contre Thèbes, fondèrent les jeux en l'honneur de l'enfant Opheltès, tué par un serpent pendant que sa nourrice leur montrait une source. Une autre tradition les rattache à Héraclès, vainqueur du lion de Némée.\n\n**Le sanctuaire.** Les fouilles américaines, menées surtout par Stephen Miller, ont dégagé un premier temple de Zeus du VIe siècle, remplacé vers 330 par un temple dont plusieurs colonnes sont aujourd'hui debout, ainsi qu'un stade avec un tunnel d'accès pour les athlètes, du IVe siècle.\n\n**Une organisation disputée.** Les jeux sont d'abord présidés par la petite cité voisine de Cléonai, puis par Argos, qui finit par les transférer dans ses murs à l'époque hellénistique.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 15, 2 et 3",
        "url": `${PAUSANIAS}:book=2:chapter=15`
      },
      {
        "kind": "modern",
        "author": "Stephen G. Miller",
        "work": "Nemea: A Guide to the Site and Museum, Berkeley, University of California Press, 1990"
      },
      {
        "kind": "modern",
        "author": "Stephen G. Miller",
        "work": "Ancient Greek Athletics, New Haven, Yale University Press, 2004"
      }
    ]
  },
  {
    "id": "heraion-de-samos",
    "title": "Grand temple d'Héra à Samos",
    "start": -569,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Le temple de Rhoïkos est daté vers 570 à 560 par les fouilles ; détruit peu après, il est remplacé par un temple plus grand, commencé vers 530 et jamais achevé.",
    "era": "archaique",
    "track": "ionie",
    "category": "building",
    "importance": 2,
    "placeId": "heraion-de-samos",
    "summary": "Vers 570 à 560, les architectes Rhoïkos et Théodoros élèvent au sanctuaire d'Héra, près de la ville de Samos, un temple immense entouré d'une double rangée de colonnes. C'est l'un des premiers grands temples ioniques ; Hérodote voit dans son successeur le plus grand temple qu'il connaisse.",
    "body": "**Un sanctuaire ancien.** Selon la légende, Héra était née à Samos, au bord de la rivière Imbrasos. Dès le VIIIe siècle, on lui élève un temple long d'une centaine de pieds, l'*hécatompédon*. Le sanctuaire reçoit des offrandes de tout le monde méditerranéen, de Chypre à l'Égypte et à l'Assyrie.\n\n**Le temple de Rhoïkos.** Vers 570 à 560, Rhoïkos et Théodoros, à qui l'on attribuait aussi l'invention de la fonte du bronze, construisent un temple diptère (à double colonnade) d'environ 50 mètres sur 100, l'un des modèles de l'ordre ionique avec l'Artémision d'Éphèse. Théodoros écrivit un traité sur ce temple, que cite encore Vitruve.\n\n**Une succession de chantiers.** Ce temple disparaît quelques décennies plus tard ; son successeur, encore plus grand, est commencé vers 530 à l'époque de Polycrate et n'est jamais terminé. Une seule colonne, incomplète, est encore debout.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "III, 60, 4",
        "url": `${HERODOTE}:book=3:chapter=60`
      },
      {
        "kind": "ancient",
        "author": "Vitruve",
        "work": "De l'architecture",
        "locus": "VII, préface, 12"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "VIII, 14, 8",
        "url": `${PAUSANIAS}:book=8:chapter=14`
      },
      {
        "kind": "modern",
        "author": "Marie-Christine Hellmann",
        "work": "L'architecture grecque, 2. Architecture religieuse et funéraire, Paris, Picard, 2006"
      }
    ]
  },
  {
    "id": "tyrannie-de-pisistrate",
    "title": "Tyrannie de Pisistrate à Athènes",
    "start": -560,
    "end": -527,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Premier coup d'État en 561/560 (archontat de Coméas), mort en 528/527 selon la Constitution des Athéniens ; la chronologie de ses deux exils est confuse et discutée.",
    "era": "archaique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "pisistrate",
      "hippias"
    ],
    "summary": "En 561/560, Pisistrate s'empare de l'Acropole avec une garde personnelle et devient tyran d'Athènes. Chassé deux fois, il revient définitivement vers 546 et gouverne jusqu'à sa mort en 528/527, en respectant les lois de Solon ; Athènes s'enrichit, se dote de fêtes et de monuments et s'affirme face aux autres cités.",
    "body": "**Trois prises de pouvoir.** Selon Hérodote, Pisistrate se blesse lui-même et prétend avoir été attaqué par ses ennemis ; l'Assemblée lui accorde une garde armée de massues, avec laquelle il prend l'Acropole. Chassé, il revient sur un char aux côtés d'une grande femme déguisée en Athéna. Exilé de nouveau, il s'enrichit grâce aux mines d'argent de Thrace, débarque à Marathon et bat ses adversaires à Pallène.\n\n**Une tyrannie modérée.** La Constitution des Athéniens note qu'il gouvernait « plus en citoyen qu'en tyran » : il prête aux paysans, crée des juges itinérants dans les dèmes et lève un impôt sur les récoltes. Athènes se dote d'une fontaine publique, d'un grand temple de Zeus Olympien, commencé par ses fils, et développe les Panathénées et les fêtes de Dionysos.\n\n**Ce qui est incertain.** Hérodote et la Constitution des Athéniens ne s'accordent pas sur la durée des exils, et les modernes proposent plusieurs chronologies. Ses fils Hippias et Hipparque lui succèdent.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 59 à 64",
        "url": `${HERODOTE}:book=1:chapter=59`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Constitution des Athéniens",
        "locus": "13 à 17"
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI, 54",
        "url": `${THUCYDIDE}:book=6:chapter=54`
      },
      {
        "kind": "modern",
        "author": "P. J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "artemision-d-ephese",
    "title": "Construction de l'Artémision d'Éphèse",
    "start": -559,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Chantier commencé vers 560, à l'époque de Crésus, dont le nom figure sur des bases de colonnes ; Pline dit que la construction dura 120 ans.",
    "era": "archaique",
    "track": "ionie",
    "category": "building",
    "importance": 2,
    "placeId": "artemision-d-ephese",
    "people": [
      "cresus"
    ],
    "summary": "Vers 560, les Éphésiens entreprennent un temple d'Artémis gigantesque, entièrement en marbre, entouré d'une double forêt de colonnes. Le roi de Lydie Crésus en offre la plupart des colonnes. Incendié en 356 et reconstruit sur le même plan, ce temple comptera parmi les Sept Merveilles du monde.",
    "body": "**Un chantier royal.** Hérodote rapporte que Crésus offrit à Éphèse des génisses d'or et la plupart des colonnes du temple. Des fragments de bases de colonnes, conservés au British Museum, portent une dédicace au nom du roi. Strabon et Pline nomment l'architecte Chersiphron, auquel Vitruve associe son fils Métagénès.\n\n**Des dimensions inédites.** Le temple mesure environ 55 mètres sur 115, avec plus d'une centaine de colonnes ioniques hautes de près de 18 mètres, dont certaines ont un tambour inférieur sculpté. Pline raconte que l'architecte fit glisser les énormes architraves sur des sacs de sable.\n\n**Une longue histoire.** Sous le temple, les fouilleurs ont trouvé des sanctuaires plus anciens et un dépôt d'offrandes contenant les plus anciennes monnaies connues. En 356, un certain Hérostrate incendie le temple pour rendre son nom immortel ; les Éphésiens le rebâtissent à l'identique, plus haut encore.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 92, 1",
        "url": `${HERODOTE}:book=1:chapter=92`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIV, 1, 22",
        "url": `${STRABON}:book=14:chapter=1:section=22`
      },
      {
        "kind": "ancient",
        "author": "Pline l'Ancien",
        "work": "Histoire naturelle",
        "locus": "XXXVI, 95 à 97"
      },
      {
        "kind": "modern",
        "author": "Anton Bammer et Ulrike Muss",
        "work": "Das Artemision von Ephesos. Das Weltwunder Ioniens in archaischer und klassischer Zeit, Mayence, Philipp von Zabern, 1996"
      }
    ]
  },
  {
    "id": "sparte-soumet-tegee",
    "title": "Sparte l'emporte sur Tégée, débuts de la ligue du Péloponnèse",
    "start": -559,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Hérodote place la victoire sous les rois Anaxandridas et Ariston, avant l'ambassade de Crésus à Sparte, vers 560 à 550 ; la date précise est inconnue.",
    "era": "archaique",
    "track": "sparte",
    "category": "war",
    "importance": 2,
    "placeId": "tegee",
    "summary": "Vers 560 à 550, après une longue guerre, Sparte l'emporte sur Tégée, en Arcadie, mais renonce à l'annexer et en fait une alliée. Ce choix inaugure le réseau d'alliances que les modernes appellent la ligue du Péloponnèse, qui fait de Sparte la première puissance de Grèce.",
    "body": "**Les os d'Oreste.** Hérodote raconte que les Spartiates, sûrs de conquérir l'Arcadie sur la foi d'un oracle, partirent contre Tégée avec des chaînes pour les futurs esclaves ; vaincus, ils durent cultiver eux-mêmes, enchaînés, la plaine de Tégée. Plus tard, un nouvel oracle leur ordonna de rapporter les ossements d'Oreste : un Spartiate les découvrit chez un forgeron tégéate, et Sparte l'emporta désormais à chaque combat.\n\n**De la conquête à l'alliance.** Au lieu de réduire les Tégéates en hilotes comme les Messéniens, Sparte conclut avec eux un traité, dont Aristote, cité par Plutarque, a conservé une clause. Ce modèle d'alliance s'étend à la plupart des cités du Péloponnèse, sauf Argos.\n\n**Ce que recouvre le mot « ligue ».** Les Grecs disaient « les Lacédémoniens et leurs alliés ». Les règles communes (un congrès des alliés, un vote avant toute guerre) ne se fixent qu'à la fin du VIe siècle, après les échecs de Cléomène contre Athènes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 65 à 68",
        "url": `${HERODOTE}:book=1:chapter=65`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Questions grecques",
        "locus": "5 (292b)"
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Sparta and Lakonia: A Regional History 1300-362 BC, 2e éd., Londres, Routledge, 2002"
      }
    ]
  },
  {
    "id": "cyrus-vainc-les-medes",
    "title": "Cyrus II l'emporte sur les Mèdes",
    "start": -549,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "La Chronique de Nabonide place la chute d'Astyage la sixième année de Nabonide, soit 550/549 ; le récit d'Hérodote sur l'enfance de Cyrus relève du conte.",
    "era": "archaique",
    "track": "perse",
    "category": "war",
    "importance": 2,
    "placeId": "pasargades",
    "people": [
      "cyrus-ii",
      "astyage"
    ],
    "summary": "Vers 550, Cyrus, roi perse d'Anshan, vassal des Mèdes, se révolte contre le roi mède Astyage, que ses propres soldats lui livrent. Il prend Ecbatane et hérite de l'empire mède : c'est la naissance de l'empire perse achéménide, qui atteindra bientôt la mer Égée.",
    "body": "**Deux récits.** Hérodote fait de Cyrus le petit-fils d'Astyage, abandonné à sa naissance puis sauvé par un berger, et raconte que le général mède Harpage, pour se venger du roi, poussa Cyrus à la révolte. La Chronique de Nabonide, texte babylonien contemporain, dit plus sobrement qu'Astyage marcha contre Cyrus, que son armée se révolta et le livra, et que Cyrus emporta le trésor d'Ecbatane.\n\n**Pasargades.** Selon Strabon, Cyrus honora Pasargades parce qu'il y avait vaincu Astyage lors de la dernière bataille. Il y fit construire des palais, des jardins et son tombeau, qui se dresse encore.\n\n**Pour les Grecs.** En une dizaine d'années, Cyrus soumet la Lydie de Crésus, les cités grecques d'Asie puis Babylone (539). Les Grecs d'Asie passent sous l'autorité d'un empire qui s'étend jusqu'à l'Asie centrale.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 123 à 130",
        "url": `${HERODOTE}:book=1:chapter=123`
      },
      {
        "kind": "ancient",
        "author": "Chronique de Nabonide",
        "work": "Chronique babylonienne (ABC 7)",
        "locus": "col. II, 1 à 4"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XV, 3, 8",
        "url": `${STRABON}:book=15:chapter=3:section=8`
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      }
    ]
  },
  {
    "id": "monnaies-d-egine",
    "title": "Les « tortues » d'Égine",
    "start": -549,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Les premières monnaies d'argent d'Égine sont datées vers 550 par les trésors monétaires, à une décennie ou deux près ; leur attribution à Pheidon d'Argos par Éphore est un anachronisme.",
    "era": "archaique",
    "track": "monde-grec",
    "category": "society",
    "importance": 3,
    "placeId": "egine",
    "summary": "Vers 550, l'île d'Égine, grande puissance commerciale, frappe des monnaies d'argent marquées d'une tortue de mer, parmi les premières de Grèce propre. Leur étalon de poids, dit éginétique, se diffuse dans le Péloponnèse, les Cyclades et la Crète.",
    "body": "**La monnaie d'une cité marchande.** Égine, île du golfe Saronique, a peu de terres mais une flotte nombreuse ; ses marchands sont présents jusqu'à Naucratis, en Égypte. Ses statères d'argent, d'environ 12 grammes, portent une tortue de mer au droit et un simple carré creux au revers. Leur succès en fait l'une des monnaies les plus répandues de la Grèce archaïque.\n\n**Une invention attribuée à Pheidon.** Éphore, cité par Strabon, rapporte que Pheidon d'Argos frappa la première monnaie d'argent à Égine. Les trouvailles montrent que les tortues sont nettement plus tardives : la tradition a rattaché à un personnage célèbre une invention dont elle ignorait l'auteur.\n\n**Après Égine.** Athènes et Corinthe frappent leurs propres monnaies dans la seconde moitié du VIe siècle : d'abord les monnaies « à blason » d'Athènes, puis, vers 515, les célèbres chouettes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VIII, 6, 16",
        "url": `${STRABON}:book=8:chapter=6:section=16`
      },
      {
        "kind": "modern",
        "author": "Colin M. Kraay",
        "work": "Archaic and Classical Greek Coins, Londres, Methuen, 1976"
      }
    ]
  },
  {
    "id": "chute-de-sardes",
    "title": "Cyrus prend Sardes, chute de Crésus",
    "start": -546,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date traditionnelle de 547/546 ; la ligne de la Chronique de Nabonide qui semblait la confirmer est abîmée et sa lecture discutée, si bien que certains historiens placent la chute de Sardes quelques années plus tard.",
    "era": "archaique",
    "track": "perse",
    "category": "war",
    "importance": 1,
    "placeId": "sardes",
    "people": [
      "cresus",
      "cyrus-ii"
    ],
    "summary": "Crésus, roi de Lydie, attaque la Perse après un oracle de Delphes qui lui annonce qu'il détruira un grand empire. Battu, il se replie à Sardes, que Cyrus prend après un siège de quatorze jours. La Perse atteint ainsi la mer Égée, et les cités grecques d'Asie passent d'un maître lydien à un maître perse.",
    "body": "**L'oracle et la guerre.** Hérodote raconte que Crésus, maître des Grecs d'Asie et généreux donateur de Delphes, consulta l'oracle : s'il attaquait les Perses, il détruirait un grand empire. Il franchit l'Halys, livre en Cappadoce une bataille indécise, puis rentre à Sardes et licencie ses mercenaires pour l'hiver. Cyrus le suit aussitôt, bat la cavalerie lydienne devant la ville et prend la citadelle par une falaise mal gardée.\n\n**Le bûcher de Crésus.** Selon Hérodote, Cyrus fait monter Crésus sur un bûcher, puis l'épargne quand une pluie envoyée par Apollon éteint les flammes ; le poète Bacchylide raconte qu'Apollon l'emporta au pays des Hyperboréens. L'oracle s'était réalisé : l'empire détruit était celui de Crésus.\n\n**Les conséquences.** Sardes devient la capitale d'une satrapie perse, le centre du pouvoir perse face aux Grecs. Les cités d'Ionie, qui avaient refusé de se rallier à Cyrus, sont soumises les années suivantes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 53 et 75 à 91",
        "url": `${HERODOTE}:book=1:chapter=75`
      },
      {
        "kind": "ancient",
        "author": "Bacchylide",
        "work": "Épinicies",
        "locus": "III, 23 à 62"
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      }
    ]
  },
  {
    "id": "conquete-perse-de-l-ionie",
    "title": "Conquête perse de l'Ionie, exil des Phocéens",
    "start": -545,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Campagnes de Mazarès puis d'Harpage dans les années qui suivent la prise de Sardes, vers 546 à 540 ; Hérodote ne donne pas d'année.",
    "era": "archaique",
    "track": "ionie",
    "category": "war",
    "importance": 2,
    "placeId": "phocee",
    "people": [
      "harpage",
      "cyrus-ii"
    ],
    "summary": "Après la chute de Sardes, le général Harpage soumet une à une les cités grecques d'Asie à l'aide de terrasses d'assaut. Plutôt que de se rendre, les Phocéens embarquent toute leur population et partent vers l'Occident, les habitants de Téos fondent Abdère en Thrace ; Milet, seule, obtient un traité.",
    "body": "**Le refus de Cyrus.** Hérodote raconte que les Ioniens, qui avaient refusé de se rallier à Cyrus, lui proposèrent ensuite de se soumettre aux mêmes conditions que sous Crésus. Cyrus leur répondit par la fable du joueur de flûte qui, n'ayant pu faire danser les poissons, les vit sauter une fois pris dans son filet. Seuls les Milésiens obtinrent un accord. Sparte se contenta d'envoyer un héraut menacer Cyrus, qui demanda qui étaient ces Lacédémoniens.\n\n**La guerre des terrasses.** Harpage, un Mède passé au service de Cyrus, assiège les villes en élevant des remblais contre leurs murs. Les Phocéens obtiennent un jour de répit, chargent sur leurs navires femmes, enfants et statues des dieux, et partent pour Alalia, en Corse ; après une bataille navale contre les Carthaginois et les Étrusques, ils s'établissent à Élée, en Italie.\n\n**Une proposition restée sans suite.** Selon Hérodote, Bias de Priène proposa aux Ioniens réunis au Panionion d'émigrer tous ensemble en Sardaigne pour y fonder une seule grande cité.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, 141, 152 et 153, 162 à 170",
        "url": `${HERODOTE}:book=1:chapter=162`
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      },
      {
        "kind": "modern",
        "author": "Alan M. Greaves",
        "work": "The Land of Ionia: Society and Economy in the Archaic Period, Chichester, Wiley-Blackwell, 2010"
      }
    ]
  },
  {
    "id": "tyrannie-de-polycrate",
    "title": "Polycrate, tyran de Samos",
    "start": -537,
    "end": -521,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Début de la tyrannie vers 538 à 532 selon les reconstructions, fin vers 522, peu avant la mort de Cambyse ; Hérodote ne donne pas d'années.",
    "era": "archaique",
    "track": "ionie",
    "category": "politics",
    "importance": 2,
    "placeId": "samos",
    "people": [
      "polycrate",
      "eupalinos"
    ],
    "summary": "Vers 535, Polycrate prend le pouvoir à Samos et fait de l'île la première puissance navale de l'Égée, avec une centaine de navires. Sa cour attire des poètes comme Anacréon, et Samos se dote d'ouvrages que Hérodote compte parmi les plus grands des Grecs, dont le tunnel d'Eupalinos.",
    "body": "**Un tyran heureux.** Hérodote raconte que Polycrate prit Samos avec ses deux frères, fit tuer l'un et exila l'autre, puis multiplia les conquêtes avec ses cent pentécontores et ses mille archers. Son allié, le pharaon Amasis, effrayé par tant de chance, lui conseilla de sacrifier son bien le plus précieux ; Polycrate jeta son anneau à la mer, mais le retrouva dans le ventre d'un poisson. Thucydide mentionne sa puissance sur mer et sa domination sur les îles.\n\n**Trois grands ouvrages.** Hérodote décrit à Samos un tunnel creusé à travers une montagne pour amener l'eau à la ville, œuvre d'Eupalinos de Mégare, une digue protégeant le port et le grand temple d'Héra. Le tunnel, long d'un peu plus d'un kilomètre, a été creusé à partir de ses deux extrémités, qui se rejoignent avec un faible écart ; on peut encore le parcourir.\n\n**Une fin cruelle.** Vers 522, le satrape perse Oroitès attire Polycrate sur le continent en lui promettant de l'or et le fait mettre à mort. Samos passe peu après sous contrôle perse.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "III, 39 à 60 et 120 à 125",
        "url": `${HERODOTE}:book=3:chapter=39`
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 13, 6",
        "url": `${THUCYDIDE}:book=1:chapter=13`
      },
      {
        "kind": "modern",
        "author": "Graham Shipley",
        "work": "A History of Samos 800-188 BC, Oxford, Clarendon Press, 1987"
      }
    ]
  },
  {
    "id": "pythagore-a-crotone",
    "title": "Pythagore s'installe à Crotone",
    "start": -529,
    "precision": "decade",
    "certainty": "traditional",
    "certaintyNote": "Date tirée d'Aristoxène, pour qui Pythagore quitta Samos à quarante ans sous la tyrannie de Polycrate ; les biographies anciennes sont tardives et mêlées de légendes.",
    "era": "archaique",
    "track": "occident",
    "category": "culture",
    "importance": 2,
    "placeId": "crotone",
    "people": [
      "pythagore",
      "polycrate"
    ],
    "summary": "Vers 530, Pythagore quitte Samos, gouvernée par Polycrate, et s'installe à Crotone, en Italie du Sud. Il y fonde une communauté qui suit des règles de vie strictes, croit à la réincarnation des âmes et cherche dans les nombres l'harmonie du monde ; ses disciples pèsent aussi sur la vie politique des cités voisines.",
    "body": "**Un maître sans écrits.** Pythagore n'a rien écrit. Hérodote le cite déjà comme un sage réputé, et le poète Xénophane se moque de sa croyance en la réincarnation : Pythagore aurait reconnu la voix d'un ami dans les cris d'un chien battu. Strabon rapporte qu'il quitta Samos parce que la tyrannie y grandissait.\n\n**La communauté pythagoricienne.** À Crotone, ses disciples partagent une discipline commune (silence, interdits alimentaires, examen de conscience). Les pythagoriciens étudient l'arithmétique, la musique et l'astronomie ; le fameux théorème lui est attribué tardivement, et les Babyloniens en connaissaient déjà des applications.\n\n**Un rôle politique.** Les pythagoriciens dominent un temps le gouvernement de Crotone et d'autres cités. Selon Polybe, une révolte les chasse au milieu du Ve siècle et leurs lieux de réunion sont incendiés. Pythagore, lui, serait mort à Métaponte.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "IV, 95",
        "url": `${HERODOTE}:book=4:chapter=95`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIV, 1, 16",
        "url": `${STRABON}:book=14:chapter=1:section=16`
      },
      {
        "kind": "ancient",
        "author": "Porphyre",
        "work": "Vie de Pythagore",
        "locus": "9 (d'après Aristoxène)"
      },
      {
        "kind": "modern",
        "author": "Walter Burkert",
        "work": "Lore and Science in Ancient Pythagoreanism, Cambridge (Mass.), Harvard University Press, 1972"
      }
    ]
  },
  {
    "id": "ceramique-a-figures-rouges",
    "title": "Invention de la céramique à figures rouges",
    "start": -529,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Datation stylistique des premiers vases, vers 530 à 520 ; l'attribution de l'invention au Peintre d'Andokidès est la plus courante, sans être certaine.",
    "era": "archaique",
    "track": "athenes",
    "category": "culture",
    "importance": 3,
    "placeId": "ceramique",
    "summary": "Vers 530, les potiers d'Athènes inversent la technique de la céramique à figures noires : les personnages gardent la couleur de l'argile et le fond est couvert de vernis noir. Les détails, tracés au pinceau, permettent de rendre muscles, plis et mouvements bien plus librement.",
    "body": "**Une technique inversée.** Dans la technique à figures noires, les personnages sont peints en noir et leurs détails incisés à la pointe. Vers 530, un atelier athénien, souvent identifié à celui du Peintre d'Andokidès, réserve les figures dans la couleur de l'argile et peint le fond en noir. Certains vases, dits bilingues, montrent la même scène dans les deux techniques, une de chaque côté.\n\n**Les « Pionniers ».** Vers 520 à 500, des peintres comme Euphronios et Euthymidès explorent les possibilités du pinceau : corps en raccourci, anatomie détaillée, poses de trois quarts. Euthymidès écrit sur un vase, en défi à son rival : « comme jamais Euphronios ».\n\n**Un succès durable.** La figure rouge domine la production athénienne pendant près de deux siècles et s'exporte jusqu'en Étrurie, où l'on a trouvé une grande partie des vases conservés. Les amphores des Panathénées, prix des concours, restent en figures noires par tradition.",
    "sources": [
      {
        "kind": "modern",
        "author": "John D. Beazley",
        "work": "Attic Red-Figure Vase-Painters, 2e éd., Oxford, Clarendon Press, 1963"
      },
      {
        "kind": "modern",
        "author": "John Boardman",
        "work": "Athenian Red Figure Vases: The Archaic Period, Londres, Thames and Hudson, 1975"
      }
    ]
  },
  {
    "id": "darius-en-scythie",
    "title": "Expédition de Darius contre les Scythes",
    "start": -512,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Hérodote ne date pas l'expédition ; les historiens la placent vers 513, dans une fourchette d'environ 519 à 512.",
    "era": "archaique",
    "track": "perse",
    "category": "war",
    "importance": 2,
    "placeId": "byzance",
    "people": [
      "darius-ier",
      "histiee",
      "miltiade"
    ],
    "summary": "Vers 513, Darius Ier franchit le Bosphore sur un pont de bateaux, traverse la Thrace et passe le Danube pour attaquer les Scythes du nord de la mer Noire. Les Scythes se dérobent ; Darius doit rentrer sans victoire, mais la Thrace et bientôt la Macédoine reconnaissent l'autorité perse.",
    "body": "**Une armée sur deux continents.** Hérodote raconte que l'ingénieur samien Mandroclès jeta un pont de bateaux sur le Bosphore, près de Byzance, et que les Grecs d'Ionie construisirent un second pont sur le Danube avec leur flotte. Il attribue à Darius 700 000 hommes et 600 navires, chiffres que les historiens jugent très exagérés.\n\n**Les Grecs gardiens du pont.** Les Scythes reculent en brûlant les pâturages et refusent la bataille. Pendant ce temps, les tyrans grecs qui gardent le pont du Danube débattent de sa destruction, qui condamnerait Darius : l'Athénien Miltiade, alors maître de la Chersonèse, y serait favorable, mais Histiée de Milet les convainc de rester fidèles, car leur pouvoir dépend de la Perse.\n\n**Les conséquences.** De retour en Asie, Darius laisse en Europe le général Mégabaze, qui soumet la Thrace et les cités de la côte ; le roi de Macédoine Amyntas reconnaît la souveraineté perse. La Perse est désormais aux portes de la Grèce.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "IV, 83 à 98 et 118 à 144 ; V, 1 et 2, 17 et 18",
        "url": `${HERODOTE}:book=4:chapter=83`
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      }
    ]
  },
  {
    "id": "expulsion-d-hippias",
    "title": "Chute des Pisistratides, Hippias chassé d'Athènes",
    "start": -509,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Année archontale 511/510 (archontat d'Harpactidès) ; le meurtre d'Hipparque, quatre ans plus tôt, date des Panathénées de 514.",
    "era": "archaique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "hippias",
      "hipparque",
      "harmodios",
      "aristogiton",
      "cleomene-ier"
    ],
    "summary": "En 514, Harmodios et Aristogiton assassinent Hipparque, frère du tyran Hippias, qui durcit alors son pouvoir. En 510, poussés par l'oracle de Delphes, les Spartiates du roi Cléomène assiègent Hippias sur l'Acropole et le contraignent à partir : la tyrannie des Pisistratides prend fin, ouvrant la voie aux réformes de Clisthène.",
    "body": "**Les tyrannicides.** Thucydide raconte que le meurtre d'Hipparque, pendant la procession des Panathénées, eut pour cause une affaire privée, une rivalité amoureuse, et non un projet politique. Harmodios fut tué sur place, Aristogiton exécuté. Les Athéniens en firent pourtant les héros de la liberté et leur élevèrent des statues sur l'agora.\n\n**L'intervention spartiate.** Les Alcméonides, exilés, échouent à Leipsydrion, puis gagnent la faveur de Delphes en reconstruisant le temple d'Apollon avec une façade de marbre. La Pythie répète aux Spartiates qu'il faut libérer Athènes. Une première expédition est repoussée par la cavalerie thessalienne ; la seconde, menée par Cléomène, assiège Hippias, qui cède après la capture de ses enfants et se retire à Sigée.\n\n**La suite.** Selon Hérodote, les Pisistratides avaient gouverné Athènes 36 ans. Hippias se réfugie à la cour de Darius ; vingt ans plus tard, il guide les Perses jusqu'à Marathon.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 55 à 65",
        "url": `${HERODOTE}:book=5:chapter=55`
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI, 54 à 59",
        "url": `${THUCYDIDE}:book=6:chapter=54`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Constitution des Athéniens",
        "locus": "18 et 19"
      },
      {
        "kind": "modern",
        "author": "P. J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "destruction-de-sybaris",
    "title": "Crotone détruit Sybaris",
    "start": -509,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date traditionnelle de 510 ; les chiffres des armées donnés par Diodore et Strabon (300 000 Sybarites contre 100 000 Crotoniates) sont invraisemblables.",
    "era": "archaique",
    "track": "occident",
    "category": "war",
    "importance": 3,
    "placeId": "sybaris",
    "people": [
      "milon-de-crotone",
      "pythagore"
    ],
    "summary": "En 510, Crotone, menée par l'athlète Milon, écrase l'armée de Sybaris, sa voisine du golfe de Tarente, prend la ville et, selon Strabon, détourne une rivière pour la submerger. La plus riche cité de Grande-Grèce disparaît ; son nom reste synonyme de luxe.",
    "body": "**Le conflit.** Diodore raconte que le démagogue Télys chassa de Sybaris cinq cents riches citoyens, qui se réfugièrent à Crotone. Sybaris exigea leur remise ; les Crotoniates, sur le conseil de Pythagore selon Diodore, refusèrent. L'armée de Crotone, commandée par Milon, six fois vainqueur de la lutte à Olympie, l'emporta en bataille rangée.\n\n**La destruction.** Strabon dit que les Crotoniates prirent la ville en soixante-dix jours et détournèrent le fleuve Crathis pour la noyer. Hérodote rapporte que les Milésiens, alliés des Sybarites, prirent tous le deuil.\n\n**Une cité légendaire.** Les auteurs anciens prêtaient aux Sybarites un luxe extravagant et un vaste empire, qu'ils chiffrent de façon exagérée. Le site, recouvert par les alluvions, a été retrouvé par forage dans les années 1960 ; Athènes fonde Thourioi au même endroit en 444.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XII, 9 et 10",
        "url": `${DIODORE}:book=12:chapter=9`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VI, 1, 13",
        "url": `${STRABON}:book=6:chapter=1:section=13`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "V, 44 et VI, 21",
        "url": `${HERODOTE}:book=5:chapter=44`
      },
      {
        "kind": "modern",
        "author": "Mogens Herman Hansen et Thomas Heine Nielsen (dir.)",
        "work": "An Inventory of Archaic and Classical Poleis, Oxford, Oxford University Press, 2004"
      }
    ]
  },
  {
    "id": "gelon-maitre-de-syracuse",
    "title": "Gélon devient maître de Syracuse",
    "start": -484,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date de 485/484, déduite d'Aristote, qui donne à Gélon sept ans de règne à Syracuse avant sa mort en 478.",
    "era": "archaique",
    "track": "occident",
    "category": "politics",
    "importance": 2,
    "placeId": "syracuse",
    "people": [
      "gelon"
    ],
    "summary": "En 485, Gélon, tyran de Géla, profite d'une guerre civile à Syracuse pour s'emparer de la ville, dont il fait sa capitale. Il y transfère par la force les habitants de plusieurs cités voisines et fait de Syracuse la plus grande ville grecque de l'Occident.",
    "body": "**De Géla à Syracuse.** Hérodote raconte que Gélon, chef de la cavalerie du tyran Hippocrate de Géla, prit le pouvoir à sa mort. À Syracuse, le peuple et les serfs indigènes avaient chassé les grands propriétaires, les *gamoroi*. Gélon les ramène, reçoit la ville et laisse Géla à son frère Hiéron.\n\n**Une capitale peuplée de force.** Gélon détruit Camarina et fait de ses habitants des Syracusains, puis y installe plus de la moitié des habitants de Géla. Il prend Mégara Hyblaea et l'Eubée de Sicile, accorde la citoyenneté aux riches et vend le peuple comme esclave. Syracuse devient une grande puissance, avec une flotte de deux cents trières selon Hérodote.\n\n**Un allié recherché.** En 481, les Grecs menacés par Xerxès lui demandent son aide. Gélon exige le commandement d'une partie des forces grecques, ce qui lui est refusé ; quelques mois plus tard, il affronte les Carthaginois à Himère.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VII, 153 à 162",
        "url": `${HERODOTE}:book=7:chapter=153`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Politique",
        "locus": "V, 12, 1315b"
      },
      {
        "kind": "modern",
        "author": "Franco De Angelis",
        "work": "Archaic and Classical Greek Sicily: A Social and Economic History, Oxford, Oxford University Press, 2016"
      }
    ]
  }
]
