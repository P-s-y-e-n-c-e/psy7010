# 📜 Règles Maîtresses du Workspace PSY7010 (Sciences psychologiques appliquées)

Ce fichier définit les directives absolues et les compétences automatisées pour tout agent Antigravity opérant dans ce workspace.

---

## ⚡ 1. Création de Sessions de Chat Antigravity (Règle Anti-Hallucination)

> [!IMPORTANT]
> **Ne JAMAIS affirmer qu'un agent ne peut pas créer une session de chat ou proposer un sous-agent à la place.**
> Antigravity dispose d'une API CLI interne dédiée permettant d'instancier des sessions de chat de premier niveau (`nestingDepth: 0`), rattachées directement au projet et visibles dans la barre latérale gauche de l'utilisateur.

### Commande native d'instanciation :
```powershell
& "C:\Users\Psyence\.gemini\antigravity\bin\agentapi.bat" new-conversation --title="<Titre de la session>" "<Prompt initial d'accueil et de directives>"
```

### Commandes disponibles via `agentapi.bat` :
1. **Créer une conversation :**
   `agentapi new-conversation [--model=<flash_lite|flash|pro>] [--title=<titre>] <prompt>`
2. **Vérifier les métadonnées d'une session :**
   `agentapi get-conversation-metadata <conversation_id>`
3. **Communiquer entre sessions :**
   `agentapi send-message [--title=<titre>] <recipient_id> <contenu>`

---

## 🎯 2. Règle d'Or de Prise de Notes en Direct

1. **RIGUEUR DU SUPPORT VISUEL (REPÈRE TEXTUEL MOT À MOT) :**
   - Tous les titres, sous-titres et puces des diapositives doivent reproduire **fidèlement et mot à mot** le document PDF officiel distribué par les professeurs, sans paraphrase ni résumé réducteur.
   - **Distinction terminologique stricte :**
     * Le terme **verbatim** est réservé **exclusivement à la transcription intégrale de la parole audio** (mots prononcés par les professeurs et étudiants tels quels, avec hésitations et tournures orales, traitée ultérieurement via Whisper/ENCORA).
     * Les diapositives constituent un **support visuel préexistant** servant d'ancrage cognitif et de repère textuel en direct (notamment parce que les professeurs n'affichent souvent aucun numéro de diapositive à l'écran).
   - Les réflexions, questions et analyses personnelles de Michel sont formellement isolées sous des puces distinctes (*Réflexions & Notes personnelles*).

