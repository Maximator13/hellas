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

**Suite** : phase 2 (tranche verticale), après validation.
