# 🎙️ PSY7010 — Séance 4 (Séminaire 1) : Boîte à Outils Podcasts NotebookLM
*Boîte à outils de préparation audio pour l'atelier du Mardi 29 septembre 2026 (Local SU-1550)*

* **Destinataire :** Michel Mercier (Cohorte Maîtrise UQAM)
* **Objectif :** Générer des capsules audio courtes (3 à 5 minutes) ciblées, vivantes et percutantes, 100 % ancrées dans les extractions de cours (`PSY7010-03_GOLD.md`) et les documents officiels.

> [!IMPORTANT]
> **Règle Linguistique Absolue : TOUJOURS Français Canada (`fr-CA`). JAMAIS France.**
> Les co-animateurs doivent impérativement s'exprimer dans un français québécois / canadien soigné, fluide et universitaire (UQAM). Bannissement absolu des tics verbaux et tournures typiques de France (*« du coup »*, *« en vrai »*, *« pour le coup »*, *« boulot »*, *« bagnole »*, etc.).

---

## 🧭 Vue d'ensemble des 4 Capsules Audio Courtes (3 à 5 min)

| N° | Titre de la Capsule | Durée visée | Angle Pédagogique & Clinique | Source dans NotebookLM | Code Source ID |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **1** | **Le Vol AF-447 : Le Piège de l'Alarme et l'Asymétrie Sensorielle** | ~4 min | Décortiquer le paradoxe de l'avertisseur de décrochage coupé sous 60 kts et les mini-manches non couplés | `[S04-Seminaire] Human Factors 101 - Vol AF447 (Air France 447)` | `2f82db34-8cd9-48a2-9e8b-87ea57bd02e4` |
| **2** | **L'Affaire des Pompes PCA (Lin et al., 1998) : Menus Aveugles et Interruptions** | ~4 min | L'opacité de 8 à 27 écrans, la mémoire de travail des soignants et la mise en garde écologique de Bédard | `[S04-Seminaire] Lin et al. (1998) - Ergonomie de l'auto-injecteur PCA` | `d8798638-4b00-40f1-b021-2bf4def48dd3` |
| **3** | **La Méthode Passalacqua (Diapo 92) : Pourquoi Blâmer l'Humain est une Erreur** | ~4 min | La grille en 4 questions et la triangulation obligatoire (observationnel, perceptuel, physiologique) | `[S03-GOLD] Verbatim intégral et enseignement Mario Passalacqua` + `[S03-Diapos]` | `0ed0f8bc-745b-44f6-88b7-34e8c9d5a1c3` & `fa46faa5-b25e-4879-a578-752de5b746b1` |
| **0** | **Le Briefing de l'Atelier (SU-1550) : Accueil & Déroulement** | ~3 min | Déroulement en 3 locaux par concentration, circulation des profs et feuille de 2 questions remises à 12h15 | `[S04-Seminaire] Cadrage public et consignes du Séminaire 1` | `ee734fb1-74ac-4017-8205-58ab43efd953` |

---

## 🛠️ Prompts NotebookLM Prêts à l'Emploi (Français Canada Obligatoire)

### Capsule 1 : Le Vol AF-447 (Le Paradoxe de l'Alarme et les Mini-Manches)
* **Configuration MCP :** `artifact_type: "audio"`, `language: "fr-CA"`, `source_ids: ["2f82db34-8cd9-48a2-9e8b-87ea57bd02e4"]`

```text
Langue et registre obligatoires : Français canadien (Québec). Les deux co-animateurs s'expriment dans un français québécois naturel, soigné et universitaire (registre de l'UQAM). Ne jamais utiliser d'accents parisiens ni de tournures ou expressions franco-françaises (interdiction de "du coup", "en vrai", "pour le coup", "boulot", etc.).

Format : Court épisode de podcast conversationnel (3 à 4 minutes max) entre deux étudiants ou chercheurs passionnés d'ingénierie cognitive et de facteurs humains.

Sujet : Pourquoi le vol Air France 447 n'est PAS une "erreur de pilotage", mais un piège d'interface redoutable.

Points obligatoires à débattre avec un rythme dynamique :
1. Le fait technique déclencheur : Le givrage temporaire des sondes Pitot en haute altitude, la perte d'indication de vitesse et le passage en loi alternative (sans protections automatiques de décrochage).
2. L'aberration de l'alarme de décrochage : Expliquer le paradoxe tragique découvert par le BEA : sous 60 nœuds de vitesse, les calculateurs jugent les sondes d'incidence invalides et COUPENT l'alarme sonore. Lorsque le copilote a poussé le manche vers l'avant pour sauver l'avion, la vitesse est remontée au-dessus de 60 nœuds et l'alarme s'est remise à hurler ! L'interface punissait l'action salvatrice.
3. Les mini-manches passifs (Side-sticks) : Contrairement aux Boeing ou aux avions classiques, les manches ne sont pas reliés mécaniquement. Le copilote de gauche ignorait totalement que son collègue de droite tirait le manche à cabrer en continu.
4. Conclusion : Rappeler la règle d'or du Pr Mario Passalacqua : « L'erreur humaine décrit le résultat, jamais la cause ».

Ton : Vivant, direct, percutant, empathique, accessible pour une écoute sur le pouce.
```

---

### Capsule 2 : L'Affaire des Pompes PCA (Lin et al., 1998)
* **Configuration MCP :** `artifact_type: "audio"`, `language: "fr-CA"`, `source_ids: ["d8798638-4b00-40f1-b021-2bf4def48dd3"]`

