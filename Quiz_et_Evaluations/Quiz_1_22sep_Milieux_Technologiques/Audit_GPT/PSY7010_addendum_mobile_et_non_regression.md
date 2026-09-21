# PSY7010 — Addendum : compatibilité de l’audit et remise en état de l’interface

## Mandat pour l’agent

Travailler sur la version courante du projet, pas en remplaçant le site par le HTML ancien fourni pour l’audit. Corriger l’expérience mobile et le rognage du podcast dans la disposition verticale. Préserver la présentation et les fonctionnalités de bureau, sauf corrections de défauts explicitement décrites ici. Appliquer les corrections académiques dans un changement distinct.

**Version publique examinée :** dépôt `P-s-y-e-n-c-e/psy7010`, jusqu’au commit `3fa9d3329c274d3be2e57a8570400ec8b648a629`, publié le 20 septembre 2026 à 19 h 26, heure du Québec. Toute modification ultérieure doit faire l’objet d’une nouvelle comparaison avant application.

**Site consulté :** `https://p-s-y-e-n-c-e.github.io/psy7010/`.

**Fichier ancien de référence :** `Quiz_entrainement_22sep_PSY7010.html` téléversé pour l’audit. Empreinte SHA-256 des octets : `d10661dcc049287ef297661a929cae8211f6f487ba25bacbc70ab4db04ec29b9`.

### Nature et limites des vérifications

Le site public, le code brut de son dépôt et les différences des cinq commits successifs ont été consultés. Après normalisation CRLF → LF, l’empreinte Git du fichier ancien est `74e904407be6903b198685cf2cf86c471e7dadd5` : elle correspond au fichier de départ indiqué par le premier des cinq correctifs. La comparaison ne repose donc pas seulement sur la ressemblance de Q01 à l’écran.

Des essais de mise en page ont été exécutés dans Chromium sur une copie locale reconstituée à partir du fichier ancien et des modifications publiées. Les essais utilisent des polices de substitution et un stockage local simulé ; les médias externes sont bloqués. Ils ne constituent ni une validation sur un téléphone physique ni un contrôle du flux audio en production. Le téléchargement direct des octets du HTML déployé n’a pas abouti ; la continuité des versions est établie par l’historique du dépôt, non par une comparaison binaire avec la réponse HTTP de production. La copie reconstituée n’est pas un livrable à déployer.

Les faits de code, les observations de reproduction locale et les propositions de conception sont distingués ci-dessous. La capture fournie par Michel montre un contenu coupé au niveau de la séparation quiz/lecteur et du texte tronqué à gauche. Elle ne permet pas, seule, de déterminer la largeur CSS, le zoom ou l’état des préférences de disposition.

---

## 1. Les retouches ont-elles invalidé l’audit académique ?

**Non : les modifications publiées depuis le fichier audité n’ont pas modifié la banque `allQuestions`.** Les 44 questions, leurs 176 options, leurs 176 rétroactions, leurs clés `correctIndex` et leurs métadonnées restent les mêmes. Les dix blocs de lecture — cinq documents en deux langues — ne sont pas modifiés par cette série de commits.

La distribution des clés demeure A = 26, B = 15, C = 3, D = 0. Les problèmes de contenu signalés dans l’audit restent donc à traiter. Cela ne dispense pas l’agent d’évaluer les corrections proposées : absence de modification n’est pas une nouvelle validation scientifique des propositions de l’audit.

### Traçabilité des changements

| Commit | Changement constaté | Incidence sur l’audit |
|---|---|---|
| `463307d` | Ajout de `setInterval(checkQuizExpiration, 30000)` à l’initialisation. | Aucun changement des questions. Modification du comportement d’expiration, à préserver sauf décision explicite. |
| `47a7f50` | Ajout de chemins audio GitHub et modification de la gestion d’un échec de lecture. | Aucun changement des questions. Ne pas annuler cet ajout en restaurant tout l’ancien HTML. |
| `606d80d` | Ajout du bloc CSS mobile ; modifications d’espacements globaux et des ressources. | Aucun changement des questions. Certaines règles touchent aussi le bureau. |
| `9387268` | Agrandissement de caractères et de commandes dans le bloc mobile. | Aucun changement des questions. La surface nécessaire augmente sans réorganisation suffisante. |
| `3fa9d33` | En-tête avec retour à la ligne, nouvelle répartition verticale 54 % / 46 %, changements de dimensions et de barre du lecteur. | Aucun changement des questions. Incidence directe sur le bureau et la séparation quiz/lecteur. |

