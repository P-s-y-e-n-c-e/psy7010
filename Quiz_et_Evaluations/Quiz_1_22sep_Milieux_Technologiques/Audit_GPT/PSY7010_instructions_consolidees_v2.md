# PSY7010 — Consigne unique de correction et de validation — V2

**Destinataire : Gemini, agent de développement.**
**Statut : remplace intégralement `PSY7010_instructions_reaudit_9f2c30e.md`. Ne pas appliquer les deux versions.**
**Référence initiale :** commit `9f2c30e040b0d3a05d13d63ef9bb58b8929ce998`, « feat(quiz): academic audit overhaul, Bristol flashcards, desktop split fix & mobile UI ».
**Objet :** achever les corrections fonctionnelles et documentaires, intégrer les problèmes mobiles décrits par Michel, préserver le bureau et ce qui fonctionne déjà. Ce document contient toutes les consignes C01–C13 ; ce n’est pas un supplément à lire avec la version précédente.

## Mandat, périmètre et valeur des constats

Travailler sur le code courant. Si HEAD diffère du commit de référence, vérifier chaque constat avant modification. Ne pas restaurer l’ancien HTML et ne pas relancer aveuglément le premier correctif JSON : la banque a déjà fait l’objet de modifications. Conserver `doc_explanation` et `exam_tip`, les médias et les originaux anglais. Les corrections académiques détaillées du premier dossier servent de référence de données ; le présent document remplace la consigne technique de second passage.

Les points C01–C13 du réaudit précédent restent couverts. Cette V2 réécrit notamment C02, C03, C07, C11 et C12 à partir du retour d’usage de Michel. **En cas de contradiction avec une ancienne recommandation d’interface, cette V2 prévaut : le titre complet et la date restent visibles ; la mascotte, le message de mode et le sélecteur de section ne sont pas supprimés.**

**Origine des éléments :**
- Les constats du premier réaudit portent sur le commit indiqué et incluaient des essais isolés de fonctions. Ils ne sont pas présentés ici comme une nouvelle campagne de tests.
- Pour cette mise à jour, les règles mobiles, les éléments du formulaire, la pagination, la vue podcast et les fonctions de redimensionnement ont été relus dans le code public de `main` [S5]. Les mécanismes décrits dans les sections révisées y sont visibles.
- Le titre tronqué, la pagination en colonne, les espacements insuffisants et le défilement répétitif des cartes sont le **retour d’usage de Michel** [S6]. La cause exacte du dernier symptôme sur son téléphone n’est pas encore reproduite : distinguer mécanismes présents dans le code et hypothèse sur l’appareil.
- Le HTML déployé complet n’a pas pu être téléchargé dans l’environnement de cette mise à jour ; ne pas prétendre à une identité binaire entre `main`, le build servi et le cache du téléphone. Aucun test sur son appareil ni lecture audio de production n’a été réalisé ici. La validation réelle ci-dessous reste à exécuter.

**Sources et repères :**
- **[S1] Code de référence :** `https://raw.githubusercontent.com/P-s-y-e-n-c-e/psy7010/9f2c30e040b0d3a05d13d63ef9bb58b8929ce998/index.html`
- **[S2] Commit :** `https://github.com/P-s-y-e-n-c-e/psy7010/commit/9f2c30e040b0d3a05d13d63ef9bb58b8929ce998`
- **[S3]** Journal fourni « Texte collé.txt », notamment la collecte de console et les déclarations de livraison.
- **[S4]** Les cinq lectures originales et le dossier d’audit académique de Michel.
- **[S5] Code public relu pour cette V2 :** `https://raw.githubusercontent.com/P-s-y-e-n-c-e/psy7010/main/index.html` ; site : `https://p-s-y-e-n-c-e.github.io/psy7010/`. `main` est une référence mobile : noter le commit réellement modifié et testé.
- **[S6]** Description verbale de Michel dans la conversation : titre/date, pagination, formulaire Test, défilement Cartes, raccourcis et espacements Podcast.

Utiliser les identifiants, classes et noms de fonctions ci-dessous, non les numéros de lignes d’un extrait web. Les dimensions d’espacement proposées sont des **cibles de conception à vérifier**, pas des résultats de recherche ni des normes prétendument universelles.

## Ce qui doit rester visuellement inchangé

Michel juge satisfaisants les quatre boutons **Étude / Test / Cartes / Podcast**, le message du mode actif, l’image de la mascotte et le menu de filtrage par section. Conserver leur structure et leur présentation ; corriger seulement leurs éventuelles dépendances fonctionnelles ou leur accessibilité. Ne pas étendre la refonte à ces composants pour convenance technique.

La présentation de bureau demeure la référence de non-régression. Limiter les nouvelles règles visuelles mobiles à la condition compacte unifiée. Les seules retouches partagées autorisées sont les défauts explicitement visés (fonctionnement, références, géométrie verticale, accessibilité), avec comparaison avant/après.

## Résultat mobile à livrer

| Zone | Résultat exigé | Section |
|---|---|---|
| En-tête | Titre complet sur toute la largeur ; date sur la rangée suivante ; progression et Plus à droite de cette seconde rangée, sans recouvrir le titre. | C07.2, C01, C09 |
| Étude | Précédente — position / total — Suivante ; aucune colonne de petits numéros. Accès direct aux questions conservé. | C07.3 |
| Test | Espaces explicites entre titre, description, groupes de champs, libellés, menus et bouton Démarrer ; simulation réellement fonctionnelle. | C02 |
| Cartes | Défilement continu, pas de retour furtif, une face à la fois, navigation lisible ; aide clavier absente de la vue mobile normale. | C03, C07.1, C11 |
| Podcast | Pas de bouton rond Play redondant en haut ; conserver Écouter/Pause ; progression séparée des liens externes par un espace visible. | C12 |

---

# P0 — Corriger avant toute nouvelle déclaration de livraison

## C01 — Réparer les commandes du menu « Plus »

**Constat [S1].** Le HTML appelle `openOptionsModal()`, `closeOptionsModal()` et `updateOptionsModalThemeText()`. Ces fonctions ne sont pas définies dans le script examiné. Le document contient la boîte `optionsModal`, mais son existence ne rend pas ses boutons fonctionnels.

**Correction demandée.** Implémenter réellement l’ouverture, la fermeture et la synchronisation du thème, ou remplacer leurs appels par une implémentation commune complète. Aucun gestionnaire vide, aucune définition fictive destinée à faire passer un test `typeof`, aucun `try/catch` silencieux. À l’ouverture, synchroniser le thème réel ; à la fermeture, restituer le focus au bouton déclencheur. Ajouter un libellé accessible à la croix. Les commandes de disposition de bureau ne doivent pas modifier subrepticement la préférence grand écran depuis un téléphone.

**Acceptation.** À 390 px : cliquer « Plus », changer le thème, fermer avec la croix, rouvrir, fermer avec Échap, rouvrir, annuler une réinitialisation. Aucun `ReferenceError`, aucun focus perdu, aucun score supprimé lors d’une annulation. Tester aussi le clavier.

## C02 — Implémenter le mode Test complet, pas seulement son écran de paramètres

**Constat [S1].** Les boutons appellent `startSimulation()` et `restartSimulationMode()`, sans définition correspondante. Les variables `simQuestions`, `simCurrentIdx`, `simTimerInterval` et `simTimeRemaining` ne constituent pas un moteur de simulation. De plus, `selectOption()` et `nextQuestion()` continuent de rendre/naviguer la banque d’étude. Enfin, `setMobileView('activity')`, dans la branche simulation, masque `qCard` même lorsque `isSimulationActive` est vrai ; le retour peut donc masquer à la fois questions, paramètres et résultats.

**Correction demandée.** Donner à la simulation trois états explicites : `setup`, `running`, `results`. Isoler sa liste, ses réponses, son index et son échéance des données d’étude. Le rendu doit recevoir la question de la simulation et non relire implicitement `filteredQuestions[currentQuestionIndex]`.

