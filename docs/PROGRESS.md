# Avancement

## Phase 0 : cadrage (21 octobre 2026)

**Fait**
- Dépôt local créé, brief versionné dans `docs/BRIEF.md` (copie nettoyée de toute mention de l'outil de production), garde-fous locaux en place (hook de message de commit, exclusions, attribution vide).
- Lecture du moteur de Roma et inventaire de portage : moteur générique sauf l'identité du site, les bornes, les époques, les pistes, l'emprise de la carte et le rendu des territoires.
- Vérification des sources de données et de leurs licences, couverture réelle de Cliopatria pour le monde grec mesurée sur le fichier.
- Cadrage historique : bornes, époques, dix-huit pistes, emprise de la carte, vingt premiers événements sourcés, instantanés de carte pour la phase 2.
- Tout est dans `docs/CADRAGE.md` ; les points douteux dans `docs/A_VERIFIER.md`.

**Décisions en attente** : section 8 de `docs/CADRAGE.md`.

**Problèmes connus**
- Le rendu des territoires de Roma n'a que deux teintes : un rendu multicolore est nécessaire (phase 1, étape 7).
- Cliopatria ne connaît ni Athènes, ni Sparte, ni Corinthe, ni Syracuse, ni la ligue de Délos, et contient des erreurs d'étiquette (conquêtes d'Alexandre nommées « Ptolemaic Kingdom » de 331 à 324) : corrections à l'import et tracés à la main.
- `robots.txt` n'est lu qu'à la racine du domaine `maximator13.github.io`, qui n'existe pas.

**Suite** : phase 1, fondations et déploiement, selon la section 7 de `docs/CADRAGE.md`, après validation.