### Les anciens fichiers restent utilisables

`PSY7010_audit_academique_44_questions.md` et `PSY7010_correctifs_textuels_44_questions.json` restent les références pour le contenu. Appliquer les changements par `id`, jamais par numéro de ligne ou position dans un filtre.

`PSY7010_correctifs_affichage.js` reste pertinent : le rendu lit toujours `q.explanation` et `q.examTip`, alors que les objets possèdent `doc_explanation` et `exam_tip`. Le test local reproduit « Explication théorique : undefined » et le conseil générique. Les mêmes erreurs concernent les cartes de révision. Les guillemets redoublés demeurent également.

**Ne pas ajouter ce fichier JS comme une nouvelle bibliothèque : intégrer ses remplacements dans les fonctions existantes.**

---

## 2. Diagnostic hiérarchisé

### P0 — UX01 : rognage du podcast par la limite du panneau quiz

**Fait de code.** La disposition verticale est passée d’une hauteur de quiz liée au contenu à deux bases flexibles de 54 % et 46 %. `body` reste limité à la hauteur de la fenêtre hors du bloc mobile. Le panneau quiz est défilant ; il peut donc se terminer au milieu du podcast. Le lecteur commence ensuite, donnant visuellement l’impression qu’il recouvre la carte.

**Interprétation à retenir.** Dans les règles examinées, les deux panneaux sont des éléments frères en flux flex. Le problème principal n’est pas démontré comme une superposition par `position: absolute` ou un mauvais `z-index`. C’est une coupure du contenu à la limite de son conteneur, compatible avec la capture. La proportion fixe ne tient compte ni de la longueur de la question, ni des rétroactions, ni du zoom, ni des polices chargées.

**Correction.** Remplacer le ratio initial arbitraire par une hauteur de quiz mesurée sur son contenu naturel, plafonnée afin de conserver une zone de lecture. Quand le contenu ne peut réellement pas tenir, garder un défilement explicite et atteignable dans le quiz. Sur mobile, ne pas conserver cette disposition à deux panneaux.

**À proscrire.** Marge négative, `translateY`, remontée artificielle du lecteur, changement de `z-index`, compensation par une grosse marge fixe ou `overflow: hidden` supplémentaire. Une barre de défilement masquée n’est pas un débordement corrigé.

### P0 — UX02 : frontières mobile/bureau incohérentes

**Fait de code.** CSS décide du mobile avec `max-width: 768px`. `updateDynamicLayout()` décide du haut/bas avec `innerHeight > innerWidth`, puis associe à cette décision la disposition de l’en-tête. Ces deux critères ne désignent pas le même besoin. Un téléphone en paysage peut sortir du bloc mobile. Une fenêtre de bureau en portrait reçoit une navigation verticale. Le clavier virtuel et les changements de dimensions peuvent déclencher des recalculs parasites.

**Correction.** Séparer trois notions : interface compacte, orientation des panneaux de bureau, mode pédagogique. Utiliser une condition de compactage partagée et explicite ; le choix « Haut/Bas / Côte à côte » demeure une préférence de bureau. Une préférence de bureau enregistrée ne doit pas forcer deux panneaux étroits sur téléphone.

**Proposition de départ à tester :** compact si largeur ≤ 48rem ; également compact lorsque hauteur ≤ 32rem et pointeur principal grossier. Ce sont des seuils de conception proposés, pas une norme ni une identification certaine du type d’appareil. Tester notamment le téléphone paysage et les tablettes. Ne pas baser l’ensemble sur le User-Agent.

### P1 — UX03 : navigation mobile empilée sans hiérarchie

**Fait de code.** Le score est placé entre les boutons de modes. Les commandes principales et les préférences sont plusieurs groupes flex avec retour à la ligne ; la classe `nav-vertical-mode` ajoute encore une direction en colonne. L’interface traite presque au même niveau un changement d’activité, un état de progression et une action destructive.

