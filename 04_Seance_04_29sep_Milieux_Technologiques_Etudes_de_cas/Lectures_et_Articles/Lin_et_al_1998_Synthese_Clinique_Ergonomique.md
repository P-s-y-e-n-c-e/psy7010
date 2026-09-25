# 🏥 Synthèse Clinique & Ergonomique : Lin et al. (1998)
## Application de l'ingénierie des facteurs humains à la conception des dispositifs médicaux : L'analgésie contrôlée par le patient (PCA)
**Référence officielle :** Lin, L., Isla, R., Doniz, K., Harkness, H., Vicente, K. J., & Doyle, D. J. (1998). *Applying human factors to the design of medical equipment: patient-controlled analgesia*. Journal of Clinical Monitoring and Computing, 14(4), 253–263.  
**Affiliations de recherche :** Cognitive Engineering Laboratory & Institute of Biomedical Engineering, University of Toronto ; Department of Anaesthesia, Toronto General Hospital (TGH).  
**Cadre académique :** PSY7010 — Sciences psychologiques appliquées : Milieux technologiques (UQAM).

---

### 1. Mise en Contexte Clinique & Problématique Systémique

Dans les unités de soins post-opératoires et d'oncologie, les pompes d'analgésie contrôlée par le patient (*Patient-Controlled Analgesia* — PCA) permettent aux patients de s'auto-administrer par voie intraveineuse des doses programmées de morphiniques (morphine, hydromorphone). L'appareil repose sur un équilibre pharmacologique et ergonomique strict : soulager la douleur aiguë tout en respectant une période de verrouillage (*lockout interval*) pour prévenir toute dépression respiratoire potentiellement fatale.

Historiquement, les données de matériovigilance de la FDA (*Center for Devices and Radiological Health*) attribuaient **60 % des décès et blessures graves liés aux dispositifs médicaux à des « erreurs de l'opérateur »**. Dans le domaine des pompes PCA, les erreurs de programmation infirmière constituent la première cause d'incidents critiques (surdoses massives ou sous-dosages sévères), surpassant les défaillances mécaniques (effet de siphon) et les erreurs du patient. 

Face à ce constat, l'approche biomédicale et hospitalière traditionnelle s'est bornée à prescrire davantage de formation et de rappels procéduraux. Lin et ses collaborateurs rejettent ce réflexe tautologique : **le problème réside dans l'opacité et l'inadéquation cognitive de l'interface utilisateur**. Plutôt que d'exiger des soignants qu'ils compensent des défauts de conception par un surcroît de vigilance sous haute tension, l'ingénierie des facteurs humains doit adapter la machine aux capacités et limites de la cognition humaine.

---

### 2. Analyse Cognitive de la Tâche & Diagnostic de l'Interface Standard

L'équipe de Toronto a mené une **analyse cognitive de la tâche** (*Cognitive Task Analysis* — CTA) sur l'un des infuseurs les plus répandus sur le marché hospitalier nord-américain : l'**Abbott Lifecare 4100 PCA Plus II**. Cette évaluation a combiné des tests sur banc d'essai (cartographie détaillée des états et flux système) et une étude de terrain au bloc de réveil (*Post-Anesthesia Care Unit*) du Toronto General Hospital (8 visites, 9 infirmières observées sur 30 programmations réelles).

L'analyse a mis en lumière cinq failles ergonomiques majeures :

#### A. Discontinuité et opacité de la structure du dialogue
L'interface standard guide l'utilisateur à travers un défilement séquentiel d'écrans sur un écran LCD très étroit. Le soignant ne dispose d'**aucune vue d'ensemble du dialogue** :
- Impossible de savoir combien de paramètres restent à programmer, ni où l'on se situe dans l'arborescence.
- Les choix liés (par exemple la sélection du mode opératoire : *PCA seule*, *Continu seul*, ou *PCA + Continu*) sont présentés comme trois décisions isolées successives en boucle fermée, plutôt que sous forme d'un menu parallèle.
- La structure impose une lourde charge sur la mémoire de travail (*working memory load*), particulièrement vulnérable aux interruptions fréquentes en salle de réveil.

#### B. Ambiguïté et multifonctionnalité trompeuse des commandes physiques
Le panneau de boutons-poussoirs (*touch switches*) souffre d'incohérences de libellés et d'un couplage arbitraire :
- **`ON` vs `RESET/START` :** Le bouton `ON` déclenche soit un démarrage à chaud (maintien des paramètres si éteint depuis moins d'une heure), soit un démarrage à froid (effacement des paramètres si éteint depuis plus d'une heure). Le bouton `RESET/START` ne réinitialise rien : il démarre ou arrête l'infusion continue.
- **`REVIEW/CHANGE` :** Touche multifonctionnelle hautement confuse. Pendant la programmation, elle sert à reculer dans la séquence d'un nombre variable et imprévisible d'écrans (bris de cohérence). Une fois la programmation terminée, la même touche fait avancer séquentiellement vers l'avant pour réviser les paramètres.