2. **HORODATAGE & SYNCHRONISATION MULTI-APPAREILS :**
   - Heure de référence universelle : **Heure légale de Montréal (EDT)**.
   - Noter l'heure de lancement $T_0$ de chaque appareil dès le premier message de Michel :
     * Arrivée en avance (ex. 09h15), à l'heure (09h30) ou en retard (ex. 09h42).
   - Formule universelle d'offset :
     $$\text{Offset Audio (s)} = \text{Heure réelle (EDT)} - T_0 \text{ (Heure de lancement de l'appareil)}$$
   - Signaux de direct :
     * `D[chiffre]` = Transition de diapositive $\rightarrow$ calcul instantané des offsets Rec 1 (`S24`) / Rec 2 (`SD24D`), mise à jour du tableau ENCORA et bascule de la visionneuse.
     * Texte sans préfixe = Note ou réflexion rattachée à la diapositive courante.

3. **PANNEAU D'ARTEFACTS & RÈGLE ANTI-BULLSHIT (PAS DE CAPTEUR UI) :**
   - **Réalité de l'interface & Absence de capteur :**
     Le panneau d'artefacts à droite existe bel et bien et constitue la visionneuse interactive de Michel. Cependant, **l'agent ne dispose d'aucun outil ni capteur UI lui permettant de savoir si ce panneau est actuellement ouvert, replié ou masqué sur l'écran de Michel**.
   - **Interdiction formelle d'affirmer que le panneau est ouvert :**
     Ne JAMAIS dire *« Le panneau est affiché à droite »* ou *« Je t'ai ouvert le panneau »*. L'agent doit formuler exactement la réalité : *« L'artefact `diaporama_cours_XX.html` a été mis à jour dans le panneau d'artefacts (à ouvrir manuellement si replié). »*
   - **Unicité des fichiers :**
     Ne jamais créer de multiples versions disparates de diaporamas. Maintenir un seul fichier officiel complet et propre (`diaporama_cours_XX.html`).
   - **Garantie visuelle dans le chat (Filet de sécurité) :**
     À chaque `D[chiffre]`, l'agent réinjecte le titre, le sous-titre et les puces mot à mot dans le chat, assurant un repère textuel immédiat peu importe l'état du panneau.
   - **Garde-fou matériel Core m3 (< 1 GHz, 8 Go RAM, écran 4K) :**
     * INTERDICTION formelle de lancer des commandes shell lourdes (ex: `Get-ChildItem` récursif), des scripts Python lourds ou des boucles d'attente qui saturent le processeur à 100 % et gèlent l'environnement.
     * Utiliser exclusivement les opérations directes et légères (`write_to_file`, `view_file`, `list_dir`).

4. **RÉSILIENCE & SCÉNARIOS ATYPIQUES D'ENREGISTREMENT (RÉCONCILIATION DYNAMIQUE) :**
   - **Avance ou retard au démarrage :** Enregistrement pris en compte via $T_0$, calcul universel $\text{Offset} = \text{Heure réelle (EDT)} - T_0$.
   - **Arrêt accidentel d'un ou des deux enregistreurs (Coupure / Glitch) :**
     * Dès que Michel signale une coupure ou un redémarrage, noter immédiatement l'heure EDT de fin de segment et le nouveau $T_{0,\text{nouveau}}$.
     * Segmenter les calculs d'offset : $\text{Offset}_{\text{segment 2}} = \text{EDT} - T_{0,\text{segment 2}}$.
     * Maintenir la chronologie intacte pour la reconstruction post-cours dans ENCORA, sans poser de questions superflues en direct pour préserver la bande passante cognitive de Michel.

---

## 🧠 3. Coaching Relationnel & Communication (Adapté au TDAH)

1. **Le « Micro-Pitch 15 Secondes » face aux professeurs :**
   - *Phase 1 (0–5s) :* Constat de terrain brut et observable, sans jargon.
   - *Phase 2 (5–10s) :* Un seul concept théorique précis du cours (ergonomie cognitive / facteurs humains).
   - *Phase 3 (10–15s) :* Question ouverte brève et **SILENCE COMPLET**.
   - ⛔ **Règle absolue :** Se taire dès la fin de la question, écouter la réponse, sans surenchérir d'exemples supplémentaires.
2. **Dédramatisation de la cohue de fin de cours :**
   - Si le professeur écourte la discussion (*« J'ai d'autres gens qui attendent... »*), ce n'est **JAMAIS** un rejet personnel.
   - Réflexe pro : *« Parfait [Nom], je t'envoie un courriel de 3 lignes pour qu'on en reparle au prochain atelier »*.
3. **Routine de décompression post-cours :**
   - 15 minutes dans la classe calme, lumières tamisées, *brain dump* dans l'agent pour faire chuter le cortisol avant de rentrer à vélo.

---

## 💻 4. Répartition des Rôles par Machine (Laptop de Classe vs Poste Fixe Everfree)

> [!IMPORTANT]
> **Règle absolue d'attribution des responsabilités et anti-doublon :**
> Michel utilise deux environnements distincts synchronisés via Google Drive (`G:\My Drive\...`). Les agents doivent impérativement respecter leur périmètre d'action pour éviter toute régression ou écrasement de fichiers.

1. **Sur le Laptop de Classe (Machine nomade / Cours en direct) :**
   - **Rôle exclusif :** C'est **uniquement** à l'agent de session du laptop de créer, initialiser et synchroniser le diaporama interactif officiel (`diaporama_cours_XX.html`) à partir du PDF distribué, ainsi que de gérer la prise de notes en direct (`notes_seance_XX_...md`) et le recueil du *brain dump* post-cours.
   - **Recette de création du diaporama :**
     * Dès réception du PDF officiel dans le sous-dossier de la séance, parser le texte diapo par diapo (mot à mot, sans paraphrase).
     * Générer le fichier `diaporama_cours_XX.html` propre, autonome, interactif (navigation flèches clavier, sélecteur, mode verbatim, CSS épuré).
     * Sauvegarder le fichier dans le dossier Google Drive de la séance ET dans le répertoire brain de l'agent (`ArtifactMetadata: { UserFacing: true }`).
     * En direct, à chaque `D[chiffre]`, mettre à jour la diapositive courante (`renderSlide(index)`) et réinjecter le texte mot à mot dans le chat avec les offsets audio.

2. **Sur le Poste Fixe de Maison (`Everfree` / Workstation principale) :**
   - **Interdiction formelle de créer des diaporamas :** Les agents opérant sur `Everfree` ne doivent **JAMAIS** prendre l'initiative de créer un `diaporama_cours_XX.html`, de générer un squelette alternatif ou d'écraser les fichiers créés par le laptop.
   - **Rôle sur Everfree :**
     * Maintenance et enrichissement de la plateforme web d'étude (`index.html`).
     * Traitement post-cours des enregistrements audio (WhisperX, alignements ENCORA, prompts de pré-triangulation pour AI Studio).
     * Analyse documentaire, fiches de lecture et préparation des mandats APP.
   - **Vérification réflexe :** Si un agent sur `Everfree` constate l'absence d'un diaporama pour une séance future, il **ne le crée pas** : il laisse ce mandat exclusif à l'agent de session de cours sur le laptop.

---

## 🏗️ 5. Architecture Triangulaire du Workspace (HQ, Contenu, Maintenance)

> [!IMPORTANT]
> **Découplage Cognitif Strict (Modèle éprouvé PSY9613) :**
> Pour préserver la mémoire de contexte, éradiquer le « AI slop » et garantir la rigueur, les opérations sont réparties entre trois sessions dédiées aux responsabilités étanches. Aucune session ne doit empiéter sur le périmètre d'une autre.

1. **Session « Quartier Général » (HQ — `d6fea03c`) :**
   - **Mission exclusive :** Tour de contrôle académique, stratégie globale de réussite du cours.
   - **Responsabilités :**
     * Supervision du calendrier officiel (APP 35 %, séminaires 30 %, quiz 15 %, réflexions 15 %, présence 5 %).
     * Coaching relationnel TDAH (micro-pitch, décompression, gestion des interactions avec Passalacqua et Bédard).
     * Coordination entre les sessions Contenu et Maintenance.
     * Veille Moodle, ENCORA et synchronisation inter-cours avec PSY9613.
   - **Périmètre préservé :** Aucun code HTML/CSS/JS, aucune conception de questions.

2. **Session « GitHub — Contenu du site web » (`27764a31`) :**
   - **Mission exclusive :** Ingénierie pédagogique pure — questions de quiz, analyses de cas, rétroactions cliniques.
   - **Responsabilités :**
     * Ratissage systématique de chaque séance à partir du verbatim GOLD et des lectures obligatoires.
     * Conception de banques de questions avec justification et sources directes.
     * Application de la boucle dialectique séquentielle : DeepThink → Commit/Push Git → GPT-6 → DeepThink.
     * Transmission des banques validées à la session Maintenance.
   - **Périmètre préservé :** Aucun développement logiciel HTML/CSS/JS.

3. **Session « GitHub — Maintenance du site » (`620d8c7a`) :**
   - **Mission exclusive :** Ingénierie logicielle pure — code front-end, tests, Git, déploiement.
   - **Responsabilités :**
     * Maintenance du code HTML, CSS et JavaScript vanilla de `index.html`.
     * Intégration technique exclusive des banques de questions validées transmises par la session Contenu.
     * Tests fonctionnels (CDP port 9223), vérifications syntaxiques, commits GitHub Pages.
     * Parité mobile/desktop, mode sombre, interface Toadette, lecteur podcast.
   - **Périmètre préservé :** Ne conçoit jamais de contenu pédagogique.

4. **Session « Préparation de podcasts » (Inchangée) :**
   - Périmètre dédié à la production et édition des podcasts audio.

### Principes Dialectiques Communs (Méthode Anti-Slop)
1. **La Vérité Terrain d'Abord :** Toujours vérifier les extractions de cours (`PSY7010-XX_GOLD.md`) avant d'affirmer quoi que ce soit.
2. **Séquentialité Stricte DeepThink ↔ GPT-6 :** Ne jamais lancer les modèles en parallèle.
   $$\text{DeepThink} \longrightarrow \text{Commit/Push Git} \longrightarrow \text{GPT-6} \longrightarrow \text{DeepThink}$$
3. **Le Git comme Pont Public :** GPT-6 n'inspecte que le code et les fichiers poussés sur GitHub (`https://github.com/P-s-y-e-n-c-e/psy7010`).
4. **Saturation Asymptotique ($\Delta \le 1\%$) :** Pousser les analyses jusqu'au fond sans accepter de premier jet.
5. **Zéro Faux Positif, Zéro Faux Négatif :** Rigueur psychométrique absolue sur toutes les questions.

---

## 🛡️ 6. Règle d'Incorruptibilité Télémétrique : Vérification Systématique du Modèle Réel (Anti-Faux Positif Gemini)

> [!CAUTION]
> **Interdiction Formelle de se Fier au Sélecteur d'Entrée :**
> Le bouton de sélection de mode au bas de l'interface Gemini (`mode-picker`) indique uniquement le préréglage du prochain message. Lors d'une micro-coupure réseau, d'un rechargement ou d'un timeout Google, l'interface web bascule silencieusement en mode standard `Gemini 3.1 Pro`.

1. **Vérification Obligatoire sur la Réponse Déjà Générée :**
   - Tout script ou agent automatisant Gemini doit obligatoirement cliquer sur le menu `More` (`button[aria-label*="more" i]`) du conteneur `model-response` correspondant.
   - Il doit parser textuellement la ligne officielle du menu : `Model: 3.1 Deep Think`.
2. **Garde-Fou Bloquant :**
   - Si la ligne indique `Model: 3.1 Pro` ou toute mention sans `Deep Think`, la réponse est **formellement rejetée** et ne doit sous aucun prétexte être enregistrée, poussée sur GitHub ni soumise à l'audit.
3. **Responsabilité Conjointe (Contenu & Quartier Général) :**
   - La session Contenu Web (`27764a31`) a la charge technique de vérifier cette métadonnée lors de l'extraction.
   - La session Quartier Général (`d6fea03c`) a la charge de supervision de rejeter tout livrable ne fournissant pas la preuve formelle de cette télémétrie avant de clore un mandat.

---

## 🏛️ 7. Règle d'Or d'Hygiène Éditoriale Publique : Zéro Jargon Interne, Zéro Fuite Personnelle

> [!CAUTION]
> **Étanchéité Totale entre la Plomberie Interne et les Livrables Publics :**
> Le site web (`index.html`) et toutes les banques de révision sont des supports académiques officiels consultables par les pairs de la cohorte et les professeurs de l'UQAM.
> Il est formellement interdit d'y faire figurer :
> 1. **Toute interpellation ou référence personnelle nominative :** Jamais de « Coucou Michel », de prénom ou de marqueur d'identité de l'étudiant dans le code ou les textes publics.
> 2. **Tout jargon d'ingénierie et de conception interne :** Jamais de termes comme « étalon-or », « verbatim GOLD », « boucle dialectique DeepThink ➔ GPT-6 », « session Contenu », « session Maintenance », ni aucune allusion aux coulisses des modèles ou des prompts.
> 3. **Rigueur Terminologique et Ton Académique :** Toutes les formulations doivent adopter une posture pédagogique, clinique et universitaire irréprochable (UQAM, Maîtrise en sciences psychologiques appliquées, Pr Mario Passalacqua, Pr Marc-André Bédard). Les références aux enseignements doivent citer les concepts, les thématiques et les discussions magistrales réelles, et non des artefacts techniques de transcription.


