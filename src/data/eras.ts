import type { Era } from './schema.ts'

export const eras: Era[] = [
  {
    id: 'bronze',
    name: 'Âge du bronze égéen',
    start: -1999,
    end: -1099,
    summary:
      "En Crète, les Minoens bâtissent à partir de 1950 environ des palais comme Cnossos, centres d'une administration qui écrit en linéaire A, une écriture encore indéchiffrée. Vers 1600, des chefs du continent se font enterrer avec un or abondant dans les tombes à fosse de Mycènes ; leurs successeurs élèvent des palais (Mycènes, Pylos, Thèbes) et tiennent leurs archives en linéaire B, la plus ancienne forme écrite du grec. Vers 1450, Cnossos passe sous contrôle mycénien. Entre 1200 et 1180 environ, les palais sont détruits ou abandonnés, et l'écriture disparaît.",
    boundsNote:
      "Les archéologues font commencer l'âge du bronze égéen vers 3200 (parfois 3100 ou 3000), avec la diffusion du travail du bronze. Le site part de 2000, avec un prologue minoen, puis s'attarde à partir de 1600 sur les Mycéniens : avant cette date, aucune écriture lisible ni aucun événement datable ne remplirait la frise. Les dates absolues reposent sur des chronologies relatives (minoen, helladique et cycladique, découpés d'après la céramique), raccrochées à l'Égypte et au radiocarbone ; une chronologie haute et une chronologie basse divergent d'environ un siècle autour de l'éruption de Théra. La fin vers 1100 est elle aussi conventionnelle : certains la placent vers 1050, au début du protogéométrique.",
  },
  {
    id: 'ages-obscurs',
    name: 'Âges obscurs',
    start: -1099,
    end: -799,
    summary:
      "Après la chute des palais, la population diminue, l'écriture disparaît pendant plus de trois siècles et les échanges lointains se raréfient. Le fer remplace peu à peu le bronze pour les armes et les outils, et des Grecs s'installent sur la côte d'Asie Mineure (Éolide, Ionie, Doride). Les archéologues suivent cette période grâce à la céramique (submycénienne, protogéométrique, géométrique), dont Athènes fournit la séquence la plus complète. Des sites comme Lefkandi, en Eubée, montrent pourtant des chefs riches et des contacts avec le Levant dès le Xe siècle.",
    boundsNote:
      "« Âges obscurs » désigne d'abord le silence des sources : ni textes, ni grands monuments. Beaucoup d'historiens préfèrent parler de « haut âge du fer » et découpent la période d'après les styles céramiques : submycénien (de 1100 à 1050 environ), protogéométrique (de 1050 à 900 environ), géométrique (de 900 à 700 environ, à cheval sur l'époque archaïque). Les fouilles de Lefkandi ou d'Athènes nuancent l'idée d'un monde entièrement appauvri. La borne de 800 est un repère commode : l'écriture, les grands sanctuaires et les premières colonies réapparaissent peu après.",
  },
  {
    id: 'archaique',
    name: 'Époque archaïque',
    start: -799,
    end: -479,
    summary:
      "La cité (polis) s'affirme : un territoire, une communauté de citoyens, des sanctuaires et bientôt des lois écrites. Les Grecs adoptent l'alphabet phénicien, se retrouvent à Olympie et à Delphes, et fondent des colonies de la mer Noire à l'Espagne. Tyrans, législateurs et réformateurs transforment les institutions, jusqu'à la démocratie athénienne de Clisthène. La période s'achève par la révolte des cités d'Ionie contre la Perse et par la première expédition perse en Grèce, repoussée à Marathon en 490.",
    boundsNote:
      "Le début varie selon les auteurs : 800 (retour de l'écriture et des échanges), 776 (premiers Jeux olympiques selon la tradition) ou 750 (premières colonies). La fin aussi : 510 ou 508 (fin de la tyrannie à Athènes et réformes de Clisthène), 490 (Marathon) ou 479 (Platées). Le site retient 480, l'invasion de Xerxès : Marathon reste archaïque, les Thermopyles et Salamine ouvrent l'époque classique. L'adjectif « archaïque » vient de l'histoire de l'art du XIXe siècle et ne veut pas dire « primitif ».",
  },
  {
    id: 'classique',
    name: 'Époque classique',
    start: -479,
    end: -322,
    summary:
      "Victorieuse des Perses, Athènes prend la tête de la ligue de Délos, la transforme en empire maritime et finance les monuments de l'Acropole ; c'est le temps du théâtre, de l'histoire (Hérodote, Thucydide) et de la philosophie (Socrate, Platon, Aristote). La guerre du Péloponnèse (de 431 à 404) l'oppose à Sparte, qui l'emporte, avant d'être battue à son tour par Thèbes à Leuctres en 371. Philippe II de Macédoine impose ensuite son hégémonie à Chéronée (338), et son fils Alexandre conquiert l'empire perse jusqu'à l'Indus.",
    boundsNote:
      "Le site commence l'époque classique en 480, avec l'invasion de Xerxès ; d'autres retiennent 510 ou 508 (fin de la tyrannie et réformes de Clisthène), 490 (Marathon) ou 479 (Platées). La fin en 323, à la mort d'Alexandre, est la plus courante ; certains s'arrêtent à Chéronée (338) ou à la mort de Philippe II (336), quand les cités perdent leur indépendance de fait. Ces bornes viennent surtout de l'histoire d'Athènes et de l'histoire de l'art.",
  },
  {
    id: 'hellenistique',
    name: 'Époque hellénistique',
    start: -322,
    end: -29,
    summary:
      "À la mort d'Alexandre, ses généraux, les Diadoques, se disputent son empire pendant une quarantaine d'années ; trois grandes dynasties en sortent, les Lagides en Égypte, les Séleucides en Asie et les Antigonides en Macédoine, à côté de Pergame, de Rhodes et des ligues de cités. La langue commune (koinè), des villes nouvelles comme Alexandrie ou Antioche et des savants comme Euclide, Archimède ou Ératosthène diffusent la culture grecque de la Méditerranée à l'Afghanistan. À partir de 200, Rome intervient en Orient : elle abat la Macédoine (168), rase Corinthe (146), hérite de Pergame (133) et annexe la Syrie séleucide (en 64 ou 63). L'Égypte de Cléopâtre VII, dernier royaume issu de l'empire d'Alexandre, tombe en 30.",
    boundsNote:
      "Le mot « hellénistique » a été répandu au XIXe siècle par l'historien allemand Johann Gustav Droysen. Le début est le plus souvent fixé à la mort d'Alexandre (323), parfois à son avènement (336) ou à son passage en Asie (334). Pour la fin, certains s'arrêtent au sac de Corinthe (146), quand la Grèce passe sous l'autorité de Rome ; le site va jusqu'à Actium (31) et à la mort de Cléopâtre VII (30), d'autres jusqu'au principat d'Auguste (27).",
  },
]
