Verdict

Les deux axes sont exploitables, mais les deux dossiers bruts doivent être corrigés avant la remise. L’AF447 transforme une limitation du retour d’information en disparition certaine de la conscience partagée. Le dossier Lin confond une mesure comportementale de reprise, une théorie de la résilience et une garantie de sécurité que les données ne permettent pas d’établir. Le contrôle porte sur le fichier figé au commit c4b8224. 
GitHub

Je retiens une question sur la coordination des commandes pour AF447 et une question sur la revalidation après interruption pour Lin, avec un fait initial plus précis et des effets à évaluer plutôt que des bénéfices présupposés.

Télécharger l’audit consolidé, les relances et la feuille finale — ZIP

Ouvrir la feuille d’une page, prête à imprimer — PDF

L’archive contient le rapport détaillé, les textes modifiables et le PDF. Les relances restent dans les notes de préparation, pas sur la feuille de remise.

Point préalable : l’exclusivité annoncée n’est pas établie

L’axe des mini-manches et de la conscience partagée figurait déjà dans l’axe A de la première banque DeepThink. Les nouvelles propositions ne peuvent donc pas être qualifiées de totalement inédites par rapport à cette banque. Le fichier actuel est lui-même accessible publiquement. 
GitHub
+1

Les formulations corrigées ci-dessous se distinguent des deux précédentes questions finales — signal d’indisponibilité de l’alarme et effet de la vue d’ensemble — mais cela ne garantit pas qu’un autre étudiant ne choisira pas un angle voisin. Pour limiter une diffusion supplémentaire, garde ce nouveau dossier hors du dépôt public.

1. Format : trois phrases présentes, durée trop optimiste

J’ai compté les trois segments, sans leurs étiquettes, en conservant les mots avec apostrophe ou trait d’union comme une unité et en excluant la ponctuation isolée.

Proposition brute	Constat / concept / question	Total réel	Durée calculée à 150 mots/min
AF447	14 / 12 / 13	39 mots	15,6 s
Lin	13 / 14 / 14	41 mots	16,4 s

Les valeurs annoncées de 37 et 38 mots ne correspondent pas à ce comptage. Les textes sont bien plus courts que ceux des premières passes, mais leur durée déclarée de treize secondes laisse trop peu de place aux pauses et aux termes techniques. 
GitHub

Ce n’est pas un motif pour les rejeter à lui seul. Les défauts de fond sont plus importants que les deux ou trois mots excédentaires. Les remplacements finaux font respectivement 30 et 32 mots, sans accélération artificielle nécessaire dans le calcul de référence.

Autre correction de méthode : un compromis réel n’a pas besoin d’être déclaré “inconciliable”. Demander à l’expert comment comparer deux exigences potentiellement concurrentes est plus solide que lui imposer une incompatibilité déjà décidée.

2. AF447 — Un problème d’observabilité, pas une preuve de destruction de la conscience partagée
Le constat doit être resserré

Le fait défendable est l’absence de liaison mécanique entre les mini-manches. Cependant, leur indépendance ne signifie pas absence de toute information ou de tout mécanisme de coordination : Airbus décrit la sommation des entrées, la signalisation des actions simultanées et la prise de priorité. 
Scribd

Le BEA relève la difficulté d’observer les actions de l’autre pilote. Il décrit aussi des positions du mini-manche à cabrer ou neutres : la présentation d’un ordre uniformément continu à cabrer est trop forte. 
Scribd
+1

Conséquence pour la question : partir de l’architecture des commandes, puis interroger ce qu’un retour supplémentaire permettrait effectivement de mieux comprendre. Ne pas présenter comme démontré qu’un couplage aurait empêché l’accident.

Endsley est pertinent, mais le lien causal est suraffirmé

