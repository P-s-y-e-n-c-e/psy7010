# Audit académique adverse — PSY7010
## Banque de 44 questions : rapport détaillé et textes de remplacement

**Périmètre.** Fichier téléversé `Quiz_entrainement_22sep_PSY7010.html` ; tableau JavaScript `allQuestions`. Lecture des 44 énoncés, 176 options, 176 rétroactions, métadonnées de source, explications et conseils. Le rapport distingue le contenu des cinq lectures des vérifications externes. Le site public n’a pas été modifié.

**Empreinte SHA-256 du fichier audité :** `d10661dcc049287ef297661a929cae8211f6f487ba25bacbc70ab4db04ec29b9`.

**Convention.** A = indice 0 ; B = 1 ; C = 2 ; D = 3. QXX désigne l’identifiant stable `id`, non une position dans une liste filtrée. Un défaut de source ne signifie pas automatiquement que la réponse est scientifiquement fausse. Un distracteur vrai dans un autre contexte n’est pas automatiquement une deuxième bonne réponse ; les cas retenus précisent le lien avec l’énoncé. Les modifications d’une fiche doivent être appliquées ensemble. Aucun score de discrimination, coefficient de fidélité ou taux de faux positifs n’est estimé sans réponses d’étudiants.

**Priorités.** 22 fiches rouges, 22 fiches jaunes. Les coquilles transversales sont regroupées à la fin. Ces catégories classent des défauts éditoriaux, pas la proportion de clés entièrement inversées.

## 🔴 Défauts transversaux

### T1 — Q01–Q44 : explications et conseils non affichés
Les objets contiennent `doc_explanation` et `exam_tip`. Le code lit `q.explanation` et `q.examTip` dans les deux modes. Il affiche donc une synthèse `undefined` et un conseil générique. Les rétroactions spécifiques `feedbacks` sont, elles, lues correctement. Il ne faut pas conclure que toutes les rétroactions sont absentes. Références techniques : fonctions de rendu vers les lignes 5151–5153 et 5576–5577 du HTML.

**Remplacements :** `q.explanation` → `q.doc_explanation` ; `q.examTip` → `q.exam_tip`, avec garde de chaîne vide comme dans le fichier `PSY7010_correctifs_affichage.js`.

Les guillemets sont aussi ajoutés par le rendu alors que les `doc_quote` les contiennent déjà. Remplacer l’affectation par `textContent = q.doc_quote || ''`. Une synthèse signalée comme telle ne doit pas être automatiquement encadrée de guillemets.

### T2 — Q01–Q44 : distribution des clés et indices de réponse
Décompte : A = 26 ; B = 15 ; C = 3 ; D = 0. Répondre systématiquement A donne **26/44 = 59,1 %**. Les options sont rendues dans leur ordre de stockage. Ce constat établit un indice exploitable, pas un coefficient psychométrique de validité.

**Texte de consigne proposé :** « Sélectionnez la proposition qui répond le mieux à l’énoncé, dans le cadre et les conditions explicitement indiqués. »

**Correction technique :** rééquilibrer les positions et éviter les séquences prédictibles, en permutant conjointement `options`, `feedbacks` et `correctIndex`. Réinitialiser ou remapper toute réponse sauvegardée par indice. Modifier seulement la clé créerait des erreurs de correction.

### T3 — Provenance bibliographique
Le PDF téléversé porte **IAAP Handbook of Applied Psychology**, Blackwell, 2011, et non *Oxford Handbook of Cognitive Engineering*. Il contient les pages imprimées 316–336 ; la plage 316–332 ne décrit donc pas l’ensemble du fichier. Le PDF seul n’autorise pas à certifier que la bibliographie du chapitre publié est intégrale, puisque l’extrait fourni s’arrête au milieu de l’ordre alphabétique des références.

**Libellé prudent prêt à remplacer la notice :** « Cañas, J. J., Velichkovsky, B. B., et Velichkovsky, B. M. (2011). Human Factors and Ergonomics. Chapitre 13 de l’IAAP Handbook of Applied Psychology. Blackwell. Extrait fourni : pages 316–336. »

Source : page 316, pied de page éditorial ; pages 335–336, références. Cela corrige l’identification du document, sans prétendre connaître la plage complète du chapitre publié.

### T4 — Un passage voisin n’est pas une preuve
Q08, Q13, Q16, Q18 et Q19 demandent des détails que le passage de Cañas affiché ne développe pas ; Q26 cite un passage sans rapport avec ses statistiques. Pour ces contenus, ajouter une lecture probante explicitement désignée ou remplacer l’objectif par une question fondée sur le corpus. Ne pas présenter une paraphrase, une traduction libre ou un assemblage réécrit comme un extrait « exact ».

**Texte de statut prêt à injecter :** « Complément théorique : cette notion n’est pas développée dans le passage de la lecture obligatoire affiché ici. Consulter la référence complémentaire indiquée. »

**Convention de citation :** guillemets = texte fidèle ; `[…]` = omission ; « traduction » = traduction attribuée ; « synthèse, non citation textuelle » = reformulation. Les commentaires de Human Factors 101 ne deviennent pas des citations d’Endsley, de Dekker ou de Bainbridge parce qu’ils les suivent à l’écran.

## Fiches par priorité


# 🔴 ANOMALIES CRITIQUES

## Q02 — Histoire : sélection ou conception

Clé initiale : **C** (`correctIndex: 2`). Clé des propositions : **C** avant toute permutation.

**1. Validité scientifique et corrigé.** Le mot « abandon » est trop fort. Le chapitre décrit un changement d’accent et l’impossibilité de compter sur quelques individus exceptionnels, non la disparition de la sélection ou de la formation.

**2. Étanchéité des distracteurs.** C reste la réponse visée, mais elle mélange la cause documentée avec des précisions non établies dans le passage : vitesse des avions, « cockpits rapides », radars saturés. Les distracteurs chronologiques n’autorisent pas ces ajouts.

**3. Qualité des rétroactions.** « WWI sans modifier les machines », « aucun entraînement » et Taylor comme antithèse absolue de l’ergonomie sont des généralisations historiques non démontrées par le chapitre.

**4. Citations et attributions.** Le passage des p. 316–317 appuie l’échelle des besoins et la conception tenant compte des caractéristiques humaines.

**5. Langue et rigueur.** « Cockpits rapides » attribue une vitesse au poste de pilotage. Employer les dénominations françaises des guerres plutôt que WWI/WWII dans le texte explicatif.

**Appuis :** Cañas, p. 316–317.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Selon Cañas et al., quel contexte historique a renforcé le passage d’une priorité donnée à la sélection des opérateurs à la conception de dispositifs adaptés à leurs caractéristiques ?",
  "options[2]": "La Seconde Guerre mondiale : l’ampleur des besoins et l’introduction de nouveaux équipements, notamment le radar, rendaient impraticable le recours à quelques opérateurs exceptionnels.",
  "feedbacks[0]": "Le chapitre situe les précurseurs de la discipline avant cette transition, mais attribue à la Seconde Guerre mondiale l’impulsion décisive vers la conception adaptée aux caractéristiques humaines.",
  "feedbacks[1]": "Le passage associe la Première Guerre mondiale au développement des tests de sélection et d’affectation. Il situe l’impulsion décisive vers la conception adaptée à l’humain pendant la Seconde Guerre mondiale.",
  "feedbacks[2]": "Le chapitre souligne l’ampleur des effectifs et des équipements à utiliser. Concevoir pour les caractéristiques des utilisateurs devenait indispensable ; cela ne signifie pas que la sélection et la formation ont été abandonnées.",
  "doc_explanation": "Le changement historique porte sur la priorité donnée à la conception des équipements, plutôt que sur l’espoir de trouver un petit nombre d’utilisateurs exceptionnels capables de s’accommoder de toute machine.",
  "exam_tip": "Première Guerre mondiale : essor de la sélection et de l’affectation. Seconde Guerre mondiale : impulsion décisive vers la conception adaptée aux utilisateurs. Ne pas en déduire la suppression de la sélection."
}
```

## Q06 — Goulot d’étranglement et mémoire de travail

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** L’énoncé demande un composant principal universel sans préciser la tâche ; B en nomme deux. Les pages invoquées ne démontrent pas l’existence d’un goulot unique, strictement fixe, applicable à toute activité complexe.

**2. Étanchéité des distracteurs.** Une limitation perceptive peut réellement limiter certaines tâches ; elle n’est pas exclue par le contexte générique. D enseigne aussi une capacité « illimitée » de mémoire à long terme sans preuve.

**3. Qualité des rétroactions.** La saturation n’entraîne pas nécessairement une vision en tunnel. Les « millions de données brutes » captées par les yeux n’expliquent pas la distinction testée.

**4. Citations et attributions.** La source traite du maintien et des opérations sur une quantité limitée de ressources, puis de plusieurs modèles. Elle ne formule pas l’équation attention sélective + mémoire de travail = principal bottleneck universel.

**5. Langue et rigueur.** Éviter le singulier « composant » suivi de deux construits. Employer « unités significatives » plutôt que chunks sans explication.

**Appuis :** Cañas, p. 329–330.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Un opérateur doit retenir plusieurs valeurs récemment affichées, les comparer et les actualiser mentalement, sans possibilité de les consulter à nouveau.",
  "question": "Quel système cognitif est directement sollicité par ce maintien temporaire et cette manipulation simultanée de l’information ?",
  "options": [
    "L’acuité visuelle périphérique, une fois les valeurs correctement lues.",
    "La mémoire de travail.",
    "La conduction motrice périphérique nécessaire pour appuyer sur une touche.",
    "Le stockage durable des connaissances en mémoire à long terme, indépendamment de leur maintien actif."
  ],
  "feedbacks": [
    "L’acuité participe à la perception des valeurs, mais ne désigne pas leur maintien actif après leur disparition.",
    "La mémoire de travail permet de maintenir temporairement des informations tout en les manipulant ; une tâche qui sollicite excessivement ces fonctions peut favoriser les erreurs.",
    "La conduction motrice concerne l’exécution du mouvement, non le maintien et la comparaison des valeurs.",
    "La mémoire à long terme conserve des connaissances durables ; elle ne suffit pas à décrire le maintien actif des valeurs de ce scénario."
  ],
  "doc_explanation": "La difficulté ciblée ici est le maintien et la manipulation d’informations temporaires. Cela n’implique pas que la mémoire de travail soit l’unique limite de toute activité complexe.",
  "exam_tip": "Identifier d’abord les exigences de la tâche : percevoir, maintenir, manipuler, récupérer ou agir. Ne pas postuler un goulot unique dans toutes les situations."
}
```

## Q07 — Affordances et conception écologique

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** La clé mélange les possibilités d’action, leur perception et une promesse d’absence de raisonnement abstrait. Rendre une contrainte perceptible ne garantit ni transparence totale ni action appropriée sans analyse.

**2. Étanchéité des distracteurs.** Les distracteurs sont faux relativement au concept, mais si caricaturaux qu’ils ne vérifient guère la distinction entre affordance, indice perceptif et automatisation.

**3. Qualité des rétroactions.** La poignée qui « invite » à tirer illustre aussi un problème de signalisation : toute affordance n’est pas réductible à une invitation comprise. Le corrigé surinterprète « supporting specific actions ».

**4. Citations et attributions.** Le chapitre rattache l’affordance à Gibson et la conception d’affordances à Vicente. Il ne soutient pas que les interfaces écologiques abolissent tout calcul abstrait.

**5. Langue et rigueur.** « Design » peut devenir « conception ». Supprimer « naïve » : c’est une appréciation de l’étudiant, non une explication.

**Appuis :** Cañas, p. 324.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Dans le passage consacré à Gibson, quelle idée est essentielle pour définir une affordance ?",
  "options[1]": "Une possibilité d’action offerte par l’environnement relativement aux capacités de l’individu ; la conception peut chercher à la rendre perceptible et exploitable.",
  "feedbacks[0]": "La psychologie écologique étudie les relations entre perception, action et environnement ; elle ne se définit pas par l’emploi de matériaux recyclables.",
  "feedbacks[1]": "La source insiste sur les aspects de l’environnement qui soutiennent des actions spécifiques. Il faut distinguer la possibilité d’action de la manière dont l’interface aide à la percevoir.",
  "doc_explanation": "Concevoir pour l’action consiste notamment à rendre les informations et contraintes pertinentes accessibles à l’utilisateur. Cela ne supprime pas les besoins de compréhension ou de raisonnement dans les situations complexes.",
  "exam_tip": "Affordance : possibilité d’action dans la relation individu–environnement. Ne pas la confondre avec un simple indice visuel ni avec une garantie d’action sans raisonnement."
}
```

## Q14 — Mistake : plan inadéquat, non intention nuisible

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A contient le trait visé, mais « exactement » transforme l’exécution conforme en condition nécessaire. Le défaut du plan demeure même si une erreur d’exécution s’y ajoute. L’intention peut être de réussir : elle n’est pas forcément « erronée dès le départ ».

**2. Étanchéité des distracteurs.** B ne permet pas de conclure à une violation sans règle connue et dérogation établie. C, réflexe incontrôlable, n’est pas automatiquement un slip au sens de cette taxonomie.

**3. Qualité des rétroactions.** Les rétroactions B et C imposent des classifications non déduites des informations proposées. Il faut construire des cas contenant les critères nécessaires.

**4. Citations et attributions.** La fin du doc_quote a été réécrite : « retrieval of inappropriate rules could lead to errors » n’est pas le texte fourni. Le passage se trouve p. 321, non p. 322.

**5. Langue et rigueur.** « Son intention est erronée » confond but, intention, diagnostic et plan.

**Appuis :** Cañas, p. 321.

**Intégration :** La distinction complète avec slips/lapses demeure un complément à documenter ; l’extrait fourni établit directement l’exemple d’erreur fondée sur une règle.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quel critère distingue principalement une erreur de planification ou de jugement (mistake) d’une erreur d’exécution ?",
  "options": [
    "Le plan ou le jugement est inadapté à l’objectif, même si les actions prévues sont exécutées correctement.",
    "Le plan est approprié, mais l’opérateur appuie involontairement sur un bouton différent de celui qu’il voulait sélectionner.",
    "Le plan est approprié, mais l’opérateur oublie involontairement une étape qu’il avait prévu de réaliser.",
    "Aucun jugement ni aucune action humaine n’est erroné ; seul un composant matériel tombe en panne."
  ],
  "feedbacks": [
    "Le critère est l’inadéquation du plan ou du jugement. Une erreur d’exécution peut éventuellement s’y ajouter : les catégories ne décrivent pas nécessairement des épisodes entièrement exclusifs.",
    "Cette proposition décrit une erreur d’exécution : l’action réalisée diffère de l’action voulue.",
    "Cette proposition décrit un oubli : une action prévue n’est pas réalisée en raison d’une défaillance de mémoire.",
    "Une défaillance matérielle, à elle seule, n’est pas une erreur de jugement humain."
  ],
  "doc_page": "Page 321 — Errors based on rules",
  "doc_quote": "« If a situation is misinterpreted the retrieved rule will be inappropriate as well. In other words, an error based on rules will occur. »",
  "doc_explanation": "L’opérateur peut poursuivre un objectif approprié, mais adopter un diagnostic, une règle ou un plan inadapté. Une intention de nuire n’est pas nécessaire.",
  "exam_tip": "Mistake : plan ou jugement inadapté. Slip : écart involontaire d’exécution. Lapse : oubli."
}
```