**Observation locale.** À 390 × 844 CSS px, l’en-tête occupe environ 248 px et le haut de la carte de question se situe vers 583 px. À 320 px de largeur, l’en-tête atteint environ 292 px. Les valeurs exactes dépendent des polices et du navigateur ; elles caractérisent la reproduction, pas tous les téléphones.

**Correction.** En-tête compact, progression non cliquable, navigation d’activités alignée, préférences dans « Plus ». Ne pas tenter de faire tenir huit commandes en diminuant leurs caractères.

### P1 — UX04 : sélecteurs du lecteur inexistants

**Fait vérifié.** Aucun élément du HTML examiné ne porte `.reader-tabs-bar`, `.reader-body` ou `.doc-paragraph`.

| Cible du nouveau CSS | Élément réel à traiter |
|---|---|
| `.reader-tabs-bar` | `.reader-header-bar` |
| `.reader-body` | `.reader-viewport` |
| `.doc-paragraph` | `.doc-para`, avec les autres types de paragraphes/listes du lecteur |

Les déclarations de hauteur et de défilement appliquées à `.reader-body` n’ont donc aucun effet. La règle alternative `.reader-pane p` agit, mais seulement sur les éléments `p`, pas uniformément sur listes, citations et autres blocs.

**Correction.** Supprimer les règles mortes ; traiter les éléments réels. Ne pas se limiter à remplacer les noms en conservant `75vh` : choisir d’abord le modèle de défilement. La proposition ci-dessous utilise une seule page défilante dans l’espace mobile actif.

### P1 — UX05 : la pagination devient une colonne comprimée

**Fait de code.** Les libellés Précédente/Suivante sont réaffichés en mobile, les boutons latéraux refusent de rétrécir, et le groupe de numéros conserve le peu de largeur restant. Les numéros peuvent revenir à la ligne tout en étant rognés horizontalement.

**Observation locale.** À 390 px, le groupe central se réduit à environ 88 px de large pour 140 px de haut. À 320 px, il descend à environ 18 px de large : les chiffres ne sont plus présentés comme une navigation lisible.

**Correction.** Une ligne mobile « Précédente — 7 / 44 — Suivante », avec flèches et noms accessibles. Le compteur ouvre un sélecteur de question. Supprimer la pagination à sept positions seulement dans la vue compacte ; la conserver sur bureau.

### P1 — UX06 : les sources sont rejetées après des ressources secondaires

**Fait de structure.** Dans l’ordre actuel, on traverse la question, les rétroactions éventuelles, la carte de promotion des flashcards et le podcast avant d’atteindre le lecteur. Ces mêmes ressources ont déjà des commandes dans l’en-tête.

**Correction.** Sur mobile, rendre le texte source accessible immédiatement depuis la question et réserver une vue au podcast. Ne pas intercaler ces deux cartes promotionnelles entre l’activité principale et sa source. Ne supprimer ni le podcast ni les sources : les déplacer fonctionnellement dans une navigation compacte.

### P1 — UX07 : saut automatique hors de la rétroaction

**Fait de code.** `renderQuestion()` et `renderFlashcard()` appellent `highlightAndScrollSource()`. Cette fonction utilise `scrollIntoView()` sans exploiter réellement son paramètre `forceOpen`. Avec une page mobile défilante, le déplacement peut concerner aussi des ancêtres, pas seulement le petit lecteur.

**Correction.** Sur mobile, une réponse affiche d’abord sa rétroaction et laisse l’utilisateur à cet endroit. La mise en évidence du passage source peut être préparée sans défilement. Seule une commande explicite « Voir le passage source » ouvre la vue de lecture et déplace celle-ci. Au retour, restaurer la question et sa position. Sur bureau, conserver l’usage de consultation simultanée, sans déplacer inutilement le panneau quiz.

### P1 — UX08 : faux défilement naturel mobile

**Fait de code.** Le mobile libère plusieurs conteneurs, mais `.reader-viewport` garde son modèle flex/défilement de bureau. Dans la reproduction à 390 px, la zone réellement disponible au texte n’est qu’environ 260 px de haut, au sein d’un lecteur de 500 px. Les nombreuses commandes consomment le reste.

