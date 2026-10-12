# PSY7010 — Séance 4 : Milieux technologiques — Analyse d'études de cas réels (Atelier)

* **Date :** Mardi 29 septembre 2026 (09h30 – 12h30 EDT)
* **Lieu :** Pavillon Adrien-Pinard, Local SU-1550
* **Format pédagogique :** **Atelier participatif & table ronde d'analyse de cas** (Discussion ouverte sans diaporama traditionnel)
* **Enseignants & Invité :**
  * Pr Mario Passalacqua (PhD — Responsable du bloc technologique)
  * Pr Marc-André Bédard (PhD — Coordination générale)
  * Pr Mario Fiset (Conférencier invité — Ergonomie aéronautique & facteurs humains)
* **Support visuel :** Aucun document PowerPoint / PDF projeté ou déposé sur Moodle (format axé sur l'étude de cas pratique et la discussion).
* **Fichiers audio sources :**
  * Principal : `PSY7010 - 29 septembre [S24].m4a`
  * Backup : `PSY7010 - 29 septembre [S24D].m4a`

---

## ⏱️ Réconciliation Temporelle & Métadonnées Audio (Atomes MVHD)

L'inspection bas niveau des conteneurs MP4 (`mvhd`) révèle l'horodatage matériel exact de l'arrêt des enregistrements sur les téléphones et permet d'en déduire à la seconde près l'heure de lancement $T_0$ :

| Paramètre | Backup Rec 2 (`S24D`) | Principal Rec 1 (`S24`) | Écart / Remarques |
| :--- | :---: | :---: | :--- |
| **Fichier** | `PSY7010 - 29 septembre [S24D].m4a` | `PSY7010 - 29 septembre [S24].m4a` | 2 perspectives audio complémentaires |
| **Taille brute** | 80 999 798 octets (~81 Mo) | 75 817 784 octets (~76 Mo) | Audio haute fidélité |
| **Durée totale** | **02:42:22** (9 742,50 s) | **02:31:59** (9 119,22 s) | $S24D$ a ~10 min 23 s de plus |
| **Arrêt / Sauvegarde (EDT)** | **13:03:53** | **13:04:26** | **Arrêt synchrone** (à 33 s d'écart) |
| **Lancement $T_0$ calculé (EDT)** | **10:21:31** | **10:32:27** | $\Delta T_0 = \mathbf{10\text{ min }56\text{ s}}$ (656 s) |

### 🔍 Chronologie reconstituée :
1. **10:21:31 EDT :** Déclenchement de l'enregistreur de secours `S24D` (arrivée au pavillon / approche du local).
2. **10:32:27 EDT :** Déclenchement de l'enregistreur principal `S24` (installation à la table de travail dans le SU-1550).
3. **10:32 – 13:03 :** Double enregistrement continu en parallèle couvrant l'ensemble des échanges, études de cas et interventions de l'atelier (~2h31 en synchronisation parfaite).
4. **13:03:53 & 13:04:26 :** Clôture des enregistrements à la sortie du cours.

---

## 🧭 Stratégie de Traitement Audio Post-Cours (Everfree / Whisper / LLM)

Puisqu'il n'y a pas eu de support de diapositives :
1. **Pas de diaporama artificiel à concevoir :** Le mandat laptop s'adapte à la réalité du terrain ; aucune tentative de créer un faux fichier `diaporama_cours_04.html`.
2. **Triangulation audio axée sur les échanges :**
   * L'alignement temporel des deux pistes permettra d'éliminer les zones de bruit de manipulation.
   * La transcription (WhisperX ou modèle multimodal étendu sur Everfree) permettra de segmenter la parole par intervenant :
     * `SPEAKER_PASSALACQUA` (Mario Passalacqua)
     * `SPEAKER_BEDARD` (Marc-André Bédard)
     * `SPEAKER_FISET` (Mario Fiset — études de cas aéronautiques et retours d'expérience)
     * `SPEAKER_MICHEL` (Interventions et questions de Michel)
     * `SPEAKER_STUDENTS` (Interventions des collègues)
3. **Objectif pédagogique :** Synthétiser les études de cas réels abordés pour alimenter la méthodologie de l'APP Groupe 3 sans surcharger cognitivement la semaine.