Mettre en œuvre la sélection du nombre demandé de questions sans doublon, les choix de réponse, la navigation, la fin manuelle, la fin chronométrée, le calcul du score et la reprise d’une nouvelle simulation. Utiliser une échéance absolue pour le temps restant ; ne pas faire dépendre la durée réelle du nombre de déclenchements d’un intervalle. À chaque nouvelle simulation, arrêter l’ancien intervalle et ne créer qu’un seul minuteur. Une simulation non chronométrée ne doit pas disposer d’une échéance active.

En mode Test, différer corrigé, rétroactions et surlignage révélant la réponse jusqu’au bilan. Le statut des lectures autorisées doit être explicite ; ne pas prétendre reproduire une règle d’examen non documentée. Par défaut, ne pas ouvrir automatiquement une source qui révèle la solution. Les réponses d’une simulation ne doivent ni être préremplies par les réponses d’étude ni écraser celles-ci.

**Acceptation.** Terminer un test de cinq questions avec des choix connus, vérifier un score calculable, lancer un second test, vérifier absence de réponses héritées et de double minuteur. Tester cinq questions sans chronomètre et avec expiration accélérée en environnement de test. Pendant un test actif, ouvrir le podcast puis revenir : retrouver la même question et la même échéance. Refaire ce parcours après un changement de taille d’écran.


### C02.2 — Aérer le formulaire mobile sans changer ses choix

**Retour Michel [S6].** Le titre, « Simule le quiz… », les deux libellés, leurs menus et « Démarrer la simulation » se touchent presque. Il ne demande pas de réduire le texte, mais de séparer ses unités.

**Code [S5].** Les classes `.sim-title`, `.sim-desc`, `.sim-form-group`, `.sim-label` et `.sim-select` sont utilisées dans le HTML, mais ne disposent pas de règles dédiées dans la feuille examinée. Le reset global retire les marges. Les libellés ne sont pas reliés aux menus par `for`.

**Correction.** Sous la condition compacte commune de C07, donner au formulaire une présentation explicite. Garder les valeurs et libellés des options, sauf correction documentaire décidée ailleurs. Relier les labels à `simCountSelect` et `simTimerSelect`. Ajouter `id="simStartBtn"` et `type="button"` au bouton existant. Ne pas changer le nombre, la durée ou le comportement d’une simulation pour faciliter sa mise en page.

Cibles d’espacement à appliquer : marge intérieure 20 px ; titre vers description 12 px ; description vers premier groupe 24 px ; label vers menu 10 px ; premier groupe vers second 20 px ; second menu vers Démarrer 24 px. Texte courant 1rem et interligne 1,5 ; menus et boutons au moins 44 px de haut. Pas de hauteur fixe sur le formulaire.

Exemple **à intégrer dans le bloc compact consolidé**, en adaptant seulement les sélecteurs si le DOM est refactorisé. Ne pas ajouter une deuxième définition concurrente :

```css
/* À l'intérieur de l'unique condition compacte : */
#simSetupCard {
  padding: 1.25rem;
  border: 1px solid var(--border-color);
  border-radius: 0.875rem;
  background: var(--bg-card);
}
#simSetupCard .sim-title {
  margin: 0 0 0.75rem;
  font-size: 1.2rem;
  line-height: 1.35;
}
#simSetupCard .sim-desc {
  margin: 0 0 1.5rem;
  font-size: 1rem;
  line-height: 1.5;
}
#simSetupCard .sim-form-group { margin: 0; }
#simSetupCard .sim-form-group + .sim-form-group {
  margin-top: 1.25rem;
}
#simSetupCard .sim-label {
  display: block;
  margin-bottom: 0.625rem;
  line-height: 1.45;
}
#simSetupCard .sim-select {
  display: block;
  width: 100%;
  min-width: 0;
  min-height: 44px;
  padding: 0.75rem;
  font: inherit;
  font-size: 1rem;
  line-height: 1.4;
  color: var(--text-main);
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
}
#simStartBtn {
  margin-top: 1.5rem;
  min-height: 44px;
  width: 100%;
  justify-content: center;
  white-space: normal;
}
```

**Acceptation spécifique.** À 320, 390 et 430 px, titre et description sont distincts ; les deux labels restent associés à leur menu ; le dernier menu ne touche jamais Démarrer. Mesurer les rectangles après chargement de la police, en clair et en sombre. L’ensemble peut nécessiter de défiler : ne pas supprimer ses espaces pour imposer un seul écran.

## C03 — Séparer changement de vue, reprise d’activité et réinitialisation

**Constat [S1 ; reproductions isolées].** `setMode('study')` rappelle `filterCategory()`, qui remet l’index à zéro. `setMode('flashcards')` réinitialise le paquet et affiche la première carte. Le gestionnaire `resize` rappelle `setMobileView()`, qui met les positions de défilement à zéro. En quittant le mobile, `resize` restaure seulement quelques conteneurs : `qCard`, les bannières et d’autres éléments peuvent rester masqués par leurs styles en ligne. `returnToQuestionFromSource()` cherche `quizCard`, alors que le véritable identifiant est `qCard`.

**Correction demandée.** Conserver un état distinct pour l’activité (`study`, `flashcards`, `simulation`), la vue compacte (`activity`, `source`, `podcast`), la simulation et les positions de reprise. Ajouter une seule fonction de rendu de visibilité qui dérive les éléments visibles de cet état. La réutiliser au chargement, lors des changements de vue et au franchissement du seuil compact. Ne pas laisser des styles `display` contradictoires être écrits par plusieurs branches indépendantes.

Un clic sur l’activité courante doit être idempotent. Revenir du podcast reprend l’activité ; ce n’est pas une demande de nouveau paquet ou de retour à Q01. Réinitialiser seulement sur une action explicite — nouvelle simulation, nouveau filtre ou réinitialisation confirmée. Stocker les positions par activité et par document/langue avant de masquer les panneaux ; restaurer après leur réaffichage. Un redimensionnement ordinaire ne doit pas provoquer de retour en haut. Réévaluer le changement de présentation avec `matchMedia(...).change` ; réserver les ajustements de géométrie aux besoins réels de redimensionnement.

Réparer l’identifiant de retour, mais **ne pas se contenter** de remplacer `quizCard` par `qCard` en gardant le saut systématique en haut. Préserver aussi la face visible de la carte et l’ordre d’un paquet mélangé. Le bouton Retour du lecteur doit indiquer l’activité de destination lorsque celle-ci est une carte, et non toujours « questionnaire ».

**Acceptation.** Q13 → Podcast → Étude revient à Q13. Carte 11 retournée → source → retour conserve cette carte retournée. Changer uniquement la hauteur de la fenêtre ne change ni index, ni face, ni filtre. Passer mobile → bureau → mobile depuis chacune des trois vues ne fait disparaître aucune activité ni ressource. La navigation Précédente/Suivante doit, elle, replacer intentionnellement le début de la nouvelle question dans la zone lisible.


### C03.2 — Corriger le défilement répétitif du mode Cartes

**Symptôme rapporté [S6].** Après un geste pour faire défiler, la vue semble s’arrêter à « Précédente / Mélanger / Suivante ». Un autre geste donne l’impression de parcourir un écran mais réaffiche presque la même zone, puis les raccourcis. Ne pas conclure à une liste dupliquée sans l’avoir constaté dans le DOM.

**Mécanisme confirmé dans le code [S5].** Le gestionnaire `window.resize` appelle `setMobileView(mobileView)`. Cette fonction écrit systématiquement `scrollTop = 0` sur `document.documentElement`, `document.body` et `quizPane`, même lorsque la vue n’a pas changé. C’est un mécanisme de saut non demandé. Les barres du navigateur, le clavier virtuel et les changements de viewport sont des situations à instrumenter ; leur rôle exact dans l’incident décrit reste à établir. Ne pas confondre un événement `window.resize` avec un événement `visualViewport.resize`.