#### C. Récupération d'erreur laborieuse et absence de voies de sortie (*Exits*)
Si une infirmière dépasse par inadvertance la valeur de concentration souhaitée (ex. 2,0 mg/ml), le système ne permet pas de reculer d'un pas. L'opérateur est forcé de faire défiler toutes les options prédéfinies en boucle pour recommencer la saisie, ce qui allonge considérablement le délai de paramétrage.

#### D. Non-concordance des valeurs par défaut
Les concentrations pré-enregistrées par défaut en usine ne correspondaient pas aux protocoles cliniques réels de l'hôpital (ex. le protocole standard à 2,0 mg/ml nécessitait de traverser 4 écrans de confirmation superflus).

#### E. Conséquences cliniques directes
Une mauvaise sélection de l'unité ou un glissement dans la séquence de saisie peut transformer une concentration de 1 mg/ml en 10 mg/ml, multipliant par dix la quantité de narcotique administrée au patient sans que l'interface ne signale visuellement cette incohérence d'échelle.

---

### 3. Conception de l'Interface Alternative (HF-Interface)

En appliquant les principes fondamentaux de Norman (*The Design of Everyday Things*) et de l'ingénierie écologique de Vicente et Rasmussen, les chercheurs ont développé un prototype informatique de l'interface sans modifier les contraintes technologiques ou les coûts matériels de production :

```
+-----------------------------------------------------------------------+
|  MODE ACTIF: PCA + CONTINU           [ÉCRAN LCD ÉLARGI]              |
|  +--------------------+---------------------------------------------+ |
|  | 1. CONCENTRATION   | Débit Continu:       1.0 ml/h               | |
|  | 2. MODE            | Dose Bolus (PCA):    0.5 ml                 | |
|  | 3. PARAMÈTRES [x]  | Période Verrou:      10 min                 | |
|  |                    | Limite 4 Heures:    15.0 ml                 | |
|  +--------------------+---------------------------------------------+ |
|  Rétroaction permanente : Statut visible, position courante balisée  |
+-----------------------------------------------------------------------+
|  COMMANDES DE PROGRAMMATION           FONCTIONS SPÉCIALES             |
|       [ OUI ]       [ HAUT ^ ]              [ DOSE BOLUS ]            |
|       [ NON ]       [ BAS  v ]              [ RÉVISION   ]            |
|      [ DÉPART ]    [ ARRÊT  ]              [ HISTORIQUE ]            |
|                                             [ MARCHE/ARRÊT ]          |
+-----------------------------------------------------------------------+
```

Les innovations ergonomiques majeures comprennent :

1. **Visibilité intégrale de l'état système (*Knowledge in the World*) :**
   - Écran LCD élargi divisé en zones fonctionnelles permanentes : affichage du mode sélectionné, menu de progression en trois étapes claires (Concentration ➔ Mode ➔ Paramètres), et fenêtre des messages d'action.
   - L'infirmière sait instantanément où elle se trouve, ce qui a été complété et ce qu'il reste à programmer, éliminant la charge mnésique de rétention.

2. **Présentation parallèle des options de décision :**
   - Remplacement des boucles de défilement séquentiel par des menus où toutes les alternatives d'un même choix (ex. les 3 modes opératoires) sont visibles simultanément à l'écran.

3. **Organisation spatiale et unifonctionnalité des commandes :**
   - Séparation stricte entre les touches de programmation courante (haut) et les touches de fonctions spéciales (bas).
   - Regroupement spatial logique : `OUI` au-dessus de `NON`, `DÉPART` au-dessus de `ARRÊT`, flèche `HAUT` au-dessus de flèche `BAS`.
   - Règle « une touche physique = une seule fonction dédiée ». Remplacement du label trompeur `LOADING DOSE` par `BOLUS DOSE` et suppression de la double commande `REVIEW/CHANGE` au profit d'une fonction `RÉVISION` stable et prévisible.

4. **Sommation et revalidation globale :**
   - Ajout d'une touche `HISTORIQUE` permettant d'afficher à tout moment un récapitulatif complet des paramètres.
   - Présentation obligatoire et synthétique de tous les réglages avant le verrouillage de la pompe et la mise sous perfusion du patient.

5. **Réduction drastique de la complexité du dialogue :**
   - La nouvelle interface passe d'un intervalle de **8 à 27 écrans** (sur l'ancienne) à un intervalle compact de **8 à 12 écrans**, soit une **réduction de 56 % du nombre maximal d'étapes de dialogue**.

