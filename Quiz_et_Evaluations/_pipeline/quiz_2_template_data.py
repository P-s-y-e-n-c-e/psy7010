# -*- coding: utf-8 -*-
"""
Générateur de modèle vierge et documentation pour le Quiz 2 (13 octobre)
"""

QUIZ_META = {
    "quiz_num": 2,
    "quiz_date": "13 octobre",
    "course_code": "PSY7010",
    "theme_title": "LA SPÉCIALITÉ : Psychologie du commerce et consommation — Économie comportementale & recherche utilisateur (UXr)",
    "professors": "Prs G. Beaulac & M. Passalacqua",
    "official_weight": "5 % (sur Moodle, 15 premières minutes)"
}

# Documents officiels du Quiz 2 (seront remplis dès que le prof déposera les PDF sur Moodle)
DOCUMENTS = [
    {
        "id": "doc_uxr_1",
        "title": "🔴 Lecture Obligatoire 1",
        "is_mandatory": True,
        "badge_label": "🔴 Lecture obligatoire",
        "english_html": "<p class='doc-para'>Texte en anglais extrait du PDF de cours...</p>",
        "french_html": "<p class='doc-para'>Traduction française académique...</p>"
    },
    {
        "id": "doc_uxr_2",
        "title": "🟢 Support UXr",
        "is_mandatory": False,
        "badge_label": "🟢 Lecture de soutien",
        "english_html": "<p class='doc-para'>Texte complémentaire...</p>",
        "french_html": "<p class='doc-para'>Traduction française...</p>"
    }
]

# Modèle de structure pour les questions du Quiz 2
QUESTIONS_SAMPLE = [
    {
        "id": 1,
        "category": "economie_comportementale",
        "doc_id": "doc_uxr_1",
        "page": "Page X",
        "doc_quote": "Citation textuelle anglaise mot à mot...",
        "doc_quote_fr": "Citation textuelle française mot à mot...",
        "context": "Mise en situation clinique ou expérimentale...",
        "question": "Énoncé précis et sans ambiguïté...",
        "choices": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "correctIndex": 0,
        "feedbacks": [
            "Pourquoi l'option A est la seule vraie selon la théorie...",
            "Pourquoi l'option B est un piège classique...",
            "Pourquoi l'option C est inexacte...",
            "Pourquoi l'option D confond deux concepts..."
        ],
        "examTip": "Astuce réflexe pour le quiz Moodle du professeur."
    }
]
