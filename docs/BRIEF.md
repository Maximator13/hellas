# Hellas, de Mycènes à Cléopâtre

Cahier des charges d'un site jumeau de « Roma, de Romulus à Constantin XI » (https://maximator13.github.io/roma/, dépôt `C:\Users\maxim\Projets VSCode\roma`), cette fois sur le monde grec. Titre de travail, modifiable.

Ce fichier contient tout ce qu'il faut pour refaire, sur un autre sujet, ce qui a été construit pour Roma : la vision, les contraintes, la méthode, l'architecture qui a marché, les pièges déjà rencontrés et les préférences de l'utilisateur. Il se lit en premier à chaque session de travail.

## 0. Mode d'emploi

1. Créer un dossier vide, par exemple `C:\Users\maxim\Projets VSCode\hellas`, et un dépôt GitHub public `hellas` (compte Maximator13).
2. Copier ce fichier dans `docs/BRIEF.md` du nouveau dépôt.
3. Créer la mémoire de projet locale, non versionnée, à partir du modèle de la section 14.
4. Première session : « Lis docs/BRIEF.md et lance la phase 0. »

Le nom « empire grec » ne convient pas : les Grecs n'ont pas formé un empire unique. Le monde grec, c'est des centaines de cités indépendantes (poleis), des ligues, puis l'empire d'Alexandre et les royaumes hellénistiques qui lui succèdent. Le site s'appelle donc « Hellas » (le nom que les Grecs donnaient à leur monde) et l'explique dès l'accueil. L'« Empire byzantin », grec de langue, est déjà couvert par Roma et reste hors sujet ici.

## 1. Vision

Un site web statique, publié sur GitHub Pages, pour étudier l'histoire du monde grec, des palais mycéniens (vers 1600 av. J.-C.) à la mort de Cléopâtre VII, dernière souveraine hellénistique (30 av. J.-C.). La frise chronologique est la colonne vertébrale : on la parcourt, et chaque événement important ouvre une scène 3D cinématique : la carte du monde grec qui essaime en colonies puis s'étend jusqu'à l'Indus avec Alexandre, l'intérieur des temples et des palais, des batailles terrestres et navales en mouvement.

Deux publics à la fois : l'utilisateur, pour apprendre la chronologie (dates fiables, sources, jeux de révision), et les visiteurs de son GitHub, qui doivent être saisis dès les premières secondes.

Critères de réussite :
- Tout événement se retrouve en trois interactions au plus, avec sa date, son niveau de certitude et ses sources.
- Les trente premières secondes (intro, carte, frise) donnent envie de continuer.
- 60 images/s visées sur un portable récent sans carte graphique dédiée (machine de mesure : i7-1065G7, Intel Iris Plus, 12 Go) ; ailleurs, la qualité s'adapte automatiquement.

## 2. Contraintes

**GitHub Pages**
- Site 100 % statique, déployé par un workflow GitHub Actions.
- Limites : site publié de 1 Go au plus, fichier de 100 Mo au plus, déploiement de 10 min au plus. Budget interne : site complet de 600 Mo au plus.
- Le site vit sous `/hellas/` : la `base` de Vite, les décodeurs (Meshopt, KTX2) et tous les assets en tiennent compte.
- Routage par hash : chaque événement et chaque scène a une URL partageable qui survit au rechargement (`#/evenement/bataille-de-salamine`, `#/scene/acropole`).
- Les binaires lourds ne vont jamais dans l'historique Git (voir section 5).

**Budget de performance** (mesuré et reporté dans PROGRESS à chaque phase)
- Premier écran utile : 5 Mo téléchargés au plus.
- Chaque scène 3D chargée à la demande : 20 Mo au plus hors vidéo. Chaque vidéo : 20 Mo au plus.
- Géométrie compressée (Meshopt), textures KTX2, instanciation pour tout ce qui se répète (colonnes, hoplites, maisons, rameurs).
- Qualité adaptative (résolution, ombres, post-traitement) et mode léger pour mobile.
- Leçon de Roma : le chargement réel s'est révélé bien plus rapide que prévu. On peut viser des scènes riches (15 à 18 Mo optimisés, environ 2 millions de triangles affichés, 350 appels de dessin), à condition de mesurer.

