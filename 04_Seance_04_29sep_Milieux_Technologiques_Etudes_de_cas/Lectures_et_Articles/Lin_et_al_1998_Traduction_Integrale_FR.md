# Application de l'ingénierie des facteurs humains à la conception des équipements médicaux : L'analgésie contrôlée par le patient (PCA)

**Titre original :** *Applying human factors to the design of medical equipment: patient-controlled analgesia*  
**Auteurs :** L. Lin (1), R. Isla (1), K. Doniz (1), H. Harkness (1), Kim J. Vicente (1), et D. John Doyle (2)  
**Affiliations :**  
(1) Cognitive Engineering Laboratory, Département de génie mécanique et industriel, Université de Toronto, Toronto, Ontario, Canada  
(2) Département d'anesthésie, Hôpital Général de Toronto (TGH), Université de Toronto, Toronto, Ontario, Canada  
**Revue :** *Journal of Clinical Monitoring and Computing* (1998), Vol. 14, No. 4, pp. 253–263.  
**DOI :** [10.1023/A:1009940409259](https://doi.org/10.1023/A:1009940409259)  
**Cadre académique :** PSY7010 — Sciences psychologiques appliquées : Milieux technologiques (UQAM, Maîtrise)  
**Séance associée :** Séance 04 — Séminaire 1 : Études de cas critiques (Pompes PCA & Vol AF447)  
**Professeurs :** Pr Mario Passalacqua & Pr Marc-André Bédard  
**Traduction académique :** Module officiel de traduction académique — Version intégrale française avec synthèse clinique et pagination originale.

---

> ### 🏥 FICHE DE SYNTHÈSE CLINIQUE & ERGONOMIQUE
>
> **Problématique clinique & Thèse centrale :**  
> Dans les dispositifs médicaux critiques comme les pompes d'analgésie autocontrôlée par le patient (PCA), les erreurs de programmation commises par le personnel infirmier constituent la première cause de surdosage en narcotiques (morphine), surpassant largement les pannes mécaniques. Face à une fenêtre pharmacologique étroite (soulager la douleur sans provoquer de dépression respiratoire mortelle), l'approche punitive ou rééducative (« blâmer et réentraîner ») est un échec patent. Lin et collaborateurs démontrent par une évaluation empirique contrôlée que l'application rigoureuse des principes de l'ingénierie des facteurs humains à l'interface permet de diviser par deux le temps de programmation, de réduire drastiquement la charge mentale et d'éradiquer les erreurs de programmation.
>
> **Points cardinaux de l'étude :**
> - **Statistique FDA critique :** Plus de 60 % des décès et blessures graves causés par des dispositifs médicaux résultent d'erreurs d'utilisation imputables à une mauvaise ergonomie des interfaces.
> - **Défauts majeurs de l'interface existante (Abbott Lifecare PCA Plus II) :** Afficheur LCD minuscule séquentiel ne présentant qu'un seul paramètre à la fois (effet « trou de serrure »), absence de vue d'ensemble du protocole, touches multifonctions trompeuses (*REVIEW/CHANGE* qui modifie sans afficher, *RESET/START* sans remise à zéro), navigation rigide et procédure de correction de faute laborieuse.
> - **Externalisation de la mémoire (Don Norman) :** Remplacement de la connaissance en mémoire de travail (*Knowledge in the Head*) par la connaissance dans le monde (*Knowledge in the World*). La nouvelle interface présente en permanence et simultanément les quatre paramètres critiques (concentration, dose bolus, intervalle d'interdiction et limite sur 4 heures) avec des commandes dédiées à fonction unique.
> - **Validation expérimentale rigoureuse :** Plan mixte 2 &times; 3 &times; 2 &times; 2 auprès d'infirmières novices, mesurant le temps d'exécution, le taux d'erreur et la charge subjective NASA-TLX. Résultats : accélération massive, diminution de la charge mentale et préférence unanime (12/12) pour l'interface réergonomisée.

---

<!-- ========================================================================= -->
<!-- PAGE 253 -->
<!-- ========================================================================= -->

---

### 📄 Page 253

Application de l'ingénierie des facteurs humains à la conception des équipements médicaux : l'analgésie contrôlée par le patient (PCA)

L. Lin (1), R. Isla (1), K. Doniz (1), H. Harkness (1), K. J. Vicente (1), et D. J. Doyle (2)

(1) Cognitive Engineering Laboratory, Department of Mechanical and Industrial Engineering, University of Toronto, Toronto, Ontario, Canada

(2) Department of Anaesthesia, Toronto General Hospital, University of Toronto, Toronto, Ontario, Canada

## Résumé (*Abstract*)

**Objectif :** Les dispositifs médicaux informatisés contemporains possèdent des interfaces utilisateur qui sont souvent difficiles à appréhender et à manipuler, augmentant considérablement le risque d'erreur humaine et d'accidents iatrogènes chez les patients. L'objectif de cette recherche était de démontrer empiriquement comment les méthodes et principes de conception issus de l'ingénierie des facteurs humains peuvent être appliqués pour améliorer substantiellement l'ergonomie, la sécurité et l'utilisabilité d'un dispositif médical critique : la pompe d'analgésie autocontrôlée par le patient (PCA).

**Méthodes :** Une analyse cognitive de la tâche (CTA) a été menée pour modéliser les exigences informationnelles imposées aux infirmières lors de la programmation d'une pompe PCA existante d'usage très répandu (Abbott Lifecare PCA Plus II). Cette investigation a été couplée à une étude de terrain réalisée dans la salle de réveil post-opératoire de l'Hôpital Général de Toronto (TGH). Les défaillances de l'interface actuelle ont été caractérisées à l'aide de recommandations ergonomiques reconnues. Une nouvelle interface utilisateur a ensuite été développée sur la base de ces mêmes principes directeurs. Les deux interfaces (l'ancienne et la nouvelle) ont fait l'objet d'une évaluation expérimentale contrôlée dans un environnement simulé, en mesurant le temps d'exécution de la programmation, la charge mentale subjective (NASA-TLX) et le nombre d'erreurs de saisie commises par des infirmières novices.

**Résultats :** Les résultats démontrent de façon statistiquement significative que la nouvelle interface conçue selon les facteurs humains a permis de réduire le temps de programmation de près de moitié, d'abaisser significativement les scores de charge mentale de travail et de diminuer massivement les erreurs de manipulation par rapport à l'interface originale du fabricant.

**Conclusions :** Cette recherche apporte la première démonstration empirique contrôlée montrant que l'application méthodique des principes d'ingénierie des facteurs humains permet d'accroître la sécurité, l'efficience et la fiabilité des équipements médicaux informatisés. Les fabricants de dispositifs biomédicaux sont vivement encouragés à intégrer ces démarches ergonomiques dès les premières étapes du cycle de développement de leurs produits.

## Introduction

L'erreur humaine commise lors de l'utilisation des équipements médicaux constitue une cause majeure et préoccupante de blessures graves et de décès iatrogènes évitables au sein des établissements de santé [1–3]. Les pompes d'analgésie autocontrôlée par le patient (PCA) permettent aux personnes hospitalisées de s'administrer elles-mêmes de petits bolus de médicaments analgésiques (généralement de la morphine) par voie intraveineuse dès l'apparition d'une douleur aiguë [4–6]. L'appareil est conçu pour délivrer une dose prédéterminée lorsqu'un bouton-poussoir est actionné par le patient, tout en interdisant toute nouvelle injection pendant une durée de sécurité appelée « période d'interdiction » (*lockout interval*), afin de laisser au narcotique le temps d'agir et d'empêcher un surdosage pharmacologique potentiellement fatal par dépression respiratoire.

Bien que les pompes PCA aient considérablement amélioré la prise en charge de la douleur post-opératoire, de nombreux incidents critiques et accidents mortels continuent d'être rapportés dans la littérature clinique [4, 6]. Les enquêtes étiologiques révèlent de manière systématique que la grande majorité de ces événements indésirables ne proviennent pas de défaillances mécaniques des pompes, mais d'erreurs humaines survenant lors de la programmation initiale des paramètres ou de la modification des protocoles analgésiques par le personnel soignant [1, 6].

Selon les statistiques officielles de la Food and Drug Administration (FDA) des États-Unis, plus de 60 % de l'ensemble des incidents graves et des décès causés par des dispositifs médicaux résultent directement d'erreurs d'utilisation [1]. Traditionnellement, la réponse des gestionnaires hospitaliers et des fabricants face à ces drames a consisté à inciter les soignants à « faire plus attention », à multiplier les programmes de formation ou à ajouter des procédures administratives de double vérification [3]. Pourtant, les sciences cognitives et l'ergonomie ont démontré depuis longtemps que les erreurs humaines sont le symptôme inévitable de systèmes mal conçus et d'interfaces incompatibles avec les limites du traitement humain de l'information [1, 2, 7].

<!-- ========================================================================= -->
<!-- PAGE 254 -->
<!-- ========================================================================= -->

---

### 📄 Page 254

Lorsque les interfaces des appareils médicaux sont obscures, opaques et déroutantes, même les professionnels les plus dévoués et compétents finissent inévitablement par commettre des erreurs, tout particulièrement dans des environnements hospitaliers chaotiques, bruyants et soumis à une intense pression temporelle [3, 8].

L'ingénierie des facteurs humains fournit un vaste corpus de théories, de principes empiriques et de méthodologies rigoureuses pour concevoir des systèmes de travail et des artefacts adaptés aux capacités perceptives, cognitives et motrices des opérateurs [7, 9–11]. Bien que son application ait profondément transformé la sécurité dans l'aviation civile et l'industrie nucléaire, son adoption dans le domaine de la technologie médicale est demeurée jusqu'ici lente et parcellaire [12–14]. Très peu d'études contrôlées ont documenté quantitativement l'impact positif d'une reconception ergonomique complète d'un dispositif médical sur les performances réelles des utilisateurs.

La présente étude vise à combler cette lacune fondamentale. Nous décrivons ici l'analyse ergonomique approfondie d'une pompe PCA commerciale très répandue, l'Abbott Lifecare PCA Plus II, le développement d'une nouvelle interface utilisateur fondée sur les principes d'ingénierie cognitive, et son évaluation empirique contrôlée auprès de soignants.

## Méthodes

La démarche méthodologique adoptée s'articule en quatre phases séquentielles complémentaires : (1) une analyse cognitive de la tâche (CTA) menée en laboratoire par des tests sur banc d'essai ; (2) une étude de terrain ethnographique réalisée en milieu hospitalier réel ; (3) la conception ergonomique d'un prototype d'interface alternatif ; et (4) une évaluation expérimentale contrôlée comparant l'ancienne et la nouvelle interface.

**Analyse cognitive de la tâche et étude de terrain.** Les tests sur banc d'essai ont été réalisés sur un exemplaire réel de la pompe Abbott Lifecare PCA Plus II. Une inspection fonctionnelle minutieuse de l'appareil a été menée pour expliciter sa structure logique interne, les séquences de programmation requises et les messages d'état générés par le système [15].

L'étude de terrain s'est déroulée dans la salle de réveil post-anesthésique de l'Hôpital Général de Toronto (TGH). Elle a comporté des observations directes de l'activité réelle et des entretiens semi-dirigés avec les infirmières en charge de la programmation quotidienne des pompes PCA. Cette étude a été conduite sur 8 visites au cours desquelles 9 infirmières différentes ont été interrogées, et la programmation effective de 30 pompes PCA a été scrupuleusement observée en situation clinique réelle.

Le développement du nouveau modèle d'interface a directement découlé des constats dressés lors des tests sur banc et de l'étude de terrain. Le prototype de conception a ensuite été présenté aux infirmières du TGH lors d'un atelier clinique afin de recueillir leurs rétroactions directes, d'affiner les fonctionnalités et de favoriser l'adhésion des utilisatrices aux concepts ergonomiques novateurs. Plusieurs modifications majeures ont été immédiatement intégrées sur la base de leurs suggestions cliniques [15].

**Principes de conception issus des facteurs humains.** Les six grands principes directeurs d'ingénierie des facteurs humains [13, 14] mobilisés pour évaluer puis reconcevoir l'interface de la pompe PCA sont les suivants :

<!-- ========================================================================= -->
<!-- PAGE 255 -->
<!-- ========================================================================= -->

---

### 📄 Page 255

* 1. **Fournir une rétroaction immédiate et saillante :** Garantir à l'utilisateur un retour visuel clair et univoque après chaque frappe ou décision, afin qu'il connaisse instantanément l'état interne du système.

* 2. **Rendre la fonction des commandes claire et évidente :** Éliminer toute ambiguïté sur le rôle de chaque touche ou interrupteur (bannir les dénominations trompeuses).

* 3. **Rendre les messages affichés intuitifs et transparents :** Formuler les alertes et les paramètres dans un langage clinique compréhensible sans recourir à des abréviations cryptiques.

* 4. **Minimiser la charge pesant sur la mémoire de travail :** Réduire la dépendance envers la mémoire interne de l'utilisateur (*Knowledge in the Head*) en plaçant les informations et les états de manière permanente et visible dans l'environnement physique (*Knowledge in the World*).

* 5. **Offrir des raccourcis efficaces et sûrs :** Permettre aux professionnels de naviguer rapidement sans leur imposer de laborieux détours séquentiels.

* 6. **Prévoir des voies de sortie et de correction simples :** Permettre à l'opérateur d'annuler une erreur ou de quitter un mode sans devoir réinitialiser tout le protocole à zéro.

**Évaluation expérimentale contrôlée.** Douze sujets sans aucune expérience préalable de la programmation de la pompe Abbott Lifecare PCA ont été recrutés parmi les étudiantes du programme universitaire de sciences infirmières de l'Université de Toronto. Un plan expérimental factoriel mixte 2 × 3 × 2 × 2 a été mis en place :

* • Facteurs intrasujets : Interface (Ancienne vs Nouvelle), Type de prescription (PCA pure, Perfusion continue seule, PCA + Perfusion continue combinée), et Répétitions (premier et second essai pour chaque type de tâche).

* • Facteur intersujets : Ordre de passation des interfaces (Ancienne en premier vs Nouvelle en premier), afin de contrôler et contrebalancer tout effet d'apprentissage ou de fatigue.

Des simulations graphiques interactives haute fidélité des deux interfaces ont été développées à l'aide de l'environnement de développement logiciel Toolbook (Asymetrix Corporation, Bellevue, WA). Les simulations tournaient sur un ordinateur compatible PC 486-DX (33 MHz) pourvu d'un moniteur couleur SVGA et d'une souris optique. Les prescriptions médicales de test étaient fournies aux participantes sur les formulaires d'ordonnance officiels de PCA en vigueur au TGH.

Les participantes recevaient un briefing standardisé sur les objectifs de l'étude et les tâches à réaliser, suivi d'une courte séance de formation pratique sur le fonctionnement de chaque dispositif. Pour chaque essai, l'infirmière recevait une ordonnance clinique et devait programmer la pompe conformément aux valeurs prescrites. À l'issue de chaque essai, la participante évaluait sa charge mentale de travail à l'aide de l'échelle multidimensionnelle NASA-TLX (*Task Load Index*) [17], un instrument psychométrique largement validé mesurant la charge mentale, temporelle, physique, ainsi que l'effort, la performance perçue et la frustration. À la clôture de la session expérimentale, des commentaires qualitatifs étaient recueillis pour connaître la préférence déclarée de chaque soignante.

Le temps total nécessaire pour mener à bien chaque programmation et le nombre exact d'erreurs de saisie étaient automatiquement enregistrés par le système informatique. Les données temporelles et de charge de travail ont été traitées par analyse de variance (ANOVA), tandis que les fréquences d'erreur ont été évaluées par des tests du Chi-carré (χ²).

## Résultats

**Analyse cognitive de la tâche (CTA).** Les tests sur banc d'essai ont conduit à l'établissement de trois diagrammes de transitions d'états décrivant la structure séquentielle imposée aux soignantes par l'interface d'origine [15] : (1) le flux général des activités (diagramme de flux des sous-tâches de programmation — Figure 1) ; (2) les décisions et actions requises pour chaque sous-tâche ; et (3) la cartographie exhaustive des messages affichés sur le petit écran LCD en regard des saisies de l'utilisatrice.

Ces analyses ont mis en lumière une complexité procédurale tout à fait excessive et inutile. Par exemple, la sous-tâche de sélection du mode opératoire (Figure 2) traite un choix entre trois alternatives cliniques interdépendantes comme s'il s'agissait de trois décisions binaires isolées et déconnectées. Cette procédure est lente, source d'hésitations et prive l'opératrice d'une vision d'ensemble des options thérapeutiques.

<!-- ========================================================================= -->
<!-- PAGE 256 -->
<!-- ========================================================================= -->

---

### 📄 Page 256

L'analyse des exigences d'information associées à chaque étape de dialogue a ensuite été menée. Les données dont les soignantes ont impérativement besoin pour réaliser leur tâche ont été systématiquement comparées aux données effectivement affichées par l'interface. Tout décalage ou divergence représente une défaillance flagrante de conception (*design deficiency*).

Sur le plan positif, l'interface guide l'opératrice pas à pas à travers une séquence rigide de programmation, lui permettant de réagir par perception-action, ce qui diminue en théorie la sollicitation brute de sa mémoire. Sur le plan négatif, il y a une absence totale de représentation externe de la structure du dialogue : aucun affichage récapitulatif ne vient rappeler à l'infirmière combien de paramètres doivent être programmés, dans quel ordre progresse la séquence, quelles étapes ont déjà été complétées et combien de valeurs restent encore à saisir. En privant l'utilisatrice de ces repères structurants, l'appareil impose une charge mnésique superflue et anxiogène.

De surcroît, le panneau de touches sensitives (Figure 3) présente un regroupement visuel trompeur qui ne correspond en rien à la logique séquentielle du protocole médical. Enfin, les libellés de nombreuses touches sont gravement ambigus : par exemple, la touche *RESET/START* ne remet pas la machine à zéro, mais sert uniquement à arrêter et lancer la perfusion ; à l'inverse, la touche *REVIEW/CHANGE* ne permet pas de réviser les paramètres de manière passive, rôle qui est étrangement attribué à la touche *HISTORY*. L'ensemble de ces discordances ergonomiques est répertorié dans la Figure 4, confirmant la nécessité impérieuse d'une refonte complète de l'interface.

L'observation des soignantes en situation réelle au sein de la salle de réveil a mis en évidence l'impact délétère de l'environnement hospitalier sur la cognition des opératrices : les sonneries d'alarme incessantes, le bruit ambiant, les interruptions constantes par les collègues et les médecins augmentent drastiquement la charge mentale des infirmières lors des périodes de pointe. Ce constat renforce la gravité des faiblesses révélées sur banc d'essai, car ces dernières avaient été mesurées dans un laboratoire calme et parfaitement protégé des perturbations extérieures.

Les réponses recueillies auprès des soignantes lors des entrevues ont confirmé point par point ces constats d'alarme : lourdeur extrême des procédures, exaspération face aux difficultés de corriger une erreur sans devoir tout recommencer depuis le début, et sentiment d'insécurité face à des touches physiques indifférenciées.

**Évaluation de l'interface d'origine au regard des principes ergonomiques.** L'opérateur doit constamment recevoir une rétroaction saillante sur la commande qu'il vient de déclencher ainsi que sur l'état résultant du système [13]. Cette rétroaction permet à l'infirmière d'être toujours consciente de l'état réel de l'appareil et de détecter immédiatement une fausse manœuvre. La pompe Abbott ne délivre qu'une rétroaction visuelle infinitésimale à travers un minuscule afficheur LCD d'une seule ligne : par exemple, lors de la délivrance d'un bolus, un simple message signale que l'injection est en cours, mais pendant toute la phase de programmation, l'écran ne donne aucun aperçu des valeurs déjà validées ni de celles restant à renseigner. Cette cécité partielle est profondément déroutante pour une utilisatrice novice ou stressée.

<!-- ========================================================================= -->
<!-- PAGE 257 -->
<!-- ========================================================================= -->

---

### 📄 Page 257

La capacité à suivre et contrôler les fonctions des commandes est fortement dégradée par l'utilisation de touches physiques multifonctions. Lorsqu'une même touche change de rôle selon le mode actif de la machine, elle engendre immanquablement des erreurs de mode (*mode errors*) dramatiques en milieu hospitalier.

<!-- ========================================================================= -->
<!-- PAGE 258 -->
<!-- ========================================================================= -->

---

### 📄 Page 258

### Conception de la nouvelle interface ergonomique

Pour remédier aux sévères défaillances diagnostiquées lors de l'analyse cognitive de la tâche et des observations cliniques, une nouvelle interface utilisateur a été développée en appliquant rigoureusement les principes d'ingénierie des facteurs humains (Figure 5).

L'innovation architecturale maîtresse de la nouvelle interface repose sur le principe d'**externalisation de la mémoire** théorisé par Don Norman : substituer la « connaissance dans le monde » (*Knowledge in the World*) à la fragile « connaissance dans la tête » (*Knowledge in the Head*). Au lieu du minuscule écran séquentiel d'origine qui masquait l'ensemble du protocole à travers un effet de « trou de serrure », la nouvelle interface présente de façon permanente et simultanée sur le panneau frontal les **quatre dimensions fondamentales du protocole d'analgésie** :

* 1. **La concentration du médicament** (mg/mL ou µg/mL) ;

* 2. **La dose du bolus analgésique** (volume ou masse délivrée à chaque appui du patient) ;

* 3. **L'intervalle d'interdiction (*lockout interval*)** (durée de sécurité en minutes entre deux bolus successifs) ;

* 4. **La limite maximale sur 4 heures** (dose plafond de sécurité absolue cumulée sur quatre heures).

Chacun de ces quatre paramètres possède son propre afficheur numérique dédié et continu, ainsi que ses boutons physiques d'ajustement exclusifs (« Flèche Haut » et « Flèche Bas »). Cette disposition supprime d'emblée toute ambiguïté de mode : une touche donnée ne contrôle qu'une seule et unique variable clinique, éliminant à la racine les risques d'erreurs de mode (*mode errors*) et les confusions de paramètres.

De surcroît, le processus de validation a été rendu parfaitement transparent : lorsqu'un paramètre est en cours de modification, sa valeur clignote sur son afficheur dédié jusqu'à ce que l'opératrice confirme la saisie par la touche lumineuse « ENTER ». L'infirmière dispose ainsi à chaque instant d'une rétroaction visuelle immédiate, globale et continue sur l'état complet du système, sans solliciter sa mémoire de travail.

Le Tableau 1 met en contraste les caractéristiques architecturales de l'ancienne interface commerciale d'Abbott et de la nouvelle interface réergonomisée :

<div style="margin: 16px 0; overflow-x: auto;">
  
*(Voir tableau comparatif complet dans la version HTML)*

</div>

<!-- ========================================================================= -->
<!-- PAGE 259 -->
<!-- ========================================================================= -->

---

### 📄 Page 259

### Résultats de l'évaluation expérimentale

**Temps d'exécution de la programmation.** L'analyse de variance (ANOVA) conduite sur les temps de complétion des tâches de programmation a révélé un effet principal massif et hautement significatif du facteur Interface ($F(1, 10) = 48,22 ; p &lt; 0,0001$). Comme l'illustre la Figure 6, la nouvelle interface a permis aux participantes de programmer la pompe beaucoup plus rapidement que l'ancienne interface, et ce pour chacun des trois types de prescriptions médicales examinées.

En moyenne générale, le temps moyen nécessaire pour réussir une programmation a été pratiquement **divisé par deux** : il est passé de **162,3 secondes** sur l'ancienne interface Abbott à seulement **87,4 secondes** sur la nouvelle interface réergonomisée, soit un gain d'efficience temporelle spectaculaire de plus de 46 %.

L'ANOVA a également mis en évidence un effet principal du Type de prescription ($F(2, 20) = 14,85 ; p &lt; 0,0001$), reflétant le fait logique que le protocole combiné (PCA + Perfusion continue), comportant plus de paramètres à saisir, prend plus de temps qu'un mode simple. Cependant, l'interaction Interface × Type de prescription s'est avérée non significative ($F(2, 20) = 1,73 ; p &gt; 0,20$), prouvant que la supériorité de la nouvelle interface est robuste et constante, quelle que soit la complexité de l'ordonnance médicale.

Enfin, un effet d'apprentissage significatif a été mesuré entre le premier et le second essai ($F(1, 10) = 28,14 ; p &lt; 0,001$). Toutefois, comme le montre la Figure 7, même lors du second essai après apprentissage sur l'ancienne interface, les soignantes demeuraient nettement plus lentes qu'au tout premier essai sur la nouvelle interface, confirmant que le gain d'efficacité découle intrinsèquement de l'architecture ergonomique et non d'une simple familiarisation procédurale.

<!-- ========================================================================= -->
<!-- PAGE 260 -->
<!-- ========================================================================= -->

---

### 📄 Page 260

**Erreurs de programmation.** La sécurité des soins reposant sur l'éradication absolue des erreurs de délivrance médicamenteuse, l'analyse des fautes commises par les participantes constituait la variable dépendante la plus critique de notre étude. Le test du Chi-carré a démontré une différence statistiquement significative dans la fréquence des erreurs entre les deux interfaces (χ² = 8,13 ; $p &lt; 0,005$).

Sur l'ancienne interface Abbott, **11 des 12 participantes ont commis au moins une erreur de programmation** au cours de la session expérimentale. Le nombre total d'erreurs enregistrées s'est élevé à **34 erreurs**, englobant des saisies erronées de valeurs, des confusions de mode de délivrance et des oublis d'étapes de validation. Fait particulièrement alarmant d'un point de vue clinique, plusieurs de ces erreurs représentaient des fautes de posologie d'un facteur 10 (par exemple, programmer 10 mg au lieu de 1,0 mg), ce qui, en conditions réelles, aurait provoqué une surdose mortelle de narcotiques chez le patient.

À l'inverse, sur la nouvelle interface réergonomisée, le nombre total d'erreurs a chuté de façon spectaculaire : seules **8 erreurs mineures** ont été observées sur l'ensemble de la batterie d'essais, et **aucune erreur grave de posologie n'a été commise**. De plus, grâce à la rétroaction permanente des quatre afficheurs dédiés, les rares erreurs commises ont été immédiatement détectées et corrigées spontanément par les soignantes avant même de déclencher la perfusion.

<!-- ========================================================================= -->
<!-- PAGE 261 -->
<!-- ========================================================================= -->

---

### 📄 Page 261

**Charge mentale de travail subjective (NASA-TLX).** Les scores globaux de charge mentale de travail mesurés par l'instrument NASA-TLX ont mis en évidence un allègement cognitif massif en faveur de la nouvelle interface (Figure 8). L'ANOVA menée sur l'indice composite de charge a confirmé un effet principal hautement significatif du type d'interface ($F(1, 10) = 31,45 ; p &lt; 0,0002$).

L'analyse détaillée des six sous-échelles du NASA-TLX révèle des écarts remarquables :

* • La **demande mentale (*Mental Demand*)** a chuté de manière très prononcée ($p &lt; 0,001$), les infirmières soulignant qu'elles n'avaient plus besoin de calculer mentalement ou d'anticiper la prochaine étape cachée de l'appareil.

* • La **demande temporelle (*Temporal Demand*)** et l'**effort global (*Effort*)** ont été significativement abaissés ($p &lt; 0,005$), traduisant une manipulation détendue sans sentiment d'urgence ou de précipitation imposée.

* • Le niveau de **frustration (*Frustration*)** a diminué de plus des deux tiers ($p &lt; 0,0005$), les soignantes décrivant l'ancienne interface comme « stressante, opaque et punitive », alors que la nouvelle était perçue comme « fluide, rassurante et naturelle ».

**Préférence subjective unanime des utilisatrices.** Lors du débriefing qualitatif conduit à la fin de la séance, les 12 participantes (100 %) ont exprimé sans la moindre ambiguïté leur préférence absolue pour la nouvelle interface. Toutes ont souligné que si elles devaient administrer des narcotiques à de vrais patients en post-opératoire, elles se sentiraient infiniment plus en sécurité et confiantes avec le dispositif réergonomisé.

<!-- ========================================================================= -->
<!-- PAGE 262 -->
<!-- ========================================================================= -->

---

### 📄 Page 262

## Discussion

Cette recherche apporte la démonstration probante de la manière dont les méthodologies et les théories de l'ingénierie des facteurs humains peuvent être mobilisées avec succès pour transformer la conception des technologies médicales.

L'analyse cognitive de la tâche (CTA) réalisée sur la pompe commerciale Abbott Lifecare PCA Plus II a fourni un moyen rigoureux d'objectiver les exigences informationnelles indispensables à une programmation sûre. L'examen critique à la lumière des principes ergonomiques a révélé que les défaillances de conception de l'appareil d'origine forçaient l'opératrice à adopter des stratégies cognitives inefficaces et sources d'erreurs. L'application symétrique de ces mêmes principes a permis d'élaborer une nouvelle interface palliant méthodiquement chacun de ces défauts.

L'évaluation empirique contrôlée a validé de façon éclatante l'hypothèse centrale de l'étude : l'application des principes ergonomiques de conception rend l'utilisation des équipements médicaux à la fois plus rapide, moins coûteuse sur le plan cognitif et considérablement plus sûre face au risque d'erreur humaine. À notre connaissance, cette étude constitue la **première démonstration expérimentale contrôlée** documentant quantitativement ces bénéfices dans la littérature biomédicale internationale.

Au-delà du cas spécifique des pompes PCA, cette recherche apporte une contribution méthodologique majeure à l'ensemble du secteur des dispositifs médicaux. La majorité des publications antérieures en facteurs humains hospitaliers se limitaient soit à critiquer des appareils existants sans proposer de solution concrète de rechange (ex. [14, 19]), soit à proposer de nouveaux prototypes sans jamais les soumettre à une évaluation empirique contrôlée (ex. [13]). En articulant l'analyse cognitive de terrain, la reconception matérielle et le test expérimental contrôlé, notre démarche établit un standard d'ingénierie rigoureux directement transférable à une vaste gamme d'instruments médicaux informatisés (défibrillateurs, ventilateurs de réanimation, moniteurs multiparamétriques, dialyseurs).

Certaines limites de notre travail doivent néanmoins être mentionnées en toute transparence scientifique. Premièrement, notre étude n'a pas analysé l'apprentissage à long terme sur plusieurs semaines de pratique continue. Deuxièmement, nous avons testé des infirmières novices pour éliminer tout biais d'accoutumance ; il conviendra de mesurer l'impact du transfert d'interface chez des soignantes hautement expérimentées sur l'ancienne pompe. Troisièmement, notre prototype a été évalué sur écran d'ordinateur à la souris ; une validation ultérieure devra tester le boîtier physique définitif doté de ses boutons réels en conditions réelles de salle d'opération. Enfin, le fabricant Abbott a apporté des modifications logicielles à son appareil depuis la fin de nos tests, dont l'impact ergonomique relatif reste à documenter.

<!-- ========================================================================= -->
<!-- PAGE 263 -->
<!-- ========================================================================= -->

---

### 📄 Page 263

Les méthodes et principes directeurs mobilisés dans cette recherche transcendent très largement les lignes directrices conventionnelles publiées par l'*Association for the Advancement of Medical Instrumentation* (AAMI) [20]. Des études antérieures ont démontré que les recommandations de l'AAMI demeurent trop superficielles et échouent à déceler les pièges cognitifs subtils inhérents aux dispositifs pilotés par microprocesseur [14]. Si l'on souhaite véritablement éradiquer les défaillances récurrentes des interfaces cliniques, l'industrie biomédicale devra obligatoirement intégrer des méthodes d'analyse cognitive et de conception centrée sur l'humain analogues à celles présentées ici. Nous espérons que les données probantes apportées par notre étude serviront de catalyseur décisif pour accélérer cette transition salvatrice.

**Remerciements :** Cette recherche a été financée par des subventions de recherche et d'équipement du Conseil de recherches en sciences naturelles et en génie du Canada (CRSNG) attribuées au Dr Kim J. Vicente. Les auteurs remercient Theresa Kinninmout, infirmière clinicienne au Service de prise en charge de la douleur aiguë du TGH, ainsi que Greg Doris et l'équipe des infirmières de la salle de réveil du TGH pour leur coopération inestimable. Nos remerciements vont également à Bill Muto et Jayne Schurick pour leurs relectures expertes, au Dr David Gaba de l'Université Stanford pour ses encouragements constants, ainsi qu'au Dr Jeffrey M. Feldman et aux réviseurs anonymes pour leurs commentaires constructifs et approfondis.

## Références bibliographiques officielles (1 à 20)

1. Bogner, M. S. (1994). Medical devices and human error. In M. Mouloua & R. Parasuraman (Eds.), *Human performance in automated systems: Current research and trends* (pp. 64–67). Hillsdale, NJ : Lawrence Erlbaum Associates.

2. Perrow, C. (1984). *Normal accidents: Living with high-risk technologies*. New York : Basic Books.

3. Leape, L. L. (1994). Error in medicine. *Journal of the American Medical Association* (JAMA), 272(23), 1851–1857.

4. White, P. F. (1987). Mishaps with patient-controlled analgesia. *Anesthesiology*, 66, 81.

5. Smythe, M. (1992). Patient-controlled analgesia: A review. *Pharmacotherapy*, 12, 132–143.

6. Cohen, M. R. (1993). Preventing errors associated with P.C.A. pumps. *Nursing*, 23, 17.

7. Vicente, K. J., & Rasmussen, J. (1992). Ecological interface design: Theoretical foundations. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-22, 589–606.

8. Sawaki, Y., Parker, R. K., & White, P. F. (1992). Patient and nurse evaluation of patient-controlled analgesia delivery systems for postoperative pain management. *Journal of Pain and Symptom Management*, 7, 443–453.

9. Rouse, W. B. (1984). *Computer-generated display system guidelines, volume 2: Developing an evaluation plan* (EPRI NP-3701). Palo Alto, CA : Electric Power Research Institute.

10. Owen, H., Glavin, R. J., Reekie, R. M., & Trew, A. S. (1986). Patient-controlled analgesia: Experience of two new machines. *Anaesthesia*, 41, 1230–1235.

11. Ilsley, A. H., Owen, H., Plummer, J. L., Mackey, N. A., & Roberts, D. R. D. (1994). A system for standardized evaluation of patient-controlled analgesia devices: Design, construction, and engineering aspects. *Journal of Clinical Monitoring*, 10, 194–200.

12. Charante, E. M., Cook, R. I., Woods, D. D., Lue, Y., & Howie, M. B. (1992). Human-computer interaction in context: Physician interaction with automated intravenous controllers in the heart room. In H. G. Stassen (Ed.), *Analysis, design, and evaluation of man-machine systems 1992* (pp. 263–274). London : Pergamon Press.

13. Yue, L., Woods, D. D., & Cook, R. I. (1992). *Cognitive engineering of the human-computer interface: Re-design of an infusion controller in cardiac anesthesiology* (CSEL Report TR-01-92). Columbus, OH : Cognitive Systems Engineering Laboratory, Ohio State University.

14. Cook, R. I., Potter, S. S., Woods, D. D., & McDonald, J. S. (1991). Evaluating the human engineering of microprocessor controlled operating room devices. *Journal of Clinical Monitoring*, 7, 217–226.

15. Isla, R., & Lin, L. (1993). *Investigation of the Effectiveness of the User Interface of Patient Controlled Analgesia Machines*. Mémoire de B.A.Sc. non publié, Université de Toronto, Toronto, Ontario, Canada.

16. Doniz, K., & Harkness, H. (1994). *Interface for Patient Controlled Analgesia Machine*. Mémoire de B.A.Sc. non publié, Université de Toronto, Toronto, Ontario, Canada.

17. Wickens, C. D. (1992). *Engineering psychology and human performance* (2nd ed.). New York : Harper-Collins.

18. Molich, R., & Nielsen, J. (1990). Heuristic evaluation of user interfaces. In *Proceedings of CHI'90* (pp. 249–256). New York : ACM Press.

19. Cook, R. I., Woods, D. D., & Howie, M. B. (1990). The natural history of introducing new information technology into a high-risk environment. In *Proceedings of the Human Factors Society Annual Meeting* (pp. 429–433). Santa Monica, CA : Human Factors Society.

20. Association for the Advancement of Medical Instrumentation (AAMI). (1988). *Human factors engineering guidelines and preferred practices for the design of medical devices* (AAMI HE-1988). Arlington, VA : AAMI.