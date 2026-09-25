# Protocole & Règles de Prise de Notes — Séance 4 (PSY7010)

* **Date de la séance :** Mardi 29 septembre 2026 (09h30 – 12h30 EDT)
* **Lieu :** Pavillon Adrien-Pinard, Local SU-1550
* **Thème du cours :** Milieux technologiques — Analyse d'études de cas réels
* **Enseignants & Conférenciers :**
  * Pr Mario Passalacqua (PhD — Responsable du bloc technologique)
  * Pr Marc-André Bédard (PhD — Coordination générale)
  * Pr Mario Fiset (Conférencier invité — Facteurs humains et ergonomie aéronautique)
* **Cadre d'analyse de cas :** Application rigoureuse des 4 étapes du 22 septembre (Comprendre ➔ Concevoir ➔ Évaluer ➔ Déployer).

---

## 💻 1. Règle d'Attribution Machine : Laptop vs Everfree

> [!IMPORTANT]
> **Rôle exclusif de l'agent de session sur le Laptop (Machine de classe) :**
> - Seul l'agent de la session de cours sur le laptop de classe est mandaté pour créer, initialiser et mettre à jour le diaporama interactif officiel (`diaporama_cours_04.html`), gérer les transitions en direct et recueillir le brain dump post-cours.
> - Les agents opérant sur le poste fixe de la maison (`Everfree`) ont l'**interdiction formelle** de tenter de créer un diaporama, de générer des doublons ou d'écraser les fichiers créés en classe.

---

## 🎯 2. Recette Technique de Création du Diaporama Interactif

Dès que le PDF officiel de la séance est déposé dans le sous-dossier `Diapos` (ex. `PSY7010_29_septembre.pdf`) :

1. **Extraction Textuelle Intégrale :**
   - Extraire chaque diapositive sans paraphrase ni résumé réducteur.
   - Respecter fidèlement la terminologie des professeurs et la pagination imprimée réelle (même si discontinue).
2. **Génération du Diaporama HTML :**
   - Créer `diaporama_cours_04.html` dans le répertoire Google Drive de la séance ET dans le répertoire brain de l'agent actif avec `ArtifactMetadata: { UserFacing: true, Summary: "Visionneuse interactive Séance 4", RequestFeedback: false }`.
   - Caractéristiques du fichier HTML :
     * Flèches clavier Gauche/Droite pour naviguer.
     * Menu déroulant (`<select>`) listant toutes les diapositives avec leur titre.
     * Mode Verbatim complet activable par bouton.
     * Design épuré, responsive, contrasté.
3. **Absence de capteur UI & Filet de sécurité dans le chat :**
   - L'agent n'a aucun moyen de savoir si le panneau d'artefacts droit est déployé ou masqué sur l'écran de Michel.
   - **Règle absolue :** À chaque `D[chiffre]`, réinjecter immédiatement dans le corps de réponse du chat :
     * Numéro et titre exact de la diapositive.
     * Sous-titre et puces mot à mot.
     * Heure réelle (EDT) et offsets Rec 1 (`S24`) / Rec 2 (`SD24D`).

---

## ⏱️ 3. Synchronisation ENCORA & Audio Multi-Appareils

* **Heure universelle :** EDT (Montréal).
* **Noter immédiatement $T_0$ de chaque appareil :**
  * Principal : `PSY7010 - 29 septembre [S24].m4a`
  * Backup : `PSY7010 - 29 septembre [S24D].m4a` (téléphone désactivé sans SIM)
* **Formule universelle d'offset :**
  $$\text{Offset Audio (s)} = \text{Heure réelle (EDT)} - T_0$$
* **Signaux en direct :**
  * `D[chiffre]` = Transition de diapositive.
  * Texte sans préfixe = Réflexion, note ou question rattachée à la diapositive courante.

---

## 🎙️ 4. Questions Préparées pour les Conférenciers Invités

* Des conférenciers invités (dont Pr Mario Fiset) interviennent lors de cette séance.
* Préparer et avoir sous la main des questions structurées, ciblées sur les facteurs humains et l'ergonomie cognitive en milieu à haute criticité (aéronautique, transport, industrie).
* En cas de prise de parole : **Micro-Pitch de 15 secondes max** (Constat terrain 5s ➔ Concept précis 5s ➔ Question ouverte 5s ➔ **Silence complet**).

---

## 👥 5. Suivi Mandat APP — Groupe 3 (5/5)

* **Objectif séance 4 :** Point de synchronisation rapide avec Louis et les 3 collègues.
* Valider l'orientation ESG (certification formelle vs démarche interne d'entreprise).
* Partager les premières pistes de milieux d'accueil identifiés.

---

## 🚲 6. Routine Post-Cours & Décompression TDAH

* Après 12h30, rester dans le local calme (SU-1550), porte fermée.
* Réaliser le *brain dump* vocal/écrit dans la session de chat.
* L'agent enregistre le document officiel dans Google Drive sous `brain_dump_post_cours_2026-09-29.md`.
* **Rappel intangible pour l'agent :** NE JAMAIS DIRE DE BOIRE MOINS DE CAFÉ.
