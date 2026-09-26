# 🧭 Guide d'Étude & Préparation — Séminaire 1
## Analyse d'incidents critiques en milieux technologiques : Aéronautique civile & Dispositifs médicaux
**Cours :** PSY7010 — Sciences psychologiques appliquées : Milieux technologiques  
**Cohorte de Maîtrise — Université du Québec à Montréal (UQAM)**  
**Séance d'évaluation :** Mardi 29 septembre 2026 (09h30 – 12h30, Local SU-1550)  
**Pondération officielle :** 10 % de la note finale (Participation aux séminaires — *La nature du travail*)  

---

### 1. À quoi s'attendre le 29 septembre : Modalités & Déroulement de l'atelier

Le Séminaire 1 est un atelier d'apprentissage par l'action (*in situ*) consacré à la discussion et à l'analyse critique de deux cas réels de défaillances sociotechniques.

* **Organisation en 3 locaux distincts par concentration :**  
  Dès l'arrivée au local SU-1550, le groupe est divisé en **trois sous-groupes répartis dans trois locaux différents**, correspondant aux trois concentrations de la maîtrise :
  1. **Santé et services sociaux**
  2. **Ingénierie et facteurs humains**
  3. **Commerce et consommation**  
  *Finalité pédagogique :* L'objectif de cette séparation par concentration est de mobiliser le regard spécifique de chaque discipline face à des problèmes concrets issus de secteurs hautement technologiques.
* **Dynamique de travail en sous-groupes :**  
  Chaque étudiant arrive avec ses réflexions et ses questions préalablement préparées. Les membres de l'équipe confrontent leurs lectures, débattent des causes profondes des incidents et vérifient la pertinence de leurs pistes de solution.
* **Circulation et présence des professeurs :**  
  Les professeurs Mario Passalacqua et Marc-André Bédard circulent activement d'un local à l'autre tout au long de la matinée pour écouter les échanges, tester la solidité de vos analyses et relancer la discussion sur les points méthodologiques sensibles.
* **Livrable officiel à la fin de la séance :**  
  À la clôture de la séance (vers 12h15–12h30), chaque étudiant remet individuellement aux professeurs **une feuille écrite comprenant deux questions ouvertes critiques** :
  * **Question 1 :** Portant sur l'accident du vol **Air France AF-447 (Airbus A330)**.
  * **Question 2 :** Portant sur l'étude d'ergonomie hospitalière de **Lin et al. (1998)** (Pompe PCA Abbott Lifecare 4100).

> [!TIP]
> **🎙️ Écoute guidée — Capsule 0 : Briefing de l'Atelier (Local SU-1550)** *(Durée : 2 min 45 • Registre fr-CA UQAM)*  
> Un briefing audio vivant pour vous projeter dans l'ambiance du pavillon Adrien-Pinard (local SU-1550), la dynamique de séparation en 3 locaux par concentration, la circulation active de Passalacqua et Bédard, et la consigne de concision pour la remise des 2 questions à 12h15.  
> 👉 **Fichier audio :** [`PSY7010_S04_Capsule_00_Briefing_Atelier_SU1550.m4a`](PSY7010_S04_Capsule_00_Briefing_Atelier_SU1550.m4a)

---

### 2. Méthode d'Analyse d'un Cas Pratique : La Grille de Raisonnement

