# Hellas, de Mycènes à Cléopâtre

Un site pour étudier l'histoire du monde grec, des palais mycéniens (vers 1600 av. J.-C.) à la mort de Cléopâtre VII (30 av. J.-C.). Les Grecs appelaient leur monde Hellas : des centaines de cités indépendantes, des ligues, puis l'empire d'Alexandre et les royaumes hellénistiques. La frise chronologique en est la colonne vertébrale, avec une piste par puissance ; la carte en relief montre leurs territoires année par année.

Site : https://maximator13.github.io/hellas/ (en construction)

## Développement

Il faut Node 24 ou plus récent.

```bash
npm install
npm run dev
```

| Commande | Rôle |
|---|---|
| `npm run dev` | serveur de développement |
| `npm run check` | style, lint, typage et tests unitaires |
| `npm run build` | validation des données puis build de production dans `dist/` |
| `npm run test:e2e` | tests de fumée Playwright sur le build |

## Licences

Code sous licence MIT (`LICENSE`). Contenus originaux sous licence CC BY 4.0 (`LICENSE-CONTENT.md`). Ressources de tiers : voir `CREDITS.md`.