## Q15 — Violation : sous-type indéterminable

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** La dérogation délibérée est établie, mais ni sa répétition habituelle ni les contraintes rendant la conformité impossible ne le sont. « Routinière (ou situationnelle) » ne constitue donc pas une classification rigoureuse du sous-type.

**2. Étanchéité des distracteurs.** Une estimation erronée du risque peut coexister avec une violation. Le corrigé invente la connaissance parfaite des justifications physiques pour exclure B.

**3. Qualité des rétroactions.** Il faut expliquer l’axe intentionnel de la dérogation, sans prétendre qu’un même événement ne peut comporter aucun jugement erroné.

**4. Citations et attributions.** Le doc_quote assemble des passages des p. 321–322 en ordre inversé et ajoute « to which the person must adapt and react ». Ces mots ne figurent pas dans le texte fourni.

**5. Langue et rigueur.** Employer « critère discriminant », non « élément discriminatoire » ; réserver le caractère délibéré à l’écart à la règle, pas au dommage.

**Appuis :** HF101-A, Human error and human performance.

**Intégration :** Déplacer anchor_q15 et anchor_q15_fr vers le passage de l’Article A cité ici.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Un opérateur connaît la procédure obligatoire de cadenassage et choisit de ne pas l’appliquer pour gagner du temps. Comment qualifier cet écart intentionnel, indépendamment de la justesse de son estimation du risque ?",
  "options[0]": "Une violation : une dérogation délibérée à une règle connue. Les informations fournies ne suffisent pas à en préciser le sous-type.",
  "feedbacks[0]": "Le choix de ne pas suivre une règle connue établit la violation. Il faudrait des données supplémentaires sur la répétition de la pratique et les contraintes de travail pour qualifier son sous-type.",
  "feedbacks[1]": "Une mauvaise estimation du risque peut coexister avec une violation. Mais la question porte sur l’écart volontaire à une procédure connue, non sur le diagnostic technique.",
  "feedbacks[3]": "Le scénario décrit un écart intentionnel. Il ne démontre ni une exécution involontaire ni une formation insuffisante.",
  "doc_id": "doc_art_a",
  "doc_title": "Human Factors 101 — Article A : Why do people break the rules ?",
  "doc_page": "Section Human error and human performance",
  "doc_quote": "« Why do people break the rules? Did the person break the rule intentionally, or is it because they didn’t know about the rule? Perhaps the rule was unworkable in practice, or a person had competing demands on their time. »",
  "doc_explanation": "L’intention de s’écarter d’une règle connue ne signifie pas l’intention de provoquer un accident. Une violation peut coexister avec une mauvaise appréciation de la situation.",
  "exam_tip": "Critère discriminant : l’écart à la règle connue est-il voulu ? Pour le sous-type, rechercher les habitudes et les contraintes, plutôt que le déduire du seul résultat."
}
```

## Q18 — NASA-TLX : bonne liste, source absente

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B donne bien les six dimensions. Il ne faut pas corriger la clé. Le défaut critique est d’exiger comme contenu de la lecture obligatoire un instrument qui n’y est pas présenté.

**2. Étanchéité des distracteurs.** C contient cinq traits de personnalité et la capacité d’attention : dire que les six éléments sont les dimensions du Big Five est faux.

**3. Qualité des rétroactions.** Le NASA-TLX original combine six évaluations et une pondération issue de quinze comparaisons par paires. Le corrigé confond ces deux opérations. « Charge mentale » est plus étroit que la charge de travail multidimensionnelle évaluée.

**4. Citations et attributions.** Les p. 329–330 parlent de charge mentale sans présenter le TLX. Le manuel officiel NASA est la source probante supplémentaire, pas la citation sur les obligations légales.

**5. Langue et rigueur.** Employer « six sous-échelles » : ce n’est pas chaque sous-échelle qui est multidimensionnelle. Préférer « autoévaluation » à « auto-rapportée ».

**Appuis :** NASA-TLX, manuel officiel, sections 2.1–2.2 ; Cañas, p. 329–330 : ne présente pas cet instrument.

**Intégration :** Ajouter le manuel comme lecture et destination du bouton source, ou retirer cette question du sous-ensemble fondé exclusivement sur les cinq lectures. Une simple modification du doc_title ne répare pas le lien.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Lecture complémentaire : manuel du NASA Task Load Index. L’instrument n’est pas décrit dans les pages de Cañas affichées comme contexte général sur la charge de travail.",
  "question": "Quelles sont les six dimensions d’autoévaluation du NASA-TLX ?",
  "feedbacks[1]": "Les six dimensions sont les exigences mentale, physique et temporelle, la performance, l’effort et la frustration. Dans la version pondérée originale, six évaluations sont combinées avec des poids issus de quinze comparaisons par paires.",
  "feedbacks[2]": "Cette liste mélange cinq dimensions de personnalité et une capacité d’attention. Elle ne correspond pas aux six dimensions du NASA-TLX.",
  "doc_title": "NASA — Task Load Index, manuel de passation ; lecture complémentaire",
  "doc_page": "Sections Rating Scales et Sources of Load (Weights)",
  "doc_quote": "Synthèse du manuel, non citation textuelle : le NASA-TLX comporte six évaluations ; la version originale ajoute une pondération obtenue par quinze comparaisons par paires.",
  "doc_explanation": "Le NASA-TLX distingue plusieurs contributions subjectives à la charge de travail. Les évaluations des dimensions et leurs poids ne sont pas la même opération.",
  "exam_tip": "NASA-TLX : exigences mentale, physique et temporelle ; performance, effort, frustration. Distinguer les évaluations des dimensions et la pondération."
}
```

## Q19 — Mesures physiologiques : inférence non spécifique

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B transforme une association possible en signature robuste suffisante, sans préciser la métrique de variabilité cardiaque, la référence individuelle ou les conditions d’acquisition. Une dilatation pupillaire n’identifie pas à elle seule la charge mentale.

**2. Étanchéité des distracteurs.** D n’est pas une combinaison interprétable comme une alternative homogène ; la résistance électrodermale ne devient pas pertinente par ajout d’une « contraction réflexe du myocarde ». A n’est pas simplement le marqueur exclusif du repos.

**3. Qualité des rétroactions.** « Le cœur se rigidifie », « le HRV s’effondre » et une règle universelle à deux signes enseignent un diagnostic abusif. Une mesure objective n’est pas une mesure spécifique du construit.

**4. Citations et attributions.** La citation de Cañas n’énonce aucune règle HRV–pupille. Une étude expérimentale de pupillométrie vérifiée souligne notamment le contrôle de la luminance et le choix d’une référence.

**5. Langue et rigueur.** La variabilité de la fréquence cardiaque : VFC en français ; HRV peut être conservé après définition. Éviter le terme « suppression » pour une simple diminution.

**Appuis :** Cañas, p. 329–330 ; Mitre-Hernandez et al. (2021), DOI 10.2196/21620.

**Intégration :** Cette version est une question méthodologique de complément. Le chapitre fournit la réserve générale sur la mesure, mais non un protocole VFC. Ne pas conserver l’ancienne règle physiologique dans le lecteur français.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Un protocole compare une tâche de référence et une tâche plus exigeante chez les mêmes participants. Il enregistre le diamètre pupillaire et des indices de variabilité de la fréquence cardiaque.",
  "question": "Quelle interprétation méthodologique des variations physiologiques est la plus rigoureuse ?",
  "options": [
    "Toute dilatation pupillaire permet d’attribuer sans autre contrôle la variation observée à la charge mentale.",
    "Ces variations peuvent contribuer à l’évaluation de l’effort, mais leur interprétation exige des références et des contrôles adaptés ; elles ne constituent pas à elles seules un diagnostic spécifique de surcharge.",
    "Le caractère objectif de l’enregistrement suffit à démontrer que la mesure est spécifique de la charge mentale.",
    "Une variation physiologique permet de déduire directement quelle règle de travail a été mal comprise."
  ],
  "feedbacks": [
    "La luminance et d’autres facteurs peuvent modifier la pupille ; l’attribution à la seule charge mentale exige des contrôles.",
    "Il faut distinguer sensibilité à une manipulation et spécificité pour un construit. Le protocole, la référence, les facteurs de confusion et la convergence avec d’autres observations conditionnent l’interprétation.",
    "L’objectivité décrit le mode d’enregistrement, non l’exclusivité de la relation entre un signal et le construit étudié.",
    "Un signal physiologique ne permet pas, à lui seul, d’identifier le contenu d’un jugement ou la règle sélectionnée."
  ],
  "doc_explanation": "La mesure d’un signal corporel ne dispense pas d’un raisonnement de validité de construit. Éviter toute équivalence universelle entre un profil physiologique et une surcharge cognitive.",
  "exam_tip": "Mesure objective ≠ indicateur spécifique. Interpréter les variations dans un protocole contrôlé et rechercher la convergence des indices."
}
```

## Q20 — Wickens : partage des ressources et interférence

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A affirme que l’interférence survient uniquement pour des ressources communes ; le conseil promet aucune interférence si les réservoirs diffèrent. Ce raccourci doit rester une simplification de modèle, non une loi garantissant la sécurité de tâches réelles.

**2. Étanchéité des distracteurs.** Comparer des modalités différentes ne garantit pas l’absence de ressources centrales communes ou de coûts de coordination. Les distracteurs doivent être évalués dans les conditions du modèle explicitées.

**3. Qualité des rétroactions.** Qualifier un modèle à ressource unique de « réfuté » sans discussion et déclarer conduite + podcast inoffensifs sur la base de canaux différents dépasse la démonstration.

**4. Citations et attributions.** Important : le chapitre lui-même donne une présentation très forte de l’indépendance entre réservoirs. La faiblesse est ici la généralisation non qualifiée et son application concrète, pas une citation nécessairement infidèle.

**5. Langue et rigueur.** Remplacer les images de conduite « détruite » par des effets probables sur la performance.

**Appuis :** Cañas, p. 330.

**Intégration :** Nuance de portée scientifique : signaler que la correction distingue la présentation simplifiée du chapitre d’une inférence universelle sur des activités réelles.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Selon le modèle des ressources multiples présenté par Cañas et al., quelle configuration fait prévoir davantage d’interférence entre deux tâches réalisées simultanément, toutes choses pertinentes égales par ailleurs ?",
  "options[0]": "Les deux tâches sollicitent fortement les mêmes ressources de traitement plutôt que des ressources davantage distinctes.",
  "feedbacks[0]": "Le partage de ressources augmente la compétition entre les tâches. Des ressources davantage distinctes peuvent réduire cette compétition ; elles ne garantissent pas l’absence de tout coût en situation réelle.",
  "feedbacks[1]": "Cette proposition ne rend pas compte de l’idée centrale de ressources multiples : l’interférence dépend aussi du recouvrement entre les exigences de traitement, et pas seulement d’une quantité globale d’effort.",
  "doc_explanation": "Le modèle guide la comparaison des exigences de traitement. Pour une activité réelle, il faut aussi examiner les ressources communes restantes, la difficulté des tâches et leur coordination ; la seule différence de modalité sensorielle ne prouve pas l’absence d’interférence.",
  "exam_tip": "Davantage de ressources communes : davantage de compétition attendue. Ressources plus distinctes : interférence potentiellement réduite, non garantie nulle."
}
```

## Q22 — Simulation et stress émotionnel

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** La difficulté de reproduire le stress est étayée. Le corrigé la transforme en impossibilité et oppose toute simulation « froide » à toute situation réelle « chaude ». L’absence de danger vital n’implique pas l’absence de stress.

**2. Étanchéité des distracteurs.** Les distracteurs sont extrêmes. Leur réfutation ne justifie ni un réalisme sensoriel presque parfait de tous les simulateurs ni une obligation universelle de simulation en formation.

**3. Qualité des rétroactions.** Le feedback B et l’explication doivent parler de fidélité psychologique et de conditions de transfert, sans garantir un type unique d’état affectif.

**4. Citations et attributions.** « Although simulation is an expensive and time-consuming methodology » ne figure pas dans le texte fourni. La phrase réellement probante est p. 333 et manque au doc_quote.

**5. Langue et rigueur.** « Inimitable », « bardés de capteurs » et « obligatoire dans toutes » manquent de portée définie.

**Appuis :** Cañas, p. 332–333.

