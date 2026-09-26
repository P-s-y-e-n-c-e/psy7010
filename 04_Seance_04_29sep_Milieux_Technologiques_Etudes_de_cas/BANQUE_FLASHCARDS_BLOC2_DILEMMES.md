# 🗂️ BANQUE OFFICIELLE DE FLASHCARDS — BLOC 2 (MILIEUX TECHNOLOGIQUES)
## PSY7010 — Sciences psychologiques appliquées : Milieux technologiques
**Cohorte de Maîtrise — Université du Québec à Montréal (UQAM)**  
**Conforme aux cours de Mario Passalacqua & Marc-André Bédard (Séance 3 & 4)**  

---

### 🎯 Pédagogie des Flashcards : Compréhension Clinique & Analyse Diagnostique
Chaque carte est structurée selon une **situation opérationnelle observable** :
- **Recto (Terrain) :** Un incident, une anomalie IHM ou un comportement opérationnel observable.
- **Verso (Ingénierie cognitive) :** Le diagnostic théorique rigoureux, les concepts clés mobilisés et le compromis de conception (*trade-off*).

---

## ✈️ MODULE A : AÉRONAUTIQUE & SYSTÈMES COMPLEXES (AF-447 & AIRBUS)

### 🗂️ Carte 1 — L'Inhibition d'Alarme sous 60 Nœuds (AF-447)
- **Recto (Terrain) :**  
  Sur l'Airbus A330 du vol AF-447, l'alarme sonore de décrochage (*Stall Warning*) s'est tue brusquement alors que l'avion était cabré et en perte d'altitude rapide. Dès que le copilote a poussé sur le manche pour piquer (manœuvre salvatrice), l'alarme a retenti avec violence. Pourquoi cette réaction du système s'est-elle produite ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Invalidation logique des mesures d'incidence par les calculateurs ADR (*Air Data Reference*) dès que la vitesse mesurée chute sous 60 kt. Lorsque le pilote pique, l'avion reprend de la vitesse (> 60 kt), ce qui réadmet les calculs et réactive l'alarme alors que l'avion est toujours en décrochage.  
  **Concept clé :** *Gouffre d'évaluation de Norman* et piège du retour d'information paradoxal. Le silence de la machine mime la sécurité, tandis que la bonne manœuvre est punie par une alerte stridente.  
  **Compromis de conception :** Pudeur algorithmique (ne pas déclencher d'alarmes sur données invalides) vs Sécurité cognitive (ne jamais faire du silence une confirmation trompeuse sous stress extrême).

---

### 🗂️ Carte 2 — Les Mini-Manches Désynchronisés (Side-Sticks Airbus)
- **Recto (Terrain) :**  
  Dans le cockpit d'un Airbus A330, le copilote de gauche a cherché à reprendre le contrôle sans réaliser pendant de longues secondes que le copilote de droite maintenait son manche tiré en arrière à fond de butée. Pourquoi cette information fondamentale lui a-t-elle échappé ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Absence de couplage mécanique et haptique entre les deux mini-manches latéraux (*passive side-sticks*). Le déplacement d'un manche n'entraîne pas le mouvement physique de l'autre, et la position des mains latérales est hors du champ visuel périphérique de l'autre pilote.  
  **Concept clé :** Rupture de la *Conscience de la Situation d'Équipe (Shared Situation Awareness / Endsley Niveau 2)* et disparition de l'affordance écologique sociale.  
  **Compromis de conception :** Réduction de la masse, fiabilité électromécanique et absence de tringlerie lourde vs Perte de la redondance proprioceptive et visuelle immédiate entre équipiers.

---

### 🗂️ Carte 3 — Transition Normal Law ➔ Alternate Law (Surprise de Mode)
- **Recto (Terrain) :**  
  Lorsque le givrage des sondes Pitot a provoqué la perte des indications de vitesse sur l'AF-447, les ordinateurs de bord sont passés de la « loi normale » à la « loi alternative ». Qu'est-ce que ce changement a modifié dans la relation pilote-avion ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** En loi normale, le système de commandes de vol électriques assure une protection d'enveloppe stricte (l'avion refuse physiquement de décrocher même si le pilote tire le manche à fond). En loi alternative, cette protection disparaît totalement sans altération sensible du comportement immédiat des gouvernes.  
  **Concept clé :** *Surprise de mode (Mode Surprise / Sarter & Woods)* et fausse croyance d'invulnérabilité automatisée. L'équipage a pu agir comme si les protections automatiques étaient toujours actives.  
  **Compromis de conception :** Continuité du contrôle manuel dégradé sans blocage logiciel vs Rupture brutale du contrat de confiance homme-machine en phase de crise.

---

