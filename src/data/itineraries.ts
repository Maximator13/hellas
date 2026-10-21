import type { Itinerary } from './schema.ts'

export const itineraries: Itinerary[] = [
  {
    "id": "campagnes-d-alexandre",
    "title": "Campagnes d'Alexandre, de Pella à Babylone",
    "summary": "Parti de Pella au printemps 334 av. J.-C., Alexandre franchit l'Hellespont, bat les Perses au Granique, à Issos et à Gaugamèles, prend Babylone, Suse et Persépolis, poursuit Darius puis ses satrapes jusqu'en Bactriane et en Sogdiane, et descend l'Indus jusqu'à la mer. Le retour par le désert de Gédrosie s'achève à Babylone, où il meurt en juin 323 av. J.-C., après onze ans de campagne.",
    "from": -333,
    "to": -322,
    "waypoints": [
      {
        "lon": 22.5185,
        "lat": 40.7546,
        "label": "Départ de Pella",
        "year": -333,
        "month": 3,
        "certainty": "attested",
        "note": "Alexandre quitte la Macédoine « au début du printemps » avec environ 30 000 fantassins et 5 000 cavaliers (Arrien, Anabase I, 11, 3 ; Diodore XVII, 17, 3 et 4), mois approximatif."
      },
      {
        "lon": 26.3893,
        "lat": 40.2134,
        "label": "Passage de l'Hellespont à Sestos",
        "year": -333,
        "month": 4,
        "certainty": "attested",
        "note": "Arrivée à l'Hellespont vingt jours après Amphipolis ; Parménion fait passer l'essentiel de l'armée de Sestos à Abydos sur 160 trières (Arrien I, 11, 5 et 6)."
      },
      {
        "lon": 26.2385,
        "lat": 39.9574,
        "label": "Troie",
        "year": -333,
        "month": 4,
        "certainty": "attested",
        "note": "Alexandre débarque au port des Achéens, sacrifie à Athéna Ilias et honore la tombe d'Achille (Arrien I, 11, 7 à 12, 1 ; Plutarque, Alexandre, 15, 7 à 9 ; Diodore XVII, 17 et 18)."
      },
      {
        "lon": 27.237,
        "lat": 40.2926,
        "label": "Bataille du Granique",
        "year": -333,
        "month": 5,
        "certainty": "attested",
        "note": "Victoire sur les satrapes d'Asie Mineure au passage du fleuve, au mois de Daisios selon Plutarque (Alexandre, 16, 2), vers mai ou juin 334 (Arrien I, 13 à 16 ; Diodore XVII, 19 à 21) ; champ de bataille situé près de Biga."
      },
      {
        "lon": 28.0403,
        "lat": 38.4883,
        "label": "Sardes",
        "year": -333,
        "month": 6,
        "certainty": "attested",
        "note": "La capitale de la Lydie et sa citadelle sont livrées sans combat par Mithrénès (Arrien I, 17, 3 à 8 ; Diodore XVII, 21, 7)."
      },
      {
        "lon": 27.2788,
        "lat": 37.5305,
        "label": "Siège de Milet",
        "year": -333,
        "month": 7,
        "certainty": "attested",
        "note": "Milet est prise d'assaut pendant l'été, la flotte grecque bloquant l'accès de la flotte perse (Arrien I, 18, 3 à 19, 11 ; Diodore XVII, 22)."
      },
      {
        "lon": 27.4222,
        "lat": 37.0404,
        "label": "Siège d'Halicarnasse",
        "year": -333,
        "month": 9,
        "certainty": "attested",
        "note": "Long siège d'automne contre Memnon de Rhodes, qui évacue la ville en laissant des garnisons dans les citadelles (Arrien I, 20, 2 à 23, 6 ; Diodore XVII, 23 à 27)."
      },
      {
        "lon": 30.5522,
        "lat": 36.5235,
        "label": "Phasélis",
        "year": -332,
        "month": 1,
        "certainty": "attested",
        "note": "Campagne d'hiver 334/333 en Lycie et en Pamphylie ; Phasélis se rallie et Alexandre longe la côte au pied du mont Climax (Arrien I, 24, 5 à 26, 2 ; Plutarque, Alexandre, 17, 6 à 8)."
      },
      {
        "lon": 30.1716,
        "lat": 38.0701,
        "label": "Kelainai",
        "year": -332,
        "month": 3,
        "certainty": "attested",
        "note": "La citadelle de la capitale phrygienne capitule ; Antigone le Borgne reçoit la satrapie de Phrygie (Arrien I, 29, 1 à 3 ; Quinte-Curce III, 1, 1 à 8)."
      },
      {
        "lon": 31.9785,
        "lat": 39.6503,
        "label": "Gordion, le nœud gordien",
        "year": -332,
        "month": 4,
        "certainty": "attested",
        "note": "L'armée se regroupe au printemps 333 à Gordion, où Alexandre tranche ou dénoue le nœud du char de Gordias (Arrien I, 29, 3 et II, 3, 1 à 8 ; Plutarque, Alexandre, 18, 2 à 4 ; Quinte-Curce III, 1, 14 à 18)."
      },
      {
        "lon": 34.8965,
        "lat": 36.914,
        "label": "Tarse",
        "year": -332,
        "month": 9,
        "certainty": "attested",
        "note": "Après le passage des Portes ciliciennes, Alexandre tombe gravement malade après un bain dans le Cydnos (Arrien II, 4, 7 à 11 ; Plutarque, Alexandre, 19 ; Quinte-Curce III, 5 et 6)."
      },
      {
        "lon": 36.2283,
        "lat": 36.7494,
        "label": "Bataille d'Issos",
        "year": -332,
        "month": 11,
        "certainty": "debated",
        "note": "Victoire sur Darius III au bord du Pinaros, au mois de Maimaktérion de l'archontat de Nicocratès (Arrien II, 6 à 11, en particulier 11, 10 ; Diodore XVII, 32 à 36 ; Quinte-Curce III, 8 à 11) ; le Pinaros est identifié au Payas ou au Deli Çay selon les auteurs, point Pleiades du Payas."
      },
      {
        "lon": 35.2018,
        "lat": 33.2693,
        "label": "Siège de Tyr",
        "year": -331,
        "month": 7,
        "certainty": "attested",
        "note": "Sept mois de siège et une digue jetée jusqu'à l'île ; la ville tombe au mois d'Hécatombaion de l'archontat de Nikétès, en juillet ou en août 332 (Arrien II, 15, 6 à 24, 6 ; Diodore XVII, 40 à 46 ; Quinte-Curce IV, 2 à 4)."
      },
      {
        "lon": 34.4517,
        "lat": 31.5202,
        "label": "Siège de Gaza",
        "year": -331,
        "month": 10,
        "certainty": "attested",
        "note": "Deux mois de siège à l'automne 332, Alexandre y est blessé à l'épaule (Arrien II, 25, 4 à 27, 7 ; Quinte-Curce IV, 6, 7 à 30 ; Plutarque, Alexandre, 25, 4 et 5)."
      },
      {
        "lon": 31.2551,
        "lat": 29.8495,
        "label": "Memphis",
        "year": -331,
        "month": 12,
        "certainty": "attested",
        "note": "Entrée en Égypte par Péluse et arrivée à Memphis à la fin de 332, où Alexandre sacrifie au taureau Apis (Arrien III, 1, 1 à 4 ; Quinte-Curce IV, 7, 1 à 5)."
      },
      {
        "lon": 29.9098,
        "lat": 31.2014,
        "label": "Fondation d'Alexandrie",
        "year": -330,
        "month": 1,
        "certainty": "debated",
        "note": "Fondation près du lac Maréotis : avant le voyage à l'oasis d'Ammon selon Arrien (III, 1, 5 à 2, 2), ordre suivi ici, après selon Diodore (XVII, 52), Quinte-Curce (IV, 8, 1 et 2) et Plutarque (Alexandre, 26, 3 à 10) ; le Roman d'Alexandre donne le 25 Tybi, soit le 7 avril 331."
      },
      {
        "lon": 27.2368,
        "lat": 31.3501,
        "label": "Paraitonion",
        "year": -330,
        "month": 2,
        "certainty": "attested",
        "note": "Marche le long de la côte sur 1 600 stades jusqu'à Paraitonion, avant de piquer au sud vers l'oasis (Arrien III, 3, 3)."
      },
      {
        "lon": 25.5435,
        "lat": 29.2052,
        "label": "Oasis d'Ammon (Siwa)",
        "year": -330,
        "month": 2,
        "certainty": "attested",
        "note": "Consultation de l'oracle d'Ammon, qui salue Alexandre comme fils du dieu, au début de 331 (Arrien III, 3, 1 à 4, 5 ; Plutarque, Alexandre, 27 ; Diodore XVII, 49 à 51 ; Quinte-Curce IV, 7, 5 à 32)."
      },
      {
        "lon": 31.2551,
        "lat": 29.8495,
        "label": "Retour à Memphis",
        "year": -330,
        "month": 4,
        "certainty": "attested",
        "note": "Retour à Memphis par la route directe selon Ptolémée, par le même chemin selon Aristobule ; organisation de l'Égypte au printemps 331 (Arrien III, 4, 5 et 5, 1 à 7)."
      },
      {
        "lon": 35.2018,
        "lat": 33.2693,
        "label": "Tyr, second passage",
        "year": -330,
        "month": 5,
        "certainty": "attested",
        "note": "Sacrifices et concours à Tyr avant la marche vers l'Euphrate (Arrien III, 6, 1)."
      },
      {
        "lon": 38.2,
        "lat": 36.4,
        "label": "Passage de l'Euphrate à Thapsaque",
        "year": -330,
        "month": 7,
        "certainty": "debated",
        "note": "Passage sur deux ponts au mois d'Hécatombaion de l'archontat d'Aristophanès (Arrien III, 7, 1 et 2) ; Thapsaque n'est pas localisée (point Pleiades 674270 sans coordonnées fiables), point indicatif entre Djerablous et Raqqa."
      },
      {
        "lon": 43.4943,
        "lat": 36.5733,
        "label": "Bataille de Gaugamèles",
        "year": -330,
        "month": 10,
        "certainty": "attested",
        "note": "Victoire décisive sur Darius III onze jours après l'éclipse de lune du 20 septembre 331, soit le 1er octobre (Arrien III, 7, 6 et 8 à 15, en particulier 15, 7 ; Plutarque, Alexandre, 31 à 33 ; Diodore XVII, 53 à 61)."
      },
      {
        "lon": 44.425,
        "lat": 32.5373,
        "label": "Babylone",
        "year": -330,
        "month": 10,
        "certainty": "attested",
        "note": "Entrée solennelle fin octobre 331, confirmée par un journal astronomique babylonien ; Mazaios garde la satrapie (Arrien III, 16, 3 à 5 ; Quinte-Curce V, 1, 17 à 23 ; Diodore XVII, 64, 3 à 6)."
      },
      {
        "lon": 48.2535,
        "lat": 32.1899,
        "label": "Suse",
        "year": -330,
        "month": 12,
        "certainty": "attested",
        "note": "Atteinte en vingt jours depuis Babylone ; Alexandre s'empare d'un trésor de 50 000 talents (Arrien III, 16, 6 et 7 ; Diodore XVII, 65 et 66)."
      },
      {
        "lon": 51.9099,
        "lat": 30.0932,
        "label": "Portes persiques",
        "year": -329,
        "month": 1,
        "certainty": "debated",
        "note": "Le satrape Ariobarzane barre le défilé ; Alexandre le contourne par un sentier de montagne en janvier 330 (Arrien III, 18, 2 à 9 ; Quinte-Curce V, 3, 16 à 4, 34 ; Diodore XVII, 68) ; défilé identifié au Tang-e Meyran ou à d'autres passes selon les auteurs."
      },
      {
        "lon": 52.8904,
        "lat": 29.9352,
        "label": "Persépolis",
        "year": -329,
        "month": 1,
        "certainty": "attested",
        "note": "Prise et pillage de la ville, séjour de quatre mois et incendie des palais au printemps 330 (Arrien III, 18, 10 à 12 ; Plutarque, Alexandre, 37 et 38 ; Diodore XVII, 70 à 72 ; Quinte-Curce V, 6 et 7)."
      },
      {
        "lon": 48.5164,
        "lat": 34.8056,
        "label": "Ecbatane",
        "year": -329,
        "month": 6,
        "certainty": "attested",
        "note": "Darius s'est enfui ; Alexandre renvoie les contingents alliés grecs et laisse Parménion et le trésor à Ecbatane (Arrien III, 19, 5 à 8)."
      },
      {
        "lon": 54.0383,
        "lat": 35.9611,
        "label": "Hécatompylos",
        "year": -329,
        "month": 7,
        "certainty": "debated",
        "note": "Darius III est assassiné par Bessos en juillet 330 au cours de la poursuite (Arrien III, 21, 10 à 22, 1) ; Quinte-Curce (VI, 2, 15) et Diodore (XVII, 75, 1) font camper l'armée à Hécatompylos, identifiée à Shahr-i Qumis."
      },
      {
        "lon": 54.4195,
        "lat": 36.8128,
        "label": "Zadracarta",
        "year": -329,
        "month": 8,
        "certainty": "debated",
        "note": "Plus grande ville d'Hyrcanie, où Alexandre séjourne quinze jours (Arrien III, 23, 6 et 25, 1) ; identifiée près de Gorgan (Qal'eh Khandan), d'autres proposent Sari."
      },
      {
        "lon": 62.1891,
        "lat": 34.3456,
        "label": "Alexandrie d'Arie (Hérat)",
        "year": -329,
        "month": 9,
        "certainty": "debated",
        "note": "Révolte du satrape Satibarzanès et marche sur Artakoana, capitale de l'Arie (Arrien III, 25, 5 à 7 ; Quinte-Curce VI, 6, 20 à 34) ; la fondation d'une Alexandrie à Hérat n'est connue que par les géographes (Pline, Histoire naturelle, VI, 61)."
      },
      {
        "lon": 62.1117,
        "lat": 32.3821,
        "label": "Phrada (Farah)",
        "year": -329,
        "month": 10,
        "certainty": "traditional",
        "note": "Capitale de la Drangiane, où éclate l'affaire de Philotas, suivie de l'exécution de Parménion à l'automne 330 (Arrien III, 26 et 27 ; Plutarque, Alexandre, 48 et 49 ; Quinte-Curce VI, 7 à VII, 2) ; renommée Prophthasia, identifiée à Farah."
      },
      {
        "lon": 65.6597,
        "lat": 31.601,
        "label": "Alexandrie d'Arachosie (Kandahar)",
        "year": -329,
        "month": 12,
        "certainty": "debated",
        "note": "Traversée de l'Arachosie pendant l'hiver 330/329 (Arrien III, 28, 1) ; la fondation d'une Alexandrie à Kandahar, admise par la plupart des modernes, repose sur des sources tardives (Isidore de Charax, Étapes parthes, 19)."
      },
      {
        "lon": 69.3105,
        "lat": 34.9925,
        "label": "Alexandrie du Caucase (vallée de Kaboul)",
        "year": -328,
        "month": 3,
        "certainty": "debated",
        "note": "Fondation au pied de l'Hindou Kouch avant sa traversée au printemps 329 (Arrien III, 28, 4 ; Quinte-Curce VII, 3, 23 ; Diodore XVII, 83, 1), localisée à Begram ou plus au nord, vers Charikar."
      },
      {
        "lon": 66.9011,
        "lat": 36.7679,
        "label": "Bactres",
        "year": -328,
        "month": 5,
        "certainty": "attested",
        "note": "Prise de Bactres après la traversée de l'Hindou Kouch ; Bessos s'enfuit au-delà de l'Oxus (Arrien III, 29, 1 à 4 ; Quinte-Curce VII, 4, 31 et 32)."
      },
      {
        "lon": 66.9472,
        "lat": 39.6565,
        "label": "Maracanda (Samarcande)",
        "year": -328,
        "month": 7,
        "certainty": "attested",
        "note": "Capitale de la Sogdiane, atteinte à l'été 329 après la capture de Bessos (Arrien III, 30, 6 ; Quinte-Curce VII, 6, 10)."
      },
      {
        "lon": 69.6406,
        "lat": 40.2648,
        "label": "Alexandrie Eschatè (Khodjent)",
        "year": -328,
        "month": 8,
        "certainty": "traditional",
        "note": "L'« Alexandrie la plus lointaine », fortifiée en vingt jours sur l'Iaxarte (Arrien IV, 1, 3 et 4, 1 ; Quinte-Curce VII, 6, 25 à 27), est identifiée à Khodjent."
      },
      {
        "lon": 66.8313,
        "lat": 39.0522,
        "label": "Nautaka, quartiers d'hiver",
        "year": -327,
        "month": 12,
        "certainty": "traditional",
        "note": "Après deux ans de guérilla contre Spitaménès, l'armée hiverne à Nautaka en 328/327 (Arrien IV, 18, 1 et 2) ; site identifié à Shahrisabz."
      },
      {
        "lon": 66.9011,
        "lat": 36.7679,
        "label": "Bactres, départ pour l'Inde",
        "year": -326,
        "month": 5,
        "certainty": "attested",
        "note": "Après la prise du Rocher sogdien et le mariage avec Roxane, Alexandre quitte Bactres à la fin du printemps 327 (Arrien IV, 22, 3)."
      },
      {
        "lon": 69.3105,
        "lat": 34.9925,
        "label": "Alexandrie du Caucase, second passage",
        "year": -326,
        "month": 6,
        "certainty": "debated",
        "note": "Retraversée de l'Hindou Kouch en dix jours et réorganisation de la ville (Arrien IV, 22, 4 et 5)."
      },
      {
        "lon": 71.6859,
        "lat": 34.7619,
        "label": "Massaga",
        "year": -326,
        "month": 11,
        "certainty": "debated",
        "note": "Siège de la capitale des Assacènes, à l'hiver 327/326 (Arrien IV, 26 et 27 ; Quinte-Curce VIII, 10, 22 à 36) ; localisation discutée entre le bas Dir et le Swat."
      },
      {
        "lon": 73.2846,
        "lat": 34.7219,
        "label": "Aornos",
        "year": -325,
        "month": 2,
        "certainty": "debated",
        "note": "Prise du rocher réputé imprenable même pour Héraclès (Arrien IV, 28 à 30 ; Diodore XVII, 85 ; Quinte-Curce VIII, 11) ; identifié à Pir-Sar par Aurel Stein (1926), d'autres proposent l'Ilam ou l'Una."
      },
      {
        "lon": 72.8152,
        "lat": 33.7457,
        "label": "Taxila",
        "year": -325,
        "month": 4,
        "certainty": "attested",
        "note": "Accueil par le roi Taxilès, allié d'Alexandre, au printemps 326 (Arrien V, 3, 5 et 6 et 8, 2 et 3 ; Plutarque, Alexandre, 59, 1 à 5 ; Quinte-Curce VIII, 12)."
      },
      {
        "lon": 73.4895,
        "lat": 32.6312,
        "label": "Bataille de l'Hydaspe",
        "year": -325,
        "month": 5,
        "certainty": "debated",
        "note": "Victoire sur le roi Pôros au mois de Mounichion de l'archontat d'Hégémon (Arrien V, 9 à 19, en particulier 19, 3 ; Plutarque, Alexandre, 60) ; champ de bataille placé près de Jhelum ou de Jalalpur, point Pleiades de Nicée, fondée sur le lieu de la victoire."
      },
      {
        "lon": 75.5472,
        "lat": 31.7301,
        "label": "Hyphase, refus de l'armée",
        "year": -325,
        "month": 8,
        "certainty": "debated",
        "note": "Après soixante-dix jours de pluies de mousson, l'armée refuse d'aller plus loin ; Alexandre élève douze autels et fait demi-tour à l'été 326 (Arrien V, 25 à 29 ; Diodore XVII, 93 à 95 ; Plutarque, Alexandre, 62) ; le lieu exact est inconnu, point Pleiades du fleuve."
      },
      {
        "lon": 73.4474,
        "lat": 32.6889,
        "label": "Bucéphalie, départ de la flotte",
        "year": -325,
        "month": 11,
        "certainty": "debated",
        "note": "La flotte construite sur l'Hydaspe descend le fleuve vers l'Indus à partir de novembre 326, peu avant le coucher des Pléiades (Arrien VI, 1 à 3 ; Strabon XV, 1, 17) ; site de Bucéphalie non retrouvé."
      },
      {
        "lon": 68.0651,
        "lat": 24.7224,
        "label": "Patala",
        "year": -324,
        "month": 7,
        "certainty": "debated",
        "note": "Arrivée au sommet du delta de l'Indus vers juillet 325, après la campagne contre les Malles où Alexandre est grièvement blessé (Arrien VI, 17 et 18 ; Diodore XVII, 104) ; Patala est placée près de Hyderabad ou plus au sud."
      },
      {
        "lon": 66.4597,
        "lat": 26.1307,
        "label": "Alexandrie des Orites (Rhambakia)",
        "year": -324,
        "month": 9,
        "certainty": "debated",
        "note": "Alexandre fonde une ville à Rhambakia, le plus grand village des Orites, avant d'entrer en Gédrosie (Arrien VI, 21, 5 et 22, 3) ; site non retrouvé."
      },
      {
        "lon": 63.05,
        "lat": 26.0,
        "label": "Désert de Gédrosie",
        "year": -324,
        "month": 10,
        "certainty": "debated",
        "note": "Soixante jours de marche dans le désert, où une grande partie de l'armée et du train périt (Arrien VI, 22, 4 à 26, 5 ; Plutarque, Alexandre, 66, 4 à 7 ; Strabon XV, 2, 5 à 7) ; tracé discuté, point indicatif dans la vallée du Kech."
      },
      {
        "lon": 60.46,
        "lat": 27.2,
        "label": "Poura",
        "year": -324,
        "month": 11,
        "certainty": "traditional",
        "note": "Résidence royale des Gédrosiens, atteinte à la fin de 325 au sortir du désert (Arrien VI, 24, 1) ; identifiée à Bampur, non localisée dans Pleiades (point indicatif)."
      },
      {
        "lon": 57.1522,
        "lat": 27.9683,
        "label": "Carmanie, retrouvailles avec Néarque",
        "year": -324,
        "month": 12,
        "certainty": "debated",
        "note": "L'amiral Néarque, venu par mer depuis l'Indus, rejoint Alexandre à cinq jours de la côte vers décembre 325 (Arrien VI, 27 et 28 ; Arrien, L'Inde, 33 à 36 ; Diodore XVII, 106) ; point Pleiades d'Alexandrie de Carmanie, vers Golashkerd."
      },
      {
        "lon": 53.1743,
        "lat": 30.1952,
        "label": "Pasargades, tombeau de Cyrus",
        "year": -323,
        "month": 2,
        "certainty": "attested",
        "note": "Alexandre trouve le tombeau de Cyrus pillé et le fait restaurer par Aristobule au début de 324 (Arrien VI, 29, 1 à 11 ; Plutarque, Alexandre, 69, 3 à 5 ; Strabon XV, 3, 7)."
      },
      {
        "lon": 48.2535,
        "lat": 32.1899,
        "label": "Suse, noces collectives",
        "year": -323,
        "month": 4,
        "certainty": "attested",
        "note": "Au printemps 324, Alexandre épouse Stateira et Parysatis et marie quatre-vingts Compagnons à des femmes de l'aristocratie perse (Arrien VII, 4, 4 à 8 ; Plutarque, Alexandre, 70, 3 ; Diodore XVII, 107, 6)."
      },
      {
        "lon": 44.7015,
        "lat": 33.1844,
        "label": "Opis, mutinerie",
        "year": -323,
        "month": 7,
        "certainty": "debated",
        "note": "Mutinerie des Macédoniens contre le renvoi des vétérans, suivie du banquet de réconciliation à l'été 324 (Arrien VII, 8 à 12 ; Plutarque, Alexandre, 71 ; Diodore XVII, 109) ; site d'Opis discuté sur le Tigre."
      },
      {
        "lon": 48.5164,
        "lat": 34.8056,
        "label": "Ecbatane, mort d'Héphaistion",
        "year": -323,
        "month": 10,
        "certainty": "attested",
        "note": "Héphaistion meurt pendant les fêtes d'Ecbatane à l'automne 324 (Arrien VII, 14, 1 à 10 ; Plutarque, Alexandre, 72 ; Diodore XVII, 110, 7 et 8)."
      },
      {
        "lon": 44.425,
        "lat": 32.5373,
        "label": "Babylone, mort d'Alexandre",
        "year": -322,
        "month": 6,
        "certainty": "attested",
        "note": "Alexandre meurt dans le palais de Nabuchodonosor le 10 ou le 11 juin 323, d'après un journal astronomique babylonien (Arrien VII, 25 à 28 ; Plutarque, Alexandre, 75 et 76 ; Diodore XVII, 116 à 118)."
      }
    ],
    "sources": [
      "Arrien, Anabase d'Alexandre, livres I à VII",
      "Arrien, L'Inde, 18 à 42 (voyage de Néarque)",
      "Plutarque, Vie d'Alexandre, 11 à 77",
      "Diodore de Sicile, Bibliothèque historique, livre XVII",
      "Quinte-Curce, Histoires d'Alexandre le Grand, livres III à X",
      "Strabon, Géographie, XV, 1 et 2 (Inde, Gédrosie et Carmanie)",
      "A. B. Bosworth, Conquest and Empire. The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988",
      "D. W. Engels, Alexander the Great and the Logistics of the Macedonian Army, Berkeley, University of California Press, 1978",
      "A. Stein, On Alexander's Track to the Indus, Londres, Macmillan, 1929",
      "Pleiades, coordonnées des lieux (point représentatif) : https://pleiades.stoa.org"
    ]
  },
  {
    "id": "retraite-des-dix-mille",
    "title": "Expédition et retraite des Dix Mille",
    "summary": "Engagés par Cyrus le Jeune contre son frère Artaxerxès II, plus de 10 000 mercenaires grecs remontent de Sardes jusqu'à Counaxa, près de Babylone, au printemps et à l'été 401 av. J.-C. Cyrus tué et leurs stratèges massacrés, ils regagnent la mer Noire par le Tigre, les monts des Carduques et les neiges d'Arménie, sous la conduite de Xénophon notamment, puis longent la côte jusqu'à Byzance à l'automne 400 av. J.-C.",
    "from": -400,
    "to": -399,
    "waypoints": [
      {
        "lon": 28.0403,
        "lat": 38.4883,
        "label": "Départ de Sardes",
        "year": -400,
        "month": 3,
        "certainty": "attested",
        "note": "Cyrus part de Sardes au printemps 401 sous prétexte de châtier les Pisidiens (Xénophon, Anabase, I, 2, 1 à 5), mois approximatif."
      },
      {
        "lon": 30.1716,
        "lat": 38.0701,
        "label": "Kelainai",
        "year": -400,
        "month": 4,
        "certainty": "attested",
        "note": "Séjour de trente jours ; revue de 11 000 hoplites et 2 000 peltastes grecs (Xénophon, Anabase, I, 2, 7 à 9)."
      },
      {
        "lon": 34.8965,
        "lat": 36.914,
        "label": "Tarse",
        "year": -400,
        "month": 6,
        "certainty": "attested",
        "note": "Vingt jours d'arrêt : les Grecs, qui devinent la vraie cible, refusent d'avancer avant d'être convaincus par Cléarque (Xénophon, Anabase, I, 2, 23 à 3, 21)."
      },
      {
        "lon": 36.1104,
        "lat": 36.5658,
        "label": "Myriandos",
        "year": -400,
        "month": 7,
        "certainty": "traditional",
        "note": "Port phénicien du golfe d'Issos, d'où l'armée quitte la côte pour l'Euphrate (Xénophon, Anabase, I, 4, 6 et 7)."
      },
      {
        "lon": 38.2,
        "lat": 36.4,
        "label": "Passage de l'Euphrate à Thapsaque",
        "year": -400,
        "month": 8,
        "certainty": "debated",
        "note": "Cyrus révèle le but de l'expédition ; l'armée passe l'Euphrate à gué (Xénophon, Anabase, I, 4, 11 à 18) ; Thapsaque n'est pas localisée, point indicatif entre Djerablous et Raqqa."
      },
      {
        "lon": 44.0,
        "lat": 33.25,
        "label": "Bataille de Counaxa",
        "year": -400,
        "month": 9,
        "certainty": "debated",
        "note": "Les Grecs l'emportent sur leur aile, mais Cyrus est tué en chargeant son frère (Xénophon, Anabase, I, 8, 1 à 10, 19 ; Diodore XIV, 22 à 24) ; Counaxa, à 500 stades de Babylone selon Plutarque (Artaxerxès, 8, 2), n'est pas localisée, point indicatif."
      },
      {
        "lon": 44.7015,
        "lat": 33.1844,
        "label": "Passage du Tigre et Opis",
        "year": -400,
        "month": 10,
        "certainty": "debated",
        "note": "Escortés par Tissapherne, les Grecs franchissent le Tigre à Sittakè sur un pont de 37 bateaux, puis passent à Opis (Xénophon, Anabase, II, 4, 13 à 25) ; site d'Opis discuté."
      },
      {
        "lon": 43.3283,
        "lat": 36.0979,
        "label": "Larissa (Nimrud)",
        "year": -400,
        "month": 10,
        "certainty": "traditional",
        "note": "Après l'arrestation des stratèges au bord du Grand Zab (Xénophon, Anabase, II, 5, 31 à 6, 1), Xénophon et les nouveaux chefs mènent la retraite le long du Tigre jusqu'à la ville déserte de Larissa, identifiée à Nimrud (III, 4, 7 à 9) ; point Pleiades du palais central de Kalhu."
      },
      {
        "lon": 43.1371,
        "lat": 36.3356,
        "label": "Mespila (Mossoul)",
        "year": -400,
        "month": 11,
        "certainty": "traditional",
        "note": "Grande ville abandonnée aux murailles de pierre, identifiée à Ninive ou à Mossoul (Xénophon, Anabase, III, 4, 10 à 12)."
      },
      {
        "lon": 42.1763,
        "lat": 37.5564,
        "label": "Monts des Carduques",
        "year": -400,
        "month": 11,
        "certainty": "debated",
        "note": "Sept jours de combats dans les montagnes du Kurdistan actuel contre les Carduques (Xénophon, Anabase, IV, 1, 2 à 3, 2) ; itinéraire exact discuté, point Pleiades du peuple."
      },
      {
        "lon": 42.3421,
        "lat": 37.9181,
        "label": "Passage du Kentritès",
        "year": -400,
        "month": 11,
        "certainty": "traditional",
        "note": "Passage en force du fleuve frontière de l'Arménie, identifié au Botan (Xénophon, Anabase, IV, 3, 1 à 34)."
      },
      {
        "lon": 41.5,
        "lat": 38.5,
        "label": "Neiges d'Arménie",
        "year": -400,
        "month": 12,
        "certainty": "debated",
        "note": "Marche dans la neige après la source du Téléboas, au cœur de l'hiver 401/400 (Xénophon, Anabase, IV, 4, 3 à 5, 36) ; point Pleiades approximatif du Téléboas."
      },
      {
        "lon": 41.6663,
        "lat": 39.9847,
        "label": "Gymnias",
        "year": -399,
        "month": 1,
        "certainty": "debated",
        "note": "Ville où un guide promet de conduire l'armée en vue de la mer en cinq jours (Xénophon, Anabase, IV, 7, 19 et 20) ; localisation discutée."
      },
      {
        "lon": 39.5,
        "lat": 40.5,
        "label": "Mont Thêchès : « La mer ! La mer ! »",
        "year": -399,
        "month": 2,
        "certainty": "debated",
        "note": "Du sommet, les soldats aperçoivent le Pont-Euxin et crient « Thalatta ! Thalatta ! » (Xénophon, Anabase, IV, 7, 21 à 27) ; montagne non identifiée, point Pleiades approximatif."
      },
      {
        "lon": 39.7233,
        "lat": 41.0043,
        "label": "Trapézonte",
        "year": -399,
        "month": 2,
        "certainty": "attested",
        "note": "Arrivée à la colonie grecque de Trapézonte, où l'armée sacrifie et organise des jeux (Xénophon, Anabase, IV, 8, 22 à 28)."
      },
      {
        "lon": 37.8704,
        "lat": 40.9984,
        "label": "Cotyora",
        "year": -399,
        "month": 5,
        "certainty": "attested",
        "note": "Séjour de quarante-cinq jours chez les Sinopéens de Cotyora (Xénophon, Anabase, V, 5, 3 à 5)."
      },
      {
        "lon": 35.143,
        "lat": 42.0258,
        "label": "Sinope",
        "year": -399,
        "month": 6,
        "certainty": "attested",
        "note": "L'armée gagne Sinope par mer et élit le Spartiate Chirisophe commandant unique (Xénophon, Anabase, VI, 1, 15 à 32)."
      },
      {
        "lon": 31.4174,
        "lat": 41.2833,
        "label": "Héraclée du Pont",
        "year": -399,
        "month": 7,
        "certainty": "attested",
        "note": "L'armée se divise en trois corps après une dispute sur la rançon à exiger des Héracléotes (Xénophon, Anabase, VI, 2, 1 à 16)."
      },
      {
        "lon": 30.1965,
        "lat": 41.1435,
        "label": "Port de Calpè",
        "year": -399,
        "month": 7,
        "certainty": "traditional",
        "note": "Les trois corps se réunissent au port de Calpè, en Thrace d'Asie (Xénophon, Anabase, VI, 2, 13 et 4, 1 à 6)."
      },
      {
        "lon": 29.0129,
        "lat": 41.0206,
        "label": "Chrysopolis",
        "year": -399,
        "month": 9,
        "certainty": "attested",
        "note": "Arrivée sur le Bosphore, face à Byzance, où l'armée vend son butin (Xénophon, Anabase, VI, 6, 38)."
      },
      {
        "lon": 28.9739,
        "lat": 41.0059,
        "label": "Byzance",
        "year": -399,
        "month": 10,
        "certainty": "attested",
        "note": "Passée en Europe à l'automne 400, l'armée manque de piller Byzance avant de passer au service du Thrace Seuthès (Xénophon, Anabase, VII, 1, 7 à 39), mois approximatif."
      }
    ],
    "sources": [
      "Xénophon, Anabase, livres I à VII",
      "Diodore de Sicile, Bibliothèque historique, XIV, 19 à 31",
      "Plutarque, Vie d'Artaxerxès, 6 à 13",
      "J. Lendle, Kommentar zu Xenophons Anabasis (Bücher 1 bis 7), Darmstadt, Wissenschaftliche Buchgesellschaft, 1995",
      "R. Lane Fox (dir.), The Long March. Xenophon and the Ten Thousand, New Haven, Yale University Press, 2004",
      "J. W. I. Lee, A Greek Army on the March. Soldiers and Survival in Xenophon's Anabasis, Cambridge, Cambridge University Press, 2007",
      "Pleiades, coordonnées des lieux (point représentatif) : https://pleiades.stoa.org"
    ]
  }
]