**Intégration :** Replacer l’ancre Q22 sur la phrase de la page 333, pas seulement sur le titre « Simulation ».

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quelle difficulté de validité écologique des simulations Cañas et al. soulignent-ils à la page 333 ?",
  "options[1]": "Il peut être difficile de reproduire le stress émotionnel et les enjeux vécus dans la situation réelle, même avec une simulation techniquement fidèle.",
  "feedbacks[0]": "Le problème souligné n’est pas une impossibilité générale de reproduire des graphismes ou des sons, mais la fidélité des conditions psychologiques.",
  "feedbacks[1]": "Une simulation peut susciter du stress, mais son intensité, sa nature et ses enjeux peuvent différer de ceux d’une situation réelle. La source parle de difficulté de reproduction, non d’impossibilité absolue.",
  "feedbacks[2]": "Le chapitre décrit explicitement des usages de simulation pour la formation et l’expérimentation ; il ne présente pas l’interdiction générale proposée.",
  "feedbacks[3]": "Le chapitre mentionne l’enregistrement de variables dépendantes, notamment les temps de réaction. Les mesures disponibles dépendent de l’équipement du simulateur.",
  "doc_quote": "« The fundamental problem with simulators is that it is not easy to reproduce the emotional stress of real situations. »",
  "doc_page": "Page 333 — Simulation of the situation",
  "doc_explanation": "La fidélité technique ne garantit pas l’équivalence des états émotionnels ni le transfert de la performance. Ces dimensions doivent être examinées empiriquement.",
  "exam_tip": "Simulation : contrôler les conditions tout en vérifiant la fidélité psychologique, notamment celle du stress émotionnel."
}
```

## Q23 — Endsley : niveaux, pas chronologie obligatoire

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** « Chronologiquement » contredit directement le doc_quote : la progression n’a pas à être linéaire ni séquentielle. A nomme les trois niveaux, mais ne peut valider une chronologie obligatoire.

**2. Étanchéité des distracteurs.** Les trois distracteurs sont des assemblages étrangers au modèle. Les qualifier de modèles inversés ou réflexes constitués leur accorde une cohérence qu’ils n’ont pas.

**3. Qualité des rétroactions.** La rétroaction correcte doit expliquer la distinction fonctionnelle et les boucles d’actualisation, plutôt qu’une cascade irréversible.

**4. Citations et attributions.** La source D affirme expressément la non-linéarité ; le chapitre p. 325 nomme les trois niveaux. La partie sur les modèles mentaux provient d’un autre passage et ne doit pas être accolée comme une suite.

**5. Langue et rigueur.** « Définition canonique absolue » masque l’ambiguïté introduite par le mot chronologiquement.

**Appuis :** HF101-D, passage sur la progression non linéaire ; Cañas, p. 325.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quels sont les trois niveaux de contenu de la conscience de la situation distingués dans le modèle d’Endsley, sans supposer une progression temporelle obligatoirement linéaire ?",
  "options[0]": "Niveau 1 : perception des éléments pertinents ; niveau 2 : compréhension de leur signification ; niveau 3 : projection de leur évolution future.",
  "feedbacks[0]": "Ces niveaux distinguent ce qui est perçu, compris et anticipé. Leur acquisition et leur actualisation sont itératives : la compréhension et les attentes peuvent orienter la recherche de nouvelles informations.",
  "feedbacks[1]": "Cette liste décrit des activités hétérogènes et ne correspond pas aux niveaux perception, compréhension et projection.",
  "feedbacks[2]": "Cette liste mélange des mécanismes neurophysiologiques et une décision ; ce n’est pas la définition des trois niveaux.",
  "feedbacks[3]": "Les modèles mentaux et les échanges peuvent contribuer à l’évaluation de la situation, mais cette liste n’est pas celle des trois niveaux de connaissance.",
  "doc_quote": "« Note that it is not necessary to progress through the three stages (Perception, Understanding and Prediction) in a linear or sequential fashion. »",
  "doc_explanation": "Une hiérarchie de contenus ne doit pas être confondue avec une succession chronologique rigide. L’information antérieure, les attentes et les nouvelles observations se combinent dans une actualisation continue.",
  "exam_tip": "Perception, compréhension, projection : distinguer les niveaux sans imposer une chaîne temporelle à sens unique."
}
```

## Q25 — Niveau 2 : modèle erroné et confirmation

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B est pertinente, mais un modèle erroné ne démontre pas à lui seul un biais de confirmation. Ce dernier suppose une sélection ou interprétation favorisant l’hypothèse préalable.

**2. Étanchéité des distracteurs.** D n’assure pas la justesse de la compréhension : on peut suivre scrupuleusement une liste inadéquate. Il ne décrit pas directement N2, mais le feedback le rejette avec une garantie injustifiée.

**3. Qualité des rétroactions.** « Toutes les pièces du puzzle » et « biais de confirmation » sont ajoutés au scénario. Une liste ne garantit pas un bon diagnostic.

**4. Citations et attributions.** Le libellé attribué à D est inventé : le texte dit Understanding information et non Interpreting information: data was observed, but not understood. L’exemple de Three Mile Island est extérieur au texte D ; Macondo y est effectivement décrit.

**5. Langue et rigueur.** Préférer « intégration et interprétation » à « il plaque un schéma », et conserver un exemple documenté.

**Appuis :** HF101-D, Understanding information ; cas Macondo.

**Intégration :** Aligner anchor_q25 et sa version française sur Understanding information ; ne pas rechercher la formulation inventée.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[3]": "L’intégration correcte des informations pertinentes dans une compréhension adéquate de la situation actuelle.",
  "feedbacks[1]": "Les données sont perçues, mais interprétées à partir d’un modèle inadapté. Un biais de confirmation peut contribuer à ce mécanisme, sans être démontré par la seule présence d’un modèle erroné.",
  "feedbacks[3]": "Cette proposition décrit une compréhension adéquate, et non une défaillance de niveau 2.",
  "doc_quote": "« Understanding information: use of an incorrect or incomplete mental model, perhaps due to a lack of experience or knowledge, or a cognitive bias, such as confirmation bias. »",
  "doc_explanation": "Dans le cas de Macondo décrit par l’Article D, les attentes relatives au test de pression négative ont influencé l’interprétation de la situation. L’exemple permet de distinguer les données disponibles, le modèle mobilisé et les biais possibles.",
  "anchor_phrase": "Understanding information"
}
```

## Q26 — Statistiques : mauvaise étude et mauvais dénominateur

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** La catégorie dominante est bien N1, mais B généralise à toutes les défaillances et les réduit aux données disponibles non perçues. L’étude vérifiée inclut aussi données indisponibles, discrimination, mauvaise perception et oubli.

**2. Étanchéité des distracteurs.** Les alternatives numériques ne corrigent pas cette erreur de dénominateur. Le feedback A donne environ 10 % pour N3 alors que l’étude citée correctement donne 3,4 %.

**3. Qualité des rétroactions.** Apprendre un pourcentage comme vérité universelle sans préciser échantillon, méthode et catégories est une erreur pédagogique.

**4. Citations et attributions.** Les données proviennent de Jones et Endsley (1996), à partir de rapports ASRS ; ni Endsley (1995) seul ni le passage Team SA/Macondo de D ne soutiennent cette statistique.

**5. Langue et rigueur.** « Proportion écrasante » et « chiffre capital » favorisent la mémorisation non critique.

**Appuis :** Jones & Endsley (1996), PMID 8827130 ; HF101-D : aucune statistique de ce type dans le passage invoqué.

**Intégration :** Ajouter l’étude comme lecture complémentaire et changer la destination source. Variante strictement limitée aux cinq lectures : remplacer cette question par Team SA versus Shared SA, avec le passage D correspondant.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Complément externe : Jones et Endsley (1996) ont classé des erreurs de conscience de la situation à partir de rapports de l’Aviation Safety Reporting System (ASRS).",
  "question": "Quelle catégorie représentait 76,3 % des erreurs de conscience de la situation identifiées dans cette étude ?",
  "options": [
    "Les erreurs de niveau 3 : projection de l’évolution future.",
    "Les erreurs de niveau 1 : perception de l’information pertinente.",
    "Les erreurs de niveau 2 : compréhension de la situation.",
    "Les violations délibérées, considérées comme un quatrième niveau de conscience de la situation."
  ],
  "feedbacks": [
    "Les erreurs de niveau 3 représentaient 3,4 % des erreurs identifiées.",
    "Le niveau 1 représentait 76,3 %. Cette catégorie ne se limitait pas aux informations disponibles non observées ; elle incluait notamment l’indisponibilité de données et des pertes de mémoire.",
    "Les erreurs de niveau 2 représentaient 20,3 % des erreurs identifiées.",
    "La classification utilisait trois niveaux de conscience de la situation ; la violation n’y constitue pas un quatrième niveau."
  ],
  "doc_title": "Jones, D. G., et Endsley, M. R. (1996) — Sources of situation awareness errors in aviation",
  "doc_page": "Aviation, Space, and Environmental Medicine, 67(6), 507–512 ; résumé",
  "doc_quote": "Synthèse, non citation textuelle : dans les rapports ASRS analysés, les erreurs identifiées se répartissaient entre le niveau 1 (76,3 %), le niveau 2 (20,3 %) et le niveau 3 (3,4 %).",
  "doc_explanation": "Ces proportions décrivent les erreurs identifiées dans les rapports étudiés. Elles ne sont pas un taux universel de tous les accidents ou de toutes les erreurs de conscience de la situation.",
  "exam_tip": "Toujours associer les pourcentages à leur étude, à leur population et à leur dénominateur ; ne pas confondre toutes les erreurs N1 avec la non-observation de données disponibles.",
  "tag": "Jones et Endsley (1996) — Répartition des erreurs de conscience de la situation dans des rapports ASRS"
}
```

## Q27 — Haynes : citation reconstruite, causalité et pourcentages

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A amalgame deux issues et laisse entendre une démonstration causale. Les taux 1,5 → 0,8 et 11 → 7 impliquent environ 46,7 % et 36,4 % de baisse relative, calculés sur les valeurs arrondies, non un pourcentage identique.

**2. Étanchéité des distracteurs.** C affirme davantage d’erreurs chez les chirurgiens expérimentés : les résultats agrégés ne testent pas cette proposition de sous-groupe. Une rétroaction doit dire qu’elle n’est pas démontrée, pas la traiter comme scientifiquement impossible.

**3. Qualité des rétroactions.** « A prouvé », « 90 secondes » et « mandarins » sont à retirer. Le plan avant–après ne démontre pas à lui seul un mécanisme causal exclusif de communication ou de conscience partagée.

**4. Citations et attributions.** Le doc_quote commençant par In another study est absent du PDF. Le passage réel est p. 326 et dit nearly 40% pour la mortalité ; il faut conserver cette approximation comme celle du chapitre et la distinguer des données primaires.

**5. Langue et rigueur.** Employer « mortalité postopératoire », « points de pourcentage » et « association ». Éviter les qualificatifs spectaculaire/colossal et l’attaque contre les chirurgiens.

**Appuis :** Cañas, p. 326 ; Haynes et al. (2009), DOI 10.1056/NEJMsa0810119 ; PMID 19144931.

**Intégration :** Replacer l’ancre Q27 sur le passage p. 326. Ajouter la référence primaire, sans modifier silencieusement la citation du chapitre pour lui faire dire les données primaires.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Cañas et al. évoquent l’étude de Haynes et al. à la page 326. La publication primaire de 2009 rapporte une comparaison avant–après dans huit hôpitaux.",
  "question": "Quelle conclusion respecte les résultats et les limites du plan d’étude de Haynes et al. (2009) ?",
  "options": [
    "La mise en œuvre de la liste de vérification a été associée à une diminution des taux observés de mortalité et de complications ; le plan avant–après ne démontre pas à lui seul une causalité exclusive.",
    "La mortalité observée a augmenté après la mise en œuvre.",
    "Le protocole a réparti aléatoirement chaque patient entre utilisation et absence de liste.",
    "Les résultats démontrent que tout chirurgien expérimenté commet davantage d’erreurs avec une liste."
  ],
  "feedbacks": [
    "Le résultat est une association avant–après, compatible avec un bénéfice mais ne permettant pas d’isoler à lui seul tous les facteurs causaux.",
    "Le taux rapporté diminue, il n’augmente pas.",
    "L’étude compare des périodes avant et après la mise en œuvre ; il ne s’agit pas d’une randomisation individuelle.",
    "Une conclusion sur tous les chirurgiens expérimentés ne se déduit pas des résultats agrégés."
  ],
  "doc_title": "Cañas et al. (2011), p. 326 ; vérification externe : Haynes et al. (2009)",
  "doc_page": "Cañas : page 326 ; Haynes : NEJM, 360, 491–499",
  "doc_quote": "« For example, a recent WHO-funded study has shown that the rate of postoperative mortality in a number of hospitals across the world could be reduced by nearly 40% [...] »",
  "doc_explanation": "Le chapitre donne une approximation. L’étude primaire rapporte une mortalité de 1,5 % puis 0,8 %, et des complications de 11 % puis 7 %. Ne pas confondre baisse relative, baisse en points de pourcentage et preuve causale.",
  "exam_tip": "Distinguer la formulation du chapitre des données primaires, puis le résultat observé du mécanisme causal supposé."
}
```

## Q29 — Ironie du concepteur : distracteurs inclus dans la bonne réponse

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A décrit l’idée générale, mais affirme que l’ingénieur injecte nécessairement des erreurs qui attendent forcément un scénario imprévu. La source emploie may.

**2. Étanchéité des distracteurs.** B et D décrivent précisément des erreurs de conception humaines susceptibles de produire des difficultés d’utilisation. Elles sont des cas particuliers compatibles avec le mécanisme de A, même si A en donne la formulation la plus générale.

**3. Qualité des rétroactions.** Le feedback D nie à tort le rapport entre une mauvaise hypothèse sur les utilisateurs et l’ironie du concepteur. L’erreur ne se conserve pas comme une quantité simplement déplacée par l’automatisation.

**4. Citations et attributions.** Le texte cité est celui de l’Article E. Le titre numéroté Irony 1 est sa structuration pédagogique, pas le titre d’une section de Bainbridge reproduite mot pour mot.

**5. Langue et rigueur.** Supprimer le ne dans « jusqu’à ce qu’un scénario […] ne survienne » et préférer « peut introduire ».

**Appuis :** HF101-E, Irony 1: Designers are human too!.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quelle formulation générale exprime l’ironie du concepteur décrite dans l’Article E à partir des travaux de Bainbridge ?",
  "options": [
    "Une automatisation conçue pour réduire certaines erreurs d’exploitation peut introduire des erreurs de conception humaines, qui influenceront ensuite le fonctionnement du système.",
    "Une erreur d’exploitation commise après la mise en service provient nécessairement de l’opérateur et ne peut avoir de lien avec la conception.",
    "Les concepteurs cessent d’être une source possible d’erreur dès que les opérations sont exécutées automatiquement.",
    "Automatiser une fonction garantit que les hypothèses faites sur les utilisateurs sont exactes."
  ],
  "feedbacks": [
    "La source souligne une source d’erreur humaine qui subsiste en amont : la conception. Elle ne dit pas que tout projet introduit nécessairement des erreurs ni que l’automatisation ne réduit jamais le risque.",
    "Des choix de conception peuvent contribuer aux difficultés rencontrées en exploitation ; exclure ce lien contredit le mécanisme étudié.",
    "Les décisions de conception restent humaines et faillibles, même lorsque l’exécution est automatisée.",
    "L’automatisation ne valide pas à elle seule les hypothèses concernant les connaissances et capacités des utilisateurs."
  ],
  "doc_explanation": "Réduire certaines occasions d’erreur à l’exploitation ne supprime pas les erreurs possibles de spécification et de conception. Il faut analyser ces contributions sans postuler un simple transfert à quantité de risque constante.",
  "exam_tip": "Les concepteurs sont eux aussi humains : examiner les hypothèses et choix de conception, pas seulement les actes de première ligne."
}
```

## Q31 — Out-of-the-loop, attribution et vocabulaire AF447

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A décrit un mécanisme possible, mais la supervision n’est pas nécessairement une sous-charge. Il faut distinguer manque de pratique, perte d’information, coûts de réorientation et charge de supervision.

