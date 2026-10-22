import type { HistoricalEvent } from './schema.ts'

const WILL_I = "Édouard Will, Histoire politique du monde hellénistique, t. I, 2e éd., Nancy, Presses universitaires de Nancy, 1979"
const WILL_II = "Édouard Will, Histoire politique du monde hellénistique, t. II, 2e éd., Nancy, Presses universitaires de Nancy, 1982"
const HABICHT = "Christian Habicht, Athènes hellénistique : histoire de la cité d'Alexandre le Grand à Marc Antoine, trad. française, Paris, Les Belles Lettres, 2000"
const GRUEN = "Erich S. Gruen, The Hellenistic World and the Coming of Rome, Berkeley, University of California Press, 1984"
const HANSEN = "Esther V. Hansen, The Attalids of Pergamon, 2e éd., Ithaca, Cornell University Press, 1971"
const FRASER = "P. M. Fraser, Ptolemaic Alexandria, 3 vol., Oxford, Clarendon Press, 1972"
const ROLLER = "Duane W. Roller, Cleopatra: A Biography, Oxford, Oxford University Press, 2010"
const CANFORA = "Luciano Canfora, La Véritable Histoire de la bibliothèque d'Alexandrie, trad. française, Paris, Desjonquères, 1988"
const CARTLEDGE = "Paul Cartledge et Antony Spawforth, Hellenistic and Roman Sparta: A Tale of Two Cities, London, Routledge, 1989"
const GRAINGER_SELEUKOS = "John D. Grainger, Seleukos Nikator: Constructing a Hellenistic Kingdom, London, Routledge, 1990"