```text
Langue et registre obligatoires : Français canadien (Québec). Les deux co-animateurs s'expriment dans un français québécois naturel, soigné et universitaire (registre de l'UQAM). Ne jamais employer de tics de langage ou d'expressions typiques de France (pas de "du coup", "en vrai", "pour le coup", etc.).

Format : Capsule audio vivante et rythmée de 3 à 4 minutes sur l'ergonomie hospitalière et la sécurité des patients.

Sujet : L'étude historique de Lin et al. (1998) sur les erreurs de programmation de la pompe à morphine Abbott Lifecare 4100.

Fil conducteur obligatoire :
1. Le constat de départ : 60 % des accidents graves avec des dispositifs médicaux selon la FDA sont des erreurs d'utilisation humaine. Pourquoi ? Pas parce que les infirmières sont négligentes, mais parce que l'interface est aveugle.
2. Les failles ergonomiques de la pompe Abbott :
   - L'opacité séquentielle : Devoir naviguer à l'aveugle à travers 8 à 27 écrans sur un minuscule afficheur LCD d'une seule ligne, sans aucune vue d'ensemble du protocole.
   - La touche ambiguë REVIEW/CHANGE qui change de rôle selon qu'on est en train d'entrer un chiffre ou de vérifier.
3. La réalité du terrain hospitalier : Les interruptions incessantes en salle de réveil. L'absence d'information dans l'environnement force l'infirmière à tout garder en mémoire de travail.
4. La mise en garde du Pr Marc-André Bédard : Rappeler que Lin a testé son prototype sur 12 étudiantes novices sur ordinateur. En milieu clinique réel, changer une interface auprès d'infirmières chevronnées soulève le risque d'intrusion de leurs anciennes habitudes motrices !

Ton : Clinique, empathique, percutant, concret.
```

---

### Capsule 3 : La Méthode Passalacqua (La Diapositive 92 et les 4 Questions)
* **Configuration MCP :** `artifact_type: "audio"`, `language: "fr-CA"`, `source_ids: ["0ed0f8bc-745b-44f6-88b7-34e8c9d5a1c3", "fa46faa5-b25e-4879-a578-752de5b746b1"]`

```text
Langue et registre obligatoires : Français canadien (Québec). Les deux co-animateurs s'expriment dans un français québécois naturel, chaleureux et rigoureux (registre de l'UQAM). Proscription totale des formules hexagonales ("du coup", "en vrai", etc.).

Format : Dialogue vif et très clair de 3 à 4 minutes pour outiller un étudiant à la maîtrise qui prépare son séminaire d'analyse de cas.

Sujet : Comment décortiquer un cas réel en facteurs humains sans jamais tomber dans le piège du blâme individuel.

Points clés à couvrir :
1. La diapositive 92 du Pr Mario Passalacqua : La boussole en 4 questions pour aborder n'importe quel accident :
   - Question 1 : Qu’est-ce qui est établi dans le cas ? (Faits techniques bruts, logs, données avérées, zéro roman).
   - Question 2 : Comment fonctionnent le système et le travail ? (L'interface, la tâche réelle, le contexte).
   - Question 3 : Quels concepts de facteurs humains expliquent ce qui se passe ? (Conscience de la situation, charge mentale, modèles mentaux).
   - Question 4 : Qu’est-ce qu’on pourrait modifier et comment l'évaluer scientifiquement ? (C'est là que se joue la note !).
2. Le principe de triangulation des mesures : Rappeler la phrase clé de Passalacqua : « Ce qui est observable ne nous dit pas automatiquement ce que la personne pense ou ressent ». Il faut toujours croiser ce qu'on observe (erreurs, temps), ce que l'usager rapporte (charge mentale ressentie) et ce que son corps manifeste (fréquence cardiaque).

Ton : Pédagogique, stimulant, très structuré.
```

---

### Capsule 0 : Le Briefing de l'Atelier (Organisation & Déroulement dans le SU-1550)
* **Configuration MCP :** `artifact_type: "audio"`, `language: "fr-CA"`, `source_ids: ["ee734fb1-74ac-4017-8205-58ab43efd953"]`

```text
Langue et registre obligatoires : Français canadien (Québec). Les deux co-animateurs adoptent un ton québécois familier mais rigoureux, complice et décontracté (UQAM). Bannir absolument les expressions de France.

Format : Court briefing d'avant-séminaire de 2 à 3 minutes, énergique et déstressant, pour préparer un étudiant qui arrive au pavillon Adrien-Pinard (Local SU-1550) le mardi 29 septembre à 9h30.

Contenu du briefing :
1. L'organisation réelle : Le groupe ne reste pas en grand amphithéâtre. Il est immédiatement scindé en trois sous-groupes dans trois locaux différents selon les concentrations (Santé et services sociaux, Ingénierie et facteurs humains, Commerce et consommation).
2. Ce qui va se passer pendant 3 heures : C'est de l'apprentissage par l'action. On discute, on débat, on confronte ses questions. Les professeurs Passalacqua et Bédard vont circuler d'un local à l'autre pour écouter, poser des questions et tester la solidité de nos arguments.
3. Le livrable officiel à 12h15 : Une feuille écrite remise en main propre aux professeurs avec DEUX questions ouvertes (une sur AF-447, une sur Lin 1998).
4. Le conseil d'or de Passalacqua pour la rédaction : « Pas de roman de 5 pages ! Écrivez de façon succincte, en puces, en reliant un fait concret à un dilemme de conception ».

Ton : Rassurant, complice, motivant et parfaitement calé sur la réalité du cours.
```