**2. Étanchéité des distracteurs.** La crainte de sanctions peut influencer une intervention ; elle n’est simplement pas le mécanisme cognitif caractéristique demandé. Dire qu’elle ne peut pas contribuer à un délai serait abusif.

**3. Qualité des rétroactions.** Le feedback D remplace un absolu par l’absolu inverse. Les compétences et la représentation peuvent être dégradées, non forcément absentes.

**4. Citations et attributions.** La référence canonique vérifiée est Endsley et Kiris (1995), pas Endsley et Kirwan. L’Article E distingue désactivation du pilote automatique et décrochage aérodynamique ultérieur.

**5. Langue et rigueur.** Un pilote automatique se désengage ; l’avion peut décrocher. « Décrochage de l’autopilote » confond deux événements.

**Appuis :** HF101-E, Irony 3 et exemple AF447 ; Endsley & Kiris (1995), DOI 10.1518/001872095779064555.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Après une période de conduite automatisée, un opérateur peut devoir reprendre rapidement le contrôle. L’Article E décrit ce problème ; l’étude complémentaire de référence est celle d’Endsley et Kiris (1995).",
  "feedbacks[0]": "Une participation réduite peut compromettre la pratique et l’actualisation de la représentation du système. La reprise demande alors de reconstituer la situation et de mobiliser des compétences éventuellement moins exercées.",
  "feedbacks[2]": "Des facteurs organisationnels peuvent contribuer à un délai d’intervention, mais ils ne définissent pas à eux seuls le mécanisme cognitif de sortie de la boucle visé ici.",
  "feedbacks[3]": "La surveillance automatisée n’est pas toujours plus chargée, ni toujours moins chargée. La difficulté dépend notamment des exigences de supervision et du passage à la reprise de contrôle.",
  "doc_explanation": "La reprise peut être difficile lorsque l’opérateur manque d’information actualisée ou de pratique. Dans l’exemple AF447 rapporté par l’Article E, il faut distinguer le désengagement du pilote automatique du décrochage aérodynamique de l’avion.",
  "exam_tip": "Out-of-the-loop : examiner l’information, la pratique et le temps de réorientation. Référence complémentaire : Endsley et Kiris (1995), non Kirwan.",
  "options[0]": "Une participation réduite peut laisser l’opérateur avec une représentation moins actualisée du système ; la reprise exige alors du temps pour comprendre la situation et intervenir."
}
```

## Q32 — Surconfiance, vigilance et automatisation

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A identifie une confiance excessive, mais le corrigé réduit la complaisance à une attitude personnelle et oppose artificiellement celle-ci à un mécanisme biologique. Les effets dépendent aussi de la tâche, de la fiabilité et de l’allocation d’attention.

**2. Étanchéité des distracteurs.** Le distracteur invoquant une chute universelle après 20–30 minutes n’est pas à valider comme définition scientifique de la vigilance. L’existence d’un temps-seuil fixe n’est pas établie par les cinq lectures.

**3. Qualité des rétroactions.** Il faut distinguer confiance mal calibrée et évolution de la performance de surveillance, tout en admettant leur interaction.

**4. Citations et attributions.** Parasuraman et Manzey (2010) constituent une référence supplémentaire, pas un article cité textuellement dans l’Article E. Les fonctions Tesla décrites par E sont explicitement non autonomes et situées en mai 2020.

**5. Langue et rigueur.** Remplacer « véhicules autonomes » par « systèmes d’aide à la conduite décrits dans l’article de 2020 » et définir complaisance plutôt que la traiter comme faute morale.

**Appuis :** HF101-E, Irony 3 et Tesla Autopilot, description située en mai 2020 ; Parasuraman & Manzey (2010), DOI 10.1177/0018720810376055.

**Intégration :** Vérifier aussi les chaînes context/tag conservées : ne pas attribuer au texte E des auteurs qu’il ne cite pas. Ne pas actualiser silencieusement les caractéristiques commerciales de Tesla.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "L’Article E, publié en 2020, décrit notamment les risques de surconfiance dans des aides à la conduite qui exigent encore une supervision humaine.",
  "feedbacks[0]": "Une confiance excessive par rapport aux capacités réelles de l’automatisation peut conduire à une surveillance insuffisante. L’analyse doit aussi considérer la tâche, la conception et l’organisation de la supervision.",
  "feedbacks[3]": "La vigilance peut se dégrader au cours d’une surveillance prolongée, mais aucun seuil universel de 20 à 30 minutes n’est établi ici. Ce phénomène ne doit pas être confondu avec une confiance excessive dans le système.",
  "doc_explanation": "La confiance doit être ajustée aux capacités et limites de l’automatisation. Les difficultés de supervision ne se réduisent pas à un défaut de motivation : elles dépendent aussi des exigences de tâche et de la conception.",
  "exam_tip": "Surconfiance : confiance supérieure aux capacités réelles du système. Vigilance : maintien de la détection au cours du temps. Ces dimensions peuvent interagir.",
  "options[0]": "Une confiance excessive par rapport aux capacités réelles du système peut conduire à réduire les vérifications et à détecter tardivement une défaillance.",
  "feedbacks[1]": "Une méfiance excessive peut conduire à une sous-utilisation de l’automatisation ; cela ne correspond pas à la confiance excessive visée par cette question.",
  "feedbacks[2]": "Une réaction de panique dans une avalanche d’alarmes ne suffit pas à établir une confiance excessive dans l’automatisation."
}
```

## Q34 — Rationalité locale et caricature de Safety-I

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A exprime la reconstitution du point de vue de l’acteur, non la preuve que son choix était objectivement optimal. Il ne faut pas universaliser les bonnes intentions.

**2. Étanchéité des distracteurs.** C est inadéquate parce qu’elle réduit l’explication à la mesure de non-conformité et à la sanction ; cette réduction n’est pas une définition de Safety-I.

**3. Qualité des rétroactions.** « Safety-I = approche juridico-bureaucratique incapable de comprendre » est une erreur théorique. Safety-I se définit par la réduction des événements indésirables et peut inclure des analyses systémiques et des barrières.

**4. Citations et attributions.** L’Article C décrit la compréhension du contexte. Il ne fournit pas la caricature de Safety-I ; Hollnagel définit explicitement Safety-I et Safety-II autrement.

**5. Langue et rigueur.** Remplacer « personne ne décide délibérément » par une formulation portant sur le cas étudié. Éviter « bannir » le biais comme s’il pouvait être supprimé par injonction.

**Appuis :** HF101-C, Incident investigations ; Hollnagel, Safety-I and Safety-II (2014), page de l’auteur.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[0]": "Reconstituer les informations, objectifs et contraintes de l’acteur permet de comprendre pourquoi le choix lui paraissait approprié. Comprendre cette logique ne prouve ni l’optimalité du choix ni l’absence de responsabilité.",
  "feedbacks[2]": "Mesurer un écart à la règle ne suffit pas à expliquer sa genèse. Cette réduction à la non-conformité ne doit pas être confondue avec Safety-I, qui vise la prévention des événements indésirables et peut intégrer une analyse systémique.",
  "doc_explanation": "L’enquête cherche à reconstruire la situation accessible à l’acteur, sans lui attribuer les informations acquises après l’événement. Compréhension du comportement et appréciation normative sont deux questions distinctes.",
  "doc_quote": "« Incident investigations should aim to identify the reasons for behaviours – examining the “context” that helps to explain why people performed in a certain way. »",
  "options[0]": "En reconstituant les informations, objectifs et contraintes accessibles à l’opérateur au moment de l’action, afin de comprendre pourquoi son choix lui paraissait approprié."
}
```

## Q35 — Travail imaginé, prescrit et réalisé

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A assimile travail imaginé à procédure officielle et qualifie toutes les adaptations d’indispensables à la réussite. Le prescrit n’épuise pas les représentations du travail, et une adaptation n’est pas sûre par définition.

**2. Étanchéité des distracteurs.** B est fausse comme condamnation générale du travail réel ; elle ne devient pas fausse parce que toute conformité serait impossible ou nuisible.

**3. Qualité des rétroactions.** « À 100 %, le système s’arrêterait net » et « plus réglementé, plus de contournements » ne sont pas établis. La confusion avec Safety-I se répète.

**4. Citations et attributions.** C parle de work as performed, de planification et de résultats habituellement réussis. Il n’établit ni identité WAI/prescrit ni loi de paralysie.

**5. Langue et rigueur.** Le tag Travail Prescrit vs Travail Réel (WAI vs WAD) mélange deux distinctions. Il faut les nommer séparément.

**Appuis :** HF101-C, Principle 3 ; Shorrock (2016), The Varieties of Human Work, sections Work-as-Imagined et Work-as-Prescribed ; clarification externe vérifiée.

**Intégration :** La distinction terminologique détaillée doit être présentée comme clarification complémentaire ; la source C fournit le contraste planification/réalisation, non toutes ces définitions techniques.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "tag": "Travail imaginé, travail prescrit et travail réalisé",
  "options[0]": "Le travail imaginé correspond aux représentations de la manière dont le travail se déroule ; le travail prescrit en formalise certaines attentes ; le travail réalisé est l’activité effectivement accomplie en situation.",
  "feedbacks[0]": "Les représentations et prescriptions ne décrivent pas entièrement l’activité située. Les adaptations observées peuvent soutenir la réussite ou introduire des risques : leurs effets doivent être examinés.",
  "feedbacks[1]": "Le travail réalisé ne se réduit pas à une indiscipline. Il faut analyser les écarts, leurs raisons et leurs effets, sans présumer que toute conformité ou toute adaptation est bénéfique.",
  "feedbacks[3]": "Des écarts entre représentation, prescription et activité peuvent exister dans des organisations de tailles et de niveaux de formalisation différents ; la source ne pose pas de relation monotone avec le nombre de règles.",
  "doc_explanation": "La distinction entre travail imaginé et réalisé concerne l’écart entre représentation et activité. La prescription formelle n’est qu’une forme particulière de représentation et d’organisation du travail.",
  "doc_quote": "« Due to these adaptations, “work as performed” may be quite different from how the work was planned. Despite this, the resilience and resourcefulness of people usually ensures that the work still gets done successfully. »",
  "exam_tip": "Imaginé : représentations. Prescrit : attentes formalisées. Réalisé : activité effective. Adaptation ne signifie pas automatiquement sécurité."
}
```

## Q36 — ETTO : aucune loi universelle de paralysie

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** La question impose une conséquence « inévitable » et A répond « paralysie totale ». Aucun des quatre choix n’est rigoureusement correct sous cette formulation générale.

**2. Étanchéité des distracteurs.** B et C promettent une maximisation sans coût ; D invente une causalité immédiate. Leur faiblesse ne rend pas A vraie.

**3. Qualité des rétroactions.** Le corrigé transforme un arbitrage ressources/exigences en nécessité de sacrifier la sécurité et en preuve que la conformité bloque toujours l’activité.

**4. Citations et attributions.** Le passage C traite des compromis entre objectifs. Il ne nomme pas ETTO et ne démontre pas une paralysie générale. La présentation de Hollnagel articule préparation, exécution, ressources et priorités.

**5. Langue et rigueur.** Pour distinguer performance atteinte et économie de ressources, préférer « efficience–minutie » à « efficacité–minutie ».

**Appuis :** HF101-C, Principle 4 ; Hollnagel, The ETTO Principle (2009), présentation de l’auteur.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "L’Article C traite des compromis entre objectifs. Le principe ETTO de Hollnagel constitue ici un rapprochement théorique complémentaire.",
  "question": "Lorsque le temps et les ressources sont limités, quel arbitrage le principe ETTO aide-t-il à analyser ?",
  "options": [
    "Accroître les vérifications et la préparation peut demander davantage de temps ou de ressources ; privilégier le débit peut conduire à réduire certaines vérifications.",
    "La minutie maximale garantit toujours une cadence maximale sans ressource supplémentaire.",
    "Toute application conforme d’une procédure entraîne nécessairement l’arrêt total du système.",
    "Tout compromis entre objectifs constitue nécessairement une violation délibérée."
  ],
  "feedbacks": [
    "Le principe porte sur l’arbitrage entre les ressources consacrées à la préparation, à la vérification et à l’exécution. Il ne démontre pas une paralysie universelle liée au respect des règles.",
    "Cette proposition nie le coût en ressources que l’arbitrage cherche à décrire.",
    "Une telle nécessité ne découle pas du principe : les effets dépendent des règles, du contexte et des ressources.",
    "Un arbitrage n’est pas nécessairement une dérogation à une règle ; il peut avoir lieu dans les marges prévues par l’organisation."
  ],
  "doc_explanation": "Le principe ETTO éclaire les arbitrages entre efficience et minutie sous contraintes. Décrire ces arbitrages ne revient pas à recommander le contournement des barrières critiques.",
  "exam_tip": "ETTO : arbitrage entre efficience et minutie. Ne pas convertir ce principe en loi selon laquelle conformité = paralysie.",
  "tag": "Compromis entre objectifs — rapprochement avec le principe ETTO (efficience–minutie)"
}
```

## Q37 — Culture : probabilité, pas destin collectif

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A transforme une influence en devenir nécessaire de la norme du groupe. Le texte dit que les comportements sûrs deviennent moins probables, pas que tous les groupes adoptent nécessairement la déviance.

**2. Étanchéité des distracteurs.** B, C et D sont des absolus. Le meilleur distracteur ne doit pas être celui qui est seulement un peu moins absolu.

**3. Qualité des rétroactions.** « Aligné mot à mot » est faux pour la clé française et « les actes priment toujours » n’est pas établi. Le contraste culture affichée/climat doit être défini avant de devenir une explication.

**4. Citations et attributions.** La citation remplace production goals par production targets et supprime justement then safe behaviour will be less likely, le qualificatif crucial.

**5. Langue et rigueur.** Modèlent peut être remplacé par « influencent ». Conserver les modalisateurs de la source.

**Appuis :** HF101-C, Principle 5.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[0]": "Les comportements observés des superviseurs influencent les priorités : tolérer des pratiques dangereuses pour atteindre les objectifs de production peut rendre les comportements sûrs moins probables.",
  "feedbacks[0]": "La source décrit une influence sur la probabilité des comportements. Les actes des superviseurs comptent, mais ils ne déterminent pas à eux seuls tous les choix des membres de l’équipe.",
  "doc_quote": "« For example, if supervisors appear to condone unsafe behaviour in order to achieve production goals, then safe behaviour will be less likely. »",
  "doc_explanation": "La culture et les pratiques managériales contribuent au contexte de décision avec les collègues, la technologie et l’environnement. Elles ne constituent pas une cause unique et déterministe.",
  "exam_tip": "Respecter la portée probabiliste : influence et probabilité accrue ou réduite, non comportement inévitable de tous les membres."
}
```

