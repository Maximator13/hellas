import type { HistoricalEvent } from './schema.ts'

const HERODOTE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0126'
const THUCYDIDE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0200'
const XENOPHON = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0206'
const PAUSANIAS = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0160'
const DIODORE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0084'
const PLUTARQUE = 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives'

export const events: HistoricalEvent[] = [
  {
    "id": "bataille-de-platees",
    "title": "Bataille de Platées",
    "start": -478,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée à la fin de l'été 479 ; Plutarque la place le 4 Boédromion du calendrier athénien (le 27 Panémos du calendrier béotien), date que les modernes situent en août ou en septembre.",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 1,
    "placeId": "platees",
    "people": [
      "pausanias-le-regent",
      "mardonios",
      "aristide"
    ],
    "summary": "À la fin de l'été 479, au pied du Cithéron, près de Platées, l'armée grecque coalisée commandée par le régent spartiate Pausanias écrase l'armée que Xerxès avait laissée en Grèce sous les ordres de Mardonios, tué dans la bataille. C'est la fin de l'invasion perse de la Grèce continentale.",
    "body": "**Des jours face à face.** Au printemps 479, Mardonios réoccupe Athènes, puis se replie en Béotie, pays allié des Perses. Les Grecs, Spartiates en tête, s'installent sur les pentes du Cithéron. Pendant plusieurs jours, la cavalerie perse harcèle leurs lignes et leur coupe l'eau, jusqu'à ce que Pausanias ordonne de nuit un repli qui tourne au désordre (Hérodote, IX, 49 à 57).\n\n**La bataille.** Croyant les Grecs en fuite, Mardonios attaque. Les Spartiates et les Tégéates soutiennent le choc puis enfoncent l'infanterie perse ; Mardonios est tué et le camp perse pris d'assaut. Les Athéniens d'Aristide battent de leur côté les Béotiens alliés des Perses. Les vainqueurs consacrent à Delphes un trépied d'or posé sur une colonne de bronze faite de trois serpents enlacés, gravée des noms de 31 cités ; la colonne se trouve aujourd'hui à Istanbul.\n\n**Les chiffres.** Hérodote (IX, 28 à 30) compte 38 700 hoplites grecs et 110 000 hommes en tout avec les troupes légères, face à 300 000 soldats de l'empire et environ 50 000 Grecs ralliés aux Perses (IX, 32). Les historiens modernes acceptent à peu près l'ordre de grandeur grec mais réduisent fortement l'armée perse, sans s'accorder sur un chiffre. Le même jour, selon Hérodote, la flotte grecque l'emportait à Mycale.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "IX, 19 à 89",
        "url": `${HERODOTE}:book=9:chapter=19`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Aristide",
        "locus": "11 à 21",
        "url": `${PLUTARQUE}/Aristides*.html`
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 132, 2 et 3 (l'inscription du trépied de Delphes)",
        "url": `${THUCYDIDE}:book=1:chapter=132`
      },
      {
        "kind": "modern",
        "author": "J. F. Lazenby",
        "work": "The Defence of Greece, 490-479 BC, Warminster, Aris and Phillips, 1993"
      },
      {
        "kind": "modern",
        "author": "Peter Green",
        "work": "The Greco-Persian Wars, Berkeley, University of California Press, 1996"
      }
    ]
  },
  {
    "id": "bataille-de-mycale",
    "title": "Bataille de Mycale",
    "start": -478,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Hérodote (IX, 90 et 100) place la bataille le même jour que Platées, coïncidence que beaucoup d'historiens jugent arrangée ; elle date en tout cas de la fin de l'été 479.",
    "era": "classique",
    "track": "ionie",
    "category": "war",
    "importance": 2,
    "placeId": "mycale",
    "people": [
      "leotychidas-ii",
      "xanthippe-pere-de-pericles"
    ],
    "summary": "À la fin de l'été 479, la flotte grecque du roi spartiate Léotychidas débarque au pied du mont Mycale, face à Samos, où les Perses ont tiré leurs navires à terre derrière un retranchement. Les Grecs prennent le camp et brûlent la flotte perse ; les cités d'Ionie se soulèvent à nouveau contre le Grand Roi.",
    "body": "**Une bataille navale livrée sur terre.** Appelée par des Samiens, la flotte grecque, 110 navires selon Hérodote (VIII, 131), traverse l'Égée. Les Perses renoncent à combattre sur mer : ils tirent leurs navires sur la plage du Mycale et les entourent d'une palissade, gardée par une armée de terre. Les Grecs débarquent, les Athéniens et leurs voisins emportent le retranchement, et les Ioniens enrôlés dans l'armée perse font défection pendant le combat (IX, 103 et 104).\n\n**Pourquoi c'est important.** Mycale fait passer la guerre de la défense de la Grèce à la libération des Grecs d'Asie. Les Spartiates proposent d'évacuer les Ioniens vers la Grèce ; les Athéniens refusent et les insulaires de Samos, de Chios et de Lesbos entrent dans l'alliance (IX, 106). Les Athéniens de Xanthippe, père de Périclès, vont ensuite assiéger Sestos, sur l'Hellespont, prise pendant l'hiver.\n\n**Ce qui est incertain.** Hérodote rapporte qu'une rumeur de la victoire de Platées parcourut les rangs grecs le jour même, ce qui sent la reconstruction. Les effectifs perses sont inconnus : il parle de 60 000 hommes commandés par Tigrane (IX, 96), chiffre invérifiable.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "IX, 90 à 107 et 114 à 121",
        "url": `${HERODOTE}:book=9:chapter=90`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XI, 34 à 36",
        "url": `${DIODORE}:book=11:chapter=34`
      },
      {
        "kind": "modern",
        "author": "Peter Green",
        "work": "The Greco-Persian Wars, Berkeley, University of California Press, 1996"
      }
    ]
  },
  {
    "id": "bataille-d-himere",
    "title": "Bataille d'Himère",
    "start": -479,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Hérodote (VII, 166) place la bataille le jour de Salamine, Diodore (XI, 24) le jour des Thermopyles : ces synchronismes sont sans doute symboliques, mais l'année 480 est sûre.",
    "era": "classique",
    "track": "occident",
    "category": "war",
    "importance": 2,
    "placeId": "himere",
    "people": [
      "gelon",
      "theron"
    ],
    "summary": "En 480, sous les murs d'Himère, sur la côte nord de la Sicile, Gélon de Syracuse et Théron d'Agrigente écrasent une grande armée carthaginoise commandée par Hamilcar, venue rétablir le tyran chassé de la ville. La victoire fait de Syracuse la première puissance de l'Occident grec.",
    "body": "**L'appel d'un tyran.** Chassé d'Himère par Théron d'Agrigente, le tyran Térillos appelle à l'aide Carthage, qui envoie une armée sous les ordres d'Hamilcar (Hérodote, VII, 165). Théron, assiégé dans la ville, reçoit le renfort de son gendre Gélon, maître de Syracuse.\n\n**La bataille.** Selon Diodore (XI, 21 et 22), Gélon fait entrer dans le camp naval carthaginois des cavaliers qui se font passer pour des alliés ; ils tuent Hamilcar et incendient les navires, puis l'armée grecque attaque. Le récit carthaginois rapporté par Hérodote (VII, 167) fait au contraire disparaître Hamilcar dans le feu d'un sacrifice. Carthage paie une indemnité de 2 000 talents (Diodore, XI, 26).\n\n**Les chiffres et la légende.** Hérodote et Diodore donnent 300 000 hommes à Hamilcar, chiffre que les historiens modernes jugent très exagéré. Les Grecs ont vite rapproché Himère de Salamine : une victoire des Grecs d'Occident sur les Barbares le même jour que celle de la Grèce sur les Perses, rapprochement que chante déjà Pindare. Le butin finance des temples à Syracuse et à Agrigente, et sans doute le temple de la Victoire d'Himère.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VII, 165 à 167",
        "url": `${HERODOTE}:book=7:chapter=165`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XI, 20 à 26",
        "url": `${DIODORE}:book=11:chapter=20`
      },
      {
        "kind": "ancient",
        "author": "Pindare",
        "work": "Pythiques",
        "locus": "I, v. 75 à 80"
      },
      {
        "kind": "modern",
        "author": "M. I. Finley",
        "work": "Ancient Sicily, 2e éd., Londres, Chatto and Windus, 1979"
      }
    ]
  },
  {
    "id": "fondation-de-la-ligue-de-delos",
    "title": "Fondation de la ligue de Délos",
    "start": -477,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Fondation datée de l'année athénienne 478/477 d'après la Constitution d'Athènes (23, 5) ; le premier montant du tribut, 460 talents selon Thucydide, est discuté.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 1,
    "placeId": "delos",
    "people": [
      "aristide",
      "pausanias-le-regent"
    ],
    "summary": "En 478/477, lassées de la brutalité du régent spartiate Pausanias, les cités d'Ionie et des îles confient à Athènes le commandement de la guerre contre la Perse. L'alliance, dont le trésor et les réunions sont fixés au sanctuaire d'Apollon à Délos, devient en une génération l'empire maritime athénien.",
    "body": "**Une alliance contre la Perse.** Selon Thucydide (I, 95 et 96), les alliés, irrités par la violence de Pausanias, demandent aux Athéniens de prendre la tête de la flotte ; Sparte se retire de la guerre maritime. Les alliés jurent une alliance perpétuelle, scellée selon la Constitution d'Athènes (23, 5) en jetant à la mer des masses de fer qui ne devaient jamais remonter.\n\n**Des navires ou de l'argent.** Aristide fixe la contribution de chaque cité : des navires équipés pour les plus puissantes (Samos, Chios, Lesbos), un tribut en argent, le phoros, pour les autres. Des magistrats athéniens, les hellénotames, gèrent la caisse déposée à Délos. Thucydide donne un premier total de 460 talents par an, chiffre que beaucoup d'historiens jugent trop élevé pour cette date.\n\n**D'une ligue à un empire.** Le nom « ligue de Délos » est moderne : les Grecs disaient « les Athéniens et leurs alliés ». Peu à peu, la plupart des cités préfèrent payer plutôt que fournir des navires, ce qui renforce la flotte athénienne. Naxos, qui veut quitter l'alliance vers 470, est réduite par la force, première cité alliée asservie selon Thucydide (I, 98), et le trésor est transféré à Athènes en 454.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 94 à 99",
        "url": `${THUCYDIDE}:book=1:chapter=94`
      },
      {
        "kind": "ancient",
        "author": "Aristote (école d')",
        "work": "Constitution d'Athènes",
        "locus": "23, 4 et 5"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Aristide",
        "locus": "23 à 25",
        "url": `${PLUTARQUE}/Aristides*.html`
      },
      {
        "kind": "modern",
        "author": "Russell Meiggs",
        "work": "The Athenian Empire, Oxford, Clarendon Press, 1972"
      }
    ]
  },
  {
    "id": "les-perses-d-eschyle",
    "title": "Les Perses d'Eschyle",
    "start": -471,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date donnée par l'argument antique de la pièce (archontat de Ménon, 473/472) : la représentation a eu lieu aux Grandes Dionysies du printemps 472.",
    "era": "classique",
    "track": "athenes",
    "category": "culture",
    "importance": 2,
    "placeId": "theatre-de-dionysos",
    "people": [
      "eschyle",
      "pericles"
    ],
    "summary": "Au printemps 472, aux Grandes Dionysies d'Athènes, Eschyle remporte le concours tragique avec une tétralogie dont fait partie Les Perses, qui montre la cour perse apprenant le désastre de Salamine. Le chorège qui finance le spectacle est le jeune Périclès. C'est la plus ancienne tragédie grecque conservée.",
    "body": "**Une tragédie d'actualité.** La pièce se déroule en Perse, devant la reine mère de Xerxès. Un messager raconte Salamine, l'ombre de Darius sort de son tombeau pour condamner la démesure de son fils, puis Xerxès revient vaincu. Aucun Grec n'y est nommé. Eschyle, qui avait combattu à Marathon et sans doute à Salamine, montre la victoire du point de vue des vaincus, huit ans à peine après les faits.\n\n**Un concours.** Selon l'argument antique, Eschyle gagne avec Phinée, Les Perses, Glaucos de Potnies et le drame satyrique Prométhée ; seule la deuxième pièce est conservée. La liste des vainqueurs des Dionysies gravée au IVe siècle (IG II² 2318) nomme Périclès, du dème de Cholarges, comme chorège, c'est-à-dire le riche citoyen chargé de payer le chœur. Phrynichos avait déjà mis en scène les guerres médiques, mais ses pièces sont perdues.\n\n**Le cadre et les chiffres.** Le théâtre de Dionysos, au pied de l'Acropole, n'a alors que des gradins de bois : le théâtre de pierre date du IVe siècle. Le récit du messager reste une source sur Salamine (310 navires grecs, 1 000 navires perses plus 207 rapides, v. 338 à 343), à lire comme un texte poétique.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Eschyle",
        "work": "Les Perses",
        "locus": "v. 249 à 514 (le récit du messager) et argument antique"
      },
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Fastes des Dionysies",
        "locus": "IG II² 2318"
      },
      {
        "kind": "modern",
        "author": "Edith Hall",
        "work": "Aeschylus: Persians, Warminster, Aris and Phillips, 1996"
      }
    ]
  },
  {
    "id": "ostracisme-de-themistocle",
    "title": "Ostracisme de Thémistocle",
    "start": -470,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date discutée : entre 472 et 470 selon les reconstructions ; Diodore (XI, 54 et 55) raconte l'affaire sous l'année 471/470.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "themistocle",
      "artaxerxes-ier"
    ],
    "summary": "Vers 471, le vainqueur de Salamine est banni d'Athènes pour dix ans par ostracisme. Réfugié à Argos, puis accusé d'avoir trahi la Grèce avec le régent Pausanias, il fuit à travers l'Égée et finit ses jours au service du roi des Perses, qui lui confie Magnésie du Méandre.",
    "body": "**Le vote.** L'ostracisme permet aux Athéniens d'écarter pour dix ans, sans le priver de ses biens, un citoyen jugé trop puissant : chacun grave un nom sur un tesson de poterie, l'ostrakon, et le vote n'est valable qu'avec 6 000 tessons au moins (Plutarque, Aristide, 7). Les fouilles de l'agora et du Céramique ont livré des centaines d'ostraka au nom de Thémistocle, dont un lot de près de 200, trouvé dans un puits au nord de l'Acropole et écrit par une poignée de mains : des bulletins préparés d'avance.\n\n**La fuite.** Installé à Argos, Thémistocle est mis en cause quand les Spartiates découvrent la trahison de Pausanias. Poursuivi par Athènes et Sparte, il passe par Corcyre et chez Admète, roi des Molosses, puis gagne l'Asie et écrit au nouveau roi Artaxerxès, qui lui donne les revenus de Magnésie, de Lampsaque et de Myonte (Thucydide, I, 135 à 138).\n\n**Ce qui est incertain.** La date de l'ostracisme, celle de la fuite (vers 466 à 465) et la cause de sa mort restent discutées : Thucydide dit qu'il mourut de maladie, tout en rapportant la rumeur d'un suicide par le poison. Ses restes auraient été ensevelis en secret en Attique.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 135 à 138",
        "url": `${THUCYDIDE}:book=1:chapter=135`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Thémistocle",
        "locus": "22 à 31",
        "url": `${PLUTARQUE}/Themistocles*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XI, 54 à 59",
        "url": `${DIODORE}:book=11:chapter=54`
      },
      {
        "kind": "modern",
        "author": "Mabel L. Lang",
        "work": "Ostraka, The Athenian Agora XXV, Princeton, American School of Classical Studies at Athens, 1990"
      },
      {
        "kind": "modern",
        "author": "Robert J. Lenardon",
        "work": "The Saga of Themistocles, Londres, Thames and Hudson, 1978"
      }
    ]
  },
  {
    "id": "premiere-victoire-de-sophocle",
    "title": "Première victoire de Sophocle",
    "start": -467,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date fixée par Plutarque et le Marbre de Paros (archontat d'Apsèphion, 469/468) : la victoire a lieu aux Dionysies du printemps 468.",
    "era": "classique",
    "track": "athenes",
    "category": "culture",
    "importance": 3,
    "placeId": "theatre-de-dionysos",
    "people": [
      "sophocle",
      "eschyle",
      "cimon"
    ],
    "summary": "Au printemps 468, Sophocle, âgé d'environ 28 ans, remporte sa première victoire au concours tragique des Dionysies, devant Eschyle. Selon Plutarque, l'archonte avait confié le jugement à Cimon et à ses collègues stratèges. Sophocle restera le plus couronné des tragiques athéniens, avec 18 à 24 victoires selon les sources.",
    "body": "**Un concours disputé.** Plutarque (Cimon, 8) raconte que la rivalité des spectateurs était si vive que l'archonte Apsèphion, au lieu de tirer au sort les juges, fit prêter serment aux dix stratèges, Cimon en tête, rentrés de campagne, et leur confia la décision. Le Marbre de Paros, chronique gravée au IIIe siècle, date la victoire de la même année et donne à Sophocle 28 ans.\n\n**Une longue carrière.** Sophocle aurait écrit plus de 120 pièces et remporté 18 victoires aux Dionysies selon Diodore (XIII, 103), 20 ou 24 selon d'autres sources ; il n'aurait jamais été classé dernier. Sept tragédies sont conservées, dont Antigone et Œdipe roi. Il exerce aussi des charges publiques : hellénotame en 443/442, stratège avec Périclès pendant la guerre de Samos.\n\n**Ce qui est incertain.** Les pièces de 468 ne sont pas connues avec certitude (peut-être Triptolème). L'anecdote d'Eschyle quittant Athènes pour la Sicile, blessé par cette défaite, vient de Plutarque et tient sans doute de la légende.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cimon",
        "locus": "8, 7 à 9",
        "url": `${PLUTARQUE}/Cimon*.html`
      },
      {
        "kind": "ancient",
        "author": "Marbre de Paros",
        "work": "Chronique de Paros",
        "locus": "A 56"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIII, 103, 4",
        "url": `${DIODORE}:book=13:chapter=103`
      },
      {
        "kind": "modern",
        "author": "Jacques Jouanna",
        "work": "Sophocle, Paris, Fayard, 2007"
      }
    ]
  },
  {
    "id": "bataille-de-l-eurymedon",
    "title": "Bataille de l'Eurymédon",
    "start": -465,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille attestée ; l'année est discutée, entre 469 et 466 selon les reconstructions, car Thucydide ne la date pas précisément.",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "eurymedon",
    "people": [
      "cimon"
    ],
    "summary": "Vers 466, à l'embouchure de l'Eurymédon, en Pamphylie, la flotte de la ligue de Délos commandée par Cimon détruit une flotte perse et phénicienne, puis bat le même jour l'armée perse sur la rive. Cette double victoire éloigne pour longtemps la menace perse de l'Égée.",
    "body": "**Une campagne en Asie Mineure.** Cimon part de Cnide avec 200 trières athéniennes et alliées, rallie à la ligue des cités de Carie et de Lycie, puis rencontre les forces perses rassemblées en Pamphylie (Plutarque, Cimon, 12). Thucydide (I, 100) résume : victoire sur terre et sur mer le même jour, et jusqu'à 200 trières phéniciennes prises ou détruites.\n\n**Pourquoi c'est important.** L'Eurymédon est la plus grande victoire de la ligue de Délos sur la Perse. Elle met fin pour une génération aux expéditions perses vers l'Égée et renforce Cimon, maître de la politique athénienne jusqu'à son ostracisme en 461. Mais, la menace écartée, des alliés comme Thasos, révoltée vers 465, se demandent à quoi sert encore la ligue.\n\n**Ce qui est incertain.** Plutarque cite des chiffres divergents pour la flotte perse (600 navires selon Phanodémos, 350 selon Éphore) et ajoute une seconde victoire, sur 80 navires phéniciens arrivés trop tard. L'emplacement exact de la bataille et sa date restent discutés.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 100, 1",
        "url": `${THUCYDIDE}:book=1:chapter=100`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cimon",
        "locus": "12 et 13",
        "url": `${PLUTARQUE}/Cimon*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XI, 60 à 62",
        "url": `${DIODORE}:book=11:chapter=60`
      },
      {
        "kind": "modern",
        "author": "Russell Meiggs",
        "work": "The Athenian Empire, Oxford, Clarendon Press, 1972"
      }
    ]
  },
  {
    "id": "seisme-de-sparte-et-revolte-des-hilotes",
    "title": "Séisme de Sparte et révolte des hilotes",
    "start": -463,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Plutarque date le séisme de la quatrième année du roi Archidamos, soit vers 464 ; Diodore le place en 469/468. La durée de la révolte (de quatre à dix ans) dépend d'un passage de Thucydide (I, 103) au texte discuté.",
    "era": "classique",
    "track": "sparte",
    "category": "nature",
    "importance": 2,
    "placeId": "sparte",
    "people": [
      "archidamos-ii",
      "cimon"
    ],
    "summary": "Vers 464, un violent séisme ravage Sparte. Les hilotes, surtout ceux de Messénie, en profitent pour se soulever et se retranchent sur le mont Ithôme. Sparte appelle ses alliés, dont Athènes, puis renvoie le contingent athénien de Cimon : cet affront rompt l'entente née des guerres médiques.",
    "body": "**Le séisme.** Selon Plutarque (Cimon, 16), la ville est presque entièrement détruite et seules cinq maisons restent debout ; Diodore (XI, 63) compte plus de 20 000 morts chez les Lacédémoniens, chiffre sans doute exagéré. Le jeune roi Archidamos II fait sonner l'alarme et rassemble les citoyens en armes, ce qui empêche les hilotes de surprendre la ville.\n\n**La révolte.** Les hilotes, dépendants qui cultivent les terres des Spartiates, se soulèvent avec deux communautés de périèques. Retranchés sur l'Ithôme, en Messénie, ils résistent plusieurs années. Sparte appelle les Athéniens, réputés habiles aux sièges ; Cimon vient avec 4 000 hoplites selon Aristophane (Lysistrata, v. 1137 à 1144), mais les Spartiates, inquiets de leur esprit, les renvoient, seuls parmi les alliés (Thucydide, I, 102). Athènes rompt alors l'alliance et se tourne vers Argos et la Thessalie.\n\n**L'issue.** Les assiégés finissent par capituler contre la vie sauve et quittent le Péloponnèse ; les Athéniens les installent à Naupacte, sur le golfe de Corinthe (Thucydide, I, 103). La crainte d'une nouvelle révolte des hilotes pèse ensuite sur toute la politique spartiate.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 101 à 103",
        "url": `${THUCYDIDE}:book=1:chapter=101`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cimon",
        "locus": "16 et 17",
        "url": `${PLUTARQUE}/Cimon*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XI, 63 et 64",
        "url": `${DIODORE}:book=11:chapter=63`
      },
      {
        "kind": "ancient",
        "author": "Aristophane",
        "work": "Lysistrata",
        "locus": "v. 1137 à 1144"
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Sparta and Lakonia: A Regional History, 1300-362 BC, 2e éd., Londres, Routledge, 2002"
      }
    ]
  },
  {
    "id": "reformes-d-ephialte",
    "title": "Réformes d'Éphialte",
    "start": -461,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Réforme datée de l'archontat de Conon (462/461) par la Constitution d'Athènes (25, 2) ; la nature exacte des pouvoirs retirés à l'Aréopage reste discutée.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "ephialte-d-athenes",
      "pericles",
      "cimon"
    ],
    "summary": "En 462/461, pendant que Cimon est parti aider Sparte, Éphialte fait voter le transfert des pouvoirs politiques de l'Aréopage, le conseil des anciens archontes, au Conseil des Cinq-Cents, à l'Assemblée et aux tribunaux populaires. Éphialte est assassiné peu après ; la démocratie athénienne prend sa forme classique.",
    "body": "**L'Aréopage dépouillé.** L'Aréopage, composé des anciens archontes nommés à vie, surveillait les magistrats et le respect des lois. Selon la Constitution d'Athènes (25, 2), Éphialte lui retire les pouvoirs « ajoutés » qui faisaient de lui le gardien de la cité, et les donne au Conseil, à l'Assemblée et aux tribunaux ; l'Aréopage ne garde que le jugement des meurtres et quelques affaires religieuses. Le retour de Cimon, renvoyé par Sparte, puis son ostracisme en 461 laissent le champ libre aux réformateurs.\n\n**Un meurtre politique.** Éphialte est assassiné peu après, par un certain Aristodicos de Tanagra selon la Constitution d'Athènes (25, 4) : c'est l'un des rares meurtres politiques connus dans l'Athènes démocratique. Son allié Périclès prend la tête du parti populaire et fait instituer une indemnité pour les juges des tribunaux (27, 3), qui permet aux pauvres de siéger.\n\n**Ce qui est incertain.** Les sources sont tardives et peu précises : on ignore la liste exacte des pouvoirs transférés. Les Euménides d'Eschyle (458), qui font de l'Aréopage un tribunal fondé par Athéna pour juger le meurtre, sont souvent lues comme un écho de la réforme, sans qu'on sache si Eschyle l'approuve.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Aristote (école d')",
        "work": "Constitution d'Athènes",
        "locus": "25 et 27, 3 et 4"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cimon",
        "locus": "15",
        "url": `${PLUTARQUE}/Cimon*.html`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Périclès",
        "locus": "7, 8 et 9, 5",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "modern",
        "author": "Peter J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "temple-de-zeus-a-olympie",
    "title": "Temple de Zeus à Olympie",
    "start": -469,
    "end": -456,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Début des travaux vers 470, d'après le style des sculptures ; le temple est achevé ou presque vers 457, quand les Spartiates y suspendent un bouclier d'or pour leur victoire de Tanagra.",
    "era": "classique",
    "track": "monde-grec",
    "category": "building",
    "importance": 2,
    "placeId": "olympie",
    "people": [
      "libon"
    ],
    "summary": "De 470 à 457 environ, les Éléens élèvent à Olympie un grand temple dorique de Zeus, œuvre de l'architecte Libon d'Élis, financé selon Pausanias par le butin d'une victoire sur Pisa. Ses frontons et ses métopes sont le chef-d'œuvre du style sévère ; il abritera la statue d'or et d'ivoire de Zeus par Phidias.",
    "body": "**Le temple.** Pausanias (V, 10, 2 et 3) décrit un temple dorique bâti en pierre locale, dont l'architecte est Libon, un Éléen ; long d'environ 64 mètres, il est alors le plus grand temple du Péloponnèse. Les Spartiates et leurs alliés y consacrent un bouclier d'or après leur victoire sur les Athéniens à Tanagra (457), avec une dédicace que Pausanias recopie (V, 10, 4) : le temple était donc achevé ou presque.\n\n**Le décor.** Le fronton est montre les préparatifs de la course de chars entre Pélops et Œnomaos, mythe fondateur du sanctuaire ; le fronton ouest, le combat des Lapithes et des Centaures autour d'Apollon ; les douze métopes, les travaux d'Héraclès. Ces sculptures, conservées au musée d'Olympie, sont le principal ensemble du style dit « sévère », entre l'art archaïque et le classicisme du Parthénon.\n\n**La suite.** Une génération plus tard, Phidias y installe la statue de Zeus, comptée parmi les sept merveilles du monde. Le temple est renversé par des séismes au VIe siècle de notre ère ; ses tambours de colonnes gisent encore au sol.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "V, 10, 2 à 10",
        "url": `${PAUSANIAS}:book=5:chapter=10`
      },
      {
        "kind": "modern",
        "author": "Alfred Mallwitz",
        "work": "Olympia und seine Bauten, Munich, Prestel, 1972"
      },
      {
        "kind": "modern",
        "author": "Judith M. Barringer",
        "work": "Olympia: A Cultural History, Princeton, Princeton University Press, 2021"
      }
    ]
  },
  {
    "id": "longs-murs",
    "title": "Construction des Longs Murs",
    "start": -457,
    "end": -456,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Travaux commencés vers 458 et achevés vers 457/456 d'après l'ordre du récit de Thucydide (I, 107, 1 et 108, 3) ; ces années sont reconstruites. Le mur intermédiaire, ajouté vers 445, est daté de façon plus vague.",
    "era": "classique",
    "track": "athenes",
    "category": "building",
    "importance": 2,
    "placeId": "longs-murs",
    "people": [
      "cimon",
      "pericles"
    ],
    "summary": "Vers 458 à 457, Athènes relie la ville à ses ports par deux longues murailles, l'une vers Phalère, l'autre vers le Pirée, longues de 6 à 7 kilomètres. Avec ce couloir fortifié, la cité devient une île : tant qu'elle domine la mer, aucune armée de terre ne peut l'affamer.",
    "body": "**Une ville reliée à la mer.** Thémistocle avait déjà fortifié le Pirée. En pleine guerre contre Corinthe, Égine et bientôt Sparte, les Athéniens construisent les Longs Murs (Thucydide, I, 107, 1), achevés peu après les batailles de Tanagra et d'Œnophyta en 457 (I, 108, 3). Thucydide (II, 13, 7) donne 35 stades au mur de Phalère et 40 à celui du Pirée. Plutarque (Cimon, 13) dit que Cimon avait payé les fondations dans les terrains marécageux. Vers 445, Périclès fait ajouter un mur intermédiaire, parallèle au mur du Pirée (Platon, Gorgias, 455e).\n\n**La stratégie de Périclès.** Pendant la guerre du Péloponnèse, les habitants de l'Attique se réfugient entre les murs pendant que l'ennemi ravage les campagnes, et la ville vit des importations par mer. Cette foule entassée favorise la propagation de l'épidémie de 430.\n\n**La fin.** À la capitulation de 404, Sparte exige la destruction des Longs Murs, abattus au son des flûtes (Xénophon, Helléniques, II, 2, 23). Conon les fait relever en 394 avec de l'argent perse. Des tronçons de fondations ont été repérés entre Athènes et le Pirée.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 107, 1 ; I, 108, 3 ; II, 13, 7",
        "url": `${THUCYDIDE}:book=1:chapter=107`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cimon",
        "locus": "13, 7",
        "url": `${PLUTARQUE}/Cimon*.html`
      },
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "II, 2, 20 à 23",
        "url": `${XENOPHON}:book=2:chapter=2`
      },
      {
        "kind": "modern",
        "author": "David H. Conwell",
        "work": "Connecting a City to the Sea: The History of the Athenian Long Walls, Leyde, Brill, 2008"
      }
    ]
  },
  {
    "id": "expedition-d-egypte",
    "title": "Expédition athénienne en Égypte",
    "start": -459,
    "end": -453,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Thucydide (I, 110) donne six ans de guerre ; la chronologie la plus courante va de 460/459 à 454. L'ampleur des pertes athéniennes est discutée.",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "memphis",
    "people": [
      "inaros",
      "megabyze",
      "artaxerxes-ier"
    ],
    "summary": "Vers 460, Athènes détourne vers l'Égypte une flotte de 200 navires pour soutenir Inaros, prince libyen révolté contre Artaxerxès Ier. Après six ans de guerre, les Grecs, assiégés dans l'île de Prosopitis, dans le delta du Nil, sont écrasés par le général perse Mégabyze vers 454 : c'est l'un des pires désastres d'Athènes au Ve siècle.",
    "body": "**Une guerre lointaine.** Selon Thucydide (I, 104), la flotte athénienne et alliée qui opérait à Chypre remonte le Nil, prend les deux tiers de Memphis et assiège la garnison perse dans la « Muraille blanche ». Une stèle portant les morts d'une seule tribu athénienne pour une année, vers 460 ou 459 (IG I³ 1147), énumère les champs de bataille de Chypre, d'Égypte, de Phénicie, d'Halieis, d'Égine et de Mégare : Athènes se bat alors sur tous les fronts.\n\n**Le désastre.** Le Grand Roi envoie Mégabyze, qui chasse les Grecs de Memphis et les enferme dans l'île de Prosopitis ; au bout de dix-huit mois, il détourne l'eau du canal et prend l'île à pied sec (I, 109). Une escadre de secours de 50 trières, qui ignore tout, est détruite à la bouche mendésienne du Nil (I, 110). Inaros, livré par trahison, est crucifié.\n\n**Ce qui est incertain.** Thucydide dit que peu de Grecs survécurent ; si les 200 navires furent tous perdus, Athènes aurait perdu des dizaines de milliers d'hommes. Ctésias ne parle que de 40 navires, et beaucoup d'historiens pensent qu'une partie de la flotte était rentrée avant la fin. Le désastre explique sans doute le transfert du trésor de la ligue à Athènes en 454.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 104 et 109 à 110",
        "url": `${THUCYDIDE}:book=1:chapter=104`
      },
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Liste des morts de la tribu Érechthéis",
        "locus": "IG I³ 1147"
      },
      {
        "kind": "ancient",
        "author": "Ctésias",
        "work": "Persika",
        "locus": "FGrHist 688 F 14"
      },
      {
        "kind": "modern",
        "author": "Russell Meiggs",
        "work": "The Athenian Empire, Oxford, Clarendon Press, 1972"
      }
    ]
  },
  {
    "id": "transfert-du-tresor-de-la-ligue",
    "title": "Le trésor de la ligue transféré à Athènes",
    "start": -453,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "La date de 454/453 vient de la première des listes, gravées à Athènes, des prémices du tribut offertes à Athéna (IG I³ 259) ; aucune source contemporaine ne donne le motif du transfert.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "pericles"
    ],
    "summary": "En 454/453, le trésor de la ligue de Délos est transféré de l'île à Athènes. Dès lors, un soixantième du tribut versé par les alliés est offert chaque année à Athéna, et ces offrandes sont gravées sur de grandes stèles de l'Acropole. Le transfert marque le passage d'une alliance à un empire, et l'argent des alliés financera en partie les monuments de Périclès.",
    "body": "**Les listes du tribut.** Les « listes des prémices » (IG I³ 259 et suivantes), dont la première est gravée sur un bloc de marbre de plus de 3,5 mètres de haut, recensent chaque année la part d'Athéna, un soixantième du tribut, cité par cité. La première liste date de 454/453 : c'est la preuve la plus solide que la caisse se trouve désormais à Athènes. Ces listes permettent de suivre les versements de plus de 150 cités.\n\n**Pourquoi Athènes ?** Aucune source contemporaine ne le dit. On rapproche souvent le transfert du désastre d'Égypte, qui pouvait faire craindre une offensive perse dans l'Égée. Plutarque (Aristide, 25) attribue la proposition aux Samiens, d'après Théophraste ; ailleurs (Périclès, 12), il rapporte que les adversaires de Périclès l'accusaient d'avoir pris ce trésor commun pour embellir la ville.\n\n**Pourquoi c'est important.** Placé sous la garde d'Athéna, le trésor devient en pratique un instrument athénien : il finance la flotte, mais aussi une partie des chantiers de l'Acropole. Les alliés qui tentent de quitter la ligue sont désormais traités en sujets révoltés.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Listes des prémices du tribut",
        "locus": "IG I³ 259 à 290"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Périclès",
        "locus": "12",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Aristide",
        "locus": "25, 3",
        "url": `${PLUTARQUE}/Aristides*.html`
      },
      {
        "kind": "modern",
        "author": "Benjamin D. Meritt, H. T. Wade-Gery et Malcolm F. McGregor",
        "work": "The Athenian Tribute Lists, 4 vol., Cambridge (Mass.) et Princeton, 1939 à 1953"
      },
      {
        "kind": "modern",
        "author": "Russell Meiggs",
        "work": "The Athenian Empire, Oxford, Clarendon Press, 1972"
      }
    ]
  },
  {
    "id": "loi-de-pericles-sur-la-citoyennete",
    "title": "Loi de Périclès sur la citoyenneté",
    "start": -450,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Loi datée de l'archontat d'Antidotos (451/450) par la Constitution d'Athènes (26, 4).",
    "era": "classique",
    "track": "athenes",
    "category": "society",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "pericles"
    ],
    "summary": "En 451/450, sur proposition de Périclès, les Athéniens décident que ne sera citoyen que l'enfant né d'un père et d'une mère tous deux athéniens. La loi ferme le corps civique au moment où la citoyenneté donne accès à des avantages croissants, et exclut les enfants des mariages avec des étrangères, jusque-là courants dans l'élite.",
    "body": "**La loi.** La Constitution d'Athènes (26, 4) l'explique par le grand nombre des citoyens. Avant elle, un fils de père athénien et de mère étrangère pouvait être citoyen : c'était le cas de Cimon, fils d'une princesse thrace, ou de Clisthène, petit-fils par sa mère d'un tyran de Sicyone. Désormais, les enfants d'une étrangère sont des bâtards (nothoi), exclus de la citoyenneté.\n\n**Une loi contre son auteur.** Périclès vit ensuite avec Aspasie, une Milésienne. Selon Plutarque (Périclès, 37), après la mort de ses deux fils légitimes pendant l'épidémie, il obtient du peuple, par exception, que le fils qu'il a eu d'Aspasie soit inscrit comme citoyen : c'est Périclès le Jeune, l'un des stratèges exécutés après les Arginuses en 406.\n\n**Ce qui est incertain.** Les motifs de la loi sont discutés : réserver aux citoyens les distributions et les indemnités, limiter les alliances des grandes familles avec l'étranger, ou fixer le statut des femmes athéniennes. Plutarque rapporte aussi qu'en 445/444, lors d'une distribution de blé offert par un roi d'Égypte, près de 5 000 personnes furent rayées des listes de citoyens, chiffre discuté.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Aristote (école d')",
        "work": "Constitution d'Athènes",
        "locus": "26, 4"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Périclès",
        "locus": "37, 2 à 5",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "modern",
        "author": "Josine Blok",
        "work": "Citizenship in Classical Athens, Cambridge, Cambridge University Press, 2017"
      },
      {
        "kind": "modern",
        "author": "Peter J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "paix-de-callias",
    "title": "Paix de Callias",
    "start": -448,
    "precision": "year",
    "certainty": "debated",
    "certaintyNote": "Existence débattue : Thucydide n'en dit rien, et l'historien Théopompe, au IVe siècle, tenait pour un faux la stèle exposée à Athènes ; Diodore la place en 449/448, Plutarque après l'Eurymédon.",
    "era": "classique",
    "track": "perse",
    "category": "politics",
    "importance": 2,
    "placeId": "suse",
    "people": [
      "callias-fils-d-hipponicos",
      "artaxerxes-ier",
      "cimon"
    ],
    "summary": "Vers 449, après une dernière campagne de Cimon à Chypre, l'Athénien Callias aurait conclu avec Artaxerxès Ier une paix interdisant à la flotte et aux armées perses d'approcher de l'Égée, en échange de la fin des opérations athéniennes contre le roi. Les orateurs du IVe siècle en font une gloire d'Athènes ; son existence même est discutée.",
    "body": "**Les clauses rapportées.** Selon Diodore (XII, 4), les cités grecques d'Asie restaient autonomes, les satrapes ne devaient pas approcher à moins de trois jours de marche de la mer, et aucun navire de guerre perse ne devait naviguer entre Phasélis et les roches Cyanées, à l'entrée du Pont-Euxin ; Athènes renonçait de son côté à attaquer le territoire du roi. Les combats cessent bien vers cette date, après la mort de Cimon devant Kition, à Chypre, vers 450.\n\n**Une paix contestée.** Thucydide, qui résume la période, ne mentionne aucun traité. Hérodote (VII, 151) signale seulement que Callias, fils d'Hipponicos, se trouvait à Suse pour une ambassade. Au IVe siècle, Isocrate et Démosthène invoquent la paix, mais Théopompe la juge fausse parce que la stèle était gravée en lettres ioniennes, adoptées officiellement à Athènes en 403 seulement.\n\n**Ce que pensent les modernes.** Certains y voient un vrai traité, d'autres un accord tacite ou une invention patriotique. L'argument de Théopompe ne prouve pas grand-chose : la stèle pouvait être une copie refaite plus tard. Le débat reste ouvert.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XII, 4, 4 à 6",
        "url": `${DIODORE}:book=12:chapter=4`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Cimon",
        "locus": "13, 4 et 5",
        "url": `${PLUTARQUE}/Cimon*.html`
      },
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "VII, 151",
        "url": `${HERODOTE}:book=7:chapter=151`
      },
      {
        "kind": "ancient",
        "author": "Théopompe",
        "work": "Philippiques",
        "locus": "FGrHist 115 F 153 et 154"
      },
      {
        "kind": "modern",
        "author": "Ernst Badian",
        "work": "The Peace of Callias, Journal of Hellenic Studies, 107, 1987",
        "locus": "p. 1 à 39"
      }
    ]
  },
  {
    "id": "paix-de-trente-ans",
    "title": "Paix de Trente Ans entre Athènes et Sparte",
    "start": -445,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Traité conclu pendant l'hiver 446/445 ; Thucydide le date indirectement, puisque la guerre de 431 éclate dans sa quinzième année (II, 2, 1).",
    "era": "classique",
    "track": "sparte",
    "category": "politics",
    "importance": 2,
    "placeId": "sparte",
    "people": [
      "pericles",
      "pleistoanax"
    ],
    "summary": "Pendant l'hiver 446/445, Athènes et Sparte concluent une paix de trente ans. Après la défaite de Coronée et la révolte de l'Eubée et de Mégare, Athènes renonce à ses conquêtes dans le Péloponnèse ; chacun reconnaît l'alliance de l'autre. Le traité prévoit de régler les différends par un arbitrage.",
    "body": "**Une crise athénienne.** En 447/446, les Athéniens sont battus à Coronée par les Béotiens et perdent la Béotie ; l'Eubée et Mégare se révoltent, et le roi spartiate Pleistoanax envahit l'Attique. Il se retire sans combattre, acheté selon la rumeur par Périclès, et sera exilé pour cela (Thucydide, I, 113 et 114 ; II, 21 ; Plutarque, Périclès, 22). Périclès reprend ensuite l'Eubée.\n\n**Le traité.** Athènes rend Nisaia, Pégai, Trézène et l'Achaïe (Thucydide, I, 115). Chaque camp garde ses alliés, les cités neutres peuvent rejoindre l'un ou l'autre, et les différends doivent être soumis à un arbitrage, clause que les Athéniens invoqueront en vain en 432 (I, 78 et 140). Pausanias (V, 23, 4) vit à Olympie la stèle de bronze où le traité était gravé.\n\n**Pourquoi c'est important.** La paix reconnaît deux blocs, la ligue du Péloponnèse sur terre et l'empire athénien sur mer. Elle tient quatorze ans : la guerre du Péloponnèse éclate en 431, dans sa quinzième année.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 113 à 115 ; II, 2, 1",
        "url": `${THUCYDIDE}:book=1:chapter=113`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XII, 7",
        "url": `${DIODORE}:book=12:chapter=7`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "V, 23, 4",
        "url": `${PAUSANIAS}:book=5:chapter=23`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Outbreak of the Peloponnesian War, Ithaca, Cornell University Press, 1969"
      }
    ]
  },
  {
    "id": "fondation-de-thourioi",
    "title": "Fondation de Thourioi",
    "start": -443,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Diodore (XII, 10) raconte la fondation sous l'année 446/445 ; la date de 444/443, la plus souvent retenue, s'appuie sur Denys d'Halicarnasse (Lysias, 1), qui y fait partir le jeune Lysias sous l'archonte Praxitèlès.",
    "era": "classique",
    "track": "occident",
    "category": "society",
    "importance": 3,
    "placeId": "thourioi",
    "people": [
      "herodote"
    ],
    "summary": "En 444/443, à l'initiative d'Athènes, des colons venus de toute la Grèce fondent Thourioi, en Italie du Sud, près des ruines de Sybaris. Cette colonie panhellénique attire l'historien Hérodote, qui en devient citoyen, et le sophiste Protagoras, chargé selon la tradition de rédiger ses lois.",
    "body": "**Une colonie de toute la Grèce.** Les survivants de Sybaris, détruite par Crotone en 510, demandent de l'aide à la Grèce. Athènes envoie dix navires sous la conduite de Lampon et de Xénocritos et invite les volontaires de toutes les cités (Diodore, XII, 10). La ville est fondée près d'une source appelée Thouria ; ses citoyens sont répartis en dix tribus selon leur origine, arcadienne, béotienne, ionienne, athénienne et d'autres encore (XII, 11).\n\n**Des intellectuels.** Hérodote est parfois dit « de Thourioi » : Aristote cite ainsi la première phrase des Histoires (Rhétorique, III, 9). Selon Diogène Laërce (IX, 50), Protagoras d'Abdère rédigea les lois de la cité, et le jeune Lysias, futur orateur, s'y installe pour plusieurs années. Une tradition plus tardive attribue le plan de la ville à Hippodamos de Milet.\n\n**Une colonie qui échappe à Athènes.** Les colons se divisent vite. Vers 434, l'oracle de Delphes déclare Apollon seul fondateur de la ville (Diodore, XII, 35) : Thourioi refuse de se dire colonie athénienne, et ses navires combattent aux côtés de Sparte après le désastre de Sicile (Thucydide, VIII, 35).",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XII, 10, 11 et 35",
        "url": `${DIODORE}:book=12:chapter=10`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VI, 1, 13"
      },
      {
        "kind": "ancient",
        "author": "Diogène Laërce",
        "work": "Vies et doctrines des philosophes illustres",
        "locus": "IX, 50"
      },
      {
        "kind": "modern",
        "author": "Mogens Herman Hansen et Thomas Heine Nielsen (dir.)",
        "work": "An Inventory of Archaic and Classical Poleis, Oxford, Oxford University Press, 2004"
      }
    ]
  },
  {
    "id": "revolte-de-samos",
    "title": "Révolte de Samos",
    "start": -439,
    "end": -438,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Guerre placée par Thucydide (I, 115) dans la sixième année de la paix de Trente Ans ; elle s'étend du printemps 440 au printemps 439 environ.",
    "era": "classique",
    "track": "ionie",
    "category": "war",
    "importance": 2,
    "placeId": "samos",
    "people": [
      "pericles",
      "sophocle"
    ],
    "summary": "En 440, Samos, l'un des derniers alliés à fournir encore des navires, entre en guerre contre Milet, puis se révolte contre Athènes, qui lui avait imposé une démocratie. Périclès mène en personne un siège de neuf mois. Samos capitule en 439 : elle livre sa flotte, rase ses murs et paie une lourde indemnité.",
    "body": "**L'origine.** Samos et Milet se disputent Priène. Milet, vaincue, se plaint à Athènes, qui intervient, installe une démocratie à Samos et prend des otages (Thucydide, I, 115). Des oligarques samiens, aidés par Pissouthnès, satrape perse de Sardes, reprennent l'île, et Byzance se joint à la révolte.\n\n**Le siège.** Périclès bat la flotte samienne, puis, renforcé par des navires venus d'Athènes, de Chios et de Lesbos, assiège la ville pendant neuf mois (I, 116 et 117). Sophocle, alors stratège, participe à la campagne. Au retour, Périclès prononce l'éloge funèbre des morts, dont Plutarque (Périclès, 28) cite une formule restée célèbre.\n\n**Ce que coûte la guerre.** Une inscription (IG I³ 363) enregistre les sommes avancées par le trésor d'Athéna pour cette guerre et pour celle de Byzance, environ 1 400 talents d'après la restitution du texte. La révolte montre que même un allié puissant ne peut quitter la ligue. Le récit d'atrocités athéniennes contre les prisonniers, transmis par l'historien Douris de Samos, est jugé suspect par Plutarque lui-même.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 115 à 117",
        "url": `${THUCYDIDE}:book=1:chapter=115`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Périclès",
        "locus": "24 à 28",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Dépenses de la guerre de Samos",
        "locus": "IG I³ 363"
      },
      {
        "kind": "modern",
        "author": "Graham Shipley",
        "work": "A History of Samos, 800-188 BC, Oxford, Clarendon Press, 1987"
      }
    ]
  },
  {
    "id": "zeus-d-olympie-de-phidias",
    "title": "Le Zeus d'Olympie de Phidias",
    "start": -434,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Date discutée : la plupart des archéologues placent la statue après l'Athéna Parthénos (438), d'après le matériel de l'atelier de Phidias, vers 435 à 430 ; d'autres la font remonter aux années 450.",
    "era": "classique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "olympie",
    "people": [
      "phidias"
    ],
    "summary": "Vers 435 à 430, Phidias réalise pour le temple d'Olympie une statue colossale de Zeus assis, en or et en ivoire, haute d'environ 12 mètres. Rangée parmi les sept merveilles du monde, elle est connue par la description de Pausanias, des monnaies d'Élis et la fouille de l'atelier où elle fut fabriquée.",
    "body": "**La statue.** Pausanias (V, 11) la décrit en détail : Zeus trône, une Victoire dans la main droite, un sceptre surmonté d'un aigle dans la gauche, sur un trône d'ébène, d'ivoire, d'or et de pierres précieuses orné de mythes. Le corps est en ivoire sur une armature de bois, le manteau en or. Strabon (VIII, 3, 30) remarque que si le dieu se levait, il crèverait le toit.\n\n**L'atelier.** Les archéologues allemands ont fouillé à Olympie, dans les années 1950, l'atelier de Phidias, bâti aux dimensions de la salle du temple. On y a trouvé des moules de terre cuite pour les draperies, des éclats d'ivoire, des outils et une petite cruche inscrite « je suis à Phidias ». La céramique de l'atelier date surtout des années 430.\n\n**Ce qui est incertain.** La date de l'œuvre dépend de la fin de Phidias, dont les récits se contredisent : Plutarque (Périclès, 31) le fait mourir en prison à Athènes après un procès pour détournement, Philochore le fait partir à Élis après 438. La statue fut plus tard emportée à Constantinople, où elle périt dans un incendie, sans doute au Ve siècle de notre ère.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "V, 11",
        "url": `${PAUSANIAS}:book=5:chapter=11`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "VIII, 3, 30"
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
        "locus": "31",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "modern",
        "author": "Alfred Mallwitz et Wolfgang Schiering",
        "work": "Die Werkstatt des Pheidias in Olympia, Olympische Forschungen V, Berlin, De Gruyter, 1964"
      },
      {
        "kind": "modern",
        "author": "Judith M. Barringer",
        "work": "Olympia: A Cultural History, Princeton, Princeton University Press, 2021"
      }
    ]
  },
  {
    "id": "bataille-des-sybota",
    "title": "Bataille des îles Sybota",
    "start": -432,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille de l'été 433, datée par le récit de Thucydide et par une inscription des dépenses athéniennes pour les escadres envoyées à Corcyre (IG I³ 364).",
    "era": "classique",
    "track": "corinthe",
    "category": "war",
    "importance": 3,
    "placeId": "sybota",
    "summary": "En 433, près des îles Sybota, face à Corcyre, la flotte de Corinthe affronte celle de Corcyre, soutenue par une petite escadre athénienne. Les Corinthiens ont l'avantage, mais l'arrivée de vingt trières athéniennes les fait renoncer. Thucydide fait de cette intervention l'un des griefs qui mènent à la guerre du Péloponnèse.",
    "body": "**Une querelle entre une métropole et sa colonie.** Corcyre et sa métropole Corinthe se disputent Épidamne, sur la côte illyrienne. Battue en 435 à Leucimme, Corinthe arme une grande flotte ; Corcyre, neutre jusque-là, demande l'alliance d'Athènes. Les Athéniens, après deux assemblées, concluent une alliance seulement défensive et envoient dix navires (Thucydide, I, 24 à 45).\n\n**La bataille.** Selon Thucydide (I, 46 à 54), 150 navires corinthiens et alliés affrontent 110 navires corcyréens. Le combat, à l'ancienne, se mène de pont à pont avec beaucoup d'hoplites embarqués. Les Corinthiens l'emportent à une aile et les Athéniens commencent à se battre, quand vingt trières athéniennes apparaissent ; les Corinthiens se retirent, et les deux camps dressent un trophée.\n\n**Pourquoi c'est important.** Corinthe accuse Athènes d'avoir rompu la paix de Trente Ans et pousse Sparte à la guerre. Avec Potidée et le décret contre Mégare, l'affaire de Corcyre forme les griefs immédiats que Thucydide distingue de la cause profonde, la crainte suscitée par la puissance athénienne (I, 23).",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "I, 24 à 55",
        "url": `${THUCYDIDE}:book=1:chapter=24`
      },
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Comptes des trésoriers d'Athéna pour les escadres de Corcyre",
        "locus": "IG I³ 364"
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Outbreak of the Peloponnesian War, Ithaca, Cornell University Press, 1969"
      }
    ]
  },
  {
    "id": "peste-d-athenes",
    "title": "L'épidémie d'Athènes",
    "start": -429,
    "end": -425,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Épidémie attestée par Thucydide, qui en fut atteint ; sa nature reste inconnue. La part de la population emportée, peut-être un quart à un tiers, est une estimation moderne.",
    "era": "classique",
    "track": "athenes",
    "category": "nature",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "pericles",
      "thucydide"
    ],
    "summary": "Au début de l'été 430, une épidémie venue d'Éthiopie et d'Égypte selon Thucydide frappe le Pirée, puis Athènes, où la population de l'Attique s'entasse derrière les murs. Revenue en 427/426, elle emporte peut-être un quart à un tiers des habitants, dont Périclès. Thucydide, qui l'a contractée, en laisse une description célèbre.",
    "body": "**Le récit de Thucydide.** L'historien décrit les symptômes (fièvre, rougeurs, ulcères, soif inextinguible, diarrhée) pour qu'on puisse reconnaître la maladie si elle revenait (II, 48 à 50). Les médecins meurent les premiers, les corps s'entassent jusque dans les sanctuaires, et la peur de la mort fait tomber le respect des lois et des dieux (II, 52 et 53).\n\n**Le bilan.** Thucydide (III, 87) compte au moins 4 400 hoplites et 300 cavaliers morts, et une foule indéterminée d'autres habitants. La concentration de la population, voulue par la stratégie de Périclès, a aggravé la contagion. Périclès lui-même meurt à l'automne 429, après avoir perdu ses deux fils légitimes.\n\n**Une maladie inconnue.** Typhus, variole, rougeole, fièvre hémorragique : aucune identification ne fait l'unanimité. En 2006, une étude de l'ADN de dents provenant d'une fosse commune du Céramique datée de cette époque a désigné la fièvre typhoïde, conclusion contestée par d'autres généticiens.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "II, 47 à 54 ; III, 87",
        "url": `${THUCYDIDE}:book=2:chapter=47`
      },
      {
        "kind": "modern",
        "author": "Manolis J. Papagrigorakis et al.",
        "work": "DNA examination of ancient dental pulp incriminates typhoid fever as a probable cause of the Plague of Athens, International Journal of Infectious Diseases, 10, 2006"
      },
      {
        "kind": "modern",
        "author": "Simon Hornblower",
        "work": "A Commentary on Thucydides, vol. I, Oxford, Clarendon Press, 1991"
      }
    ]
  },
  {
    "id": "mort-de-pericles",
    "title": "Mort de Périclès",
    "start": -428,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Thucydide (II, 65, 6) dit que Périclès survécut deux ans et six mois au début de la guerre : il meurt à l'automne 429.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "pericles",
      "cleon",
      "thucydide"
    ],
    "summary": "À l'automne 429, Périclès meurt de l'épidémie, après avoir dominé la vie politique athénienne pendant une trentaine d'années. Thucydide en fait l'éloge : il conduisait le peuple plus qu'il n'était conduit par lui. Après lui, des orateurs comme Cléon se disputent la faveur de l'Assemblée.",
    "body": "**Une dernière année difficile.** En 430, les Athéniens, éprouvés par l'invasion et par l'épidémie, envoient sans succès des ambassadeurs à Sparte, retirent à Périclès son commandement et lui infligent une amende ; peu après, ils le réélisent stratège (Thucydide, II, 59 à 65). Il meurt l'année suivante, après avoir perdu ses fils Xanthippe et Paralos.\n\n**Le jugement de Thucydide.** Dans un passage célèbre (II, 65), Thucydide écrit qu'Athènes était, sous Périclès, une démocratie de nom, mais en fait le gouvernement du premier citoyen. Il juge que sa stratégie (tenir la mer, ne pas livrer bataille sur terre, ne pas agrandir l'empire pendant la guerre) aurait mené Athènes à la victoire, et que ses successeurs l'ont perdue en se disputant la première place.\n\n**Ce qui est discuté.** Ce portrait, écrit après la défaite de 404, est aussi un plaidoyer. Les comédies et les adversaires de Périclès, que rapporte Plutarque, montrent une figure contestée, accusée de tyrannie et de gaspiller l'argent des alliés. Le portrait de Cléon en démagogue vient surtout de Thucydide et d'Aristophane, qui étaient ses ennemis.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "II, 59 à 65",
        "url": `${THUCYDIDE}:book=2:chapter=65`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Périclès",
        "locus": "35 à 39",
        "url": `${PLUTARQUE}/Pericles*.html`
      },
      {
        "kind": "modern",
        "author": "Vincent Azoulay",
        "work": "Périclès. La démocratie athénienne à l'épreuve du grand homme, Paris, Armand Colin, 2010"
      }
    ]
  },
  {
    "id": "revolte-de-mytilene",
    "title": "Révolte de Mytilène et débat de l'Assemblée",
    "start": -427,
    "end": -426,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Révolte de l'été 428, reddition et débat de l'été 427, d'après Thucydide (III, 2 à 50). Le nombre des exécutés, « un peu plus de mille », est corrigé par certains éditeurs.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "mytilene",
    "people": [
      "cleon",
      "diodote"
    ],
    "summary": "En 428, Mytilène, principale cité de Lesbos et alliée qui fournissait encore des navires, fait défection. Assiégée, elle se rend en 427. L'Assemblée athénienne vote d'abord la mort de tous les hommes et l'esclavage des femmes et des enfants, puis se ravise le lendemain : une seconde trière arrive juste à temps pour empêcher le massacre.",
    "body": "**La défection.** Les oligarques de Mytilène préparent depuis longtemps la sortie de l'alliance et obtiennent l'appui de Sparte, dont la flotte arrive trop tard. Assiégée par Pachès et affamée, la ville capitule à l'été 427, quand le peuple, armé sur le conseil du Spartiate Salaithos, refuse d'obéir aux oligarques (Thucydide, III, 27 et 28).\n\n**Le débat.** L'Assemblée décide de tuer tous les Mytiléniens adultes et envoie une trière porter l'ordre. Le lendemain, une nouvelle séance est convoquée : Cléon défend la sévérité au nom de la sécurité de l'empire, Diodote plaide la clémence, non par pitié mais par intérêt, pour ne pas pousser les révoltés à résister jusqu'au bout (III, 36 à 49). La clémence l'emporte de justesse ; la seconde trière, dont les rameurs mangent sans quitter leur banc, rejoint la première à Lesbos.\n\n**Le prix.** Plus de mille responsables envoyés à Athènes sont tout de même exécutés sur la proposition de Cléon ; les murs sont rasés, la flotte confisquée, et les terres de l'île divisées en 3 000 lots attribués à des Athéniens (III, 50). Le chiffre de mille, très élevé, est ramené à trente par certains éditeurs du texte.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "III, 2 à 50",
        "url": `${THUCYDIDE}:book=3:chapter=2`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XII, 55",
        "url": `${DIODORE}:book=12:chapter=55`
      },
      {
        "kind": "modern",
        "author": "Simon Hornblower",
        "work": "A Commentary on Thucydides, vol. I, Oxford, Clarendon Press, 1991"
      }
    ]
  },
  {
    "id": "pylos-et-sphacterie",
    "title": "Pylos et Sphactérie",
    "start": -424,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Campagne de l'été 425, racontée en détail par Thucydide (IV, 2 à 41) ; le blocus de Sphactérie dure 72 jours.",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "pylos-coryphasion",
    "people": [
      "demosthene-stratege",
      "cleon",
      "brasidas"
    ],
    "summary": "À l'été 425, le stratège Démosthène fortifie le promontoire de Pylos, en Messénie. Les Spartiates débarqués sur l'île voisine de Sphactérie pour l'assiéger s'y retrouvent bloqués. Après 72 jours, Cléon et Démosthène prennent l'île : 292 hommes, dont environ 120 Spartiates, se rendent, ce qui stupéfie la Grèce.",
    "body": "**Un fort en territoire ennemi.** Retenue par le mauvais temps à Pylos, la flotte athénienne laisse Démosthène fortifier le promontoire avec quelques navires. Les Spartiates attaquent par terre et par mer ; Brasidas, blessé en tentant d'aborder, s'évanouit et perd son bouclier (Thucydide, IV, 11 et 12). Ils débarquent 420 hoplites sur Sphactérie, coupés du continent quand la flotte athénienne revient et bat la leur.\n\n**Cléon et l'île.** Sparte demande la paix, qu'Athènes refuse. Le blocus traîne ; à l'Assemblée, Cléon reproche aux stratèges leur lenteur, et Nicias lui cède le commandement. Cléon promet de ramener les Spartiates, vivants ou morts, en vingt jours, et tient parole avec Démosthène, qui débarque des troupes légères, dont 800 archers et au moins autant de peltastes (IV, 26 à 39).\n\n**Pourquoi c'est important.** On croyait les Spartiates incapables de se rendre (IV, 40). Les 292 prisonniers, otages à Athènes, arrêtent les invasions de l'Attique, et la garnison de Pylos accueille les hilotes en fuite. Un bouclier de bronze pris à Pylos, avec sa dédicace athénienne, a été retrouvé dans l'agora d'Athènes, où Pausanias (I, 15, 4) avait vu ces trophées.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "IV, 2 à 41",
        "url": `${THUCYDIDE}:book=4:chapter=2`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 15, 4",
        "url": `${PAUSANIAS}:book=1:chapter=15`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Archidamian War, Ithaca, Cornell University Press, 1974"
      }
    ]
  },
  {
    "id": "bataille-de-delion",
    "title": "Bataille de Délion",
    "start": -423,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille du début de l'hiver 424/423, sans doute en novembre 424, d'après Thucydide (IV, 89 à 101).",
    "era": "classique",
    "track": "thebes",
    "category": "war",
    "importance": 3,
    "placeId": "delion",
    "people": [
      "pagondas",
      "alcibiade",
      "socrate"
    ],
    "summary": "À la fin de 424, l'armée athénienne qui a fortifié le sanctuaire d'Apollon à Délion, en Béotie, est attaquée sur le chemin du retour par les Béotiens du Thébain Pagondas. Les Thébains, rangés sur 25 rangs de profondeur, et une charge de cavalerie surprise mettent les Athéniens en déroute : près de mille hoplites et le stratège Hippocrate sont tués.",
    "body": "**Un plan trop ambitieux.** Athènes veut soulever la Béotie par des attaques simultanées en plusieurs points, mais le plan est éventé. Le stratège Hippocrate se contente de fortifier le sanctuaire de Délion, près de la frontière, puis renvoie une partie des troupes (Thucydide, IV, 89 et 90).\n\n**La bataille.** Pagondas convainc les béotarques de combattre. Les Thébains se rangent sur 25 boucliers de profondeur (IV, 93) et enfoncent l'aile gauche athénienne ; à droite, les Athéniens l'emportent, mais la cavalerie béotienne, cachée derrière une colline, sème la panique. Les Athéniens perdent près de mille hoplites et Hippocrate (IV, 101). Les Béotiens reprennent ensuite Délion avec une machine à feu, une poutre creuse soufflant sur le rempart du charbon, du soufre et de la poix (IV, 100).\n\n**Des témoins célèbres.** Socrate combat comme hoplite et se replie en bon ordre avec Lachès ; Alcibiade, à cheval, les accompagne, selon le récit que Platon lui prête (Banquet, 221a et b). La bataille montre la force de la colonne profonde thébaine, qu'Épaminondas reprendra à Leuctres.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "IV, 89 à 101",
        "url": `${THUCYDIDE}:book=4:chapter=89`
      },
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Banquet",
        "locus": "220e à 221b"
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Archidamian War, Ithaca, Cornell University Press, 1974"
      }
    ]
  },
  {
    "id": "bataille-d-amphipolis",
    "title": "Brasidas à Amphipolis",
    "start": -421,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Prise de la ville par Brasidas pendant l'hiver 424/423, bataille à la fin de l'été 422, d'après Thucydide (IV, 102 à 108 ; V, 6 à 11).",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 2,
    "placeId": "amphipolis",
    "people": [
      "brasidas",
      "cleon",
      "thucydide"
    ],
    "summary": "Pendant l'hiver 424/423, le Spartiate Brasidas s'empare par surprise d'Amphipolis, colonie athénienne clé de la Thrace ; le stratège Thucydide, arrivé trop tard, est exilé. En 422, Cléon vient reprendre la ville : Brasidas attaque son armée en retraite. Les deux chefs sont tués, ce qui ouvre la voie à la paix.",
    "body": "**La prise d'Amphipolis.** Brasidas traverse la Thessalie avec 1 700 hoplites, dont 700 hilotes armés, et rallie les cités de Chalcidique en leur promettant la liberté. Par une nuit de neige, il franchit le pont du Strymon et obtient la reddition d'Amphipolis à des conditions modérées (Thucydide, IV, 102 à 106). Thucydide, stratège à Thasos, sauve seulement le port d'Éion ; il passe vingt ans en exil, ce qui lui permet, dit-il, de s'informer auprès des deux camps (V, 26).\n\n**La bataille.** En 422, Cléon s'installe à Éion puis s'approche de la ville. Croyant pouvoir se retirer sans danger, il fait faire demi-tour à son armée ; Brasidas sort brusquement et frappe la colonne en marche. Cléon est tué dans la fuite, Brasidas mortellement blessé ; les Athéniens perdent environ 600 hommes, leurs adversaires 7 (V, 6 à 11).\n\n**Pourquoi c'est important.** Les Amphipolitains honorent Brasidas comme le fondateur de leur cité. La mort des deux hommes les plus hostiles à la paix, selon Thucydide (V, 16), permet à Nicias et à Pleistoanax de négocier le traité de 421.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "IV, 78 à 108 ; V, 6 à 11 et 26",
        "url": `${THUCYDIDE}:book=5:chapter=6`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Archidamian War, Ithaca, Cornell University Press, 1974"
      }
    ]
  },
  {
    "id": "paix-de-nicias",
    "title": "Paix de Nicias",
    "start": -420,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Traité conclu au début du printemps 421, juste après les Grandes Dionysies, le 25 Élaphébolion selon Thucydide (V, 19 et 20), vers la fin mars ou le début d'avril.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "nicias",
      "pleistoanax"
    ],
    "summary": "Au printemps 421, Athènes et Sparte concluent une paix de cinquante ans, négociée par Nicias et le roi Pleistoanax : chacun doit rendre prisonniers et conquêtes, dont Amphipolis et Pylos. Mais Corinthe, les Béotiens, Mégare et l'Élide refusent de signer, les restitutions ne se font pas, et la guerre reprend sous d'autres formes.",
    "body": "**Dix ans de guerre.** La guerre dite d'Archidamos (de 431 à 421) n'a pas de vainqueur : Sparte veut récupérer les prisonniers de Sphactérie, Athènes est affaiblie par Délion et Amphipolis. Aux Dionysies de 421, juste avant la signature, Aristophane fait jouer La Paix, où le vigneron Trygée délivre la déesse de la Paix.\n\n**Le traité.** Thucydide (V, 18) en recopie le texte : libre accès aux sanctuaires communs, restitution d'Amphipolis à Athènes, de Pylos et des prisonniers à Sparte, autonomie de plusieurs cités de Chalcidique moyennant le tribut fixé jadis par Aristide. Quelques semaines plus tard, Athènes et Sparte concluent aussi une alliance (V, 23 et 24).\n\n**Une paix fragile.** Les Béotiens, les Corinthiens, les Éléens et les Mégariens votent contre (V, 17). Le Spartiate Cléaridas refuse de livrer Amphipolis, et Athènes garde Pylos. Thucydide refuse d'y voir une vraie paix : pour lui, la guerre dure vingt-sept ans d'un seul tenant (V, 26).",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "V, 14 à 26",
        "url": `${THUCYDIDE}:book=5:chapter=14`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Nicias",
        "locus": "9 et 10",
        "url": `${PLUTARQUE}/Nicias*.html`
      },
      {
        "kind": "ancient",
        "author": "Aristophane",
        "work": "La Paix"
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Peace of Nicias and the Sicilian Expedition, Ithaca, Cornell University Press, 1981"
      }
    ]
  },
  {
    "id": "temple-d-athena-nike",
    "title": "Temple d'Athéna Nikè",
    "start": -426,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Date discutée : un décret (IG I³ 35) confie le projet à Callicratès, vers 448 selon l'écriture, plus tard selon d'autres ; la construction est le plus souvent placée vers 427 à 424, la balustrade sculptée vers 415 à 410.",
    "era": "classique",
    "track": "athenes",
    "category": "building",
    "importance": 3,
    "placeId": "temple-d-athena-nike",
    "people": [
      "callicrates"
    ],
    "summary": "Vers 427 à 424, les Athéniens élèvent sur le bastion qui domine l'entrée de l'Acropole un petit temple ionique dédié à Athéna Nikè, la Victoire, d'après un plan de l'architecte Callicratès. Sa frise montre notamment des Grecs combattant des Perses ; sa balustrade, ornée de Victoires, est un chef-d'œuvre de la sculpture de la fin du Ve siècle.",
    "body": "**Un culte ancien, un temple nouveau.** Un autel et un petit sanctuaire d'Athéna Nikè existaient déjà sur le bastion qui flanque l'entrée de l'Acropole. Un décret (IG I³ 35) ordonne de donner à la déesse une prêtresse, choisie parmi toutes les Athéniennes, et de construire un temple et une porte sur le plan de Callicratès, l'un des architectes du Parthénon. Un second décret (IG I³ 36), de 424/423, fixe le salaire de la prêtresse.\n\n**Le temple.** C'est un petit édifice ionique en marbre du Pentélique, avec quatre colonnes devant et quatre derrière. La frise montre une assemblée de dieux et des batailles, dont une contre des Perses, peut-être Marathon. Vers 415 à 410, le bastion reçoit une balustrade sculptée de Victoires, dont la célèbre Victoire rattachant sa sandale, au musée de l'Acropole. Pausanias (I, 22, 4) l'appelle le temple de la Victoire sans ailes.\n\n**Ce qui est incertain.** La date du premier décret est un débat classique de l'épigraphie attique : la forme des lettres invitait à le placer vers 448, mais cette méthode de datation a été contestée. Démonté par les Ottomans en 1686 pour fortifier l'Acropole, le temple a été remonté à partir de 1835.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Décrets sur le sanctuaire d'Athéna Nikè",
        "locus": "IG I³ 35 et 36"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 22, 4",
        "url": `${PAUSANIAS}:book=1:chapter=22`
      },
      {
        "kind": "modern",
        "author": "Ira S. Mark",
        "work": "The Sanctuary of Athena Nike in Athens: Architectural Stages and Chronology, Hesperia Supplement 26, Princeton, 1993"
      },
      {
        "kind": "modern",
        "author": "Bernard Holtzmann",
        "work": "L'Acropole d'Athènes. Monuments, cultes et histoire du sanctuaire d'Athèna Polias, Paris, Picard, 2003"
      }
    ]
  },
  {
    "id": "erechtheion",
    "title": "Construction de l'Érechthéion",
    "start": -420,
    "end": -405,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Début des travaux vers 421, date discutée ; la reprise en 409/408 est attestée par le rapport des commissaires (IG I³ 474) et l'achèvement vers 406 par les comptes suivants (IG I³ 475 à 479).",
    "era": "classique",
    "track": "athenes",
    "category": "building",
    "importance": 2,
    "placeId": "erechtheion",
    "summary": "À partir de 421 environ, et surtout de 409 à 406, les Athéniens construisent sur l'Acropole, au nord du Parthénon, un temple ionique complexe qui abrite l'antique statue d'Athéna Polias en bois d'olivier et les cultes d'Érechthée et de Poséidon. Son portique des Caryatides, six jeunes femmes sculptées qui servent de colonnes, est l'une des images les plus célèbres de l'Acropole.",
    "body": "**Un temple pour les plus vieux cultes.** Le temple, que les inscriptions appellent « le temple où se trouve l'ancienne statue », réunit sur un terrain en pente plusieurs lieux sacrés : la statue d'Athéna Polias, les marques du trident de Poséidon, l'olivier sacré d'Athéna, la tombe de Cécrops. Pausanias (I, 26, 5 à 27, 3) l'appelle Érechthéion. Son plan sur deux niveaux, avec trois portiques différents, est unique dans l'architecture grecque.\n\n**Un chantier en temps de guerre.** Interrompu sans doute pendant l'expédition de Sicile, le chantier reprend en 409/408 : un rapport de commissaires (IG I³ 474) fait l'état des pierres posées ou à tailler, et les comptes suivants nomment des dizaines d'ouvriers, citoyens, métèques et esclaves, payés le plus souvent une drachme par jour. Ces comptes sont l'une des meilleures sources sur le travail à Athènes.\n\n**Ce qui est incertain.** La date du début et le nom de l'architecte sont inconnus. Une des six Caryatides est au British Museum depuis son enlèvement par lord Elgin ; les autres sont au musée de l'Acropole, remplacées sur place par des copies.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Rapport des commissaires et comptes de l'Érechthéion",
        "locus": "IG I³ 474 à 479"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "I, 26, 5 à 27, 3",
        "url": `${PAUSANIAS}:book=1:chapter=26`
      },
      {
        "kind": "modern",
        "author": "Gorham Phillips Stevens et al.",
        "work": "The Erechtheum, Cambridge (Mass.), Harvard University Press, 1927"
      },
      {
        "kind": "modern",
        "author": "Bernard Holtzmann",
        "work": "L'Acropole d'Athènes. Monuments, cultes et histoire du sanctuaire d'Athèna Polias, Paris, Picard, 2003"
      }
    ]
  },
  {
    "id": "bataille-de-mantinee-418",
    "title": "Bataille de Mantinée (418)",
    "start": -417,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille de l'été 418, d'après Thucydide (V, 64 à 74).",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 2,
    "placeId": "mantinee",
    "people": [
      "agis-ii",
      "alcibiade"
    ],
    "summary": "À l'été 418, près de Mantinée, en Arcadie, le roi spartiate Agis II écrase la coalition d'Argos, de Mantinée et d'Athènes formée à l'instigation d'Alcibiade. Plus grande bataille d'hoplites de la guerre selon Thucydide, elle rend à Sparte le prestige perdu à Sphactérie et brise l'alliance argienne.",
    "body": "**Une coalition contre Sparte.** Après la paix de Nicias, Argos, libérée de son traité avec Sparte, réunit Mantinée, l'Élide et, grâce à Alcibiade, Athènes dans une alliance (Thucydide, V, 43 à 47). Le texte du traité nous est parvenu par Thucydide et, en partie, par une inscription athénienne (IG I³ 83).\n\n**La bataille.** Les deux armées se heurtent dans la plaine de Mantinée. Thucydide (V, 71) explique que toute armée glisse vers sa droite, chaque homme cherchant l'abri du bouclier de son voisin. Les manœuvres d'Agis ouvrent une brèche dans sa propre ligne, mais le centre spartiate enfonce les Argiens et les Athéniens ; seule l'aile gauche spartiate est battue par les Mantinéens.\n\n**Le bilan.** Thucydide (V, 74) estime les pertes des alliés à environ 1 100 hommes, dont 200 Athéniens et Éginètes et les deux stratèges Lachès et Nicostratos, et celles des Spartiates à environ 300, en avouant ne pas connaître les effectifs exacts, tant les Spartiates gardaient le secret (V, 68). Argos passe peu après à l'oligarchie et s'allie à Sparte.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "V, 43 à 81",
        "url": `${THUCYDIDE}:book=5:chapter=64`
      },
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Alliance d'Athènes avec Argos, Mantinée et l'Élide",
        "locus": "IG I³ 83"
      },
      {
        "kind": "modern",
        "author": "J. F. Lazenby",
        "work": "The Peloponnesian War: A Military Study, Londres, Routledge, 2004"
      }
    ]
  },
  {
    "id": "massacre-de-melos",
    "title": "Siège et massacre de Mélos",
    "start": -415,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Siège de l'été et de l'hiver 416/415, d'après Thucydide (V, 84 à 116) ; le dialogue est une composition de l'historien, non un compte rendu.",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "melos",
    "summary": "En 416, Athènes somme Mélos, île des Cyclades restée neutre et colonie de Sparte, d'entrer dans son empire. Les Méliens refusent. Après un siège de plusieurs mois, la ville se rend : les Athéniens tuent les hommes adultes, réduisent en esclavage les femmes et les enfants et installent 500 colons. Thucydide en tire son célèbre dialogue sur la loi du plus fort.",
    "body": "**Le dialogue mélien.** Avant le siège, Thucydide (V, 85 à 113) met en scène un débat entre les envoyés athéniens et les magistrats de Mélos. Les Athéniens refusent de parler de justice : entre puissances inégales, disent-ils, le fort fait ce qu'il peut et le faible cède. Les Méliens comptent sur les dieux et sur Sparte, qui ne viendra pas. Ce texte, reconstitution littéraire, est l'une des pages les plus commentées de l'histoire grecque.\n\n**Le siège.** Les Athéniens viennent avec 30 navires, plus 6 de Chios et 2 de Lesbos, 1 200 hoplites athéniens, 300 archers, 20 archers à cheval et environ 1 500 hoplites alliés (V, 84). La ville, bloquée, tient jusqu'à l'hiver, puis se rend sans conditions, peut-être après une trahison (V, 116).\n\n**Ce qui est discuté.** Thucydide raconte le massacre sans commentaire, mais le place juste avant l'expédition de Sicile, où l'orgueil athénien sera puni. On le rapproche souvent des Troyennes d'Euripide, jouées au printemps 415, sans preuve d'un lien direct. Mélos figure pour 15 talents dans l'évaluation du tribut de 425 (IG I³ 71), sans qu'on sache si elle a jamais payé.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "V, 84 à 116",
        "url": `${THUCYDIDE}:book=5:chapter=84`
      },
      {
        "kind": "ancient",
        "author": "Inscriptions attiques",
        "work": "Décret d'évaluation du tribut de 425",
        "locus": "IG I³ 71"
      },
      {
        "kind": "modern",
        "author": "Simon Hornblower",
        "work": "A Commentary on Thucydides, vol. III, Oxford, Oxford University Press, 2008"
      }
    ]
  },
  {
    "id": "expedition-de-sicile",
    "title": "Expédition de Sicile",
    "start": -414,
    "end": -412,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Expédition partie au début de l'été 415, anéantie en septembre 413 ; l'éclipse de lune qui retarde la retraite athénienne (Thucydide, VII, 50) est celle du 27 août 413.",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 1,
    "placeId": "syracuse",
    "people": [
      "nicias",
      "alcibiade",
      "lamachos",
      "gylippe",
      "demosthene-stratege",
      "hermocrate"
    ],
    "summary": "En 415, Athènes envoie contre Syracuse la plus grande flotte jamais armée par une cité grecque, sous Nicias, Alcibiade et Lamachos. Privée d'Alcibiade, rappelé pour sacrilège et passé à Sparte, l'expédition s'enlise. Renforcée en 413, elle est détruite : battue dans le grand port, l'armée en retraite capitule, Nicias et Démosthène sont exécutés.",
    "body": "**Un pari.** Appelée par Ségeste, en guerre contre Sélinonte, alliée de Syracuse, l'Assemblée vote l'expédition malgré Nicias (Thucydide, VI, 8 à 26). Juste avant le départ, des inconnus mutilent les hermès de la ville, et Alcibiade est accusé d'avoir parodié les Mystères d'Éleusis. Rappelé pour être jugé, il s'enfuit à Sparte, à qui il conseille d'envoyer un général à Syracuse et de fortifier Décélie (VI, 27 à 29, 53 à 61 et 88 à 93).\n\n**L'enlisement.** La flotte compte 134 trières et 5 100 hoplites (VI, 43). Les Athéniens tardent à attaquer, puis entreprennent d'encercler Syracuse d'un mur. Lamachos est tué ; le Spartiate Gylippe arrive en 414 et coupe le mur athénien. Démosthène amène en 413 une seconde flotte de 73 navires, mais l'attaque nocturne des Épipoles échoue. Une éclipse de lune fait différer le départ (VII, 50), et la flotte, enfermée dans le grand port, est battue.\n\n**Le désastre.** L'armée tente de fuir par terre ; harcelée, elle est massacrée au passage de l'Assinaros. Nicias et Démosthène sont exécutés malgré Gylippe, et au moins 7 000 prisonniers sont parqués dans les carrières de Syracuse (VII, 84 à 87). Peu revinrent, sur un grand nombre, conclut Thucydide. Athènes a perdu en deux ans environ 200 trières et des dizaines de milliers d'hommes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI et VII",
        "url": `${THUCYDIDE}:book=6:chapter=1`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Nicias",
        "locus": "12 à 30",
        "url": `${PLUTARQUE}/Nicias*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIII, 2 à 33",
        "url": `${DIODORE}:book=13:chapter=2`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Peace of Nicias and the Sicilian Expedition, Ithaca, Cornell University Press, 1981"
      }
    ]
  },
  {
    "id": "occupation-de-decelie",
    "title": "Les Spartiates fortifient Décélie",
    "start": -412,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Fortification commencée au début du printemps 413 par le roi Agis, d'après Thucydide (VII, 19).",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 3,
    "placeId": "decelie",
    "people": [
      "agis-ii",
      "alcibiade"
    ],
    "summary": "Au printemps 413, sur le conseil d'Alcibiade, le roi spartiate Agis II fortifie Décélie, au nord de l'Attique, à environ 120 stades d'Athènes. Au lieu d'invasions saisonnières, une garnison occupe désormais le pays toute l'année : plus de 20 000 esclaves s'enfuient, le bétail est perdu et Athènes doit tout faire venir par mer.",
    "body": "**Une idée d'Alcibiade.** Réfugié à Sparte, Alcibiade conseille d'occuper un point fort en Attique (Thucydide, VI, 91, 6 et 7). Décélie, sur les pentes du Parnès, commande la route de l'Eubée et voit Athènes. Agis s'y installe au printemps 413, au moment où Athènes envoie des renforts en Sicile.\n\n**Une guerre permanente.** Thucydide (VII, 27 et 28) décrit les conséquences : plus de 20 000 esclaves, en grande partie des artisans, désertent ; chevaux et bétail sont perdus ; la cité, gardée jour et nuit, devient une forteresse, et le blé d'Eubée doit contourner le cap Sounion par mer. Le travail des mines d'argent du Laurion, dont Alcibiade avait annoncé la ruine, est sans doute désorganisé.\n\n**La fin.** La garnison reste jusqu'à la capitulation d'Athènes en 404. Agis y reçoit transfuges et ambassades, et Décélie sert de base à la pression spartiate sur la ville pendant toute la dernière phase du conflit, que l'on appelle pour cette raison la guerre de Décélie.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VI, 91, 6 et 7 ; VII, 19 et 27 à 28",
        "url": `${THUCYDIDE}:book=7:chapter=19`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Fall of the Athenian Empire, Ithaca, Cornell University Press, 1987"
      }
    ]
  },
  {
    "id": "coup-d-etat-des-quatre-cents",
    "title": "Coup d'État des Quatre-Cents",
    "start": -410,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Coup d'État du printemps 411, au mois de Thargélion selon la Constitution d'Athènes (32, 1) ; le régime tient environ quatre mois.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "pisandre",
      "antiphon",
      "theramene",
      "alcibiade"
    ],
    "summary": "En 411, après le désastre de Sicile, des oligarques athéniens menés par Pisandre et Antiphon font voter la fin de la démocratie, en promettant l'aide perse que ferait venir Alcibiade. Un conseil de Quatre-Cents gouverne Athènes, mais la flotte de Samos reste démocrate. Au bout de quatre mois, les Quatre-Cents tombent ; la démocratie est rétablie en 410.",
    "body": "**Le complot.** Alcibiade, réfugié auprès du satrape Tissapherne, fait savoir qu'il rallierait la Perse à Athènes si la démocratie était abolie. Pisandre fait accepter l'idée à l'Assemblée, puis les conjurés font régner la terreur par des assassinats (Thucydide, VIII, 47 à 66). Réunie à Colone, hors de la ville, l'Assemblée supprime les indemnités et confie le pouvoir à quatre cents hommes, qui chassent le Conseil des Cinq-Cents (VIII, 67 à 70).\n\n**Deux Athènes.** À Samos, les marins de la flotte refusent le coup d'État, se proclament la vraie cité et rappellent Alcibiade (VIII, 73 à 77). À Athènes, les Quatre-Cents négocient avec Sparte. La perte de l'Eubée, en septembre 411, provoque leur chute, menée par Théramène, l'un des leurs. Phrynichos est assassiné, Antiphon jugé et exécuté.\n\n**Les Cinq-Mille.** Le pouvoir passe à une assemblée réservée aux citoyens capables de s'armer en hoplites, régime que Thucydide (VIII, 97) juge le meilleur qu'Athènes ait connu de son temps. La démocratie complète est rétablie en 410, après la victoire navale de Cyzique. La Constitution d'Athènes (29 à 33) donne une version différente, avec des projets de constitution dont la valeur est discutée.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VIII, 45 à 98",
        "url": `${THUCYDIDE}:book=8:chapter=45`
      },
      {
        "kind": "ancient",
        "author": "Aristote (école d')",
        "work": "Constitution d'Athènes",
        "locus": "29 à 33"
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Fall of the Athenian Empire, Ithaca, Cornell University Press, 1987"
      },
      {
        "kind": "modern",
        "author": "Peter J. Rhodes",
        "work": "A Commentary on the Aristotelian Athenaion Politeia, Oxford, Clarendon Press, 1981"
      }
    ]
  },
  {
    "id": "synoecisme-de-rhodes",
    "title": "Fondation de la ville de Rhodes",
    "start": -407,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Diodore (XIII, 75, 1) date le regroupement de l'archontat d'Euctémon (408/407) ; la construction de la ville nouvelle s'étale sur plusieurs années.",
    "era": "classique",
    "track": "rhodes",
    "category": "politics",
    "importance": 2,
    "placeId": "rhodes",
    "summary": "En 408/407, les trois cités de l'île de Rhodes, Lindos, Ialysos et Camiros, s'unissent pour fonder une capitale commune à la pointe nord de l'île, Rhodes. Ce synœcisme, réalisé quelques années après la sortie de l'île de l'alliance athénienne, donne naissance à l'une des grandes puissances maritimes de l'époque hellénistique.",
    "body": "**Trois cités, une ville.** Les cités doriennes de l'île existaient depuis l'époque archaïque ; des Rhodiens avaient fondé Géla, en Sicile, avec des Crétois. Diodore (XIII, 75, 1) rapporte que leurs habitants se regroupent dans une ville nouvelle, appelée Rhodes. Les anciennes cités ne disparaissent pas : elles restent des communautés et des sanctuaires, comme celui d'Athéna à Lindos.\n\n**Une ville planifiée.** Strabon (XIV, 2, 9) attribue le plan de Rhodes à l'architecte qui avait dessiné le Pirée, que l'on identifie souvent à Hippodamos de Milet, ce qui pose un problème de chronologie. Le plan en damier, les ports et les murailles en font une ville admirée dans l'Antiquité.\n\n**Pourquoi c'est important.** Rhodes avait quitté l'alliance athénienne pendant l'hiver 412/411 (Thucydide, VIII, 44). Unifiée, elle devient un acteur indépendant de l'Égée, alliée tour à tour de Sparte, d'Athènes et des rois hellénistiques ; le Colosse sera élevé après le siège de 305 à 304.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIII, 75, 1",
        "url": `${DIODORE}:book=13:chapter=75`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIV, 2, 9"
      },
      {
        "kind": "ancient",
        "author": "Thucydide",
        "work": "Histoire de la guerre du Péloponnèse",
        "locus": "VIII, 44",
        "url": `${THUCYDIDE}:book=8:chapter=44`
      },
      {
        "kind": "modern",
        "author": "Richard M. Berthold",
        "work": "Rhodes in the Hellenistic Age, Ithaca, Cornell University Press, 1984"
      }
    ]
  },
  {
    "id": "bataille-des-arginuses",
    "title": "Bataille des Arginuses et procès des stratèges",
    "start": -405,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille de la fin de l'été 406 ; le procès des stratèges a lieu à l'automne, après la fête des Apatouries (Xénophon, Helléniques, I, 7, 8).",
    "era": "classique",
    "track": "athenes",
    "category": "war",
    "importance": 2,
    "placeId": "arginuses",
    "people": [
      "callicratidas",
      "conon",
      "theramene",
      "thrasybule",
      "socrate"
    ],
    "summary": "En 406, près des îles Arginuses, entre Lesbos et l'Asie, une flotte athénienne armée en urgence, avec des esclaves promis à la liberté, bat la flotte spartiate de Callicratidas, qui se noie. Mais une tempête empêche de recueillir les naufragés : à Athènes, six des stratèges vainqueurs sont condamnés à mort ensemble par l'Assemblée, au mépris de la loi.",
    "body": "**Un dernier effort.** Conon, bloqué dans Mytilène, risque de perdre la flotte. Athènes arme en trente jours 110 navires, en embarquant tous les hommes en âge de servir, libres et esclaves (Xénophon, Helléniques, I, 6, 24) ; les esclaves qui combattent seront affranchis (Aristophane, Grenouilles, v. 693 et 694). Avec les alliés, la flotte compte plus de 150 navires contre 120 à Callicratidas (I, 6, 25 et 26).\n\n**La victoire.** Les Spartiates perdent environ 70 navires et leur navarque ; les Athéniens en perdent 25 (I, 6, 34). Une tempête se lève : les triérarques Théramène et Thrasybule, chargés de recueillir les équipages des épaves, ne peuvent le faire, et un grand nombre d'hommes se noient (I, 6, 35).\n\n**Le procès.** À Athènes, Théramène se retourne contre les stratèges. L'Assemblée, dans un climat de colère, décide de les juger ensemble par un seul vote, contrairement à la loi ; Socrate, membre du conseil qui préside ce jour-là, refuse en vain de mettre la proposition aux voix (Xénophon, I, 7, 15 ; Platon, Apologie, 32b). Les six stratèges présents, dont Périclès le Jeune, sont exécutés. Les Athéniens s'en repentent peu après (I, 7, 35).",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "I, 6, 24 à I, 7, 35",
        "url": `${XENOPHON}:book=1:chapter=6`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIII, 97 à 103",
        "url": `${DIODORE}:book=13:chapter=97`
      },
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Apologie de Socrate",
        "locus": "32b et c"
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Fall of the Athenian Empire, Ithaca, Cornell University Press, 1987"
      }
    ]
  },
  {
    "id": "bataille-d-aigos-potamos",
    "title": "Bataille d'Aigos Potamos",
    "start": -404,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille de la fin de l'été ou de l'automne 405, d'après Xénophon (Helléniques, II, 1, 17 à 32), qui n'en donne pas le jour.",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 2,
    "placeId": "aigos-potamos",
    "people": [
      "lysandre",
      "conon",
      "alcibiade"
    ],
    "summary": "En 405, sur la rive européenne de l'Hellespont, à Aigos Potamos, le Spartiate Lysandre surprend la flotte athénienne de 180 navires, dont les équipages sont dispersés à terre, et la capture presque entière. Seul Conon s'échappe avec quelques navires. Privée de flotte, Athènes ne peut plus recevoir le blé de la mer Noire : elle capitule au printemps suivant.",
    "body": "**Cinq jours face à face.** Lysandre, financé par Cyrus le Jeune, prend Lampsaque. La flotte athénienne s'installe en face, sur une plage sans port, loin de son ravitaillement à Sestos. Chaque jour, elle offre la bataille, puis les équipages se dispersent. Alcibiade, retiré dans ses forteresses de Chersonèse, vient conseiller aux stratèges de se replier sur Sestos ; ils le renvoient (Xénophon, Helléniques, II, 1, 25 et 26).\n\n**La surprise.** Le cinquième jour, Lysandre attaque au moment où les Athéniens sont à terre et capture presque tous les navires sur la plage. Conon s'enfuit avec huit navires vers Chypre, et la trière Paralos porte la nouvelle à Athènes (II, 1, 28 et 29). Lysandre fait exécuter les prisonniers athéniens, environ 3 000 selon Plutarque (Lysandre, 13).\n\n**La fin de la guerre.** Cette nuit-là, écrit Xénophon (II, 2, 3), personne ne dormit à Athènes. Lysandre soumet les alliés d'Athènes, puis bloque le Pirée ; la ville, affamée, capitule au printemps 404. Les soupçons de trahison visant certains stratèges, évoqués par Xénophon et par Lysias, n'ont jamais été prouvés.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "II, 1, 17 à II, 2, 4",
        "url": `${XENOPHON}:book=2:chapter=1`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Lysandre",
        "locus": "9 à 13",
        "url": `${PLUTARQUE}/Lysander*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIII, 105 et 106",
        "url": `${DIODORE}:book=13:chapter=105`
      },
      {
        "kind": "modern",
        "author": "Donald Kagan",
        "work": "The Fall of the Athenian Empire, Ithaca, Cornell University Press, 1987"
      }
    ]
  },
  {
    "id": "hippocrate-et-la-medecine-de-cos",
    "title": "Hippocrate et la médecine de Cos",
    "start": -429,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Hippocrate est attesté par Platon, son contemporain ; la date de 430 environ correspond à son activité supposée. On ignore lesquels des traités de la Collection hippocratique sont de lui.",
    "era": "classique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "cos",
    "people": [
      "hippocrate"
    ],
    "summary": "Dans la seconde moitié du Ve siècle, Hippocrate de Cos, issu d'une famille de médecins qui se disaient descendants d'Asclépios, enseigne une médecine fondée sur l'observation des malades et la recherche de causes naturelles. Son nom couvre la Collection hippocratique, une soixantaine de traités écrits par plusieurs auteurs entre 430 et 330 environ.",
    "body": "**Ce que l'on sait de l'homme.** Platon, son contemporain, le présente comme un médecin célèbre de Cos, de la famille des Asclépiades, qui enseigne contre salaire (Protagoras, 311b et c), et lui prête une méthode qui étudie le corps en le rapportant à la nature de l'ensemble (Phèdre, 270c et d). Aristote le cite comme exemple de grand médecin (Politique, VII, 4). Les biographies plus tardives, qui le font naître vers 460, sont peu fiables.\n\n**La Collection hippocratique.** Ces traités, réunis plus tard, sans doute à Alexandrie, décrivent des cas cliniques jour après jour (Épidémies), l'influence du climat sur la santé (Airs, eaux, lieux), ou refusent l'origine divine de l'épilepsie (Maladie sacrée). Le Serment, qui engage le médecin à ne pas nuire et à garder le secret, en fait partie, à une date discutée.\n\n**Ce qui est incertain.** Dès l'Antiquité, on se demandait quels traités étaient d'Hippocrate lui-même : c'est la « question hippocratique », qui n'a pas de réponse sûre. La Collection mêle des auteurs, des doctrines et des époques différentes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Protagoras",
        "locus": "311b et c"
      },
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Phèdre",
        "locus": "270c et d"
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Politique",
        "locus": "VII, 4, 1326a 15"
      },
      {
        "kind": "modern",
        "author": "Jacques Jouanna",
        "work": "Hippocrate, Paris, Fayard, 1992"
      }
    ]
  },
  {
    "id": "medee-d-euripide",
    "title": "Médée d'Euripide",
    "start": -430,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date donnée par l'argument antique de la pièce : archontat de Pythodoros (432/431), donc Grandes Dionysies du printemps 431.",
    "era": "classique",
    "track": "athenes",
    "category": "culture",
    "importance": 3,
    "placeId": "theatre-de-dionysos",
    "people": [
      "euripide",
      "sophocle"
    ],
    "summary": "Au printemps 431, quelques jours avant le début de la guerre du Péloponnèse, Euripide présente aux Dionysies Médée, l'histoire de la magicienne qui tue ses enfants pour se venger de Jason. Il n'obtient que la troisième place, derrière Euphorion, fils d'Eschyle, et Sophocle. La pièce deviendra l'une des tragédies grecques les plus jouées.",
    "body": "**Un concours perdu.** Selon l'argument antique, Euripide présentait Médée avec Philoctète, Dictys et le drame satyrique Les Moissonneurs ; il est classé troisième. C'est un sort fréquent pour Euripide, qui fait jouer ses premières pièces en 455 mais ne remporte de son vivant que quatre victoires selon la Souda, pour environ 90 pièces.\n\n**Une tragédie dérangeante.** Médée, princesse de Colchide abandonnée à Corinthe par Jason qui épouse la fille du roi, tue sa rivale puis ses propres enfants, et s'enfuit sur le char du Soleil. La pièce donne la parole à une femme étrangère qui dénonce la condition des épouses grecques. On ne sait pas si le meurtre des enfants par leur mère est une invention d'Euripide ou s'il le reprend d'un poète antérieur.\n\n**Le poète.** Euripide, né vers 480, passe pour un esprit novateur, proche des sophistes, souvent moqué par Aristophane. Dix-huit de ses tragédies sont conservées, plus que pour Eschyle et Sophocle réunis. Il meurt en 406 en Macédoine, à la cour du roi Archélaos.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Euripide",
        "work": "Médée",
        "locus": "argument antique attribué à Aristophane de Byzance"
      },
      {
        "kind": "ancient",
        "author": "Souda",
        "work": "Lexique",
        "locus": "s.v. Euripide"
      },
      {
        "kind": "modern",
        "author": "Donald J. Mastronarde",
        "work": "Euripides: Medea, Cambridge, Cambridge University Press, 2002"
      }
    ]
  },
  {
    "id": "histoires-d-herodote",
    "title": "Les Histoires d'Hérodote",
    "start": -429,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Date discutée : les Histoires mentionnent des faits de 431 et 430 (VII, 137 et 233 ; IX, 73), et Aristophane semble les parodier dans Les Acharniens en 425 ; leur diffusion est donc placée vers 430 à 425.",
    "era": "classique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "halicarnasse",
    "people": [
      "herodote"
    ],
    "summary": "Vers 430 à 425, Hérodote d'Halicarnasse diffuse ses Histoires, première grande œuvre en prose de l'histoire grecque : une enquête (historiê) sur les causes et le déroulement des guerres entre Grecs et Perses, mêlée de descriptions de l'Égypte, de la Scythie ou de Babylone. Cicéron l'appellera le père de l'histoire.",
    "body": "**Un projet nouveau.** Hérodote annonce qu'il expose son enquête pour que le temps n'efface pas les actions des hommes et pour dire pourquoi Grecs et Barbares se sont fait la guerre. Il a voyagé en Égypte, au Proche-Orient et en mer Noire, interrogé des témoins et confronté les versions, en disant souvent ce qu'il ne croit pas. Ses neuf livres, divisés plus tard par les savants d'Alexandrie, vont de Crésus à la prise de Sestos en 479.\n\n**L'homme.** Né à Halicarnasse, en Carie, sujet de l'empire perse, il quitte sa cité sous le tyran Lygdamis, séjourne à Samos et à Athènes, puis devient citoyen de Thourioi. Plutarque, qui lui est hostile, rapporte qu'Athènes lui aurait voté dix talents (De la malignité d'Hérodote, 26).\n\n**Ce qui est discuté.** On ignore quand Hérodote est mort et si l'œuvre est achevée. Thucydide, qui écrit peu après, critique sans le nommer les récits qui cherchent à plaire plutôt qu'à établir la vérité (I, 22). Les modernes ont longtemps douté de sa fiabilité ; l'archéologie et les sources orientales confirment pourtant une bonne partie de ce qu'il rapporte, mais pas ses chiffres.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Hérodote",
        "work": "Histoires",
        "locus": "I, préambule ; VII, 137 et 233 ; IX, 73",
        "url": `${HERODOTE}:book=1:chapter=1`
      },
      {
        "kind": "ancient",
        "author": "Cicéron",
        "work": "Des lois",
        "locus": "I, 5"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "De la malignité d'Hérodote",
        "locus": "26 (Moralia 862a et b)"
      },
      {
        "kind": "modern",
        "author": "François Hartog",
        "work": "Le Miroir d'Hérodote. Essai sur la représentation de l'autre, Paris, Gallimard, 1980"
      },
      {
        "kind": "modern",
        "author": "Carolyn Dewald et John Marincola (dir.)",
        "work": "The Cambridge Companion to Herodotus, Cambridge, Cambridge University Press, 2006"
      }
    ]
  }
]