---

### 4. Protocole Expérimental & Résultats Empiriques

L'évaluation a été menée auprès de **12 étudiantes en sciences infirmières** de l'Université de Toronto (sans expérience préalable sur la pompe Lifecare 4100).

- **Devis expérimental :** Plan mixte factoriel $2 \times 3 \times 2 \times 2$ :
  * Facteur intra-sujet : Interface (Ancienne vs Nouvelle).
  * Facteur intra-sujet : Tâche de programmation (PCA, Continu, PCA + Continu).
  * Facteur intra-sujet : Répétitions (Bloc 1 vs Bloc 2).
  * Facteur inter-sujet : Ordre d'exposition (Ancienne en premier vs Nouvelle en premier).
- **Mesures recueillies :** Temps de complétion total, nombre d'erreurs de programmation, et charge mentale subjective évaluée via l'échelle multidimensionnelle **NASA-TLX**.

#### Résultats statistiques officiels :

| Métrique d'évaluation | Interface Ancienne | Interface Nouvelle (HF) | Test Statistique & Signification |
|---|---|---|---|
| **Temps moyen de programmation** | 2,03 minutes | 1,76 minutes | $F(1,11) = 6,85,\ p < 0,025$ (**-15 % de temps**) |
| **Nombre total d'erreurs** | 20 erreurs | 10 erreurs | $\chi^2(1) = 3,33,\ p < 0,05$ unilatéral (**-50 % d'erreurs**) |
| **Score moyen de charge NASA-TLX** | 15 % | 7 % | $F(1,11) = 2,2,\ p = 0,12$ (bilatéral) ; $\chi^2(1) = 4,45,\ p < 0,025$ |
| **Préférence subjective déclarée** | 0 / 12 (0 %) | 12 / 12 (100 %) | Adhésion unanime pour la nouvelle interface |

#### Phénomènes cognitifs remarquables observés :
1. **Asymétrie de transfert d'apprentissage (*Order $\times$ Interface Interaction*, $p < 0,01$) :**  
   Les participantes ayant commencé sur l'ancienne interface ont vu leurs performances s'améliorer considérablement en passant sur la nouvelle (-0,59 min). En revanche, celles ayant commencé sur la nouvelle interface n'ont presque pas progressé en découvrant l'ancienne (-0,05 min). L'interface mal conçue a agi comme un frein inhibiteur, neutralisant les bénéfices de la pratique antérieure.
2. **Subtilité psychométrique de la charge perçue :**  
   Bien que l'ANOVA globale bilatérale sur le score NASA-TLX n'atteigne pas le seuil classique ($p = 0,12$), la charge mentale perçue moyenne a été divisée par deux (15 % vs 7 %), et 82 % des participantes ont ressenti une charge de travail plus élevée avec l'ancienne interface. Cela illustre la difficulté des questionnaires post-hoc à capturer des micro-pics de tension cognitive lorsque les scores globaux se situent au plancher de l'échelle.

---

### 5. Portée Théorique, Limites et Implications pour le Cours PSY7010

Cette recherche pionnière démontre empiriquement qu'une part massive des accidents médicaux attribués à la « négligence » ou à la « fatigue » des soignants est en réalité **provoquée par l'incompétence ergonomique des systèmes informatisés**.

Pour l'ergonome et le psychologue du travail (démarche en 4 étapes de Passalacqua & Bédard) :
- **Étape 1 (Comprendre) :** L'analyse de terrain et l'analyse cognitive de la tâche sont indispensables pour observer le décalage entre la tâche prescrite par le manuel et l'activité réelle dans le tumulte d'un service hospitalier.
- **Étape 2 (Concevoir) :** L'organisation visuelle et spatiale (*externalisation de l'information*) allège la charge de travail mnésique et rend les erreurs immédiatement observables avant l'administration du produit.
- **Étape 3 (Évaluer) :** L'évaluation ne peut se limiter à des avis subjectifs de convivialité (*user-friendly*) ; elle exige des protocoles expérimentaux mesurant objectivement les temps, les taux d'erreurs et les transferts d'apprentissage.
- **Étape 4 (Déployer / Limites du modèle) :** Lin et al. soulignent lucidement que leur étude a été conduite sur simulateur d'ordinateur (clavier/souris) auprès d'étudiantes novices. Le déploiement clinique à grande échelle d'une nouvelle interface physique exige de vérifier le transfert d'habiletés chez des infirmières chevronnées déjà conditionnées aux anciens réflexes moteurs, sous peine de générer de nouveaux types d'erreurs de substitution d'habitudes.