**Autres vérifications nécessaires.** La racine et plusieurs conteneurs portent des contraintes de hauteur ou d’overflow héritées ; vérifier leurs valeurs calculées, non seulement leur CSS écrit. Les règles mobiles neutralisent déjà la 3D : ajouter un autre `transform:none` n’est donc pas une correction suffisante. L’aide clavier est un élément de fin de carte ; sa présence n’établit pas qu’elle est la cause du saut.

**Correction, dans cet ordre :**
1. Retirer les remises à zéro du scroll de la fonction générique de visibilité. Elle ne doit ni naviguer, ni reconstruire un paquet, ni réinitialiser une face.
2. Utiliser l’événement `change` du `MediaQueryList` pour un vrai changement de présentation. Le `resize` ordinaire ne doit ajuster que la géométrie qui en dépend, sans changer de vue ni d’index ; le calcul du séparateur reste réservé au bureau. Ne pas déplacer les mêmes remises à zéro dans un autre gestionnaire.
3. En compact, conserver un seul défilement principal de page. Retirer les hauteurs fixes et les scrolls internes du quiz, du wrapper, de la scène et du verso. Examiner aussi `.quiz-pane.full-width` et les dimensions en ligne venant du séparateur. `body` ne doit pas devenir un second panneau de hauteur contrainte et défilant dans une page déjà défilante. Identifier la racine avec `document.scrollingElement`.
4. Une seule face participe au flux et à l’accessibilité. La face cachée ne réserve aucun espace et n’offre aucun contrôle focalisable. Supprimer les transitions de hauteur mobile ; conserver les longues réponses intégrales. Révéler ne doit pas déplacer les boutons de navigation au milieu du texte.
5. Retirer `.fc-keyboard-helper` du flux mobile (`display:none`, pas `visibility:hidden` ni `opacity:0`). Conserver l’aide et les raccourcis sur ordinateur ; voir C11.
6. Les gestes sur le texte doivent faire défiler, pas déclencher `flipCurrentCard()` ou `nextFlashcard()`. Préférer une commande explicite Révéler/Masquer pour l’activation accessible. Ne pas installer un `touchmove.preventDefault()` global. Si le toucher de la carte reste une commande, ne pas interpréter un déplacement de doigt comme un tap.

**Position de lecture.** Après un simple resize, ne programmer aucun scroll. À la reprise d’une vue, restaurer sa position sauvegardée une fois son contenu rendu. Après une action explicite Suivante/Précédente, présenter le début de la nouvelle carte. Au retournement, garder le haut de la carte lisible ; ne pas reconstituer le paquet. Au retour d’une source, conserver l’identifiant de carte, l’ordre du paquet et la face révélée.

**Navigation des cartes.** Pour `.fc-nav-bar`, trois colonnes stables (Précédente, Mélanger, Suivante), avec au moins 8 px entre commandes et 44 px de hauteur. Autoriser le retour du texte à l’intérieur d’une commande étroite, pas le recouvrement des commandes. Garder cette barre dans le flux ; ne pas la fixer sur le contenu pour cacher le problème.

**Acceptation spécifique.** Sur une carte courte puis la carte au verso le plus long, faire au moins dix gestes successifs, vers le bas puis vers le haut. Refaire après révélation, après retour source, et en paysage. La fin de la carte se trouve une seule fois ; la navigation aussi ; aucun écran fantôme et aucun `scrollTop=0` déclenché par resize. Faire l’essai avec les barres du navigateur visibles puis rétractées. Une capture d’écran ne valide pas un mouvement : fournir une courte vidéo ou une trace des événements et positions. En environnement émulé, une variation de hauteur seule doit conserver l’ancre visuelle et l’état, sous réserve du bornage normal en fin de document. Ne pas exiger un `scrollY` numériquement identique si la géométrie impose légitimement ce bornage.

Documentation de comportement : `https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia`, `https://developer.mozilla.org/en-US/docs/Web/API/Document/scrollingElement`, `https://developer.mozilla.org/en-US/docs/Web/API/VisualViewport/resize_event`.

## C04 — Terminer les références et les ancres des questions corrigées

**Constat [S1/S4].** Des champs textuels ont été corrigés sans déplacer les cibles correspondantes. Exemples vérifiés : Q15 cite l’Article A mais `anchor_q15` reste dans Cañas, page 322 ; Q17 désigne l’Article E mais `anchor_q17` reste aussi dans Cañas ; Q26 porte désormais sur Jones et Endsley (1996), alors que son ancre renvoie toujours à la conscience de la situation en équipe. Q18 est annoncée comme complément NASA, mais son rattachement reste `doc_canas`. Q13 comporte encore la mention « à documenter par une lecture complémentaire ». Q16 annonce Reason (2000) sans que l’ancien rattachement à Cañas démontre le modèle.

Le résolveur `highlightAndScrollSource()` recherche globalement `anchor_q` + identifiant, sans vérifier que l’ancre appartient au document affiché. Il ignore `q.anchor_id` et ne transforme pas `anchor_phrase` en cible. Une ancre trouvée dans un panneau caché n’est pas un lien source valide.

**Correction demandée.** Contrôler les 44 destinations et leurs deux langues. Distinguer explicitement source intégrée, référence externe et synthèse pédagogique. Pour une source intégrée, utiliser une cible déclarée et vérifier sa présence **dans le viewport du document et de la langue concernés**. Ne jamais basculer silencieusement vers une ancre anglaise cachée lorsque la version française est absente.

Déplacer les ancres de Q15 vers le passage de l’Article A sur les violations et de Q17 vers la citation de Reason dans E, sans réécrire ces passages originaux. Pour Q13, Q16, Q18 et Q26, fournir la référence complémentaire réelle avec un lien explicite, ou proposer une réécriture dans le corpus pour décision. La simple présence d’un thème similaire dans Cañas ne vaut pas justification documentaire. Pour Q27, distinguer le passage de Cañas des résultats et limites du protocole de la publication primaire.

Un renvoi externe doit porter « Ouvrir la référence externe » ; ne pas afficher « Voir le passage officiel » en dirigeant vers un extrait sans rapport. Ne pas attribuer le badge « Lecture obligatoire » à une référence externe simplement parce qu’un ancien `doc_id` vaut `doc_canas`. Classer séparément le thème pédagogique et le statut de la lecture. Dériver les compteurs des données, pas des valeurs écrites en dur.

Contrôler également `toggleDocLanguage()` : changer la langue d’un document choisi librement ne doit pas rappeler le document lié à la question. Actuellement son appel à `highlightAndScrollSource(q.id,...)` peut effectuer ce changement non demandé. De même, le badge source de la question appelle seulement `switchTab()` : sur mobile, il faut aussi afficher explicitement la vue de lecture lorsqu’il constitue une commande utilisateur.

**Acceptation.** Pour chaque source intégrée, l’ancre appartient au viewport attendu, devient visible et cible un passage qui étaye effectivement l’item. Pour chaque source externe, le lien et le statut sont explicites. Depuis Q01, ouvrir librement E puis changer de langue : rester dans E. Répondre à une question mobile ne doit pas ouvrir de force le lecteur.

## C05 — Ne plus présenter un texte enrichi comme une traduction fidèle

**Constat [S1/S4].** La version française intégrée à Cañas contient notamment NASA-TLX et SWAT, absents des pages anglaises correspondantes. Elle possède aussi une bibliographie enrichie. Corriger la question NASA tout en conservant ces ajouts dans la prétendue traduction laisse une contradiction documentaire. La traduction française des quatre articles attribue leur auteur à « Mark Sujan / Human Factors 101 ». Le site Human Factors 101 présente Martin Anderson comme son fondateur et créateur des contenus : `https://humanfactors101.com/about/` et `https://humanfactors101.com/about/martin-anderson/`.

**Correction demandée.** Ne pas modifier silencieusement les originaux pour les faire correspondre aux synthèses. Si les textes français n’ont pas été comparés intégralement avec leurs originaux, les classer temporairement comme **notes de révision enrichies**, distinctes d’une traduction. Afficher une réserve visible ; exclure ces notes de la catégorie « citation originale ». Une véritable traduction doit conserver le sens, les réserves, les attributions et l’organisation du texte source, sans y insérer des compléments non signalés. Sa vérification constitue un lot documentaire séparé.