Lors du cours du 22 septembre, le professeur Mario Passalacqua a projeté à la **diapositive 92** la grille de raisonnement guidé indispensable pour décortiquer n'importe quelle étude de cas en facteurs humains :

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                       LES 4 QUESTIONS FONDAMENTALES D'ANALYSE DE CAS                        │
│                           (Pr Mario Passalacqua, Diapositive 92)                            │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Qu’est-ce qui est établi dans le cas ?                                                   │
│    -> Les faits techniques bruts, les constats avérés et documentés, sans spéculation.     │
│                                                                                             │
│ 2. Comment fonctionnent le système et le travail ?                                          │
│    -> La tâche réelle, l'organisation de l'équipe, l'environnement physique et l'interface. │
│                                                                                             │
│ 3. Quels concepts de facteurs humains aident réellement à expliquer ce qui se passe ?       │
│    -> Conscience de la situation, charge mentale, modèles mentaux, retours sensoriels.      │
│                                                                                             │
│ 4. Qu’est-ce qu’on pourrait modifier dans le système, et qu’est-ce qu’il faudrait         │
│    encore savoir pour évaluer cette piste ?                                                 │
│    -> Arbitrage de conception (compromis) et définition d'un protocole de mesure empirique. │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Lien avec la démarche de recherche *in situ* en 4 phases (Guide officiel Moodle)
Cette grille s'inscrit directement dans la démarche méthodologique en 4 phases distribuée sur Moodle (`Methode_4_Phases.pdf`) :
1. **Comprendre (Cadrage & Diagnostic) :** Établir si le problème est véritablement cognitivo-comportemental (et non purement mécanique ou financier).
2. **Concevoir (Idéation & Faisabilité) :** Déterminer ce qu'il faut modifier ou préserver dans l'interface et le système sociotechnique.
3. **Évaluer (Expérimentation de terrain) :** Tester la solution via des protocoles contrôlés (tests A/B, quasi-expérimentations) en mesurant les variables avant et après.
4. **Déployer (Analyse critique & Diffusion) :** Anticiper les effets pervers dans la durée, les différences écologiques de terrain et les risques de contournements (*workarounds*) par les opérateurs.

#### Principe de triangulation des mesures (Diapos 61 à 64)
Mario Passalacqua a insisté sur un axiome central : **« Ce qui est observable ne nous dit pas automatiquement ce que la personne pense ou ressent »** (exemple des six vérifications consécutives d'un opérateur). Une analyse rigoureuse nécessite de croiser les trois familles d'indicateurs :
* **Mesures observationnelles :** Ce qu'on observe directement (temps d'exécution, nombre d'erreurs de frappe, déviations de trajectoire, logs système).
* **Mesures perceptuelles :** Ce que l'opérateur rapporte subjectivement (questionnaires de charge mentale comme le NASA-TLX, sentiment d'autonomie ou d'incompréhension).
* **Mesures physiologiques :** Ce qui se passe dans le corps (variations de la fréquence cardiaque, activité électrodermale sous stress aigu).

> [!TIP]
> **🎙️ Écoute guidée — Capsule 3 : La Méthode Passalacqua (Diapo 92 & Triangulation)** *(Durée : 3 min 50 • Registre fr-CA UQAM)*  
> Décortique la grille des 4 questions fondamentales, le refus catégorique de blâmer l'humain (*« l'erreur décrit le résultat, jamais la cause »*) et la triangulation obligatoire des trois familles de mesures (observationnelle, perceptuelle, physiologique).  
> 👉 **Fichier audio :** [`PSY7010_S04_Capsule_03_Methode_Passalacqua_Diapo92.m4a`](PSY7010_S04_Capsule_03_Methode_Passalacqua_Diapo92.m4a)

---

### 3. Fiches de Repères sur les Deux Dossiers de Cas

> [!NOTE]
> **Consultation des sources complètes :**  
> Les deux textes officiels intégraux sont directement consultables dans le volet de lecture à droite de la plateforme :
> - Onglet `✈️ AF447 (Human Factors 101)` : Rapport complet traduit en français et version anglaise originale.
> - Onglet `🏥 Lin et al. (1998) : Pompes PCA` : Synthèse clinique et expérimentale intégrale.

