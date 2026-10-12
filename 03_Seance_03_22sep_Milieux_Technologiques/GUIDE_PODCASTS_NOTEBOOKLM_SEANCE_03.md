# 🎙️ PSY7010 — Séance 3 : Boîte à Outils Podcasts NotebookLM pour le Trajet

* **Destinataire :** Michel Mercier
* **Date :** Mardi 22 septembre 2026 (Matin — Trajet pré-cours)
* **Séance visée :** Séance 3 — *Milieux technologiques : La Spécialité (Psychologie de l'ingénierie et facteurs humains)*
* **Enseignant :** Pr Mario Passalacqua (PhD) — Pavillon Adrien-Pinard, SU-1550 (09h30)
* **Corpus source :** 92 Diapositives officielles (`PSY7010_22_septembre.pdf`), Chapitre Cañas (2011), Textes HSE & Bainbridge (1983).

---

## 🧭 Vue d'ensemble des 4 Scénarios de Podcast

| Scénario | Format / Durée | Angle Pédagogique | Trajet Idéal | Sources Recommandées dans NotebookLM |
| :--- | :---: | :--- | :--- | :--- |
| **1. Le Grand Panoramique** | ~18–22 min | Cartographie complète des 92 diapos (Comprendre $\rightarrow$ Mesurer $\rightarrow$ Concevoir $\rightarrow$ Évaluer) | Trajet métro / bus complet ou vélo calme | `diaporama_cours_03.md` + `A_Qu_est_ce_que_les_facteurs_humains.md` |
| **2. Le Sprint Facteurs Humains** | ~12–15 min | Maîtrise des concepts d'examen (Endsley, Bainbridge, Triangulation de mesure) | Trajet dynamique, focus haute intensité | `diaporama_cours_03.md` + `D_Conscience_de_la_situation.md` + `E_Paradoxes_de_l_automatisation.md` |
| **3. L'Immersion Terrain (Agnico Eagle)** | ~10–12 min | Cas vécus du prof : téléopération minière et inspection IA sous l'angle ergonomique | Immersion narrative & concrète | `diaporama_cours_03.md` (Sections 1, 2, 3) |
| **4. Le Briefing Tactique & Micro-Pitch** | ~6–8 min | Posture mentale, gestion de la cohue, structure du pitch oral de 15s | Derniers kilomètres à pied ou 15 min pré-cours | `INSTRUCTIONS_ET_REGLES_SEANCE_03.md` + `diaporama_cours_03.md` |

---

## 🛠️ Prompts de Guidage NotebookLM (Prêts à copier-coller)

### Scénario 1 : Le Grand Panoramique (Vue d'ensemble des 92 Diapos)
> **Objectif :** Poser la structure mentale du cours pour ne jamais perdre le fil pendant les 3 heures.

```text
Générez un épisode de podcast conversationnel vivant, rythmé et captivant pour un étudiant à la maîtrise en sciences psychologiques appliquées qui effectue son trajet matinal vers l'université.

Thème de l'épisode : "De la mine à l'IA : Voyage au cœur des systèmes sociotechniques avec le Pr Mario Passalacqua".

Structure obligatoire du dialogue entre les deux co-animateurs :
1. Introduction & Présentation du professeur : Présenter Mario Passalacqua (profil rare à l'UQAM : bac en psycho, maîtrise UX, doctorat en génie industriel). Expliquer comment ses projets de recherche réels (mines Agnico Eagle, CHSLD Amical, chauffeurs-livreurs, inspection industrielle) incarnent le pont entre la psychologie et l'ingénierie.
2. Le Grand Principe Fondateur : Insister avec force sur la formule clé : « L'erreur humaine décrit le résultat, pas la cause ! ». L'erreur est un symptôme systémique. Décomposer le système sociotechnique (Technologie/Interface, Tâche/Contexte, Organisation/Interactions).
3. Les 4 Temps de la Démarche Ergonomique :
   - COMPRENDRE : L'analyse du travail réel vs prescrit, la cognition en action (attention, modèles mentaux, conscience de la situation, charge mentale, vigilance, fatigue).
   - MESURER : La règle d'or de la triangulation (physiologique, perceptuel/subjectif, observationnel). Pourquoi un biomarqueur isolé ne suffit jamais.
   - CONCEVOIR : L'allocation des fonctions humain-machine et la mise en garde de Lisanne Bainbridge (les ironies de l'automatisation).
   - ÉVALUER & COMMUNIQUER : Pourquoi une solution parfaite sur papier échoue si elle n'est pas adaptée à la réalité du terrain et aux parties prenantes.
4. Conclusion tonique : Rappeler à l'auditeur qu'il arrive en classe avec une vision systémique limpide, prêt à faire le lien entre chaque diapositive et les défis du monde réel.

Ton : Naturel, collégial, enthousiaste, sans jargon inutile mais rigoureux sur les concepts théoriques.
```

---

### Scénario 2 : Le Sprint Facteurs Humains (Concepts Clés & Rigueur d'Examen)
> **Objectif :** Consolider le vocabulaire technique précis et les mécanismes cognitifs pour les interventions et les synthèses.

```text
Générez un épisode de podcast dense, stimulant et pédagogique focalisé sur les 3 grands piliers théoriques de la psychologie de l'ingénierie pour la séance d'aujourd'hui.

Thème : "Le Triptyque Ergonomique : Conscience de la situation, Ironies de l'automatisation et Triangulation méthodologique".

Points incontournables à débattre et vulgariser entre les deux hôtes :
1. La Conscience de la Situation (Mica Endsley) :
   - Distinguer très clairement les 3 niveaux : Niveau 1 (Percevoir les éléments), Niveau 2 (Comprendre la signification opérationnelle), Niveau 3 (Projeter l'état futur).
   - Donner l'exemple d'un opérateur de salle de contrôle ou d'un conducteur : voir un voyant rouge (Niv 1) vs savoir ce qu'il implique pour la machine (Niv 2) vs anticiper une rupture dans 2 minutes (Niv 3).
2. Les Paradoxes et Ironies de l'Automatisation (Lisanne Bainbridge, 1983) :
   - Expliquer le paradoxe suprême : les ingénieurs automatisent ce qui est facile et prévisible, laissant à l'opérateur humain les situations imprévues, hautement complexes et dégradées... précisément les moments où l'humain a perdu sa pratique et sa vigilance !
   - Faire le lien direct avec l'intelligence artificielle générative et l'aide au diagnostic industriel.
3. La Triangulation des Mesures :
   - Comparer les trois familles : Physiologiques (ECG, eye-tracking), Perceptuelles (NASA-TLX, SUS), Comportementales (logs, erreurs, temps).
   - Expliquer pourquoi l'ergonome sérieux ne se fie jamais à un seul indicateur ("Plus de mesures ne veut pas dire meilleure étude").

Ton : Débat intellectuel percutant, formules mémorables, analogies concrètes du quotidien et du monde industriel.
```

---

### Scénario 3 : L'Immersion Terrain (La Téléopération Minière & l'IA)
> **Objectif :** Développer l'empathie ergonomique et se projeter dans les recherches de terrain de Mario Passalacqua.

```text
Générez une discussion immersive et vivante de style reportage / analyse de cas centrée sur le passage du travail souterrain à la téléopération en surface.

Thème : "À 1000 mètres de la roche : Quand le mineur devient opérateur d'écrans".

Fil conducteur pour les deux présentateurs :
1. La rupture sensorielle : Décrire ce que vit un mineur qui passe de la machine physique dans la galerie (ressentir les vibrations du roc dans ses bottes, entendre le moteur peiner, sentir la poussière) à une cabine climatisée avec 6 écrans et des joysticks.
2. Les défis ergonomiques invisibles :
   - La perte du feedback haptique et kinesthésique.
   - La surcharge attentionnelle visuelle (partager son attention entre plusieurs caméras à angle mort).
   - L'effet "tunnel" et le délai de transmission (latence réseau).
   - La vigilance : lutter contre l'hypovigilance quand tout va bien, et gérer la panique instantanée quand une alarme retentit.
3. Le sentiment d'autonomie et le sens du travail : Comment la technologie reconfigure la fierté de métier, le contrôle perçu et la relation avec les collègues sous terre.
4. Transition vers l'inspection par IA : Comment ces mêmes principes s'appliquent à l'opérateur d'usine assisté par une IA de vision artificielle.

Ton : Narratif, incarné, profondément humain, mettant en valeur l'importance de comprendre le "travail réel" plutôt que le "travail prescrit".
```

---

### Scénario 4 : Le Briefing Tactique & Coaching Relationnel (Pré-Cours)
> **Objectif :** Apaisement du système nerveux, posture communicationnelle et préparation aux interactions avec les professeurs.

```text
Générez un court briefing d'avant-cours motivant, bienveillant et structurant pour un étudiant à la maîtrise en sciences psychologiques appliquées qui s'apprête à entrer dans la salle de classe.

Thème : "Cap sur le SU-1550 : Clarté cognitive et communication à impact".

Les hôtes doivent aborder avec bienveillance et dynamisme les points suivants :
1. Poser le décor : C'est le bloc technologique avec Mario Passalacqua. Le groupe APP est déjà complet et sécurisé (5/5). Zéro stress administratif, 100 % focus sur l'apprentissage !
2. L'Art du Micro-Pitch de 15 Secondes :
   - Étape 1 (5s) : Le constat de terrain brut, sans fioritures ni jargon.
   - Étape 2 (5s) : L'ancrage sur un concept théorique unique du cours (ex: décrément de vigilance, perte de modèle mental, charge intrinsèque).
   - Étape 3 (5s) : La question ouverte qui remet la balle dans le camp du prof... puis le silence total pour écouter !
3. Dédramatiser la cohue de 12h30 : Rappeler que si le prof est pressé ou sollicité en fin de cours, ce n'est jamais personnel. La phrase magique : « Je t'envoie un courriel de 3 lignes pour qu'on en reparle au prochain atelier ! ».
4. Clôture décompression : Respirer un grand coup, savourer la découverte des facteurs humains, et aborder la séance avec curiosité et sérénité.

Ton : Chaleureux, complice, énergisant, orienté vers la réussite et la régulation attentionnelle.
```