Libellé transitoire prêt à employer :

> Notes de révision en français générées par IA — adaptation enrichie, non traduction intégrale vérifiée. Pour les citations et les attributions, consulter l’original anglais et les références explicitement indiquées.

Corriger l’attribution générale des articles après vérification de leurs notices :

> Auteur de l’article : Martin Anderson — Human Factors 101. Les auteurs des travaux cités sont indiqués dans le texte.

Convertir le Markdown affiché littéralement dans le HTML (`**...**`, `*...*`, liens `[...](...)`) en balisage HTML approprié. Conserver les titres et les citations originaux ; ne pas les « améliorer » par paraphrase non signalée.

**Acceptation.** Aucun ajout propre aux notes françaises n’est présenté comme un passage traduit de Cañas. Aucun des quatre articles n’attribue sans justification son texte à Mark Sujan. Le statut de la version française est compréhensible avant de l’utiliser comme preuve.

---

# P1 — Fiabilité de l’affichage et de l’entraînement

## C06 — Corriger la géométrie verticale et préserver le réglage manuel

**Constat [S1].** La dernière règle remplace le ratio par `max-height: calc(100% - 220px)` pour le quiz et `min-height: 220px` pour le lecteur. Le séparateur de 8 px n’est pas compté dans cette réserve. Le wrapper conserve `min-height: 100%`. `updateDynamicLayout()` efface les dimensions manuelles à chaque redimensionnement ; `userHasDraggedSplit` est affecté mais pas utilisé pour protéger ce réglage. L’affirmation « proportion optimale automatique » n’est donc pas démontrée.

**Correction demandée.** Distinguer hauteur naturelle du contenu et taille disponible du panneau. En disposition verticale seulement, supprimer la contrainte qui étire artificiellement le wrapper servant à mesurer cette hauteur. Calculer la place utile à partir du conteneur réel, moins le séparateur et la place réservée au lecteur. Cette réserve doit inclure ses commandes et une zone de texte utilisable, pas seulement une valeur globale arbitraire.

Principe de calcul : `hauteurQuiz = min(hauteurNaturelleQuiz, hauteurDisponible - séparateur - réserveLecteur)`, avec bornes cohérentes et stratégie de défilement si l’espace manque. Ne pas faire croire que tout peut tenir sur une petite fenêtre. Préférer un panneau de quiz clairement défilant à un lecteur hors écran ou à un chevauchement. Aucun décalage négatif destiné à masquer le symptôme.

Recalculer après changement de question, apparition de rétroaction, changement de mode, chargement des polices et changement effectif de taille. Regrouper les calculs avec `requestAnimationFrame` ; si `ResizeObserver` est employé, ne pas créer une boucle en observant sans garde les dimensions que l’on modifie. Après déplacement manuel du séparateur, conserver la préférence et la borner seulement si elle ne tient plus. Double-clic : revenir au calcul automatique. Le tactile doit suivre la même règle que la souris.

**Acceptation.** En fenêtre haute, ressources et podcast visibles avant le lecteur, sans grand vide artificiel. En fenêtre basse, contenu intégralement atteignable par un défilement clair. La somme des panneaux et du séparateur reste dans l’espace disponible. Après réglage manuel, une variation modérée de taille ne remet pas le séparateur à zéro. Vérifier côte à côte sans modifier ses dimensions par défaut.

## C07 — Interface mobile : règles cohérentes, titre lisible et pagination horizontale

### C07.1 — Une seule condition compacte et une géométrie cohérente

**Constat [S1/S5].** Deux stratégies coexistent : un bloc à 768 px et un bloc `(max-width: 48rem), (max-height: 32rem) and (pointer: coarse)`. Le rétablissement du défilement racine appartient au premier seulement. En paysage tactile au-delà de 768 px, la vue compacte peut donc coexister avec une racine `overflow:hidden`. La règle générale `.mobile-only { display:block !important; }` écrase le `display:flex` des outils. Le `top:48px` du lecteur suppose un bouton retour de hauteur invariable.

**Correction.** Consolider les règles sous la même condition en CSS et en JavaScript. Le critère actuellement employé peut être conservé, à condition de le rendre identique pour tous les composants et de tester ses frontières. Retirer les déclarations concurrentes plutôt que déposer une troisième couche de `!important`. Ne pas appliquer les dimensions de la disposition bureau dans la vue compacte, même si une classe d’orientation reste présente.

Séparer **visibilité** et **disposition** : le moteur de visibilité de C03 indique quel composant est masqué ; le CSS du composant détermine s’il est en grid, flex ou block. Ne pas remplacer arbitrairement un flex par `style.display='block'`. Nettoyer les styles en ligne concernés. S’assurer que tout élément déclaré caché reste réellement caché, sans qu’une règle d’affichage ne le ressuscite.

Une seule zone principale défilante en mobile pour Étude, Cartes et Podcast ; pas d’overflow global caché comme seule réparation d’un débordement. La vue de lecture utilise elle aussi le flux mobile prévu. Regrouper retour et outils du lecteur dans un bloc sticky dont la hauteur est réelle, ou mesurer l’offset si deux blocs sont indispensables. Pas de hauteur 48 px présumée correcte après zoom ou retour à la ligne. Les dialogues peuvent avoir un défilement propre : cela ne doit pas créer un second scroll permanent dans l’activité.

### C07.2 — Titre complet, date rétablie, progression et Plus hors de la ligne du titre

**Retour Michel [S6].** « PSY7010 Quiz d’entraînement » est rogné par le score et Plus ; la date manque. Les quatre boutons d’activité, la mascotte et le filtre sont satisfaisants : ne pas les redessiner.

**Code [S5].** `.header-brand` hérite de `white-space:nowrap` et `flex-shrink:0`. Les outils partagent sa rangée étroite. La date n’est pas seulement recouverte : `.quiz-sub-date { display:none !important; }` la masque explicitement. La règle générique `.mobile-only` désorganise aussi la rangée des outils.

**Disposition à livrer, sans raccourcir silencieusement le titre :**

```text
PSY7010 Quiz d’entraînement
22 septembre                 0/44   [Plus]
[ Étude ] [ Test ] [ Cartes ] [ Podcast ]
```

Le titre peut occuper deux lignes si nécessaire à 320 px ou après agrandissement, mais ne doit pas être tronqué. Les outils ne sont jamais positionnés par-dessus lui. La date demeure distincte, à la rangée suivante. Le score est une information, pas un bouton inactif. Le libellé Plus reste explicite ; son ouverture est traitée en C01.

**Implémentation.** Dans le DOM de l’en-tête mobile, répartir le titre sur toute la largeur, puis date et outils sur une seconde rangée. Garder un seul `h1`, une seule date et l’unique compteur mobile existant ; ne pas dupliquer des identifiants. La solution peut employer une grille à zones. Le wrapper `.header-brand` est un `div` sans rôle particulier : le rendre `display:contents` uniquement en compact permet de placer son titre et sa date dans la grille parente, ou refactoriser le DOM en préservant le rendu bureau. Ne pas choisir cette technique pour un élément sémantique dont le rôle risquerait d’être perdu.

Exemple à intégrer **après suppression des anciennes règles mobiles incompatibles** et du style inline de `.mobile-header-tools` :

```css
/* Dans la condition compacte commune : */
.header-brand-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  grid-template-areas: "title title" "date tools";
  align-items: center;
  width: 100%;
  gap: 0.5rem 0.75rem;
  min-width: 0;
}
.header-brand-row > .header-brand { display: contents; }
.header-brand-row .quiz-main-title {
  grid-area: title;
  min-width: 0;
  white-space: normal;
  overflow: visible;
  text-overflow: clip;
  line-height: 1.3;
}
.header-brand-row .quiz-sub-date {
  display: block;
  grid-area: date;
  white-space: normal;
  line-height: 1.35;
}
.header-brand-row .mobile-header-tools {
  display: flex;
  grid-area: tools;
  align-items: center;
  gap: 0.5rem;
}
```