La conscience partagée concerne les informations qui doivent être communes lorsque les responsabilités se recouvrent. Elle ne signifie ni que les équipiers savent tous exactement la même chose, ni qu’un canal sensoriel particulier est nécessaire et suffisant à cette compréhension. L’Article D fourni présente cette distinction en citant Endsley. 

D_Conscience_de_la_situation

Le problème de la formulation brute est donc son caractère catégorique : elle déduit directement une dégradation globale de la conscience partagée de l’absence de couplage. 
GitHub

Une formulation rigoureuse doit distinguer :

Ce que le dispositif rend perceptible ; ce que le pilote en comprend ; ce qu’il suppose des intentions de son collègue.

Sentir un mouvement ne suffit pas à connaître son intention. Le GOLD rappelle précisément que l’observation du comportement ne révèle pas, à elle seule, son pourquoi. 
GitHub

Le scénario de saturation totale n’est pas une donnée établie

Le développement suppose que les autres canaux deviennent entièrement inutilisables et que le retour corporel permettrait une compréhension sans attention dirigée. Ce mécanisme n’est pas documenté dans le dossier. 
GitHub

Il faut en faire une hypothèse à éprouver, non le point de départ de l’évaluation. La question intéressante est justement de savoir dans quelles conditions un retour haptique apporte une information utile, lorsqu’il distrait, et lorsqu’il pourrait provoquer une action incorrecte.

De même, une nuit simulée et plusieurs pannes ne constituent pas, par leur seule présence, une mesure de « charge allostatique ». Il faut définir les exigences du scénario et ce que les mesures retenues permettront réellement de conclure.

Le dilemme matériel est trop étroit

L’opposition entre allègement mécanique et transparence cognitive présuppose une comparaison de masse, de maintenance et de performance qui n’est pas fournie. La solution ne se réduit pas nécessairement à choisir entre une tringlerie lourde et aucun retour.

Je propose de déplacer le compromis vers l’usage :

Améliorer la connaissance des actions du collègue sans perturber la commande ni la prise de priorité.

Cela ouvre une comparaison entre plusieurs formes de retour, sans présumer que la solution active sera préférable.

La relance corrigée doit permettre de rejeter la solution

Le protocole proposé devrait examiner une amélioration possible, mais aussi une information haptique erronée ou indisponible, une prise de priorité et des mouvements involontaires. Il faut mesurer la justesse de la coordination, pas seulement la rapidité.

Une double entrée n’est d’ailleurs pas nécessairement une opposition entre pilotes : des commandes simultanées peuvent aller dans le même sens. 
Scribd

Enfin, aucun résultat de simulateur ne permet, à lui seul, de déclarer inévitable une décision réglementaire. Le déploiement doit rester une étape de validation, pas une injonction politique ou administrative présupposée.

3. Lin — Remplacer le débat général sur les limites par une difficulté réellement décrite
Le constat initial n’est pas un résultat de Lin

L’étude comporte une analyse de tâches avec observations de terrain, puis une comparaison de deux interfaces simulées auprès de douze étudiants en soins infirmiers. La démarche ne se limite donc pas à un laboratoire déconnecté du terrain. Le protocole expérimental ne compare pas des limites dures et douces sous interruptions contrôlées. 
Springer
+1

Pour donner à la nouvelle question un ancrage propre au texte, je retiens REVIEW/CHANGE. Lin décrit une commande qui permet de revenir en arrière pendant la programmation, mais fait progresser dans une séquence de révision après sa réalisation, avec d’autres incohérences de retour. 
ResearchGate

Ce fait permet de poser une question sur la reprise et la vérification, sans inventer un effet expérimental d’interruptions.

L’interruption et la revalidation deviennent les conditions d’une étude complémentaire proposée, pas des manipulations attribuées à Lin.

Le resumption lag est correctement attribué dans le développement, mais mal interprété

Il faut reconnaître ce qui est déjà juste : DeepThink nomme Altmann et Trafton, pas Hollnagel, lorsqu’il évoque explicitement le délai de reprise. 
GitHub