**Correction.** Un seul propriétaire du défilement principal dans chaque vue mobile. Pour la solution proposée : défilement de page, lecteur de hauteur naturelle, aucune sous-fenêtre fixe de 500 px ou 75vh, sauf composant expressément justifié. En bureau : un défilement pour le quiz et un pour le texte, sans ajouter un deuxième ascenseur inutile autour du lecteur.

### P1 — UX09 : cartes de révision fondées sur des faces absolues

**Risque structurel, à tester sur les contenus longs.** `.fc-face` est en position absolue, tandis que scène et carte reposent sur une hauteur minimale de 310 px. Le verso possède une zone interne limitée à 200 px. Augmenter les caractères ne donne pas automatiquement une hauteur suffisante à ces parents.

**Correction proposée en compact.** Remplacer visuellement le retournement 3D par une révélation recto/verso en flux normal. Seule la face active participe à la mise en page. Le verso et ses commandes d’évaluation suivent la longueur réelle du contenu. Conserver le retournement de bureau. Ne pas raccourcir les synthèses pour les faire entrer dans une carte fixe.

### P2 — UX10 : séparateur tactile encore actif

**Fait de code.** Le CSS mobile met `cursor: default`, mais les écouteurs `touchstart` et `touchmove` demeurent. Modifier le curseur ne désactive pas les interactions. Les dimensions écrites par ces écouteurs peuvent ensuite être contredites par les `!important` du CSS.

**Correction.** Masquer et désactiver le séparateur en interface compacte, y compris au clavier et dans les gestionnaires d’événements. Conserver la fonction en bureau. Ne pas réinitialiser systématiquement une taille choisie par l’utilisateur à chaque événement `resize`.

### P2 — UX11 : largeur cachée plutôt que corrigée

**Constat.** Des conteneurs internes dépassent la largeur disponible alors que `overflow-x: hidden` cache le résultat. Le titre, les textes longs, les commandes audio et les groupes sans retour constituent des cibles à examiner. La cause exacte du rognage à gauche de la capture de Michel n’est pas établie par la seule image.

**Correction.** Utiliser `min-width: 0` sur les éléments flex/grid qui doivent rétrécir, des colonnes `minmax(0, 1fr)`, une largeur disponible de 100 %, et le retour à la ligne des textes longs. Garder les lettres A/B/C/D non rétrécissables, mais permettre au texte de réponse de prendre la largeur restante. Tester les débordements internes, pas uniquement `documentElement.scrollWidth` : un ancêtre qui masque le débordement peut donner une fausse impression de réussite.

### P2 — UX12 : échec audio silencieux

**Fait de changement.** Le gestionnaire de rejet de `audio.play()` rétablit les icônes et écrit un avertissement dans la console. Il ne présente pas à lui seul un message d’échec compréhensible à l’utilisateur.

**Correction.** Conserver l’hébergement ajouté ; présenter un état Chargement/Lecture/Pause/Indisponible et une commande explicite de secours vers le lien existant. Ne pas ouvrir automatiquement un nouvel onglet pour chaque rejet de lecture. Les nouveaux tests doivent couvrir une vraie réponse HTTP audio et une source indisponible. Le flux audio n’a pas été validé dans les essais locaux décrits ici.

---

## 3. Architecture mobile à réaliser

### 3.1 En-tête : identité et état, pas une collection de boutons

Une première ligne affiche `PSY7010`, le progrès sous forme de texte compact, puis `Plus`. Le titre complet et la date peuvent rester visibles dans une présentation secondaire, sans imposer une bannière haute. Le score ne doit pas interrompre la suite des activités.

La commande `Plus` contient le thème, l’accès aux informations utiles et la réinitialisation avec confirmation. La réinitialisation n’est jamais une action de premier niveau voisine d’Étude. La préférence de disposition des panneaux n’est pas exposée comme une commande active en compact.

### 3.2 Quatre activités alignées

Afficher une barre régulière : **Étude | Test | Cartes | Podcast**.

À partir de 360 CSS px environ, quatre colonnes de même largeur sont proposées. En dessous, une grille explicite de deux colonnes et deux lignes reste préférable à quatre boutons trop étroits. Ces seuils doivent également supporter le zoom et les préférences de caractères. Les mots restent visibles : pas une barre composée seulement d’icônes.