La règle générique `.mobile-only` ne doit plus imposer `display:block !important` : l’enlever/réorganiser et définir l’affichage voulu par composant dans le même bloc compact. Les définitions non compactes restent en place. Après agrandissement très important, autoriser une rangée supplémentaire pour les outils plutôt que rogner un contenu. Aucun `line-clamp`, `ellipsis`, largeur négative ou réduction automatique de police pour faire rentrer le titre.

**Acceptation.** À 320, 390 et 430 px, dans Étude, Test, Cartes et Podcast : texte complet visible, date visible, outils sans intersection avec le titre ; nombre de titres/date conforme. Agrandir le texte, puis vérifier le bureau. La mascotte, le message de mode, le filtre et les quatre commandes validées conservent leur présentation.

### C07.3 — Remplacer la colonne de numéros par une navigation adaptée

**Retour Michel [S6].** Les numéros 1, 2, 3, 4, 5 se rangent verticalement entre Précédente et Suivante : l’ensemble ressemble à une croix.

**Code [S5].** `.google-pagination` autorise `flex-wrap:wrap !important` sur mobile, alors que les boutons latéraux ne rétrécissent pas. La colonne du centre récupère trop peu de largeur. La fonction `renderGooglePagination()` réécrit également `display:flex` en ligne.

**Correction.** Conserver la pagination détaillée pour le bureau, mais ne plus essayer de la faire tenir sur téléphone. Dans la vue compacte, afficher **Précédente — 7 / 44 — Suivante** sur trois colonnes stables. La position centrale donne accès à un sélecteur natif ou à un dialogue simple « Aller à la question ». Préférence ici : un sélecteur natif compact, avec un nom accessible. Ne pas fabriquer un sélecteur personnalisé si cela complique inutilement le focus et le tactile.

Créer un composant central mobile, par exemple `mobileQuestionSelect`. Ses valeurs correspondent à la liste active, pas à une supposition sur `id-1`. Afficher « 7 / 44 » pour sa sélection courante ; les options permettent d’atteindre chaque question. Recalculer total et position après filtre et dans la simulation. Une simulation de cinq questions affiche x / 5 ; une section de six questions, x / 6. Ne pas donner la bonne réponse ou son statut avant le bilan du Test.

Faire rendre simultanément le contenu des contrôles appropriés ou les dériver de l’état, mais ne pas laisser `renderGooglePagination()` forcer l’affichage de la version bureau sur mobile. Si `[hidden]` sert à masquer un composant, s’assurer que les règles CSS ne l’annulent pas. La variante cachée ne reçoit pas le focus.

Grille mobile de départ : `grid-template-columns: minmax(0, 1fr) minmax(4.5rem, auto) minmax(0, 1fr)` ; `gap:8px` ; commandes d’au moins 44 px de haut ; `min-width:0`. Les mots peuvent revenir à la ligne **dans** un bouton si nécessaire, jamais les numéros en colonne. À 320 px, ne pas réserver de grandes marges aux boutons latéraux et ne pas réduire leurs polices pour préserver sept numéros inutiles.

**Acceptation.** Première, milieu et dernière question ; banque complète et filtres ; Test. Compteur juste, commandes alignées, Précédente/Suivante désactivées ou remplacées selon les bornes et la fin de test. Accès direct fonctionnel, aucun bouton invisible mais focalisable, aucun effet de croix. La pagination bureau demeure inchangée.

### C07.4 — Cartes, source et frontières d’affichage

Appliquer le correctif de défilement de C03 et la suppression de l’aide clavier de C11 ; ne pas créer un autre moteur de navigation spécifique aux cartes. Conserver la structure de carte mobile et les quatre onglets déjà acceptés. Le bouton retour du lecteur doit mener à l’activité réelle et restaurer sa position. Gérer les zones sûres et le clavier virtuel sans recouvrir les dernières commandes.

**Acceptation globale C07.** 320×568, 390×844, 430×932, puis 844×390 avec entrée tactile ; 768/769 px, zoom et passage compact ↔ bureau. Les contrôles sont dans la zone visible et atteignables, et la page ne change pas d’activité pendant un geste de défilement. Une règle `overflow-x:hidden` ne vaut pas preuve d’absence de rognage.

## C08 — Réparer la recherche documentaire

**Constat [S1 ; essais isolés].** Le champ est injecté directement dans `new RegExp(term, 'gi')`. `SA(` produit une `SyntaxError`. Le flag global rend les appels successifs à `test()` dépendants de `lastIndex` : deux paragraphes contenant chacun « SA » peuvent être comptés comme un seul. Les nœuds dont le parent est `MARK` sont exclus : des extraits surlignés sont introuvables. Le tableau contient des parents de nœuds, pas des occurrences. Effacer le champ change le libellé sans vider les résultats. Une bascule document/langue ne nettoie pas correctement l’état de recherche.

**Correction demandée.** Faire une recherche littérale par défaut. Échapper correctement une expression si cette voie est retenue, ou utiliser des comparaisons de chaînes. Ne pas conserver un `lastIndex` entre nœuds. Indexer les occurrences réelles avec leurs positions ; rechercher aussi dans les marques sources. Ne pas détruire ni renuméroter les ancres permanentes lors du surlignage de recherche. Utiliser des marques distinctes ou des plages de texte.

Réinitialiser résultats, index, compteur et surlignage quand le champ devient vide ou que le document change. Recalculer si un terme doit rester actif. Compter des occurrences, ou annoncer explicitement que l’unité est le passage. Gérer les clics, le collage et la saisie mobile via les événements appropriés, pas seulement `keyup`. Faire défiler le lecteur concerné, pas la station entière sur ordinateur.

**Acceptation.** `SA(` et `[` ne provoquent aucune erreur ; deux occurrences sont trouvées dans deux paragraphes et dans un même paragraphe ; un terme uniquement présent dans une ancre reste trouvable. Après effacement, Suivant ne navigue plus vers un ancien résultat. Après changement de langue ou document, aucune destination périmée. Voir MDN : `https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test`.

## C09 — Synchroniser scores, statistiques et stockage

**Constat [S1 ; essai isolé].** `mobMasteryBadge` affiche une valeur initiale, mais `updateMasteryBadge()` ne met à jour que le badge de bureau. Une bonne réponse peut donc donner 1/44 sur ordinateur et 0/44 sur téléphone. `userAnswers` est en mémoire seulement, contrairement à `cardStats`. `JSON.parse(localStorage.getItem(...))` est exécuté sans protection au démarrage. Les statistiques sont indexées par identifiant de question sans révision du contenu.

**Correction demandée.** Dériver les deux badges du même calcul. Actualiser aussi après « Réessayer », réinitialisation et restauration. Séparer les résultats d’étude de ceux de la simulation. Éviter qu’un double clic sur une même réponse déjà validée crée deux tentatives : exiger une nouvelle tentative explicite.

Mettre la lecture/écriture du stockage derrière une fonction protégée, valider le schéma et continuer en mémoire si le stockage est indisponible. Une donnée corrompue doit donner un avertissement intelligible, pas empêcher toute initialisation. Versionner les statistiques par révision de banque ou empreinte des items : les résultats d’une ancienne formulation ne prouvent pas la maîtrise de la nouvelle. Prévoir une migration explicite ; ne pas effacer indistinctement toutes les préférences.

Si la progression d’étude doit être conservée au rechargement, la sauvegarder réellement avec sa version. Sinon, annoncer « réponses de cette session » et ne pas présenter l’ensemble comme une progression persistante. Préserver en tout cas index et réponses lors des simples changements de vue dans la session.

**Acceptation.** Les deux scores évoluent ensemble. Répondre, ouvrir une autre vue et revenir ne modifie pas le résultat. Tester stockage vide, valide, JSON mal formé et stockage refusé. Réinitialiser les scores ne change pas le thème, le lien audio ou les préférences de disposition.

## C10 — Unifier la notion de difficulté des cartes

