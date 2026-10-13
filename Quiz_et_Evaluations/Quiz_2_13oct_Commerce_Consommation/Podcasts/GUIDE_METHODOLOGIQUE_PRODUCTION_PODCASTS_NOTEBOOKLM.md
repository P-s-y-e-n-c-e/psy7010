# 🎙️ Guide Méthodologique & Playbook de Production Audio (NotebookLM)
## Cours PSY7010 — Sciences psychologiques appliquées (UQAM)
### Session dédiée : `PODCAST - Salle de production` (`c4cc8418-9ede-4afb-9b3b-37c2e4090e79`)

---

## 🧭 1. Philosophie & Règle d'Or : De la Vulgarisation Molle à l'Or Raffiné

Par défaut, lorsqu'on alimente NotebookLM avec de simples articles scientifiques au format PDF, l'algorithme d'« Audio Overview » produit des discussions agréables mais **cognitiverment lisses et superficielles** :
- Les animateurs s'extasient en permanence (« *C'est fascinant !* », « *Tout à fait !* »).
- Les nuances critiques d'examen sont éludées au profit d'un résumé généraliste.
- Le ton dérive vers un français international parisianisé pollué par des tics de langage (« *du coup* », « *en fait* », « *voilà* »).

Pour transformer NotebookLM en une **machine de guerre pédagogique de cycle supérieur**, nous avons conçu un protocole itératif et dialectique en 5 piliers éprouvé lors de la séance 06 (Commerce et consommation 1).

---

## 🛠️ 2. Le Dispositif des « Hack-Sources » (Infiltration Conceptuelle)

Pour briser le biais de lissage de l'IA sans toucher au code interne de Google, nous téléversons en sources actives deux documents textuels synthétiques denses :