Le bouton actif a un état visuel et un état accessible. Si l’agent choisit de vrais onglets ARIA, il doit aussi implémenter leur clavier et leurs relations aux panneaux. Sinon, employer des boutons de navigation avec un état correctement annoncé, sans ajouter un rôle ARIA incomplet.

Limiter les effets décoratifs aux états utiles. Les couleurs de réussite/erreur et l’identification des documents peuvent rester sémantiques. Les menus et boutons courants n’ont pas besoin chacun de leur propre dégradé, contour et ombre.

### 3.3 Vue Étude

Afficher un sélecteur « Section » avec son compte de questions, puis la question. Les longues rangées de pastilles sont remplacées dans cette vue compacte par ce sélecteur. Les filtres demeurent inchangés sur bureau.

Le contexte scientifique et les quatre options restent intégralement lisibles. Ne pas cacher un contexte nécessaire pour répondre. Une commande « Texte source » est disponible avant réponse lorsque les règles du mode actuel l’autorisent ; après réponse, « Voir le passage source » mène précisément à l’extrait.

La rétroaction apparaît sous les options. Précédente/Suivante restent à proximité de la fin de la question ; le compteur ouvre un accès direct aux autres questions. Ne pas imposer que toute question longue entre sans défilement dans une hauteur d’écran.

### 3.4 Vue de lecture

Ouvrir le lecteur existant dans l’espace mobile principal. Afficher « Retour à la question », un sélecteur de document, la langue et l’accès à la recherche. La recherche peut être développée sur demande plutôt qu’imposer en permanence un champ, un compteur et deux flèches.

Afficher le document complet et conserver les dix versions existantes. Le retour restaure la question, la réponse et la position antérieures. Conserver aussi la position de lecture par document et par langue, sauf demande explicite de rejoindre un autre passage.

Dans cette solution, le lecteur est une vue de l’application, **pas un deuxième exemplaire du texte ajouté dans une fenêtre modale**. Éviter la duplication des identifiants, des ancres et des gestionnaires. Le bouton Retour du navigateur doit être pris en compte si l’ouverture crée une entrée dans l’historique ; dans tous les cas, un retour interne explicite est requis.

### 3.5 Vue Podcast

Réutiliser l’élément `<audio>` existant. Présenter le titre, Lecture/Pause, progression, durée et vitesse. Les liens externes restent disponibles dans une section secondaire.

Changer de vue ne recrée pas l’élément audio et ne remet pas sa position à zéro. Si l’écoute continue pendant le quiz, la navigation indique qu’elle est en cours. Ne pas lancer une seconde piste en dupliquant le lecteur. Aucun démarrage automatique.

### 3.6 Vue Cartes

La face active a une hauteur naturelle et contient toute l’information. Révéler la réponse avec une vraie commande utilisable au clavier et au toucher ; éviter que le même événement retourne la carte puis déclenche involontairement une autre action. Les évaluations Difficile/Moyen/Facile restent à la suite du texte, avec des surfaces tactiles suffisantes.

---

## 4. Organisation du code : limiter les conflits

### Séparer les états

Conserver `currentMode` pour les modes existants (`study`, `simulation`, `flashcards`). Ajouter un état d’affichage compact distinct, par exemple `mobileView = 'activity' | 'source' | 'podcast'`.

Ouvrir la source ou le podcast ne doit pas appeler un `setMode()` qui réinitialise un test, son chronomètre, une carte ou le filtre. Ne pas utiliser simultanément trois indicateurs contradictoires pour masquer la même zone (`collapsed`, `hidden` et une valeur inline de `display`) sans préciser quelle fonction en est propriétaire.

Conserver les objets de données et les identifiants existants. Un en-tête mobile peut avoir ses propres identifiants de commandes, synchronisés avec l’état partagé ; il ne faut pas cloner les panneaux de contenu. L’élément masqué doit être absent de la navigation clavier, pas seulement déplacé hors de l’écran.

### Une seule décision compacte

Exemple de contrat d’intégration, à adapter dans les fonctions existantes :

```javascript
const compactMedia = window.matchMedia(
  '(max-width: 48rem), (max-height: 32rem) and (pointer: coarse)'
);

function isCompactUI() {
  return compactMedia.matches;
}
```