**Constat [S1 ; essai isolé].** Une carte peut être comptée « maîtrisée » lorsque `fcRating === 'easy'` et score zéro, mais rester dans le paquet difficile parce qu’elle a eu une erreur historique. Le badge et la liste ne décrivent alors pas les mêmes cartes. Le paquet difficile ignore également le filtre de catégorie. `consecutiveEasy` n’est pas remis à zéro après `medium`. `wasHard` consulte `stat.fcRating` après son remplacement par la nouvelle note. La notation n’exige pas que le verso soit révélé. Aucun intervalle ou échéance de révision n’est implémenté dans la logique examinée malgré l’étiquette SRS.

**Correction demandée.** Calculer un statut unique par carte, puis l’utiliser pour les badges, les compteurs, le tri, le paquet et les célébrations. Conserver l’historique d’erreurs sans en faire une condamnation permanente. Capturer l’ancien statut avant mutation ; remettre la série de « faciles » à zéro après toute note non facile. N’autoriser la notation que sur une carte révélée, dans l’activité visible, hors d’une boîte de dialogue.

Appliquer le filtre de catégorie au paquet difficile et afficher un vrai état vide au lieu de revenir silencieusement aux 44 cartes. Garantir que le compteur du paquet reflète exactement son contenu. Ne pas ajouter précipitamment un nouvel algorithme de répétition espacée : tant qu’il n’existe pas de calendrier de révision, renommer honnêtement le mécanisme.

Libellé prêt à employer :

> Révision active avec priorisation des difficultés — le paquet est organisé selon vos erreurs et vos autoévaluations.

**Acceptation.** Après une erreur puis des évaluations faciles suffisantes, statut, compteur et appartenance au paquet restent cohérents. Une carte non révélée ne peut pas être notée par les raccourcis. La séquence facile → moyen → facile ne donne pas trois faciles consécutifs. Le paquet de difficultés d’une section ne contient pas les autres sections.

## C11 — Rendre les interactions accessibles et éviter les commandes cachées

**Constat [S1].** Les raccourcis globaux restent actifs quand le lecteur, le podcast ou une boîte de dialogue est visible. Espace peut intercepter l’activation native d’un bouton. Des zones cliquables sont des `span`/`div`. L’état actif repose principalement sur une classe CSS. Les boîtes de dialogue n’implémentent pas les garanties de focus nécessaires.

**Correction demandée.** Borner les raccourcis à l’activité visible et suspendre ceux de l’arrière-plan pendant une boîte de dialogue. Respecter les champs éditables, les boutons, les liens, les touches de modification et les activations natives. Employer des boutons pour les commandes ; nommer les sliders, champs de recherche et sélecteurs. Exposer l’état actif par une sémantique adaptée (`aria-current` ou `aria-pressed`, selon le composant).

Utiliser `<dialog>` avec ses comportements corrects, ou implémenter le motif modal complet : nom accessible, focus initial, cycle de tabulation interne, Échap et restitution du focus. Ne pas supprimer le contour de focus sans remplacement visible. Distinguer visuellement et textuellement succès/erreur, pas uniquement par couleur. Respecter la préférence de réduction des animations et limiter les pulsations persistantes. Rendre le séparateur utilisable au clavier et uniformiser souris/tactile avec Pointer Events si ce lot est modifié.

**Aide clavier sur téléphone [S6].** Masquer `.fc-keyboard-helper` dans le mode compact normal, en retirant aussi son espace réservé. Remplacer la consigne mobile « Cliquer ou [Espace] pour révéler » par « Toucher pour révéler » ou le libellé du bouton Révéler. Conserver les raccourcis et leur aide sur bureau. Un téléphone peut recevoir un clavier externe : ne pas désactiver arbitrairement toute entrée clavier ; c’est l’aide visible permanente qui est supprimée. Les garde-fous d’activité, de dialogue et de champ éditable restent obligatoires. Masquer cette aide n’est pas, à lui seul, la correction du défilement C03.

Pour les cartes de bureau, vérifier que les faces en position absolue ne débordent pas sur la navigation : leur parent à hauteur minimale fixe ne grandit pas automatiquement avec elles. Utiliser une géométrie qui prend en compte la hauteur réelle, tout en conservant le style de bureau. Ne pas tronquer les explications pour faire tenir le gabarit.

**Acceptation.** Navigation entièrement au clavier ; ouverture/fermeture des dialogues sans commande envoyée au questionnaire caché ; lecture et retour source sans changement furtif de carte ; cartes les plus longues lisibles recto/verso. Motif W3C : `https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/`.

---

# P2 — Finaliser sans masquer les défauts précédents

## C12 — Podcast : supprimer le doublon mobile, aérer et vérifier la lecture réelle

### C12.1 — Présentation mobile demandée par Michel

**Retour Michel [S6].** L’ensemble est acceptable hormis des éléments trop serrés. Le grand bouton rond Play en haut fait doublon avec Écouter ; l’en-tête devrait commencer directement par « Podcast de révision • Trajet UQAM ». La progression et ses temps sont trop proches d’« Ouvrir sur Google Drive ».

**Code [S5].** Le bouton rond est `#podcastAvatarCircle`, distinct du bouton utile `#audioPlayPauseBtn`. `setMobileView('podcast')` impose `podcastBanner.style.display='block'`. Or l’espacement entre les parties de `.podcast-banner` dépend d’un `gap` de flex : en block, ce `gap` ne sépare plus les enfants. Ce mécanisme explique un manque d’espacement sans démontrer qu’il en est l’unique cause sur l’appareil.

**Correction.** En compact uniquement, masquer `#podcastAvatarCircle` sans réserver de place. Conserver cet élément dans le DOM si les fonctions audio ou le bureau s’y réfèrent, et préserver son apparence bureau. **Ne pas retirer** `#audioPlayPauseBtn`, l’élément audio, les temps ou la progression. Un seul bouton de lecture visible dans la vue mobile suffit ; Écouter devient Pause selon l’état réel.

Ne plus forcer `display:block` depuis la fonction de changement de vue. Le moteur C03 gère la visibilité ; le CSS gère la disposition en grille ou flex. Conserver une présentation simple :

```text
Podcast de révision • Trajet UQAM
Titre de l’épisode
Description

[Écouter / Pause]                         [Vitesse]
00:00  ───────── progression ─────────  durée

[Ouvrir sur Google Drive]
[Gemini Notebook]
[Liens et options]
```

Cibles de conception : padding du panneau 20 px ; 8 px entre titre et description ; 16 px avant les commandes ; 12 à 16 px entre commandes et progression ; **24 px entre le bloc progression/temps et le premier lien externe** ; 10 à 12 px entre les liens. Ne pas simplement ajouter une marge au temps `00:00` : espacer les groupes entiers.

Grille compacte suggérée pour `.custom-audio-controls` : zones `"play speed"` puis `"timeline timeline"`, avec `grid-template-columns:minmax(0,1fr) auto` et `gap:14px 12px`. Assigner les zones au bouton, à `.audio-speed-wrap` et à `.audio-timeline-wrap`, et retirer l’ancien `order:3 !important` contradictoire. La ligne de temps peut employer `grid-template-columns:auto minmax(0,1fr) auto`, un intervalle de 8 px et une largeur minimale nulle pour le slider. Les temps ne doivent pas se superposer au slider ni aux liens.

Pour obtenir les 24 px de séparation externe, utiliser un seul mécanisme calculable, par exemple `row-gap:24px` entre `.podcast-banner-center` et `.podcast-banner-right` dans la grille visible. Retirer les marges résiduelles contradictoires plutôt qu’empiler plusieurs écarts. La zone tactile du slider doit être assez haute (cible 44 px) tout en gardant un rail fin : ne pas confondre hauteur cliquable et épaisseur graphique. Préserver son fonctionnement clavier et tactile.

**Acceptation visuelle.** Aucun rond Play en mobile, un bouton Écouter/Pause fonctionnel, en-tête intact, temps entièrement visibles. À 320/390/430 px, mesurer au moins 24 px entre le bas de la zone progression et le lien Drive ; les liens ne recouvrent jamais le curseur. Naviguer Podcast → Étude → Podcast et changer la largeur : mêmes dispositions, même position audio. Sur bureau, pas de suppression du bouton rond ni de dégradation du panneau.

