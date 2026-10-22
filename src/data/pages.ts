import type { PageId } from '../core/route.ts'

export interface Page {
  id: PageId
  title: string
  description: string
  body: string
}

export const pages: Page[] = [
  {
    id: 'mentions-legales',
    title: 'Mentions légales',
    description: 'Éditeur, hébergeur et propriété intellectuelle du site Hellas.',
    body: `## Éditeur

Ce site est édité à titre personnel et non commercial par **Maximator13** (pseudonyme).

Contact : par les [issues du dépôt GitHub](https://github.com/Maximator13/hellas/issues).

## Hébergeur

GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis ([github.com](https://github.com)), via le service GitHub Pages.

## Propriété intellectuelle

Le code source est publié sous licence MIT. Les contenus originaux (textes, données, modèles 3D et vidéos produits pour le projet) sont publiés sous licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr). Les ressources de tiers gardent leur propre licence : voir la page Sources et crédits.`,
  },
  {
    id: 'confidentialite',
    title: 'Confidentialité',
    description: "Données personnelles, stockage local et mesure d'audience sur le site Hellas.",
    body: `## En bref

Ce site ne dépose aucun cookie et ne vous demande aucune donnée personnelle. Toutes ses ressources (code, polices, images, modèles 3D) sont servies par le site lui-même : votre navigateur ne contacte aucun service tiers.

## Stockage dans votre navigateur

Le site peut enregistrer dans votre navigateur (\`localStorage\`) vos préférences, votre choix sur la mesure d'audience, votre progression dans les jeux de révision et dans la collection de cartes (cartes obtenues, drachmes, scènes visitées et fiches lues, pour les récompenses). Ces données restent sur votre appareil ; vous pouvez les effacer à tout moment depuis les réglages de votre navigateur.

## Mesure d'audience

Aucune mesure d'audience n'est active pour l'instant. Si elle est activée, elle reposera sur GoatCounter, un outil sans cookie qui ne conserve pas votre adresse IP, et ne se chargera qu'après votre accord explicite. Vous pourrez retirer cet accord à tout moment.

## Hébergement

L'hébergeur, GitHub, peut journaliser les adresses IP des visiteurs pour assurer la sécurité de son service. Voir la [déclaration de confidentialité de GitHub](https://docs.github.com/fr/site-policy/privacy-policies/github-general-privacy-statement).`,
  },
  {
    id: 'conditions',
    title: "Conditions d'utilisation",
    description: "Conditions d'utilisation du site Hellas : accès, contenus, licences et responsabilité.",
    body: `## Objet

Hellas est un site éducatif gratuit, consacré à l'histoire du monde grec, des palais de Crète et de Mycènes à la mort de Cléopâtre VII (de 2000 à 30 av. J.-C.). Il est accessible sans inscription.

## Contenus

Les contenus sont rédigés avec soin et appuyés sur des sources citées pour chaque événement. Les dates traditionnelles, légendaires ou débattues sont signalées comme telles. Le site est fourni en l'état, sans garantie d'exactitude ni d'exhaustivité. Pour signaler une erreur, ouvrez une [issue sur le dépôt](https://github.com/Maximator13/hellas/issues).

## Réutilisation

Vous pouvez réutiliser les contenus originaux selon la licence CC BY 4.0, en citant « Hellas, de Mycènes à Cléopâtre, par Maximator13 » et l'adresse du dépôt. Le code est sous licence MIT. Les ressources de tiers suivent leur propre licence.

## Liens externes

Les liens vers d'autres sites (traductions de sources antiques, ouvrages, bases de données) sont fournis pour information ; l'éditeur n'est pas responsable de leur contenu.

## Évolution

Ces conditions peuvent évoluer avec le site. Elles sont régies par le droit français.`,
  },
  {
    id: 'sources',
    title: 'Sources et crédits',
    description: 'Méthode, conventions de dates, sources et crédits du site Hellas.',
    body: `## Méthode

Chaque événement indique sa date, son niveau de certitude et au moins une source : un auteur antique, avec la référence du passage, ou un ouvrage de référence moderne. Pour l'âge du bronze et les âges obscurs, sans textes, les dates viennent de l'archéologie et sont approximatives.

- **Attesté** : fait rapporté par des sources contemporaines ou jugées fiables, ou établi par l'archéologie.
- **Traditionnel** : transmis par la tradition antique, plausible mais sans source contemporaine (premiers Jeux olympiques en 776, dates de fondation des colonies).
- **Légendaire** : récit légendaire, sans fondement historique établi (guerre de Troie, héros fondateurs).
- **Débattu** : date ou fait discuté par les historiens ; la fourchette est indiquée.

Les chiffres antiques, souvent gonflés (l'armée de Xerxès compte plus de cinq millions d'hommes chez Hérodote), sont toujours donnés avec leur source et, quand elle existe, l'estimation des historiens modernes.

## Dates

Toutes les dates de la frise sont antérieures à notre ère : de 2000 à 30 av. J.-C., elle couvre 1 970 ans. Les bornes des époques sont des conventions d'historiens, expliquées pour chacune d'elles.

Les Grecs ne comptaient pas les années comme nous : chaque cité les nommait d'après un magistrat (à Athènes, l'archonte), et les historiens à partir du IIIe siècle av. J.-C. les ont rangées par olympiades. L'année athénienne commençait en été : une date comme « 508/507 » chevauche donc deux de nos années, et beaucoup de conversions restent incertaines d'un an. Les dates au jour près viennent de calculs astronomiques (éclipses) ou de documents babyloniens.

## Le nom

Hellas est le nom que les Grecs donnaient à leur monde, celui des Hellènes. Il ne désigne pas un État : le monde grec a rassemblé des centaines de cités indépendantes, des ligues, puis l'empire d'Alexandre et les royaumes qui en sont issus, sans jamais former un empire unique.

## Crédits

- Polices : EB Garamond (Georg Duffner et Octavio Pardo) et Didact Gothic (The Didact Gothic Project Authors), sous licence SIL Open Font License 1.1.
- Bibliothèques : React, three.js, React Three Fiber, drei, troika-three-text, meshoptimizer, Zustand et marked (licence MIT), postprocessing (licence zlib), N8AO (licence ISC), Basis Universal (licence Apache 2.0), GSAP (licence gratuite propre à Webflow).
- Relief et fonds marins : NOAA NCEI, ETOPO 2022 (CC0 1.0), [doi:10.25921/fd45-gt74](https://doi.org/10.25921/fd45-gt74).
- Traits de côte, lacs et cours d'eau : Made with Natural Earth (domaine public).
- Relief des scènes de l'Acropole, des Thermopyles, de Rhodes, d'Olympie, d'Éphèse et d'Halicarnasse : Copernicus DEM GLO-30, produit à partir de Copernicus WorldDEM-30 © DLR e.V. 2010-2014 et © Airbus Defence and Space GmbH 2014-2018, fourni dans le cadre de COPERNICUS par l'Union européenne et l'ESA, qui n'assument aucune responsabilité pour l'usage qui en est fait.
- Illustrations des cartes de la collection : œuvres du domaine public et photographies sous CC0, CC BY ou CC BY-SA, surtout de Wikimedia Commons, recadrées et réduites ; chaque carte cite son œuvre, son auteur et sa licence, et les photographies sous CC BY-SA restent sous cette licence. Les cartes des scènes 3D et de quelques unités sont des rendus du projet (CC BY 4.0).
- Lieux antiques : [Pleiades](https://pleiades.stoa.org), © les contributeurs, CC BY 3.0.
- Liste et localisation des cités : [Wikidata](https://www.wikidata.org), CC0 1.0.
- Territoires des royaumes et des ligues année par année : J. S. Bennett, E. Mutch, A. Tollefson et al., [Cliopatria v0.2.1](https://github.com/Seshat-Global-History-Databank/cliopatria) (Seshat Global History Databank), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ; données modifiées (extraction des entités grecques et de leurs voisins, simplification, étiquettes corrigées).
- Sons d'ambiance : enregistrements du domaine public et sous CC0 (Wikimedia Commons, Freesound, xeno-canto, OpenGameArt) ; vagues du port : « Smallwaves » par Torsten Nilsson, Work With Sounds, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), modifié. Détail dans le fichier CREDITS.md du dépôt.

La liste complète des ressources, avec leurs auteurs, licences et modifications, est tenue à jour dans le fichier [CREDITS.md](https://github.com/Maximator13/hellas/blob/main/CREDITS.md) du dépôt.`,
  },
]