### 🗂️ Carte 4 — Les Ironies de l'Automatisation en Croisière (Bainbridge)
- **Recto (Terrain) :**  
  Des pilotes chevronnés passent 98 % de leur temps de vol en croisière à surveiller un pilote automatique. Pourquoi cette assistance prolongée les rend-elle plus vulnérables au moment où l'assistance tombe en panne ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Le phénomène d'exclusion de la boucle de contrôle (*Out-of-the-loop phenomenon*). L'humain n'étant plus actif dans le pilotage direct, son modèle mental de l'état de l'aéronef devient discontinu et imprécis.  
  **Concept clé :** *Ironies de l'automatisation (Lisanne Bainbridge, 1983)*. L'automatisation décharge le pilote des tâches faciles en conditions nominales, mais lui renvoie brutalement la commande manuelle dans les situations imprévues et complexes, au moment où ses compétences actives sont les plus émoussées.  
  **Compromis de conception :** Confort et optimisation de carburant vs Atrophie des habiletés sensori-motrices et allongement du temps de reprise en main (*resumption lag*).

---

## 🏥 MODULE B : TECHNOLOGIES MÉDICALES & SANTÉ (LIN ET AL. 1998)

### 🗂️ Carte 5 — La Vue d'Ensemble en 4 Fenêtres (Pompe Lifecare 4100)
- **Recto (Terrain) :**  
  Dans l'étude de Lin et al. (1998), la nouvelle interface regroupe la concentration, la dose bolus, la période d'interdiction et la limite sur un seul écran divisé en 4 fenêtres titrées. Pourquoi cette organisation réduit-elle les erreurs de 50 % alors que les paramètres à saisir sont exactement les mêmes ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** L'ancienne interface imposait un dialogue séquentiel écran par écran qui obligeait le soignant à stocker en mémoire de travail les valeurs saisies précédemment. La vue d'ensemble fournit une externalisation visuelle permanente de l'état de la prescription.  
  **Concept clé :** *Externalisation de la mémoire de travail (Norman / Zhang & Norman)* et réduction de la charge cognitive extrinsèque (*Sweller*). L'information est disponible dans le monde plutôt qu'en mémoire interne.  
  **Compromis de conception :** Richesse visuelle sur un petit écran (risque d'encombrement / *visual clutter*) vs Navigation séquentielle aveugle.

---

### 🗂️ Carte 6 — Le Paradoxe Statistique du NASA-TLX chez Lin et al.
- **Recto (Terrain) :**  
  L'étude de Lin et al. (1998) montre une baisse spectaculaire des erreurs de programmation (de 20 à 10 erreurs), mais l'analyse de variance (ANOVA) sur la charge mentale globale (NASA-TLX) donne un résultat bilatéral non significatif ($p = 0.12$). Comment interpréter cette discordance ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Deux facteurs expliquent ce paradoxe : (1) La faible taille d'échantillon ($N=12$), et (2) un effet plancher métacognitif : les soignants évaluaient déjà leur charge à des niveaux très bas (15 % vs 7 % de l'échelle), le NASA-TLX statique post-tâche peinant à capturer les micro-pics de charge cognitive transitoires.  
  **Concept clé :** *Non-linéarité entre charge subjective déclarée et performance objective*. Une forte amélioration clinique peut ne pas se traduire par une significativité statistique écrasante sur un questionnaire post-hoc.  
  **Compromis de conception :** Rigueur de la validation réductionniste en laboratoire vs Validité clinique écologique d'un dispositif qui divise par deux les erreurs de programmation.

---

### 🗂️ Carte 7 — La Reprogrammation en Cours de Traitement (Titration d'Urgence)
- **Recto (Terrain) :**  
  Sur les pompes à perfusion d'analgésie contrôlée par le patient (PCA), pourquoi les erreurs de saisie surviennent-elles plus souvent lors d'un changement de dose en cours de perfusion que lors de l'installation initiale ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Lors de l'installation initiale, l'infirmière suit une procédure protocolaire linéaire complète. Lors d'un ajustement de titration, elle est en mode réactif, souvent interrompue par les plaintes de douleur du patient, et modifie un sous-paramètre sans réinitialiser son modèle mental des autres variables verrouillées.  
  **Concept clé :** *Piège d'activation de schéma partiel (Reason, 1990)* et vulnérabilité aux interruptions de tâche (*Altmann & Trafton*).  
  **Compromis de conception :** Accès rapide en un clic pour soulager rapidement le patient vs Forçage de confirmation systématique de l'ordonnance globale.

---

## 🧭 MODULE C : MÉTHODOLOGIE & 4 ÉTAPES (PASSALACQUA & BÉDARD)

### 🗂️ Carte 8 — Étape 1 COMPRENDRE : « L'erreur humaine comme résultat »
- **Recto (Terrain) :**  
  Lorsqu'un accident industriel ou hospitalier survient, un gestionnaire conclut : *« L'accident est dû à l'inattention de l'opérateur qui n'a pas respecté la procédure »*. Pourquoi Mario Passalacqua rejette-t-il catégoriquement cette conclusion dès l'étape COMPRENDRE ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** L'inattention ou l'erreur humaine est un symptôme ou un résultat systémique, jamais la cause première. Conclure à l'erreur humaine bloque l'analyse des facteurs sous-jacents (interface trompeuse, charge mentale, organisation du travail, ambiguïté des procédures).  
  **Concept clé :** *Postulat de Rasmussen & Reason* : « L'erreur humaine décrit le résultat, jamais la cause » (Séance 3 — Pr Mario Passalacqua). L'opérateur adapte son comportement à l'écologie de son poste.  
  **Règle d'or de terrain :** *Observable ≠ Pensée sous-jacente* (Séance 3 — Pr Passalacqua). Observer un comportement ne révèle jamais à lui seul l'intention mentale de l'opérateur.