## Q39 — Décision naturaliste : portée de la critique

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** La formulation condamne globalement des modèles formels comme inapplicables et trompeurs. Le chapitre dit que certains résultats de tâches décontextualisées se transfèrent mal et que certaines formations algorithmiques peuvent induire en erreur sous forte contrainte.

**2. Étanchéité des distracteurs.** Le manque de temps pour comparer exhaustivement des alternatives ne signifie pas qu’un expert ne considère jamais plusieurs possibilités ou que toute décision d’urgence est évidente.

**3. Qualité des rétroactions.** La reconnaissance d’une situation familière, la construction d’alternatives et leur évaluation en contexte ne se réduisent pas au déclenchement instantané d’une réponse.

**4. Citations et attributions.** Le texte p. 328 utilise notamment can be rather misleading ; préserver cette modalité. Ne pas attribuer à toute la décision naturaliste un unique mécanisme de reconnaissance.

**5. Langue et rigueur.** Remplacer « inapplicables » par une formulation de limites de généralisation.

**Appuis :** Cañas, p. 327–328.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Pourquoi Cañas et al. mettent-ils en garde contre la généralisation de certaines tâches de décision décontextualisées à la gestion d’incidents critiques ?",
  "options[0]": "Les professionnels doivent souvent interpréter une situation changeante, construire des possibilités d’action et décider avec peu de temps et d’information ; une comparaison exhaustive d’options prédéfinies peut alors être inadaptée.",
  "feedbacks[0]": "La critique concerne les hypothèses et conditions d’application. Elle n’implique ni que tous les modèles formels sont inutiles ni que toutes les décisions expertes sont immédiates.",
  "doc_explanation": "La décision naturaliste examine l’activité de personnes expérimentées dans son contexte. Des procédures et outils formels peuvent rester utiles lorsque leur usage correspond à la situation et au temps disponible.",
  "exam_tip": "Examiner l’adéquation entre modèle, expertise, information, temporalité et dynamique de la situation ; ne pas opposer simplement intuition bonne et analyse mauvaise.",
  "feedbacks[1]": "La critique du passage porte sur les conditions d’application des modèles, non sur une incapacité intellectuelle des opérateurs.",
  "feedbacks[2]": "Les outils formels peuvent être utilisés par des personnes. Leur pertinence dépend des hypothèses, de la tâche et du contexte ; ils ne sont pas réservés aux systèmes sans humains."
}
```

## Q41 — Ergonomie proactive : fausse citation

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A exprime l’orientation générale, mais la distinction proactive/réactive ne signifie pas que l’une appartient exclusivement au présent et l’autre au passé.

**2. Étanchéité des distracteurs.** Les distracteurs ne rivalisent pas conceptuellement. Le rejet du blâme comme fin exclusive ne justifie pas une exonération automatique de toute action individuelle.

**3. Qualité des rétroactions.** Un projet peut bénéficier d’une intervention tardive substantielle ; dire qu’il ne reste que de la cosmétique ou que l’ergonome est toujours là dès le premier jour dépasse le texte.

**4. Citations et attributions.** Le doc_quote reconstruit plusieurs phrases, ajoute from its inception et une phrase de conceptualization/evaluation non présentes. Le conseil de mémoriser inception comme mot de Cañas est donc particulièrement trompeur.

**5. Langue et rigueur.** Employer « dès l’amont » ou « dès la conception », mais en paraphrase clairement identifiée.

**Appuis :** Cañas, p. 319–320.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quelle différence d’orientation distingue une intervention ergonomique proactive d’une intervention déclenchée par des difficultés déjà observées ?",
  "feedbacks[0]": "Une démarche proactive apporte des connaissances et des données à la conception pour anticiper les conséquences des choix. Une démarche réactive part de difficultés observées. Les deux peuvent coexister.",
  "feedbacks[1]": "La démarche proactive contribue aux décisions de conception en amont ; elle ne se limite pas à rédiger des manuels après la fabrication.",
  "feedbacks[3]": "Le blâme n’est pas l’objectif de la conception proactive : celle-ci cherche à anticiper les effets des choix sur l’activité et le système.",
  "doc_quote": "« Today, the process of innovation requires that ergonomists “proactively” supply ideas and empirical data for the design of future artifacts improving human performance and public acceptance of new technologies [...] »",
  "doc_page": "Page 320 — Design",
  "doc_explanation": "L’intervention proactive cherche à influencer les choix avant leur mise en œuvre. L’analyse des difficultés et la correction après déploiement restent aussi des activités ergonomiques.",
  "exam_tip": "Proactif : anticiper et contribuer à la conception. Réactif : partir de problèmes observés. Le mot inception ne figure pas dans le passage cité.",
  "options[0]": "Une démarche réactive part de difficultés observées ; une démarche proactive fournit en amont des connaissances et des données pour orienter la conception."
}
```

# 🟡 AMÉLIORATIONS RECOMMANDÉES

## Q01 — Définition de l’IEA

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** La clé B répond au double objectif. En revanche, « garantit » transforme un objectif de conception en garantie de résultat : la définition n’établit ni absence d’accident ni résilience assurée.

**2. Étanchéité des distracteurs.** Pas de deuxième réponse complète identifiée. D contient des moyens possibles — sélection et formation — mais ne donne pas le double objectif ; il faut expliquer cette insuffisance plutôt que déclarer ces moyens abandonnés.

**3. Qualité des rétroactions.** La rétroaction D oppose artificiellement sélection et conception et introduit un « humain moyen ». Le conseil prédit les attentes de Mario Passalacqua sans document pédagogique à l’appui.

**4. Citations et attributions.** La définition est étayée p. 316. Les prédictions sur le professeur ne le sont pas.

**5. Langue et rigueur.** Remplacer « contre-sens » par « contresens ». Réduire les qualificatifs laudatifs qui tiennent lieu de démonstration.

**Appuis :** Cañas, p. 316–317.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[0]": "Cette proposition privilégie le rendement et l’adaptation des salariés aux exigences de l’organisation ; elle ne formule pas l’optimisation conjointe du bien-être humain et de la performance du système.",
  "feedbacks[3]": "La sélection et la formation peuvent contribuer à la sécurité, mais elles ne définissent pas le double objectif de l’ergonomie et ne dispensent pas de concevoir des systèmes adaptés aux utilisateurs.",
  "doc_explanation": "L’ergonomie vise conjointement le bien-être humain et la performance globale du système. Ces objectifs orientent la conception et l’évaluation ; ils ne constituent pas une garantie d’absence d’erreur ou d’accident.",
  "exam_tip": "Retenir les deux objectifs de la définition : bien-être humain et performance globale du système. Une proposition qui ne formule qu’un seul de ces objectifs ne répond pas entièrement à cette question."
}
```

## Q03 — Domaines d’expertise

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** Ne pas déclarer la clé A fausse parce que le chapitre distingue quatre domaines : l’énoncé annonce expressément le triptyque classique et l’ajout de la neuroergonomie. Toutefois, le chapitre seul ne documente pas la codification institutionnelle de l’IEA invoquée.

**2. Étanchéité des distracteurs.** La distinction domaines d’expertise / secteurs d’application est pertinente. D n’est cependant pas une liste cohérente de « types d’interventions temporelles » : « ergonomie de sanction » n’est pas une catégorie établie par la source.

**3. Qualité des rétroactions.** La rétroaction D légitime une pseudo-catégorie. L’équivalence stricte entre ergonomie organisationnelle et macroergonomie mérite d’être évitée dans une question de définitions.

**4. Citations et attributions.** Pour une question exclusivement fondée sur les p. 317–318, interroger les quatre domaines effectivement énumérés, sans reconstituer une histoire de la nomenclature de l’IEA.

**5. Langue et rigueur.** Minuscules aux noms communs des domaines. Ne pas faire de « macroergonomie » une traduction obligatoire de « organizational ergonomics ».

**Appuis :** Cañas, p. 317–318.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Cañas et al. distinguent quatre domaines d’expertise aux pages 317–318.",
  "question": "Quels sont les quatre domaines d’expertise explicitement distingués par Cañas et al. ?",
  "options[0]": "L’ergonomie physique, l’ergonomie cognitive, la neuroergonomie et l’ergonomie sociale ou organisationnelle.",
  "feedbacks[0]": "Le chapitre distingue ces quatre domaines : caractéristiques physiques, processus cognitifs, méthodes neurophysiologiques et organisation des systèmes sociotechniques.",
  "feedbacks[3]": "Cette liste mélange des modalités d’intervention avec une « ergonomie de sanction » que le chapitre ne définit pas. Elle ne correspond pas aux domaines d’expertise énumérés.",
  "exam_tip": "Dans ce chapitre, retenir quatre domaines : physique, cognitif, neuroergonomique et social ou organisationnel."
}
```

## Q04 — Système sociotechnique

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B reste la meilleure réponse. « Tout changement technique » et « le système échoue » imposent une causalité nécessaire que la source n’établit pas.

**2. Étanchéité des distracteurs.** Les trois distracteurs sont des positions absolues facilement éliminables. L’analyse conjointe ne signifie pas que toute modification technique bouleverse nécessairement tous les rôles.

**3. Qualité des rétroactions.** Les rétroactions doivent expliquer l’interdépendance, et non la remplacer par un déterminisme technique inversé.

**4. Citations et attributions.** La citation combine deux passages des p. 316 et 318 ; le premier commence à l’intérieur d’une phrase sans le signaler. L’histoire de Tavistock n’est pas documentée dans ce passage.

**5. Langue et rigueur.** « Co-conçus » peut être remplacé par « conçus conjointement ». Corriger « contre-sens ».

**Appuis :** Cañas, p. 316, 318, 323–324.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[1]": "L’approche sociotechnique étudie les interdépendances entre outils, tâches, personnes et organisation. Une modification technique doit donc être évaluée aussi pour ses effets possibles sur le travail collectif.",
  "feedbacks[2]": "Ignorer les facteurs sociaux contredit l’analyse des interactions entre les composantes techniques et organisationnelles.",
  "feedbacks[3]": "Une défaillance technique peut modifier les communications, les responsabilités et la charge de travail. Affirmer qu’elle n’a aucun effet possible exclut précisément les interactions à analyser.",
  "doc_explanation": "Une solution techniquement fonctionnelle peut rester inadaptée à l’organisation du travail. L’analyse sociotechnique examine ses effets sur les tâches, les compétences, les communications et les responsabilités, sans présumer que tout changement entraîne nécessairement un échec.",
  "doc_quote": "« Social or organizational ergonomics deals with the optimization of sociotechnical work systems, including their structures, policies, and organizational processes. »",
  "doc_page": "Page 318 — Social or organizational ergonomics"
}
```

## Q05 — Étymologie d’ergonomie

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** La bonne option introduit « lois naturelles », absent de la formulation citée. Il s’agit d’une interprétation, non du sens littéral établi par le passage.

**2. Étanchéité des distracteurs.** C signifie à tort « ergon = outil ». La qualifier d’anthropométrie ne corrige pas l’erreur : aucun élément de l’option ne désigne le corps humain.

**3. Qualité des rétroactions.** Il faut restituer les racines effectivement citées au lieu de commenter les réponses comme simplement « fantaisistes ».

**4. Citations et attributions.** La source écrit « work » et « law », puis « science of work ». Elle ne donne pas « natural laws ».

**5. Langue et rigueur.** « Lois du travail » peut évoquer le droit du travail. Privilégier « science du travail » et expliciter les deux racines.

**Appuis :** Cañas, p. 316.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[0]": "Ergon : travail ; nomos : loi. Le terme est présenté comme désignant étymologiquement la science du travail.",
  "feedbacks[0]": "Le chapitre traduit ergon par « travail » et nomos par « loi », puis présente l’ergonomie comme la science du travail. Il n’ajoute pas le qualificatif « naturelles ».",
  "feedbacks[2]": "Dans la source, ergon signifie « travail », et non « outil » ; la seconde racine du mot ergonomie est nomos, et non metron.",
  "feedbacks[3]": "Eros et gnosis ne sont pas les racines du mot ergonomie données dans le chapitre.",
  "doc_explanation": "L’étymologie renvoie au travail et à son étude. La définition scientifique contemporaine ajoute l’analyse des interactions entre les humains et les autres composantes des systèmes.",
  "exam_tip": "Ergon = travail ; nomos = loi ; formulation du chapitre : science du travail."
}
```

## Q08 — Théorie de l’activité : contenu hors du passage invoqué

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** La hiérarchie activité–actions–opérations est la réponse théorique visée. Le problème principal est l’alignement avec la lecture : le chapitre ne développe pas cette hiérarchie. « Conditions matérielles et automatisées » réduit abusivement le dernier niveau.

**2. Étanchéité des distracteurs.** Les trois mauvaises réponses sont facilement éliminables, mais la rétroaction C attribue sans justification un schéma de boîte noire au cognitivisme computationnel.

**3. Qualité des rétroactions.** B n’est pas une hiérarchie skinnérienne canonique. Qualifier une liste hétérogène de modèle établi remplace une erreur par une autre.

**4. Citations et attributions.** Le passage p. 324 traite des origines socioculturelles, de l’intériorisation et du contexte historique. Il ne peut servir de citation justificative du triptyque demandé.

**5. Langue et rigueur.** Harmoniser Léontiev dans les textes français tout en conservant Leontiev dans une référence bibliographique originale.

**Appuis :** Cañas, p. 324.