Utiliser la même condition pour les styles et les comportements. L’agent doit intégrer le branchement dans `updateDynamicLayout()`, le séparateur et la navigation de sources. Ajouter seulement ce fragment sans remplacer les décisions concurrentes n’est pas une correction.

Un changement de taille qui ne change ni le besoin de compactage ni la disposition voulue ne doit pas reconstruire toute l’interface. Préserver les préférences de bureau dans leur stockage actuel. Sortir du compact restitue ces préférences, sans avoir enregistré « portrait mobile » comme nouveau choix de bureau.

### Exemple de grille, pas un sélecteur supposé existant

La classe `.mobile-modebar` ci-dessous est **un nouveau composant à créer**, contrairement aux anciens sélecteurs erronés du lecteur.

```css
.mobile-modebar {
  display: none;
}

@media (max-width: 48rem), (max-height: 32rem) and (pointer: coarse) {
  .mobile-modebar {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.5rem;
  }

  .mobile-modebar > button {
    min-inline-size: 0;
    min-block-size: 2.75rem;
    padding: 0.5rem 0.25rem;
    white-space: normal;
    line-height: 1.25;
  }
}

@media (max-width: 22.49rem) {
  .mobile-modebar {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

Cible de conception proposée : environ 44 × 44 CSS px pour les petites commandes tactiles isolées ; une réponse longue doit pouvoir grandir. Le minimum du critère WCAG 2.2 AA 2.5.8 est 24 × 24 CSS px, avec exceptions définies : ne pas présenter 44 px comme son minimum obligatoire.

### Défilement mobile

Pour la proposition retenue, libérer la hauteur de la page et des panneaux mobiles actifs ; enlever leur base flexible de bureau et les hauteurs de lecture fixes. Le lecteur actif utilise les vrais sélecteurs `.reader-header-bar` et `.reader-viewport`. Sa barre a une hauteur automatique.

Ne pas supprimer `overflow-y: auto` globalement du bureau. Ne pas ajouter une pile de `!important` pour lutter contre des dimensions toujours réécrites en JavaScript : arrêter d’écrire ces dimensions en compact.

Si des commandes sont fixes ou collantes, leur hauteur réelle et les zones de sécurité du téléphone doivent être prises en compte. Aucun contenu ni élément ayant le focus ne doit passer derrière elles. Préférer une seule barre compacte utile à plusieurs bandes fixes. Respecter la préférence de réduction des mouvements pour défilements et retournements.

---

## 5. Correction spécifique du bureau haut/bas

Cette correction est distincte de la refonte mobile. Ne pas transformer tous les ordinateurs en vue à un panneau.

### Objectif géométrique

Au chargement, placer la séparation après le contenu naturel du quiz lorsque celui-ci tient tout en laissant un lecteur utilisable. Ne pas distribuer systématiquement 54 % de la hauteur au quiz. Si le quiz est plus long, plafonner son panneau et autoriser son défilement. Une limite de panneau défilant n’est pas un contenu perdu, à condition que sa fin et ses commandes soient réellement atteignables.

### Méthode proposée

Mesurer `.quiz-content-wrap` après l’avoir soustrait aux contraintes circulaires : hauteur naturelle, `min-height: 0`, et absence de rétrécissement dans le panneau vertical. Sa mesure doit inclure les ressources et le remplissage inférieur. Mesurer aussi la hauteur disponible du conteneur après l’en-tête réel, pas en retranchant une constante supposée de 68 px.

Calcul conceptuel :

```text
H = hauteur utile du conteneur de travail
D = hauteur du séparateur
N = hauteur naturelle complète du contenu du quiz
R = hauteur minimale de lecteur choisie pour cette configuration

