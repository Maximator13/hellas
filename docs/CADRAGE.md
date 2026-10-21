# Cadrage (phase 0)

Décisions de cadrage proposées pour Hellas, à valider avant la phase 1. Années astronomiques entre parenthèses (1 av. J.-C. = 0).

## 1. Bornes

**De 1600 à 30 av. J.-C., avec un prologue minoen depuis 2000.** La frise s'ouvre en 2000 (-1999) et se ferme en 30 (-29).

- Avant 1600, aucune écriture lisible (le linéaire A n'est pas déchiffré) et aucun événement datable : partir de 3200 laisserait 1 600 ans de frise presque vides. Le prologue garde Cnossos et Théra sans étirer l'échelle.
- 1600 correspond aux tombes à fosse de Mycènes (cercles A et B) : c'est le « de Mycènes » du titre.
- 30 est la fin conventionnelle de l'époque hellénistique. S'arrêter en 146 couperait l'Orient grec (Pergame en 133, Mithridate, sac d'Athènes en 86, fin des Séleucides, Égypte lagide). La frise se raccorde ainsi à Roma, qui couvre Actium et Auguste. Le sac de Corinthe (146) reste un événement.

## 2. Époques

Intervalles semi-ouverts : une époque commence à sa borne incluse et s'arrête juste avant la suivante. Thermopyles et Salamine (-479) sont donc classiques, Marathon (-489) archaïque, la mort d'Alexandre (-322) hellénistique.

| id | Libellé | Bornes | Astro | Conventions concurrentes expliquées sur le site |
|---|---|---|---|---|
| `bronze` | Âge du bronze égéen | de 3200 à 1100 (affiché depuis 2000) | -1999 à -1100 | début vers 3100 ou 3000 ; chronologie relative minoenne et helladique ; chronologies haute et basse liées à Théra |
| `ages-obscurs` | Âges obscurs | de 1100 à 800 | -1099 à -800 | « Haut Âge du fer » ; submycénien, protogéométrique, géométrique ; Lefkandi nuance l'obscurité |
| `archaique` | Époque archaïque | de 800 à 480 | -799 à -480 | début en 776 ou 750 ; fin en 510, 508, 490 ou 479 |
| `classique` | Époque classique | de 480 à 323 | -479 à -323 | début en 510, 508 ou 490 ; fin en 338 (Chéronée) ou 336 |
| `hellenistique` | Époque hellénistique | de 323 à 30 | -322 à -29 | début en 336 ou 334 ; fin en 146, 31 ou 27 |

