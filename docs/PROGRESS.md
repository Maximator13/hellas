# Avancement

## Phase 0 : cadrage (21 octobre 2026)

**Fait**
- Dépôt local créé, brief versionné dans `docs/BRIEF.md` (copie nettoyée de toute mention de l'outil de production), garde-fous locaux en place (hook de message de commit, exclusions, attribution vide).
- Lecture du moteur de Roma et inventaire de portage : moteur générique sauf l'identité du site, les bornes, les époques, les pistes, l'emprise de la carte et le rendu des territoires.
- Vérification des sources de données et de leurs licences, couverture réelle de Cliopatria pour le monde grec mesurée sur le fichier.
- Cadrage historique : bornes, époques, dix-huit pistes, emprise de la carte, vingt premiers événements sourcés, instantanés de carte pour la phase 2.
- Tout est dans `docs/CADRAGE.md` ; les points douteux dans `docs/A_VERIFIER.md`.

**Décisions** : section 8 de `docs/CADRAGE.md`, toutes prises le 21 octobre.

**Problèmes connus**
- Le rendu des territoires de Roma n'a que deux teintes : un rendu multicolore est nécessaire (phase 1, étape 7).
- Cliopatria ne connaît ni Athènes, ni Sparte, ni Corinthe, ni Syracuse, ni la ligue de Délos, et contient des erreurs d'étiquette (conquêtes d'Alexandre nommées « Ptolemaic Kingdom » de 331 à 324) : corrections à l'import et tracés à la main.
- `robots.txt` n'est lu qu'à la racine du domaine `maximator13.github.io`, qui n'existe pas.

**Suite** : phase 1.

## Phase 1 : fondations et déploiement (21 octobre 2026)

Site en ligne : https://maximator13.github.io/hellas/ (dépôt https://github.com/Maximator13/hellas).

