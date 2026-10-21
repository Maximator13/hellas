# Plan de design

Statut : direction en place sur le site, établie sans validation à la demande de l'utilisateur (phase 2 en autonomie, 21 octobre 2026). Les valeurs ci-dessous sont celles du code (`src/styles.css`, `src/stage/grading.ts`, `src/data/tracks.ts`, `src/map/terrainMaterial.ts`) ; une modification se fait là, puis ici.

## Palette nommée

| Nom | Valeur | Rôle |
|---|---|---|
| Nuit égéenne | `#0C1219` | fond de page et des panneaux (à 93 % d'opacité sur la 3D) |
| Marbre de Paros | `#F2EEE4` | texte principal |
| Pierre du Pentélique | `#C8C2B4` | texte secondaire, légendes, aides |
| Or de Phidias | `#D8B25A` | accent par défaut : filets, bouton principal, année courante |
| Bleu égéen | `#3D8BD9` | Athènes, accent de l'époque classique |
| Rouge de Cnossos | `#D9603B` | Crète minoenne, accent de l'âge du bronze |

Contraste sur Nuit égéenne : Marbre de Paros 16,2:1, Pierre du Pentélique 10,6:1, Or de Phidias 9,3:1. L'accent change avec l'époque ; pour le texte, il passe par `readableAccent`, qui l'éclaircit jusqu'à 4,5:1 au moins sur le fond (testé sur toute la frise).

### Accent et lumière par époque

La carte et les scènes passent d'une époque à l'autre en vingt ans de frise.

| Époque | Accent | Lumière |
|---|---|---|
| Âge du bronze égéen | ocre rouge des fresques de Cnossos | fin de jour chaude, soleil bas, ciel orangé |
| Âges obscurs | terre brûlée | lumière basse, tons terreux, feu de foyer |
| Époque archaïque | rouge des korès | matin clair, couleurs vives, ciel bleu franc |
| Époque classique | bleu égéen | midi éclatant, marbre blanc, mer d'un bleu profond |
| Époque hellénistique | or | fin d'après-midi dorée, ombres longues |

### Couleurs des puissances

Une couleur par piste, partagée par la frise (barre, nom, marqueurs) et la carte (territoire, frontière, nom). Les couleurs voisines dans le temps restent distinctes : à 480 (ivoire du monde grec, bleu d'Athènes, rouge de Sparte, olive de la Perse, magenta de la Macédoine, orange de Syracuse) comme à 200 (teal des Lagides, ocre des Séleucides, indigo de Rome, vert de Pergame, rose de Rhodes, kaki des ligues). La certitude d'un événement se lit toujours par la forme de son marqueur, jamais par sa couleur.

## Typographies

- **Didact Gothic** (SIL OFL 1.1), linéale à trait uniforme dont les capitales espacées rappellent l'écriture stoichédon des inscriptions attiques : titres, noms d'époques, boutons, noms des puissances et des villes sur la carte. Toujours en capitales, interlettrage de 0,08 à 0,22 em. Sous-ensembles latin et grec.
- **EB Garamond** (SIL OFL 1.1), Garamond de lecture : textes, cartels, sources ; italique pour les notes. Corps de 17 px (16 px sur mobile), interligne 1,55. Sous-ensembles latin, grec et grec étendu, pour les mots grecs polytoniques des cartels.
- Typographie française appliquée au rendu : espaces insécables fines avant les signes doubles, guillemets « », apostrophes.

## Principes

1. **La 3D est le moment fort.** L'interface se tient en bordure : une frise en bas, un cartel sur le côté, rien au centre de l'image.
2. **Des cartels de musée.** Chaque fiche et chaque point d'intérêt d'une scène est un cartel : titre en capitales, date, certitude, texte court, sources.
3. **L'exactitude se voit.** Certitude (attesté, traditionnel, légendaire, débattu) sur chaque événement ; fourchettes et sources pour les chiffres antiques ; doutes dans `docs/A_VERIFIER.md`.
4. **Plusieurs puissances, une lecture.** La frise attribue ses quatre rangées secondaires aux puissances qui ont des événements à l'écran ; la carte montre toutes les puissances actives à l'année du curseur.
5. **Des couleurs franches.** Tonemapping neutre, saturation au-dessus de 1 dans les étalonnages, mer profonde, aucun gris délavé : chaque changement visuel se vérifie sur capture.
6. **Une seule famille de mouvements.** Une seule courbe (`power3`) ; la caméra circule sans coupure de la frise à la carte puis à la scène. Avec `prefers-reduced-motion`, les mouvements deviennent des fondus.
7. **Un seul appel à l'action principal par écran** : « Commencer vers 1600 av. J.-C. » à l'accueil, « Point suivant » dans une scène, « Visiter en 3D » dans une fiche liée à une scène.
8. **Mobile d'abord.** Sur téléphone, la frise reste en bas, les fiches couvrent l'écran et le cartel d'une scène devient une feuille basse qui laisse voir la 3D.

## Carte

Relief stylisé dont la teinte suit l'époque, mer animée avec reflets ; territoires remplis de la couleur de leur puissance, frontière lumineuse, nom en capitales espacées. Cadrage par période : Égée jusqu'à 800, Méditerranée des colonies de 800 à 550, Égée de 550 à 336, Orient d'Alexandre de 336 à 301, royaumes hellénistiques ensuite.

## Scènes 3D

Réalisme stylisé éclairé comme un film : formes simplifiées, proportions et matériaux fidèles (marbre du Pentélique et de Paros, calcaire, bronze, terre cuite), polychromie attestée montrée avec retenue et sources citées, lumière égéenne franche, ombres bleutées, brume légère.