La correction porte sur la mesure. Altmann et Trafton définissent opérationnellement ce délai comme l’intervalle entre la fin de la tâche secondaire et la première action ultérieure dans la tâche principale. Ce n’est pas une mesure directe d’une récupération cognitive complète. 
eScholarship

La première action peut être incorrecte. Une reprise plus lente peut aussi comporter une vérification utile. Il faut donc distinguer, dans le protocole proposé :

Délai jusqu’au premier geste ; délai jusqu’à une reprise correcte ; erreurs et omissions ; durée totale de la tâche.

Réduire le seul délai de reprise pourrait faire paraître meilleure une interface qui encourage à agir vite sans avoir correctement retrouvé l’état du système.

Hollnagel ne fournit pas une preuve de supériorité des limites douces

La résilience, dans la présentation de Hollnagel consultée, mobilise des capacités de réponse, de surveillance, d’apprentissage et d’anticipation. Elle ne se réduit pas au droit de contourner une règle ou à la suppression de contraintes. 
Syddansk Universitet

Deux assimilations doivent donc disparaître :

Adaptation humaine ≠ adaptation nécessairement sûre.
Fonction de forçage ≠ obstacle nécessairement nuisible.

Une barrière peut prévenir une classe d’erreurs tout en créant d’autres difficultés. C’est précisément ce qu’il faut comparer, sans décider d’avance que la flexibilité est supérieure.

Les limites dures ne rendent pas toute surdose impossible

Les recommandations de l’ISMP décrivent des limites qui empêchent de poursuivre une programmation au-delà de seuils définis. Elles soulignent aussi l’importance de la configuration et de la sélection appropriée des paramètres. Cette protection ne couvre pas automatiquement toutes les erreurs possibles. 
ECRI and ISMP

Un contre-exemple logique suffit : une valeur incorrecte restant dans l’intervalle admis ne sera pas rejetée pour dépassement de cet intervalle.

Cette référence sur les pompes intelligentes est un complément postérieur, pas la description d’un essai réalisé par Lin en 1998.

Pour éviter de transformer la discussion en opposition générale entre sécurité et flexibilité, je recommande d’évaluer une revalidation ciblée après interruption, à limites de dose inchangées. On teste ainsi l’effet de la vérification sans supprimer les protections cliniques pour les besoins de l’argument.

La relance ne doit pas attribuer d’avance une intention au personnel

La recherche d’un seuil exact où une infirmière déciderait d’un contournement présuppose déjà son motif, son choix et une régularité individuelle universelle. Ce seuil n’est pas établi dans les sources examinées. 
GitHub

La bonne question est : quelles données feraient retenir ou rejeter une étape obligatoire de revalidation ? Les adaptations observées doivent être analysées selon leur contexte et leurs effets, plutôt que classées d’avance comme sabotage ou comme preuve de résilience.

4. Justification corrigée selon les quatre étapes

Le GOLD demande de distinguer les comportements de leurs explications, de choisir les mesures en fonction des objectifs, de chercher les conséquences imprévues et de vérifier l’application dans le contexte visé. 
GitHub
+2
GitHub
+2

La matrice suivante constitue une proposition de travail pour le séminaire, non une reconstitution des méthodes historiques du BEA ou de Lin.

Étape	AF447	Lin
Comprendre	Reconstituer les commandes, indications, annonces et transferts de priorité ; identifier l’information utile à chaque rôle.	Observer les interruptions, les états de programmation et les stratégies de reprise ; distinguer reprise rapide et reprise correcte.
Concevoir	Définir l’information transmise par le retour haptique et ses effets possibles sur la commande.	Comparer une aide à la reprise et une revalidation obligatoire, avec les mêmes informations et limites de dose.
Évaluer	Tester aussi des retours absents ou erronés ; mesurer coordination correcte, délais et actions involontaires.	Comparer les conditions avec et sans interruption ; mesurer erreurs, récupération, retards et validations sans vérification effective.
Déployer	Examiner intégration, modes de panne, formation, maintenance et suivi des usages.	Vérifier le transfert sur dispositif physique et auprès des utilisateurs visés, puis les effets organisationnels et les critères de révision.