**Fait**
- Moteur de Roma copié sans son historique ni ses scènes ; moteur de bataille retiré (il sera repris de Roma et adapté en phase 2 avec les camps grecs et perses).
- Identité Hellas : titre, description, Open Graph, image de partage, favicon provisoire (méandre), clés de stockage local, manifeste d'assets vide, README, licences, crédits.
- Années de -1999 à -29, cinq époques et leurs étalonnages (ocre et rouge de Cnossos, tons terreux, couleurs vives archaïques, marbre et bleu égéen à midi, or hellénistique).
- Frise : dix-huit pistes colorées ; quatre rangées secondaires attribuées dynamiquement aux pistes qui ont des événements à l'écran ; marqueurs d'événements à la couleur de leur piste (la forme porte toujours la certitude).
- Carte : emprise de 7 O à 78 E et de 22 à 49 N ; relief ETOPO 2022 à 30 secondes d'arc, en deux moitiés qui partagent la colonne de 35,5 E (2,3 Mo et 2,0 Mo) ; cadrage par période (Égée, Méditerranée des colonies, Orient d'Alexandre, royaumes hellénistiques).
- Territoires Cliopatria rattachés aux pistes grecques, avec l'erreur d'étiquette corrigée (conquêtes d'Alexandre de 331 à 324) : 248 tranches, 371 Ko ; rendu multicolore avec frontières entre voisins et nom de chaque puissance sur la carte.
- Contenu : 26 événements sourcés (au moins 3 par époque), 23 lieux, 48 personnes, 36 villes, identifiants Pleiades vérifiés ; pages Sources et crédits, Mentions légales, Confidentialité, Conditions d'utilisation ; accueil qui explique le nom Hellas.
- Polices : Didact Gothic (titres) et EB Garamond (texte), sous-ensembles grecs servis.
- Site racine `maximator13.github.io` : page d'accueil vers Roma et Hellas, `robots.txt` qui déclare les deux sitemaps, 404.

**Mesures**
- Premier écran : 3,0 Mo sur ordinateur (budget 5 Mo) ; la moitié est du relief (2,0 Mo) se charge ensuite.
- En ligne, Chromium au premier plan avec GPU : moteur 3D à 3,6 s (connexion à froid), territoires à 4,2 s, relief ouest à 4,6 s, relief est à 9,5 s.
- Site publié : 17,6 Mo, 76 fichiers.
- `npm run check` : 139 tests ; Playwright : 6 tests sur ordinateur en local, ordinateur et mobile en CI.
- Images par seconde : à relever sur le portable de mesure avec `?debug`.

**Problèmes connus**
- L'accueil s'ouvre au milieu de la frise, donc sur les âges obscurs, l'époque la plus sombre de l'étalonnage : premier coup d'œil moins éclatant que l'époque classique.
- Les noms des puissances chevauchent parfois ceux des villes en Grèce.
- Territoires absents de Cliopatria, à tracer à la main en phase 2 : Athènes et la ligue de Délos, Sparte avant 550 et après 338, Corinthe, Syracuse, Ionie, Rhodes avant 188, Égypte lagide de 322 à 308.
- Six pistes sans événement : Perse, Séleucides, Rome, Pergame, Rhodes, ligues.
- Graduation « 1 apr. J.-C. » visible au bout de la frise, dans la marge au-delà de 30 av. J.-C.

**Suite** : phase 2 (tranche verticale), validée par l'utilisateur le 21 octobre, à faire en autonomie.

## Phase 2 : tranche verticale (21 et 22 octobre 2026, faite sans validation, en autonomie)

Site : https://maximator13.github.io/hellas/ ; scènes : `#/scene/acropole` et `#/scene/thermopyles`.

**Fait**
- Accueil sur la frise de 800 à 30 av. J.-C., centrée sur l'époque classique (au lieu des âges obscurs, trop sombres pour un premier regard).
- Plan de design (`docs/DESIGN.md`) : palette « Nuit égéenne », Marbre de Paros, Pierre du Pentélique, Or de Phidias ; Didact Gothic et EB Garamond ; principes. Contrastes mesurés : 16,2, 10,6 et 9,3 pour 1.
- Lien de fin de frise vers Roma (« la suite : l'Empire romain », vers le principat d'Auguste) et lien depuis la fiche d'Actium.
- Piste « Mythes et héros » : 13 mythes placés aux dates des chronographes antiques (Marbre de Paros, Ératosthène, Eusèbe et Jérôme), tous légendaires ; la guerre de Troie y passe.
- Carte : 34 territoires tracés à la main là où Cliopatria manque (ligue de Délos et empire athénien en quatre périodes, Sparte et la Messénie, Corinthie, Syracuse de Gélon à Hiéron II, Tarente, Ionie, Béotie, Égypte de Ptolémée de 322 à 308, Rhodes et sa pérée), sans simplification ; itinéraires d'Alexandre (55 étapes) et des Dix Mille (21 étapes).
- Kit Blender grec : ordres dorique et ionique grecs, temple périptère, stoa, propylon, polychromie, figurines (citoyens, hoplites, Spartiates, Perses).
- Moteur de bataille porté depuis Roma avec des camps génériques, et enrichi (reddition, unités au camp, colonnes le long d'un sentier, sol en plusieurs morceaux, largeur des flèches).
- Scène des Thermopyles : proposition, relecture contradictoire, terrain Copernicus avec la côte de 480 restituée, 10 phases, 1 figurine pour 5 soldats, compteurs sourcés ; 4,2 Mo.
- Scène de l'Acropole vers 432 : proposition, relecture contradictoire, relief restitué, Parthénon peint avec l'Athéna Parthénos, Propylées inachevés, grande Athéna de bronze, vieux temple, pente sud, agora, Pnyx, ville, Longs Murs et ports, passants et fumées ; 14,2 Mo, environ 1,78 million de triangles, 340 appels de dessin.
- Script d'assets : plafond des textures réglable par texture (`largeTextures`) pour les terrains.

**Mesures**
- Thermopyles : 4,2 Mo ; Acropole : 14,2 Mo (budget 20 Mo).
- `npm run check` : 159 tests ; déploiements verts.
- Images par seconde : à relever sur le portable de mesure avec `?debug`, sur la carte et dans les deux scènes.

**Problèmes connus**
- Acropole : visage de l'Athéna Parthénos encore stylisé ; plafond à caissons très vif ; les points de vue tournés vers le soleil du matin restent en contre-jour ; le point « grande Athéna de bronze » est recadré dans la configuration de la scène (`views`) plutôt que dans le modèle.
- Thermopyles : légère irrégularité de la côte au loin ; figurines encore petites au dernier combat ; pas de clair de lune pour la marche de nuit ; sources chaudes déplacées au pied de la falaise (hypothèse).
- Figurines très simples (bras en bâtons, bouclier octogonal) : à affiner.
- Deux scènes seulement parmi celles de la section 10 du brief ; plans pré-rendus (vidéo) non encore produits.

**Suite** : phase 3 (environ 200 événements, figures, lieux, territoires de toutes les époques, recherche, quiz, mini-jeux), après validation ; ou reprise des défauts ci-dessus.

## Phase 3 : contenu et apprentissage (22 octobre 2026, faite sans validation, en autonomie)

**Fait**
- 207 événements sourcés (8, 21 et 3 à l'âge du bronze par importance ; 1, 1, 1 aux âges obscurs ; 7, 30, 10 à l'époque archaïque ; 7, 65, 11 à l'époque classique ; 7, 26, 9 à l'époque hellénistique), environ 150 personnes et une centaine de lieux reliés à Pleiades ; données réparties par période (`src/data/events-*.ts`, `people-*.ts`, `places-*.ts`).
- Relecture contradictoire des trois blocs : dates, loci, références modernes et identifiants Pleiades contrôlés ; convention fixée : un fait sûr dont la date est discutée reste « attesté » avec une note de certitude ; « débattu » est réservé aux faits eux-mêmes discutés. Doutes restants dans `docs/A_VERIFIER.md`.
- Apprendre (`#/apprendre`) : quiz de dix questions (dates, puissances, lieux), « Remets dans l'ordre », « Situe la date », « Où ? » avec clic sur la carte et repères de réponse ; filtre par époque.
- Recherche (`#/recherche`) : événements, personnes et lieux, sans accents ni casse.
- Progression sur l'appareil seulement (`localStorage`, protégé contre un stockage absent) : fiches ouvertes et meilleurs scores.

**Problèmes connus**
- Liens Perseus parfois indisponibles (serveur saturé) : à recontrôler.
- Théâtre d'Épidaure : vers 330 ou vers 300, à trancher.
- Fin des Séleucides : 64 ou 63, à harmoniser entre la fiche et `A_VERIFIER.md`.
- Les territoires restent limités aux tracés de Cliopatria et aux 34 tracés à la main.

**Suite** : phase 4 (scènes de la section 10 du brief : Salamine, Cnossos, Mycènes, Olympie, Delphes, Gaugamèles, Alexandrie, Rhodes, Pergame, Syracuse), après validation.


## Phase 4, première partie : les cinq merveilles grecques et la collection (22 et 23 octobre 2026, faite sans validation, en autonomie)

**Fait**
- Propositions des cinq scènes des merveilles (`docs/scenes/phare.md`, `colosse.md`, `olympie.md`, `artemision.md`, `mausolee.md`), chacune passée en relecture contradictoire ; doutes dans `docs/A_VERIFIER.md`.
- Scènes 3D en ligne, reliées à leur événement de la frise :
  - Phare d'Alexandrie vers 280 av. J.-C., au crépuscule, feu allumé et lune levante (2,2 Mo) ; champ facultatif `skySun` et ciel de crépuscule `TwilightSky`.
  - Colosse de Rhodes vers 250 av. J.-C., sur l'hypothèse de la colline (7,6 Mo).
  - Olympie aux Jeux de 420 av. J.-C., avec le Zeus de Phidias (5 Mo) ; champ facultatif `interior.sunScale`.
  - Artémision d'Éphèse vers 200 av. J.-C. (6,2 Mo).
  - Mausolée d'Halicarnasse vers 345 av. J.-C. (7,3 Mo).
- Fichiers lourds publiés dans les versions `assets-v3` et `assets-v4`.
- Collection de cartes (`#/collection`) reprise de Roma : paquet du jour, garanties, doublons changés en drachmes, fabrication, récompenses d'exploration, séries ; 120 cartes et 20 divinités (`docs/COLLECTION.md`), 137 illustrées (œuvres libres et rendus du projet), crédits dans `CREDITS.md` et sur la page Sources.
- Titres des panneaux : « J.-C. » n'est plus coupé en fin de ligne.

**Problèmes connus**
- Shader d'eau commun : rayures près de la caméra (Rhodes, Halicarnasse).
- Halo clair du ciel et vignette sur les vues horizontales ; brume blanche sur plusieurs vues du Mausolée ; vues de Salmakis et de la porte de Myndos faibles.
- Statue du Colosse encore un peu « mannequin » de près ; figurants d'Olympie très schématiques ; Héraion trop jaune.
- Trois cartes sans illustration : Lefkandi, peltastes, cataphractes (pas d'œuvre libre utilisable ni de figurine dans le kit).
- Chargement des scènes en échec chez l'utilisateur sur son appareil : détail technique attendu.

**Suite** : scènes restantes de la section 10 du brief (Salamine, Cnossos, Mycènes, Delphes, Gaugamèles, Pergame, Syracuse), reprise des défauts ci-dessus.
