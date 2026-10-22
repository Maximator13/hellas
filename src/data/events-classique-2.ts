import type { HistoricalEvent } from './schema.ts'

const XENOPHON = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0206'
const DIODORE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0084'
const PAUSANIAS = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0160'
const STRABON = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0198'
const PLUTARQUE = 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives'

export const events: HistoricalEvent[] = [
  {
    "id": "regime-des-trente-et-retour-de-la-democratie",
    "title": "Les Trente et le retour de la démocratie à Athènes",
    "start": -403,
    "end": -402,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "critias",
      "thrasybule",
      "theramene",
      "lysandre"
    ],
    "summary": "Après la capitulation d'Athènes, en 404, Lysandre fait installer un gouvernement de trente oligarques, les Trente, qui exécutent ou chassent leurs adversaires. Les démocrates exilés de Thrasybule reprennent le Pirée en 403 ; la démocratie est restaurée à l'automne, avec une amnistie générale.",
    "body": "**La terreur des Trente.** À l'été 404, sous la pression de Lysandre, l'assemblée confie le pouvoir à trente hommes chargés de rédiger de nouvelles lois. Menés par Critias, ils s'appuient sur une garnison spartiate, réservent les droits politiques à 3 000 citoyens et font exécuter sans jugement des métèques riches et des opposants ; Théramène, qui proteste, est lui-même mis à mort. Selon Aristote, au moins 1 500 personnes périssent.\n\n**Le retour des démocrates.** Pendant l'hiver 404/403, Thrasybule s'empare de la forteresse de Phylé avec environ soixante-dix exilés selon Xénophon, puis du Pirée. Critias est tué au combat de Mounychie au printemps 403. Le roi spartiate Pausanias, rival de Lysandre, arbitre alors une réconciliation : les démocrates rentrent en ville, et les derniers oligarques se retirent à Éleusis, réintégrée en 401/400.\n\n**L'amnistie.** Les Athéniens jurent de « ne pas rappeler les maux passés » : seuls les Trente et quelques magistrats sont exclus du pardon. Cette amnistie, l'une des premières connues, a été largement respectée, même si les procès de la décennie suivante, dont celui de Socrate, portent la trace de ces années.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "II, 3, 11 à II, 4, 43",
        "url": `${XENOPHON}:book=2:chapter=3`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Constitution des Athéniens",
        "locus": "34 à 40"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIV, 3 à 6 et 32 à 33",
        "url": `${DIODORE}:book=14:chapter=3`
      },
      {
        "kind": "modern",
        "author": "Peter Krentz",
        "work": "The Thirty at Athens, Ithaca, Cornell University Press, 1982"
      }
    ]
  },
  {
    "id": "proces-et-mort-de-socrate",
    "title": "Procès et mort de Socrate",
    "start": -398,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Le procès a lieu sous l'archonte Lachès (400/399), au printemps 399 ; le jour exact n'est pas connu.",
    "era": "classique",
    "track": "athenes",
    "category": "society",
    "importance": 1,
    "placeId": "athenes",
    "people": [
      "socrate",
      "platon",
      "xenophon"
    ],
    "summary": "Au printemps 399, Socrate, âgé de 70 ans, est accusé d'impiété et de corruption de la jeunesse. Un tribunal de 500 ou 501 citoyens le condamne à mort ; il boit le poison un mois plus tard, après avoir refusé de s'enfuir. Sa mort, racontée par Platon, devient l'un des récits fondateurs de la philosophie.",
    "body": "**L'accusation.** Selon l'acte d'accusation, que Diogène Laërce dit encore conservé de son temps, Socrate « ne reconnaît pas les dieux de la cité, introduit des divinités nouvelles et corrompt la jeunesse » ; les accusateurs sont Mélétos, Anytos et Lycon. Socrate se défend lui-même. D'après l'Apologie de Platon, il est déclaré coupable à une trentaine de voix près ; invité à proposer sa peine, il suggère d'abord d'être nourri au prytanée, ce qui aggrave le second vote.\n\n**La mort.** L'exécution est retardée d'environ trente jours, le temps du retour du navire sacré envoyé à Délos, pendant lequel aucune mise à mort n'est permise. Socrate refuse l'évasion que lui propose son ami Criton et boit le poison, entouré de ses disciples ; Platon, absent ce jour-là, décrit la scène dans le Phédon. Le texte parle seulement du « poison » : l'identification avec la ciguë vient de la tradition.\n\n**Pourquoi ?** L'amnistie de 403 interdisait de poursuivre les actes politiques passés, mais Socrate avait eu pour proches Alcibiade et Critias, et Anytos était un chef démocrate : beaucoup d'historiens voient dans le procès une affaire politique autant que religieuse. Socrate n'ayant rien écrit, on ne le connaît que par Platon, Xénophon et la caricature d'Aristophane, qui ne concordent pas toujours.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Apologie de Socrate",
        "locus": "24b à 38b"
      },
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Phédon",
        "locus": "116a à 118a"
      },
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Mémorables",
        "locus": "I, 1, 1 et IV, 8, 2"
      },
      {
        "kind": "ancient",
        "author": "Diogène Laërce",
        "work": "Vies et doctrines des philosophes illustres",
        "locus": "II, 40 à 44"
      },
      {
        "kind": "modern",
        "author": "Claude Mossé",
        "work": "Le Procès de Socrate, Bruxelles, Complexe, 1987"
      }
    ]
  },
  {
    "id": "bataille-de-counaxa",
    "title": "Bataille de Counaxa",
    "start": -400,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Date reconstruite d'après les étapes notées par Xénophon (fin de l'été ou début de l'automne 401) ; l'emplacement exact de Counaxa n'est pas identifié.",
    "era": "classique",
    "track": "perse",
    "category": "war",
    "importance": 2,
    "placeId": "counaxa",
    "people": [
      "cyrus-le-jeune",
      "artaxerxes-ii",
      "clearque",
      "xenophon"
    ],
    "summary": "À la fin de l'été 401, au nord de Babylone, Cyrus le Jeune affronte son frère, le roi Artaxerxès II, pour le trône perse. Les mercenaires grecs de Cyrus enfoncent l'aile qui leur fait face, mais Cyrus, lancé contre son frère, est tué : sa mort transforme la victoire grecque en défaite.",
    "body": "**Une guerre de succession.** Satrape en Asie Mineure, Cyrus prépare sa révolte en recrutant, sous divers prétextes, 10 400 hoplites et 2 500 peltastes grecs selon Xénophon, commandés par l'exilé spartiate Cléarque. Parti de Sardes au printemps 401, il descend l'Euphrate jusqu'à Counaxa, à quelques dizaines de kilomètres au nord de Babylone. Xénophon prête au roi 1 200 000 hommes, chiffre impossible ; les modernes pensent à quelques dizaines de milliers de combattants de chaque côté.\n\n**La bataille.** Placés à droite, le long du fleuve, les Grecs mettent en fuite l'aile gauche royale presque sans pertes. Au centre, Cyrus charge avec 600 cavaliers vers son frère et le blesse, selon le médecin grec Ctésias, présent dans le camp royal, puis tombe sous les coups de l'escorte du roi. Les Grecs, vainqueurs de leur côté, apprennent le lendemain qu'ils n'ont plus ni chef ni cause.\n\n**Les sources.** Le récit de Xénophon, qui combattait parmi les mercenaires, reste la source principale ; Diodore et Plutarque, qui suit Ctésias, le complètent. La date exacte et l'emplacement du champ de bataille, sur l'Euphrate, ne sont connus qu'approximativement.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Anabase",
        "locus": "I, 7 à 10"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIV, 22 à 24",
        "url": `${DIODORE}:book=14:chapter=22`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Artaxerxès",
        "locus": "8 à 13",
        "url": `${PLUTARQUE}/Artaxerxes*.html`
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      }
    ]
  },
  {
    "id": "retraite-des-dix-mille",
    "title": "Retraite des Dix Mille",
    "start": -400,
    "end": -399,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "monde-grec",
    "category": "war",
    "importance": 2,
    "placeId": "trapezonte",
    "people": [
      "xenophon",
      "clearque",
      "tissapherne"
    ],
    "summary": "Après Counaxa, les mercenaires grecs de Cyrus, dont le satrape Tissapherne a fait arrêter les généraux par traîtrise, élisent de nouveaux chefs, parmi lesquels Xénophon. Ils remontent le Tigre, franchissent en plein hiver les montagnes du Kurdistan et de l'Arménie, et atteignent la mer Noire à Trapézonte au début de 400.",
    "body": "**Une armée sans chefs.** Quelques semaines après la bataille, Tissapherne invite Cléarque et les autres généraux à une négociation et les fait arrêter ; ils sont exécutés. Les Grecs élisent de nouveaux stratèges, dont le jeune Athénien Xénophon, et décident de rentrer par le nord, à travers des pays hostiles, sans guides sûrs ni ravitaillement assuré.\n\n**La marche.** Harcelés par les Carduques dans les montagnes, puis éprouvés par la neige en Arménie, ils arrivent au mont Théchès, d'où l'avant-garde aperçoit la mer et crie « Thalatta ! Thalatta ! » (« La mer ! La mer ! »). De Trapézonte, ils longent la côte jusqu'à Byzance, servent un prince thrace, puis sont engagés par Sparte contre la Perse au printemps 399. Lors d'une revue à Cérasonte, ils sont encore 8 600.\n\n**Une leçon pour les Grecs.** L'Anabase de Xénophon, écrite des années plus tard et parfois soupçonnée de grandir le rôle de son auteur, montre qu'une armée grecque peut traverser l'empire perse de part en part. L'orateur Isocrate en tire argument pour une grande expédition commune des Grecs, et l'on y voit souvent l'une des sources de l'ambition d'Agésilas puis d'Alexandre.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Anabase",
        "locus": "II, 5 à VII, 8 ; IV, 7, 21 à 26 ; V, 3, 3"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIV, 25 à 31",
        "url": `${DIODORE}:book=14:chapter=25`
      },
      {
        "kind": "modern",
        "author": "Robin Lane Fox (dir.)",
        "work": "The Long March: Xenophon and the Ten Thousand, New Haven, Yale University Press, 2004"
      }
    ]
  },
  {
    "id": "agesilas-en-asie",
    "title": "Campagnes d'Agésilas en Asie Mineure",
    "start": -395,
    "end": -393,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "sparte",
    "category": "war",
    "importance": 3,
    "placeId": "sardes",
    "people": [
      "agesilas-ii",
      "tissapherne",
      "pharnabaze",
      "lysandre"
    ],
    "summary": "De 396 à 394, le roi spartiate Agésilas II fait campagne en Asie Mineure pour défendre les cités grecques contre les satrapes perses. Vainqueur près de Sardes en 395, il doit rentrer au printemps 394, rappelé par la guerre que Thèbes, Athènes, Corinthe et Argos, aidées par l'or perse, viennent d'ouvrir contre Sparte.",
    "body": "**Une expédition panhellénique.** Sparte est en guerre avec la Perse depuis 400 pour protéger les cités d'Ionie. En 396, Agésilas, devenu roi avec l'appui de Lysandre, veut sacrifier à Aulis, comme Agamemnon avant la guerre de Troie ; les Béotiens interrompent le sacrifice, affront qu'il n'oubliera pas.\n\n**Les campagnes.** Au printemps 395, il marche sur Sardes et bat la cavalerie de Tissapherne près du Pactole ; le satrape, disgracié, est exécuté sur ordre du roi. Agésilas pille ensuite la satrapie de Pharnabaze, en Phrygie hellespontique. Le récit de Xénophon, ami et admirateur du roi, diffère de celui d'un historien anonyme conservé sur papyrus, les Helléniques d'Oxyrhynchos, sur le déroulement de la bataille de Sardes.\n\n**Le rappel.** La Perse finance les ennemis de Sparte en Grèce. Au printemps 394, Agésilas est rappelé ; Plutarque lui prête un mot sur les « archers » du Grand Roi qui le chassent d'Asie, les dariques d'or frappés à l'effigie d'un archer. Il rentre par l'Hellespont et la Thrace et bat les coalisés à Coronée en août 394.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "III, 4 ; IV, 1 ; IV, 2, 1 à 8",
        "url": `${XENOPHON}:book=3:chapter=4`
      },
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Agésilas",
        "locus": "I, 6 à 38"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Agésilas",
        "locus": "6 à 15",
        "url": `${PLUTARQUE}/Agesilaus*.html`
      },
      {
        "kind": "modern",
        "author": "Paul Cartledge",
        "work": "Agesilaos and the Crisis of Sparta, Londres, Duckworth, 1987"
      }
    ]
  },
  {
    "id": "guerre-de-corinthe",
    "title": "Guerre de Corinthe",
    "start": -394,
    "end": -386,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "corinthe",
    "category": "war",
    "importance": 2,
    "placeId": "corinthe",
    "people": [
      "agesilas-ii",
      "lysandre",
      "conon",
      "pharnabaze",
      "iphicrate"
    ],
    "summary": "De 395 à 387, Thèbes, Athènes, Corinthe et Argos, financées par la Perse, s'allient contre Sparte. Victorieuse sur terre à Némée et à Coronée, Sparte perd sa flotte à Cnide en 394, et Athènes relève ses Longs Murs. La guerre, qui s'enlise autour de l'isthme de Corinthe, s'achève par la paix du Roi.",
    "body": "**La coalition.** En 395, un conflit local entre Phocidiens et Locriens dresse Thèbes contre Sparte ; Lysandre est tué devant Haliarte. Athènes, Corinthe et Argos rejoignent Thèbes, avec l'argent perse apporté par le Rhodien Timocrate. En 394, Sparte bat les coalisés à Némée, puis Agésilas, revenu d'Asie, l'emporte à Coronée.\n\n**Sur mer.** En août 394, au large de Cnide, la flotte perse de Pharnabaze et de l'Athénien Conon détruit la flotte spartiate : l'empire maritime de Sparte s'effondre. Conon revient à Athènes en 393 et fait reconstruire les Longs Murs avec l'or perse. Autour de Corinthe, la guerre se poursuit ; en 390, près du port du Léchaion, les peltastes d'Iphicrate détruisent une unité d'hoplites spartiates (une more), dont environ 250 sont tués selon Xénophon.\n\n**La fin.** Inquiète du redressement athénien, la Perse se rapproche de Sparte. Le conflit, qui doit son nom aux combats prolongés autour de Corinthe, s'achève en 387/386 par la paix du Roi, qui consacre l'arbitrage perse dans les affaires grecques. La chronologie des années 393 à 388 reste incertaine sur plusieurs points.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "III, 5 à V, 1 ; IV, 3, 10 à 12 ; IV, 5, 11 à 17",
        "url": `${XENOPHON}:book=3:chapter=5`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIV, 81 à 86 et 91 à 92",
        "url": `${DIODORE}:book=14:chapter=81`
      },
      {
        "kind": "modern",
        "author": "Charles D. Hamilton",
        "work": "Sparta's Bitter Victories: Politics and Diplomacy in the Corinthian War, Ithaca, Cornell University Press, 1979"
      }
    ]
  },
  {
    "id": "paix-du-roi",
    "title": "Paix du Roi (paix d'Antalcidas)",
    "start": -386,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Paix conclue pendant l'hiver 387/386 ou au printemps 386 ; la conversion des années athéniennes laisse une incertitude d'un an.",
    "era": "classique",
    "track": "perse",
    "category": "politics",
    "importance": 2,
    "placeId": "sardes",
    "people": [
      "artaxerxes-ii",
      "antalcidas",
      "agesilas-ii"
    ],
    "summary": "En 387/386, le roi perse Artaxerxès II impose aux Grecs une paix générale négociée par le Spartiate Antalcidas : les cités d'Asie Mineure et Chypre lui reviennent, toutes les autres cités grecques doivent être autonomes. Sparte, garante du traité, s'en sert pour dissoudre les ligues de ses rivales.",
    "body": "**Le message du roi.** À Sardes, le satrape Tiribaze lit aux délégués grecs le message royal, scellé du sceau du roi, que Xénophon reproduit : les cités d'Asie, avec Clazomènes et Chypre, appartiennent au roi ; les autres cités, petites et grandes, seront autonomes, sauf Lemnos, Imbros et Skyros, laissées à Athènes. Ceux qui refuseraient auront le roi pour ennemi.\n\n**Une paix au service de Sparte.** Au nom de l'autonomie, Sparte oblige Thèbes à dissoudre la confédération béotienne, sépare Corinthe d'Argos et, en 385, disperse Mantinée en villages. Pour les Grecs du IVe siècle, cette paix, dite aussi d'Antalcidas, reste le symbole de l'abandon des Grecs d'Asie, un siècle après les guerres médiques.\n\n**Une formule durable.** La paix du Roi est la première d'une série de « paix communes » (koinè eirènè), renouvelées en 375, en 371 et après, qui prétendent garantir l'autonomie de toutes les cités. Elle fait du roi de Perse l'arbitre des affaires grecques jusqu'à l'avènement de Philippe II.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "V, 1, 25 à 36 ; V, 2, 1 à 7",
        "url": `${XENOPHON}:book=5:chapter=1`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIV, 110",
        "url": `${DIODORE}:book=14:chapter=110`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Agésilas",
        "locus": "23",
        "url": `${PLUTARQUE}/Agesilaus*.html`
      },
      {
        "kind": "modern",
        "author": "T. T. B. Ryder",
        "work": "Koine Eirene: General Peace and Local Independence in Ancient Greece, Oxford, Oxford University Press, 1965"
      }
    ]
  },
  {
    "id": "fondation-de-l-academie",
    "title": "Platon fonde l'Académie",
    "start": -386,
    "precision": "decade",
    "certainty": "traditional",
    "certaintyNote": "Date déduite (vers 387) du retour de Platon de son premier voyage en Sicile ; aucune source antique ne donne l'année de la fondation.",
    "era": "classique",
    "track": "athenes",
    "category": "culture",
    "importance": 2,
    "placeId": "academie",
    "people": [
      "platon",
      "aristote"
    ],
    "summary": "Vers 387, de retour d'un premier voyage en Italie du Sud et en Sicile, Platon commence à enseigner dans le gymnase de l'Académie, aux portes d'Athènes. L'école qu'il y fonde réunit philosophes, mathématiciens et futurs hommes d'État, dont Aristote, et lui survit jusqu'au Ier siècle av. J.-C.",
    "body": "**Un lieu.** L'Académie est un bois sacré du héros Akadémos, aménagé en gymnase, à environ 1,5 km au nord-ouest de la porte du Dipylon. Platon, qui possède aussi un petit jardin tout proche, y réunit des disciples à son retour de Sicile, où il a rencontré Denys l'Ancien ; d'après la Lettre VII, il a alors une quarantaine d'années.\n\n**Une école.** On y discute de philosophie, de mathématiques et d'astronomie (Eudoxe de Cnide y séjourne), mais aussi de lois et de constitutions. Aristote y étudie une vingtaine d'années, de 367 à la mort de Platon en 348/347. Après Platon, l'école est dirigée par son neveu Speusippe, puis par Xénocrate. L'enseignement s'y interrompt pendant la guerre contre Mithridate : en 86, Sylla, qui assiège Athènes, fait abattre les arbres du bois sacré.\n\n**Ce qui est incertain.** La date de 387 est déduite du récit de Platon et de Diogène Laërce. La célèbre inscription « Que nul n'entre ici s'il n'est géomètre » n'est attestée que par des auteurs du VIe siècle apr. J.-C. Les fouilles menées depuis les années 1930 ont dégagé une partie du site, mais peu de vestiges remontent au temps de Platon.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Platon",
        "work": "Lettre VII",
        "locus": "324a et 326b à 327a"
      },
      {
        "kind": "ancient",
        "author": "Diogène Laërce",
        "work": "Vies et doctrines des philosophes illustres",
        "locus": "III, 7 ; IV, 1 ; V, 9"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Sylla",
        "locus": "12",
        "url": `${PLUTARQUE}/Sulla*.html`
      },
      {
        "kind": "modern",
        "author": "John Dillon",
        "work": "The Heirs of Plato: A Study of the Old Academy (347-274 BC), Oxford, Clarendon Press, 2003"
      }
    ]
  },
  {
    "id": "denys-l-ancien-prend-motye",
    "title": "Denys l'Ancien prend Motyé",
    "start": -396,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "occident",
    "category": "war",
    "importance": 2,
    "placeId": "motye",
    "people": [
      "denys-l-ancien"
    ],
    "summary": "En 397, Denys l'Ancien, tyran de Syracuse, assiège Motyé, cité phénicienne bâtie sur un îlot de l'ouest de la Sicile et alliée de Carthage. Il fait construire une digue à travers la lagune, approche des tours roulantes et emploie des catapultes, une arme nouvelle mise au point à Syracuse. La ville est prise d'assaut et ses habitants massacrés ou vendus.",
    "body": "**Le tyran de Syracuse.** Arrivé au pouvoir en 405, pendant une guerre contre Carthage, Denys gouverne Syracuse pendant trente-huit ans, jusqu'à sa mort en 367. Il fortifie la ville, notamment le plateau des Épipoles, et prépare la reprise de la guerre en réunissant des artisans venus de tout le monde grec : selon Diodore, c'est à cette occasion qu'est inventée la catapulte, en 399.\n\n**Le siège.** Diodore attribue à Denys 80 000 fantassins et près de 200 navires de guerre, chiffres sans doute gonflés. Les Motyéens ayant coupé la chaussée qui les reliait à la terre, Denys fait construire une digue à travers la lagune, y pousse des tours de six étages et bat les murailles avec des béliers, tandis que les catapultes balaient les défenseurs. Après de durs combats de rue, la ville tombe.\n\n**Une victoire sans lendemain.** Dès 396, le général carthaginois Himilcon reprend l'ouest de l'île et assiège Syracuse, sauvée par une épidémie dans son camp. Motyé n'est pas reconstruite : les survivants s'installent à Lilybée, sur la côte voisine. Les fouilles de l'îlot ont mis au jour des destructions et des armes attribuées à ce siège.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XIV, 41 à 43 ; XIV, 47 à 53 ; XIV, 70 à 71",
        "url": `${DIODORE}:book=14:chapter=47`
      },
      {
        "kind": "modern",
        "author": "Brian Caven",
        "work": "Dionysius I: War-Lord of Sicily, New Haven, Yale University Press, 1990"
      }
    ]
  },
  {
    "id": "liberation-de-thebes-et-bataillon-sacre",
    "title": "Libération de Thèbes et création du Bataillon sacré",
    "start": -378,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Le coup de main a lieu en hiver, à la fin de 379 selon la plupart des historiens ; certains le placent au début de 378.",
    "era": "classique",
    "track": "thebes",
    "category": "politics",
    "importance": 2,
    "placeId": "thebes",
    "people": [
      "pelopidas"
    ],
    "summary": "Pendant l'hiver 379/378, Pélopidas et d'autres exilés thébains rentrent déguisés à Thèbes, tuent les chefs du parti favorable à Sparte et obtiennent le départ de la garnison spartiate installée sur la Cadmée depuis 382. Thèbes se dote ensuite d'une troupe d'élite de 300 hommes, le Bataillon sacré.",
    "body": "**Le coup de main.** En 382, le Spartiate Phoibidas s'était emparé par surprise de la Cadmée, la citadelle de Thèbes, en pleine paix. Réfugiés à Athènes, des exilés thébains reviennent un soir d'hiver ; selon Xénophon, certains se déguisent en femmes invitées à un banquet. Ils tuent les polémarques Archias et Philippos, puis Léontiadès. La garnison spartiate, assiégée, capitule et se retire.\n\n**Le Bataillon sacré.** Selon Plutarque, Gorgidas forme alors un corps permanent de 300 hommes, entretenus par la cité et cantonnés sur la Cadmée, composé de couples d'amants, pour que chacun combatte sous les yeux de l'autre. Commandé ensuite par Pélopidas, il joue un rôle décisif à Tégyres (375) et à Leuctres (371), et périt presque entièrement à Chéronée en 338.\n\n**Ce qui est discuté.** Xénophon, peu favorable à Thèbes, raconte le coup de main sans nommer Pélopidas et ne mentionne jamais le Bataillon sacré. Le récit de Plutarque, plus détaillé, est en partie romancé. La composition du Bataillon par couples d'amants, rapportée par des auteurs plus tardifs, est acceptée par la plupart des historiens mais reste difficile à vérifier.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "V, 2, 25 à 36 et V, 4, 1 à 12",
        "url": `${XENOPHON}:book=5:chapter=4`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Pélopidas",
        "locus": "7 à 13 et 18 à 19",
        "url": `${PLUTARQUE}/Pelopidas*.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XV, 25 à 27",
        "url": `${DIODORE}:book=15:chapter=25`
      },
      {
        "kind": "modern",
        "author": "John Buckler",
        "work": "The Theban Hegemony, 371-362 BC, Cambridge (Massachusetts), Harvard University Press, 1980"
      }
    ]
  },
  {
    "id": "seconde-confederation-athenienne",
    "title": "Seconde confédération athénienne",
    "start": -377,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "L'alliance se forme en 378 ; sa charte, le décret d'Aristotélès, est votée sous l'archonte Nausinicos (378/377), au début de 377.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "summary": "En 378/377, Athènes fonde une nouvelle alliance maritime contre Sparte. Le décret d'Aristotélès, gravé sur une stèle de marbre, promet aux alliés ce que l'empire du Ve siècle leur avait refusé : ni tribut, ni garnison, ni colons athéniens sur leurs terres. Plusieurs dizaines de cités y adhèrent.",
    "body": "**Une alliance contre Sparte.** Après l'occupation de la Cadmée et le raid manqué du Spartiate Sphodrias sur le Pirée (378), Athènes s'allie à Thèbes et invite les Grecs à une alliance « pour que les Lacédémoniens laissent les Grecs vivre libres et autonomes », dans le respect de la paix du Roi. Chios, Byzance, Rhodes et Mytilène figurent parmi les premiers membres.\n\n**Des garanties.** Le décret d'Aristotélès garantit l'autonomie des membres et interdit aux Athéniens d'acquérir des terres sur leur territoire. Les alliés siègent dans un conseil (synédrion) distinct de l'assemblée athénienne et versent des contributions (syntaxeis) au lieu du tribut. La stèle porte la liste des membres, complétée au fil des adhésions ; Diodore parle de soixante-dix cités.\n\n**Le déclin.** Les victoires de Chabrias à Naxos (376) et de Timothée en mer Ionienne étendent la ligue, mais Athènes revient peu à peu aux pratiques impériales, garnisons et clérouquies. La guerre des Alliés (de 357 à 355), où Chios, Rhodes, Cos et Byzance font sécession, l'affaiblit durablement ; la ligue disparaît après Chéronée (338).",
    "sources": [
      {
        "kind": "ancient",
        "author": "Décret d'Aristotélès (inscription)",
        "work": "Inscriptiones Graecae, II², 43"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XV, 28 à 30",
        "url": `${DIODORE}:book=15:chapter=28`
      },
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "V, 4, 20 à 34",
        "url": `${XENOPHON}:book=5:chapter=4`
      },
      {
        "kind": "modern",
        "author": "Jack Cargill",
        "work": "The Second Athenian League: Empire or Free Alliance?, Berkeley, University of California Press, 1981"
      }
    ]
  },
  {
    "id": "bataille-de-mantinee-362",
    "title": "Bataille de Mantinée (362)",
    "start": -361,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Bataille de l'été 362 ; le jour exact est discuté.",
    "era": "classique",
    "track": "thebes",
    "category": "war",
    "importance": 2,
    "placeId": "mantinee",
    "people": [
      "epaminondas",
      "xenophon"
    ],
    "summary": "En 362, près de Mantinée en Arcadie, l'armée thébaine et ses alliés battent les Spartiates, les Mantinéens et les Athéniens, mais Épaminondas est mortellement blessé au moment de la victoire. Sans lui, Thèbes ne poursuit pas son avantage : la bataille consacre l'épuisement de toutes les grandes cités.",
    "body": "**La dernière campagne d'Épaminondas.** Les Arcadiens se divisent, et Mantinée passe du côté de Sparte et d'Athènes. Épaminondas envahit le Péloponnèse pour la quatrième fois avec les Béotiens, les Tégéates, les Argiens et les Messéniens. Diodore lui prête plus de 30 000 fantassins et 3 000 cavaliers, contre plus de 20 000 fantassins et 2 000 cavaliers en face, chiffres plausibles mais invérifiables.\n\n**La bataille.** Comme à Leuctres, Épaminondas renforce son aile gauche et l'engage en colonne profonde, soutenue par la cavalerie. La ligne adverse est enfoncée, mais Épaminondas est frappé à la poitrine ; ses troupes, privées de chef, ne poursuivent pas l'ennemi, et les deux camps dressent un trophée. Gryllos, fils de Xénophon, tombe dans les combats de cavalerie.\n\n**Le bilan.** Xénophon termine ses Helléniques sur ce constat : après la bataille, il y eut en Grèce encore plus de confusion et de désordre qu'avant. Une paix commune est conclue, que Sparte refuse parce qu'elle reconnaît l'indépendance de la Messénie. L'hégémonie thébaine ne survit pas à Épaminondas ; trois ans plus tard, Philippe II monte sur le trône de Macédoine.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Xénophon",
        "work": "Helléniques",
        "locus": "VII, 5, 18 à 27",
        "url": `${XENOPHON}:book=7:chapter=5`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XV, 82 à 89",
        "url": `${DIODORE}:book=15:chapter=84`
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "VIII, 11, 5 à 10",
        "url": `${PAUSANIAS}:book=8:chapter=11`
      },
      {
        "kind": "modern",
        "author": "John Buckler",
        "work": "The Theban Hegemony, 371-362 BC, Cambridge (Massachusetts), Harvard University Press, 1980"
      }
    ]
  },
  {
    "id": "philippe-ii-roi-de-macedoine",
    "title": "Philippe II prend le pouvoir en Macédoine",
    "start": -358,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "macedoine",
    "category": "politics",
    "importance": 2,
    "placeId": "pella",
    "people": [
      "philippe-ii"
    ],
    "summary": "En 359, le roi Perdiccas III est tué avec 4 000 Macédoniens par les Illyriens. Son frère Philippe, 23 ans, prend le pouvoir dans un royaume envahi et disputé par des prétendants. En deux ans, il écarte ses rivaux, bat les Illyriens et réorganise l'armée : la Macédoine devient la première puissance du nord de la Grèce.",
    "body": "**Un royaume en danger.** Otage à Thèbes dans sa jeunesse, au temps d'Épaminondas et de Pélopidas, Philippe y a observé la meilleure armée de son temps. À la mort de son frère, il doit faire face aux Illyriens de Bardylis, aux Péoniens et à deux prétendants, Pausanias, soutenu par les Thraces, et Argaios, soutenu par Athènes. Il achète le départ des uns, bat Argaios et, en 358, écrase les Illyriens : Diodore compte plus de 7 000 morts dans l'armée de Bardylis.\n\n**Une armée nouvelle.** Diodore attribue à Philippe l'organisation de la phalange macédonienne, aux rangs serrés, armée de la sarisse, une pique de 5 à 6 mètres environ, et appuyée par la cavalerie des Compagnons. Payés et entraînés en permanence, ses soldats forment une armée professionnelle, rare dans le monde grec.\n\n**Ce qui est discuté.** Selon Justin, Philippe aurait d'abord gouverné comme tuteur de son neveu, le jeune Amyntas, avant de prendre le titre de roi ; beaucoup d'historiens en doutent. La part exacte de Philippe dans la réforme militaire, peut-être amorcée par ses prédécesseurs, est également débattue.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 1 à 4",
        "url": `${DIODORE}:book=16:chapter=2`
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "VII, 5"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie de Pélopidas",
        "locus": "26",
        "url": `${PLUTARQUE}/Pelopidas*.html`
      },
      {
        "kind": "modern",
        "author": "N. G. L. Hammond et G. T. Griffith",
        "work": "A History of Macedonia, vol. II, 550-336 B.C., Oxford, Clarendon Press, 1979"
      },
      {
        "kind": "modern",
        "author": "George Cawkwell",
        "work": "Philip of Macedon, Londres, Faber and Faber, 1978"
      }
    ]
  },
  {
    "id": "naissance-d-alexandre",
    "title": "Naissance d'Alexandre",
    "start": -355,
    "month": 7,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Plutarque donne le 6 Hécatombéon (Loos chez les Macédoniens), vers juillet 356 ; la conversion est incertaine d'environ un mois, et les coïncidences qu'il rapporte relèvent de la légende.",
    "era": "classique",
    "track": "macedoine",
    "category": "politics",
    "importance": 2,
    "placeId": "pella",
    "people": [
      "alexandre-le-grand",
      "philippe-ii",
      "olympias"
    ],
    "summary": "Alexandre, fils de Philippe II et de la princesse épirote Olympias, naît à Pella vers juillet 356. Plutarque associe sa naissance à trois bonnes nouvelles arrivées le même jour et à l'incendie du temple d'Artémis à Éphèse, coïncidences qui relèvent sans doute de la légende.",
    "body": "**Une date à peu près sûre.** Plutarque place la naissance le 6 du mois d'Hécatombéon, que les Macédoniens appelaient Loos, soit vers juillet 356. L'âge d'Alexandre à sa mort, en juin 323, donné par Arrien d'après Aristobule (32 ans et 8 mois), concorde avec cette année.\n\n**Les présages.** Selon Plutarque, Philippe, qui vient de prendre Potidée, apprend le même jour la victoire de Parménion sur les Illyriens et celle de ses chevaux aux Jeux olympiques. Le jour de la naissance, le temple d'Artémis à Éphèse brûle, incendié par un homme avide de célébrité, Hérostrate : les mages d'Éphèse y auraient vu l'annonce d'un fléau pour l'Asie. Ces récits ont été composés après coup, à la gloire du conquérant.\n\n**Une éducation royale.** Fils d'une mère qui se disait descendante d'Achille et d'un père qui se réclamait d'Héraclès, Alexandre est élevé à la cour de Pella, puis confié de 343 à 340 environ au philosophe Aristote, à Miéza.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "2 à 3",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "VII, 28, 1"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XIV, 1, 22",
        "url": `${STRABON}:book=14:chapter=1`
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "premiere-philippique",
    "title": "Démosthène contre Philippe : la Première Philippique",
    "start": -351,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Discours daté de l'archontat d'Aristodèmos (352/351) par Denys d'Halicarnasse ; certains historiens ont proposé 349.",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 3,
    "placeId": "athenes",
    "people": [
      "demosthene",
      "philippe-ii"
    ],
    "summary": "En 352/351, le jeune orateur Démosthène dénonce devant l'assemblée athénienne l'inertie d'Athènes face aux progrès de Philippe II et réclame une force permanente, payée et en partie composée de citoyens. Cette Première Philippique ouvre une lutte de quinze ans entre l'orateur et le roi de Macédoine.",
    "body": "**Le discours.** Philippe a pris Amphipolis (357), Pydna et Potidée, puis s'est avancé jusqu'aux Thermopyles (352). Démosthène reproche aux Athéniens de réagir toujours trop tard, comme ces boxeurs maladroits qui portent la main là où ils viennent d'être frappés. Il propose une force de 2 000 fantassins, dont 500 citoyens, de 200 cavaliers et de 10 trières rapides, stationnée en permanence dans le nord.\n\n**La suite.** Les Athéniens ne suivent pas ses propositions. Démosthène prononce ensuite les Olynthiennes (349), pour secourir Olynthe, puis la Deuxième (344) et la Troisième Philippique (341), et finit par rallier Thèbes contre Philippe à la veille de Chéronée (338). Le mot « philippique » désigne depuis un discours violent contre quelqu'un.\n\n**La date.** Denys d'Halicarnasse place le discours sous l'archonte Aristodèmos (352/351). Certains historiens ont proposé 349, en supposant que le texte transmis réunit deux discours ; le site retient 352/351.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Démosthène",
        "work": "Première Philippique (discours IV)",
        "locus": "19 à 29 et 40"
      },
      {
        "kind": "ancient",
        "author": "Denys d'Halicarnasse",
        "work": "Première lettre à Ammée",
        "locus": "4"
      },
      {
        "kind": "modern",
        "author": "Pierre Carlier",
        "work": "Démosthène, Paris, Fayard, 1990"
      }
    ]
  },
  {
    "id": "mausolee-d-halicarnasse",
    "title": "Le Mausolée d'Halicarnasse",
    "start": -349,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Chantier daté vers 360 à 350 environ : commencé peut-être du vivant de Mausole (mort en 353), achevé après la mort d'Artémise (351).",
    "era": "classique",
    "track": "monde-grec",
    "category": "building",
    "importance": 2,
    "placeId": "halicarnasse",
    "people": [
      "mausole",
      "artemise-ii"
    ],
    "summary": "Vers 350, à Halicarnasse, en Carie, s'élève le tombeau monumental du dynaste Mausole, mort en 353, poursuivi par sa veuve Artémise puis achevé après elle. Haut d'environ 45 mètres, orné par les plus grands sculpteurs du temps, il compte parmi les Sept Merveilles du monde et a donné son nom à tous les mausolées.",
    "body": "**Le monument.** Pline l'Ancien le décrit comme un haut soubassement portant une colonnade de 36 colonnes, coiffée d'une pyramide de 24 degrés et d'un quadrige de marbre, pour une hauteur totale de 140 pieds (environ 45 mètres). Les architectes Satyros et Pythéos en ont écrit une description, et quatre sculpteurs, Scopas, Bryaxis, Timothéos et Léocharès, se sont partagé les quatre côtés.\n\n**Mausole et Artémise.** Dynaste de Carie au service du roi perse de 377 à 353, Mausole fait d'Halicarnasse sa capitale et l'embellit. Sa sœur et épouse Artémise lui succède et poursuit le chantier ; selon Pline, les sculpteurs l'achèvent après la mort de la reine, en 351, pour leur propre gloire. Le tombeau était peut-être déjà en construction du vivant de Mausole.\n\n**Après l'Antiquité.** Ébranlé par des séismes, le monument est démantelé au début du XVIe siècle par les chevaliers de Saint-Jean, qui en réutilisent les pierres pour le château de Bodrum. Charles Newton en fouille les fondations en 1856 et 1857 ; des statues et des plaques de frise sont au British Museum.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pline l'Ancien",
        "work": "Histoire naturelle",
        "locus": "XXXVI, 30 à 31"
      },
      {
        "kind": "ancient",
        "author": "Vitruve",
        "work": "De l'architecture",
        "locus": "II, 8, 10 à 15 ; VII, préface, 12 à 13"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 36, 2 et XVI, 45, 7",
        "url": `${DIODORE}:book=16:chapter=36`
      },
      {
        "kind": "modern",
        "author": "Simon Hornblower",
        "work": "Mausolus, Oxford, Clarendon Press, 1982"
      }
    ]
  },
  {
    "id": "prise-d-olynthe",
    "title": "Philippe II prend et rase Olynthe",
    "start": -347,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Prise datée de l'archontat de Théophilos (348/347) par Philochore, cité par Denys d'Halicarnasse : sans doute à la fin de l'été ou à l'automne 348.",
    "era": "classique",
    "track": "macedoine",
    "category": "war",
    "importance": 2,
    "placeId": "olynthe",
    "people": [
      "philippe-ii",
      "demosthene"
    ],
    "summary": "En 348, Philippe II prend Olynthe, capitale de la confédération chalcidienne, grâce à la trahison de deux de ses magistrats. La ville est rasée et ses habitants réduits en esclavage, malgré les appels de Démosthène, qui avait pressé Athènes de la secourir. Ses ruines, fouillées au XXe siècle, sont une source majeure sur la maison grecque classique.",
    "body": "**La guerre.** Alliée de Philippe, puis inquiète de sa puissance, Olynthe se rapproche d'Athènes. En 349, Philippe attaque les cités de Chalcidique ; Démosthène prononce les trois Olynthiennes pour obtenir des secours, mais l'aide athénienne arrive tard et en petit nombre. Selon Diodore, Philippe entre dans la ville grâce à deux magistrats achetés, Euthycratès et Lasthénès.\n\n**La destruction.** Philippe rase la ville et vend la population. Quelques années plus tard, Démosthène parle de trente-deux cités de Thrace détruites, chiffre de polémiste. La chute d'Olynthe pousse Athènes à négocier avec Philippe, ce qui aboutit à la paix de Philocrate en 346.\n\n**Une ville figée.** Les fouilles de David M. Robinson, de 1928 à 1938, ont dégagé un quartier bâti au IVe siècle sur un plan en damier, avec une centaine de maisons. Des balles de fronde en plomb au nom de Philippe témoignent du siège. Abandonnée en 348, la ville montre l'état des maisons grecques à une date précise.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 52, 9 à 53, 3",
        "url": `${DIODORE}:book=16:chapter=53`
      },
      {
        "kind": "ancient",
        "author": "Démosthène",
        "work": "Olynthiennes (discours I à III) ; Troisième Philippique (discours IX)",
        "locus": "IX, 26"
      },
      {
        "kind": "modern",
        "author": "David M. Robinson et al.",
        "work": "Excavations at Olynthus, 14 vol., Baltimore, Johns Hopkins Press, 1929-1952"
      },
      {
        "kind": "modern",
        "author": "Nicholas Cahill",
        "work": "Household and City Organization at Olynthus, New Haven, Yale University Press, 2002"
      }
    ]
  },
  {
    "id": "paix-de-philocrate",
    "title": "Paix de Philocrate et fin de la guerre sacrée",
    "start": -345,
    "precision": "year",
    "certainty": "attested",
    "era": "classique",
    "track": "athenes",
    "category": "politics",
    "importance": 2,
    "placeId": "athenes",
    "people": [
      "philocrate",
      "demosthene",
      "eschine",
      "philippe-ii"
    ],
    "summary": "En 346, Athènes conclut avec Philippe II une paix négociée par Philocrate, Démosthène et Eschine, qui reconnaît les conquêtes macédoniennes. Philippe en profite pour franchir les Thermopyles, obtenir la capitulation des Phocidiens, mettre fin à la troisième guerre sacrée et entrer au conseil amphictyonique de Delphes.",
    "body": "**La négociation.** Après la chute d'Olynthe, Athènes envoie deux ambassades à Pella, où figurent notamment Philocrate, Eschine et Démosthène. L'assemblée vote la paix et l'alliance au printemps 346, au mois d'Élaphébolion ; Athènes renonce à Amphipolis. Philippe retarde ses serments jusqu'à ce que son armée soit prête à marcher vers le sud.\n\n**La fin de la guerre sacrée.** Depuis 356, les Phocidiens occupaient Delphes et payaient leurs mercenaires avec le trésor du sanctuaire. Exclus de la paix, ils capitulent devant Philippe au début de l'été 346. Le conseil amphictyonique transfère leurs deux voix au roi de Macédoine, qui préside les Jeux pythiques de l'automne : il devient un acteur reconnu des affaires grecques.\n\n**Une paix contestée.** Démosthène, qui l'avait votée, la juge bientôt désastreuse. Philocrate, accusé de corruption, s'exile en 343 et est condamné à mort par contumace ; la même année, Démosthène poursuit Eschine, acquitté de justesse. Les deux discours Sur l'ambassade, parvenus jusqu'à nous, donnent deux versions opposées des mêmes faits.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Démosthène",
        "work": "Sur l'ambassade (discours XIX)"
      },
      {
        "kind": "ancient",
        "author": "Eschine",
        "work": "Sur l'ambassade (discours II)"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 59 à 60",
        "url": `${DIODORE}:book=16:chapter=59`
      },
      {
        "kind": "modern",
        "author": "George Cawkwell",
        "work": "Philip of Macedon, Londres, Faber and Faber, 1978"
      },
      {
        "kind": "modern",
        "author": "Pierre Carlier",
        "work": "Démosthène, Paris, Fayard, 1990"
      }
    ]
  },
  {
    "id": "ligue-de-corinthe",
    "title": "Ligue de Corinthe",
    "start": -336,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Première réunion à Corinthe à la fin de 338 ou au début de 337 ; le vote de la guerre contre la Perse date de 337.",
    "era": "classique",
    "track": "macedoine",
    "category": "politics",
    "importance": 2,
    "placeId": "corinthe",
    "people": [
      "philippe-ii",
      "parmenion"
    ],
    "summary": "Après Chéronée, Philippe II réunit à Corinthe les délégués des cités grecques, Sparte exceptée. Ils jurent une paix commune et forment une alliance, la ligue de Corinthe, dont Philippe est le chef (hégémôn). En 337, le conseil de la ligue vote la guerre contre la Perse, pour venger les sanctuaires brûlés par Xerxès.",
    "body": "**Une paix sous contrôle.** Le serment des cités, conservé en partie par une inscription d'Athènes, les engage à respecter la paix, à ne renverser ni les régimes en place ni la royauté de Philippe et de ses descendants, et à combattre quiconque la violerait. Un conseil commun (synédrion), où chaque cité est représentée selon son importance, juge les conflits ; des garnisons macédoniennes tiennent Thèbes, Corinthe et Chalcis.\n\n**La guerre contre la Perse.** Le conseil élit Philippe stratège avec les pleins pouvoirs pour une guerre de représailles contre le Grand Roi. Au printemps 336, une avant-garde commandée par Parménion et Attale passe en Asie. L'assassinat de Philippe, quelques mois plus tard, laisse le projet à Alexandre, qui fait renouveler l'alliance en sa faveur.\n\n**Le sens du traité.** Pour beaucoup d'historiens, la ligue de Corinthe marque la fin de l'indépendance politique des grandes cités, même si la paix commune reprend une formule grecque ancienne. Le nom de « ligue de Corinthe » est moderne : les Anciens parlaient des Grecs alliés de Philippe.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 89 et XVI, 91, 2",
        "url": `${DIODORE}:book=16:chapter=89`
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "IX, 5"
      },
      {
        "kind": "ancient",
        "author": "Serment des Grecs (inscription)",
        "work": "Inscriptiones Graecae, II², 236"
      },
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "I, 1, 1 à 3"
      },
      {
        "kind": "modern",
        "author": "N. G. L. Hammond et G. T. Griffith",
        "work": "A History of Macedonia, vol. II, 550-336 B.C., Oxford, Clarendon Press, 1979"
      }
    ]
  },
  {
    "id": "assassinat-de-philippe-ii",
    "title": "Assassinat de Philippe II",
    "start": -335,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Meurtre de l'été ou de l'automne 336, sous l'archonte Pythodèlos (336/335) selon Arrien ; le mois exact est discuté.",
    "era": "classique",
    "track": "macedoine",
    "category": "politics",
    "importance": 2,
    "placeId": "aigai",
    "people": [
      "philippe-ii",
      "alexandre-le-grand",
      "olympias",
      "pausanias-d-orestide"
    ],
    "summary": "En 336, à Aigai, l'ancienne capitale macédonienne, Philippe II est poignardé par Pausanias, l'un de ses gardes du corps, au théâtre où se célèbrent les noces de sa fille. Alexandre, 20 ans, est aussitôt reconnu roi par l'armée. Les mobiles du meurtrier et ses éventuels complices restent discutés.",
    "body": "**Le meurtre.** Philippe marie sa fille Cléopâtre à Alexandre, roi d'Épire et frère d'Olympias. Au matin des fêtes, il entre au théâtre, derrière une procession où sa statue suit celles des douze dieux, en laissant ses gardes à distance. Pausanias le frappe d'un poignard, s'enfuit vers les chevaux qui l'attendent, puis est rattrapé et tué par d'autres gardes.\n\n**Pourquoi ?** Aristote, contemporain des faits, rapporte que Pausanias se vengeait d'un outrage subi de la part de l'entourage d'Attale, oncle de la dernière épouse de Philippe, que le roi avait refusé de punir. Les Anciens soupçonnaient aussi Olympias, répudiée, voire Alexandre lui-même, ou le roi perse ; aucune preuve ne permet de trancher. Alexandre élimine ensuite plusieurs rivaux, dont Attale.\n\n**Le tombeau.** En 1977, Manolis Andronikos découvre à Vergina, l'antique Aigai, une tombe royale inviolée (tombe II), qu'il attribue à Philippe II. D'autres archéologues y voient la tombe de Philippe III Arrhidée, demi-frère d'Alexandre ; le débat n'est pas clos.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVI, 91 à 94",
        "url": `${DIODORE}:book=16:chapter=91`
      },
      {
        "kind": "ancient",
        "author": "Aristote",
        "work": "Politique",
        "locus": "V, 10, 1311b"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "10",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "IX, 6 à 7"
      },
      {
        "kind": "modern",
        "author": "Manolis Andronikos",
        "work": "Vergina: The Royal Tombs and the Ancient City, Athènes, Ekdotike Athenon, 1984"
      },
      {
        "kind": "modern",
        "author": "N. G. L. Hammond et G. T. Griffith",
        "work": "A History of Macedonia, vol. II, 550-336 B.C., Oxford, Clarendon Press, 1979"
      }
    ]
  },
  {
    "id": "destruction-de-thebes",
    "title": "Alexandre détruit Thèbes",
    "start": -334,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Prise à l'automne 335 ; le jour exact n'est pas connu.",
    "era": "classique",
    "track": "thebes",
    "category": "war",
    "importance": 2,
    "placeId": "thebes",
    "people": [
      "alexandre-le-grand",
      "perdiccas",
      "demosthene"
    ],
    "summary": "En 335, alors qu'Alexandre fait campagne contre les Illyriens, Thèbes se soulève sur la rumeur de sa mort. Le roi arrive en moins de deux semaines, prend la ville d'assaut et laisse ses alliés grecs décider de son sort : Thèbes est rasée, à l'exception des temples et de la maison du poète Pindare, et sa population vendue.",
    "body": "**La révolte.** Les Thébains assiègent la garnison macédonienne de la Cadmée et appellent les Grecs à la liberté ; Athènes, encouragée par Démosthène, hésite et n'envoie pas de troupes. Alexandre, parti des confins de l'Illyrie, surgit devant la ville, propose d'abord un pardon, puis attaque. Selon Ptolémée, cité par Arrien, l'assaut est lancé sans ordre par le bataillon de Perdiccas.\n\n**Le châtiment.** Diodore compte plus de 6 000 Thébains tués et plus de 30 000 prisonniers, chiffres que l'on ne peut vérifier. Le sort de la ville est décidé par les alliés présents, dont des ennemis de longue date de Thèbes (Phocidiens, Platéens, Orchoméniens), ce qui permet à Alexandre de le présenter comme un verdict grec. Il réclame ensuite à Athènes ses orateurs hostiles, dont Démosthène, puis y renonce.\n\n**Une leçon pour la Grèce.** La destruction de l'une des plus anciennes cités grecques terrorise les autres et assure à Alexandre une Grèce soumise pendant son départ pour l'Asie. Thèbes ne sera rebâtie qu'en 316, par Cassandre.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "I, 7 à 10"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 8 à 14",
        "url": `${DIODORE}:book=17:chapter=8`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "11 à 13",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "bataille-du-granique",
    "title": "Bataille du Granique",
    "start": -333,
    "month": 5,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Plutarque situe la bataille au mois macédonien de Daisios, vers mai 334 ; la conversion est approximative.",
    "era": "classique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "granique",
    "people": [
      "alexandre-le-grand",
      "parmenion",
      "memnon-de-rhodes",
      "clitos-le-noir"
    ],
    "summary": "En mai 334, quelques semaines après avoir franchi l'Hellespont, Alexandre attaque l'armée des satrapes perses d'Asie Mineure, postée derrière le Granique. Il traverse la rivière à la tête de sa cavalerie, échappe de peu à la mort et remporte une victoire qui lui ouvre l'Asie Mineure.",
    "body": "**Le passage en Asie.** Au printemps 334, Alexandre franchit l'Hellespont avec un peu plus de 30 000 fantassins et environ 5 000 cavaliers selon Arrien. Les satrapes rejettent le conseil du chef de mercenaires Memnon de Rhodes, qui voulait brûler les récoltes pour affamer l'envahisseur, et attendent derrière le Granique, cavalerie en première ligne, mercenaires grecs en retrait. Arrien leur prête 20 000 cavaliers et près de 20 000 mercenaires, chiffres sans doute exagérés.\n\n**La bataille.** Selon Arrien, Alexandre passe outre le conseil de Parménion, qui voulait attendre l'aube, et attaque aussitôt. Dans la mêlée de cavalerie sur la rive, son casque est fendu d'un coup de sabre ; Clitos le Noir tranche le bras d'un noble perse qui allait l'abattre. Les mercenaires grecs, encerclés, sont massacrés ; 2 000 survivants sont envoyés aux travaux forcés en Macédoine, comme traîtres à la cause grecque.\n\n**Deux récits.** Diodore décrit une bataille livrée à l'aube, après une traversée sans combat, ce qui est difficile à concilier avec Arrien. Alexandre envoie 300 panoplies perses à Athènes, avec une dédicace qui exclut ostensiblement les Lacédémoniens : la guerre se veut celle des Grecs, au nom de la ligue de Corinthe.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "I, 11 à 16"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 17 à 21",
        "url": `${DIODORE}:book=17:chapter=19`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "16",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "bataille-d-issos",
    "title": "Bataille d'Issos",
    "start": -332,
    "month": 11,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Arrien date la bataille de l'archontat de Nicocratès, au mois de Maimaktérion, soit vers novembre 333 ; la conversion est incertaine d'environ un mois.",
    "era": "classique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "issos",
    "people": [
      "alexandre-le-grand",
      "darius-iii",
      "parmenion"
    ],
    "summary": "En novembre 333, Darius III surprend les arrières d'Alexandre en Cilicie, près du golfe d'Issos. Sur une plaine étroite entre mer et montagnes, la cavalerie macédonienne enfonce la gauche perse et Alexandre fonce vers Darius, qui s'enfuit en abandonnant son camp, sa mère, sa femme et ses enfants.",
    "body": "**Une manœuvre manquée.** Darius rassemble une grande armée à Babylone et passe les montagnes de l'Amanus derrière Alexandre, qui avançait vers la Syrie. Alexandre fait demi-tour et accepte la bataille sur la rivière Pinaros, où la plaine, resserrée, empêche les Perses de profiter de leur nombre. Arrien parle de 600 000 Perses, chiffre impossible, et Polybe critiquait déjà les chiffres de Callisthène ; les modernes pensent à quelques dizaines de milliers d'hommes de chaque côté.\n\n**La bataille.** Alexandre charge à droite avec les Compagnons, tandis que la phalange peine à franchir la rivière face aux mercenaires grecs de Darius. La gauche perse cède, et Darius s'enfuit sur son char, puis à cheval. Les cavaliers perses de l'autre aile, qui pressaient Parménion le long de la mer, se débandent en apprenant la fuite du roi.\n\n**Les suites.** La famille royale capturée est traitée avec égards. Darius propose une rançon, puis un partage de l'empire, qu'Alexandre refuse. Au lieu de le poursuivre, Alexandre descend la côte phénicienne pour priver la flotte perse de ses bases. La mosaïque de la maison du Faune, à Pompéi, représente sans doute Issos, ou peut-être Gaugamèles.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "II, 6 à 14"
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "III, 8 à 12"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 32 à 37",
        "url": `${DIODORE}:book=17:chapter=33`
      },
      {
        "kind": "ancient",
        "author": "Polybe",
        "work": "Histoires",
        "locus": "XII, 17 à 22"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "siege-de-tyr",
    "title": "Siège de Tyr",
    "start": -331,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Siège de sept mois selon Diodore et Plutarque, achevé au mois d'Hécatombéon (juillet ou août 332) selon Arrien ; il a donc commencé vers janvier 332.",
    "era": "classique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "tyr",
    "people": [
      "alexandre-le-grand"
    ],
    "summary": "De janvier à l'été 332, Alexandre assiège Tyr, la grande cité phénicienne bâtie sur une île, qui lui refuse l'entrée. Il fait construire une digue à travers le bras de mer, puis attaque les murailles depuis des navires. Après sept mois, la ville est prise d'assaut : 8 000 défenseurs sont tués et 30 000 habitants vendus selon Arrien.",
    "body": "**Une île imprenable.** Tyr accepte de se soumettre, mais refuse qu'Alexandre vienne sacrifier à Melqart, l'Héraclès tyrien, dans le temple de l'île. Alexandre décide de la prendre pour ne laisser aucune base à la flotte perse. Ses ingénieurs construisent une digue depuis la côte, à 4 stades (environ 700 mètres) ; les Tyriens l'incendient avec un brûlot, et il faut la reconstruire plus large.\n\n**L'assaut.** Le ralliement des flottes phéniciennes et des rois de Chypre, plus de 200 navires, donne la maîtrise de la mer à Alexandre. Des béliers montés sur des navires ouvrent une brèche au sud de la ville ; l'assaut final, mené par Alexandre lui-même, fait tomber Tyr à l'été 332. Diodore et Quinte-Curce ajoutent que 2 000 jeunes hommes furent crucifiés sur le rivage, détail absent d'Arrien.\n\n**Une île devenue presqu'île.** Les sédiments se sont accumulés de part et d'autre de la digue, qui a fini par former l'isthme sur lequel s'étend la ville actuelle de Sour. Selon les géomorphologues, la digue s'est appuyée sur un banc de sable naturel préexistant, ce qui explique la rapidité de l'ouvrage.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "II, 15 à 24"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 40 à 46",
        "url": `${DIODORE}:book=17:chapter=40`
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "IV, 2 à 4"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "24 à 25",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "modern",
        "author": "Nick Marriner, Christophe Morhange et Samuel Meulé",
        "work": "Holocene morphogenesis of Alexander the Great's isthmus at Tyre in Lebanon, Proceedings of the National Academy of Sciences, 104, 22, 2007"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "fondation-d-alexandrie",
    "title": "Fondation d'Alexandrie",
    "start": -330,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Début de 331 selon la plupart des historiens ; certains placent la fondation à la fin de 332. Les sources ne s'accordent pas sur l'ordre de la fondation et de la visite à Siwa.",
    "era": "classique",
    "track": "alexandre",
    "category": "building",
    "importance": 1,
    "placeId": "alexandrie",
    "people": [
      "alexandre-le-grand",
      "dinocrate"
    ],
    "summary": "Au début de 331, Alexandre choisit, à l'ouest du delta du Nil, une bande de terre entre la mer et le lac Maréotis pour y fonder une ville à son nom, dont l'architecte Dinocrate dessine le plan. Capitale des Ptolémées, Alexandrie deviendra la plus grande cité du monde grec et son principal foyer savant.",
    "body": "**Le choix du site.** Entré sans combat en Égypte à la fin de 332, Alexandre est accueilli à Memphis comme le libérateur de la domination perse. En descendant la branche canopique du Nil, il repère près du village égyptien de Rhakotis un site abrité par l'île de Pharos, propice à deux ports et relié au Nil par le lac Maréotis. Faute de craie, raconte Plutarque, on trace l'enceinte avec de la farine d'orge, que des oiseaux viennent manger : les devins y voient le signe d'une ville qui nourrira bien des peuples.\n\n**Une ville au plan régulier.** Selon Vitruve, Dinocrate de Rhodes dessine la ville, avec de larges rues se coupant à angle droit. Plus tard, une digue de sept stades, l'Heptastade, relie Pharos au continent. Alexandre ne revoit jamais sa ville ; il y est pourtant enterré, après que Ptolémée a détourné son cortège funèbre.\n\n**La date.** Arrien et Plutarque placent la fondation avant la visite à l'oracle d'Ammon, Diodore et Quinte-Curce après. La plupart des historiens retiennent le début de 331 ; une tradition alexandrine, conservée par le Roman d'Alexandre, célébrait un jour précis, dont la conversion est discutée.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "III, 1, 5 à 2, 2"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "26",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 52",
        "url": `${DIODORE}:book=17:chapter=52`
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "IV, 8, 1 à 6"
      },
      {
        "kind": "ancient",
        "author": "Vitruve",
        "work": "De l'architecture",
        "locus": "II, préface, 4"
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XVII, 1, 6 à 8",
        "url": `${STRABON}:book=17:chapter=1`
      },
      {
        "kind": "modern",
        "author": "P. M. Fraser",
        "work": "Ptolemaic Alexandria, 3 vol., Oxford, Clarendon Press, 1972"
      }
    ]
  },
  {
    "id": "oracle-d-ammon-a-siwa",
    "title": "Alexandre consulte l'oracle d'Ammon à Siwa",
    "start": -330,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Visite attestée, au début de 331 ou à la fin de 332 ; la réponse de l'oracle n'est connue que par des récits contradictoires.",
    "era": "classique",
    "track": "alexandre",
    "category": "religion",
    "importance": 2,
    "placeId": "oasis-de-siwa",
    "people": [
      "alexandre-le-grand"
    ],
    "summary": "Au début de 331, Alexandre traverse le désert libyque jusqu'à l'oasis de Siwa pour consulter l'oracle d'Ammon, dieu que les Grecs identifiaient à Zeus. Le prêtre l'aurait salué comme fils du dieu. La consultation reste secrète, mais Alexandre se présente ensuite volontiers comme fils de Zeus-Ammon.",
    "body": "**Le voyage.** De Paraitonion, sur la côte, Alexandre et une petite escorte marchent plusieurs jours dans le désert ; un vent du sud efface la piste. Ptolémée raconte que deux serpents doués de parole guidèrent la troupe, Aristobule que ce furent deux corbeaux ; Arrien rapporte les deux versions. L'oracle d'Ammon était réputé chez les Grecs depuis le VIe siècle, au même titre que Delphes ou Dodone.\n\n**La réponse.** Selon Arrien, Alexandre entendit ce qu'il souhaitait et n'en dit pas davantage. Callisthène, son historien officiel, cité par Strabon, affirme que le prêtre le proclama fils de Zeus. Plutarque rapporte une anecdote : le prêtre, voulant dire en grec « mon enfant » (ô paidion), aurait prononcé « ô pai Dios », « fils de Zeus ».\n\n**Les conséquences.** Le titre de fils d'Ammon prend de l'importance dans l'image du roi : après sa mort, ses successeurs, comme Lysimaque, le représentent sur leurs monnaies avec les cornes de bélier d'Ammon. Les soldats macédoniens s'en moqueront lors de la mutinerie d'Opis, en 324.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "III, 3 à 4"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "26 à 27",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 49 à 51",
        "url": `${DIODORE}:book=17:chapter=49`
      },
      {
        "kind": "ancient",
        "author": "Strabon",
        "work": "Géographie",
        "locus": "XVII, 1, 43",
        "url": `${STRABON}:book=17:chapter=1`
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "incendie-de-persepolis",
    "title": "Incendie de Persépolis",
    "start": -329,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Incendie du printemps 330, sans doute vers mai ; les circonstances (décision politique ou banquet) divergent selon les sources.",
    "era": "classique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "persepolis",
    "people": [
      "alexandre-le-grand",
      "parmenion"
    ],
    "summary": "Au printemps 330, après y avoir passé l'hiver, Alexandre fait incendier les palais de Persépolis, cœur cérémoniel de l'empire achéménide. Arrien y voit une décision réfléchie, vengeance des temples d'Athènes brûlés par Xerxès en 480 ; d'autres auteurs, un geste d'ivresse suggéré par la courtisane athénienne Thaïs.",
    "body": "**La prise.** Entré à Persépolis au début de 330, Alexandre livre la ville basse au pillage et s'empare du trésor royal : 120 000 talents selon Diodore et Quinte-Curce, une somme énorme, emportée par des milliers de bêtes de somme. Il reste dans la région environ quatre mois.\n\n**L'incendie.** Arrien, qui suit Ptolémée et Aristobule, rapporte que Parménion conseilla d'épargner ce qui appartenait désormais au roi, et qu'Alexandre voulut punir les Perses pour l'invasion de la Grèce. Diodore, Plutarque et Quinte-Curce racontent un banquet où Thaïs, future maîtresse de Ptolémée, invite les convives à brûler le palais de Xerxès ; Alexandre jette la première torche. Plutarque ajoute qu'il regretta aussitôt son geste.\n\n**Ce que montrent les fouilles.** Les fouilles de l'Institut oriental de Chicago, dans les années 1930, ont trouvé d'épaisses couches de cendres dans l'Apadana, la salle aux Cent Colonnes et le trésor, vidé auparavant. Les deux versions ne s'excluent pas : beaucoup d'historiens y voient un geste politique, qui annonce aux Grecs la fin de la guerre de vengeance.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "III, 18, 10 à 12"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 70 à 72",
        "url": `${DIODORE}:book=17:chapter=70`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "37 à 38",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "V, 6 à 7"
      },
      {
        "kind": "modern",
        "author": "Erich F. Schmidt",
        "work": "Persepolis, 3 vol., Chicago, University of Chicago Press, 1953-1970"
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      }
    ]
  },
  {
    "id": "mort-de-darius-iii",
    "title": "Mort de Darius III",
    "start": -329,
    "month": 7,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Arrien date la mort du mois d'Hécatombéon, sous l'archonte Aristophon, soit vers juillet 330 ; la conversion est incertaine d'environ un mois. Le lieu exact n'est pas connu.",
    "era": "classique",
    "track": "perse",
    "category": "politics",
    "importance": 2,
    "placeId": "hecatompylos",
    "people": [
      "darius-iii",
      "bessos",
      "alexandre-le-grand"
    ],
    "summary": "En juillet 330, Darius III, en fuite vers l'est devant Alexandre, est arrêté par ses propres satrapes, menés par Bessos, satrape de Bactriane. Rattrapés par la cavalerie macédonienne, les conjurés le poignardent et l'abandonnent. Avec lui s'éteint la dynastie achéménide, et Alexandre se pose en successeur légitime.",
    "body": "**La fuite.** Après Gaugamèles, Darius se réfugie à Ecbatane, puis fuit vers les satrapies orientales quand Alexandre approche. Ses compagnons le déposent et l'enchaînent, avec des chaînes d'or selon Quinte-Curce. Alexandre lance une poursuite épuisante, avec ses meilleurs cavaliers, au-delà des Portes Caspiennes.\n\n**La mort.** Rejoints, les conjurés frappent Darius et s'enfuient. Arrien dit qu'il était mort quand Alexandre arriva ; Plutarque, qu'un soldat macédonien le trouva mourant et lui donna à boire. Alexandre fait envoyer le corps à Persépolis pour des funérailles royales. Bessos se proclame roi sous le nom d'Artaxerxès V ; livré à Alexandre en 329, il est mutilé puis exécuté.\n\n**Ce qui est incertain.** Le lieu exact de la mort n'est pas connu : il se situe en Parthie, à l'est des Portes Caspiennes, peut-être près d'Hécatompylos ; Justin nomme un village, Thara. La date (mois d'Hécatombéon, sous l'archonte Aristophon) vient d'Arrien.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "III, 19 à 22 ; IV, 7, 3"
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "V, 8 à 13"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "42 à 43",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 73",
        "url": `${DIODORE}:book=17:chapter=73`
      },
      {
        "kind": "ancient",
        "author": "Justin",
        "work": "Abrégé des Histoires philippiques de Trogue Pompée",
        "locus": "XI, 15"
      },
      {
        "kind": "modern",
        "author": "Pierre Briant",
        "work": "Histoire de l'Empire perse, de Cyrus à Alexandre, Paris, Fayard, 1996"
      }
    ]
  },
  {
    "id": "bataille-de-l-hydaspe",
    "title": "Bataille de l'Hydaspe",
    "start": -325,
    "month": 5,
    "precision": "month",
    "certainty": "attested",
    "certaintyNote": "Arrien donne le mois de Mounychion, sous l'archonte Hégémon (avril ou mai 326), mais décrit un fleuve gonflé par les pluies d'été : certains historiens préfèrent juillet.",
    "era": "classique",
    "track": "alexandre",
    "category": "war",
    "importance": 2,
    "placeId": "hydaspe",
    "people": [
      "alexandre-le-grand",
      "poros",
      "cratere"
    ],
    "summary": "Au printemps 326, au bord de l'Hydaspe, l'actuel Jhelum, Alexandre affronte le roi indien Poros et ses éléphants de guerre. Il franchit le fleuve en crue de nuit, en amont du camp ennemi, et remporte sa dernière grande bataille rangée. Poros, blessé, est maintenu dans son royaume comme allié.",
    "body": "**La traversée.** Poros garde la rive opposée avec son armée et ses éléphants, que les chevaux macédoniens refusent d'affronter. Pendant des nuits, Alexandre multiplie les feintes, puis traverse à 150 stades (environ 27 km) en amont, sous un orage, avec une partie de l'armée, tandis que Cratère reste face au camp indien. Arrien prête à Poros environ 30 000 fantassins, 4 000 cavaliers, 300 chars et 200 éléphants ; Diodore donne d'autres chiffres.\n\n**La bataille.** La cavalerie d'Alexandre bouscule les cavaliers indiens, puis la phalange affronte les éléphants, qui font des ravages dans les deux camps avant de refluer. Poros, blessé, se rend ; à Alexandre qui lui demande comment le traiter, il aurait répondu : « en roi ». Alexandre lui rend son royaume, agrandi, et fonde deux villes, Nicée et Bucéphalie, du nom de son cheval Bucéphale, mort à cette époque.\n\n**La date.** Arrien place la bataille au mois de Mounychion, soit vers avril ou mai 326, mais il décrit aussi le fleuve gonflé par les pluies d'été, ce qui fait pencher certains historiens pour juillet. Quelques mois plus tard, sur l'Hyphase, l'armée refuse d'aller plus loin.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "V, 8 à 19"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "60 à 62",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 87 à 89",
        "url": `${DIODORE}:book=17:chapter=87`
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "VIII, 13 à 14"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Alexander and the East: The Tragedy of Triumph, Oxford, Clarendon Press, 1996"
      }
    ]
  },
  {
    "id": "noces-de-suse",
    "title": "Noces de Suse",
    "start": -323,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Noces du printemps 324 ; le jour exact n'est pas connu.",
    "era": "classique",
    "track": "alexandre",
    "category": "society",
    "importance": 2,
    "placeId": "suse",
    "people": [
      "alexandre-le-grand",
      "hephaistion",
      "seleucos-ier"
    ],
    "summary": "Au printemps 324, à Suse, Alexandre épouse deux princesses achéménides, une fille de Darius III et une fille d'Artaxerxès III, et marie environ 80 de ses Compagnons à des filles de la noblesse perse et mède. Ces noces collectives, célébrées selon le rite perse, affichent l'union des élites des deux peuples.",
    "body": "**Les noces.** Selon Arrien, qui suit Aristobule, Alexandre épouse l'aînée des filles de Darius, que la plupart des sources nomment Stateira (Arrien l'appelle Barsine), et Parysatis, fille d'Artaxerxès III. Les mariages sont célébrés le même jour, selon le rite perse : chaque époux boit à la santé de sa promise, qui vient s'asseoir près de lui. Héphaistion épouse Drypétis, autre fille de Darius, afin que ses enfants soient les cousins de ceux d'Alexandre. Charès de Mytilène, chambellan du roi, décrit cinq jours de fêtes.\n\n**La politique d'Alexandre.** Alexandre fait aussi recenser les Macédoniens qui ont pris une épouse asiatique, plus de 10 000, et leur fait des présents, puis paye les dettes de ses soldats. Au même moment arrivent à Suse 30 000 jeunes Iraniens formés à la macédonienne, les Épigones, ce qui inquiète les vétérans.\n\n**Ce qu'il en reste.** La plupart de ces unions sont rompues après la mort d'Alexandre. Séleucos, qui garde son épouse Apama, fille d'un chef sogdien, fait exception : leur fils Antiochos Ier régnera sur l'empire séleucide. Le sens de ces noces, fusion des peuples ou simple alliance avec l'aristocratie perse, divise les historiens.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "VII, 4, 4 à 8 ; VII, 5 ; VII, 6, 1"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "70 à 71",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 107, 6",
        "url": `${DIODORE}:book=17:chapter=107`
      },
      {
        "kind": "ancient",
        "author": "Athénée",
        "work": "Deipnosophistes",
        "locus": "XII, 538b à 539a"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "mutinerie-d-opis",
    "title": "Mutinerie et banquet d'Opis",
    "start": -323,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Été 324 ; le jour exact n'est pas connu.",
    "era": "classique",
    "track": "alexandre",
    "category": "politics",
    "importance": 3,
    "placeId": "opis",
    "people": [
      "alexandre-le-grand",
      "cratere"
    ],
    "summary": "À l'été 324, à Opis, sur le Tigre, Alexandre annonce le renvoi en Macédoine des vétérans usés ou blessés. L'armée macédonienne se mutine et lui reproche de lui préférer les Perses. Alexandre fait exécuter les meneurs, confie des commandements à des Perses, puis se réconcilie avec ses soldats lors d'un immense banquet.",
    "body": "**La mutinerie.** Les Macédoniens, inquiets de l'arrivée des Épigones iraniens et de l'entrée de cavaliers orientaux dans les unités d'élite, demandent à partir tous, et raillent le roi : qu'il fasse campagne avec son père Ammon. Alexandre fait arrêter treize meneurs, livrés à l'exécution, puis prononce un discours, recomposé par Arrien, où il rappelle tout ce que les Macédoniens doivent à Philippe et à lui.\n\n**La réconciliation.** Au bout de trois jours, Alexandre commence à attribuer à des Perses des titres et des unités macédoniennes. Les soldats viennent alors supplier à la porte de son palais. Un banquet réunit 9 000 convives, Macédoniens autour du roi, Perses ensuite, puis gens des autres peuples ; Alexandre prie pour la concorde (homonoia) et l'association des Macédoniens et des Perses au pouvoir. Environ 10 000 vétérans repartent ensuite vers la Macédoine sous la conduite de Cratère.\n\n**Une prière discutée.** L'historien W. W. Tarn voyait dans cette prière le rêve d'une fraternité de tous les hommes. La plupart des historiens, à la suite d'Ernst Badian, y lisent plutôt une alliance politique entre les élites macédonienne et perse, au service du roi.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "VII, 8 à 12"
      },
      {
        "kind": "ancient",
        "author": "Quinte-Curce",
        "work": "Histoires d'Alexandre le Grand",
        "locus": "X, 2 à 4"
      },
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "XVII, 109",
        "url": `${DIODORE}:book=17:chapter=109`
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "71",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "modern",
        "author": "Ernst Badian",
        "work": "Alexander the Great and the Unity of Mankind, Historia, 7, 1958"
      },
      {
        "kind": "modern",
        "author": "A. B. Bosworth",
        "work": "Conquest and Empire: The Reign of Alexander the Great, Cambridge, Cambridge University Press, 1988"
      }
    ]
  },
  {
    "id": "aristote-fonde-le-lycee",
    "title": "Aristote ouvre son école au Lycée",
    "start": -334,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Retour d'Aristote à Athènes daté de l'archontat d'Évainétos (335/334) par le chronographe Apollodore, cité par Diogène Laërce.",
    "era": "classique",
    "track": "athenes",
    "category": "culture",
    "importance": 2,
    "placeId": "lycee",
    "people": [
      "aristote"
    ],
    "summary": "En 335/334, Aristote, ancien élève de Platon et précepteur d'Alexandre, revient à Athènes et enseigne au Lycée, un gymnase consacré à Apollon Lykeios, à l'est de la ville. Pendant douze ans, il y organise avec ses élèves des recherches sur presque tous les savoirs, de la logique à la biologie et à l'histoire des constitutions.",
    "body": "**De l'Académie au Lycée.** Né à Stagire, en Chalcidique, en 384, Aristote étudie une vingtaine d'années à l'Académie, jusqu'à la mort de Platon en 348/347. Après des séjours à Assos et à Mytilène, il est appelé par Philippe II pour éduquer Alexandre à Miéza. Revenu à Athènes, il n'y est qu'un étranger résident (métèque) et ne peut posséder de terrain : il enseigne dans un gymnase public.\n\n**Une école de recherche.** Ses élèves, appelés péripatéticiens, peut-être parce qu'il enseignait en marchant le long d'une allée couverte (peripatos), rassemblent des observations sur les animaux, les plantes et les régimes politiques : la Constitution des Athéniens est issue d'une collection de 158 constitutions. Après la mort d'Alexandre, menacé d'un procès pour impiété, Aristote se retire à Chalcis, où il meurt en 322 ; Théophraste lui succède.\n\n**Les vestiges.** En 1996, des fouilles préventives près de la rue Rigillis, dans le centre d'Athènes, ont mis au jour une palestre identifiée comme celle du Lycée. Les dates de la vie d'Aristote viennent surtout de Diogène Laërce, qui cite le chronographe Apollodore.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diogène Laërce",
        "work": "Vies et doctrines des philosophes illustres",
        "locus": "V, 1 à 11"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "7 à 8",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Denys d'Halicarnasse",
        "work": "Première lettre à Ammée",
        "locus": "5"
      },
      {
        "kind": "modern",
        "author": "John Patrick Lynch",
        "work": "Aristotle's School: A Study of a Greek Educational Institution, Berkeley, University of California Press, 1972"
      }
    ]
  },
  {
    "id": "aphrodite-de-cnide",
    "title": "L'Aphrodite de Cnide de Praxitèle",
    "start": -349,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Statue datée de 360 à 340 environ, d'après la carrière de Praxitèle ; aucune source ne donne l'année.",
    "era": "classique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 2,
    "placeId": "cnide",
    "people": [
      "praxitele"
    ],
    "summary": "Vers 350, le sculpteur athénien Praxitèle réalise pour Cnide, en Carie, une statue de marbre d'Aphrodite entièrement nue, la première grande statue de la déesse ainsi représentée. Admirée dans toute l'Antiquité, elle est perdue, mais connue par de nombreuses copies romaines.",
    "body": "**Une commande célèbre.** Selon Pline l'Ancien, Praxitèle avait sculpté deux Aphrodites : les habitants de Cos choisirent la statue drapée, jugée plus convenable, et ceux de Cnide prirent la nue. Placée dans un petit sanctuaire, visible de tous côtés, elle attire les voyageurs. Pline raconte que le roi Nicomède de Bithynie offrit de payer toute la dette de la cité pour l'acquérir, et que les Cnidiens refusèrent.\n\n**Un tournant.** Jusque-là, la sculpture grecque montrait des hommes nus, mais des déesses vêtues. Praxitèle représente Aphrodite au moment du bain, posant son vêtement sur un vase, dans une attitude de pudeur. Ses œuvres, aux corps souples et aux surfaces polies, influencent durablement la sculpture grecque puis romaine.\n\n**Ce qui est incertain.** L'original a disparu ; il aurait été emporté à Constantinople, où il aurait brûlé au Ve siècle apr. J.-C. Sa date n'est connue qu'à peu près : Pline place l'apogée de Praxitèle dans la 104e olympiade (de 364 à 361), et la statue est généralement datée de 360 à 340. Parmi les copies les plus fidèles figurent la Vénus Colonna du Vatican et la Vénus Braschi de Munich.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pline l'Ancien",
        "work": "Histoire naturelle",
        "locus": "XXXIV, 50 ; XXXVI, 20 à 22"
      },
      {
        "kind": "ancient",
        "author": "Pseudo-Lucien",
        "work": "Les Amours",
        "locus": "13 à 17"
      },
      {
        "kind": "modern",
        "author": "Alain Pasquier et Jean-Luc Martinez (dir.)",
        "work": "Praxitèle, Paris, Musée du Louvre éditions et Somogy, 2007"
      },
      {
        "kind": "modern",
        "author": "Christine Mitchell Havelock",
        "work": "The Aphrodite of Knidos and Her Successors, Ann Arbor, University of Michigan Press, 1995"
      }
    ]
  },
  {
    "id": "lysippe-sculpteur-d-alexandre",
    "title": "Lysippe, sculpteur d'Alexandre",
    "start": -329,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Pline place l'apogée de Lysippe dans la 113e olympiade (de 328 à 325) ; ses œuvres sont difficiles à dater précisément.",
    "era": "classique",
    "track": "monde-grec",
    "category": "culture",
    "importance": 3,
    "placeId": "sicyone",
    "people": [
      "lysippe",
      "alexandre-le-grand"
    ],
    "summary": "Vers 330, Lysippe de Sicyone, sculpteur sur bronze, est au sommet de sa carrière. Seul autorisé, selon Plutarque, à représenter Alexandre, il fixe l'image du roi conquérant, la tête légèrement inclinée et la chevelure dressée au-dessus du front. Il impose aussi au corps humain de nouvelles proportions, plus élancées.",
    "body": "**Un artiste prolifique.** Pline attribue à Lysippe 1 500 œuvres, presque toutes en bronze, et place son apogée dans la 113e olympiade (de 328 à 325). Il réduit la taille de la tête et allonge le corps ; selon Pline, il disait que ses prédécesseurs représentaient les hommes tels qu'ils étaient, et lui tels qu'ils paraissaient. Son Apoxyomène, un athlète qui se nettoie avec un strigile, est connu par une copie en marbre conservée au Vatican.\n\n**Le portraitiste du roi.** Alexandre aurait réservé son portrait sculpté à Lysippe, comme sa peinture à Apelle et ses gravures sur pierre fine à Pyrgotélès. Après le Granique, il lui commande un groupe de bronze représentant les 25 Compagnons tombés au premier choc, dressé à Dion, en Macédoine, puis emporté à Rome au IIe siècle av. J.-C.\n\n**Ce qui est incertain.** Aucun original sûr de Lysippe n'est conservé : ses œuvres sont connues par des copies romaines et des descriptions, et les attributions restent souvent discutées. Les portraits d'Alexandre qui nous sont parvenus, comme l'hermès Azara du Louvre, ne sont que des reflets plus ou moins fidèles de ses modèles.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pline l'Ancien",
        "work": "Histoire naturelle",
        "locus": "VII, 125 ; XXXIV, 37, 51 et 61 à 65"
      },
      {
        "kind": "ancient",
        "author": "Plutarque",
        "work": "Vie d'Alexandre",
        "locus": "4, 1",
        "url": `${PLUTARQUE}/Alexander*/home.html`
      },
      {
        "kind": "ancient",
        "author": "Arrien",
        "work": "Anabase d'Alexandre",
        "locus": "I, 16, 4"
      },
      {
        "kind": "modern",
        "author": "Andrew Stewart",
        "work": "Faces of Power: Alexander's Image and Hellenistic Politics, Berkeley, University of California Press, 1993"
      }
    ]
  },
  {
    "id": "theatre-d-epidaure",
    "title": "Le théâtre d'Épidaure",
    "start": -329,
    "precision": "decade",
    "certainty": "debated",
    "certaintyNote": "Date discutée : vers 340 à 330 d'après l'attribution de Pausanias à Polyclète, sans doute le Jeune ; vers 300 pour la première phase selon l'étude architecturale d'Armin von Gerkan et Wolfgang Müller-Wiener (1961).",
    "era": "classique",
    "track": "monde-grec",
    "category": "building",
    "importance": 2,
    "placeId": "theatre-d-epidaure",
    "summary": "Dans le sanctuaire d'Asclépios à Épidaure, un grand théâtre de pierre est construit à la fin du IVe siècle ou vers 300. Pausanias le jugeait sans rival pour son harmonie et sa beauté. Remarquablement conservé, réputé pour son acoustique, il accueille encore des représentations chaque été.",
    "body": "**Le sanctuaire d'Asclépios.** Au IVe siècle, le sanctuaire du dieu guérisseur, à environ 8 km de la ville d'Épidaure, connaît un grand essor : on y bâtit un nouveau temple, la tholos et de vastes portiques où dorment les malades venus chercher un rêve de guérison. Le théâtre, adossé au mont Kynortion, sert aux concours organisés en l'honneur du dieu.\n\n**Le monument.** Les gradins, un peu plus qu'un demi-cercle, entourent un orchestre circulaire de près de 20 mètres de diamètre. Les 34 rangées du bas ont été complétées plus tard par 21 rangées supplémentaires, ce qui porte la capacité à 12 000 ou 14 000 spectateurs. La pente régulière et la forme des gradins assurent une acoustique remarquable.\n\n**Une date discutée.** Pausanias attribue le théâtre à Polyclète, sans doute le Jeune, architecte de la tholos, ce qui a conduit à le dater vers 340 à 330. L'étude architecturale d'Armin von Gerkan et Wolfgang Müller-Wiener place plutôt la première phase vers 300 et l'agrandissement au IIe siècle av. J.-C. Le site le place vers 330, avec cette incertitude.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 27, 5",
        "url": `${PAUSANIAS}:book=2:chapter=27`
      },
      {
        "kind": "modern",
        "author": "Armin von Gerkan et Wolfgang Müller-Wiener",
        "work": "Das Theater von Epidauros, Stuttgart, Kohlhammer, 1961"
      },
      {
        "kind": "modern",
        "author": "R. A. Tomlinson",
        "work": "Epidauros, Londres, Granada, 1983"
      }
    ]
  }
]