**Intégration :** Remplacement centré sur le corpus : la cible d’apprentissage change. Pour conserver le triptyque original, ajouter un extrait primaire de Léontiev et une référence précise.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Le passage de Cañas et al. consacré à la théorie de l’activité porte sur les origines socioculturelles de la pensée et de l’action.",
  "question": "Quel déplacement de l’analyse cognitive la théorie de l’activité introduit-elle dans ce passage ?",
  "options": [
    "Analyser la pensée et l’action en tenant compte des pratiques sociales, de l’histoire des artefacts et du contexte de développement des personnes.",
    "Réduire toute activité professionnelle à une succession de réflexes innés.",
    "Expliquer la cognition sans considérer les actions externes ni les interactions sociales.",
    "Identifier les niveaux de l’activité aux seuls niveaux hiérarchiques de l’entreprise."
  ],
  "feedbacks": [
    "Le chapitre insiste sur les origines socioculturelles de la pensée et de l’action ainsi que sur l’intériorisation d’actions sociales.",
    "La théorie présentée ne réduit pas le travail à des réflexes innés.",
    "Cette proposition exclut précisément les dimensions sociales et pratiques mises en avant par le passage.",
    "L’activité psychologique ne se confond pas avec l’organigramme administratif."
  ],
  "doc_explanation": "Dans ce passage, les pensées et les actions sont étudiées dans leur continuité avec les pratiques sociales et l’histoire des personnes et des artefacts. La hiérarchie activité–actions–opérations exige une lecture complémentaire de Léontiev.",
  "exam_tip": "Pour ce passage : origines socioculturelles, intériorisation et contexte historique de l’activité."
}
```

## Q09 — Cognition distribuée

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B exprime le cadre distribué. L’explication étend cependant le système à « tous » les artefacts physiques, sans définir la frontière analytique pertinente pour la tâche.

**2. Étanchéité des distracteurs.** A, C et D sont des caricatures ; aucune deuxième réponse adéquate n’a été identifiée. Les exclure par « réductionnisme » ne démontre pas à lui seul leur inadéquation.

**3. Qualité des rétroactions.** L’exemple confond potentiellement vitesse actuelle et repères de vitesses cibles. Décrire les représentations, leur coordination et leur transformation est plus exact que dire que la vitesse elle-même est partagée.

**4. Citations et attributions.** Hutchins est correctement rattaché à la cognition distribuée dans le chapitre. Il n’est pas nécessaire d’attribuer cet exemple particulier au livre plutôt qu’à l’ensemble des travaux.

**5. Langue et rigueur.** « Boîte crânienne » n’apporte pas de précision au critère de délimitation du système.

**Appuis :** Cañas, p. 324.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[1]": "Dans un cockpit, des représentations de la vitesse actuelle et de vitesses cibles circulent entre personnes, instruments et repères. L’analyse porte sur leur coordination et leur transformation dans l’activité.",
  "feedbacks[3]": "Des mesures cérébrales individuelles peuvent contribuer à une étude, mais elles ne suffisent pas à décrire les échanges et transformations d’information entre personnes et artefacts.",
  "doc_explanation": "L’unité d’analyse peut comprendre les personnes et les artefacts qui participent à la réalisation d’une tâche. Sa frontière dépend de l’activité étudiée : elle ne comprend pas automatiquement tous les objets présents."
}
```

## Q10 — Système cognitif conjoint

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B reste défendable dans le contexte de conduite de procédés. La définition serait trop restrictive si elle était présentée comme limitée à tout système industriel dynamique.

**2. Étanchéité des distracteurs.** Les distracteurs informatique, syndical et psychométrique ne constituent pas des réponses concurrentes, mais « absurde » et « non fondé » ne disent pas pourquoi.

**3. Qualité des rétroactions.** Le rejet de toute analyse des composantes est excessif : la thèse est l’insuffisance d’une analyse séparée pour comprendre l’activité conjointe, non l’interdiction de distinguer les composantes.

**4. Citations et attributions.** Le chapitre cite Hollnagel et Woods en 2007 : ne pas substituer silencieusement une date d’édition différente. La citation est un assemblage de deux passages correctement signalé par une ellipse.

**5. Langue et rigueur.** Uniformiser « système cognitif conjoint » et éviter les capitales de slogan.

**Appuis :** Cañas, p. 322–324.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Dans le contexte de la conduite de procédés décrit ici, que désigne un système cognitif conjoint ?",
  "feedbacks[1]": "L’analyse porte sur la manière dont personnes et dispositifs coordonnent leurs activités pour atteindre leurs objectifs et maintenir le contrôle. Étudier séparément leurs capacités ne suffit pas à expliquer le fonctionnement conjoint.",
  "feedbacks[2]": "Un comité peut être étudié comme collectif de travail, mais sa composition syndicale ne définit pas le système cognitif conjoint décrit dans cette question.",
  "feedbacks[3]": "Un score de quotient intellectuel ne décrit ni les interactions avec les artefacts ni la coordination de l’activité.",
  "doc_explanation": "L’analyse d’un système cognitif conjoint examine comment personnes et dispositifs réalisent ensemble une activité dans son contexte, plutôt que de déduire son fonctionnement de la simple addition de capacités individuelles."
}
```

## Q11 — Modèles mentaux

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B décrit une fonction pertinente. En revanche, un modèle erroné ne rend pas nécessairement « toutes » les décisions inadaptées : l’erreur peut concerner une partie du système ou rester sans effet dans certaines situations.

**2. Étanchéité des distracteurs.** Suivre une procédure sans comprendre tout le système n’est pas en soi une absence totale de modèle mental et n’entraîne pas nécessairement une catastrophe.

**3. Qualité des rétroactions.** La rétroaction C et l’explication apprennent des implications universelles injustifiées.

**4. Citations et attributions.** La source décrit une représentation subjective et ses fonctions, sans ces garanties négatives.

**5. Langue et rigueur.** Remplacer mismatch par « écart » ou « inadéquation ».

**Appuis :** Cañas, p. 326.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[0]": "Mémoriser des coordonnées peut être utile, mais ne décrit pas une représentation de la structure et du fonctionnement du système.",
  "feedbacks[2]": "L’application d’une procédure ne remplace pas la compréhension du système. En situation non couverte ou mal reconnue, un modèle mental inadéquat peut compromettre le diagnostic.",
  "doc_explanation": "Un modèle mental est une représentation subjective de la structure et du fonctionnement du système. Une représentation incomplète ou erronée peut conduire à des diagnostics et prévisions inadéquats, sans rendre nécessairement toutes les décisions incorrectes."
}
```

## Q12 — Rasmussen : niveau fondé sur les connaissances

Clé initiale : **C** (`correctIndex: 2`). Clé des propositions : **C** avant toute permutation.

**1. Validité scientifique et corrigé.** C est la réponse attendue. Le contrôle conscient élevé n’est pas forcément « maximal » et le recours aux connaissances ne sature pas nécessairement la mémoire de travail.

**2. Étanchéité des distracteurs.** Le niveau heuristic-based n’appartient pas au triptyque SRK : son rejet est correct. Ne pas en déduire que les heuristiques n’existent pas aux niveaux pertinents.

**3. Qualité des rétroactions.** L’explication transforme une sollicitation accrue en saturation automatique ; le moyen mnémotechnique assimile le niveau habiletés à une absence totale d’attention.

**4. Citations et attributions.** L’attribution à Rasmussen (1983), et non à Reason comme inventeur de SRK, est correcte dans le chapitre.

**5. Langue et rigueur.** « Accroît drastiquement » ne précise ni condition ni mesure. Employer une formulation conditionnelle.

**Appuis :** Cañas, p. 321.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "doc_explanation": "Face à un problème nouveau pour lequel les routines et règles disponibles ne suffisent pas, l’opérateur doit construire et évaluer un plan. Cette activité sollicite fortement les ressources cognitives et peut accroître le risque d’erreur, sans entraîner nécessairement leur saturation.",
  "exam_tip": "SRK : habiletés = conduites largement automatisées ; règles = sélection de règles apprises ; connaissances = résolution d’un problème nouveau nécessitant un contrôle conscient important."
}
```

## Q13 — Reason : slips et lapses

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A exprime la distinction visée, mais un slip n’est pas toute déficience motrice. « Classification psychologique universelle » surévalue le statut d’une taxonomie.

**2. Étanchéité des distracteurs.** Les distracteurs ne donnent pas cette distinction. La rétroaction doit distinguer erreur d’exécution, erreur de mémoire, erreur de planification et écart intentionnel sans les réduire à des professions ou à un degré d’expertise.

**3. Qualité des rétroactions.** Le mécanisme d’attention ou de mémoire doit être explicité par des exemples, non par une formule ambiguë de « défaillance perceptivo-motrice de l’attention ».

**4. Citations et attributions.** Le doc_title annonce Reason (1990), mais le bouton mène à Cañas et à un passage qui ne développe pas slips/lapses. Une référence mentionnée dans une bibliographie ne remplace pas le passage probant.

**5. Langue et rigueur.** « Glissade d’action » est un calque peu transparent ; employer « erreur d’exécution (slip) » et « oubli (lapse) ».

**Appuis :** Cañas, p. 321 ; référence à Norman et Reason sans développement de cette distinction ; Reason (2000), Human error: models and management, DOI 10.1136/bmj.320.7237.768.

**Intégration :** Ne pas présenter la citation générique de Cañas comme preuve textuelle de la distinction. Ajouter un extrait primaire portant précisément sur les définitions avant utilisation sommative.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Complément à la lecture de Cañas : dans la distinction associée aux travaux de Reason, on sépare les erreurs d’exécution et les oublis lorsque le plan d’action est approprié.",
  "question": "Quelle distinction sépare une erreur d’exécution (slip) d’un oubli (lapse) ?",
  "options[0]": "Dans un slip, l’action exécutée s’écarte involontairement de l’action voulue ; dans un lapse, une défaillance de mémoire perturbe la réalisation de l’action prévue.",
  "feedbacks[0]": "Appuyer involontairement sur le bouton voisin illustre un slip ; oublier une étape prévue illustre un lapse. L’analyse porte sur l’exécution ou la mémoire, et non d’abord sur la pertinence du plan.",
  "doc_explanation": "Distinguer le plan inadapté, l’exécution qui s’écarte du plan et l’oubli d’une action prévue. Ces catégories servent à décrire des mécanismes et à choisir des moyens de prévention adaptés.",
  "doc_title": "Cañas et al. (2011) — contexte général ; distinction slips/lapses à documenter par une lecture complémentaire",
  "exam_tip": "Slip : action exécutée différente de l’action voulue. Lapse : oubli perturbant l’action prévue. Ne pas les confondre avec un plan inadéquat."
}
```

## Q16 — Reason : modèle du fromage suisse

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A est la réponse visée. Une ouverture dans une barrière ne suffit pas à produire un accident ; l’alignement représente une trajectoire possible d’exposition au danger.

**2. Étanchéité des distracteurs.** La réfutation d’un récit uniquement centré sur l’opérateur ne doit pas affirmer que Reason aurait rejeté toute structure séquentielle : le modèle des barrières conserve une représentation de trajectoire.

**3. Qualité des rétroactions.** Préciser que les brèches proviennent de défaillances actives et de conditions latentes plutôt que d’assimiler chaque trou à une seule catégorie.

**4. Citations et attributions.** Le titre Reason (1997) associé à une citation de Cañas/Wilpert p. 322 est une attribution trompeuse. Le modèle du fromage suisse n’est pas développé dans ce passage.

**5. Langue et rigueur.** « Alignement accidentel des trous » suggère une pure coïncidence ; préciser la conjonction des conditions et les dépendances possibles.

**Appuis :** Reason (2000), DOI 10.1136/bmj.320.7237.768 ; Cañas, p. 322 : contexte systémique, mais pas exposition de ce modèle.

**Intégration :** Ajouter la source complémentaire et corriger le bouton de navigation : ne plus présenter le passage de Cañas comme extrait du livre de Reason. Retirer l’ajout automatique de guillemets pour la synthèse proposée.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "context": "Complément aux cinq lectures : le modèle des barrières de James Reason est présenté explicitement dans Human error: models and management (2000).",
  "feedbacks[0]": "Les tranches représentent des défenses et leurs ouvertures des faiblesses. Un accident devient possible lorsque ces faiblesses permettent au danger de traverser les défenses ; une seule ouverture ne suffit pas nécessairement.",
  "feedbacks[1]": "Le modèle ne réduit pas l’accident à la faute d’un seul opérateur : il examine les défaillances des défenses et les conditions qui permettent une trajectoire accidentelle.",
  "doc_title": "James Reason (2000) — Human error: models and management",
  "doc_page": "Section The Swiss cheese model of system accidents",
  "doc_quote": "Synthèse, non citation textuelle : des faiblesses présentes dans plusieurs défenses peuvent se combiner et permettre une trajectoire accidentelle.",
  "doc_explanation": "Analyser plusieurs couches de défense, leurs faiblesses et leurs interactions. La présence d’une seule faiblesse ne détermine pas à elle seule l’issue de l’événement.",
  "exam_tip": "Tranches : défenses. Trous : faiblesses liées aux défaillances actives et aux conditions latentes. Accident possible : trajectoire du danger à travers les défenses."
}
```

## Q17 — Défaillances actives et conditions latentes

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A comporte déjà « souvent », mais l’explication tend à transformer l’opérateur en simple déclencheur automatique. L’analyse systémique ne prouve pas a priori que toute défaillance active est causée par une décision lointaine déterminée.

**2. Étanchéité des distracteurs.** Les distracteurs ne menacent pas directement l’unicité. D inverse les temporalités, mais les termes désignent d’abord des effets et positions dans le système, non des personnes définitivement classées actives ou latentes.

**3. Qualité des rétroactions.** Le mécanisme doit être expliqué sans exonération automatique ni déterminisme rétrospectif.

**4. Citations et attributions.** Le doc_title Reason (1997) ne correspond pas à l’extrait de Cañas/Hollnagel et Woods. L’Article E comporte en revanche un extrait de Reason attribué à Human error (1990).

**5. Langue et rigueur.** « Pointe acérée » et « bout émoussé » demandent une définition fonctionnelle ; éviter de les employer comme catégories morales.

**Appuis :** HF101-E, Irony 1 ; Reason (1990) cité secondairement ; Reason (2000), DOI 10.1136/bmj.320.7237.768.

**Intégration :** Déplacer les ancres Q17 vers l’extrait de Reason dans l’Article E.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Pourquoi l’identification d’une défaillance active ne suffit-elle généralement pas à expliquer un accident dans une analyse systémique ?",
  "doc_id": "doc_art_e",
  "doc_title": "Human Factors 101 — Article E, citation secondaire de James Reason (1990)",
  "doc_page": "Section Irony 1: Designers are human too!",
  "doc_quote": "« Rather than being the main instigators of an accident, operators tend to be the inheritors of system defects created by poor design, incorrect installation, faulty maintenance and bad management decisions. »",
  "doc_explanation": "Une action de première ligne doit être étudiée avec les conditions de conception, de maintenance, de ressources et d’organisation qui ont influencé l’activité et les défenses. Cette démarche n’impose ni culpabilité ni exonération avant l’enquête.",
  "exam_tip": "Distinguer les effets immédiats des actes de première ligne et les conditions du système susceptibles de préparer une situation dangereuse ; analyser leur combinaison.",
  "feedbacks[0]": "La présence d’un acte de première ligne ne clôt pas l’enquête. L’Article E reprend Reason pour souligner que les opérateurs peuvent hériter de défauts de conception, d’installation, de maintenance et d’organisation.",
  "options[0]": "Parce qu’une défaillance active peut se combiner avec des conditions de conception, de maintenance et d’organisation qui ont affaibli les défenses ou rendu l’erreur plus probable."
}
```