#### Dossier A : L'Accident du Vol Air France 447 (Airbus A330)
* **Contexte technique :** Dans la nuit du 1er juin 2009, suite au givrage passager des sondes Pitot en haute altitude, les calculateurs perdent la mesure fiable de vitesse. Le pilote automatique et l'automanette se déconnectent. L'appareil passe en loi alternative (*Alternate Law*), désactivant les protections automatiques contre le décrochage.
* **Faits empiriques établis :**
  1. *L'inhibition paradoxale de l'alarme de décrochage :* Lorsque la vitesse mesurée descend sous 60 nœuds, les calculateurs jugent les valeurs d'incidence non valides et coupent l'alarme sonore. Lorsque le copilote pousse sur le manche pour piquer et regagner de la portance, la vitesse repasse au-dessus de 60 nœuds, ce qui **réactive l'alarme sonore**, induisant chez l'équipage l'illusion que l'action à piquer aggrave le problème !
  2. *Les mini-manches latéraux passifs (Side-sticks) :* Les commandes des deux pilotes ne sont pas couplées mécaniquement. Le copilote surveillant (PNF) n'avait aucun retour tactile ni visuel direct pour constater que son collègue maintenait le manche cabré à fond pendant la quasi-totalité de la chute.
  3. *Perte de conscience de la situation (Niveaux 1, 2 et 3) :* L'alarme de décrochage a retenti pendant près de 4 minutes sans jamais être verbalisée ni discutée par les pilotes, saturés par les alertes visuelles secondaires de l'ECAM.

> [!TIP]
> **🎙️ Écoute guidée — Capsule 1 : Le Crash AF-447 (Le Piège de l'Alarme & les Side-Sticks)** *(Durée : 3 min 40 • Registre fr-CA UQAM)*  
> Analyse percutante des facteurs humains du vol AF-447 : le paradoxe de l'alarme coupée sous 60 nœuds (qui se remet à hurler quand le copilote pousse à piquer), les mini-manches passifs désynchronisés et le gouffre d'évaluation de Norman.  
> 👉 **Fichier audio :** [`PSY7010_S04_Capsule_01_Vol_AF447.m4a`](PSY7010_S04_Capsule_01_Vol_AF447.m4a)

#### Dossier B : Ergonomie des Pompes PCA (Lin et al., 1998)
* **Contexte clinique :** Les pompes d'analgésie autocontrôlée par le patient (PCA) permettent aux personnes hospitalisées d'administrer des doses précises de morphine sous prescription stricte. Les statistiques hospitalières démontrent que **60 % des incidents graves sont dus à des erreurs d'utilisation humaine** et non à des pannes de mécanique.
* **Faits empiriques établis :**
  1. *Opacité du dialogue séquentiel :* Sur l'appareil standard (Abbott Lifecare 4100), la programmation impose de naviguer à l'aveugle à travers 8 à 27 écrans sur un minuscule afficheur LCD d'une seule ligne, sans vue d'ensemble du protocole.
  2. *Touches multifonctions ambiguës :* La même touche (`REVIEW/CHANGE`) sert tantôt à valider un paramètre, tantôt à en modifier la valeur, créant des risques majeurs d'erreurs de mode.
  3. *L'impact critique des interruptions :* En salle de réveil ou aux soins intensifs, les infirmières sont continuellement interrompues. L'absence de visibilité immédiate de l'état système oblige à stocker les réglages en mémoire de travail, provoquant un délai de reprise (*resumption lag*) propice aux erreurs de programmation.
  4. *La nuance écologique (« No one-size-fits-all ») :* L'étude de Lin et al. a validé son interface révisée auprès de 12 étudiantes novices sur ordinateur de laboratoire. En milieu hospitalier réel, implanter une nouvelle interface chez des soignants très expérimentés peut provoquer des erreurs d'intrusion dues au conflit avec leurs anciennes habitudes motrices.

> [!TIP]
> **🎙️ Écoute guidée — Capsule 2 : L'Affaire Lin et al. 1998 (Pompes PCA, Menus Aveugles & Interruptions)** *(Durée : 3 min 45 • Registre fr-CA UQAM)*  
> Analyse clinique de l'ergonomie hospitalière de la pompe Abbott 4100 : l'opacité de 8 à 27 écrans, la touche ambiguë `REVIEW/CHANGE`, la surcharge en mémoire de travail sous interruptions continues et la mise en garde écologique de Bédard sur les 12 novices.  
> 👉 **Fichier audio :** [`PSY7010_S04_Capsule_02_Pompes_PCA_Lin1998.m4a`](PSY7010_S04_Capsule_02_Pompes_PCA_Lin1998.m4a)

---

### 4. Comment Formuler une Question Ouverte Pertinente & Pièges à Éviter

Pour réussir votre évaluation et alimenter des discussions stimulantes lors du séminaire, appliquez les directives énoncées par le corps professoral en classe :

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                          STRUCTURE D'UNE QUESTION D'INGÉNIERIE COGNITIVE                     │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Le Constat Observable :                                                                  │
│    Un fait technique précis et indiscutable tiré du cas (sans jugement de valeur).          │
│                                                                                             │
│ 2. Le Mécanisme Cognitif :                                                                  │
│    Pourquoi ce fait affecte-t-il le traitement humain de l'information (retour sensoriel,   │
│    affordance, modèle mental, mémoire de travail) ?                                         │
│                                                                                             │
│ 3. L'Arbitrage Ouvert (Le Dilemme de Conception) :                                          │
│    Une interrogation ouverte débutant par « Comment... » ou « Selon quel compromis... »,    │
│    mettant en tension deux exigences (sécurité vs flexibilité, automatisation vs contrôle)  │
│    ou interrogeant le protocole d'évaluation de la solution.                                │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Les 4 pièges réels à éviter impérativement :