Étalonnage de chaque époque : celui de la section 7 du brief (ocre et rouge de Cnossos, tons terreux et feu de foyer, couleurs vives des korès, marbre blanc et bleu égéen à midi, or et pourpre de fin d'après-midi).

## 3. Pistes

Dix-huit pistes, chacune avec deux plages : `active` (visible au zoom) et `overview` (visible en vue d'ensemble). Avec les fenêtres ci-dessous, jamais plus de six pistes à la fois en vue d'ensemble (six en 336, en 312 et en 280 ; cinq en 480). La Macédoine antigonide reste dans `macedoine` : même royaume, autre dynastie.

| id | Libellé | Active | Vue d'ensemble | Capitale (Pleiades) |
|---|---|---|---|---|
| `minoens` | Crète minoenne | de 1950 à 1450 env. | oui | Cnossos (589872) |
| `myceniens` | Royaumes mycéniens | de 1600 à 1100 env. | oui | Mycènes (570491) |
| `monde-grec` | Monde grec (sanctuaires, colonies, culture) | de 1100 à 30 | oui | Delphes (540726), Olympie (570531) |
| `athenes` | Athènes | de 800 à 86 | jusqu'en 322 | Athènes (579885) |
| `sparte` | Sparte | de 800 à 192 | jusqu'en 371 | Sparte (570685) |
| `corinthe` | Corinthe | de 750 à 146 | non | Corinthe (570182) |
| `thebes` | Thèbes et Béotie | de 550 à 335 | non | Thèbes (541138) |
| `ionie` | Ionie et Milet | de 700 à 334 | non | Milet (599799) |
| `occident` | Syracuse et Grecs d'Occident | de 733 à 212 | oui | Syracuse (462503) |
| `perse` | Empire perse achéménide | de 550 à 330 | oui | Persépolis (922695), Suse (912936) |
| `macedoine` | Macédoine (Argéades puis Antigonides) | de 650 à 168 | dès 359 | Aigai (491512) puis Pella (491687) |
| `alexandre` | Empire d'Alexandre et Diadoques | de 336 à 301 | oui | Pella puis Babylone (893951) |
| `lagides` | Égypte lagide | de 323 à 30 | oui | Alexandrie (727070) |
| `seleucides` | Empire séleucide | de 312 à 63 | oui | Séleucie du Tigre (894084) puis Antioche (658381) |
| `pergame` | Pergame attalide | de 282 à 133 | non | Pergame (550812) |
| `rhodes` | Rhodes | de 408 à 43 | non | Rhodes (590030) |
| `ligues` | Ligues achéenne et étolienne | de 280 à 146 | non | Aigion (570049), Thermon (541139) |
| `rome` | Rome | de 280 à 30 | oui | Rome (423025) |

Chaque piste reçoit une couleur propre, partagée par la frise et la carte. Les rangées de la frise sont dérivées des pistes (Roma les fixait en dur), et la validation refuse deux pistes qui se chevauchent sur une même rangée.

## 4. Carte

**Emprise des données : de 7 ouest à 78 est, de 22 à 49 nord** (85 degrés sur 27).

| Bord | Lieux qui le fixent |
|---|---|
| Ouest | Colonnes d'Héraclès (-5,4) et Mainaké (-4,1) pour Tartessos ; Emporion (3,1) et Massalia (5,4) |
| Nord | Tanaïs (47,3) et Olbia (46,7) |
| Est | Hyphase (75,5), Alexandrie Eschatè (69,6), Phasis (41,7) |
| Sud | Syène (24,1), Patala (24,7), oasis d'Ammon (29,2), Cyrène (32,8), Naucratis (30,9) |

Une seule boîte de données (relief, territoires), trois cadrages de caméra : `egee` (de 19 à 30,5 est, de 34,5 à 42 nord ; par défaut jusqu'en 336), `mediterranee` (de 7 ouest à 42,5 est, de 29 à 49 nord ; colonisation), `orient` (de 19 à 78 est, de 22 à 45 nord ; Alexandre et les royaumes).

**Relief.** Roma utilisait 60 pixels par degré ; ici, cela donnerait 5 100 pixels de large, au-delà de la limite de 4 096 de nombreux GPU mobiles.

| Option | Contenu | Netteté en Égée | Poids estimé |
|---|---|---|---|
| A | une texture de 4 080 × 1 296 (48 px par degré) | environ 1,8 km par pixel, un peu moins net que Roma | 1,3 Mo |
| B | A plus une texture de détail de l'Égée (160 px par degré), chargée au zoom | environ 0,5 km par pixel | 1,3 Mo puis 0,6 Mo à la demande |
| C | deux textures de 4 080 (96 px par degré) | environ 0,9 km par pixel partout | 5 Mo, premier écran hors budget |

Recommandation : **A en phase 1, B en phase 2** si l'Égée paraît floue sur les captures.

**Territoires.** Le rendu de Roma ne connaît que deux teintes (piste principale et le reste). Il faut un rendu multicolore : une couleur par puissance, des frontières tracées entre voisins, le nom de chaque puissance sur la carte. Cliopatria couvre les grands États (voir section 5) mais ni Athènes, ni Sparte, ni Corinthe, ni Syracuse, ni la ligue de Délos : ces territoires seront tracés à la main, sources citées, avec des bords flous qui disent l'imprécision. Les colonies sont des points instanciés (des centaines possibles), étiquetés seulement pour les plus importantes.

Instantanés pour la phase 2 : vers 1250, 480, 431, 323, 200, plus 30 pour l'état final.

## 5. Sources de données et licences

Vérifiées le 21 octobre 2026.

| Source | Licence | Usage prévu | Verdict |
|---|---|---|---|
| Cliopatria v0.2.1 (Seshat) | CC BY 4.0 | territoires des grands États | oui, avec corrections à l'import |
| Pleiades v4.1 | CC BY 3.0 | lieux, coordonnées (`places.csv`, champ `reprPoint`) | oui |
| Wikidata, propriété P8137 (Inventory of Archaic and Classical Poleis) | CC0 | liste des cités : 816 poleis, dont 751 avec coordonnées et 747 avec identifiant Pleiades | oui |
| ETOPO 2022 (NOAA) | CC0 1.0 | relief de la carte ; extrait à refaire jusqu'à 78 est (celui de Roma s'arrête à 53) | oui |
| Natural Earth 5.1.2 | domaine public | côtes, lacs, rivières (`ne_10m_rivers_lake_centerlines`) ; retirer les barrages modernes, redessiner le lac Copaïs | oui |
| Copernicus DEM GLO-30 | licence Copernicus DEM, mention obligatoire | relief des scènes | oui, avec la mention et la clause de non-responsabilité |
| AWMC geodata | ODbL 1.0 (versions d'avant juin 2016 en NC, exclues) | côtes antiques retouchées (delta du Méandre pour Milet, golfe Thermaïque pour Pella) | oui sous conditions : fichiers dérivés isolés et publiés sous ODbL |
| ToposText | contradictoire (ODC-By déclarée, « All Rights Reserved » en pied de page) | recoupement seulement | à décider |
| Sons Freesound, Wikimedia Commons, xeno-canto | CC0 ou domaine public, vérifiés son par son | ambiances ; les 26 sons de Roma (11 Mo) sont réutilisables | oui |
| DARE | CC BY-SA 3.0 | aucun | à éviter |
| POLIS (Stanford) | aucune licence | aucun | à éviter |

**Cliopatria en détail.** Couverts : Minoens (de 1600 à 1401), Mycéniens (de 1500 à 1101), un bloc « Greek City-States » pour toutes les poleis (de 800 à 77 apr. J.-C.), ligue du Péloponnèse (de 550 à 338), Perse achéménide, Lydie, Phrygie, Macédoine (de 675 à 292), Carthage, Thrace odryse, Bosphore, Lagides, Séleucides, Antigonides, Pergame, Rhodes (de 188 à 165 seulement), ligues achéenne et étolienne, Gréco-Bactriens, Pont, Rome. Défauts à corriger à l'import :
- de 331 à 324, les conquêtes d'Alexandre sont étiquetées « Ptolemaic Kingdom » : à renommer ;
- l'Attique est vide de 480 à 405 (ni ligue de Délos ni empire athénien), la Grèce continentale vide de 337 à 324 (ligue de Corinthe) ;
- l'Égypte des XXVIIIe et XXIXe dynasties (de 404 à 380) est comptée comme perse ; la dynastie saïte commence en 615 au lieu de 664 ;
- côtes grossières : Syracuse, Tarente, Rhodes, Byzance, Panticapée tombent de 2 à 10 km hors des polygones ; découper et dilater sur le masque Natural Earth.

À tracer à la main (travail propre, sources citées) : ligue de Délos et empire athénien ; territoires d'Athènes, Sparte, Corinthe, Argos, Thèbes, Thessalie ; Épire de Pyrrhos ; Syracuse et Tarente ; ligue de Corinthe ; Égypte de 404 à 343 ; Mycènes avant 1500 ; Rhodes et sa pérée avant 188. Aucun jeu ouvert n'existe pour les colonies (métropole et date) ni pour l'itinéraire d'Alexandre : les deux seront construits à partir de Pleiades et de Wikidata.

**Polices (Fontsource, OFL 1.1).** Texte courant : EB Garamond, comme Roma, qui couvre le grec polytonique (ajouter les sous-ensembles `greek` et `greek-ext`, absents de Roma). Cinzel n'a pas de grec. Pour les titres :

| Police | Grec | Allure |
|---|---|---|
| Didact Gothic | polytonique | linéale à trait uniforme, O rond ; en capitales espacées, évoque l'écriture stoichédon des inscriptions attiques |
| GFS Neohellenic | polytonique | reprise du New Hellenic de 1927, faible contraste, la plus « grecque » des trois |
| Ysabeau SC | monotonique | petites capitales humanistes évasées, graisses fines proches de la lettre incisée |

Recommandation : Didact Gothic en phase 1, à confirmer en phase 2 sur une planche comparative du plan de design.

## 6. Premiers événements (phase 1)

Vingt événements, sur toutes les époques et plusieurs pistes ; cinq ne sont pas attestés. Identifiants Pleiades vérifiés un par un. Les dates discutées sont dans `docs/A_VERIFIER.md`.

| id | Date | Certitude | Piste | Lieu (Pleiades) | Sources |
|---|---|---|---|---|---|
| `eruption-de-thera` | vers 1600 (fourchette de 1630 à 1500) | débattue | minoens | Akrotiri (599478) | Friedrich et al., *Science* 312 (2006) ; Manning, *A Test of Time Revisited* (2014) |
| `destruction-des-palais-myceniens` | de 1200 à 1180 env. | attestée | myceniens | Mycènes (570491) | Shelmerdine (dir.), *Cambridge Companion to the Aegean Bronze Age* (2008) ; Cline, *1177 av. J.-C.* (2014) |
| `guerre-de-troie` | de 1194 à 1184 selon Ératosthène | légendaire | myceniens | Troie (550595) | Homère, *Iliade* ; Hérodote, II, 145 ; Marbre de Paros, ép. 24 ; Clément, *Stromates*, I, 21 |
| `grand-edifice-de-lefkandi` | vers 950 | attestée | monde-grec | Lefkandi (176836030) | Popham, Calligas, Sackett, *Lefkandi* II.2 (1993) |
| `premiers-jeux-olympiques` | 776 | traditionnelle | monde-grec | Olympie (570531) | Pausanias, V, 8, 6 ; Plutarque, *Numa*, 1 |
| `fondation-de-syracuse` | 733 | traditionnelle | occident | Syracuse (462503) | Thucydide, VI, 3, 2 |
| `fondation-de-marseille` | vers 600 | traditionnelle | monde-grec | Massalia (148127) | Thucydide, I, 13, 6 ; Athénée, XIII, 576a |
| `reformes-de-clisthene` | 508/507 | attestée | athenes | Athènes (579885) | Hérodote, V, 66 et 69 ; Aristote, *Constitution d'Athènes*, 21 |
| `bataille-de-marathon` | août ou septembre 490 | attestée | athenes | Marathon (580021) | Hérodote, VI, 102 à 117 |
| `bataille-des-thermopyles` | fin d'été 480 | attestée | sparte | Thermopyles (541140) | Hérodote, VII, 201 à 233 ; Diodore, XI, 4 à 10 |
| `bataille-de-salamine` | fin septembre 480 | attestée | athenes | Salamine (580101) | Hérodote, VIII, 40 à 96 ; Eschyle, *Les Perses* |
| `construction-du-parthenon` | de 447 à 432, dédicace en 438 | attestée | athenes | Parthénon (168254096) | IG I³ 436 à 451 ; Philochore, FGrHist 328 F 121 ; Plutarque, *Périclès*, 13 |
| `guerre-du-peloponnese` | de 431 à 404 | attestée | sparte | Athènes (579885) | Thucydide, II, 2, 1 et V, 26 ; Xénophon, *Helléniques*, II, 2, 20 à 23 |
| `bataille-de-leuctres` | juillet 371 | attestée | thebes | Leuctres (540913) | Xénophon, *Helléniques*, VI, 4, 4 à 15 ; Plutarque, *Camille*, 19 |
| `bataille-de-cheronee` | août 338 | attestée | macedoine | Chéronée (540701) | Diodore, XVI, 85 et 86 ; Plutarque, *Camille*, 19 |
| `bataille-de-gaugameles` | 1er octobre 331 | attestée | alexandre | Gaugamèles (874478) | Arrien, III, 8 à 15 ; Plutarque, *Alexandre*, 31 ; journal astronomique babylonien (ADART I, -330) |
| `mort-d-alexandre` | 11 juin 323 | attestée | alexandre | Babylone (893951) | BM 45962 (ADART I, -322 B) ; Arrien, VII, 25 à 28 ; Plutarque, *Alexandre*, 75 et 76 |
| `bataille-d-ipsos` | été 301 | attestée | alexandre | Ipsos (609415) | Plutarque, *Démétrios*, 28 à 30 ; Diodore, XXI, 1 |
| `sac-de-corinthe` | 146 | attestée | corinthe | Corinthe (570182) | Pausanias, VII, 16, 7 à 10 ; Strabon, VIII, 6, 23 |
| `actium-et-mort-de-cleopatre` | de septembre 31 à août 30 | attestée | lagides | Actium (530772) | Dion Cassius, LI, 1, 1 ; Plutarque, *Antoine*, 65 à 68, 85 et 86 |

## 7. Plan de la phase 1 : fondations et déploiement

| # | Étape | Taille |
|---|---|---|
| 1 | Copier le moteur de Roma sans son historique ni ses scènes romaines ; `npm ci` ; `npm run check` au vert | petite |
| 2 | Identité Hellas : `site.ts`, `index.html`, Open Graph, favicon provisoire, clés de stockage local, manifeste d'assets vide, README, licences | petite |
| 3 | Bornes (-1999 à -29), cinq époques et leurs étalonnages, tests des dates | petite à moyenne |
| 4 | Dix-huit pistes : couleur, plage de vue d'ensemble, rangées dérivées, validation sans chevauchement | moyenne |
| 5 | Contenu : vingt événements, leurs lieux et personnes, une trentaine de villes, accueil qui explique « Hellas », pages légales (Mentions légales, Confidentialité, Conditions d'utilisation) | moyenne |
| 6 | Relief sur la nouvelle emprise (option A), points de contrôle du test refaits, cadrages de caméra | moyenne |
| 7 | Territoires : sources Cliopatria grecques, rendu multicolore avec frontières et noms ; tracés à la main reportés en phase 2 | grande |
| 8 | Tests de bout en bout, image de partage, `CREDITS.md`, contrôle des poids (premier écran sous 5 Mo) | petite |
| 9 | Dépôt public, Pages par GitHub Actions, push, vérifications en ligne (HTTPS, 404, sitemap, pages de partage) | petite |

Hors phase 1 : colonies en points (phase 2), cités tracées à la main (phase 2), camps grecs et perses du moteur de bataille, ordre dorique du kit Blender (phases 2 et 4).

## 8. Décisions à prendre

1. Bornes : de 2000 (prologue) à 30. Recommandé.
2. Ajouter une catégorie `nature` (Théra, séisme de Sparte en 464, engloutissement d'Hélikè en 373, chute du Colosse vers 227). Recommandé.
3. Relief : option A, puis B en phase 2 si besoin. Recommandé.
4. `robots.txt` : il n'est lu qu'à la racine du domaine (`maximator13.github.io/robots.txt`, aujourd'hui en 404). Roma s'en passe. Option recommandée : un petit dépôt public `maximator13.github.io` avec un `robots.txt` qui déclare les sitemaps de Roma et de Hellas (sert aussi à Roma).
5. Police des titres : Didact Gothic en provisoire, choix définitif en phase 2. Recommandé.
6. Mesure d'audience : GoatCounter sans cookie, comme Roma, désactivé tant que le code n'est pas créé. Recommandé.
7. ToposText : recoupement seulement, aucune donnée reprise. Recommandé.
8. AWMC (ODbL) : accepter les côtes antiques retouchées, dans des fichiers isolés sous ODbL. Recommandé.
