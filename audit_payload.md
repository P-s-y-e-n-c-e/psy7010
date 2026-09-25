# 📄 DOSSIER D'INGÉNIERIE COGNITIVE POUR AUDIT — SÉMINAIRE 1 (10 %)
## PSY7010 — Sciences psychologiques appliquées : Milieux technologiques
**Université du Québec à Montréal (UQAM) — Trimestre d'Automne 2026**  
**Séance du Mardi 29 septembre 2026**  
**Évaluateurs :** Pr Mario Passalacqua (PhD), Pr Marc-André Bédard (PhD)  
**Conférencier invité :** Pr Mario Fiset (Aviation civile & Ergonomie aérospatiale)  
**Étudiant :** Candidat  

---

### 🎯 CONSIGNES OFFICIELLES DU SÉMINAIRE (SÉANCE 3 & PLAN DE COURS)
- Remise obligatoire d'**une feuille écrite de deux questions critiques ouvertes** à la fin du séminaire.
- **Question 1 :** Cas d'ingénierie aérospatiale du **Vol AF-447** (Airbus A330).
- **Question 2 :** Cas d'ergonomie médicale et hospitalière de **Lin et al. (1998)** (Pompe PCA Lifecare 4100).
- **Format exigé :** Structure concise en trois volets (*Constat observable sans jargon > Concept théorique précis > Question ouverte sur un compromis de conception*), calibrée pour une prise de parole percutante de 15 secondes.
- **Exclusivité :** Ces questions sont réservées à la remise notée de Candidat et sont distinctes des banques publiques de la cohorte.

---

## ✈️ QUESTION 1 — VOL AF-447 : COORDINATION DES COMMANDES ET RETOUR HAPTIQUE

### 📝 Texte officiel à imprimer pour la remise (30 mots — ~12 secondes) :
> **« Sur AF447, les mini-manches ne sont pas mécaniquement couplés. Cela interroge la conscience partagée d’Endsley. Comment tester un retour haptique pour améliorer la coordination sans gêner la reprise de priorité ? »**

### 🔍 Décorticage et rigueur scientifique :
1. **Constat de terrain observable (Rapport officiel BEA) :** Sur l'Airbus A330, les mini-manches latéraux (*side-sticks*) sont indépendants et dépourvus de liaison mécanique. En cas d'actions simultanées, le système effectue une sommation algébrique des ordres avec alerte sonore/visuelle (*Dual Input*), mais aucun retour d'effort physique n'informe passivement un pilote du mouvement imprimé par son collègue.
2. **Concept d'ingénierie cognitive :** *Conscience de la situation partagée (Shared Situation Awareness — Endsley)*. Dans un cockpit multipilote en situation d'urgence, la coordination repose sur la perception mutuelle immédiate des actions en cours sans exiger une redirection du regard vers des témoins visuels.
3. **Compromis de conception (*Trade-off*) :** Restitution de la transparence sensorielle et de la coordination intuitive vs risque de confusion biomécanique, de résistance tactile involontaire ou de perturbation lors d'une reprise d'urgence de la priorité de pilotage.
4. **Question de relance pour la discussion orale :**
   * *« Professeur Passalacqua [ou Professeur Fiset], quel protocole d'évaluation permettrait de décider si un retour haptique apporte un bénéfice net, lorsque l'on teste systématiquement un signal erroné, une indisponibilité capteur et une reprise de priorité sous stress ? »*

---

## 🏥 QUESTION 2 — CAS LIN ET AL. (1998) : REPRISE DE PROGRAMMATION ET REVALIDATION

### 📝 Texte officiel à imprimer pour la remise (32 mots — ~13 secondes) :
> **« Chez Lin, REVIEW/CHANGE change de fonction selon l’étape. Le délai de reprise après interruption reste à évaluer. Comment tester une revalidation obligatoire des réglages sans retarder les soins ni favoriser les contournements ? »**