* ❌ **Piège 1 : Blâmer l'opérateur humain (« L'erreur du pilote » ou « L'inattention infirmière »)**  
  *Directrice de Mario Passalacqua :* **« L'erreur humaine décrit le résultat, jamais la cause »**. Blâmer l'usager est un non-sens en facteurs humains. L'analyse consiste à comprendre ce qui, dans la structure de l'interface et le contexte du travail, a rendu l'action de l'opérateur rationnelle à ses yeux au moment où il l'a accomplie.
* ❌ **Piège 2 : La fausse question fermée (Oui / Non)**  
  *Directive de Marc-André Bédard :* Une question dont la réponse se résume par un « oui » ou un « non » bloque la discussion et n'apporte rien. Vos questions doivent inviter à un arbitrage de conception complexe.
* ❌ **Piège 3 : Le « roman » de 500 mots**  
  *Directive de Mario Passalacqua :* Les professeurs demandent de la concision. Évitez les longues tournures académiques. Une formulation courte, télégraphique ou articulée en quelques puces directes est beaucoup plus percutante et professionnelle.
* ❌ **Piège 4 : Le problème formulé comme un simple détail mécanique**  
  Veillez à toujours relier le dysfonctionnement technique à la perception ou au comportement de l'opérateur (ex. une force excessive sur un outil n'est pas qu'un frottement mécanique, c'est un déficit de retour haptique qui empêche l'opérateur de confirmer l'état de son action).

---

### 5. Grille de Validation Personnelle (Avant le Dépôt de votre Feuille)

Avant de remettre votre feuille aux professeurs à 12h15, vérifiez que vos deux questions respectent ces cinq critères essentiels :

- [ ] **Exactitude factuelle :** Mes questions reposent-elles sur des faits techniques avérés et documentés (rapport BEA, texte de Lin et al.) ?
- [ ] **Approche systémique :** Ai-je banni toute formulation blâmant l'inattention, la fatigue ou l'erreur de l'opérateur ?
- [ ] **Processus cognitif explicite :** Ai-je identifié le problème d'interface sous l'angle du traitement de l'information (feedback, conscience de la situation, mémoire de travail) ?
- [ ] **Formulation ouverte :** Mes questions débutent-elles par *« Comment... »* ou *« Selon quel compromis... »* et posent-elles un véritable dilemme de conception ou de méthode ?
- [ ] **Concision :** Chaque question est-elle rédigée de façon claire et succincte ?