---

### 🗂️ Carte 9 — Étape 1 COMPRENDRE : La Triangulation Méthodologique
- **Recto (Terrain) :**  
  Pourquoi est-il scientifiquement dangereux d'évaluer la charge mentale d'un opérateur uniquement à l'aide d'un capteur de fréquence cardiaque ou de variabilité cardiaque (VRC) ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Les mesures physiologiques souffrent d'un problème de *non-univocité*. Une élévation cardiaque peut résulter d'un effort physique, d'un stress émotionnel, d'une tasse de café ou d'un sursaut acoustique, sans lien avec la charge de travail cognitive.  
  **Concept clé :** *Triangulation méthodologique obligatoire (Passalacqua — D60 à D67)* :  
  1. Mesures physiologiques (objectives mais non-univoques).  
  2. Mesures perceptuelles / subjectives (NASA-TLX, sensibles mais biaisées par le rappel et la désirabilité sociale).  
  3. Mesures observationnelles / comportementales (précises sur les actions, mais muettes sur les états mentaux internes).

---

### 🗂️ Carte 10 — Étape 2 CONCEVOIR : L'Inspection Automatisée (Cas TSL Outdoors)
- **Recto (Terrain) :**  
  Dans le cas industriel de TSL Outdoors présenté par Mario Passalacqua, une caméra IA inspecte les défauts sur les raquettes à neige avec 99 % de précision. Pourtant, au bout de quelques semaines, les rares défauts non détectés par l'IA passent tout droit sous les yeux de l'opérateur humain. Pourquoi ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** La quasi-perfection apparente de l'automate induit un phénomène de complaisance technologique (*complacency*). L'opérateur humain réduit son balayage visuel actif, son attention s'émousse face à la rareté de l'événement cible (*vigilance decrement*), et il perd son expertise de détection fine.  
  **Concept clé :** *Allocation de fonctions sous-optimale (Fitts' List dépassée / Parasuraman & Wickens)*. L'humain n'est pas un bon superviseur passif de signaux rares.  
  **Compromis de conception :** Vitesse de production robotisée vs Maintien de l'engagement cognitif de l'opérateur (nécessité de générer des contrôles croisés actifs).

---

### 🗂️ Carte 11 — Étape 3 ÉVALUER : Le Dwell Majeur D83 (Effets Secondaires Imprévus)
- **Recto (Terrain) :**  
  Une équipe d'ingénieurs déploie une alarme sonore stridente pour empêcher les ouvriers d'oublier une étape critique. Les tests montrent que l'oubli tombe à 0 %. Pourquoi l'ergonome cognitif refuse-t-il de valider la solution à l'étape ÉVALUER ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** L'évaluation ne doit pas seulement mesurer si la solution résout le défaut initial, mais traquer les *conséquences secondaires imprévues* (Dwell majeur D83, Passalacqua [01:53:40]). L'alarme stridente peut induire une saturation sensorielle, masquer d'autres alertes vitales ou pousser les opérateurs à saboter le haut-parleur avec du ruban adhésif (*workaround*).  
  **Concept clé :** *Effets pervers des rustines IHM et contournements opérationnels*.  
  **Règle Passalacqua :** « Ne pas seulement regarder ce qu'on pense qui est important, regarder plus gros et voir ce qu'on n'a pas prévu ».

---

### 🗂️ Carte 12 — Étape 4 DÉPLOYER : L'Avis Bédard (Validité Contextuelle)
- **Recto (Terrain) :**  
  Une solution d'interface a obtenu des résultats parfaits en laboratoire de simulation à McGill avec des étudiants volontaires. Pourquoi le professeur Marc-André Bédard met-il en garde contre son déploiement direct en milieu réel ?
- **Verso (Ingénierie cognitive) :**  
  **Diagnostic :** Une validation en laboratoire contrôlé ne garantit aucunement la transférabilité écologique (*no one-size-fits-all*, Bédard [02:20:02]). Dans l'usine ou l'hôpital réel, il y a des interruptions constantes, des équipes de nuit fatiguées, des pressions hiérarchiques de cadence et une culture d'entreprise préexistante.  
  **Concept clé :** *Validité écologique et faisabilité organisationnelle (Cañas 2011, Chap. 13)*.  
  **Compromis de conception :** Rigueur du contrôle expérimental en milieu stérile vs Robustesse face au bruit et à la variabilité du monde réel.
