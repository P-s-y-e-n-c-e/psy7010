# 🎯 MANDAT PRIORITAIRE — SÉMINAIRE 1 (Mardi 29 septembre 2026)
## Destinataire : Session « GitHub — Contenu du site web » (`27764a31`)
### Émetteur : Quartier Général PSY7010 (`d6fea03c`) | Responsable : Michel Mercier
### Échéance : Mardi 29 septembre 2026 (09h30 EDT) | Poids : 10 % de la note finale

---

## 📌 1. CADRAGE STRATÉGIQUE DU MANDAT

Pour la Séance 4, le cours porte sur les **milieux technologiques et l'analyse d'études de cas réels**. Les professeurs Mario Passalacqua (responsable du bloc) et Marc-André Bédard accueillent un conférencier invité, le Pr Mario Fiset (facteurs humains et aéronautique).

**Livrable exigé à la fin du cours :**
Une feuille imprimée unique comportant **deux questions ouvertes critiques** remises au professeur :
1. **Question 1 :** Sur l'accident du vol **Air France AF-447** (Rio-Paris, 2009).
2. **Question 2 :** Sur l'ergonomie de l'auto-injecteur d'analgésie contrôlée par le patient (**Lin et al., 1998**).

---

## 📚 2. SOURCES DE VÉRITÉ TERRAIN SUR GITHUB

Avant d'interroger GPT-6, assure-toi que les fichiers sont committés et utilise les liens directs vers `https://raw.githubusercontent.com/P-s-y-e-n-c-e/psy7010/main/...` :
1. **Verbatim GOLD Séance 3 :** `03_Seance_03_22sep_Milieux_Technologiques/PSY7010-03_GOLD.md`
2. **Extraction acoustique RAW Séance 3 :** `03_Seance_03_22sep_Milieux_Technologiques/PSY7010-03_RAW_PRETRIANGULATION.json`
   * *Consigne de fallback :* Si un passage du GOLD semble ambigu ou tronqué, vérifier dans le RAW, en gardant en tête les hallucinations acoustiques possibles de Whisper. C'est la confrontation des deux qui fait foi.
3. **Texte Lin et al. (1998) :** `04_Seance_04_29sep_Milieux_Technologiques_Etudes_de_cas/Lectures_et_Articles/Lin_et_al_1998_Patient_Controlled_Analgesia.pdf`
4. **Supports Moodle AF-447 :**
   - Vidéo A1 (YouTube) : *Le vol AF-447 : Que s'est-il vraiment passé ?*
   - Article A2 (Web) : *Facteurs humains de l'ingénierie : Le vol Air France 447*
5. **Cadre méthodologique :** Les 4 étapes de Passalacqua (Comprendre ➔ Concevoir ➔ Évaluer ➔ Déployer).

---

## ⚔️ 3. PROTOCOLE DIALECTIQUE ADVERSARIAL SÉQUENTIEL

Tu dois piloter la boucle entre nos deux stations dédiées :
- **DeepThink :** `scripts/gemini_7010_client.js` (Gem `Auditeur Doctoral PSY7010`, ID `49d384634d73`)
- **GPT-6 :** `scripts/chatgpt_7010_client.js` (`UQAM - PSY7010 - Audit station`)

### La boucle obligatoire :
1. **Élaboration par DeepThink :**
   - Formuler 3 à 4 propositions candidates pour la Question AF-447 et 3 à 4 pour la Question Lin 1998.
   - Chaque question doit suivre la structure du **Micro-Pitch** :
     * Constat terrain précis (5s).
     * Concept théorique sous-jacent (Conscience de la situation N1/N2/N3 Endsley, Modèle SRK Rasmussen, Taxonomie Reason, Complaisance d'automatisation Bainbridge).
     * Question ouverte provocatrice, méthodologique et inattaquable.
2. **Commit & Push Git :** Sauvegarder les propositions brutes dans `04_Seance_04_.../Dossier_Audit_GPT6/` et pousser sur `origin/main`.
3. **Audit sans complaisance par GPT-6 :**
   - Transmettre les liens GitHub à GPT-6 via `chatgpt_7010_client.js`.
   - Ordre d'attaque à GPT-6 : Détecter les questions trop convenues, les clichés de salon, le manque d'ancrage dans la réalité de l'ingénierie cognitive, ou l'absence de lien avec les 4 étapes de Passalacqua.
4. **Contre-attaque DeepThink :**
   - Réinjecter les critiques dans DeepThink pour aiguiser les formulations jusqu'au niveau diamant.

---

## 🛡️ 4. CONSIGNES SUPRÊMES DE MICHEL MERCIER

1. **La règle du 1 % bonifiée :** Même si le delta $\Delta \le 1\%$ semble atteint, on ne s'arrête pas la nuit si on peut continuer à affiner et durcir la rigueur académique.
2. **Incorruptibilité épistémique :** Ne jamais accepter un message d'auto-satisfaction d'un modèle (« travail parfait », « mission accomplie »). C'est toi qui juges, en arbitrant DeepThink contre GPT-6.
3. **Surveillance des blocages :**
   - Si DeepThink affiche une erreur ➔ relancer ou cliquer sur Réessayer.
   - Si ChatGPT décroche sans générer après sa recherche web (bouton stop disparu) ➔ injecter `"Continue."`.
4. **Périmètre strict :** Aucun code de site web. Tout le contenu validé sera transmis à la session Maintenance.