## Q21 — Ethnographie et savoir tacite

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A est pertinente, mais « inaccessibles » et « seule » excèdent le constat de difficultés d’explicitation des connaissances tacites.

**2. Étanchéité des distracteurs.** La durée n’oppose pas scientifiquement une observation qui prendrait nécessairement des semaines à des méthodes toujours rapides. D doit être réfuté pour la finalité méthodologique, pas par un calendrier universel.

**3. Qualité des rétroactions.** Les entretiens situés, l’analyse de tâche et la confrontation avec des traces ne sont pas rendus inutiles par l’intérêt de l’observation.

**4. Citations et attributions.** Le chapitre critique aussi la prétention à observer sans présupposé ; conserver cette réserve, absente de l’éloge unilatéral de l’immersion.

**5. Langue et rigueur.** « Tacite » ne signifie pas absolument inconscient et définitivement impossible à verbaliser dans toute méthode.

**Appuis :** Cañas, p. 330–331 ; HF101-A, méthodes : observation, analyse de tâche et walk-through/talk-through.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[0]": "Pour observer des routines, ajustements et interactions dont les acteurs rendent difficilement compte dans un questionnaire seul.",
  "feedbacks[0]": "L’observation donne accès à l’activité située et à certains ajustements peu explicités. Elle peut être combinée à des entretiens et à l’analyse de traces pour comprendre leur signification.",
  "feedbacks[3]": "Le choix de l’observation se justifie ici par l’accès à l’activité en contexte, non par une durée supposée toujours plus courte ou toujours plus longue que celle des autres méthodes.",
  "doc_explanation": "L’observation et les études de terrain peuvent révéler des dimensions de l’activité peu accessibles au seul déclaratif. Elles ne sont pas les seuls moyens d’étudier le savoir tacite et ne sont pas dépourvues de présupposés."
}
```

## Q24 — Défaillance de niveau 1

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B illustre le défaut de perception. L’explication et le conseil étendent cependant la défaillance à l’absence de toute perception et à l’impossibilité de tout traitement supérieur.

**2. Étanchéité des distracteurs.** Une donnée critique peut être manquée alors que de nombreuses autres sont correctement perçues. Le diagnostic N1 n’exige ni cécité ni surdité globale.

**3. Qualité des rétroactions.** Le scénario ne suffit pas à démontrer une vision en tunnel comme cause unique ; il décrit d’abord un indice non perçu.

**4. Citations et attributions.** Le doc_quote modifie la phrase d’introduction et le libellé de Gathering information. Citer directement la formulation fournie.

**5. Langue et rigueur.** Si la variable est la pression artérielle, parler d’un moniteur physiologique plutôt que d’un moniteur cardiaque au sens d’un ECG seul.

**Appuis :** HF101-D, Gathering information.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[1]": "L’information pertinente n’a pas été perçue. Cela caractérise une défaillance de niveau 1 ; la cause précise — présentation, attention, charge ou autre facteur — doit encore être étudiée.",
  "doc_quote": "« Gathering information: data was not observed, or data was not visible, perhaps due to a high workload, distractions, interruptions, or poor design of displays and interfaces. »",
  "doc_explanation": "Une défaillance de niveau 1 peut porter sur un seul indice pertinent. Elle ne signifie pas que l’opérateur ne perçoit rien ni qu’il ne peut mobiliser aucune connaissance antérieure.",
  "exam_tip": "Niveau 1 : une information pertinente manque dans ce qui a été perçu ou retenu. Niveau 2 : l’information est interprétée de manière inadéquate.",
  "options[1]": "Un anesthésiste, accaparé par une intubation difficile, ne perçoit pas l’alarme visuelle et sonore d’un moniteur physiologique signalant une chute brutale de pression artérielle.",
  "feedbacks[3]": "Cette proposition décrit une action exploratoire ; elle n’établit pas qu’une information pertinente a été manquée. Elle ne suffit donc pas à illustrer la défaillance N1 demandée."
}
```

## Q28 — Définition d’une ironie

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B exprime l’idée générale, mais la source dit opposé à ce qui était attendu, non nécessairement opposé à une intention consciente particulière.

**2. Étanchéité des distracteurs.** Les alternatives sont des causes de panne ou plaisanteries, plutôt que des définitions concurrentes plausibles. Elles ne menacent pas l’unicité dans ce cadre.

**3. Qualité des rétroactions.** Une conséquence contraire aux attentes n’est pas nécessairement tragique. Ne pas définir toute automatisation comme une tentative d’éliminer toute compétence humaine.

**4. Citations et attributions.** La définition est donnée dans l’Article E et dans l’article original. Attribuer la formulation française à une traduction, non à un verbatim français de 1983.

**5. Langue et rigueur.** Remplacer « intentionnellement recherché » par « attendu ».

**Appuis :** HF101-E, définition de l’ironie ; Bainbridge (1983), Automatica, 19(6), 775–779.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[1]": "Une combinaison de circonstances dont le résultat s’avère contraire à ce qui était attendu.",
  "feedbacks[1]": "L’ironie tient à l’écart entre l’effet attendu et l’effet obtenu. Dans l’automatisation, une intervention destinée à alléger le rôle humain peut, dans certaines situations, rendre son intervention plus exigeante.",
  "doc_explanation": "L’automatisation peut apporter des bénéfices tout en produisant des conséquences inattendues sur le travail humain. Identifier une ironie ne revient pas à conclure que toute automatisation est nuisible.",
  "exam_tip": "Ironie : résultat contraire aux attentes. Examiner la transformation du rôle humain plutôt que présumer sa disparition."
}
```

## Q30 — Tâches résiduelles et citation de Bainbridge

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A reste une traduction acceptable de l’idée. Le problème est la revendication de mot à mot dans le feedback anglais.

**2. Étanchéité des distracteurs.** B n’est pas à valider comme formulation historique exacte de la liste de Fitts. C n’est pas une définition générale de la conception à défaillance sûre ; une commande manuelle mécanique universelle n’en découle pas.

**3. Qualité des rétroactions.** Expliquer les tâches résiduelles sans déclarer que toute automatisation ne laisse que les pannes et détruit nécessairement toute pratique.

**4. Citations et attributions.** Original p. 777 : « easy parts of his task ». L’Article E et le feedback écrivent « of the task ». Le doc_quote colle ensuite à la citation un paragraphe rédactionnel de l’Article E. Séparer les auteurs et les niveaux de citation.

**5. Langue et rigueur.** En français, annoncer « traduction » ; supprimer « citation textuelle culte ».

**Appuis :** Bainbridge (1983), p. 777, original contrôlé visuellement ; HF101-E, Irony 2.

**Intégration :** Le bouton doit ouvrir la source originale ou signaler expressément une citation secondaire ; conserver une seule paire de guillemets.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quelle formulation résume l’effet possible d’une répartition résiduelle des tâches humaines, souligné par Bainbridge ?",
  "feedbacks[0]": "L’automatisation peut retirer des composantes qui entretenaient la pratique et la compréhension, tout en laissant à l’opérateur des interventions difficiles. C’est un effet possible à prendre en compte lors de la répartition des fonctions.",
  "feedbacks[1]": "Une règle d’allocation des fonctions ne formule pas ici le paradoxe des tâches humaines résiduelles ; cette phrase ne doit pas être attribuée comme citation à Bainbridge.",
  "feedbacks[2]": "Une exigence universelle de commande manuelle mécanique n’est ni la citation étudiée ni une définition générale de la conception à défaillance sûre.",
  "feedbacks[3]": "La supervision et la reprise de contrôle peuvent rester nécessaires après automatisation. Leur suppression générale n’est pas la conclusion de Bainbridge.",
  "doc_title": "Bainbridge, L. (1983) — Ironies of Automation",
  "doc_page": "Page 777 — Human–computer collaboration",
  "doc_quote": "« By taking away the easy parts of his task, automation can make the difficult parts of the human operator’s task more difficult. »",
  "doc_explanation": "Une bonne répartition des fonctions doit considérer la cohérence de l’activité humaine restante, les possibilités de pratique et les exigences de reprise de contrôle.",
  "exam_tip": "Ne pas évaluer seulement ce que l’automate sait faire : évaluer aussi le travail qu’il laisse à l’humain."
}
```

## Q33 — HSG48 : prévention et tolérance à l’erreur

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A reprend le message central. Toutefois, un système tolérant aux erreurs et un système à défaillance sûre ne sont pas deux étiquettes strictement interchangeables.

**2. Étanchéité des distracteurs.** Les autres propositions ne répondent pas à la combinaison prévention/tolérance. La consigne « cet extrait » est peu autonome si l’extrait n’est visible qu’après la réponse.

**3. Qualité des rétroactions.** Expliquer la réduction de la probabilité des erreurs et la limitation de leurs conséquences. Ne pas présenter la formation comme inutile.

**4. Citations et attributions.** La citation HSG48 est reproduite dans A, p. 18 de la publication de 1999. L’expression sur le contrôle le moins efficace par le comportement se trouve explicitement dans C ; ne pas l’attribuer mot pour mot à A.

**5. Langue et rigueur.** Dans A, « empêcher leur apparition » a un antécédent grammatical ambigu. Écrire explicitement « prévenir les erreurs ».

**Appuis :** HF101-A, citation HSG48 (1999), p. 18 ; HF101-C, Work planning and risk assessment.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quel principe le HSG48, cité dans l’Article A, formule-t-il au sujet de l’erreur humaine et de la conception des systèmes ?",
  "options[0]": "Même des personnes formées et motivées peuvent commettre des erreurs ; il faut chercher à prévenir ces erreurs et concevoir des systèmes capables d’en limiter les conséquences.",
  "feedbacks[0]": "La prévention cherche à réduire la probabilité d’erreur ; la tolérance à l’erreur vise à empêcher qu’une erreur entraîne directement des conséquences graves. Les deux démarches sont complémentaires.",
  "doc_explanation": "Concevoir un système tolérant à l’erreur consiste à limiter les conséquences des erreurs prévisibles. Cela ne se confond pas strictement avec toute conception à défaillance sûre et n’exclut pas le rôle de la formation.",
  "exam_tip": "Deux objectifs complémentaires : prévenir les erreurs et limiter leurs conséquences lorsqu’elles surviennent."
}
```

## Q38 — Accrétion, ajustement et restructuration

Clé initiale : **C** (`correctIndex: 2`). Clé des propositions : **C** avant toute permutation.

**1. Validité scientifique et corrigé.** C correspond à la restructuration. B réduit cependant le tuning à l’action motrice ; la source parle des paramètres de nos actions sans cette restriction.

**2. Étanchéité des distracteurs.** D ajoute un transfert « sous-cortical » sans source. Un distracteur faux ne doit pas servir à enseigner une localisation cérébrale fictive.

**3. Qualité des rétroactions.** Toute technologie nouvelle n’exige pas nécessairement une restructuration profonde. L’explication doit réserver ce cas aux changements de relations conceptuelles.

**4. Citations et attributions.** Cañas écrit que Norman (1986) décrit ces formes. Cela ne démontre pas qu’il en serait l’unique inventeur en 1986. Ne pas surinterpréter la date de la référence secondaire.

**5. Langue et rigueur.** Le conseil prédisant ce que « les professeurs aiment » n’est pas étayé. Utiliser « ajustement » après définition de tuning.

**Appuis :** Cañas, p. 327.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[1]": "L’ajustement (tuning), qui modifie progressivement les paramètres d’une manière d’agir déjà acquise.",
  "options[3]": "La répétition d’une séquence connue sans modification de ses relations conceptuelles.",
  "feedbacks[1]": "L’ajustement modifie les paramètres de l’action ; il ne se définit pas par la découverte de nouvelles relations conceptuelles et n’est pas limité aux gestes moteurs.",
  "feedbacks[2]": "La restructuration correspond à l’apprentissage de nouvelles relations conceptuelles. Elle peut être nécessaire lorsqu’un système ne peut pas être compris avec l’organisation antérieure des connaissances.",
  "feedbacks[3]": "La répétition d’une séquence connue ne suffit pas à définir une réorganisation conceptuelle.",
  "doc_explanation": "Une nouvelle technologie peut demander de nouveaux faits, un ajustement des façons d’agir ou une restructuration conceptuelle. La forme d’apprentissage requise dépend du changement à comprendre.",
  "exam_tip": "Dans la présentation de Norman citée par Cañas : accrétion = faits ; ajustement = paramètres de l’action ; restructuration = nouvelles relations conceptuelles."
}
```

## Q40 — Réseaux attentionnels

Clé initiale : **B** (`correctIndex: 1`). Clé des propositions : **B** avant toute permutation.

**1. Validité scientifique et corrigé.** B décrit une contribution possible aux fluctuations, mais le chapitre écrit can explain et non une explication exclusive ou un diagnostic individualisé.

**2. Étanchéité des distracteurs.** La perte définitive de synapses après quinze minutes, l’inversion des hémisphères et l’arrêt total des récepteurs sont des alternatives caricaturales. Elles évaluent surtout la détection de l’absurde.

**3. Qualité des rétroactions.** Le corrigé attribue la découverte à 2007 et nomme les réseaux, tandis que le chapitre se contente de mentionner trois réseaux et une référence. Le détail est un complément, pas le contenu littéral de la phrase.

**4. Citations et attributions.** La référence à Posner, Rueda et Kanske est bien présente p. 326. Elle ne prouve ni l’antériorité historique ni une mesure directe de toute perte de SA.

**5. Langue et rigueur.** Supprimer « tendance lourde du cours » sans programme de cours attestant cette priorité.