### 🔍 Décorticage et rigueur scientifique :
1. **Constat de terrain observable (Lin et al., 1998) :** Dans la pompe PCA Lifecare 4100, la commande `REVIEW/CHANGE` présente une ambiguïté contextuelle : elle permet de reculer d'un pas pendant la saisie des paramètres, mais fait avancer séquentiellement dans la révision une fois la programmation amorcée.
2. **Concept d'ingénierie cognitive :** *Délai de reprise cognitive (Resumption Lag — Altmann & Trafton)* et *Fonctions de forçage (Norman)*. Lors d'une interruption clinique imprévue au chevet du patient, l'opérateur doit reconstruire l'état exact de la machine avant d'agir.
3. **Compromis de conception (*Trade-off*) :** Sécurisation algorithmique par revalidation bloquante systématique vs charge temporelle en soins intensifs et risque d'induire des contournements informels (*workarounds*) par le personnel soignant.
4. **Question de relance pour la discussion orale :**
   * *« Professeur Passalacqua, à guidage et limites de dose identiques, quelles données probantes vous feraient retenir ou rejeter une étape de revalidation obligatoire après interruption, en mesurant à la fois les erreurs résiduelles, les délais de soin et les contournements clandestins ? »*

---

## 🧭 MATRICE MÉTHODOLOGIQUE DES 4 ÉTAPES (PASSALACQUA & BÉDARD)

| Étape de la démarche | Question 1 : AF-447 (Aviation civile) | Question 2 : Lin et al. 1998 (Santé hospitalière) |
|---|---|---|
| **1. COMPRENDRE**<br>*(Observable ≠ Pensée sous-jacente)* | Reconstituer précisément les commandes, les alertes d'affichage, les annonces vocales et les transferts de priorité ; identifier les vecteurs sensoriels effectivement disponibles sans présumer des intentions internes des pilotes. | Observer in situ les interruptions réelles au chevet, la structure des états de programmation et les stratégies spontanées de reprise ; distinguer une reprise motrice rapide d'une reprise cognitivement correcte. |
| **2. CONCEVOIR**<br>*(Allocation de fonctions & Trade-offs)* | Modéliser l'information transmise par un retour d'effort actif (*Active Inceptors*) et anticiper ses interactions avec les logiques de désengagement et de bouton de priorité. | Comparer une assistance visuelle à la reprise d'état avec une fonction de forçage exigeant une revalidation active, à limites de dose pharmacologiques inchangées. |
| **3. ÉVALUER**<br>*(Traque systématique des effets pervers)* | Tester en simulateur sous charge élevée les scénarios critiques : absence de retour, retour erroné, actions asynchrones et mesure du délai de résolution effective du conflit. | Évaluer en protocole double tâche avec interruptions contrôlées : mesurer les erreurs de titration, le temps de récupération, les retards d'administration et les tentatives de validation aveugle. |
| **4. DÉPLOYER**<br>*(Validité contextuelle et terrain — Bédard)* | Analyser l'intégration technique aux calculateurs avioniques, la formation sur les nouveaux modes de défaillance haptique et le suivi de maintenance opérationnelle. | Valider le transfert sur automate physique en service clinique réel avec des infirmières en rotation de nuit ; suivre l'émergence d'éventuels contournements procéduraux organisationnels. |

---

## 💼 QUESTIONS DE RÉSERVE (VARIANTE MÉTHODOLOGIQUE B)
*Si la discussion de classe aborde déjà les mini-manches ou les interruptions hospitalières, utiliser cette seconde paire entièrement calibrée :*

- **Variante AF-447 (Disponibilité de l'alarme — 28 mots) :**  
  > *« Sur AF447, certaines actions à piquer réactivent l’alarme de décrochage. Cela interroge le gouffre d’évaluation de Norman. Comment évaluer un signal d’indisponibilité sans retarder la reconnaissance du danger ? »*
- **Variante Lin et al. (Vue d'ensemble et mémoire de travail — 31 mots) :**  
  > *« Chez Lin, la refonte modifie plusieurs éléments de l’interface. La vue d’ensemble pourrait réduire les exigences de mémoire de travail. Comment isoler son effet sur les erreurs après une interruption réaliste ? »*

---

### 🏛️ VALIDATION SCIENTIFIQUE ET FACTUELLE
- **Sources primaires contrôlées :** Rapport officiel du BEA (Vol AF-447), article original Lin, Isla, Donchin et al. (1998, *Human Factors*), chapitre 13 Cañas (2011), enseignements magistraux des Prs Passalacqua et Bédard.
- **Rigueur éditoriale :** Document exempt de tout jargon interne de développement, directement imprimable pour la remise officielle du mardi 29 septembre 2026.