**Licences**
- Uniquement des ressources gratuites, aucune API payante.
- Par ordre de préférence : ce qu'on crée dans Blender, puis CC0 et domaine public, puis CC BY, polices OFL. CC BY-SA et ODbL acceptées en documentant l'obligation de partage à l'identique. Toute ressource NC ou ND : demander d'abord.
- Chaque ressource externe entre dans `CREDITS.md` (source, auteur, licence, modifications) et sur la page « Sources et crédits » du site au moment où elle est ajoutée.

**Langue et style**
- Interface et contenus en français ; code, types et commits en anglais. Identifiants de contenu en slugs français, réutilisés dans les URL. Tous les textes vivent dans les fichiers de données.
- Aucun tiret cadratin ni demi-cadratin, nulle part (site, documentation, commits) : virgules, deux-points, parenthèses, et « de 490 à 479 av. J.-C. » pour les intervalles. Un script de contrôle le vérifie.
- Le code ne contient aucun commentaire : des noms explicites et des fonctions courtes portent le sens. Le même script le vérifie.
- Rien de ce qui est publié ne mentionne l'outil de production : ni le code, ni la documentation publiée, ni le site, ni l'historique Git (aucune ligne de co-auteur, de session ou de signature dans les commits ni les pull requests).

**Prérequis web non négociables** (préférences globales de l'utilisateur)
- HTTPS forcé ; aucune clé dans le front ; anti-spam sur tout formulaire ; sauvegardes.
- Bandeau cookies avec consentement avant tout script de mesure ; pages Mentions légales, Confidentialité, Conditions d'utilisation.
- Mobile first ; images en WebP, chargement différé, minification ; contrastes vérifiés ; page 404 personnalisée.
- Meta title et description uniques par page ; `alt` sur toutes les images ; `robots.txt`, `sitemap.xml` ; Search Console préparée.
- Open Graph et Twitter Cards ; mesure d'audience respectueuse du consentement ; un seul appel à l'action principal par page ; favicon.

## 3. Stack

Reprendre celle de Roma, éprouvée : Vite, TypeScript strict, React 19, three.js, React Three Fiber, drei, @react-three/postprocessing (avec N8AO pour l'occlusion), GSAP pour les mouvements de caméra, Zustand pour l'état, zod pour valider les données au build, marked pour le markdown des fiches, Vitest, Playwright, ESLint. Node 24 ou plus. Polices auto-hébergées via Fontsource.

## 4. Point de départ : le code de Roma

Ne pas repartir de zéro. Le dépôt Roma contient un moteur complet et testé, à copier puis à adapter :

| Partie de Roma | À reprendre | À changer |
|---|---|---|
| `src/core/` (dates astronomiques, routes, mouvement réduit, son d'ambiance) | tel quel | rien, sauf les bornes |
| `src/timeline/` (frise à zoom sémantique, pistes parallèles, certitude) | tel quel | les pistes : cités et royaumes grecs |
| `src/map/` (carte en relief, territoires animés par année, villes, itinéraires) | le moteur | `MAP_BOUNDS` (de la Sicile à l'Indus pour Alexandre, voir section 8), les données |
| `src/stage/` (Canvas unique, étalonnage par époque, qualité adaptative, HUD `?debug`, bascule carte et scène) | tel quel | les étalonnages des époques grecques |
| `src/scenes/kit/` (chargement glTF, atmosphère, rail de caméra, vie, eau, fumée, feux, éruption) | tel quel | rien |
| `src/scenes/battle/` (maquette tactique de Cannes) | le moteur | unités grecques et perses, batailles navales à ajouter |
| `scripts/` (validation des données, contrôle de style, optimisation et publication des assets, post-build, relief, territoires) | tel quel | les sources géographiques |
| `blender/kit/` (ordres, géométrie, matériaux, terrain, personnages, vie) | comme base | ajouter l'ordre dorique grec, les temples périptères, les trières |
| `tests/` (fumée, captures, image de partage) | tel quel | les routes testées |
| `.github/workflows/deploy.yml` | tel quel | le nom du dépôt |

Lire d'abord dans Roma : `docs/ARCHITECTURE.md` (surtout le contrat des scènes), `docs/DESIGN.md`, `docs/PROGRESS.md` (décisions et problèmes connus), la mémoire de projet (pièges). Copier le code, pas l'historique Git.

## 5. Architecture qui a marché (à conserver)

- **Un seul Canvas WebGL 2**, monté une fois, derrière l'interface : la carte et les scènes s'y succèdent, la caméra circule sans rechargement.
- **La frise est en DOM**, accessible au clavier et aux lecteurs d'écran.
- **Routage par hash**, plus une page statique par événement et par scène prête (générée au post-build) pour les moteurs de recherche et les réseaux sociaux, avec Open Graph propre.
- **Données** : un fichier par type dans `src/data/` (époques, pistes, événements, lieux, personnes, villes, scènes, itinéraires, pages), validé par zod au build ; `npm run validate` refuse une scène « prête » sans son module ni son script Blender.
- **Assets lourds** : jamais dans Git. `npm run assets` optimise (gltf-transform, Meshopt, KTX2, `prune` avec `keepLeaves: true`) ; `npm run assets:publish -- --only=scenes/<id>/<id>.glb` publie dans une GitHub Release `assets-vN` et met à jour un manifeste versionné (chemin, taille, SHA-256, release) ; `npm run assets:pull` les récupère en CI, avec cache.
- **Contrat des scènes** (dans le `.glb` exporté par Blender) :
  - `poi_<id>` (caméra) et `poi_<id>_target` (sujet) pour chaque point d'intérêt, plus `poi_vue-d-ensemble` ;
  - `walk_<trajet>_<nn>` posés exactement sur le sol, espacés de 3 m au plus ; maillages `walker_<variante>` (pieds à l'origine, hors scène) ;
  - `smoke_<n>`, `birds_<n>`, `ash_<n>`, `eruption_vent`, `beacon` (feu), `oculus` et `sunbeam_target` (rayon de lumière) ;
  - matériaux nommés `water`, `sea` ou `river` : remplacés par une eau animée qui reflète le ciel ;
  - matériaux `terrain*` et `ground*` : grain de détail au sol ;
  - extra `cast_shadow: false` sur les petits objets.
- **Une scène simple tient en une configuration** (`ModelScene`) : modèle, soleil, brume, ciel, vue d'ensemble, exposition propre, intérieur éventuel. Le cartel de chaque point (titre, texte, sources) vit dans `src/data/scenes.ts`.
- **Son d'ambiance** libre (CC0), coupé par défaut, choisi par point d'intérêt (agora, port, chantier, foule, vent, fontaine…).
- **Rendu** : tonemapping neutre (Khronos PBR Neutral, pas ACES qui délave), étalonnage par époque, léger halo sur les sources lumineuses, ombres selon la qualité, occlusion N8AO.

## 6. Production 3D avec Blender

- Blender 5.2.2 LTS : `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (hors PATH). KTX-Software 4.4.2 : `C:\Program Files\KTX-Software\bin\ktx.exe`. ffmpeg et gh dans le PATH.
- Chaque scène a son script `blender/<id>.py` qui la reconstruit entièrement et exporte le glTF ; le script est la source de vérité. Le code commun vit dans `blender/kit/`, le code propre à une scène dans `blender/kit/<id>_*.py`.
- Terrain réel quand une source libre existe : Copernicus DEM GLO-30 (attribution) pour la Grèce, l'Asie Mineure, l'Égypte ; retoucher pour restituer les côtes antiques (Thermopyles, Milet, Éphèse, Alexandrie ont beaucoup changé).
- Kit d'architecture : ordres dorique, ionique et corinthien grecs (pas romains : pas de base au dorique grec, entasis, triglyphes et métopes), temples périptères, stoas, théâtres creusés dans la pente, murs cyclopéens mycéniens, trières (170 rameurs sur trois rangs), tholos.
- Personnages low poly faits par script, instanciés, posés au sol (vérifier qu'aucun pied ne s'enfonce), vêtus selon la date : chiton, himation, péplos, chlamyde ; hoplites avec bouclier rond (aspis), casque corinthien puis chalcidien ou thrace selon l'époque, lance (dory) ; phalange macédonienne avec sarisse de 5 à 7 m.
- Statues et temples peints : la polychromie antique est attestée, la montrer (avec retenue et en citant les études).
- Plans pré-rendus : EEVEE, 1920×1080, 24 i/s, 8 à 15 s, MP4 H.264 et image d'affiche. Tout rendu de plus de 10 minutes : estimation et accord avant de lancer.
- Ressources : Poly Haven et ambientCG (CC0). Sketchfab seulement modèle par modèle, licence vérifiée.

## 7. Direction artistique : réalisme stylisé, éclairé comme un film, et vif

- Formes simplifiées, proportions et matériaux fidèles : marbre du Pentélique et de Paros, calcaire, bronze, terre cuite, peintures vives, or et ivoire (Athéna Parthénos). Lumière égéenne franche, mer d'un bleu profond, ciel pur, ombres bleutées, brume légère. Références d'ambiance : Alma-Tadema, Leighton (domaine public), les restitutions de Jean-Claude Golvin pour l'esprit (ne pas copier).
- Leçon de Roma : l'utilisateur a trouvé les couleurs « un peu fades ». Viser d'emblée des couleurs saturées et lumineuses, un tonemapping neutre, et vérifier sur captures que rien n'est gris ni délavé.
- Étalonnage par époque, qui glisse de l'un à l'autre en parcourant la frise (accent de l'interface et lumière de la carte et des scènes) :
  - Âge du bronze : ocre, rouge des fresques de Cnossos, lumière chaude de fin de jour.
  - Âges obscurs : couleurs terreuses, lumière basse, feu de foyer.
  - Époque archaïque : couleurs vives des korès, bleu et rouge, matin clair.
  - Époque classique : marbre blanc et bleu égéen, midi éclatant.
  - Époque hellénistique : or, pourpre, lumière dorée de fin d'après-midi.
- Carte : relief stylisé dont la teinte suit l'époque (l'utilisateur a préféré ce rendu à un fond de carte réaliste type Natural Earth II), couleurs franches, mer animée avec reflets.
- Interface sobre autour de la 3D : fiches en cartels de musée, titres en capitales lapidaires grecques (une police OFL d'inspiration épigraphique grecque, à choisir), texte en sérif de lecture. Une seule famille de courbes d'accélération ; avec `prefers-reduced-motion`, les mouvements deviennent des fondus.

## 8. Contenu historique

### Époques (bornes conventionnelles, que le site explique)

| Époque | Dates | Remarques |
|---|---|---|
| Âge du bronze égéen | de 3200 à 1100 av. J.-C. | Minoens puis Mycéniens ; fin des palais vers 1200 |
| Âges obscurs | de 1100 à 800 av. J.-C. | appelés aussi « époque géométrique » à la fin |
| Époque archaïque | de 800 à 480 av. J.-C. | cités, colonies, premiers Jeux (776, date traditionnelle) |
| Époque classique | de 480 à 323 av. J.-C. | de Salamine à la mort d'Alexandre (certains commencent en 510 ou 490) |
| Époque hellénistique | de 323 à 30 av. J.-C. | royaumes des Diadoques, jusqu'à Actium et Cléopâtre |

Décider en phase 0 si le site commence vers 1600 (Mycéniens) ou vers 3200 (Minoens) et s'il s'arrête en 146 (sac de Corinthe) ou en 30 (Égypte lagide). Recommandation : de 1600 à 30, avec un prologue minoen.

### Pistes parallèles (la grande différence avec Roma)

Il n'y a pas un État unique : la frise a des pistes par puissance, actives selon leurs dates. Par exemple Athènes, Sparte, Corinthe, Thèbes, la Macédoine, Syracuse et la Grande-Grèce, les Perses achéménides (adversaire), puis l'empire d'Alexandre, l'Égypte lagide, l'empire séleucide, la Macédoine antigonide, Pergame, Rhodes. La carte montre plusieurs territoires à la fois, colorés par puissance, plus les colonies grecques en points.

### Modèle de données (repris de Roma)

```ts
type Year = number;
type Certainty = "attested" | "traditional" | "legendary" | "debated";

interface HistoricalEvent {
  id: string;
  title: string;
  start: Year;
  end?: Year;
  precision: "day" | "month" | "year" | "decade" | "century";
  certainty: Certainty;
  era: EraId;
  track: TrackId;
  category: "politics" | "war" | "building" | "religion" | "society" | "culture";
  importance: 1 | 2 | 3;
  placeId?: string;
  summary: string;
  body: string;
  sources: Source[];
  people?: string[];
  scene?: string;
}
```

- `Year` est une année astronomique : 1 av. J.-C. = 0, donc 480 av. J.-C. = -479 et 776 av. J.-C. = -775. Toutes les dates passent par un module de conversion unique, couvert par des tests.
- `placeId` renvoie aux lieux (coordonnées et identifiant Pleiades), `people` aux personnes, `scene` à une scène 3D. `sources` contient au moins un auteur antique ou un ouvrage de référence.

### Exactitude, priorité absolue (pièges propres au monde grec)

- Mythe, tradition et faits attestés sont distingués : la guerre de Troie (légendaire ou débattue), Thésée, Lycurgue, la date de 776 pour les premiers Jeux (traditionnelle).
- Les Grecs dataient par archontes, par olympiades ou par listes de prêtresses : les conversions modernes ont souvent une incertitude d'un an (l'année athénienne commençait en été). Le dire.
- Chiffres antiques gonflés : armée de Xerxès (Hérodote parle de millions ; estimations modernes de 100 000 à 300 000), les « 300 » des Thermopyles (en réalité plusieurs milliers de Grecs). Toujours une fourchette et la source.
- Anachronismes à éviter : pas de casques à crête transversale hollywoodiens pour les Spartiates, pas de cuirasses musculaires partout, pas de phalange macédonienne avant Philippe II, pas d'éléphants avant les campagnes d'Alexandre en Inde (puis chez les Diadoques), pas de monnaie avant le VIIe siècle (Lydie), pas de théâtre de pierre complet avant le IVe siècle (le théâtre de Dionysos est d'abord en bois).
- Le Parthénon : commencé en 447, consacré en 438, décor achevé en 432 ; l'Athéna Parthénos de Phidias ; l'Érechthéion est plus tardif (de 421 à 406 environ). Vérifier l'état de chaque monument à la date de la scène.
- Le Phare d'Alexandrie, le Colosse de Rhodes, le Mausolée : merveilles hellénistiques, déjà en partie couvertes par Roma (scène d'Alexandrie) ; ici, les montrer à leur date de construction.
- Ce dont on n'est pas sûr va dans `docs/A_VERIFIER.md`, avec la meilleure hypothèse et les sources : l'utilisateur tranche.

### Sources de données (licence à vérifier avant usage)

- Pleiades (CC BY) : lieux antiques et coordonnées.
- Cliopatria (Seshat, CC BY 4.0) : territoires par année, utilisé par Roma ; vérifier la couverture des cités grecques, des Achéménides et des royaumes hellénistiques. Là où les données manquent, tracer des polygones approximatifs, citer les sources et montrer l'imprécision (bords flous).
- AWMC (ODbL, versions anciennes en NC : vérifier) : côtes antiques, régions.
- ETOPO 2022 (NOAA, domaine public) pour le relief de la carte ; Natural Earth (domaine public) pour les côtes ; Copernicus DEM GLO-30 pour le relief des scènes.
- ToposText (textes antiques géolocalisés) : licence à vérifier avant tout usage de données.
- Textes antiques en traduction libre de droits (Hérodote, Thucydide, Xénophon, Plutarque, Arrien, Pausanias) ; citer livre et paragraphe.

## 9. L'expérience

- **Intro**, passable : le globe, la plongée vers la mer Égée, l'Acropole, le titre.
- **Frise** : toujours présente, navigable à la molette, au glisser, au clavier et au toucher ; zoom sémantique, des siècles à la décennie ; pistes parallèles ; indicateur de certitude par la forme, jamais la couleur seule ; recherche.
- **Carte** : relief stylisé de la Sicile à l'Indus, synchronisé avec l'année de la frise : territoires des puissances, colonies, villes, sanctuaires, itinéraires animés (retraite des Dix Mille, campagnes d'Alexandre).
- **Monuments et villes** : caméra guidée sur un rail entre des points d'intérêt, regard libre limité, cartels sur les détails, son d'ambiance, passants, fumées, oiseaux, eau animée.
- **Batailles**, temps réel et vidéo mêlés : maquette tactique 3D (terrain réel, unités en formation, 1 figurine = N soldats avec l'échelle affichée, phases scriptées, lecture, pause, défilement, flèches de manœuvre, vue tactique et vue rasante), plus un ou deux plans pré-rendus aux moments décisifs. Ajouter les batailles navales (trières, éperonnage, diekplous et periplous).
- **Apprendre en jouant** : un quiz par époque, « Remets dans l'ordre », « Situe la date », « Où ? » sur la carte, fiches débloquées en explorant, progression en `localStorage`.

## 10. Scènes envisagées (ordre de départ, modifiable)

Pour chaque scène : proposition vérifiée, production, captures, puis validation par l'utilisateur.

1. **Athènes et l'Acropole vers 432 av. J.-C.** : Parthénon peint et achevé, Propylées en chantier, Athéna Promachos, agora, Pnyx, théâtre de Dionysos. Tranche verticale « monument ».
2. **Bataille des Thermopyles (480 av. J.-C.)** ou **de Marathon (490)** : maquette tactique terrestre. Tranche verticale « bataille ».
3. **Bataille de Salamine (480 av. J.-C.)** : bataille navale, trières dans le détroit.
4. **Cnossos vers 1450 av. J.-C.** : palais minoen, fresques, couleurs vives.
5. **Mycènes vers 1250 av. J.-C.** : porte des Lionnes, murs cyclopéens, cercle de tombes.
6. **Olympie pendant les Jeux** : temple de Zeus et sa statue chryséléphantine, stade, foule.
7. **Delphes** : sanctuaire d'Apollon en terrasses, trésors, théâtre, la Pythie.
8. **Bataille de Gaugamèles (331 av. J.-C.)** : Alexandre contre Darius III, chars à faux, phalange.
9. **Alexandrie et le Phare** à son achèvement (vers 280 av. J.-C.), Bibliothèque et Musée.
10. **Rhodes et son Colosse**, **Pergame** et son autel, **Syracuse assiégée** (Archimède, 213 à 212).

L'utilisateur aime les scènes spectaculaires (éruption du Vésuve, phare allumé) : prévoir des moments forts (incendie de l'Acropole par les Perses en 480, Salamine au lever du jour, flamme des Jeux, phare la nuit).

## 11. Méthode de travail

- Une phase à la fois. En fin de phase : mettre à jour `docs/PROGRESS.md` (fait, décisions, problèmes connus, suite), commit, push, vérifier le site déployé, puis attendre la validation. Si l'utilisateur dit de travailler en autonomie (« fais tout sans me demander », « toute la nuit »), enchaîner sans attendre, tout noter dans PROGRESS comme « fait sans validation », et ne s'arrêter que pour ce qui est irréversible ou interdit.
- Commits petits et fréquents, en anglais, sans aucune ligne d'attribution.
- Chaque changement visuel se vérifie sur des captures Playwright regardées avant de le dire terminé. Pour juger le rendu, lancer Chromium sur le vrai GPU (`--use-angle=d3d11 --enable-gpu --ignore-gpu-blocklist`) : en headless logiciel (SwiftShader), le WebGL tourne à 2 i/s. Comparer avant et après côte à côte (ffmpeg `hstack`).
- Les i/s se mesurent chez l'utilisateur avec le HUD `?debug` ; les demander en fin de phase visuelle.
- Compromis de performance, de poids, de licence ou d'exactitude : deux ou trois options chiffrées, une recommandation, l'utilisateur choisit.
- Chaque scène est un module autonome (`src/scenes/<id>/` et `blender/<id>.py`) chargé à la demande.
- Donner souvent des nouvelles courtes : l'utilisateur suit depuis son téléphone et demande « t'en es où ».

### Chaîne de production d'une scène (a fait ses preuves sur Roma)

Lancée en arrière-plan par sous-agents ou workflow, deux scènes en parallèle au plus (Blender tourne sur le même portable) :
1. **Recherche** : proposition complète (date justifiée, monuments avec dimensions, état à la date, coordonnées et Pleiades, vie et lumière, points d'intérêt et cartels, plan de caméra, événements liés, assets libres, budget, anachronismes, doutes).
2. **Vérification contradictoire** : un second agent cherche à réfuter chaque date, chiffre, citation et licence, corrige et déplace l'incertain dans les doutes.
3. **Construction Blender** par script, avec rendus de prévisualisation regardés et itérés, puis `npm run assets` et rapport de poids.
4. **Relecture** par un historien et un chef opérateur (sur les rendus).
5. **Correction** des remarques.
6. **Intégration** par la session principale : `src/scenes/<id>/index.tsx`, entrée dans `src/data/scenes.ts` (points et cartels), ville et événements liés, sons, crédits, `docs/scenes/<id>.md`, `A_VERIFIER`, captures, publication de l'asset, commit, push, vérification en ligne.

## 12. Phases

### Phase 0 : cadrage (aucun code)
Lire ce brief et le code de Roma ; fixer les bornes, les époques, les pistes et l'emprise de la carte ; vérifier les sources de données et leurs licences ; proposer le plan de la phase 1. Attendre la validation.

### Phase 1 : fondations et déploiement
Copier et adapter le moteur de Roma ; dépôt, CI, déploiement Pages, pages légales, bandeau cookies, SEO, 404, frise avec une vingtaine d'événements, carte avec relief, premiers territoires. Site en ligne.

### Phase 2 : tranche verticale
Plan de design (palette nommée, typographies, principes) à valider ; carte animée à au moins cinq dates (dont 480 et 323) avec l'itinéraire d'Alexandre ; une scène monument (l'Acropole) ; une bataille (Thermopyles ou Marathon) ; transitions continues frise, carte, scène. Terminé quand le parcours fonctionne en ligne, que chaque scène tient son budget et que l'utilisateur a validé le rendu sur sa machine.

### Phase 3 : tout le contenu et l'apprentissage
Environ 200 événements, les grandes figures (tyrans, stratèges, rois, philosophes, poètes), les lieux reliés à Pleiades, les territoires de toutes les époques ; recherche, quiz, mini-jeux, fiches, progression.

### Phase 4 : les scènes, une par une
Selon la section 10.

### Phase 5 : finitions
Intro définitive, son, accessibilité (clavier, contrastes, sous-titres, mouvement réduit), mobile, README avec captures et GIF, `CREDITS.md` complet, audit Lighthouse noté dans PROGRESS.

## 13. Pièges déjà rencontrés sur Roma (à éviter d'emblée)

- Les outils d'écriture de fichiers et les heredocs convertissent les séquences d'échappement des tirets U+2013 et U+2014 en vrais tirets : les construire avec `String.fromCharCode(0x2013, 0x2014)` dans le script de contrôle.
- `prune()` de gltf-transform supprime les nœuds vides : sans `keepLeaves: true`, les repères `poi_<id>` disparaissent.
- Passants les pieds dans le sol : la géométrie optimisée perd la transformation du nœud ; recaler chaque modèle pour que le bas de sa boîte englobante soit à l'origine, et poser les trajets exactement sur le sol.
- En développement, React monte puis démonte chaque effet : ne jamais libérer un modèle 3D dans un nettoyage immédiat (libération différée), sinon `compileAsync` attend des programmes détruits.
- Les étiquettes 3D (troika) lancent un worker dont la requête `blob:` ne finit jamais sur mobile émulé : ne jamais attendre `networkidle` dans Playwright.
- `vite preview` renvoie l'application pour toute adresse : le vrai 404 ne se vérifie qu'en ligne.
- Un sous-agent peut se voir refuser l'exécution de Blender : la session principale peut le lancer. Vérifier les rapports des agents avant de supposer qu'un modèle existe.
- Les tests Playwright expirent quand Blender tourne en parallèle sur la même machine : relancer, ou se fier à la CI.
- Un `.glb` produit par une autre session n'est pas en local : `npm run assets:pull` avant de tester.
- Eau : des vagues régulières créent du moirage au loin ; les filtrer selon la taille du pixel (`fwidth`).
- Ciel très lumineux (éruption, brume dense) : prévoir une exposition propre à la scène.
- Push : d'abord `git pull --rebase`, d'autres sessions poussent aussi. Si `gh` n'est pas dans le PATH de la session : `git -c credential.helper= -c "credential.helper=!'/c/Program Files/GitHub CLI/gh.exe' auth git-credential" push`.
- Suivi du déploiement : `"/c/Program Files/GitHub CLI/gh.exe" run watch <id> --exit-status`.

## 14. Modèle de mémoire de projet (fichier local, non versionné)

```markdown
# Hellas : mémoire de projet

Au début de chaque session, lire `docs/BRIEF.md` (cahier des charges) puis `docs/PROGRESS.md` (avancement et décisions). Ne pas les importer ici.

## Règles fixes

- Une phase à la fois. En fin de phase : mettre à jour PROGRESS, commit, push, vérifier le site déployé, puis attendre la validation (sauf autonomie accordée).
- Interface et contenus en français ; code, types et commits en anglais ; slugs français dans les URL.
- Aucun commentaire dans le code. Aucun tiret cadratin ni demi-cadratin nulle part (site, docs, commits) : virgules, deux-points, parenthèses.
- Rien de publié ne mentionne l'outil de production : pas de ligne de co-auteur, de session ni de signature. Garde-fous locaux non versionnés : réglages locaux (attribution vide), `.git/hooks/commit-msg`, `.git/info/exclude`.
- Années astronomiques (1 av. J.-C. = 0), toujours via le module de dates unique.
- Toute ressource externe entre dans `CREDITS.md` au moment de l'ajout ; licence NC ou ND : demander d'abord.
- Compromis de performance, poids, licence ou exactitude : deux ou trois options chiffrées, une recommandation, l'utilisateur choisit.
- Fait incertain : `docs/A_VERIFIER.md`, avec hypothèse et sources.
- Rendu Blender de plus de 10 minutes : estimation et accord avant de lancer.
- Changement visuel : captures Playwright regardées avant de le déclarer terminé.

## Outils locaux

- Blender 5.2.2 LTS : `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (hors PATH).
- KTX-Software 4.4.2 : `C:\Program Files\KTX-Software\bin\ktx.exe` (hors PATH, à ajouter au PATH du script d'assets).
- ffmpeg et gh (compte Maximator13) dans le PATH.
- Machine de mesure : i7-1065G7, Intel Iris Plus, 12 Go.
- Projet de référence : `C:\Users\maxim\Projets VSCode\roma` (même moteur, sujet romain).

## Commandes

- `npm run dev` : développement (http://localhost:5173/hellas/).
- `npm run check` : style (commentaires, tirets), ESLint, typage, Vitest.
- `npm run build` : validation des données, build, pages de partage, budget du site.
- `npm run test:e2e` : Playwright sur le build (desktop et mobile).
- `npm run assets`, `npm run assets:publish -- --only=<chemin>`, `npm run assets:pull` : fichiers lourds.

## Pièges connus

Reprendre la section 13 du brief et la compléter au fil des sessions.
```

## 15. Préférences de l'utilisateur (constatées sur Roma)

- Écrit en français, souvent vite et sans accents : comprendre l'intention, ne pas faire répéter.
- Veut de l'efficacité et de l'autonomie : quand il dit « fais tout », « bosse toute la nuit », « fais ce que tu veux », avancer au maximum sans poser de questions, en parallèle quand c'est possible, et tout consigner dans PROGRESS.
- Aime le spectaculaire et le vivant : détails, foules, fumées, eau, sons, lumière de cinéma, couleurs franches. Trouve vite un rendu « fade ».
- Tient à ses choix de style : il a préféré garder la carte stylisée dont la couleur suit l'époque, simplement plus vive. Proposer un changement de direction artistique avant de le faire.
- Suit l'avancement depuis son téléphone : messages d'état courts et fréquents, captures envoyées quand une scène est en ligne.
- Mesure lui-même la fluidité sur son portable ; lui dire où cliquer (`?debug`) et quoi relever.