export const events: HistoricalEvent[] = [
  {
    "id": "guerre-lamiaque",
    "title": "Guerre lamiaque et fin de la démocratie athénienne",
    "start": -322,
    "end": -321,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Guerre attestée, de l'automne 323 à l'automne 322 ; Plutarque place la bataille de Crannon le 7 Métageitnion, en août 322.",
    "era": "hellenistique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "lamia",
    "people": [
      "leosthene",
      "antipatros",
      "demosthene"
    ],
    "summary": "À l'annonce de la mort d'Alexandre, Athènes et ses alliés se soulèvent contre la Macédoine et assiègent Antipatros dans Lamia. Vaincus sur mer près d'Amorgos puis sur terre à Crannon en 322, les Athéniens doivent accepter une garnison macédonienne et un régime censitaire : la démocratie athénienne prend fin.",
    "body": "**Le soulèvement.** Dès l'automne 323, Athènes lève une armée, en grande partie de mercenaires, sous le commandement de Léosthène, rejointe par les Étoliens et une partie des Thessaliens. Antipatros, battu en Thessalie, s'enferme dans Lamia, que les Grecs assiègent tout l'hiver ; Léosthène y est tué. Les Grecs parlaient de « guerre hellénique » ; le nom de guerre lamiaque vient du siège.\n\n**La défaite.** Renforcé par les vétérans de Cratère venus d'Asie, Antipatros l'emporte à Crannon en août 322, tandis que la flotte athénienne est battue près d'Amorgos. Athènes reçoit une garnison à Munychie, au Pirée, et réserve les droits politiques aux hommes possédant au moins 2 000 drachmes. Selon Diodore, 9 000 citoyens gardent leurs droits et plus de 22 000 les perdent ; Plutarque parle de 12 000 exclus. Démosthène, poursuivi, s'empoisonne à Calaurie.\n\n**Ce qui change.** La démocratie, rétablie par moments ensuite, ne retrouve plus la stabilité qu'elle avait connue depuis 403. Les chiffres du corps civique restent discutés : ils reposent sur deux auteurs qui ne concordent pas.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVIII, 8 à 18"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Phocion",
        "locus": "23 à 28"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Démosthène",
        "locus": "27 à 30"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Camille",
        "locus": "19, 5"
      },
      {
        "kind": "modern",
        "author": "Christian Habicht",
        "work": HABICHT,
        "locus": "chap. 2"
      }
    ]
  },
  {
    "id": "accords-de-triparadisos",
    "title": "Accords de Triparadisos",
    "start": -320,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Accords attestés ; selon la chronologie des Diadoques retenue, « haute » ou « basse », ils datent de 321 ou de 320.",
    "era": "hellenistique",
    "track": "macedoine",
    "category": "politics",
    "importance": 3,
    "placeId": "triparadisos",
    "people": [
      "antipatros",
      "perdiccas",
      "ptolemee-ier",
      "seleucos-ier",
      "antigone-le-borgne"
    ],
    "summary": "Après le meurtre du régent Perdiccas en Égypte, les généraux macédoniens se réunissent à Triparadisos, en Syrie. Antipatros devient régent et ramène les rois en Macédoine ; Antigone le Borgne reçoit le commandement en Asie, Séleucos la satrapie de Babylonie, et Ptolémée garde l'Égypte.",
    "body": "**Après Perdiccas.** Le régent Perdiccas, parti attaquer Ptolémée, a été tué par ses propres officiers au bord du Nil. Ptolémée avait détourné vers l'Égypte la dépouille d'Alexandre, déposée d'abord à Memphis. Les chefs de l'armée royale se retrouvent à Triparadisos, un ancien parc royal perse dans la haute vallée de l'Oronte, où les soldats, mal payés, manquent de lyncher Antipatros.\n\n**Le nouveau partage.** Antipatros prend la régence et la garde des deux rois, Philippe III Arrhidée et l'enfant Alexandre IV, qu'il emmène en Macédoine. Antigone le Borgne est chargé de la guerre contre Eumène de Cardia, resté fidèle à Perdiccas ; Séleucos reçoit la Babylonie, d'où partira son royaume.\n\n**Une date discutée.** Les historiens hésitent entre 321 et 320, selon qu'ils suivent la chronologie « haute » ou « basse » des premières années des Diadoques, reconstruite à partir de Diodore et de documents babyloniens.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVIII, 36 à 39"
      },
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Histoire des successeurs d'Alexandre (abrégé de Photius)",
        "locus": "fr. 1, 30 à 38"
      },
      {
        "kind": "modern",
        "author": "Edward M. Anson",
        "work": "Alexander's Heirs: The Age of the Successors, Chichester, Wiley-Blackwell, 2014"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": WILL_I
      }
    ]
  },
  {
    "id": "agathocle-debarque-en-afrique",
    "title": "Agathocle débarque en Afrique",
    "start": -309,
    "month": 8,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Mois déduit de l'éclipse de soleil que Diodore place pendant la traversée, identifiée avec celle du 15 août 310.",
    "era": "hellenistique",
    "track": "occident",
    "category": "war",
    "importance": 3,
    "placeId": "carthage",
    "people": [
      "agathocle"
    ],
    "summary": "Assiégé dans Syracuse par les Carthaginois, Agathocle force le blocus en août 310 avec une soixantaine de navires et débarque en Afrique, où il brûle sa flotte. Pendant trois ans, il ravage le territoire de Carthage, avant de devoir abandonner son armée et rentrer en Sicile en 307.",
    "body": "**Un pari audacieux.** Maître de Syracuse depuis 317/316, Agathocle a été battu par Carthage en Sicile et se trouve enfermé dans sa ville. Plutôt que de subir le siège, il embarque l'élite de ses troupes, profite d'un relâchement du blocus et gagne la côte africaine. Diodore note qu'une éclipse de soleil plongea le jour dans la nuit pendant la traversée, ce qui permet de dater l'événement.\n\n**La guerre d'Afrique.** Une fois débarqué, il fait brûler ses navires pour que ses soldats n'aient d'autre choix que vaincre, bat une armée carthaginoise et prend plusieurs villes. Mais il ne peut prendre Carthage, et la révolte de son armée en 307 l'oblige à rentrer en Sicile en abandonnant ses fils, qui sont tués.\n\n**Après l'Afrique.** Agathocle prend le titre de roi vers 304, comme les Diadoques, et conclut la paix avec Carthage. Son expédition montre que Carthage est vulnérable sur son propre sol, ce que Rome vérifiera à son tour pendant les guerres puniques.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XX, 3 à 18 (l'éclipse en XX, 5, 5) et XX, 69 à 70"
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XXII, 4 à 8"
      },
      {
        "kind": "modern",
        "author": "Moses I. Finley",
        "work": "A History of Sicily: Ancient Sicily to the Arab Conquest, London, Chatto and Windus, 1968"
      }
    ]
  },
  {
    "id": "seleucos-reprend-babylone",
    "title": "Séleucos reprend Babylone : début de l'ère séleucide",
    "start": -311,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Retour attesté, en 312 ou au début de 311 ; l'ère séleucide part de l'automne 312 dans le calendrier macédonien et du printemps 311 dans le calendrier babylonien.",
    "era": "hellenistique",
    "track": "seleucides",
    "category": "politics",
    "importance": 1,
    "placeId": "babylone",
    "people": [
      "seleucos-ier",
      "ptolemee-ier",
      "antigone-le-borgne"
    ],
    "summary": "Chassé de Babylonie par Antigone le Borgne en 315, Séleucos y revient en 312 avec un millier d'hommes, après la victoire de Ptolémée sur Démétrios à Gaza, et reprend Babylone. Ce retour devient l'an 1 de l'ère séleucide, l'un des premiers comptes continus des années, employé pendant des siècles au Proche-Orient.",
    "body": "**Le retour.** Satrape de Babylonie depuis Triparadisos, Séleucos a fui en Égypte en 315 devant Antigone. Il combat aux côtés de Ptolémée à Gaza, puis remonte vers l'Euphrate avec, selon Diodore, 800 fantassins et environ 200 cavaliers. Bien accueilli par les Babyloniens, il reprend la citadelle, puis repousse les généraux d'Antigone ; la guerre babylonienne dure jusqu'en 309 ou 308.\n\n**Une ère nouvelle.** Les années sont désormais comptées à partir de ce retour, sans repartir à zéro à chaque règne : c'est l'ère séleucide. Elle commence au 1er Dios (automne 312) dans le calendrier macédonien et au 1er Nisan (printemps 311) dans le calendrier babylonien. Des communautés juives et syriaques l'ont employée jusqu'au Moyen Âge et au-delà.\n\n**Vers l'empire.** Séleucos prend le titre de roi en 305/304, étend son pouvoir jusqu'à l'Inde puis, après Ipsos (301), jusqu'à la Syrie, où il fonde Antioche. Les étapes de la guerre babylonienne ne sont connues que par Diodore et par une chronique babylonienne fragmentaire.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIX, 90 à 92"
      },
      {
        "kind": "ancient",
        "author": "Appien",
        "work": "Histoire romaine, livre syriaque",
        "locus": "54"
      },
      {
        "kind": "ancient",
        "author": "Chronique babylonienne des Diadoques",
        "work": "ABC 10, dans A. K. Grayson, Assyrian and Babylonian Chronicles, Locust Valley, J. J. Augustin, 1975"
      },
      {
        "kind": "modern",
        "author": "John D. Grainger",
        "work": GRAINGER_SELEUKOS
      },
      {
        "kind": "modern",
        "author": "Susan Sherwin-White et Amélie Kuhrt",
        "work": "From Samarkhand to Sardis: A New Approach to the Seleucid Empire, London, Duckworth, 1993"
      }
    ]
  },
  {
    "id": "siege-de-rhodes",
    "title": "Siège de Rhodes par Démétrios Poliorcète",
    "start": -304,
    "end": -303,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Siège attesté ; il commence en 305 et s'achève en 304, après environ un an.",
    "era": "hellenistique",
    "track": "rhodes",
    "category": "war",
    "importance": 2,
    "placeId": "rhodes",
    "people": [
      "demetrios-poliorcete",
      "ptolemee-ier"
    ],
    "summary": "En 305, Démétrios, fils d'Antigone le Borgne, assiège Rhodes, qui refuse de rompre avec Ptolémée. Malgré l'Hélépolis, une tour de siège géante, la ville résiste un an, ravitaillée par mer, et Démétrios lève le siège en 304. Il garde pourtant le surnom de Poliorcète, « le preneur de villes ».",
    "body": "**L'enjeu.** Rhodes, grande place de commerce, entretient des liens étroits avec l'Égypte et refuse de suivre Antigone contre Ptolémée. Démétrios débarque avec une flotte immense ; Diodore parle de 200 navires de guerre et de plus de 170 transports, suivis de navires de marchands attirés par le butin.\n\n**Les machines.** Le siège est une vitrine de l'ingénierie militaire hellénistique : béliers, galeries couvertes et surtout l'Hélépolis, tour mobile de neuf étages garnie de catapultes, haute d'une centaine de coudées selon Diodore, soit 40 à 45 m. Les Rhodiens, ravitaillés par les navires de Ptolémée, de Cassandre et de Lysimaque, réparent leurs murs à mesure que l'ennemi les abat.\n\n**L'issue.** Au bout d'un an, Antigone, qui a besoin de son fils en Grèce, le laisse traiter : Rhodes garde son autonomie et promet son aide à Antigone, sauf contre Ptolémée. Selon Pausanias, les Rhodiens donnent alors à Ptolémée le nom de Sauveur (Sôter) ; selon Pline, ils vendent les machines abandonnées pour payer le Colosse.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XX, 81 à 88 et 91 à 100"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Démétrios",
        "locus": "21 à 22"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 8, 6"
      },
      {
        "kind": "modern",
        "author": "Richard A. Billows",
        "work": "Antigonos the One-Eyed and the Creation of the Hellenistic State, Berkeley, University of California Press, 1990"
      },
      {
        "kind": "modern",
        "author": "Vincent Gabrielsen",
        "work": "The Naval Aristocracy of Hellenistic Rhodes, Aarhus, Aarhus University Press, 1997"
      }
    ]
  },
  {
    "id": "euclide-et-les-elements",
    "title": "Euclide écrit les Éléments",
    "start": -299,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "L'œuvre est conservée, mais Euclide n'est daté que par Proclus, philosophe du Ve siècle apr. J.-C., qui le place sous Ptolémée Ier ; aucun document contemporain ne parle de sa vie.",
    "era": "hellenistique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "alexandrie",
    "people": [
      "euclide",
      "ptolemee-ier"
    ],
    "summary": "Vers 300, à Alexandrie, Euclide rassemble dans les treize livres des Éléments la géométrie et l'arithmétique grecques, présentées à partir de définitions, de postulats et de démonstrations. L'ouvrage sert de manuel pendant plus de deux mille ans ; de son auteur, on ne sait presque rien.",
    "body": "**L'œuvre.** Les Éléments partent de définitions, de cinq postulats et de notions communes, puis enchaînent des propositions démontrées : géométrie plane, proportions, nombres (dont la preuve qu'il existe une infinité de nombres premiers), grandeurs irrationnelles, solides réguliers. Euclide y ordonne des résultats plus anciens, dus notamment à Eudoxe et à Théétète.\n\n**L'homme.** Proclus le place sous Ptolémée Ier, entre les élèves de Platon et Archimède. Il lui prête une réponse au roi qui cherchait un chemin plus court : « il n'y a pas de voie royale en géométrie ». L'anecdote est suspecte, car Stobée la raconte à propos de Ménechme et d'Alexandre.\n\n**La transmission.** Le texte grec que nous lisons dérive surtout de l'édition de Théon d'Alexandrie (IVe siècle apr. J.-C.) ; un manuscrit du Vatican conserve une version antérieure. Traduits en arabe puis en latin, les Éléments restent la base de l'enseignement de la géométrie jusqu'au XIXe siècle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Proclus",
        "work": "Commentaire sur le premier livre des Éléments d'Euclide",
        "locus": "prologue, p. 68, 6 à 20 Friedlein"
      },
      {
        "kind": "modern",
        "author": "Bernard Vitrac",
        "work": "Euclide, Les Éléments, traduction et commentaire, vol. I, Paris, Presses universitaires de France, 1990"
      },
      {
        "kind": "modern",
        "author": "Thomas L. Heath",
        "work": "The Thirteen Books of Euclid's Elements, 2e éd., Cambridge, Cambridge University Press, 1926"
      }
    ]
  },
  {
    "id": "colosse-de-rhodes",
    "title": "Colosse de Rhodes",
    "start": -293,
    "end": -281,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Statue attestée ; les douze ans de chantier donnés par Pline sont placés vers 294 à 282, et sa chute vers 227 ou 226 : ces dates sont déduites et discutées.",
    "era": "hellenistique",
    "track": "rhodes",
    "category": "building",
    "importance": 1,
    "placeId": "rhodes",
    "people": [
      "chares-de-lindos"
    ],
    "summary": "Avec le produit de la vente des machines laissées par Démétrios, les Rhodiens font élever par Charès de Lindos une statue de bronze du dieu Hélios haute de 70 coudées, soit environ 32 m. Achevé vers 282 après douze ans de travaux, le Colosse est renversé par un séisme vers 227 ou 226 et reste à terre pendant des siècles.",
    "body": "**Un remerciement au dieu.** Après le siège de 305 et 304, les Rhodiens dédient à Hélios, leur dieu protecteur, une statue colossale. Selon Pline l'Ancien, Charès de Lindos, élève de Lysippe, y travaille douze ans pour 300 talents ; elle mesure 70 coudées, soit 31 à 33 m selon la coudée retenue.\n\n**Où se dressait-il ?** L'image d'un géant enjambant l'entrée du port est une invention de la fin du Moyen Âge et de la Renaissance : aucun texte antique ne la décrit, et une telle pose était techniquement impossible. Le Colosse se trouvait sans doute près du port ou dans un sanctuaire de la ville ; son emplacement exact reste inconnu.\n\n**La chute.** Un tremblement de terre le brise aux genoux, selon Strabon, qui ajoute qu'un oracle interdit de le relever. Polybe raconte comment les rois rivalisèrent alors de dons pour aider Rhodes. Selon Pline, même couché, il émerveillait : peu d'hommes pouvaient embrasser son pouce. Ses débris auraient été vendus après la prise de l'île par les Arabes, en 653 apr. J.-C.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pline l'Ancien",
        "work": "Histoire naturelle",
        "locus": "XXXIV, 41"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIV, 2, 5"
      },
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "V, 88 à 90"
      },
      {
        "kind": "modern",
        "author": "Reynold Higgins",
        "work": "The Colossus of Rhodes, dans Peter A. Clayton et Martin J. Price (dir.), The Seven Wonders of the Ancient World, London, Routledge, 1988"
      }
    ]
  },
  {
    "id": "musee-et-bibliotheque-d-alexandrie",
    "title": "Fondation du Musée et de la Bibliothèque d'Alexandrie",
    "start": -289,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Le Musée et la Bibliothèque sont attestés ; leur fondation, attribuée à Ptolémée Ier ou à Ptolémée II, se place vers 295 à 280, sans date précise.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "culture",
    "importance": 1,
    "placeId": "alexandrie",
    "people": [
      "ptolemee-ier",
      "ptolemee-ii",
      "demetrios-de-phalere"
    ],
    "summary": "Vers 290, les premiers Ptolémées fondent à Alexandrie le Musée, communauté de savants entretenus par le roi, et la Bibliothèque, qui cherche à réunir tous les livres grecs. Poètes, philologues, médecins et astronomes y travaillent pendant trois siècles, faisant d'Alexandrie la capitale intellectuelle du monde hellénistique.",
    "body": "**Le Musée.** Strabon, qui visite Alexandrie vers 25, le décrit comme une partie du palais royal, avec une promenade, une exèdre et une grande salle où les savants prennent leurs repas en commun ; ils sont exemptés d'impôts et dirigés par un prêtre nommé par le roi. Le nom vient des Muses, auxquelles l'institution est consacrée.\n\n**La Bibliothèque.** La Lettre d'Aristée en attribue l'idée à Démétrios de Phalère, réfugié auprès de Ptolémée Ier. Les rois font acheter, copier et parfois saisir des livres ; Callimaque en dresse le catalogue (les Pinakes), et Zénodote, Ératosthène ou Aristarque de Samothrace y établissent le texte d'Homère.\n\n**Ce qu'on ignore.** Aucun vestige de la Bibliothèque n'a été identifié. Les chiffres anciens vont de 200 000 à 700 000 rouleaux selon les auteurs, sans qu'on puisse les vérifier, et sa fin est obscure : l'incendie de 48 n'en est qu'un épisode, et l'institution décline lentement sous l'Empire.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XVII, 1, 8"
      },
      {
        "kind": "ancient",
        "author": "Lettre d'Aristée à Philocrate",
        "work": "Lettre d'Aristée",
        "locus": "9 à 11"
      },
      {
        "kind": "ancient",
        "author": "Aulu-Gelle",
        "work": "Nuits attiques",
        "locus": "VII, 17, 3"
      },
      {
        "kind": "modern",
        "author": "P. M. Fraser",
        "work": FRASER
      },
      {
        "kind": "modern",
        "author": "Luciano Canfora",
        "work": CANFORA
      }
    ]
  },
  {
    "id": "phare-d-alexandrie",
    "title": "Phare d'Alexandrie",
    "start": -279,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Monument attesté ; son achèvement vers 283 à 280, sous Ptolémée II, repose sur des chronographes tardifs, et le début des travaux sous Ptolémée Ier n'est pas daté.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "building",
    "importance": 1,
    "placeId": "ile-de-pharos",
    "people": [
      "sostrate-de-cnide",
      "ptolemee-ii"
    ],
    "summary": "Vers 280, sous Ptolémée II, une tour monumentale est achevée à la pointe orientale de l'île de Pharos, à l'entrée du port d'Alexandrie. Haute peut-être de plus de 100 m, elle guide les navires vers une côte basse et sans repères, et son nom a donné le mot « phare ».",
    "body": "**Une tour pour une côte plate.** Le delta du Nil n'offre aucun relief visible du large, et ses abords sont semés de hauts-fonds. La tour, en trois étages (carré, octogonal puis cylindrique selon les descriptions arabes du Moyen Âge), portait au sommet une statue, peut-être de Zeus Sauveur. Pline indique un coût de 800 talents.\n\n**Sostrate.** Strabon rapporte qu'une inscription nommait Sostrate de Cnide, « ami des rois », qui l'avait dédiée pour le salut des navigateurs. Lucien raconte qu'il aurait caché son nom sous un enduit portant celui du roi, une anecdote sans doute inventée. On ignore si Sostrate fut l'architecte ou seulement le dédicant.\n\n**Sa hauteur.** Aucun texte antique ne la donne ; les estimations modernes, tirées des descriptions arabes, vont de 100 à 140 m environ. Ébranlé par plusieurs séismes, le Phare est en ruine au XIVe siècle. Des blocs et des statues en sont repêchés depuis 1994 par l'équipe de Jean-Yves Empereur, au pied du fort de Qaitbay bâti sur ses fondations.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XVII, 1, 6"
      },
      {
        "kind": "ancient",
        "author": "Pline l'Ancien",
        "work": "Histoire naturelle",
        "locus": "XXXVI, 83"
      },
      {
        "kind": "ancient",
        "author": "Lucien",
        "work": "Comment il faut écrire l'histoire",
        "locus": "62"
      },
      {
        "kind": "modern",
        "author": "Jean-Yves Empereur",
        "work": "Le Phare d'Alexandrie : la merveille retrouvée, Paris, Gallimard, 1998"
      },
      {
        "kind": "modern",
        "author": "P. M. Fraser",
        "work": FRASER
      }
    ]
  },
  {
    "id": "philetairos-fait-defection",
    "title": "Philétairos garde Pergame et son trésor",
    "start": -281,
    "precision": "year",
    "certainty": "attested",
    "era": "hellenistique",
    "track": "pergame",
    "category": "politics",
    "importance": 3,
    "placeId": "pergame",
    "people": [
      "philetairos",
      "lysimaque",
      "seleucos-ier"
    ],
    "summary": "En 282, Philétairos, chargé de garder à Pergame un trésor de 9 000 talents pour Lysimaque, se rallie à Séleucos. Il conserve la forteresse et l'argent, et s'en sert pour se tailler une principauté : c'est le point de départ de la dynastie des Attalides, nommée d'après son père Attale.",
    "body": "**Le trésor de Lysimaque.** Strabon rapporte que Lysimaque avait confié à Philétairos, originaire de Tiéion sur la mer Noire, la citadelle de Pergame et les 9 000 talents qu'elle abritait. Brouillé avec la cour de Lysimaque, Philétairos fait défection et se place sous l'autorité de Séleucos, qui bat Lysimaque l'année suivante.\n\n**Une puissance née de l'argent.** Après la mort de Séleucos, Philétairos reste maître de Pergame en reconnaissant de loin la suzeraineté séleucide ; ses monnaies portent le portrait de Séleucos. Il emploie le trésor à gagner des alliés, à doter des sanctuaires et à aider les cités voisines contre les Galates.\n\n**Une dynastie.** À sa mort, en 263, son neveu Eumène Ier lui succède ; Attale Ier sera le premier à prendre le titre de roi. Strabon insiste sur la condition d'eunuque de Philétairos, trait qui vient peut-être de traditions hostiles ; le montant du trésor ne repose que sur son témoignage.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIII, 4, 1 à 2"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 8, 1"
      },
      {
        "kind": "modern",
        "author": "Esther V. Hansen",
        "work": HANSEN
      }
    ]
  },
  {
    "id": "bataille-de-couroupedion",
    "title": "Bataille de Couroupédion et meurtre de Séleucos",
    "start": -280,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée, au début de 281 selon la plupart des historiens ; la plaine de Couroupédion, en Lydie, près de Magnésie du Sipyle et de Sardes, n'est pas localisée précisément.",
    "era": "hellenistique",
    "track": "seleucides",
    "category": "war",
    "importance": 2,
    "placeId": "magnesie-du-sipyle",
    "people": [
      "seleucos-ier",
      "lysimaque"
    ],
    "summary": "Au début de 281, Séleucos bat Lysimaque, roi de Thrace, d'Asie Mineure et de Macédoine, dans la plaine de Couroupédion, en Lydie ; Lysimaque est tué. Séleucos, dernier survivant des compagnons d'Alexandre, passe en Europe pour prendre la Macédoine, mais il est assassiné quelques mois plus tard par Ptolémée Kéraunos.",
    "body": "**La crise.** Lysimaque a fait exécuter son fils Agathocle, sur les intrigues, dit-on, de sa femme Arsinoé, fille de Ptolémée Ier. Les partisans du prince et plusieurs cités d'Asie appellent Séleucos à l'aide.\n\n**La bataille.** Les sources ne décrivent presque pas le combat ; on sait seulement que Lysimaque y meurt et que l'Asie Mineure passe à Séleucos. Justin souligne que les deux adversaires étaient les derniers compagnons d'Alexandre et leur donne 74 et 77 ans ; d'autres auteurs vieillissent encore Lysimaque.\n\n**Le meurtre.** Vers la fin de l'été 281, alors qu'il passe en Thrace pour prendre la Macédoine, Séleucos est tué près de Lysimacheia par Ptolémée Kéraunos, fils de Ptolémée Ier écarté de la succession égyptienne. Le rêve de réunir l'empire d'Alexandre s'éteint avec lui.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XVII, 1 à 2"
      },
      {
        "kind": "ancient",
        "author": "Appien",
        "work": "Histoire romaine, livre syriaque",
        "locus": "62 à 64"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 10, 4 à 5"
      },
      {
        "kind": "modern",
        "author": "Helen S. Lund",
        "work": "Lysimachus: A Study in Early Hellenistic Kingship, London, Routledge, 1992"
      },
      {
        "kind": "modern",
        "author": "John D. Grainger",
        "work": GRAINGER_SELEUKOS
      }
    ]
  },
  {
    "id": "guerre-de-pyrrhos-en-italie",
    "title": "Pyrrhos en Italie : les « victoires à la Pyrrhus »",
    "start": -279,
    "end": -274,
    "precision": "year",
    "certainty": "attested",
    "era": "hellenistique",
    "track": "rome",
    "category": "war",
    "importance": 2,
    "placeId": "heraclee-de-lucanie",
    "people": [
      "pyrrhos"
    ],
    "summary": "Appelé par Tarente contre Rome, Pyrrhos, roi d'Épire, débarque en Italie avec des éléphants. Il gagne à Héraclée (280) et à Ausculum (279), au prix de pertes si lourdes qu'on parle encore de « victoire à la Pyrrhus », passe en Sicile, puis est arrêté à Bénévent en 275 et rentre en Grèce.",
    "body": "**L'appel de Tarente.** En 281, Tarente, colonie spartiate en conflit avec Rome, sollicite Pyrrhos, parent d'Alexandre par sa mère et chef réputé. Il passe en Italie au printemps 280 avec, selon Plutarque, 20 000 fantassins, 3 000 cavaliers, 2 000 archers, 500 frondeurs et 20 éléphants, les premiers que voient les Romains.\n\n**Des victoires coûteuses.** À Héraclée, près du Siris, puis à Ausculum, la phalange et les éléphants l'emportent, mais Pyrrhos perd ses meilleurs officiers. À un compagnon qui le félicitait, il aurait répondu qu'une autre victoire de ce genre le perdrait. Rome refuse de traiter et lève de nouvelles armées. Les chiffres des pertes varient beaucoup : Plutarque compare lui-même Hiéronymos de Cardia et Denys d'Halicarnasse.\n\n**L'échec.** De 278 à 276, Pyrrhos combat les Carthaginois en Sicile sans pouvoir prendre Lilybée. Revenu en Italie, il est battu, ou du moins arrêté, à Bénévent en 275 et rentre en Épire ; il meurt en 272 dans un combat de rues à Argos. La même année, Tarente se rend aux Romains, maîtres désormais de l'Italie du Sud.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Pyrrhos",
        "locus": "13 à 26 et 34"
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XVIII, 1 à 2 et XXV, 3 à 5"
      },
      {
        "kind": "modern",
        "author": "Pierre Lévêque",
        "work": "Pyrrhos, Paris, De Boccard, 1957"
      }
    ]
  },
  {
    "id": "galates-a-delphes",
    "title": "Les Galates attaquent Delphes",
    "start": -278,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Attaque attestée, pendant l'hiver 279/278 ; le récit de la défaite des Galates mêle des faits et des prodiges rapportés par la tradition delphique.",
    "era": "hellenistique",
    "track": "monde-grec",
    "category": "war",
    "importance": 2,
    "placeId": "delphes",
    "people": [
      "brennos"
    ],
    "summary": "En 279, des bandes galates conduites par Brennos envahissent la Grèce, contournent les Thermopyles et marchent sur Delphes. Repoussées par les Étoliens et les Phocidiens, dans le froid et, selon la tradition, grâce à Apollon, elles se retirent ; Brennos se tue. Delphes célèbre la victoire par les fêtes des Sôtéria.",
    "body": "**L'invasion.** Après avoir tué Ptolémée Kéraunos, roi de Macédoine, au début de 279, des groupes celtes ravagent la Macédoine et la Thessalie. Pausanias donne à Brennos 152 000 fantassins et 20 400 cavaliers, chiffres sans doute très exagérés. Les Grecs les attendent aux Thermopyles, que les Galates finissent par contourner, comme les Perses en 480.\n\n**Delphes.** Le sanctuaire est défendu surtout par les Étoliens et les Phocidiens. Le récit de Pausanias mêle combats, tremblement de terre, orage, neige, chutes de rochers du Parnasse et apparitions de héros. Brennos, blessé, se donne la mort pendant la retraite.\n\n**Une victoire de prestige.** Les Étoliens, qui dominent ensuite l'amphictionie de Delphes, en tirent un immense prestige ; les Sôtéria célèbrent le salut des Grecs. Une partie des Galates passe en Asie Mineure en 278/277 et s'installe en Galatie, où ils deviennent les adversaires des rois de Pergame.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "X, 19 à 23"
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XXIV, 6 à 8"
      },
      {
        "kind": "modern",
        "author": "Georges Nachtergael",
        "work": "Les Galates en Grèce et les Sôtéria de Delphes, Bruxelles, Académie royale de Belgique, 1977"
      }
    ]
  },
  {
    "id": "antigone-gonatas-roi-de-macedoine",
    "title": "Antigone Gonatas, vainqueur des Galates, roi de Macédoine",
    "start": -276,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Victoire près de Lysimacheia en 277, prise du pouvoir en Macédoine en 276.",
    "era": "hellenistique",
    "track": "macedoine",
    "category": "politics",
    "importance": 3,
    "placeId": "lysimacheia",
    "people": [
      "antigone-gonatas",
      "pyrrhos"
    ],
    "summary": "En 277, près de Lysimacheia, Antigone Gonatas, fils de Démétrios Poliorcète, attire une armée galate dans un piège et la détruit. Fort de ce succès, il s'empare de la Macédoine en 276 et y installe la dynastie antigonide, qui règne jusqu'à la défaite de Persée à Pydna en 168.",
    "body": "**Après le chaos.** Depuis la mort de Ptolémée Kéraunos, la Macédoine n'a plus de roi stable et les Galates la pillent. Antigone, qui ne tient que quelques places en Grèce, débarque en Chersonèse de Thrace ; selon Justin, il abandonne son camp, attend que les Galates s'y dispersent pour piller, puis les massacre.\n\n**Un royaume durable.** Reconnu roi par les Macédoniens, Antigone doit encore repousser Pyrrhos, qui envahit le pays en 274. Il règne jusqu'en 239, contrôle la Grèce par des garnisons (Corinthe, Chalcis, le Pirée) et fréquente les philosophes, dont le stoïcien Zénon.\n\n**Une victoire mise en scène.** Comme les Étoliens à Delphes, Antigone se pose en sauveur des Grecs face aux Barbares. Ses monnaies à la tête de Pan sont souvent rattachées à cette victoire, le dieu passant pour semer la panique chez l'ennemi. Le récit de Justin, le seul un peu détaillé, reste sommaire.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XXV, 1 à 3"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Pyrrhos",
        "locus": "26"
      },
      {
        "kind": "modern",
        "author": "W. W. Tarn",
        "work": "Antigonos Gonatas, Oxford, Clarendon Press, 1913"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": WILL_I
      }
    ]
  },
  {
    "id": "traduction-de-la-septante",
    "title": "Traduction grecque de la Bible : la Septante",
    "start": -269,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Traduction attestée ; celle du Pentateuque est placée par les historiens vers le milieu du IIIe siècle ; le récit de la Lettre d'Aristée, qui la rattache à Ptolémée II, est légendaire dans ses détails.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "religion",
    "importance": 2,
    "placeId": "alexandrie",
    "people": [
      "ptolemee-ii",
      "demetrios-de-phalere"
    ],
    "summary": "Au IIIe siècle, les cinq premiers livres de la Bible hébraïque sont traduits en grec à Alexandrie, où vit une importante communauté juive de langue grecque. Selon la Lettre d'Aristée, 72 savants venus de Jérusalem l'auraient fait à la demande de Ptolémée II, d'où le nom de Septante.",
    "body": "**La légende.** La Lettre d'Aristée, écrite sans doute au IIe siècle, raconte que Démétrios de Phalère conseilla à Ptolémée II de faire entrer la Loi des Juifs dans la Bibliothèque. Le grand prêtre envoya six anciens par tribu, 72 au total, qui achevèrent leur travail en 72 jours dans l'île de Pharos. Philon d'Alexandrie ajoute que leurs traductions, faites séparément, se révélèrent identiques.\n\n**Ce que disent les historiens.** Le récit comporte des invraisemblances : selon Diogène Laërce, Démétrios de Phalère fut disgracié par Ptolémée II dès son avènement. La traduction répond plus probablement aux besoins des Juifs d'Égypte, qui ne lisaient plus l'hébreu ; elle date pour le Pentateuque du milieu du IIIe siècle environ, et les autres livres suivent jusqu'au Ier siècle.\n\n**Une portée immense.** La Septante est la Bible des Juifs de langue grecque, puis des premiers chrétiens, qui la citent dans le Nouveau Testament ; elle reste l'Ancien Testament de l'Église orthodoxe. C'est l'une des plus anciennes grandes traductions connues.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Lettre d'Aristée à Philocrate",
        "work": "Lettre d'Aristée",
        "locus": "9 à 11 et 301 à 311"
      },
      {
        "kind": "ancient",
        "author": "Flavius Josèphe",
        "work": "Antiquités juives",
        "locus": "XII, 11 à 118"
      },
      {
        "kind": "ancient",
        "author": "Philon d'Alexandrie",
        "work": "Vie de Moïse",
        "locus": "II, 25 à 44"
      },
      {
        "kind": "ancient",
        "author": "Diogène Laërce",
        "work": "Vies et doctrines des philosophes illustres",
        "locus": "V, 78"
      },
      {
        "kind": "modern",
        "author": "Gilles Dorival, Marguerite Harl et Olivier Munnich",
        "work": "La Bible grecque des Septante : du judaïsme hellénistique au christianisme ancien, Paris, Cerf, 1988"
      }
    ]
  },
  {
    "id": "guerre-chremonideenne",
    "title": "Guerre chrémonidéenne",
    "start": -267,
    "end": -261,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Guerre attestée ; son début (268/267 ou 265/264) et la capitulation d'Athènes (263/262 ou 262/261) dépendent de la liste des archontes athéniens, encore discutée.",
    "era": "hellenistique",
    "track": "athenes",
    "category": "war",
    "importance": 3,
    "placeId": "athenes",
    "people": [
      "chremonide",
      "antigone-gonatas",
      "ptolemee-ii"
    ],
    "summary": "Vers 268, sur proposition de Chrémonidès, Athènes s'allie à Sparte et à Ptolémée II contre Antigone Gonatas. Assiégée, mal secourue par la flotte égyptienne, la ville capitule vers 262 après la mort du roi spartiate Areus. Elle reçoit une garnison macédonienne et ne joue plus de rôle militaire indépendant.",
    "body": "**Le décret.** Le décret de Chrémonidès, conservé par une inscription, célèbre l'alliance d'Athènes et de Sparte, comme au temps des guerres médiques, pour la liberté des Grecs. Ptolémée II soutient la coalition, qui veut chasser les garnisons d'Antigone, notamment celle de Corinthe.\n\n**La guerre.** Antigone bloque Athènes par terre et par mer. Le roi de Sparte Areus Ier est tué vers 265 près de Corinthe, et la flotte de Ptolémée, commandée par Patroclos, ne force pas le blocus. Affamée, Athènes se rend vers 262.\n\n**Les conséquences.** Antigone installe des garnisons dans la ville, sur la colline du Mouseion, et au Pirée, et surveille Athènes jusqu'en 229. Chrémonidès et son frère se réfugient en Égypte. Pour beaucoup d'historiens, cette guerre marque la fin d'Athènes comme puissance politique.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Décret de Chrémonidès",
        "work": "Inscription d'Athènes, IG II² 686 et 687 (Syll.³ 434/435)"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 1, 1 et III, 6, 4 à 6"
      },
      {
        "kind": "modern",
        "author": "Christian Habicht",
        "work": HABICHT,
        "locus": "chap. 5"
      }
    ]
  },
  {
    "id": "aratos-prend-l-acrocorinthe",
    "title": "Aratos prend l'Acrocorinthe",
    "start": -242,
    "precision": "year",
    "certainty": "attested",
    "era": "hellenistique",
    "track": "ligues",
    "category": "war",
    "importance": 3,
    "placeId": "acrocorinthe",
    "people": [
      "aratos-de-sicyone",
      "antigone-gonatas"
    ],
    "summary": "En 243, Aratos de Sicyone, stratège de la ligue achéenne, s'empare par surprise, de nuit, de l'Acrocorinthe, la citadelle de Corinthe tenue par une garnison d'Antigone Gonatas. Corinthe, Mégare et d'autres cités rejoignent la ligue, qui devient la principale puissance du Péloponnèse.",
    "body": "**Une ligue renaissante.** La ligue achéenne, confédération des petites cités d'Achaïe sur la rive sud du golfe de Corinthe, s'est reconstituée vers 280. Aratos, qui a chassé le tyran de sa patrie Sicyone en 251 et l'a fait entrer dans la ligue, en est élu stratège pour la première fois en 245.\n\n**Le coup de main.** Plutarque raconte l'opération en détail : guidés par des frères syriens qui connaissaient un passage le long des remparts, quelques centaines d'hommes escaladent la citadelle de nuit, au clair de lune, et la garnison macédonienne est forcée de se rendre au matin. L'Acrocorinthe commande l'isthme : Polybe rapporte que Philippe V l'appelait l'une des « entraves de la Grèce ».\n\n**Une confédération originale.** Les cités membres gardent leurs institutions mais partagent une armée, des poids, des mesures, une monnaie et des magistrats fédéraux élus. Polybe, lui-même achéen, en fait l'éloge comme d'un modèle d'union entre Grecs.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Aratos",
        "locus": "16 à 24"
      },
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "II, 37 à 43 et XVIII, 11, 5"
      },
      {
        "kind": "modern",
        "author": "F. W. Walbank",
        "work": "Aratos of Sicyon, Cambridge, Cambridge University Press, 1933"
      }
    ]
  },
  {
    "id": "attale-ier-vainqueur-des-galates",
    "title": "Attale Ier bat les Galates et prend le titre de roi",
    "start": -239,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Victoire et titre royal attestés ; la date, le plus souvent placée vers 238, est discutée entre 240 et 230.",
    "era": "hellenistique",
    "track": "pergame",
    "category": "war",
    "importance": 2,
    "placeId": "pergame",
    "people": [
      "attale-ier"
    ],
    "summary": "Vers 238, Attale Ier, maître de Pergame, refuse de payer tribut aux Galates et les bat près des sources du Caïque. Il prend alors le titre de roi et célèbre sa victoire par des monuments, dont dériveraient les célèbres copies romaines du Galate mourant et du Galate se tuant avec sa femme.",
    "body": "**Le tribut.** Installés en Anatolie centrale depuis 278/277, les Galates rançonnent les cités et les dynastes d'Asie Mineure. Selon Tite-Live, Attale est le premier à refuser de leur payer tribut. Cette victoire, puis d'autres sur Antiochos Hiérax et ses alliés galates, lui permettent de s'étendre en Asie Mineure.\n\n**Le titre royal.** Polybe écrit qu'après avoir vaincu les Galates, le peuple le plus redoutable de l'Asie, Attale se proclama roi. Il est le premier des Attalides à porter ce titre, que ses successeurs garderont jusqu'en 133.\n\n**Les monuments.** Des bases inscrites du sanctuaire d'Athéna à Pergame commémorent ces victoires. Le Galate mourant du Capitole et le groupe du Galate Ludovisi sont souvent tenus pour des copies romaines d'originaux en bronze de Pergame, un lien admis par beaucoup mais non prouvé. Pausanias décrit aussi les statues de Galates vaincus qu'Attale fit dédier sur l'Acropole d'Athènes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XVIII, 41"
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XXXVIII, 16, 14"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 25, 2"
      },
      {
        "kind": "modern",
        "author": "Esther V. Hansen",
        "work": HANSEN
      },
      {
        "kind": "modern",
        "author": "R. E. Allen",
        "work": "The Attalid Kingdom: A Constitutional History, Oxford, Clarendon Press, 1983"
      }
    ]
  },
  {
    "id": "eratosthene-mesure-la-terre",
    "title": "Ératosthène mesure la Terre",
    "start": -239,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Mesure attestée, mais sa méthode n'est connue que par Cléomède, auteur bien plus tardif ; ni la date de la mesure ni la longueur du stade employé ne sont connues.",
    "era": "hellenistique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "alexandrie",
    "people": [
      "eratosthene"
    ],
    "summary": "Vers 240, Ératosthène, bibliothécaire d'Alexandrie, calcule la circonférence de la Terre en comparant l'ombre du soleil de midi, au solstice d'été, à Syène et à Alexandrie. Il obtient 250 000 stades, valeur arrondie ensuite à 252 000, soit environ 40 000 km avec un stade de 157,5 m, une équivalence discutée.",
    "body": "**La méthode.** À Syène (Assouan), le jour du solstice d'été, le soleil de midi éclaire le fond des puits : il est au zénith. Au même moment, à Alexandrie, supposée sur le même méridien, l'ombre d'un gnomon dans un cadran hémisphérique indique un écart d'un cinquantième de cercle. La distance entre les deux villes étant estimée à 5 000 stades, la circonférence vaut 50 fois 5 000, soit 250 000 stades.\n\n**Combien de kilomètres ?** Tout dépend du stade employé, que les textes ne précisent pas. Avec un stade de 157,5 m, on trouve environ 39 400 km, très proche des 40 000 km réels ; avec le stade attique d'environ 185 m, plus de 46 000 km, soit 15 % de trop. Les approximations (Syène n'est exactement ni sur le tropique ni sur le méridien d'Alexandrie) se compensent en partie.\n\n**Le savant.** Ératosthène de Cyrène, appelé à Alexandrie par Ptolémée III, est aussi géographe, chronographe (il date la prise de Troie et les premières olympiades) et poète. Selon la Souda, ses rivaux le surnommaient « Bêta », le deuxième en toutes les disciplines.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Cléomède",
        "work": "Théorie élémentaire (Caelestia)",
        "locus": "I, 7 (édition Todd ; I, 10 dans les éditions anciennes)"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "II, 5, 7 et II, 5, 34"
      },
      {
        "kind": "modern",
        "author": "Germaine Aujac",
        "work": "Ératosthène de Cyrène, le pionnier de la géographie, Paris, Éditions du CTHS, 2001"
      }
    ]
  },
  {
    "id": "bataille-de-sellasie",
    "title": "Bataille de Sellasie",
    "start": -221,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée, en général datée de l'été 222 ; quelques historiens la placent en 221.",
    "era": "hellenistique",
    "track": "sparte",
    "category": "war",
    "importance": 3,
    "placeId": "sellasie",
    "people": [
      "cleomene-iii",
      "antigone-doson",
      "philopoemen"
    ],
    "summary": "En 222, à Sellasie, au nord de Sparte, Antigone Doson, roi de Macédoine allié à la ligue achéenne, écrase l'armée du roi réformateur Cléomène III. Sparte est occupée par un ennemi, ce qui ne lui était jamais arrivé, et Cléomène s'enfuit en Égypte, où il meurt en 219.",
    "body": "**Les réformes de Cléomène.** Roi depuis 235, Cléomène III fait tuer les éphores en 227, annule les dettes, redistribue les terres et donne la citoyenneté à des périèques, reprenant le programme d'Agis IV. Ses succès contre la ligue achéenne poussent Aratos à appeler la Macédoine, l'ennemie de toujours.\n\n**La bataille.** Polybe donne à Antigone 28 000 fantassins et 1 200 cavaliers, à Cléomène environ 20 000 hommes, retranchés sur deux collines qui barrent la route de Sparte. La phalange macédonienne enfonce l'aile tenue par Cléomène ; le jeune Philopœmen, à la tête des cavaliers de Mégalopolis, se distingue en chargeant sans en avoir reçu l'ordre.\n\n**La fin d'un rêve.** Antigone entre dans Sparte, rétablit les anciennes institutions et repart défendre la Macédoine. Cléomène, réfugié à Alexandrie, tente un soulèvement et se donne la mort en 219 ; Plutarque fait de lui, avec Agis, un héros de la justice sociale.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "II, 65 à 70"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cléomène",
        "locus": "7 à 11 et 27 à 29"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Philopœmen",
        "locus": "6"
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge et Antony Spawforth",
        "work": CARTLEDGE
      }
    ]
  },
  {
    "id": "bataille-de-raphia",
    "title": "Bataille de Raphia",
    "start": -216,
    "month": 6,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Le décret de Raphia place la victoire le 10 Pachôns de l'an 5 de Ptolémée IV, soit vers le 22 juin 217 ; la conversion des calendriers laisse une petite marge.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "war",
    "importance": 2,
    "placeId": "raphia",
    "people": [
      "ptolemee-iv",
      "antiochos-iii"
    ],
    "summary": "En juin 217, près de Raphia, au sud de Gaza, Ptolémée IV bat Antiochos III, qui voulait lui prendre la Syrie du Sud. C'est l'une des plus grandes batailles hellénistiques, avec plus de 140 000 hommes et 175 éléphants selon Polybe, et la première où les Lagides engagent en masse des Égyptiens dans leur phalange.",
    "body": "**La quatrième guerre de Syrie.** La Coelé-Syrie, entre le Liban et l'Égypte, est disputée entre Lagides et Séleucides depuis Ipsos. Antiochos III, jeune roi ambitieux, l'envahit en 219 ; Ptolémée IV, conseillé par son ministre Sosibios, profite des négociations pour lever et entraîner une armée.\n\n**La bataille.** Selon Polybe, Ptolémée aligne 70 000 fantassins, 5 000 cavaliers et 73 éléphants d'Afrique, Antiochos 62 000 fantassins, 6 000 cavaliers et 102 éléphants d'Inde. Les éléphants indiens mettent en fuite ceux de Ptolémée et Antiochos l'emporte sur son aile, mais il poursuit trop loin ; au centre, la phalange lagide, renforcée de 20 000 Égyptiens, enfonce celle de son adversaire.\n\n**Les conséquences.** Ptolémée garde la Coelé-Syrie, pour une quinzaine d'années seulement. Polybe estime que l'armement des Égyptiens leur donna confiance et fut à l'origine des révoltes indigènes qui troublent ensuite l'Égypte. Le décret trilingue de Raphia célèbre la victoire du roi selon les formes pharaoniques.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "V, 79 à 86 et V, 107, 1 à 3"
      },
      {
        "kind": "ancient",
        "author": "Décret de Raphia (stèle de Pithom)",
        "work": "H. Gauthier et H. Sottas, Un décret trilingue en l'honneur de Ptolémée IV, Le Caire, Institut français d'archéologie orientale, 1925"
      },
      {
        "kind": "modern",
        "author": "Bezalel Bar-Kochva",
        "work": "The Seleucid Army: Organization and Tactics in the Great Campaigns, Cambridge, Cambridge University Press, 1976"
      }
    ]
  },
  {
    "id": "archimede-et-le-siege-de-syracuse",
    "title": "Archimède et le siège de Syracuse",
    "start": -212,
    "end": -211,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Siège attesté, de 213 à 212 ; Marcellus arrive en Sicile dès 214 et Tite-Live fait commencer les assauts cette année-là ; la mort d'Archimède est racontée en plusieurs versions, et les miroirs ardents sont une légende tardive.",
    "era": "hellenistique",
    "track": "occident",
    "category": "war",
    "importance": 2,
    "placeId": "syracuse",
    "people": [
      "archimede",
      "marcellus",
      "hieron-ii"
    ],
    "summary": "Après la mort de Hiéron II, Syracuse passe dans le camp de Carthage. Assiégée par Marcellus à partir de 213, elle résiste longtemps grâce aux machines d'Archimède, puis tombe en 212 ; Archimède est tué par un soldat romain. La prise de la ville met fin à l'indépendance des Grecs de Sicile.",
    "body": "**Les machines.** Polybe, Tite-Live et Plutarque décrivent des catapultes réglées pour toutes les distances et des grues qui saisissent l'avant des navires romains pour les soulever et les fracasser. Archimède, auteur de travaux sur la sphère et le cylindre, les leviers et les corps flottants, avait servi le roi Hiéron II. Les miroirs qui auraient enflammé la flotte n'apparaissent que chez des auteurs bien plus tardifs.\n\n**La chute.** Marcellus, renonçant à l'assaut, bloque la ville. En 212, il profite d'une fête d'Artémis pour franchir les murs ; les derniers quartiers tombent ensuite par trahison, et la ville est pillée. Ses œuvres d'art, emportées à Rome, y répandent le goût de l'art grec.\n\n**La mort d'Archimède.** Selon la version la plus connue, rapportée par Plutarque, il était absorbé par un problème de géométrie quand un soldat le tua, malgré l'ordre de Marcellus de l'épargner. Cicéron raconte avoir retrouvé sa tombe, envahie de broussailles, grâce à la sphère et au cylindre qui y étaient sculptés.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "VIII, 3 à 7 (numérotation de l'édition Loeb)"
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XXIV, 34 et XXV, 23 à 31"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Marcellus",
        "locus": "14 à 19"
      },
      {
        "kind": "ancient",
        "author": "Cicéron",
        "work": "Tusculanes",
        "locus": "V, 64 à 66"
      },
      {
        "kind": "modern",
        "author": "E. J. Dijksterhuis",
        "work": "Archimedes, trad. anglaise, Princeton, Princeton University Press, 1987"
      }
    ]
  },
  {
    "id": "bataille-de-cynoscephales",
    "title": "Bataille de Cynoscéphales",
    "start": -196,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée, au printemps ou au début de l'été 197.",
    "era": "hellenistique",
    "track": "macedoine",
    "category": "war",
    "importance": 2,
    "placeId": "cynoscephales",
    "people": [
      "philippe-v",
      "flamininus"
    ],
    "summary": "En 197, dans les collines de Cynoscéphales, en Thessalie, les légions du consul Flamininus et leurs alliés étoliens battent la phalange de Philippe V. Polybe y voit la preuve de la supériorité de la légion, plus souple, sur la phalange macédonienne, redoutable de face mais vulnérable sur un terrain accidenté.",
    "body": "**La deuxième guerre de Macédoine.** En 200, Rome, sollicitée par Pergame et Rhodes, déclare la guerre à Philippe V, qui s'étend en Égée. Flamininus, consul en 198, prend le commandement et rallie la ligue achéenne.\n\n**La bataille.** Les deux armées, de 25 000 à 26 000 hommes chacune environ, se heurtent par surprise dans le brouillard, de part et d'autre de collines aux sommets arrondis, les « têtes de chien ». L'aile droite de Philippe repousse les Romains, mais son aile gauche, qui arrive en désordre, est rompue par les éléphants. Un tribun resté anonyme prend alors à revers la phalange victorieuse avec une vingtaine de manipules. Selon Polybe, Philippe perd environ 8 000 tués et 5 000 prisonniers, les Romains 700 hommes.\n\n**La paix.** Philippe doit évacuer la Grèce, livrer sa flotte et payer 1 000 talents. Polybe consacre à la bataille une célèbre comparaison de la phalange et de la légion.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XVIII, 18 à 32"
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XXXIII, 6 à 10"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Flamininus",
        "locus": "7 à 8"
      },
      {
        "kind": "modern",
        "author": "F. W. Walbank",
        "work": "Philip V of Macedon, Cambridge, Cambridge University Press, 1940"
      },
      {
        "kind": "modern",
        "author": "Erich S. Gruen",
        "work": GRUEN
      }
    ]
  },
  {
    "id": "flamininus-proclame-la-liberte-des-grecs",
    "title": "Flamininus proclame la liberté des Grecs",
    "start": -195,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Proclamation attestée, lors des Jeux isthmiques de 196, au printemps ou au début de l'été.",
    "era": "hellenistique",
    "track": "rome",
    "category": "politics",
    "importance": 2,
    "placeId": "isthmia",
    "people": [
      "flamininus",
      "philippe-v"
    ],
    "summary": "Aux Jeux isthmiques de 196, devant une foule venue de toute la Grèce, un héraut proclame au nom du Sénat et de Flamininus la liberté des Grecs soumis jusque-là à Philippe V. Selon Plutarque, les cris de joie font tomber des oiseaux du ciel. Rome se présente en libératrice et devient l'arbitre des affaires grecques.",
    "body": "**Le texte.** Polybe rapporte la proclamation : Corinthiens, Phocidiens, Locriens, Eubéens, Achéens de Phthiotide, Magnètes, Thessaliens et Perrhèbes seront libres, sans garnison ni tribut, et vivront selon leurs propres lois. Il raconte que la foule, n'en croyant pas ses oreilles, fit répéter le héraut.\n\n**Une liberté sous condition.** Les Romains évacuent en 194 les places fortes de Corinthe, Chalcis et Démétrias, ce qui surprend les Grecs. Mais les Étoliens, déçus du partage, dénoncent une liberté octroyée par un protecteur, et Rome intervient désormais dans les conflits entre cités.\n\n**Un langage royal.** Proclamer la liberté des Grecs était déjà un geste des rois, d'Antigone le Borgne aux Ptolémées. Flamininus reprend ce langage, reçoit des honneurs cultuels dans plusieurs cités et fait frapper des statères d'or à son portrait.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XVIII, 46"
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XXXIII, 32 à 33"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Flamininus",
        "locus": "10 à 12"
      },
      {
        "kind": "modern",
        "author": "Jean-Louis Ferrary",
        "work": "Philhellénisme et impérialisme : aspects idéologiques de la conquête romaine du monde hellénistique, Rome, École française de Rome, 1988"
      },
      {
        "kind": "modern",
        "author": "Erich S. Gruen",
        "work": GRUEN
      }
    ]
  },
  {
    "id": "pierre-de-rosette",
    "title": "Décret de Memphis, gravé sur la pierre de Rosette",
    "start": -195,
    "month": 3,
    "day": 27,
    "precision": "day",
    "certainty": "attested",
    "certaintyNote": "Date donnée par le texte lui-même (4 Xandikos, 18 Méchir de l'an 9 de Ptolémée V). La pierre de Rosette est l'une des copies du décret, retrouvée en 1799.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "religion",
    "importance": 1,
    "placeId": "memphis",
    "people": [
      "ptolemee-v"
    ],
    "summary": "Le 27 mars 196, les prêtres d'Égypte réunis à Memphis honorent le jeune Ptolémée V par un décret gravé en hiéroglyphes, en démotique et en grec sur des stèles dressées dans les temples. L'une de ces stèles, retrouvée en 1799 à Rosette (Rachid), a permis à Champollion de déchiffrer les hiéroglyphes en 1822.",
    "body": "**Le décret.** Le synode des prêtres, réuni pour le couronnement de Ptolémée V selon le rite pharaonique, énumère ses bienfaits : remises d'impôts, amnisties, dons aux temples, victoire sur les rebelles retranchés à Lycopolis, dans le Delta. En échange, il décide d'honorer le roi d'un culte dans tous les temples. Le texte montre combien le pouvoir lagide dépend du clergé, alors que le Sud de l'Égypte est en révolte.\n\n**La pierre.** La stèle de granodiorite, brisée, avait été remployée dans un mur. Des soldats français l'y découvrent en juillet 1799, lors de travaux au fort de Rachid ; cédée aux Britanniques par la capitulation d'Alexandrie en 1801, elle est au British Museum depuis 1802.\n\n**Le déchiffrement.** Le grec, lisible, donnait le sens du texte. Thomas Young reconnaît des noms royaux dans les cartouches, et Jean-François Champollion montre en 1822, dans sa Lettre à M. Dacier, que les hiéroglyphes combinent des signes qui notent des sons et des signes qui notent des idées.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Décret de Memphis (texte grec)",
        "work": "W. Dittenberger, Orientis Graeci Inscriptiones Selectae",
        "locus": "OGIS 90"
      },
      {
        "kind": "modern",
        "author": "R. B. Parkinson",
        "work": "Cracking Codes: The Rosetta Stone and Decipherment, London, British Museum Press, 1999"
      }
    ]
  },
  {
    "id": "sparte-entre-dans-la-ligue-acheenne",
    "title": "Mort de Nabis : Sparte entre dans la ligue achéenne",
    "start": -191,
    "precision": "year",
    "certainty": "attested",
    "era": "hellenistique",
    "track": "sparte",
    "category": "politics",
    "importance": 3,
    "placeId": "sparte",
    "people": [
      "nabis",
      "philopoemen"
    ],
    "summary": "En 192, le roi Nabis est assassiné par des Étoliens venus en alliés. Profitant du désordre, Philopœmen, stratège de la ligue achéenne, entre dans Sparte et la fait adhérer à la confédération. La cité qui avait dominé le Péloponnèse pendant des siècles n'est plus qu'un membre parmi d'autres d'une ligue qu'elle avait combattue.",
    "body": "**Nabis.** Roi depuis 207, Nabis poursuit les réformes radicales de Cléomène : exil des riches, partage des terres, affranchissement d'hilotes. Polybe et Tite-Live, qui lui sont hostiles, en font un tyran cruel. Battu par Flamininus en 195, il perd le port de Gythion et les cités côtières de Laconie.\n\n**Le meurtre.** En 192, les Étoliens, qui préparent la guerre aux côtés d'Antiochos III, envoient à Sparte un contingent sous prétexte d'aide ; leur chef Alexaménos tue Nabis pendant une revue. Les Spartiates massacrent les Étoliens, et Philopœmen arrive pour imposer l'adhésion à la ligue.\n\n**Une adhésion forcée.** Sparte ne se résigne pas : ses révoltes conduisent Philopœmen à abattre ses murs et à abolir les lois de Lycurgue en 188. Les querelles entre Sparte et la ligue fourniront à Rome le prétexte de la guerre d'Achaïe, en 146.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XXXV, 35 à 37"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Philopœmen",
        "locus": "15 à 16"
      },
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XIII, 6 à 8"
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge et Antony Spawforth",
        "work": CARTLEDGE
      }
    ]
  },
  {
    "id": "magnesie-et-paix-d-apamee",
    "title": "Bataille de Magnésie et paix d'Apamée",
    "start": -189,
    "end": -187,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "La bataille de Magnésie se place en décembre 190 ou en janvier 189, le calendrier romain étant alors décalé ; la paix d'Apamée est conclue en 188.",
    "era": "hellenistique",
    "track": "seleucides",
    "category": "war",
    "importance": 2,
    "placeId": "magnesie-du-sipyle",
    "people": [
      "antiochos-iii",
      "lucius-scipion",
      "eumene-ii"
    ],
    "summary": "Vaincu aux Thermopyles en 191, Antiochos III est écrasé près de Magnésie du Sipyle, vers la fin de 190, par l'armée de Lucius Scipion et d'Eumène II de Pergame. Par la paix d'Apamée (188), il abandonne l'Asie Mineure au nord du Taurus et doit payer 15 000 talents ; Pergame et Rhodes se partagent ses possessions.",
    "body": "**La guerre antiochique.** Antiochos III, qui a reconquis l'Orient, la Coelé-Syrie et une partie de l'Asie Mineure, passe en Grèce en 192 à l'appel des Étoliens. Battu aux Thermopyles en 191, il repasse en Asie ; les Romains, aidés des flottes de Rhodes et de Pergame, l'y suivent.\n\n**Magnésie.** Tite-Live donne au roi 60 000 fantassins et plus de 12 000 cavaliers, avec des éléphants et des chars à faux, contre environ 30 000 hommes aux Romains. Antiochos, vainqueur sur son aile, poursuit trop loin, comme à Raphia ; ses chars, affolés, désorganisent sa propre gauche, que la cavalerie d'Eumène II met en fuite, et sa phalange, encerclée, est massacrée.\n\n**Apamée.** Le traité interdit au roi d'entretenir des éléphants et plus de dix navires de guerre, et lui impose des otages, dont son fils, le futur Antiochos IV. Eumène II reçoit l'essentiel de l'Asie Mineure, Rhodes la Lycie et la Carie au sud du Méandre. Rome n'annexe rien, mais aucun royaume ne peut plus lui tenir tête.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XXXVII, 37 à 44 et XXXVIII, 38"
      },
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XXI, 42 à 45 (numérotation de l'édition Loeb)"
      },
      {
        "kind": "ancient",
        "author": "Appien",
        "work": "Histoire romaine, livre syriaque",
        "locus": "30 à 39"
      },
      {
        "kind": "modern",
        "author": "John D. Grainger",
        "work": "The Roman War of Antiochos the Great, Leiden, Brill, 2002"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": WILL_II
      }
    ]
  },
  {
    "id": "grand-autel-de-pergame",
    "title": "Grand Autel de Pergame",
    "start": -179,
    "end": -159,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Monument conservé, à la date discutée : la plupart des historiens placent l'autel sous Eumène II, entre 180 et 160 environ ; certains le rattachent aux victoires sur les Galates de 168 à 166.",
    "era": "hellenistique",
    "track": "pergame",
    "category": "building",
    "importance": 2,
    "placeId": "pergame",
    "people": [
      "eumene-ii"
    ],
    "summary": "Sous Eumène II, Pergame élève sur son acropole un immense autel de marbre, dont la frise, longue de plus de 110 m, montre le combat des dieux contre les Géants. Chef-d'œuvre de la sculpture hellénistique, dégagé à partir de 1878 par Carl Humann, il est remonté à Berlin, au Pergamonmuseum.",
    "body": "**Le monument.** Sur un socle d'environ 36 m sur 34, un escalier monumental mène à une cour où se trouvait l'autel des sacrifices. La grande frise, haute de 2,30 m, court autour du socle : Zeus, Athéna et les dieux de l'Olympe y écrasent les Géants, image d'un ordre vainqueur du chaos, comme les Attalides vainqueurs des Galates. Une petite frise intérieure raconte la vie de Télèphe, ancêtre mythique des rois de Pergame.\n\n**Une seule mention antique.** Le compilateur latin Ampelius, sans doute au IIe ou IIIe siècle apr. J.-C., cite à Pergame un grand autel de marbre haut de 40 pieds, orné d'une gigantomachie. Ni la divinité honorée (Zeus, Athéna, ou les dieux en général) ni la date exacte ne sont assurées ; la céramique et les monnaies trouvées dans les fondations nourrissent la discussion.\n\n**Redécouverte.** L'ingénieur Carl Humann repère des plaques de la frise remployées dans des murs byzantins, et les fouilles commencent en 1878. Les fragments partent à Berlin, où l'autel est remonté dans le Pergamonmuseum, ouvert en 1930.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Ampelius",
        "work": "Liber memorialis",
        "locus": "8, 14"
      },
      {
        "kind": "modern",
        "author": "François Queyrel",
        "work": "L'Autel de Pergame : images et pouvoir en Grèce d'Asie, Paris, Picard, 2005"
      },
      {
        "kind": "modern",
        "author": "Esther V. Hansen",
        "work": HANSEN
      }
    ]
  },
  {
    "id": "bataille-de-pydna",
    "title": "Bataille de Pydna : fin du royaume de Macédoine",
    "start": -167,
    "month": 6,
    "day": 22,
    "precision": "day",
    "certainty": "attested",
    "certaintyNote": "Date tirée de l'éclipse de lune survenue la veille, que décrit Tite-Live et que les astronomes placent dans la nuit du 21 au 22 juin 168 ; le calendrier romain, décalé, donnait une autre date.",
    "era": "hellenistique",
    "track": "macedoine",
    "category": "war",
    "importance": 1,
    "placeId": "pydna",
    "people": [
      "persee-de-macedoine",
      "paul-emile"
    ],
    "summary": "Le 22 juin 168, près de Pydna, le consul Paul-Émile écrase l'armée de Persée, dernier roi de Macédoine. La phalange, disloquée sur un terrain inégal, est taillée en pièces en peu de temps. Persée est capturé, la royauté antigonide supprimée, et la Macédoine divisée en quatre républiques sous contrôle romain.",
    "body": "**La troisième guerre de Macédoine.** Persée, fils de Philippe V, relève la puissance macédonienne et gagne des sympathies en Grèce. Eumène II de Pergame le dénonce à Rome, qui lui déclare la guerre en 171. Après trois ans d'opérations indécises, Paul-Émile, consul en 168, l'oblige à combattre dans la plaine de Pydna.\n\n**L'éclipse et la bataille.** La veille, une éclipse de lune effraie les Macédoniens ; un officier romain, Sulpicius Gallus, l'avait annoncée à ses soldats. Le combat s'engage presque par hasard, autour d'un cheval échappé selon Plutarque. La phalange avance d'abord irrésistiblement, mais sur le terrain accidenté elle s'ouvre, et les manipules s'engouffrent dans les brèches. Tite-Live compte 20 000 Macédoniens tués et 11 000 prisonniers ; Plutarque, une centaine de morts romains au plus.\n\n**La fin d'un royaume.** Persée, réfugié à Samothrace, se rend ; il figure au triomphe de Paul-Émile et meurt captif à Albe. La dynastie antigonide disparaît, et la Macédoine devient province romaine en 148, après la révolte d'Andriscos.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XLIV, 36 à 42 et XLV, 29"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Paul-Émile",
        "locus": "16 à 22"
      },
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XXIX, 15 à 17"
      },
      {
        "kind": "modern",
        "author": "N. G. L. Hammond",
        "work": "The Battle of Pydna, Journal of Hellenic Studies, 104, 1984",
        "locus": "p. 31 à 47"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": WILL_II
      }
    ]
  },
  {
    "id": "jour-d-eleusis",
    "title": "Le jour d'Éleusis : Rome chasse Antiochos IV d'Égypte",
    "start": -167,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Entrevue attestée, à l'été 168, peu après Pydna ; les auteurs anciens n'en donnent pas le jour.",
    "era": "hellenistique",
    "track": "seleucides",
    "category": "politics",
    "importance": 2,
    "placeId": "alexandrie",
    "people": [
      "antiochos-iv",
      "popilius-laenas"
    ],
    "summary": "À l'été 168, Antiochos IV, qui marche sur Alexandrie, reçoit à Éleusis, faubourg de la ville, l'ambassadeur romain Popillius Laenas. Celui-ci lui remet l'ordre du Sénat de quitter l'Égypte, trace un cercle autour du roi avec son bâton et exige une réponse avant qu'il n'en sorte. Antiochos cède.",
    "body": "**La sixième guerre de Syrie.** Antiochos IV a envahi l'Égypte en 170 et 169, profitant de la faiblesse des jeunes Ptolémée VI et Ptolémée VIII ; en 168, il occupe Chypre et Memphis et marche sur Alexandrie. Les Lagides demandent l'aide de Rome, alors occupée par la guerre contre Persée.\n\n**Le cercle.** Polybe, contemporain et bien informé, raconte la scène : Popillius refuse la main que lui tend le roi, qu'il avait connu à Rome, et lui donne la tablette du Sénat. Antiochos demande à consulter ses conseillers ; Popillius trace un cercle autour de lui avec son bâton de sarment. Le roi, après un moment de stupeur, accepte, et Popillius lui serre enfin la main.\n\n**La portée.** La nouvelle de Pydna, arrivée peu avant, rendait la menace crédible. Sans un soldat, Rome impose sa volonté au plus puissant roi d'Orient : l'épisode symbolise la fin de l'autonomie des royaumes hellénistiques.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XXIX, 27"
      },
      {
        "kind": "ancient",
        "author": "Tite-Live",
        "work": "Histoire romaine",
        "locus": "XLV, 12"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XXXI, 2"
      },
      {
        "kind": "modern",
        "author": "Otto Mørkholm",
        "work": "Antiochus IV of Syria, Copenhague, Gyldendal, 1966"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": WILL_II
      }
    ]
  },
  {
    "id": "otages-acheens-a-rome",
    "title": "Mille otages achéens à Rome, dont Polybe",
    "start": -166,
    "precision": "year",
    "certainty": "attested",
    "era": "hellenistique",
    "track": "ligues",
    "category": "politics",
    "importance": 3,
    "placeId": "rome",
    "people": [
      "polybe",
      "paul-emile"
    ],
    "summary": "Après Pydna, Rome se fait livrer un millier de notables achéens jugés peu sûrs, parmi lesquels l'historien Polybe. Retenus en Italie sans jugement pendant seize ans, ils ne sont libérés qu'en 150, quand les survivants ne sont plus que 300 environ. Polybe, devenu l'ami de Scipion Émilien, écrit à Rome l'histoire de la conquête romaine.",
    "body": "**Les listes de Callicratès.** Le stratège achéen Callicratès, partisan de Rome, dénonce les hommes politiques qui avaient prôné la neutralité pendant la guerre contre Persée. Le Sénat convoque plus de mille d'entre eux en Italie, officiellement pour les juger ; ils sont répartis dans les villes d'Étrurie et ne sont jamais jugés.\n\n**Polybe.** Fils du stratège Lycortas et hipparque de la ligue en 170/169, Polybe obtient de rester à Rome grâce à l'amitié de Paul-Émile et de ses fils. Il devient le mentor de Scipion Émilien, qu'il accompagnera au siège de Carthage en 146, et écrit une histoire en quarante livres pour expliquer comment Rome a soumis presque tout le monde habité en moins de 53 ans.\n\n**La libération.** En 150, sur intervention de Scipion, le Sénat laisse rentrer les survivants. Quatre ans plus tard, la ligue achéenne entre en guerre contre Rome, ce qui mène au sac de Corinthe.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "I, 1, 5 ; XXX, 13 et 32 ; XXXI, 23 à 25"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "VII, 10, 7 à 12"
      },
      {
        "kind": "modern",
        "author": "F. W. Walbank",
        "work": "Polybius, Berkeley, University of California Press, 1972"
      },
      {
        "kind": "modern",
        "author": "Erich S. Gruen",
        "work": GRUEN
      }
    ]
  },
  {
    "id": "attale-iii-legue-pergame-a-rome",
    "title": "Attale III lègue Pergame à Rome",
    "start": -132,
    "precision": "year",
    "certainty": "attested",
    "era": "hellenistique",
    "track": "pergame",
    "category": "politics",
    "importance": 2,
    "placeId": "pergame",
    "people": [
      "attale-iii",
      "aristonicos"
    ],
    "summary": "En 133, Attale III meurt sans enfant et lègue son royaume au peuple romain. Aristonicos, qui se dit fils d'Eumène II, soulève une partie du pays contre Rome jusqu'en 129. Le royaume devient la province romaine d'Asie, première province de Rome en Asie Mineure.",
    "body": "**Le testament.** Attale III, roi depuis 138, est décrit par les auteurs anciens comme un souverain étrange, passionné de botanique, de poisons et de sculpture. Son testament laisse au peuple romain ses biens et son royaume, mais déclare Pergame libre. Un décret de Pergame, conservé, accorde la citoyenneté à de nouvelles catégories d'habitants au lendemain de sa mort, pour souder la cité.\n\n**Aristonicos.** Se faisant appeler Eumène III, Aristonicos rallie des paysans, des esclaves et des soldats, qu'il nomme « citoyens de la cité du Soleil » (Héliopolites). Il bat et tue le consul Crassus en 130, avant d'être pris par Perperna en 129 et exécuté à Rome.\n\n**L'Asie romaine.** Manius Aquillius organise la province d'Asie de 129 à 126. À Rome, Tiberius Gracchus veut employer le trésor d'Attale pour financer sa réforme agraire, ce qui envenime son conflit avec le Sénat. La province, riche, devient la proie des publicains, les sociétés de collecte des impôts.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIII, 4, 2 et XIV, 1, 38"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Tiberius Gracchus",
        "locus": "14"
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XXXVI, 4"
      },
      {
        "kind": "ancient",
        "author": "Décret de Pergame",
        "work": "W. Dittenberger, Orientis Graeci Inscriptiones Selectae",
        "locus": "OGIS 338"
      },
      {
        "kind": "modern",
        "author": "R. E. Allen",
        "work": "The Attalid Kingdom: A Constitutional History, Oxford, Clarendon Press, 1983"
      },
      {
        "kind": "modern",
        "author": "Erich S. Gruen",
        "work": GRUEN
      }
    ]
  },
  {
    "id": "venus-de-milo",
    "title": "La Vénus de Milo",
    "start": -149,
    "end": -124,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Statue conservée ; sa date, tirée du style et de l'inscription d'une plinthe perdue dont le rattachement est discuté, est placée par le Louvre vers 150 à 125, par d'autres jusque vers 100.",
    "era": "hellenistique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "melos",
    "summary": "Dans la seconde moitié du IIe siècle, un sculpteur, peut-être Alexandros d'Antioche du Méandre, taille pour Mélos une Aphrodite de marbre plus grande que nature. Découverte en 1820 par un paysan de l'île et offerte au roi Louis XVIII, la Vénus de Milo est devenue au Louvre l'une des œuvres antiques les plus célèbres.",
    "body": "**L'œuvre.** Haute de 2,04 m selon le Louvre, faite de deux blocs de marbre de Paros, la déesse se tient debout, le torse nu, une draperie glissant sur les hanches. Elle reprend des modèles du IVe siècle, mais la torsion du corps et le contraste entre la peau et l'étoffe sont typiques de l'art hellénistique. Ses bras, perdus, ont suscité des dizaines de restitutions : tenait-elle une pomme, un bouclier, un miroir ?\n\n**La découverte.** En avril 1820, le paysan Yorgos Kentrotas la trouve dans les ruines de l'antique Mélos. Des officiers de marine français, dont Dumont d'Urville, la signalent, et l'ambassadeur de France à Constantinople, le marquis de Rivière, l'acquiert et l'offre à Louis XVIII.\n\n**L'énigme de la plinthe.** Un fragment de base portant la signature d'Alexandros, fils de Ménidès, d'Antioche du Méandre, fut trouvé avec la statue puis perdu au Louvre ; il n'est connu que par des dessins, et sa lecture est en partie restituée. Son lien avec la statue reste discuté, mais il a fait abandonner l'attribution à Praxitèle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Signature d'Alexandros d'Antioche du Méandre",
        "work": "Inscription de la plinthe perdue, connue par des dessins faits peu après la découverte"
      },
      {
        "kind": "modern",
        "author": "Musée du Louvre",
        "work": "Notice de la Vénus de Milo, inv. Ma 399, collections.louvre.fr",
        "url": "https://collections.louvre.fr/ark:/53355/cl010277627"
      },
      {
        "kind": "modern",
        "author": "Alain Pasquier",
        "work": "La Vénus de Milo et les Aphrodites du Louvre, Paris, Réunion des musées nationaux, 1985"
      },
      {
        "kind": "modern",
        "author": "Rachel Kousser",
        "work": "Creating the Past: The Vénus de Milo and the Hellenistic Reception of Classical Greece, American Journal of Archaeology, 109, 2005",
        "locus": "p. 227 à 250"
      }
    ]
  },
  {
    "id": "sylla-prend-athenes",
    "title": "Sylla prend Athènes",
    "start": -85,
    "month": 3,
    "day": 1,
    "precision": "day",
    "certainty": "attested",
    "certaintyNote": "Plutarque date la prise des calendes de mars, soit le 1er mars 86 du calendrier romain d'alors, qui pouvait être décalé par rapport au calendrier julien.",
    "era": "hellenistique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "sylla",
      "aristion",
      "mithridate-vi"
    ],
    "summary": "En 88, Athènes se range aux côtés de Mithridate VI, roi du Pont, en guerre contre Rome. Sylla assiège la ville et le Pirée pendant l'hiver 87/86 et prend Athènes d'assaut le 1er mars 86 : le massacre est terrible, le tyran Aristion est exécuté et le Pirée détruit peu après. La ville perd ce qui lui restait de puissance.",
    "body": "**Mithridate en Grèce.** En 88, Mithridate VI envahit l'Asie romaine et y fait massacrer en un jour des dizaines de milliers d'Italiens. À Athènes, le philosophe Athénion, puis Aristion, prennent le pouvoir et rallient la ville au roi, dont le général Archélaos occupe le Pirée.\n\n**Le siège.** Sylla débarque en 87 et assiège à la fois Athènes et le Pirée ; il fait abattre les arbres de l'Académie et du Lycée pour construire ses machines et puise dans les trésors de Delphes, d'Olympie et d'Épidaure pour payer ses troupes. Athènes, affamée, est prise par une brèche entre la porte du Pirée et la porte Sacrée ; Plutarque décrit le sang qui inonde le Céramique jusqu'à la porte du Dipylon.\n\n**Après le sac.** Sylla déclare épargner les vivants par égard pour les morts, les grands Athéniens du passé ; Aristion, réfugié sur l'Acropole, se rend et est exécuté. Le Pirée et ses arsenaux sont détruits. Sylla bat ensuite les armées de Mithridate à Chéronée et à Orchomène, et emporte à Rome la bibliothèque d'Apellicon, qui contenait des œuvres d'Aristote.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Sylla",
        "locus": "12 à 14 et 26"
      },
      {
        "kind": "ancient",
        "author": "Appien",
        "work": "Histoire romaine, livre mithridatique",
        "locus": "28 à 41"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 20, 4 à 7"
      },
      {
        "kind": "modern",
        "author": "Christian Habicht",
        "work": HABICHT,
        "locus": "chap. 13"
      },
      {
        "kind": "modern",
        "author": "Brian C. McGing",
        "work": "The Foreign Policy of Mithridates VI Eupator, King of Pontus, Leiden, Brill, 1986"
      }
    ]
  },
  {
    "id": "machine-d-anticythere",
    "title": "Naufrage d'Anticythère et sa machine astronomique",
    "start": -69,
    "end": -59,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Épave et machine conservées ; le naufrage est daté vers 70 à 60 par les monnaies et la céramique ; la date de construction de la machine reste discutée, de la fin du IIIe siècle au début du Ier siècle.",
    "era": "hellenistique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "anticythere",
    "summary": "Vers 70 à 60, un navire chargé d'œuvres d'art coule près de l'île d'Anticythère. Parmi les objets remontés à partir de 1900 se trouve un mécanisme de bronze à engrenages, le plus ancien calculateur astronomique connu : il indiquait les positions du soleil et de la lune, les phases lunaires, les éclipses et le calendrier des grands jeux.",
    "body": "**L'épave.** En 1900, des pêcheurs d'éponges de Symi découvrent l'épave par 45 à 55 m de fond. Les plongeurs remontent des statues de bronze et de marbre, de la vaisselle et des amphores ; en 1902, l'archéologue Valérios Staïs remarque une roue dentée dans des blocs de bronze corrodé. Le navire venait sans doute de l'Égée orientale et faisait route vers l'Italie.\n\n**La machine.** Radiographies puis tomographies (Derek de Solla Price dans les années 1970, l'Antikythera Mechanism Research Project à partir de 2005) ont permis de reconstituer une trentaine de roues dentées conservées. Une manivelle actionnait des cadrans : calendrier égyptien de 365 jours, zodiaque, cycle de Méton de 19 ans, cycle du saros de 223 mois pour prévoir les éclipses, calendrier des jeux panhelléniques. Les inscriptions mentionnent aussi les planètes.\n\n**Questions ouvertes.** On ignore qui l'a construite et où ; on évoque Rhodes, où enseignait Posidonios, ou une tradition remontant à Archimède. Cicéron décrit des sphères mobiles d'Archimède et de Posidonios qui reproduisaient le mouvement des astres : la machine montre que ces récits n'avaient rien d'invraisemblable. Les dates proposées pour sa construction vont de 205 environ au début du Ier siècle.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Cicéron",
        "work": "De la république",
        "locus": "I, 21 à 22"
      },
      {
        "kind": "ancient",
        "author": "Cicéron",
        "work": "De la nature des dieux",
        "locus": "II, 88"
      },
      {
        "kind": "modern",
        "author": "Derek de Solla Price",
        "work": "Gears from the Greeks: The Antikythera Mechanism, a Calendar Computer from ca. 80 B.C., Transactions of the American Philosophical Society, 64, 7, 1974"
      },
      {
        "kind": "modern",
        "author": "Tony Freeth et al.",
        "work": "Decoding the ancient Greek astronomical calculator known as the Antikythera Mechanism, Nature, 444, 2006",
        "locus": "p. 587 à 591"
      },
      {
        "kind": "modern",
        "author": "Christián C. Carman et James Evans",
        "work": "On the epoch of the Antikythera mechanism and its eclipse predictor, Archive for History of Exact Sciences, 68, 2014"
      }
    ]
  },
  {
    "id": "pompee-met-fin-aux-seleucides",
    "title": "Pompée met fin au royaume séleucide",
    "start": -63,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Pompée dépose Antiochos XIII et organise la province de Syrie en 64 ou au début de 63.",
    "era": "hellenistique",
    "track": "seleucides",
    "category": "politics",
    "importance": 2,
    "placeId": "antioche",
    "people": [
      "pompee",
      "antiochos-xiii",
      "mithridate-vi"
    ],
    "summary": "Vainqueur de Mithridate VI, Pompée refuse de reconnaître Antiochos XIII, dernier roi séleucide en place, et fait de la Syrie une province romaine en 64. Le royaume fondé par Séleucos Ier, réduit à quelques villes autour d'Antioche par les conquêtes parthes et les querelles dynastiques, disparaît après deux siècles et demi.",
    "body": "**Un royaume en lambeaux.** Après Magnésie et la perte de l'Iran et de la Mésopotamie au profit des Parthes, les Séleucides s'épuisent dans des guerres entre branches rivales de la dynastie. De 83 à 69, la Syrie est même gouvernée par Tigrane II d'Arménie ; Lucullus, vainqueur de Tigrane, rétablit Antiochos XIII.\n\n**La décision de Pompée.** Chargé de la guerre contre Mithridate, Pompée arrive en Syrie et estime, selon Justin, qu'un roi incapable de défendre son royaume contre les Juifs et les Arabes ne doit pas le garder. Il refuse le trône à Antiochos XIII, bientôt tué par un dynaste arabe d'Émèse, et crée la province de Syrie.\n\n**La fin d'une dynastie.** Pompée réorganise tout l'Orient : il prend Jérusalem en 63 et fonde ou restaure des cités. Les derniers épisodes séleucides restent confus, car un autre prétendant, Philippe II, apparaît encore dans les sources.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Appien",
        "work": "Histoire romaine, livre syriaque",
        "locus": "49 et 70"
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XL, 2"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XL, 1a à 1b"
      },
      {
        "kind": "modern",
        "author": "A. N. Sherwin-White",
        "work": "Roman Foreign Policy in the East, 168 B.C. to A.D. 1, London, Duckworth, 1984"
      },
      {
        "kind": "modern",
        "author": "Édouard Will",
        "work": WILL_II
      }
    ]
  },
  {
    "id": "cleopatre-vii-devient-reine",
    "title": "Cléopâtre VII devient reine",
    "start": -50,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Ptolémée XII meurt au début de 51 ; le mois exact, entre février et l'été, est discuté.",
    "era": "hellenistique",
    "track": "lagides",
    "category": "politics",
    "importance": 2,
    "placeId": "alexandrie",
    "people": [
      "cleopatre-vii",
      "ptolemee-xii",
      "ptolemee-xiii"
    ],
    "summary": "À la mort de Ptolémée XII Aulète, en 51, sa fille Cléopâtre VII, âgée de 18 ans, monte sur le trône avec son jeune frère Ptolémée XIII, comme le prévoyait le testament de leur père, déposé à Rome. Écartée par les conseillers de son frère en 49, elle lève une armée aux confins de la Syrie pour reprendre le pouvoir.",
    "body": "**L'héritage d'Aulète.** Ptolémée XII doit son trône à l'appui de Rome, qu'il a payé très cher ; chassé par les Alexandrins en 58, il a été rétabli en 55 par une armée romaine. Son testament, dont un exemplaire est envoyé à Rome, désigne comme héritiers ses deux aînés, Cléopâtre et Ptolémée XIII, et les place sous la protection du peuple romain.\n\n**Une reine lettrée.** Plutarque assure qu'elle parlait de nombreuses langues et qu'elle fut la première de sa dynastie à apprendre l'égyptien. Ses premières années de règne coïncident avec des crues du Nil insuffisantes et des difficultés financières.\n\n**La rupture.** En 49, les régents de Ptolémée XIII, l'eunuque Pothin et le général Achillas, chassent Cléopâtre d'Alexandrie. C'est dans ce conflit entre frère et sœur qu'interviennent, en 48, l'arrivée de Pompée vaincu puis celle de César.",
    "sources": [
      {
        "kind": "ancient",
        "author": "César",
        "work": "Guerre civile",
        "locus": "III, 103 et 107 à 108"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Antoine",
        "locus": "27"
      },
      {
        "kind": "ancient",
        "author": "Dion Cassius",
        "work": "Histoire romaine",
        "locus": "XLII, 35"
      },
      {
        "kind": "modern",
        "author": "Duane W. Roller",
        "work": ROLLER
      },
      {
        "kind": "modern",
        "author": "Michel Chauveau",
        "work": "L'Égypte au temps de Cléopâtre, Paris, Hachette, 1997"
      }
    ]
  },
  {
    "id": "cesar-a-alexandrie",
    "title": "César à Alexandrie et l'incendie des livres",
    "start": -47,
    "end": -46,
    "month": 10,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "La guerre d'Alexandrie, d'octobre 48 à mars 47, et l'incendie sont attestés ; l'ampleur de l'incendie et les dégâts subis par la Bibliothèque sont discutés, car les sources anciennes ne concordent pas.",
    "era": "hellenistique",
    "track": "rome",
    "category": "war",
    "importance": 2,
    "placeId": "alexandrie",
    "people": [
      "jules-cesar",
      "cleopatre-vii",
      "ptolemee-xiii",
      "pompee"
    ],
    "summary": "Arrivé à Alexandrie en octobre 48, peu après le meurtre de Pompée, César s'allie à Cléopâtre et se retrouve assiégé dans le quartier royal par l'armée de Ptolémée XIII. Pendant les combats, il fait incendier des navires, et le feu gagne des entrepôts du port : selon des auteurs plus tardifs, des dizaines de milliers de livres brûlent.",
    "body": "**Le piège alexandrin.** Pompée, vaincu à Pharsale, cherche refuge en Égypte, où les conseillers de Ptolémée XIII le font assassiner à son débarquement, fin septembre 48. César arrive quelques jours plus tard, avec peu de troupes, et prétend arbitrer entre le roi et sa sœur ; Cléopâtre le rejoint en secret. Pothin et Achillas soulèvent l'armée et la population, et César reste assiégé plusieurs mois.\n\n**L'incendie.** Pour ne pas laisser la flotte égyptienne à l'ennemi, César fait brûler les navires du port. Sénèque parle de 40 000 livres brûlés, Dion Cassius de dépôts de grain et de livres incendiés près des docks, Plutarque de la « grande bibliothèque » ; Aulu-Gelle, au IIe siècle apr. J.-C., avance 700 000 volumes. César lui-même n'en dit rien.\n\n**Ce qu'on peut retenir.** Il s'agit sans doute de livres entreposés près du port, plutôt que de la Bibliothèque elle-même : Strabon fréquente le Musée une vingtaine d'années plus tard. Renforcé par des troupes venues d'Asie, César gagne la bataille du Nil en mars 47, où Ptolémée XIII se noie, et installe Cléopâtre sur le trône.",
    "sources": [
      {
        "kind": "ancient",
        "author": "César",
        "work": "Guerre civile",
        "locus": "III, 106 à 112"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de César",
        "locus": "48 à 49"
      },
      {
        "kind": "ancient",
        "author": "Sénèque",
        "work": "De la tranquillité de l'âme",
        "locus": "9, 5"
      },
      {
        "kind": "ancient",
        "author": "Dion Cassius",
        "work": "Histoire romaine",
        "locus": "XLII, 38"
      },
      {
        "kind": "ancient",
        "author": "Aulu-Gelle",
        "work": "Nuits attiques",
        "locus": "VII, 17, 3"
      },
      {
        "kind": "modern",
        "author": "Roger S. Bagnall",
        "work": "Alexandria: Library of Dreams, Proceedings of the American Philosophical Society, 146, 2002",
        "locus": "p. 348 à 362"
      },
      {
        "kind": "modern",
        "author": "Duane W. Roller",
        "work": ROLLER
      }
    ]
  }
]
