import type { HistoricalEvent } from './schema.ts'

const PAUSANIAS = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0160'
const DIODORE = 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0084'

export const events: HistoricalEvent[] = [
  {
    "id": "ecriture-lineaire-a",
    "title": "Écriture linéaire A",
    "start": -1799,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique : les premiers documents remontent au minoen moyen II, vers 1800, et la plupart datent des destructions de 1450 environ. L'écriture n'est pas déchiffrée.",
    "era": "bronze",
    "track": "minoens",
    "category": "culture",
    "importance": 2,
    "placeId": "haghia-triada",
    "summary": "Vers 1800, les scribes crétois commencent à noter leurs comptes dans une écriture syllabique, le linéaire A, sur des tablettes d'argile, des scellés et des objets de culte. Elle n'est toujours pas déchiffrée : on lit les chiffres et le son approximatif de nombreux signes, mais on ignore la langue qu'ils notent.",
    "body": "**Une écriture de comptables.** Le linéaire A apparaît au minoen moyen II, d'abord à Phaistos, à côté du hiéroglyphique crétois, qu'il finit par supplanter. On en connaît environ 1 400 documents, souvent très courts ; le plus gros lot vient de la villa d'Haghia Triada, près de Phaistos, avec près de 150 tablettes. On y trouve des listes de denrées (grain, vin, huile, figues) suivies de chiffres décimaux, et des formules gravées sur des tables à libation offertes dans les sanctuaires.\n\n**Pourquoi c'est important.** C'est la première écriture administrative du monde égéen. Les Mycéniens l'ont adaptée pour noter le grec : le linéaire B en reprend une grande partie des signes, ce qui permet de prononcer approximativement les mots du linéaire A, comme ku-ro, qui précède les totaux.\n\n**Ce qui reste inconnu.** Les sons ainsi obtenus ne correspondent de façon convaincante à aucune langue connue, ni grecque, ni sémitique, ni anatolienne, malgré de nombreuses tentatives. Le disque de Phaistos, trouvé en 1908 et imprimé avec des tampons, porte une autre écriture, isolée et elle aussi indéchiffrée.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Archives d'Haghia Triada",
        "work": "Tablettes en linéaire A de la série HT",
        "locus": "GORILA, vol. I"
      },
      {
        "kind": "modern",
        "author": "Louis Godart et Jean-Pierre Olivier",
        "work": "Recueil des inscriptions en linéaire A (GORILA), 5 vol., Paris, Geuthner, 1976 à 1985 (Études crétoises, 21)"
      },
      {
        "kind": "modern",
        "author": "Cynthia W. Shelmerdine (dir.)",
        "work": "The Cambridge Companion to the Aegean Bronze Age, Cambridge, Cambridge University Press, 2008"
      }
    ]
  },
  {
    "id": "seconds-palais-minoens",
    "title": "Seconds palais de Crète",
    "start": -1699,
    "end": -1449,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique : les premiers palais sont détruits à la fin du minoen moyen II, vers 1700, et les seconds durent jusqu'aux destructions du minoen récent IB, vers 1450. Ces dates varient de plusieurs décennies selon les chronologies.",
    "era": "bronze",
    "track": "minoens",
    "category": "building",
    "importance": 2,
    "placeId": "cnossos",
    "summary": "Vers 1700, les premiers palais crétois sont détruits, sans doute par des séismes, puis reconstruits plus vastes et plus riches. Pendant deux siècles et demi, Cnossos, Phaistos, Malia et Zakros dominent une Crète prospère, couverte de villas et de sanctuaires, dont l'art et les produits gagnent les Cyclades, le continent et l'Égypte.",
    "body": "**Détruire et rebâtir.** À la fin du minoen moyen II, les palais de Cnossos, Phaistos et Malia sont ruinés presque en même temps ; les fouilleurs y voient surtout l'effet de tremblements de terre. Ils sont reconstruits sur le même plan, autour de la cour centrale, avec des façades en pierre de taille, des escaliers monumentaux, des puits de lumière et des salles peintes à fresque. Un nouveau palais s'élève à Zakros, à l'extrémité orientale de l'île.\n\n**Une Crète rayonnante.** C'est l'apogée de la civilisation minoenne : villas comme Haghia Triada ou Tylissos, sanctuaires de sommet, céramique fine, vases de pierre, sceaux gravés. Des objets et des usages crétois (poids, écriture, fresques) se répandent dans les Cyclades, à Akrotiri notamment, et les peintures des tombes thébaines du XVe siècle montrent des porteurs d'offrandes venus du pays de Keftiou, nom égyptien de la Crète.\n\n**Ce qu'on ignore.** On ne sait ni qui gouvernait (un roi, des prêtres, plusieurs grandes familles) ni si Cnossos dominait toute l'île. L'image d'une Crète pacifique, chère à Arthur Evans, a été nuancée, et une bonne part des fresques que l'on voit aujourd'hui à Cnossos sont des reconstitutions modernes.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Diodore de Sicile",
        "work": "Bibliothèque historique",
        "locus": "V, 78, 2 (Minos fondateur de Cnossos, de Phaistos et de Kydonia)",
        "url": `${DIODORE}:book=5:chapter=78`
      },
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "XIX, 178 et 179 (Cnossos, ville de Minos)"
      },
      {
        "kind": "modern",
        "author": "J. Lesley Fitton",
        "work": "Minoans, Londres, British Museum Press, 2002"
      },
      {
        "kind": "modern",
        "author": "Cynthia W. Shelmerdine (dir.)",
        "work": "The Cambridge Companion to the Aegean Bronze Age, Cambridge, Cambridge University Press, 2008"
      }
    ]
  },
  {
    "id": "fresques-d-akrotiri",
    "title": "Fresques d'Akrotiri",
    "start": -1699,
    "end": -1599,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Les fresques sont antérieures à l'éruption de Théra, datée vers 1600 par le radiocarbone ou vers 1530 à 1500 par la chronologie archéologique : leur date absolue dépend de ce débat.",
    "era": "bronze",
    "track": "minoens",
    "category": "culture",
    "importance": 2,
    "placeId": "akrotiri",
    "summary": "Dans les maisons d'Akrotiri, à Théra, des peintres couvrent les murs de fresques d'une grande fraîcheur : un pêcheur portant ses poissons, deux enfants qui boxent, des cueilleuses de safran, un paysage de lis et d'hirondelles, une flottille entre deux villes. Ensevelies par l'éruption, elles forment le plus bel ensemble de peinture murale de l'âge du bronze égéen.",
    "body": "**Une ville peinte.** Les fouilles commencées en 1967 par Spyridon Marinatos, poursuivies par Christos Doumas, ont dégagé des maisons à deux ou trois étages dont beaucoup de pièces étaient peintes sur enduit frais. La Maison Ouest a livré le pêcheur et une longue frise miniature où des navires d'apparat vont d'une ville à l'autre ; le bâtiment appelé Xeste 3 montre des jeunes filles cueillant le safran pour une déesse assise, accompagnée d'un singe et d'un griffon.\n\n**Pourquoi c'est important.** Les fresques de Cnossos sont pour la plupart des fragments restaurés ; à Akrotiri, la cendre a gardé des murs entiers, à leur place. Elles montrent une société des Cyclades très proche de la Crète minoenne par la technique et les thèmes, avec son propre style, et renseignent sur les navires, les vêtements, les rites et les paysages de l'Égée.\n\n**Ce qui est discuté.** Le sens des scènes (fête, rite d'initiation, récit d'expédition) reste affaire d'interprétation, et leur date absolue suit celle de l'éruption, entre le XVIIe et le XVIe siècle.",
    "sources": [
      {
        "kind": "modern",
        "author": "Christos G. Doumas",
        "work": "The Wall-Paintings of Thera, Athènes, Thera Foundation, 1992"
      },
      {
        "kind": "modern",
        "author": "Spyridon Marinatos",
        "work": "Excavations at Thera, I à VII, Athènes, Société archéologique d'Athènes, 1968 à 1976"
      }
    ]
  },
  {
    "id": "destructions-de-1450-en-crete",
    "title": "Destructions de 1450 en Crète et Cnossos mycénienne",
    "start": -1449,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Destructions attestées par l'archéologie à la fin du minoen récent IB, vers 1450 en chronologie courante (de 1500 à 1450 selon les auteurs) ; leurs causes et le moment où une élite mycénienne prend Cnossos restent débattus.",
    "era": "bronze",
    "track": "minoens",
    "category": "politics",
    "importance": 2,
    "placeId": "phaistos",
    "summary": "Vers 1450, les palais et les villas de Crète sont incendiés presque partout : Phaistos, Malia, Zakros, Haghia Triada. Seule Cnossos s'en tire, mais elle change de maîtres : ses tombes de guerriers, sa céramique et bientôt ses archives en grec montrent qu'une élite venue du continent mycénien la gouverne désormais.",
    "body": "**Une vague d'incendies.** À la fin du minoen récent IB, la plupart des centres crétois brûlent, et beaucoup ne retrouvent jamais leur rôle de palais. Cnossos subit des dégâts plus limités et reste le seul grand palais de l'île, qui semble alors en contrôler une large part.\n\n**Une Cnossos mycénienne.** Dans les décennies suivantes apparaissent autour de Cnossos des tombes de guerriers, avec épées, casques et armes de bronze à la manière du continent, une céramique au décor plus rigide (le style dit « du Palais ») et surtout des tablettes en linéaire B, qui notent du grec. Les Grecs plus tardifs se souvenaient d'une Crète habitée par plusieurs peuples, dont des Achéens.\n\n**Ce qui est débattu.** Conquête venue du continent, guerre entre centres crétois dont des Mycéniens auraient profité, séismes, contrecoups lointains de l'éruption de Théra : aucune explication ne fait l'unanimité. On discute aussi de savoir si l'élite mycénienne s'installe à Cnossos dès 1450 ou une génération plus tard.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Odyssée",
        "locus": "XIX, 172 à 177 (les peuples de la Crète, dont les Achéens)"
      },
      {
        "kind": "modern",
        "author": "Jan Driessen et Colin F. Macdonald",
        "work": "The Troubled Island: Minoan Crete before and after the Santorini Eruption, Liège, Université de Liège, 1997 (Aegaeum, 17)"
      },
      {
        "kind": "modern",
        "author": "Oliver Dickinson",
        "work": "The Aegean Bronze Age, Cambridge, Cambridge University Press, 1994"
      }
    ]
  },
  {
    "id": "archives-en-lineaire-b-de-cnossos",
    "title": "Archives en linéaire B de Cnossos",
    "start": -1399,
    "end": -1349,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "La plupart des tablettes ont été cuites par l'incendie du palais au minoen récent IIIA2, vers 1370 à 1350 ; certaines sont plus anciennes (salle des Tablettes aux chars), et une minorité de chercheurs place l'incendie final vers 1200.",
    "era": "bronze",
    "track": "myceniens",
    "category": "society",
    "importance": 1,
    "placeId": "cnossos",
    "summary": "Le palais de Cnossos, désormais aux mains d'une élite mycénienne, tient ses comptes en linéaire B, une écriture syllabique tirée du linéaire A pour noter le grec. L'incendie du palais a cuit et conservé plusieurs milliers de tablettes : ce sont les plus anciens textes en langue grecque, déchiffrés par Michael Ventris en 1952.",
    "body": "**Des comptes en grec.** Les tablettes de Cnossos, trouvées par Arthur Evans dès 1900, recensent des troupeaux de dizaines de milliers de moutons, la laine et les tissus, des chars et des armes, des rations, des terres et des offrandes aux dieux. Elles nomment des lieux de toute la Crète centrale et occidentale, comme Phaistos, Amnisos ou Kydonia. Une tablette (KN V 52) cite Athana Potnia, Enyalios, Paiawon et Poséidon, noms familiers de la religion grecque plus tardive.\n\n**Un déchiffrement célèbre.** En 1952, l'architecte britannique Michael Ventris montre que le linéaire B note une forme ancienne du grec ; il publie la démonstration en 1953 avec le philologue John Chadwick. La découverte recule de plus de cinq siècles l'histoire écrite de la langue grecque et confirme que Cnossos était alors gouvernée par des Grecs.\n\n**Une date discutée.** Les tablettes ne portent pas de date : on les date par le contexte de l'incendie qui les a cuites. La plupart des spécialistes le placent au minoen récent IIIA2, vers 1370 à 1350, mais certains le font descendre vers 1200, ce qui changerait l'histoire de la Crète mycénienne.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Archives du palais de Cnossos",
        "work": "Tablette en linéaire B KN V 52",
        "locus": "Athana Potnia, Enyalios, Paiawon, Poséidon"
      },
      {
        "kind": "modern",
        "author": "Michael Ventris et John Chadwick",
        "work": "Evidence for Greek Dialect in the Mycenaean Archives, Journal of Hellenic Studies, 73, 1953",
        "locus": "p. 84 à 103"
      },
      {
        "kind": "modern",
        "author": "Michael Ventris et John Chadwick",
        "work": "Documents in Mycenaean Greek, 2e éd., Cambridge, Cambridge University Press, 1973"
      },
      {
        "kind": "modern",
        "author": "John Chadwick",
        "work": "The Decipherment of Linear B, Cambridge, Cambridge University Press, 1958"
      }
    ]
  },
  {
    "id": "liste-egeenne-d-amenhotep-iii",
    "title": "Les Égéens dans les textes égyptiens : la liste d'Amenhotep III",
    "start": -1379,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Amenhotep III règne de 1390 à 1352 environ selon la chronologie égyptienne courante ; la lecture de plusieurs noms de la liste reste discutée.",
    "era": "bronze",
    "track": "myceniens",
    "category": "politics",
    "importance": 2,
    "placeId": "temple-d-amenhotep-iii",
    "people": ["amenhotep-iii"],
    "summary": "Sur le socle d'une statue de son temple funéraire de Thèbes, à Kom el-Hettan, le pharaon Amenhotep III fait graver une liste de lieux égéens, sous les noms de Keftiou (la Crète) et de Tanaja (sans doute le continent grec) : Cnossos, Amnisos, Phaistos, Kydonia, Mycènes, Nauplie, Cythère. Certains y voient l'itinéraire d'une ambassade.",
    "body": "**Une liste gravée dans la pierre.** Le temple funéraire d'Amenhotep III, sur la rive ouest de Thèbes, avait dans sa cour des statues dont les socles énumèrent les peuples du monde connu. L'un d'eux, publié en 1966 par l'égyptologue Elmar Edel, porte en tête Keftiou et Tanaja, suivis d'une douzaine de noms de lieux crétois et continentaux, dans un ordre qui ressemble à un trajet par mer.\n\n**Des échanges bien attestés.** Sous Thoutmosis III déjà, les tombes de hauts fonctionnaires, comme celle du vizir Rekhmirê, montrent des Keftiou apportant des vases. Sous Amenhotep III et son fils Akhénaton, la céramique mycénienne abonde en Égypte, notamment à Amarna, et des plaques de faïence au nom d'Amenhotep III ont été trouvées à Mycènes. L'Égée exporte de l'huile parfumée, du vin et des vases ; elle reçoit de l'or, de l'ivoire, du verre et des pierres précieuses.\n\n**Ce qui est discuté.** Certaines lectures sont contestées, et l'on ignore si la liste reflète une ambassade réelle, des relations commerciales ou une géographie savante. Elle montre en tout cas que l'Égypte connaissait la Crète et le continent grec comme deux ensembles distincts.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Amenhotep III",
        "work": "Socle de statue du temple funéraire de Kom el-Hettan portant la liste égéenne (dit socle EN)"
      },
      {
        "kind": "modern",
        "author": "Elmar Edel",
        "work": "Die Ortsnamenlisten aus dem Totentempel Amenophis III., Bonn, Hanstein, 1966 (Bonner biblische Beiträge, 25)"
      },
      {
        "kind": "modern",
        "author": "Eric H. Cline",
        "work": "Sailing the Wine-Dark Sea: International Trade and the Late Bronze Age Aegean, Oxford, Tempus Reparatum, 1994 (BAR International Series, 591)"
      }
    ]
  },
  {
    "id": "ahhiyawa-dans-les-textes-hittites",
    "title": "Ahhiyawa dans les textes hittites",
    "start": -1399,
    "end": -1219,
    "precision": "century",
    "certainty": "debated",
    "certaintyNote": "L'identification d'Ahhiyawa avec les Achéens, donc avec un royaume mycénien, est admise par la plupart des spécialistes mais n'est pas prouvée ; les textes s'échelonnent du début du XIVe siècle à la fin du XIIIe, avec des dates approximatives.",
    "era": "bronze",
    "track": "myceniens",
    "category": "politics",
    "importance": 2,
    "placeId": "hattusa",
    "people": ["hattusili-iii"],
    "summary": "Une trentaine de textes des archives royales hittites, à Hattusa, mentionnent un pays d'Ahhiyawa, puissance d'outre-mer active sur la côte ouest de l'Anatolie autour de Millawanda (Milet). La plupart des historiens y voient les Achéens d'Homère, donc un royaume mycénien : ces lettres seraient alors les seuls témoignages étrangers sur sa politique.",
    "body": "**Ce que disent les textes.** Le plus ancien, l'acte d'accusation de Madduwatta (vers 1400), évoque un certain Attarissiya, « homme d'Ahhiya », qui mène des fantassins et des chars en Anatolie. Vers 1250, la lettre dite de Tawagalawa, sans doute écrite par Hattusili III, traite le roi d'Ahhiyawa de « frère », c'est-à-dire d'égal, au sujet d'un aventurier, Piyamaradu, réfugié à Millawanda ; elle évoque aussi un différend passé au sujet de Wilusa, que beaucoup rapprochent d'Ilios, Troie. Vers 1220, dans un traité de Tudhaliya IV avec le roi d'Amurru, le roi d'Ahhiyawa est inscrit parmi les grands rois, puis effacé.\n\n**Pourquoi c'est important.** Si Ahhiyawa désigne bien les Achéens, un royaume mycénien a pris part à la diplomatie des grandes puissances du Proche-Orient et a tenu un pied en Asie Mineure, à Milet, où l'archéologie confirme une forte présence mycénienne.\n\n**Ce qui reste discuté.** Le rapprochement entre Ahhiyawa et Achaioi, proposé par Emil Forrer en 1924, a longtemps été contesté ; il est aujourd'hui largement admis, mais on ignore où siégeait ce roi (Mycènes, Thèbes, Rhodes ?) et si Ahhiyawa fut toujours un seul royaume.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Arnuwanda Ier",
        "work": "Acte d'accusation de Madduwatta (CTH 147, KUB XIV 1)"
      },
      {
        "kind": "ancient",
        "author": "Hattusili III (attribution probable)",
        "work": "Lettre dite de Tawagalawa (CTH 181, KUB XIV 3)"
      },
      {
        "kind": "modern",
        "author": "Gary M. Beckman, Trevor R. Bryce et Eric H. Cline",
        "work": "The Ahhiyawa Texts, Atlanta, Society of Biblical Literature, 2011"
      },
      {
        "kind": "modern",
        "author": "Trevor R. Bryce",
        "work": "The Kingdom of the Hittites, nouv. éd., Oxford, Oxford University Press, 2005"
      }
    ]
  },
  {
    "id": "tresor-d-atree",
    "title": "Trésor d'Atrée",
    "start": -1299,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Date discutée : la céramique trouvée sous le seuil et dans les remblais place la construction entre 1350 et 1250 environ selon les fouilleurs (helladique récent IIIA ou IIIB).",
    "era": "bronze",
    "track": "myceniens",
    "category": "building",
    "importance": 2,
    "placeId": "tresor-d-atree",
    "summary": "Vers 1300, un souverain de Mycènes se fait bâtir une tombe à coupole (tholos) d'une ampleur jamais atteinte : un couloir de 36 mètres mène à une salle ronde de près de 15 mètres de diamètre et de 13 mètres de haut, couverte d'assises de pierre en encorbellement. Pausanias y voyait le trésor d'Atrée, père d'Agamemnon.",
    "body": "**Une prouesse de bâtisseurs.** La salle est couverte par une fausse coupole : 33 assises de blocs taillés, chacune avançant un peu sur la précédente, jusqu'à une pierre de fermeture. Le linteau intérieur de la porte, un bloc unique d'environ 8 mètres de long, pèse sans doute plus de 100 tonnes. La façade était ornée de demi-colonnes et de plaques de pierre de couleur, dont des fragments sont au British Museum ; une petite chambre latérale servait peut-être de sépulture.\n\n**Pourquoi c'est important.** C'est l'aboutissement de la tombe à tholos, apparue en Messénie et en Argolide quelques siècles plus tôt, et la preuve de la richesse et de la main-d'œuvre que commandaient les souverains de Mycènes, au moment où ils agrandissent leur citadelle.\n\n**Ce qui est incertain.** La tombe a été pillée dès l'Antiquité et l'on ignore qui y fut enterré : le nom d'Atrée vient de la tradition rapportée par Pausanias, pas d'une inscription. Sa date oscille entre le XIVe et le XIIIe siècle selon la lecture des tessons trouvés sous le seuil.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 16, 6 (les chambres souterraines d'Atrée et de ses fils)",
        "url": `${PAUSANIAS}:book=2:chapter=16`
      },
      {
        "kind": "modern",
        "author": "Alan J. B. Wace",
        "work": "Mycenae: An Archaeological History and Guide, Princeton, Princeton University Press, 1949"
      },
      {
        "kind": "modern",
        "author": "Oliver Dickinson",
        "work": "The Aegean Bronze Age, Cambridge, Cambridge University Press, 1994"
      }
    ]
  },
  {
    "id": "epave-d-uluburun",
    "title": "Épave d'Uluburun",
    "start": -1309,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Naufrage daté de la fin du XIVe siècle, vers 1320 à 1300, par la dendrochronologie du bois embarqué et par un scarabée d'or au nom de Néfertiti, qui donne une date après laquelle le navire a coulé.",
    "era": "bronze",
    "track": "myceniens",
    "category": "society",
    "importance": 2,
    "placeId": "uluburun",
    "summary": "Vers 1310, un navire marchand coule au large du cap d'Uluburun, en Lycie, avec une cargaison venue de tout le Proche-Orient : une dizaine de tonnes de lingots de cuivre, une tonne d'étain, du verre, de l'ivoire, de l'ébène, de la résine, des bijoux et des objets mycéniens. Fouillée de 1984 à 1994, l'épave est le plus riche témoignage du commerce de l'âge du bronze.",
    "body": "**Une cargaison de roi.** Repérée en 1982 par un pêcheur d'éponges, l'épave gît entre 44 et 52 mètres de fond. L'Institute of Nautical Archaeology (George Bass, puis Cemal Pulak) y a remonté 354 lingots de cuivre en forme de peau de bœuf et une centaine d'autres, environ une tonne d'étain, de quoi fondre une dizaine de tonnes de bronze, quelque 175 lingots de verre, des jarres cananéennes pleines de résine de térébinthe, des défenses d'éléphant et d'hippopotame, des bijoux d'or et d'argent, et un scarabée d'or au nom de la reine Néfertiti.\n\n**Pourquoi c'est important.** Le navire, sans doute parti de la côte du Levant ou de Chypre et en route vers l'ouest, montre concrètement les circuits qui reliaient l'Égypte, le Levant, Chypre et l'Égée. Quelques objets mycéniens (épées, sceaux, vases) laissent penser que des Égéens étaient à bord, peut-être pour accompagner un chargement destiné à un palais.\n\n**Ce qui reste incertain.** Le port de départ, la destination et la nature de la cargaison (commerce privé ou cadeau entre souverains) sont discutés, de même que la date exacte, connue à quelques décennies près.",
    "sources": [
      {
        "kind": "modern",
        "author": "Cemal Pulak",
        "work": "The Uluburun Shipwreck: An Overview, International Journal of Nautical Archaeology, 27, 3, 1998",
        "locus": "p. 188 à 224"
      },
      {
        "kind": "modern",
        "author": "Cemal Pulak",
        "work": "The Uluburun Shipwreck and Late Bronze Age Trade, dans Joan Aruz et al. (dir.), Beyond Babylon: Art, Trade, and Diplomacy in the Second Millennium B.C., New York, Metropolitan Museum of Art, 2008"
      }
    ]
  },
  {
    "id": "porte-des-lions",
    "title": "Porte des Lions et murs cyclopéens de Mycènes",
    "start": -1249,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique : agrandissement de l'enceinte à l'helladique récent IIIB, vers 1250, à quelques décennies près.",
    "era": "bronze",
    "track": "myceniens",
    "category": "building",
    "importance": 2,
    "placeId": "porte-des-lions",
    "summary": "Vers 1250, la citadelle de Mycènes est agrandie : une nouvelle muraille de blocs énormes englobe le cercle A des tombes royales et s'ouvre par la porte des Lions, surmontée de deux fauves dressés de part et d'autre d'une colonne. C'est le seul grand relief sculpté de l'âge du bronze égéen resté en place.",
    "body": "**Une enceinte de géants.** Les murs de Mycènes, épais de 5 à 8 mètres, sont faits de blocs de calcaire à peine équarris, si lourds que les Grecs plus tardifs les attribuaient aux Cyclopes ; d'où le nom de maçonnerie cyclopéenne. L'extension du XIIIe siècle fait entrer dans la citadelle le cercle A, que l'on respecte et réaménage. La porte, large d'environ 3 mètres, est couverte d'un linteau monolithe, surmonté d'un triangle de décharge où s'inscrit le relief.\n\n**Pourquoi c'est important.** Les deux animaux, lions ou lionnes, posent les pattes avant sur des autels, autour d'une colonne qui symbolise peut-être le palais ou une divinité. Leurs têtes, sculptées à part et aujourd'hui perdues, regardaient le visiteur. Le motif, connu sur les sceaux, devient ici un emblème du pouvoir, à l'entrée du chemin qui monte au palais.\n\n**Ce qui est discuté.** La date précise de la porte et des différentes phases de l'enceinte, l'espèce des animaux et le sens exact du relief restent discutés. Peu après, vers 1200, la citadelle est encore renforcée, avec un passage souterrain vers une citerne.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 16, 5 (l'enceinte et la porte aux lions, œuvre des Cyclopes)",
        "url": `${PAUSANIAS}:book=2:chapter=16`
      },
      {
        "kind": "modern",
        "author": "Elizabeth B. French",
        "work": "Mycenae: Agamemnon's Capital. The Site in Its Setting, Stroud, Tempus, 2002"
      },
      {
        "kind": "modern",
        "author": "Alan J. B. Wace",
        "work": "Mycenae: An Archaeological History and Guide, Princeton, Princeton University Press, 1949"
      }
    ]
  },
  {
    "id": "citadelle-de-tirynthe",
    "title": "Citadelle de Tirynthe",
    "start": -1249,
    "end": -1199,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Datation archéologique : dernière phase de l'enceinte et du palais à l'helladique récent IIIB, de 1250 à 1200 environ, à quelques décennies près.",
    "era": "bronze",
    "track": "myceniens",
    "category": "building",
    "importance": 3,
    "placeId": "tirynthe",
    "summary": "Au XIIIe siècle, Tirynthe, près de la mer en Argolide, s'enferme dans l'une des plus impressionnantes murailles cyclopéennes du monde mycénien, avec des galeries voûtées dans l'épaisseur des murs et un palais orné de fresques. L'Iliade la dit « entourée de murs », et Pausanias en admirait encore les blocs.",
    "body": "**Des murs et des galeries.** L'enceinte, agrandie en plusieurs étapes, atteint à la fin de l'helladique récent IIIB une épaisseur considérable ; les galeries couvertes en encorbellement des flancs est et sud, bordées de casemates, servaient sans doute de magasins. La ville haute porte le palais, avec son mégaron à foyer central et des fresques de chasse et de procession ; la ville basse est enclose à son tour, et des passages souterrains mènent à des sources hors les murs.\n\n**Pourquoi c'est important.** Tirynthe montre la main-d'œuvre qu'un palais mycénien pouvait mobiliser, et sa position proche de la côte en fait sans doute le port de la plaine d'Argos, à quinze kilomètres de Mycènes. Les légendes grecques y faisaient régner Eurysthée et vivre Héraclès.\n\n**Après les palais.** Détruite vers 1200, Tirynthe est l'un des rares sites où la vie reprend aussitôt et s'étend même : les fouilles allemandes ont montré que la ville basse est reconstruite et peuplée au XIIe siècle. Les rapports exacts entre Tirynthe et Mycènes, royaume distinct ou dépendance, restent discutés.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Iliade",
        "locus": "II, 559 (Tirynthe entourée de murs)"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "II, 25, 8 (les murs, œuvre des Cyclopes)",
        "url": `${PAUSANIAS}:book=2:chapter=25`
      },
      {
        "kind": "modern",
        "author": "Joseph Maran",
        "work": "Tiryns, dans Eric H. Cline (dir.), The Oxford Handbook of the Bronze Age Aegean, Oxford, Oxford University Press, 2010",
        "locus": "p. 722 à 734"
      }
    ]
  },
  {
    "id": "palais-de-pylos",
    "title": "Palais de Pylos et ses archives",
    "start": -1299,
    "end": -1199,
    "precision": "century",
    "certainty": "attested",
    "certaintyNote": "Le palais prend sa forme finale au XIIIe siècle et brûle vers 1200, parfois daté vers 1180 ; les tablettes conservées datent de ses derniers mois.",
    "era": "bronze",
    "track": "myceniens",
    "category": "society",
    "importance": 2,
    "placeId": "palais-de-nestor",
    "summary": "À Ano Englianos, en Messénie, le palais dit « de Nestor » gouverne au XIIIe siècle un royaume divisé en deux provinces. L'incendie qui le détruit vers 1200 a cuit plus d'un millier de tablettes en linéaire B : elles décrivent les terres, les redevances, les artisans, les offrandes aux dieux et les derniers préparatifs militaires du royaume.",
    "body": "**Le palais le mieux conservé.** Fouillé par Carl Blegen à partir de 1939, le palais a livré dès le premier jour sa salle d'archives. On y lit le plan type du palais mycénien : un vestibule, puis la grande salle du trône (mégaron) avec son foyer circulaire peint, ses colonnes et ses fresques, entourée de magasins d'huile et de vin, d'ateliers et d'une salle de bains avec sa baignoire.\n\n**Un royaume en chiffres.** Les tablettes nomment le roi (wanax), un chef de l'armée (lawagetas), des dizaines de localités réparties entre une province proche et une province lointaine, des femmes employées au textile, des bronziers, des rameurs. Une série (PY An 657 et suivantes) répartit des « guetteurs » le long de la côte ; une autre (PY Tn 316) enregistre des vases d'or et, semble-t-il, des hommes et des femmes offerts à des divinités, dont Zeus, Héra et Hermès.\n\n**Ce qui est discuté.** On ne sait si les guetteurs et les rameurs trahissent une menace précise juste avant l'incendie. Le lien avec Nestor, roi de Pylos chez Homère, relève de la tradition, et la date de l'incendie varie selon les auteurs entre 1200 et 1180 environ.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Archives du palais de Pylos",
        "work": "Tablettes en linéaire B PY An 657 et PY Tn 316"
      },
      {
        "kind": "ancient",
        "author": "Homère",
        "work": "Iliade",
        "locus": "II, 591 à 602 (le contingent de Pylos et de Nestor)"
      },
      {
        "kind": "modern",
        "author": "Carl W. Blegen et Marion Rawson",
        "work": "The Palace of Nestor at Pylos in Western Messenia, I, The Buildings and Their Contents, Princeton, Princeton University Press, 1966"
      },
      {
        "kind": "modern",
        "author": "Michael Ventris et John Chadwick",
        "work": "Documents in Mycenaean Greek, 2e éd., Cambridge, Cambridge University Press, 1973"
      }
    ]
  },
  {
    "id": "archives-de-la-cadmee-de-thebes",
    "title": "Archives de la Cadmée de Thèbes",
    "start": -1229,
    "end": -1199,
    "precision": "decade",
    "certainty": "attested",
    "certaintyNote": "Les tablettes, conservées par l'incendie du palais, datent de la fin de l'helladique récent IIIB, vers 1225 à 1200 selon les fouilleurs ; leur interprétation est très discutée.",
    "era": "bronze",
    "track": "myceniens",
    "category": "society",
    "importance": 3,
    "placeId": "thebes",
    "summary": "Sous la ville moderne de Thèbes, les fouilles de la Cadmée ont mis au jour les restes d'un grand palais mycénien et ses archives : plusieurs centaines de tablettes et de scellés en linéaire B, dont environ 240 tablettes trouvées de 1993 à 1995 rue Pélopidas, et un trésor de sceaux-cylindres orientaux. Elles font de Thèbes l'un des grands royaumes de la fin du XIIIe siècle.",
    "body": "**Un palais sous la ville.** Thèbes n'a jamais cessé d'être habitée, et son palais ne se fouille que par morceaux, au gré des chantiers de construction. On y a retrouvé depuis le début du XXe siècle des ateliers, des magasins, des fresques et, en 1963 et 1964, une quarantaine de sceaux-cylindres, pour la plupart en lapis-lazuli, venus de Mésopotamie et de Syrie, dont certains d'époque kassite : sans doute un cadeau diplomatique ou un butin.\n\n**Des archives en grec.** Les tablettes de la rue Pélopidas enregistrent surtout des distributions d'orge, de vin et d'autres denrées à des personnes, à des lieux et peut-être à des sanctuaires. Elles nomment des lieux de Béotie et d'Eubée, comme Amarynthos, et un homme dit « de Lacédémone ». D'autres séries comptent la laine et les tissus.\n\n**Ce qui est discuté.** Les éditeurs ont lu dans certaines tablettes des offrandes à des divinités et à des animaux sacrés ; d'autres linguistes contestent ces lectures. Le rang de Thèbes, que certains proposent comme siège du roi d'Ahhiyawa des textes hittites, est lui aussi débattu.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Archives du palais de Thèbes",
        "work": "Tablettes en linéaire B de la rue Pélopidas (séries TH Fq, Av, Gp)"
      },
      {
        "kind": "ancient",
        "author": "Pausanias",
        "work": "Description de la Grèce",
        "locus": "IX, 5, 1 et 2 (Cadmos et la Cadmée)",
        "url": `${PAUSANIAS}:book=9:chapter=5`
      },
      {
        "kind": "modern",
        "author": "Vassilis L. Aravantinos, Louis Godart et Anna Sacconi",
        "work": "Thèbes. Fouilles de la Cadmée, I, Les tablettes en linéaire B de la Odos Pelopidou. Édition et commentaire, Pise et Rome, Istituti editoriali e poligrafici internazionali, 2001"
      },
      {
        "kind": "modern",
        "author": "Edith Porada",
        "work": "The Cylinder Seals Found at Thebes in Boeotia, Archiv für Orientforschung, 28, 1981"
      }
    ]
  },
  {
    "id": "peuples-de-la-mer",
    "title": "Ramsès III contre les Peuples de la mer",
    "start": -1176,
    "precision": "year",
    "certainty": "attested",
    "certaintyNote": "Campagne attestée par des textes contemporains ; l'an 8 de Ramsès III correspond à 1177 environ selon la chronologie égyptienne courante, à quelques années près. Le récit est celui de la propagande royale, et l'identité de ces peuples comme leur rôle dans la chute des palais égéens sont débattus.",
    "era": "bronze",
    "track": "myceniens",
    "category": "war",
    "importance": 2,
    "placeId": "medinet-habou",
    "people": ["ramses-iii"],
    "summary": "En l'an 8 de son règne, vers 1177, Ramsès III affirme avoir repoussé sur terre et sur mer une coalition de peuples venus « de leurs îles », après qu'ils eurent dévasté le Hatti, Chypre et la Syrie. Les reliefs de son temple de Médinet Habou donnent l'image la plus célèbre de la crise qui emporte, entre 1200 et 1150, les grands États de la Méditerranée orientale.",
    "body": "**Le récit du pharaon.** L'inscription de l'an 8, gravée sur les murs du temple funéraire de Ramsès III à Médinet Habou, énumère les Peleset, les Tjeker, les Shekelesh, les Denyen et les Weshesh ; elle affirme qu'aucun pays n'a tenu devant eux, du Hatti à Alashiya (Chypre) et à Amurru, avant que l'Égypte ne les arrête à ses frontières et dans les bouches du Nil. Les reliefs montrent une bataille navale et des chariots à bœufs chargés de femmes et d'enfants : des migrants autant que des pillards. Une génération plus tôt, vers 1208, Mérenptah avait déjà repoussé des Ekwesh, des Shardana et des Lukka alliés aux Libyens.\n\n**Pourquoi c'est important.** Les Peleset sont les Philistins, installés ensuite sur la côte de Canaan avec une céramique d'inspiration mycénienne. Certains noms ont été rapprochés de peuples égéens : les Denyen des Danaens, les Ekwesh des Achéens. Ces textes sont le seul récit contemporain de l'effondrement de la fin de l'âge du bronze.\n\n**Ce qui est débattu.** L'inscription est un texte de propagande, et ces peuples sont peut-être autant une conséquence qu'une cause de la crise. Rien ne prouve qu'ils aient détruit les palais grecs : les causes de la chute de Pylos ou de Mycènes restent multiples et discutées.",
    "sources": [
      {
        "kind": "ancient",
        "author": "Ramsès III",
        "work": "Inscription de l'an 8, temple funéraire de Médinet Habou"
      },
      {
        "kind": "ancient",
        "author": "Ramsès IV (au nom de Ramsès III)",
        "work": "Grand papyrus Harris I",
        "locus": "76, 6 à 11 (les guerres de Ramsès III)"
      },
      {
        "kind": "modern",
        "author": "William F. Edgerton et John A. Wilson",
        "work": "Historical Records of Ramses III: The Texts in Medinet Habu, Volumes I and II, Chicago, University of Chicago Press, 1936"
      },
      {
        "kind": "modern",
        "author": "Nancy K. Sandars",
        "work": "The Sea Peoples: Warriors of the Ancient Mediterranean, Londres, Thames and Hudson, 1978"
      },
      {
        "kind": "modern",
        "author": "Eric H. Cline",
        "work": "1177 avant J.-C. Le jour où la civilisation s'est effondrée, Paris, La Découverte, 2015"
      }
    ]
  }
]