### C12.2 — Fiabilité des commandes et de l’hébergement

**Constat du réaudit [S1].** La vitesse est affichée avec `toFixed(1)` : 1,25 devient 1,3 et 1,75 devient 1,8. L’échec de lecture ne donne qu’un avertissement console. Plusieurs chemins sont équivalents ou adaptés à des profondeurs différentes. Le journal montre une requête HEAD, pas une preuve de lecture [S3].

Afficher exactement la vitesse choisie, par exemple avec `Intl.NumberFormat('fr-CA', { maximumFractionDigits: 2 })`. Gérer `loadedmetadata`, `play`, `pause`, `ended` et `error` pour synchroniser les commandes, y compris une pause externe. Afficher un message d’échec visible et un lien de secours actionnable ; ne pas ouvrir automatiquement un onglet. Réutiliser le même `#localPodcastAudio` lors des changements de vue, sans réaffecter sa source ni le recréer.

Résoudre un chemin correct pour chaque point d’entrée. Éviter les 404 prévisibles comme fonctionnement normal ; ne pas compter les versions Unicode et encodée d’une URL comme deux hébergements indépendants. Tester page racine et fichier de sous-dossier si les deux sont maintenus.

**Acceptation fonctionnelle.** Un clic réel fait progresser `currentTime` ; pause, reprise, seek et vitesse exacte fonctionnent. Le bouton restant suffit. Un échec simulé informe l’utilisateur sans planter. Après reprise de vue, `currentTime` ne repart pas à zéro. Un statut HTTP 200 ou un fichier m4a présent ne valide pas ces critères.

## C13 — Nettoyage et reliquats académiques ciblés

Supprimer la double affectation consécutive de `fbDocQuote`. Corriger `var(--error)` en utilisant la variable de danger réellement définie. Harmoniser les commentaires contradictoires, notamment `docLanguage = 'en'` accompagné d’un commentaire français. Remplacer les messages « regarde à droite » par un libellé adapté à la présentation. Générer les nombres de questions, de cartes et de catégories depuis les données.

**Deux corrections textuelles supplémentaires identifiées dans les items conservés [S1/S4] :**

- **Q12, `feedbacks[0]` :** remplacer la formulation « hors de tout contrôle conscient » par :

> Le niveau fondé sur les habiletés correspond à des conduites très familières et largement automatisées. Le scénario décrit au contraire un problème inédit pour lequel ces routines ne suffisent pas.

- **Q16, `options[0]` :** remplacer l’accident présenté comme conséquence automatique de l’alignement par :

> Les tranches représentent des défenses successives ; les trous représentent leurs faiblesses. Une trajectoire accidentelle devient possible lorsqu’un danger peut traverser plusieurs défenses rendues inefficaces.

Ces deux ajustements n’autorisent pas une réécriture spontanée des autres items. Ils ferment des formulations que les remplacements précédents avaient laissées intactes. Ne pas considérer mon premier JSON comme une preuve de perfection intrinsèque : ses avertissements et ses dépendances documentaires font partie de son contenu.

La répartition des réponses reste une opération distincte du remplacement textuel. Inventorier la distribution réelle de la banque courante. Le rendu examiné conserve l’ordre des options. Rééquilibrer sans motif prévisible, ou mélanger une permutation par question et par session en conservant la liaison option–rétroaction–solution. Ne jamais modifier `correctIndex` seul, ni mélanger de nouveau au moment d’afficher la rétroaction. Les réponses sauvegardées doivent utiliser un identifiant stable de choix ou être remappées explicitement.

Retirer du compte rendu les garanties non mesurées comme « saisie rétinienne immédiate sans balayage des yeux », « zéro secousse » et « proportion optimale ». Un `max-width` CSS n’établit pas ces propriétés. Le message de célébration ne doit pas prétendre mesurer la consolidation d’un réseau mnésique à partir d’un clic « Facile ».

---

# Procédure de validation obligatoire

## V01 — Installer une vraie collecte d’erreurs

Le journal fourni évalue `window.errors || []`, puis imprime un message de réussite sans exploiter le résultat ni établir que la page collecte réellement les erreurs. L’absence d’un tableau d’erreurs n’est pas l’absence d’erreurs.

Installer la collecte **avant** la navigation. Exemple de base Playwright à intégrer au vrai test, pas au site :

```javascript
import { test, expect } from '@playwright/test';

const BASE_URL = process.env.PSY7010_TEST_URL || 'http://127.0.0.1:8080/';

test('Les options mobiles sont opérationnelles', async ({ page }) => {
  const pageErrors = [];
  const consoleErrors = [];
  page.on('pageerror', error => pageErrors.push(error.message));
  page.on('console', message => {
    if (message.type() === 'error') consoleErrors.push(message.text());
  });

  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(BASE_URL, { waitUntil: 'domcontentloaded' });
  await expect(page.locator('#qQuestionTitle')).not.toBeEmpty();
  await page.getByRole('button', { name: /Plus/ }).click();
  await expect(page.locator('#optionsModal')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.locator('#optionsModal')).not.toBeVisible();

  expect(pageErrors).toEqual([]);
  expect(consoleErrors).toEqual([]);
});
```

Pour les tests mobiles en paysage, utiliser aussi un contexte tactile, pas seulement `setViewportSize`. Capturer les échecs réseau séparément et vérifier les statuts des ressources locales ; ne pas transformer tous les incidents réseau en réussites silencieuses. Les erreurs externes éventuelles doivent être identifiées et expliquées. Documentation : `https://playwright.dev/docs/api/class-page`.

Exécuter les clics réels sur les boutons. Un appel direct à `setMode('simulation')` suivi d’une capture prouve seulement que l’écran de paramètres est affichable. Il ne teste pas « Démarrer la simulation ».

## V02 — Critères d’acceptation des parcours

| Test | Résultat exigé |
|---|---|
| Chargement propre | Question et options affichées ; aucune exception non traitée. |
| En-tête des quatre vues mobiles | Titre complet visible, date visible à la ligne suivante, score et Plus sans recouvrement. |
| Éléments acceptés par Michel | Onglets d’activité, mascotte, message de mode et filtre conservés visuellement. |
| Pagination mobile | Une rangée Précédente / position-total / Suivante ; accès direct et total filtré exacts. |
| Espaces du formulaire Test | 12 px titre-description ; 24 px description-groupe ; 10 px label-menu ; 20 px entre groupes ; 24 px avant Démarrer, avec ajustements justifiés seulement. |
| Défilement Cartes répété | Dix gestes dans chaque sens, carte courte et verso long, pas de reset de scroll ni écran répété ; trace ou vidéo. |
| Aide clavier mobile | Absente sans espace réservé ; aide de bureau et support clavier conservés. |
| Podcast compact | Rond Play masqué, Écouter/Pause conservé, 24 px entre progression et lien Drive. |
| Plus / thème / Échap | Dialogue utilisable, thème synchronisé, focus rendu. |
| Test cinq questions | Démarrage, réponses, fin, score exact, nouvelle session indépendante. |
| Expiration du chronomètre | Fin une seule fois ; durée fondée sur l’échéance, pas sur le nombre de ticks. |
| Q13 → Podcast → Étude | Même question, même choix, même position de reprise. |
| Carte 11 retournée → source → retour | Même carte, même face, même ordre de paquet. |
| Resize dans l’activité | Aucun retour en haut ou à Q01 non demandé. |
| Mobile ↔ bureau depuis source/podcast | Aucune carte ni ressource définitivement masquée. |
| Réponse correcte / Réessayer | Scores des deux présentations cohérents ; double clic sans double tentative. |
| Sources des 44 questions | Source correcte ; ancre dans le document/langue cible, ou renvoi externe explicite. |
| E choisi librement → changement de langue | Document E conservé. |
| Recherche et effacement | Recherche littérale, occurrences correctes, pas de résultats périmés. |
| Difficultés filtrées | Liste et badge identiques, filtre respecté, état vide explicite. |
| Stockage corrompu/refusé | Application utilisable et avertissement ; pas de blocage au démarrage. |
| Podcast réel | Temps de lecture qui avance, pause, seek et vitesse exacte. |
| Clavier et dialogues | Focus visible, raccourcis suspendus sur les vues cachées. |
| Lecture française | Statut documentaire exact, pas de synthèse présentée comme citation. |
| Bureau côte à côte / haut-bas | Aucun chevauchement ; réglage manuel conservé ; contenu long accessible. |