### Fichier A — Méta-Document des Controverses Épistémologiques (`05_Meta_Document.txt`)
* **Rôle :** Verrouiller les oppositions théoriques irréconciliables.
* **Contenu type :**
  1. *Rationalité limitée (Simon) vs Optimisation néoclassique :* Le « satisficing » comme adaptation optimale sous contrainte de charge mentale, et non comme de la paresse.
  2. *Théorie des Perspectives (Kahneman & Tversky) :* Courbe en S, aversion aux pertes (douleur double d'un gain équivalent) vs simple aversion au risque.
  3. *Le Grand Schisme définitionnel (Congiu & Moscati, 2022) :* Définition originelle Thaler & Sunstein (2008) vs sens étroit Hansen (2016, exploitation instrumentale des biais) vs sens large Sunstein (2018, information factuelle et GPS).
  4. *Nudge vs Boost (Hertwig & Grüne-Yanoff) :* Dépendance in situ vs émancipation par compétence pérenne.
  5. *Normes sociales (Schultz et al., 2007 / Opower) :* Effet boomerang de la norme descriptive neutralisé par la norme injonctive (smiley moral).

### Fichier B — Fiche d'Ancrage Clinique & Active Recall (`06_Fiche_Ancrage.txt`)
* **Rôle :** Fournir le fil narratif incarné et les tests cognitifs interactifs.
* **Contenu type :**
  1. *Le Parcours de Maya (08h00 à 19h00) :* Comparaison d'assurance, abonnement média avec effet leurre, adhésion par défaut SMarT, facture énergétique Opower.
  2. *Séquence d'Active Recall :* 4 pièges d'examen avec pauses réflexives de 2 secondes.
  3. *Grille décisionnelle du Quiz en 4 critères :* Mécanisme (Type 1/2) $\rightarrow$ Définition (T&S/Hansen/Sunstein) $\rightarrow$ Bénéficiaire (Pro-self/Prosocial) $\rightarrow$ Pérennité (Nudge/Boost).

---

## ✍️ 3. Recette des Prompts Maîtres (Custom Instructions)

Le champ de personnalisation de l'Audio Overview dans NotebookLM accepte jusqu'à 5 000 caractères. Pour obtenir des épisodes de 20 à 25 minutes de calibre exceptionnel, le prompt doit comporter :

1. **Directive sociolinguistique explicite :**
   ```text
   TON ET LANGUE :
   - Français québécois/canadien universitaire d'une rigueur absolue, dynamique, complice et chaleureux.
   - Zéro tic de langage parisien (INTERDICTION FORMELLE de dire « du coup », « voilà », « c'est clair »).
   - Utiliser des repères locaux naturels (« 5 sous », « sacs d'épicerie », « mettons »).
   ```
2. **Attribution de rôles contradictoires (Tension dialectique) :**
   - **Voix 1 :** L'économiste comportemental puriste et intransigeant, gardien des textes originaux (Simon, Kahneman, Thaler, Congiu & Moscati).
   - **Voix 2 :** La chercheuse UX clinicienne, obsédée par la réalité de terrain, la charge mentale et les limites de la verbalisation concourante (*Think-Aloud*).
   - Consigne : *« Ne soyez jamais d'accord immédiatement ! Débattez vivement à chaque étape. »*
3. **Dispositif « Commando Active Recall » :**
   - Imposer exactement 2 à 4 questions pièges avec consigne formelle : *« Annoncez un silence de 2 secondes avant de révéler la clé conceptuelle. Ne lisez aucune métadonnée textuelle à voix haute. »*

---

## ⚡ 4. Automatisation Technique (CDP & CLI `nlm`)

### Interaction avec NotebookLM via Chrome CDP (Port 9223)
* Pour insérer le texte dans la fenêtre modale Angular sans désynchroniser le modèle de données, utiliser :
  ```javascript
  ta.focus();
  ta.select();
  document.execCommand('selectAll', false, null);
  document.execCommand('insertText', false, promptText);
  ta.dispatchEvent(new Event('input', { bubbles: true }));
  ta.dispatchEvent(new Event('change', { bubbles: true }));
  ```
* Vérifier le statut de génération sans saturer le processeur :
  ```powershell
  nlm studio status <notebook_id>
  ```
* Télécharger l'épisode terminé dès propagation de l'URL média :
  ```powershell
  nlm download audio <notebook_id> --id <artifact_id> -o "<chemin_sortie.m4a>"
  ```

---

## 🧠 5. Audit Multimodal Zéro-CPU dans Google AI Studio

> [!CAUTION]
> **Protection du matériel portable (Core m3 / 8 Go RAM) :**
> Ne jamais lancer de transcription Whisper locale ou de calcul lourd sur la machine nomade. Cela sature le CPU à 100 % et bloque l'environnement de travail de Michel.

* **Procédure d'audit native :**
  1. Ouvrir Google AI Studio sur le modèle `Gemini Flash Latest`.
  2. Injecter directement le fichier audio `.m4a` dans la boîte de dialogue via `DOM.setFileInputFiles` (30 000 à 35 000 tokens audio pour un épisode de 15 à 20 minutes).
  3. Lancer la grille d'évaluation matricielle sur 100 points :
     - *Exactitude conceptuelle & Épistémologie :* /30
     - *Posture & Rigueur UX :* /20
     - *Scénarisation & Narration clinique :* /20
     - *Sociolinguistique québécoise & Ton :* /15
     - *Intégration des sources prescrites :* /15
  4. L'inférence s'exécute dans le cloud en 60 à 90 secondes avec **0 % de charge CPU locale**.

---

## 🔄 6. Boucle Dialectique Multi-Modèles (GPT-6.1 Sol ↔ Gemini 3.1 Deep Think)

Pour concevoir le candidat définitif (Le Joyau d'Or) :
1. Générer une série exploratoire de 4 candidats couvrant des angles typés :
   - *C1 : Choc Dialectique* (Tension pure).
   - *C2 : Parcours Usager* (Storytelling chronologique).
   - *C3 : Clinique & Éthique* (Zones grises, opt-out, paradoxe UX).
   - *C4 : Commando Quiz* (Active recall intensif avec pauses).
2. Soumettre les audits des 4 candidats à **GPT-6.1 Sol** et **Gemini 3.1 Deep Think**.
3. Récolter leurs critiques contradictoires pour formuler le *Master Prompt C5*.
4. Générer le **Candidat 5** qui fusionne le meilleur de chaque angle.

---

## 📋 7. Grille d'Arbitrage des Scores Obtenus en Séance 06

| Candidat | Format | Durée | Note /100 | Mention | Recommandation |
|---|---|:---:|:---:|:---:|---|
| **Candidat 1** | Choc Dialectique | 15:38 | 90 / 100 | B+ | Idéal pour le débat sur la taxe de 5 sous |
| **Candidat 2** | Parcours Usager Maya | 14:15 | 93 / 100 | A- | Mémorisation clinique exceptionnelle (08h–19h) |
| **Candidat 3** | Clinique & Éthique | 18:42 | **99 / 100** | **A+** | **Excellence théorique, éthique et UX intégrale** |
| **Candidat 4** | Commando Quiz | 06:45 | **98 / 100** | **A+** | **Bootcamp d'Active Recall avec pauses de 2s** |
| **Candidat 5** | **Le Joyau d'Or** | **23:15** | **99+ / 100** | **Élite** | **La capsule de référence absolue pour la cohorte** |

Ce protocole garantit à la session `PODCAST - Salle de production` une autonomie totale, une reproductibilité scientifique irréprochable et un gain de temps massif pour tous les quiz et séminaires à venir.
