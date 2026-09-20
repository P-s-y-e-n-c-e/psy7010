# 🚀 Pipeline de Génération Automatique des Quiz PSY7010

Ce répertoire contient le moteur universel permettant de générer les stations d'étude interactives pour tous les quiz du cours PSY7010, **sans jamais avoir à recoder l'interface ou les fonctionnalités en dur**.

---

## 🎯 Architecture Modulaire

```
Quiz_et_Evaluations/
├── _pipeline/
│   ├── README_PIPELINE.md         # Guide et documentation
│   ├── template_workstation.html  # Gabarit maître (CSS, JS, Moteur SRS, Simulateur, Lecteur)
│   ├── build_quiz_workstation.py  # Script de compilation automatisée
│   ├── quiz_1_data.py             # Données du Quiz 1 (22 sep - Milieux technologiques)
│   └── quiz_2_template_data.py    # Gabarit vierge pour le Quiz 2 (13 oct - Commerce & UXr)
├── Quiz_1_22sep_Milieux_Technologiques/
│   └── Quiz_entrainement_22sep_PSY7010.html
└── Quiz_2_13oct_Commerce_UXr/     # Dossier généré automatiquement pour le Quiz 2
```

---

## ⚡ Comment générer un nouveau Quiz (ex. Quiz 2 du 13 octobre) ?

Pour le prochain quiz (Économie comportementale & UXr), il suffit de 3 étapes simples :

### 1. Remplir le fichier de données `quiz_2_data.py`
Définir simplement :
- `QUIZ_TITLE` = "PSY7010 Quiz d'entraînement"
- `QUIZ_DATE` = "13 octobre"
- `DOCUMENTS` = Liste des textes obligatoires et complémentaires (id, titre, texte original EN, traduction FR).
- `QUESTIONS` = Liste des questions au format standardisé (question, doc_id, page, quote, choices, correctIndex, feedbacks, examTip).
- `PODCAST_CONFIG` (facultatif) = Titre, fichier local ou lien Drive si un podcast NotebookLM est généré.

### 2. Lancer la commande de compilation
```bash
python Quiz_et_Evaluations/_pipeline/build_quiz_workstation.py --quiz 2
```

### 3. Résultat instantané
Le script compile et produit automatiquement :
- `Quiz_et_Evaluations/Quiz_2_13oct_Commerce_UXr/Quiz_entrainement_13oct_PSY7010.html`

Ce fichier hérite immédiatement et sans effort de **toutes les améliorations de design et d'ergonomie** :
- ✅ Séparateur 50/50 en mode horizontal et ajustement naturel sans scrollbar en mode vertical.
- ✅ Mode sombre persistant avec libellés dynamiques `Mode sombre 🌓` / `Mode clair ☀️`.
- ✅ Simulateur de quiz calibré sur le format officiel Moodle du prof (5 questions, 15 minutes).
- ✅ Entraînement mémoire avec répétition espacée (SRS Leitmner).
- ✅ Démasquage automatique au clic sur les onglets de lecture.
- ✅ Balise anti-crawlers `<meta name="robots" content="noindex, nofollow, ...">` pour protéger la diffusion privée.
- ✅ Mascotte interactive Toadette intégrée en Base64 (zéro dépendance externe).