**Appuis :** Cañas, p. 325–326.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "question": "Quelle explication possible des fluctuations de performance Cañas et al. évoquent-ils en lien avec les réseaux attentionnels ?",
  "options": [
    "La performance résulte uniquement des connaissances durables ; les variations attentionnelles n’y contribuent pas.",
    "Des variations de l’équilibre fonctionnel entre réseaux attentionnels peuvent contribuer aux fluctuations de performance.",
    "Le niveau de vigilance détermine à lui seul toute la compréhension de la situation, indépendamment des connaissances.",
    "Les fluctuations de performance observées permettent à elles seules d’identifier précisément l’activité de chaque réseau."
  ],
  "feedbacks": [
    "Le chapitre fait intervenir les variations attentionnelles ; les connaissances durables ne sont donc pas sa seule explication.",
    "Le texte propose une contribution des réseaux attentionnels aux fluctuations temporelles, sans en faire une explication unique de chaque événement.",
    "La conscience de la situation dépend aussi des connaissances, de l’information et des exigences de la tâche.",
    "Une observation comportementale ne suffit pas, sans protocole de mesure approprié, à identifier séparément les mécanismes neuraux."
  ],
  "doc_explanation": "Le chapitre présente la neuroergonomie comme une voie d’étude des mécanismes de la performance. Une hypothèse de contribution ne doit pas être convertie en diagnostic certain d’une défaillance particulière.",
  "exam_tip": "Réseaux attentionnels : contribution possible aux fluctuations ; ne pas confondre hypothèse explicative et diagnostic causal."
}
```

## Q42 — Doublon de rationalité locale

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** La clé est compatible avec le principe 2, mais l’item évalue presque le même objectif que Q34. La répétition peut être voulue en entraînement ; en examen, elle doit être justifiée par le plan de couverture.

**2. Étanchéité des distracteurs.** Les réponses sont à nouveau aisément séparables par les indices moraux et les absolus. Deux réussites ne constituent pas deux preuves indépendantes de compréhension.

**3. Qualité des rétroactions.** Les exemples et le conseil réitèrent le même message, au détriment de l’examen d’un outil d’enquête distinct.

**4. Citations et attributions.** L’Article C contient un outil non exploité par ce doublon : le test de substitution. Il permet un remplacement restant dans le corpus.

**5. Langue et rigueur.** Remplacer « faisaient sens » par « avaient du sens » ou « paraissaient cohérentes » ; éviter « crasher ».

**Appuis :** HF101-C, Incident investigations.

**Intégration :** Déplacer les ancres Q42 sur substitution test. Cette proposition change explicitement l’objectif de l’item pour réduire le doublon avec Q34.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "tag": "HF101-C — Test de substitution en enquête",
  "context": "L’Article C propose d’examiner si des pairs placés dans les mêmes circonstances auraient vraisemblablement agi de façon similaire.",
  "question": "Quelle est la fonction du test de substitution dans cette analyse ?",
  "options": [
    "Explorer dans quelle mesure le contexte pouvait conduire des pairs comparables à adopter un comportement similaire, sans que cela prouve à lui seul l’innocuité ou la justification du comportement.",
    "Établir automatiquement l’absence de responsabilité de toute personne dès qu’un collègue aurait fait la même chose.",
    "Remplacer l’étude des informations disponibles par un vote sur la popularité de l’opérateur.",
    "Prouver que toutes les personnes réagissent toujours de manière identique dans une même situation."
  ],
  "feedbacks": [
    "Le test examine l’influence plausible du contexte au-delà des caractéristiques d’un seul individu ; il ne constitue pas un verdict automatique.",
    "La similarité probable des comportements n’établit ni la sécurité ni la justification normative de l’acte.",
    "Le test porte sur des circonstances comparables et des informations disponibles, non sur la popularité.",
    "Le principe 2 reconnaît précisément que des personnes peuvent interpréter différemment la même situation."
  ],
  "doc_id": "doc_art_c",
  "doc_title": "Human Factors 101 — Article C : Incident investigations",
  "doc_page": "Section Incident investigations",
  "doc_quote": "« The investigation may identify that in the same circumstances, an individual’s peer group would have likely behaved in the same way (the “substitution test”). »",
  "doc_explanation": "Le test de substitution sert à examiner la contribution du contexte et des contraintes partagées. Il ne remplace ni la reconstitution des faits ni l’évaluation des conséquences.",
  "exam_tip": "Test de substitution : que feraient vraisemblablement des pairs comparables dans les mêmes circonstances ? C’est un outil d’analyse, pas une exonération automatique."
}
```

## Q43 — Situation awareness versus situation assessment

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A distingue correctement état et processus, mais « produit final » suggère un état terminal. La SA reste actualisable et influence à son tour les processus.

**2. Étanchéité des distracteurs.** Les distracteurs caricaturaux n’explorent pas les vraies confusions : état de connaissance versus performance, conscience versus traitement volontaire, individuel versus partagé.

**3. Qualité des rétroactions.** Le feedback réduit la SA à un contenu de mémoire de travail et les processus à des opérations actives. La source ne limite pas l’acquisition à une activité consciente délibérée.

**4. Citations et attributions.** La phrase après Endsley, 1995, p. 36 appartient au commentaire de l’Article D ; elle a en plus été modifiée et collée à la citation d’Endsley. Séparer l’auteur cité et le commentaire secondaire.

**5. Langue et rigueur.** Remplacer « état final » par « état à un moment donné ».

**Appuis :** HF101-D, Is Situation Awareness a process, or the end state? ; Sensemaking.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "options[0]": "La situation awareness désigne un état de connaissance de la situation ; la situation assessment désigne les processus par lesquels cet état est acquis et maintenu.",
  "feedbacks[0]": "La distinction porte sur l’état de connaissance et les processus qui le produisent et l’actualisent. Cet état n’est pas définitif et peut à son tour orienter la recherche d’information.",
  "doc_quote": "« It is necessary to distinguish the term situation awareness, as a state of knowledge, from the processes used to achieve that state. »",
  "doc_title": "Human Factors 101 — Article D, citation secondaire d’Endsley (1995, p. 36)",
  "doc_explanation": "La SA est l’état de connaissance ; l’évaluation de la situation désigne les processus d’acquisition et de maintien. Cette distinction ne signifie pas que la SA serait figée ni que tout processus serait consciemment délibéré.",
  "exam_tip": "SA : état de connaissance actualisable. Situation assessment : processus d’acquisition et de maintien, pas état final."
}
```

## Q44 — Dekker : critique de l’explication, non abolition du construit

Clé initiale : **A** (`correctIndex: 0`). Clé des propositions : **A** avant toute permutation.

**1. Validité scientifique et corrigé.** A rend la mise en garde de Dekker, à condition de viser le constat utilisé seul comme explication. On ne doit pas en déduire que toute analyse de SA est vide ni que le construit est impossible à étudier.

**2. Étanchéité des distracteurs.** B porte sur la mesure en équipe ; citer trois instruments individuels sans préciser leur adaptation ne réfute pas directement cette formulation. C et D sont des distracteurs d’autorité sans intérêt conceptuel.

**3. Qualité des rétroactions.** « Inévitable » dans l’explication reproduit le déterminisme rétrospectif dénoncé. Une bonne enquête ne présuppose pas les facteurs qu’elle doit établir.

**4. Citations et attributions.** Le commentaire de l’Article D et la citation de Dekker doivent rester distingués. L’aphorisme anglais du conseil n’est pas à présenter comme une citation authentifiée de Dekker.

**5. Langue et rigueur.** Préférer « jugement rétrospectif » à une alternance post hoc/post-hoc/hindsight, et supprimer le vocabulaire d’arme théorique.

**Appuis :** HF101-D, Incident investigations: A health warning.

### Remplacements mot à mot

Les propriétés non mentionnées sont à conserver, sous réserve des défauts transversaux.

```json
{
  "feedbacks[0]": "Utilisée seule, l’étiquette ne précise ni les informations accessibles ni leur interprétation. Elle doit conduire à examiner les mécanismes et conditions de l’activité, plutôt qu’à tenir lieu d’explication.",
  "feedbacks[1]": "La critique citée porte sur l’usage explicatif d’une étiquette dans l’enquête, non sur une démonstration d’impossibilité de toute mesure de la conscience de la situation en équipe.",
  "doc_quote": "« There is a danger that a loss of situation awareness becomes a convenient explanation in accident investigations; when in fact, on its own, it explains very little. The use of this term should be a prompt to investigate further. »",
  "doc_title": "Human Factors 101 — Article D, commentaire suivant la citation de Dekker (2013)",
  "doc_explanation": "L’enquête doit établir quelles informations étaient accessibles, comment elles ont été interprétées et quelles conditions ont contribué à une représentation inadéquate. Elle ne doit pas présumer que la dégradation était inévitable.",
  "exam_tip": "« Perte de SA » utilisée seule : point de départ d’une enquête, non explication causale suffisante. Cette formulation est une synthèse, pas une citation de Dekker."
}
```

# 🟢 COQUILLES ET DÉTAILS MINEURS

## M1 — Q01, Q04 et autres occurrences de « contre-sens »
**Problème :** graphie erronée dans les textes français originaux de la banque. **Remplacement :** `contre-sens` → `contresens`. Ne pas appliquer une substitution dans une citation originale d’un auteur sans signalement.

## M2 — Q18–Q19 : sigles et termes de mesure
**Problème :** emploi fluctuant de HRV, « du HRV », et « auto-rapportée ». **Remplacements :** « variabilité de la fréquence cardiaque (VFC ; HRV en anglais) » à la première occurrence ; « la VFC » ensuite ; « évaluation subjective par autoévaluation » à la place de « évaluation subjective auto-rapportée ».

## M3 — Q27 : chirurgie
**Problème :** alternance check-list/checklist/check-lists et post-opératoire. **Remplacements éditoriaux :** « liste de vérification chirurgicale » ; « mortalité postopératoire ». Le titre anglais officiel d’un instrument reste inchangé dans sa référence.

## M4 — Q29 : subordonnée temporelle
**Problème :** « jusqu’à ce qu’un scénario opérationnel imprévu ne survienne ». **Remplacement minimal :** « jusqu’à ce qu’un scénario opérationnel survienne ». La réécriture scientifique de Q29 proposée plus haut supprime aussi l’idée que le scénario doit nécessairement être imprévu.

## M5 — Q34, Q42 : rationalité locale
**Problème :** « faisaient sens », « crasher », slogans en anglais. **Remplacements :** « paraissaient cohérentes aux personnes concernées » ; « provoquer un accident » ; « biais rétrospectif ».

## M6 — Q01–Q44 : ponctuation et citations
**Problème :** doubles guillemets ajoutés à une chaîne déjà citée, majuscules de noms communs, omissions indiquées par des points non délimités. **Remplacements :** une seule paire de guillemets ; `[…]` pour une coupe ; minuscules à « facteurs humains », « ergonomie cognitive », « conscience de la situation » hors début de phrase ou titre. Les langues originales et noms propres restent respectés.

## M7 — Onglets français servant de preuve aux Q19, Q40 et autres questions
**Problème :** certaines traductions contiennent des ajouts conceptuels absents du texte anglais, ainsi que des marques Markdown affichées littéralement (`**…**`, `*…*`). Cela concerne notamment les réseaux nommés de Posner et les précisions sur la charge. Ces ajouts ne peuvent authentifier une réponse comme s’ils étaient le texte source.

**Bannière de remplacement :** « Adaptation pédagogique française : cette version peut contenir des reformulations ou compléments. Pour vérifier une citation, consulter le texte anglais original et la référence indiquée. »

**Exemple HTML :** remplacer `<li>**Réduire les calculs mentaux :** …</li>` par `<li><strong>Réduire les calculs mentaux :</strong> …</li>`. Corriger séparément le contenu : une conversion typographique ne rend pas une traduction fidèle.

# Références externes vérifiées et statut

Les cinq documents téléversés constituent le corpus principal. Les références ci-dessous servent à vérifier les points signalés ; elles ne sont pas réputées avoir été intégrées au lecteur HTML.

- **Reason (2000)**, *Human error: models and management*, BMJ, 320, 768–770. DOI `10.1136/bmj.320.7237.768`. Texte consulté : `https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/`.
- **NASA**, *NASA Task Load Index, manuel v1.0*, sections sur les échelles, évaluations et pondérations ; copie officielle consultée : `https://www.nasa.gov/wp-content/uploads/2026/03/nasa-tlx-v1-0-searchable-text-and-forms.pdf`. La date du répertoire de mise en ligne n’est pas la date de création de l’instrument.
- **Jones et Endsley (1996)**, *Sources of situation awareness errors in aviation*, Aviation, Space, and Environmental Medicine, 67(6), 507–512. Résumé primaire consulté : `https://pubmed.ncbi.nlm.nih.gov/8827130/`. Les méthodes et pourcentages sont vérifiés dans le résumé ; aucune analyse du fichier ASRS brut n’a été réalisée.
- **Haynes et al. (2009)**, *A surgical safety checklist to reduce morbidity and mortality in a global population*, NEJM, 360, 491–499. DOI `10.1056/NEJMsa0810119`. Résumé primaire consulté : `https://pubmed.ncbi.nlm.nih.gov/19144931/`.
- **Bainbridge (1983)**, *Ironies of Automation*, Automatica, 19(6), 775–779. DOI `10.1016/0005-1098(83)90046-8`. Copie de l’article contrôlée, notamment p. 777 : `https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf`.
- **Endsley et Kiris (1995)**, *The Out-of-the-Loop Performance Problem and Level of Control in Automation*, Human Factors, 37(2), 381–394. DOI `10.1518/001872095779064555`. Notice et résumé éditeur consultés.
- **Parasuraman et Manzey (2010)**, *Complacency and Bias in Human Use of Automation: An Attentional Integration*, Human Factors, 52(3), 381–410. DOI `10.1177/0018720810376055`. Texte primaire déposé par auteur et notice consultés ; ne pas prétendre que l’Article E le cite.
- **Hollnagel**, présentation du principe ETTO : `https://erikhollnagel.com/ideas/the-etto-principle-2009/` ; distinction Safety-I/Safety-II : `https://erikhollnagel.com/ideas/safety-i-and-safety-ii-2014`.
- **Shorrock (2016)**, *The Varieties of Human Work*, présentation de l’auteur, sections Work-as-Imagined et Work-as-Prescribed : `https://humanisticsystems.com/2016/12/05/the-varieties-of-human-work/`. Clarification externe, à distinguer de la formulation de l’Article C.
- **Mitre-Hernandez et al. (2021)**, *Pupillary Responses for Cognitive Load Measurement to Classify Difficulty Levels in an Educational Video Game: Empirical Study*. DOI `10.2196/21620`. Texte primaire : `https://pmc.ncbi.nlm.nih.gov/articles/PMC7834946/`. Utilisé pour l’exemple de contrôle de luminance et de référence ; il ne valide pas une règle universelle de VFC.

# Décision d’audit

La banque ne doit pas être présentée comme scientifiquement univoque dans son état actuel. Les corrections urgentes portent sur les contradictions de définition, les généralisations absolues, les citations reconstruites et le rattachement trompeur à des passages sources. Plusieurs clés désignent encore la meilleure réponse parmi les choix proposés ; cela ne transforme pas leur formulation en énoncé scientifiquement irréprochable.

Avant un usage noté : appliquer les réécritures retenues, réparer le rendu, vérifier chaque lien d’ancre, distinguer lectures obligatoires et compléments, rééquilibrer les positions sans désynchroniser les rétroactions, puis faire une seconde lecture indépendante de la version finale. Les statistiques psychométriques nécessitent ensuite des réponses d’étudiants : cet audit éditorial ne les remplace pas.