Pour la géométrie : 320×568, 390×844, 430×932, 844×390 tactile, 768×1024, 1024×1366, 1366×768 et 1920×1080 ; états clair/sombre, rétroaction longue ouverte, carte retournée, source française. Tester le zoom et le clavier virtuel. Les mesures ne doivent pas se limiter à `scrollWidth <= clientWidth` : `overflow-x:hidden` peut masquer un élément hors écran. Examiner aussi les rectangles des contrôles visibles et leurs captures.

Le réagencement à 320 pixels CSS est une référence WCAG pour ce contenu ; la cible principale de 44 px proposée ici ne doit pas être confondue avec le critère WCAG 2.2 AA de 24×24 px et ses exceptions. Références : `https://www.w3.org/WAI/WCAG22/Understanding/reflow.html` et `https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html`.

### Contrôle de mouvement, pas uniquement d’image

Enregistrer temporairement, dans le test uniquement : `window.scrollY`, `document.scrollingElement.scrollTop`, les `scrollTop` des panneaux, les hauteurs `scrollHeight/clientHeight`, l’activité, la vue, l’identifiant de carte et sa face. Horodater les événements `scroll`, `window.resize`, `visualViewport.resize` et le `change` de la media query. Ces traces permettent de distinguer un scroll interne, un rebond natif, un changement de hauteur et une remise à zéro programmée.

Exécuter un parcours utilisateur, pas une boucle qui appelle le gestionnaire manuellement et conclut ensuite que tous les gestes fonctionnent. L’émulation tactile couvre une partie des défauts ; tester Safari iOS et Chrome Android lorsque ces appareils sont disponibles. En l’absence de l’un d’eux, le mentionner comme **non testé**, pas « validé mobile ». Ne pas bloquer le rebond ou tous les gestes pour dissimuler une erreur de navigation. Ne pas conserver cette instrumentation dans la version finale.

## V03 — Contrôles des données et de la publication

Vérifier automatiquement 44 identifiants uniques, quatre options et quatre rétroactions par item, un index entier valide, aucune chaîne vide inattendue et aucune propriété de rapport injectée comme objet question. Comparer **chaque remplacement demandé** avec la banque, y compris les chemins `feedbacks[n]`. Ce contrôle d’intégration ne remplace pas l’examen sémantique.

Sauvegarder l’empreinte des blocs anglais avant les travaux et la comparer après, en distinguant les balises d’ancrage du texte. Les ajouts documentaires doivent être séparés et signalés. Ne pas obtenir artificiellement le même hash en excluant des fragments substantiels de la comparaison.

Si deux HTML sont maintenus, les produire depuis une même source ou vérifier leurs différences autorisées, notamment les chemins de ressources. Ne pas affirmer leur synchronisation après avoir modifié un seul fichier.

Identifier le build déployé dans la page ou un manifeste généré lors de la publication. Après déploiement, vérifier que le contenu réellement servi correspond au build testé, avec cache désactivé. Un `git push` et un statut 200 ne démontrent pas cette correspondance.

La date d’expiration existante du quiz fait partie du comportement courant. La conserver sauf instruction de Michel, mais la couvrir dans les tests : avant, pendant et après l’expiration. Si la page est fermée en cours de session, arrêter les minuteurs et empêcher les gestionnaires de modifier un DOM supprimé. Ne pas contourner définitivement l’expiration pour faire passer les tests ; utiliser une horloge de test contrôlée.

---

# Résultats historiques du premier réaudit — non rejoués dans cette V2

Ces résultats proviennent des montages isolés du premier réaudit au commit de référence. Ils sont conservés pour ne perdre aucune correction, non présentés comme des essais supplémentaires. Ils ne remplacent pas V01–V03 sur le fichier courant et le build déployé.

| Branche testée | Résultat observé dans le montage isolé |
|---|---|
| `setMode('study')` avec index 12 | Index ramené à 0. |
| `setMode('flashcards')` avec index 10 | Index ramené à 0. |
| Simulation active + vue activité | Questions, paramètres et résultats tous à `display:none`. |
| Podcast compact puis branche resize bureau | `qCard` reste masqué. |
| Activité compacte puis branche resize bureau | Podcast et bannière de cartes restent masqués. |
| Mise à jour d’une bonne réponse | Badge bureau à 1/44 ; badge mobile inchangé. |
| Recherche `SA(` | `SyntaxError` de construction de l’expression. |
| Deux paragraphes contenant chacun SA | Un seul résultat au lieu de deux. |
| Mot uniquement dans `mark` | Aucun résultat. |
| Effacement de recherche | Libellé à zéro, ancien résultat encore stocké. |
| Une erreur passée, puis carte facile avec score zéro | Statut maîtrisé, mais carte encore dans le paquet difficile. |
| Affichage des vitesses 1,25 et 1,75 | Libellés arrondis à 1,3 et 1,8. |

# Ordre de travail et livraison unique

**Lot 1 — Fonctionnement et stabilité :** C01, moteur C02, C03 et règles de flux de C07.1. Aucun bouton sans effet ; aucune vue vide ; aucun changement de taille qui réinitialise l’activité. Le défilement des cartes est un défaut de fonctionnement, pas une retouche cosmétique.

**Lot 2 — Mobile demandé par Michel :** C07.2 titre/date/outils ; C07.3 pagination ; C02.2 espacement du Test ; C11 aide clavier ; C12.1 podcast. Ne pas modifier les quatre onglets, la mascotte ou le filtre déjà acceptés. Intégrer chaque retouche dans ses règles définitives, pas dans un bloc de surcharges supplémentaires.

**Lot 3 — Complétude du réaudit :** C04–C06 et C08–C13, selon leurs dépendances. Les sources, statistiques, données persistantes, raccourcis et commandes audio restent obligatoires. Ne pas abandonner ces points parce que les nouvelles captures mobiles paraissent meilleures.

**Lot 4 — Validation et publication :** V01–V03. Tester avant de publier, puis vérifier le build réellement servi. Conserver des captures bureau avant/après sur les mêmes données et fenêtres. Ne pas déclarer une validation globale si des tests ou appareils manquent.

Pour chaque identifiant C01–C13 et ses sous-points, fournir : correction, fichiers/fonctions modifiés, test exécuté, résultat, limite. Livrer le HTML courant complet corrigé (et les autres fichiers réellement nécessaires), le commit testé, le build publié, puis un tableau **corrigé et testé / corrigé non testé / restant à corriger**. Fournir une trace ou vidéo pour le problème de défilement, pas une capture immobile en guise de preuve.

**Interdits :** gestionnaires vides ; supprimer une fonction pour faire disparaître une erreur ; masquer un débordement comme unique correction ; retirer date/titre/mascotte malgré la demande ; retirer Écouter au lieu du rond Play ; cacher les raccourcis et déclarer le scroll réparé sans l’essayer ; désactiver globalement les gestes tactiles ; modifier `correctIndex` seul ; effacer silencieusement l’historique ; réécrire les originaux ; remplacer la version récente par l’ancien HTML ; affirmer « perfection », « zéro bug » ou « tout vérifié » sans preuves.

**Instruction d’envoi :** ce document V2 est l’unique consigne technique consolidée à utiliser pour ce passage. Il remplace le document du ZIP précédent ; ne pas additionner leurs recommandations contradictoires. Le premier dossier académique reste une référence de données déjà intégrées, à consulter au besoin, non un correctif à réappliquer automatiquement.