hauteur initiale du quiz = min(N, H - D - R)
```

Ce calcul n’est valable que si le budget restant est positif et compatible avec une hauteur minimale de quiz utilisable. Prévoir explicitement les fenêtres très basses : ne jamais imposer deux minimums dont la somme dépasse H. Dans ce cas, proposer la consultation d’un panneau à la fois ou une répartition défilante adaptée.

R peut, par exemple, partir de 240 CSS px pour le lecteur dans une fenêtre suffisamment haute, mais il s’agit d’un paramètre à tester, pas d’une nouvelle constante universelle. Ne pas inscrire aveuglément cette valeur sur un téléphone paysage.

Utiliser un observateur de redimensionnement pour les changements réels de contenu ou de fenêtre, avec écritures regroupées et changement uniquement lorsque la taille cible diffère. Après un déplacement manuel du séparateur, conserver le choix de l’utilisateur ; ne pas recalculer systématiquement la hauteur automatique à chaque réponse. Reborner ce choix si la fenêtre rétrécit.

### Espacements à rétablir

Prévoir un remplissage inférieur cohérent — par exemple 16 px dans la configuration concernée — après la carte podcast, puis le séparateur. Ne pas cumuler un `margin-bottom` de carte, un grand `padding-bottom` du wrapper et un min-height qui crée encore un vide résiduel. Examiner chacun des trois mécanismes avant de supprimer de l’espace.

Le passage de `width: 100vw` à `width: 100%` et une barre de lecteur à hauteur automatique ne sont pas à annuler automatiquement. En revanche, les changements d’espacements de bureau sans lien avec le défaut demandé doivent être justifiés ou rétablis selon la référence visuelle acceptable.

---

## 6. Ordre de réalisation et contrôle des versions

**Étape A — figer les références.** Conserver le commit courant et les captures de bureau. Extraire la banque `allQuestions`, les dix blocs de lecture et la liste des ancres. Distinguer le HTML à la racine et celui du sous-dossier ; leurs chemins audio relatifs ne sont pas nécessairement identiques.

**Étape B — correctif technique isolé.** Corriger les propriétés d’affichage `doc_explanation` / `exam_tip`, les guillemets ajoutés par le rendu et le rognage vertical. Ne modifier aucun contenu académique dans cette étape. Contrôler la séparation des panneaux avant de reprendre l’apparence mobile.

**Étape C — interface compacte.** Introduire le contrat de compactage partagé, la barre d’activités, le menu Plus, la sélection de section, la navigation simplifiée et les vues Source/Podcast. Nettoyer les règles mobiles contradictoires et les sélecteurs inexistants. Désactiver le séparateur compact. Ne pas reconstruire le site avec un nouveau framework pour ces changements.

**Étape D — contenu académique.** Appliquer ensuite les propositions retenues de l’audit dans un commit distinct. Modifier ensemble chaque énoncé, ses options, ses rétroactions et sa clé ; déplacer les ancres ou ajouter les références complémentaires lorsque requis. La banque doit volontairement changer dans cette étape, mais pas dans B/C.

**Étape E — livraison contrôlée.** Vérifier les deux points d’entrée, les chemins de ressources et l’URL GitHub Pages après publication. Ne pas conclure « mobile corrigé » uniquement parce qu’un émulateur affiche la page initiale à 390 px.

---

## 7. Critères de réception

### Géométrie et lisibilité

Tester 320, 360, 390, 430, 768, 820, 1024, 1280, 1440 et 1920 CSS px selon les formats pertinents. Ajouter les valeurs juste avant, au niveau et juste après les points de rupture. Tester portrait/paysage ; notamment 844 × 390 avec un profil tactile. Tester aussi une fenêtre de bureau de dimensions similaires, sans présumer que toute petite hauteur implique un téléphone.

Contrôler les zooms 100 %, 125 %, 150 %, 200 % et le reflow à une largeur équivalente à 320 CSS px. Un contrôle à 400 % depuis 1280 px peut servir au test de reflow. Tester le grossissement du texte : il ne doit pas être compensé par une réduction forcée des polices ni empêcher d’accéder aux commandes.

Aucune réponse, rétroaction, commande du podcast ou commande de navigation ne doit être inaccessible par rognage. Une question longue peut défiler. Le lecteur ne doit pas recouvrir une carte ; en bureau, la fin d’un panneau défilant doit pouvoir être atteinte. Le thème sombre doit garder des états lisibles, y compris réponse incorrecte et focus clavier.

Les quatre activités principales sont ordonnées et alignées ; le score ne les interrompt pas. Les numéros des questions ne deviennent pas une colonne de chiffres entre les deux flèches. Les éléments cachés sont également exclus du parcours clavier.

### Interactions

Sur les 44 questions : réponse correcte, réponse incorrecte, rétroaction, nouvel essai, précédent/suivant et filtre. Vérifier des rétroactions longues, pas uniquement Q01 avant réponse. Contrôler qu’aucune synthèse n’affiche `undefined`.

Pour les sources : les cinq documents, les deux langues, les ancres, la recherche et le retour à la bonne question. Une réponse mobile ne provoque pas de saut automatique vers le document. Le contexte et les possibilités de consultation du mode Test ne doivent pas changer silencieusement.

Pour les cartes : révélation, retour au recto, navigation, évaluation et sauvegarde des statistiques. Pour le Test : préparation, lancement, réponses, chronomètre et bilan. Ouvrir puis quitter Source/Podcast ne réinitialise pas l’activité en cours.

Pour le podcast : lecture réelle, pause, déplacement dans la piste, vitesse, fin, chargement et erreur. Une seule instance audio. Tester hors connexion ou avec ressource indisponible pour vérifier la clarté du message, sans prétendre que le site est intégralement utilisable hors connexion.

### Préservation du bureau

Comparer des captures avant/après de bureau à données, polices, zoom, animations, progression et thème identiques. Conserver les deux panneaux et les fonctions de séparation. Documenter les différences autorisées : correction du rognage vertical, des explications manquantes et des défauts de reflow. Une modification « générale » des tailles et espacements n’est pas acceptée sans raison.

### Intégrité de contenu

Après les seuls changements B/C, la comparaison structurée de `allQuestions` doit être strictement identique ; les dix blocs de lecture et les ancres doivent rester présents et fidèles. Si des déplacements de DOM sont nécessaires, comparer les sous-arbres pertinents indépendamment de leur parent, plutôt que tout le HTML comme une chaîne.

Après D, chaque changement de données doit correspondre à une correction académique identifiée. Vérifier 44 identifiants uniques, quatre options et quatre rétroactions par question, et un entier `correctIndex` entre 0 et 3. Ne pas changer seulement les indices pour rééquilibrer les bonnes réponses : permuter les options et leurs rétroactions ensemble.

Aucune erreur JavaScript nouvelle. Préserver les clés de stockage et les données de progression existantes. Les réponses uniquement conservées en mémoire dans l’application actuelle ne doivent pas être présentées comme déjà persistantes au rechargement.

---

## 8. Références techniques et pistes de vérification

Les éléments ci-dessous servent à vérifier le code et les critères, pas à justifier une préférence esthétique universelle.

**Historique public :**

- Point de départ et contrôle d’expiration : `https://github.com/P-s-y-e-n-c-e/psy7010/commit/463307d.patch`.
- Modifications audio : `https://github.com/P-s-y-e-n-c-e/psy7010/commit/47a7f50`.
- Premier correctif mobile : `https://github.com/P-s-y-e-n-c-e/psy7010/commit/606d80d.patch`.
- Agrandissement mobile : `https://github.com/P-s-y-e-n-c-e/psy7010/commit/9387268.patch`.
- Répartition et dimensions de bureau : `https://github.com/P-s-y-e-n-c-e/psy7010/commit/3fa9d3329c274d3be2e57a8570400ec8b648a629`.
- Source : `https://raw.githubusercontent.com/P-s-y-e-n-c-e/psy7010/3fa9d3329c274d3be2e57a8570400ec8b648a629/index.html`.

**Documentation primaire :**

- W3C, WCAG 2.2, compréhension de 1.4.10 Reflow : `https://www.w3.org/WAI/WCAG22/Understanding/reflow.html`.
- W3C, WCAG 2.2, compréhension de 2.5.8 Target Size (Minimum) : `https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html`.
- MDN, `min-width` et tailles minimales des éléments flex/grid : `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width`.
- MDN, `Element.scrollIntoView()` et conteneurs affectés : `https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView`.

## Livrable demandé à l’agent

Retourner les fichiers du site corrigés, un résumé des modifications par étape, les captures de comparaison mobile/bureau et les résultats des tests. Signaler explicitement les points non testés. Ne pas retourner simplement une nouvelle feuille CSS non intégrée. Ne pas modifier le contenu scientifique dans le même changement que la disposition sans fournir une comparaison séparée.