Il ne faut ni disqualifier le laboratoire ni confondre un résultat sur prototype avec une preuve de sécurité en exploitation. Cañas présente précisément la comparaison des variantes et le compromis entre contrôle expérimental et validité écologique. 

1-CANAS2011(CHAP-13-humanFactor)

Le rapport fournit les huit paragraphes de remplacement — quatre par dossier — pour empêcher qu’une formulation courte correcte soit accompagnée d’une justification encore excessive.

5. Formulations finales pour la remise
Question 1 — AF447 : coordination et retour haptique

Sur AF447, les mini-manches ne sont pas mécaniquement couplés. Cela interroge la conscience partagée d’Endsley. Comment tester un retour haptique pour améliorer la coordination sans gêner la reprise de priorité ?

30 mots — environ 12 secondes à 150 mots/minute, avant les pauses.

Le constat porte sur l’architecture documentée des commandes. L’application du cadre d’Endsley et la valeur du retour haptique restent des propositions d’analyse et d’évaluation, pas des conclusions causales attribuées au BEA. 
Scribd
 

D_Conscience_de_la_situation

Relance orale, destinée au professeur demandé :

Professeur Passalacqua, quel protocole permettrait de décider si un retour haptique apporte un bénéfice net, lorsque l’on teste aussi un signal erroné, son indisponibilité et une reprise de priorité ?

Cette relance oblige à discuter les conditions d’échec de la solution, plutôt qu’à approuver un bénéfice annoncé.

Question 2 — Lin et al. : reprise et revalidation

Chez Lin, REVIEW/CHANGE change de fonction selon l’étape. Le délai de reprise après interruption reste à évaluer. Comment tester une revalidation obligatoire des réglages sans retarder les soins ni favoriser les contournements ?

32 mots — environ 12,8 secondes au même débit, avant les pauses.

Le comportement de REVIEW/CHANGE est documenté dans l’article. Le délai de reprise est défini par la littérature complémentaire ; la revalidation après interruption est une étude proposée, pas un résultat de 1998. Cette distinction apparaît aussi dans la note du PDF. 
ResearchGate
+1

Relance orale :

Professeur Passalacqua, à guidage et limites de dose identiques, quels résultats vous feraient retenir ou rejeter une revalidation obligatoire après interruption, en considérant les erreurs, les retards et les contournements ?

Cette formulation conserve le compromis entre vérification et continuité du soin, mais élimine la garantie de sécurité et le diagnostic préalable des intentions du personnel.

Décision de clôture

Les deux formulations corrigées sont utilisables pour la remise et la discussion. Les deux dossiers bruts ne sont pas validés. La modification de Lin est volontairement plus substantielle : elle remplace un débat général sur les limites par une propriété précise de l’interface, puis une question d’évaluation identifiable.

La validation porte sur la cohérence documentaire et rédactionnelle, pas sur une garantie de note, d’exclusivité ou d’efficacité technique. La durée réelle doit encore être chronométrée à voix haute, notamment pour « AF447 » et « REVIEW/CHANGE ».

Le contrôle technique s’appuie sur les sections pertinentes d’une reproduction du rapport final du BEA et d’un article Airbus, ainsi que sur le texte de Lin déposé par un coauteur et sa notice éditeur. Le PDF officiel volumineux du BEA n’a pas été chargé intégralement dans cette passe. Les données individuelles, l’audio du cours et des performances humaines réelles n’ont pas été examinés.

Il n’est pas nécessaire de relancer une génération générale. Utilise les deux textes du PDF et les justifications corrigées, sans réintroduire les affirmations absolues du dossier initial.