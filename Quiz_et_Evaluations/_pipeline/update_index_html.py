# -*- coding: utf-8 -*-
"""
Script de mise à jour sécurisée de index.html
1. Remplacement de S6_MASTER_QUESTIONS par les 24 questions ZPD étalons-or.
2. Mise à jour des ancres textuelles dans les viewports Chen 2024, Congiu 2022 et UX Researcher (FR et EN).
"""

import json
import re

# 1. Charger les 24 questions
with open('Quiz_et_Evaluations/_pipeline/s6_master_24_questions.json', encoding='utf-8') as f:
    master_questions = json.load(f)

# 2. Charger index.html
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# -----------------------------------------------------------------------------
# ÉTAPE A : MISE À JOUR DE S6_MASTER_QUESTIONS
# -----------------------------------------------------------------------------
questions_json_str = json.dumps(master_questions, ensure_ascii=False, indent=2)

pattern_q = r'const S6_MASTER_QUESTIONS = \[[\s\S]*?\n    \];\n    const S6_MASTER_FLASHCARDS'
replacement_q = f'const S6_MASTER_QUESTIONS = {questions_json_str};\n    const S6_MASTER_FLASHCARDS'

if not re.search(pattern_q, html):
    # Essai motif alternatif sans indentation stricte
    pattern_q = r'const S6_MASTER_QUESTIONS = \[[\s\S]*?\];\s*const S6_MASTER_FLASHCARDS'
    replacement_q = f'const S6_MASTER_QUESTIONS = {questions_json_str};\n    const S6_MASTER_FLASHCARDS'

assert re.search(pattern_q, html), "Impossible de localiser S6_MASTER_QUESTIONS dans index.html !"
html = re.sub(pattern_q, replacement_q, html, count=1)
print("✅ S6_MASTER_QUESTIONS remplacé avec succès (24 questions).")

# -----------------------------------------------------------------------------
# ÉTAPE B : MISE À JOUR DU VIEWPORT CHEN 2024 (FR & EN)
# -----------------------------------------------------------------------------
chen_fr_html = """      <!-- VIEWPORT : CHEN (2024) - FRANÇAIS -->
      <div class="reader-viewport" id="viewport_doc_chen2024_fr" style="display: none;">
        <h2 class="doc-art-title">Chen, Y. (2024) — Économie Comportementale : Comprendre les Facteurs Psychologiques Déterminant les Décisions des Consommateurs</h2>
        <ul class="doc-list">
          <li><strong>Source officielle :</strong> <em>International Journal of Global Economics and Management</em>, 4(1), 99–104.</li>
          <li><strong>Cadre pédagogique :</strong> PSY7010 - Séance 06 : Commerce et consommation 1 (Guillaume Beaulac &amp; Mario Passalacqua)</li>
          <li><strong>Thématiques clés :</strong> Rationalité limitée, Heuristiques et biais, Émotions (peur, joie, culpabilité), Cadrage des prix, Nudges et politiques publiques.</li>
          <li><strong>Traduction de travail académique française pour la cohorte de maîtrise (UQAM).</strong></li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Introduction et Définition</h3>
        <p class="doc-para">
          L'économie comportementale est un domaine interdisciplinaire qui combine les connaissances de la psychologie et de l'économie pour comprendre comment les individus prennent des décisions. Contrairement à l'économie traditionnelle qui postule des acteurs rationnels maximisant toujours leur utilité, elle reconnaît que les choix humains sont influencés par des facteurs cognitifs, émotionnels et sociaux.
        </p>
        <p class="doc-para">
          <mark id="anchor_chen_q13" class="source-anchor-target" data-qid="13" title="Extrait officiel pour la Question 13 (Chen 2024, p. 100)">Les politiques publiques peuvent utiliser des 'nudges', comme l'inscription automatique des salariés à un plan d'épargne-retraite avec option de désengagement (opt-out), augmentant significativement la participation sans restreindre la liberté de choix (« without restricting freedom of choice »).</mark>
        </p>

        <h3 class="doc-art-h2">2. Contexte Historique</h3>
        <p class="doc-para">
          L'économie néoclassique repose sur l'hypothèse de l'agent rationnel (Homo Economicus). L'économie comportementale a émergé pour critiquer ce modèle idéalisé en démontrant des déviations systématiques causées par les biais cognitifs, les émotions et les contraintes attentionnelles.
        </p>

        <h3 class="doc-art-h2">3. Concepts Fondamentaux</h3>
        
        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">3.1 Rationalité Limitée et Recherche d'un Choix Satisfaisant</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q1" class="source-anchor-target" data-qid="1" title="Extrait officiel pour la Question 1 (Chen 2024, p. 101)">Selon Herbert Simon, les individus sont confrontés à des limites cognitives (mémoire et capacité computationnelle limitées) et à une information incomplète. Face à ces contraintes, les décideurs utilisent des modèles simplifiés et adoptent des règles pratiques menant à un choix 'satisfaisant' plutôt qu'optimal : ils choisissent une option suffisamment bonne dans les circonstances (« choosing an option that is good enough under the circumstances ») plutôt que la meilleure option possible.</mark>
        </p>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">3.2 Heuristiques et Biais Cognitifs</h4>
        <p class="doc-para">
          Les heuristiques sont des raccourcis mentaux qui simplifient la décision mais mènent à des biais systématiques. L'heuristique de disponibilité évalue la fréquence par la facilité de rappel ; l'ancrage calibre le jugement sur la première valeur rencontrée.
        </p>
        <p class="doc-para">
          <mark id="anchor_chen_q2" class="source-anchor-target" data-qid="2" title="Extrait officiel pour la Question 2 (Chen 2024, p. 101-102)">Le biais de confirmation amène les individus à rechercher et privilégier les informations qui confirment leurs croyances préalables tout en ignorant ou sous-évaluant les preuves qui les contredisent (« seek out and favor information that confirms their preexisting beliefs »).</mark>
        </p>

        <h3 class="doc-art-h2">4. Facteurs Psychologiques</h3>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">4.1 Influences Émotionnelles</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q7" class="source-anchor-target" data-qid="7" title="Extrait officiel pour la Question 7 (Chen 2024, p. 102)">La peur de perdre peut conduire à des choix excessivement conservateurs. L'aversion aux pertes implique que les individus ressentent les pertes de façon plus intense que les gains équivalents (« experience losses more intensely than equivalent gains »), évitant des risques même lorsque les bénéfices potentiels dépassent les pertes envisageables.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_chen_q14" class="source-anchor-target" data-qid="14" title="Extrait officiel pour la Question 14 (Chen 2024, p. 102)">À l'inverse, la joie et l'excitation peuvent entraîner des décisions plus impulsives et des achats imprévus (« can lead to more impulsive decisions »). La culpabilité peut pousser un individu à faire des dons ou à adopter des conduites socialement responsables pour soulager un sentiment d'inconfort moral (« alleviate feelings of moral discomfort »).</mark>
        </p>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">4.2 Influences Sociales</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q9" class="source-anchor-target" data-qid="9" title="Extrait officiel pour la Question 9 (Chen 2024, p. 102)">La preuve sociale (social proof) est une influence puissante où les individus se fient aux actions et avis des autres pour guider leurs propres décisions : les produits bénéficiant de notes élevées ou d'avis positifs sont perçus comme plus fiables et désirables.</mark>
        </p>

        <h3 class="doc-art-h2">5. Applications Pratiques</h3>
        <p class="doc-para">
          <mark id="anchor_chen_q8" class="source-anchor-target" data-qid="8" title="Extrait officiel pour la Question 8 (Chen 2024, p. 103)">Dans les stratégies marketing, le cadrage du prix (price framing) utilise notamment le modèle du rabais où le prix régulier est barré à côté du prix réduit (« regular price is crossed out and a lower price is displayed, making the discount seem more significant »). Les mentions de rareté et d'offres limitées dans le temps exploitent la peur de manquer l'occasion pour accélérer l'achat.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_chen_q15" class="source-anchor-target" data-qid="15" title="Extrait officiel pour la Question 15 (Chen 2024, p. 103)">En pratique d'affaires et ergonomie, la conception de l'expérience utilisateur (UX) est améliorée en réduisant la charge cognitive et en rendant les interfaces plus intuitives (« reducing cognitive load and making interfaces more intuitive »), facilitant la comparaison et l'engagement.</mark>
        </p>
      </div>"""

chen_en_html = """      <!-- VIEWPORT : CHEN (2024) - ENGLISH ORIGINAL -->
      <div class="reader-viewport" id="viewport_doc_chen2024_en" style="display: none;">
        <h2 class="doc-art-title">Chen, Y. (2024) — Behavioral Economics: Understanding the Psychological Factors Driving Consumer Decisions</h2>
        <ul class="doc-list">
          <li><strong>Original Source:</strong> <em>International Journal of Global Economics and Management</em>, 4(1), 99–104.</li>
          <li><strong>Academic Scope:</strong> PSY7010 - Session 06: Commerce &amp; Consumer Psychology 1 (Profs. Guillaume Beaulac &amp; Mario Passalacqua)</li>
          <li><strong>Key Concepts:</strong> Bounded rationality, Heuristics &amp; Biases, Emotions &amp; Social proof, Price framing, Policy nudges.</li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Introduction</h3>
        <p class="doc-para">
          <mark id="anchor_chen_q13_en" class="source-anchor-target" data-qid="13" title="Official excerpt for Question 13 (Chen 2024, p. 100)">Policies that use 'nudges,' such as automatically enrolling employees in retirement savings plans with an opt-out option, can significantly increase participation rates without restricting freedom of choice.</mark>
        </p>

        <h3 class="doc-art-h2">3. Core Concepts</h3>
        
        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">3.1 Bounded Rationality</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q1_en" class="source-anchor-target" data-qid="1" title="Official excerpt for Question 1 (Chen 2024, p. 101)">Bounded rationality, a concept introduced by Herbert Simon, challenges the traditional economic assumption of perfect rationality. The constraints include limited cognitive resources and incomplete information, leading to decisions that are 'satisficing' rather than optimizing—choosing an option that is good enough under the circumstances rather than the best possible choice.</mark>
        </p>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">3.2 Heuristics and Biases</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q2_en" class="source-anchor-target" data-qid="2" title="Official excerpt for Question 2 (Chen 2024, p. 101-102)">Confirmation bias is another significant cognitive bias, where people tend to seek out and favor information that confirms their preexisting beliefs while ignoring or undervaluing evidence that contradicts them.</mark>
        </p>

        <h3 class="doc-art-h2">4. Psychological Factors</h3>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">4.1 Emotional Influences</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q7_en" class="source-anchor-target" data-qid="7" title="Official excerpt for Question 7 (Chen 2024, p. 102)">This phenomenon, known as loss aversion, suggests that people experience losses more intensely than equivalent gains, causing them to avoid risks that could lead to losses.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_chen_q14_en" class="source-anchor-target" data-qid="14" title="Official excerpt for Question 14 (Chen 2024, p. 102)">Conversely, joy and excitement can lead to more impulsive decisions... guilt might drive a person to make charitable donations or engage in socially responsible behaviors to alleviate feelings of moral discomfort.</mark>
        </p>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">4.2 Social Influences</h4>
        <p class="doc-para">
          <mark id="anchor_chen_q9_en" class="source-anchor-target" data-qid="9" title="Official excerpt for Question 9 (Chen 2024, p. 102)">Social proof is a powerful social influence where individuals look to others' actions to guide their own decisions, observing that products with high user ratings or positive reviews are perceived as more trustworthy.</mark>
        </p>

        <h3 class="doc-art-h2">5. Practical Applications</h3>
        <p class="doc-para">
          <mark id="anchor_chen_q8_en" class="source-anchor-target" data-qid="8" title="Official excerpt for Question 8 (Chen 2024, p. 103)">Price framing involves presenting prices in a way that makes them appear more attractive. An example is the 'discount' model, where a product's regular price is crossed out and a lower price is displayed, making the discount seem more significant.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_chen_q15_en" class="source-anchor-target" data-qid="15" title="Official excerpt for Question 15 (Chen 2024, p. 103)">User experience design can be enhanced by applying principles like reducing cognitive load and making interfaces more intuitive, which helps in making tasks easier and more engaging for users.</mark>
        </p>
      </div>"""

pattern_chen = r'<!-- VIEWPORT : CHEN \(2024\) - FRANÇAIS -->[\s\S]*?<!-- VIEWPORT : CHEN \(2024\) - ENGLISH ORIGINAL -->[\s\S]*?</div>\s*</div>'
# Remplacement sécurisé des viewports Chen
pattern_chen_both = r'<!-- VIEWPORT : CHEN \(2024\) - FRANÇAIS -->[\s\S]*?<!-- VIEWPORT : CONGIU & MOSCATI \(2022\) - FRANÇAIS -->'
replacement_chen_both = f"{chen_fr_html}\n    \n\n{chen_en_html}\n    \n\n      <!-- VIEWPORT : CONGIU & MOSCATI (2022) - FRANÇAIS -->"

assert re.search(pattern_chen_both, html), "Impossible de localiser le bloc Chen dans index.html !"
html = re.sub(pattern_chen_both, replacement_chen_both, html, count=1)
print("✅ Viewports Chen 2024 (FR & EN) actualisés avec succès.")

# -----------------------------------------------------------------------------
# ÉTAPE C : MISE À JOUR DU VIEWPORT CONGIU & MOSCATI (2022) (FR & EN)
# -----------------------------------------------------------------------------
congiu_fr_html = """      <!-- VIEWPORT : CONGIU & MOSCATI (2022) - FRANÇAIS -->
      <div class="reader-viewport" id="viewport_doc_congiu2022_fr" style="display: none;">
        <h2 class="doc-art-title">Congiu, R., &amp; Moscati, I. (2022) — Revue Critique des Nudges : Définitions, Justifications et Efficacité</h2>
        <ul class="doc-list">
          <li><strong>Source officielle :</strong> <em>European Economic Review</em> (Journal of Economic Surveys, 36(1), 188–213).</li>
          <li><strong>Cadre pédagogique :</strong> PSY7010 - Séance 06 : Commerce et consommation 1 (Guillaume Beaulac &amp; Mario Passalacqua)</li>
          <li><strong>Thématiques clés :</strong> Définition officielle de Thaler &amp; Sunstein (2008), Effet leurre, Typologie de Hansen &amp; Jespersen, Paternalisme libertarien, Nudges vs Boosts, Don d'organes et choix par défaut.</li>
          <li><strong>Traduction de travail académique française pour la cohorte de maîtrise (UQAM).</strong></li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Définition et Composantes Académiques du Nudge</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q16" class="source-anchor-target" data-qid="16" title="Extrait officiel pour la Question 16 (Congiu &amp; Moscati 2022, p. 191)">Dans leur définition séminale, Thaler et Sunstein (2008, p. 6) posent quatre conditions indispensables : (1) aucune option n'est interdite, (2) aucun incitatif économique n'est modifié de façon significative, (3) l'intervention doit être facile et peu coûteuse à éviter (« cheap and easy to avoid »), et (4) son mécanisme influence les agents à rationalité limitée tout en étant ignoré par les agents néoclassiquement rationnels.</mark>
        </p>

        <h3 class="doc-art-h2">2. L'Effet Leurre et les Incitatifs Économiques</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q4" class="source-anchor-target" data-qid="4" title="Extrait officiel pour la Question 4 (Congiu &amp; Moscati 2022, p. 191)">L'effet leurre (decoy effect) modifie l'architecture du choix en introduisant une option asymétriquement dominée. Selon Congiu et Moscati (§2.1, p. 191), cette intervention constitue un nudge au sens original : les options initiales restent disponibles aux mêmes prix, aucune interdiction n'est posée, et un agent parfaitement rationnel ignorerait simplement l'option dominée (« would be ignored by an Econ »).</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q3" class="source-anchor-target" data-qid="3" title="Extrait officiel pour la Question 3 (Congiu &amp; Moscati 2022, p. 193-194)">La taxe de cinq cents sur les sacs jetables illustre une divergence de classification : pour la définition originale de 2008, elle est exclue du champ des nudges car elle modifie les incitatifs économiques et ne serait pas ignorée par un Econ (« would not be ignored by an Econ », §2.4, p. 193). En revanche, selon la définition de Hansen (§3.1, p. 194), le fait que l'efficacité repose sur l'aversion aux pertes transforme cette taxe en nudge (« turns the five-cent tax into a nudge »).</mark>
        </p>

        <h3 class="doc-art-h2">3. Typologie de Hansen &amp; Jespersen : Mode Cognitif et Transparence</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q6" class="source-anchor-target" data-qid="6" title="Extrait officiel pour la Question 6 (Congiu &amp; Moscati 2022, p. 192-193)">Hansen et Jespersen (2013) classifient les nudges selon deux axes : le mode cognitif sollicité (Type 1 automatique vs Type 2 réflexif) et le degré de transparence de l'influence pour le décideur (transparent vs opaque).</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q10" class="source-anchor-target" data-qid="10" title="Extrait officiel pour la Question 10 (Congiu &amp; Moscati 2022, p. 192-193)">Cette matrice à 4 quadrants permet de distinguer : un nudge transparent de type 2 (ex. une lettre invitant à comparer explicitement ses dépenses à celles d'un ménage moyen) et un nudge opaque de type 1 (ex. des lignes peintes sur la chaussée dont l'espacement décroissant déclenche un ralentissement automatique sans délibération).</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q19" class="source-anchor-target" data-qid="19" title="Extrait officiel pour la Question 19 (Congiu &amp; Moscati 2022, p. 192)">Dans le cas d'une cible visuelle gravée au fond d'un urinoir, le canal d'influence sollicite une réponse automatique à un repère perceptif (« an automatic response »), sans contraindre l'usager ni modifier ses incitatifs économiques, ce qui caractérise un nudge de type 1.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q22" class="source-anchor-target" data-qid="22" title="Extrait officiel pour la Question 22 (Congiu &amp; Moscati 2022, p. 192)">Concernant les options par défaut, les auteurs expliquent qu'un décideur a tendance à conserver le défaut (« decision-maker tends to adopt it ») lorsque ses préférences ne sont pas clairement définies ou qu'il ne dispose pas des capacités cognitives ou de calcul requises pour évaluer les options complexes.</mark>
        </p>

        <h3 class="doc-art-h2">4. Normes Sociales et Rapprochement Fiscal</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q12" class="source-anchor-target" data-qid="12" title="Extrait officiel pour la Question 12 (Congiu &amp; Moscati 2022, p. 196)">Dans les interventions d'efficacité énergétique (O-Power), la comparaison avec les voisins (norme descriptive) réduit la consommation des surconsommateurs. Pour neutraliser l'effet boomerang chez les ménages économes, l'adjonction d'un symbole positif (smiley) introduit une norme injonctive qui valide le comportement sobre.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q20" class="source-anchor-target" data-qid="20" title="Extrait officiel pour la Question 20 (Congiu &amp; Moscati 2022, p. 196)">De même, dans les rappels fiscaux britanniques, informer les contribuables retardataires que leurs pairs paient leurs impôts à temps (« their peers pay their taxes on time ») rend visible la norme descriptive pour inciter à la conformité sans introduire de pénalité nouvelle.</mark>
        </p>

        <h3 class="doc-art-h2">5. Justification Philosophique et Objections Éthiques</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q5" class="source-anchor-target" data-qid="5" title="Extrait officiel pour la Question 5 (Congiu &amp; Moscati 2022, p. 195)">Sunstein défend une définition du nudge au sens large (« broad sense ») incluant des démarches éducatives et réflexives destinées à aider les personnes à faire de meilleurs choix selon leur propre jugement.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q23" class="source-anchor-target" data-qid="23" title="Extrait officiel pour la Question 23 (Congiu &amp; Moscati 2022, p. 200)">Cependant, les critiques analysées au §6.3 soulignent que des interventions qui exploitent les biais de façon opaque et contournent la délibération peuvent compromettre l'autonomie décisionnelle (« subversion of the decision-maker's autonomy »), même si toutes les options matérielles restent juridiquement accessibles.</mark>
        </p>

        <h3 class="doc-art-h2">6. Nudges vs Boosts : Paradigmes d'Autonomie</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q11" class="source-anchor-target" data-qid="11" title="Extrait officiel pour la Question 11 (Congiu &amp; Moscati 2022, p. 202-203)">La distinction de Ralph Hertwig et Till Grüne-Yanoff (2017) oppose deux visions : les nudges guident le comportement immédiat par l'agencement du contexte sans accroître les compétences de l'agent, tandis que les 'boosts' développent et outillent les compétences cognitives et heuristiques des personnes pour favoriser des décisions autonomes durables.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q17" class="source-anchor-target" data-qid="17" title="Extrait officiel pour la Question 17 (Congiu &amp; Moscati 2022, p. 203)">Cette différence explique que les effets d'un nudge s'estompent fréquemment dès son retrait, alors que les boosts visent des compétences décisionnelles pérennes et transférables.</mark>
        </p>

        <h3 class="doc-art-h2">7. Efficacité Empirique et Acceptabilité Publique : Le Don d'Organes</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q21" class="source-anchor-target" data-qid="21" title="Extrait officiel pour la Question 21 (Congiu &amp; Moscati 2022, p. 204)">Dans les programmes de don d'organes, le passage au consentement présumé par défaut génère des taux d'adhésion spectaculairement supérieurs (« dramatically higher donation rates »). Les auteurs soulignent néanmoins qu'il faut séparer rigoureusement cette efficacité comportementale de l'acceptabilité publique réelle et des questions d'autonomie éthique (§7.3, p. 202 et §9, p. 204).</mark>
        </p>
      </div>"""

congiu_en_html = """      <!-- VIEWPORT : CONGIU & MOSCATI (2022) - ENGLISH ORIGINAL -->
      <div class="reader-viewport" id="viewport_doc_congiu2022_en" style="display: none;">
        <h2 class="doc-art-title">Congiu, R., &amp; Moscati, I. (2022) — A review of nudges: Definitions, justifications, effectiveness</h2>
        <ul class="doc-list">
          <li><strong>Source:</strong> <em>European Economic Review</em> (Journal of Economic Surveys, 36(1), 188–213).</li>
          <li><strong>Academic Focus:</strong> Definitions, Decoy effect, Hansen &amp; Jespersen typologies, Nudges vs Boosts, Defaults.</li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Academic Definitions and Original Components</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q16_en" class="source-anchor-target" data-qid="16" title="Official excerpt for Question 16 (Congiu 2022, p. 191)">Thaler and Sunstein's original definition (2008, p. 6) entails four conditions: no options forbidden, no significant change in economic incentives, cheap and easy to avoid, and altering choices of boundedly rational agents while being ignored by neoclassical Econs.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q4_en" class="source-anchor-target" data-qid="4" title="Official excerpt for Question 4 (Congiu 2022, p. 191)">The decoy effect introduces an asymmetrically dominated alternative. Since existing options remain unchanged, it alters behavior without forbidding options, and would be ignored by an Econ.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q3_en" class="source-anchor-target" data-qid="3" title="Official excerpt for Question 3 (Congiu 2022, p. 193-194)">A five-cent plastic bag tax would not be ignored by an Econ (§2.4, p. 193), excluding it under the 2008 definition. Under Hansen's criterion (§3.1, p. 194), loss aversion turns the five-cent tax into a nudge.</mark>
        </p>

        <h3 class="doc-art-h2">2. Hansen &amp; Jespersen Quadrants</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q6_en" class="source-anchor-target" data-qid="6" title="Official excerpt for Question 6 (Congiu 2022, p. 192-193)">Hansen and Jespersen (2013) classify nudges along two axes: cognitive mode (System 1 automatic vs. System 2 reflective) and transparency (transparent vs. opaque influence).</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q10_en" class="source-anchor-target" data-qid="10" title="Official excerpt for Question 10 (Congiu 2022, p. 192-193)">Transparent type 2 nudges invoke conscious deliberation; opaque type 1 nudges trigger an automatic response without conscious reasoning.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q19_en" class="source-anchor-target" data-qid="19" title="Official excerpt for Question 19 (Congiu 2022, p. 192)">Visual cues like a fly etched in a urinal stimulate an automatic response without changing financial incentives or imposing constraints.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q22_en" class="source-anchor-target" data-qid="22" title="Official excerpt for Question 22 (Congiu 2022, p. 192)">When agents lack well-defined preferences or cognitive and computational skills to determine optimal plans, the decision-maker tends to adopt the default.</mark>
        </p>

        <h3 class="doc-art-h2">3. Social Norms and Peer Comparison</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q12_en" class="source-anchor-target" data-qid="12" title="Official excerpt for Question 12 (Congiu 2022, p. 196)">Coupling descriptive norms with injunctive feedback (smiley faces) prevents the boomerang effect among efficient households.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q20_en" class="source-anchor-target" data-qid="20" title="Official excerpt for Question 20 (Congiu 2022, p. 196)">Tax collection reminders informing debtors that their peers pay their taxes on time harness descriptive norms to promote compliance.</mark>
        </p>

        <h3 class="doc-art-h2">4. Philosophical Justification &amp; Autonomy</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q5_en" class="source-anchor-target" data-qid="5" title="Official excerpt for Question 5 (Congiu 2022, p. 195)">Sunstein supports a definition in the broad sense, incorporating educative and reflective nudges that inform decision-makers.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q23_en" class="source-anchor-target" data-qid="23" title="Official excerpt for Question 23 (Congiu 2022, p. 200)">Ethical critics argue that opaque behavioral interventions that bypass conscious deliberation can lead to a subversion of the decision-maker's autonomy.</mark>
        </p>

        <h3 class="doc-art-h2">5. Nudges vs Boosts</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q11_en" class="source-anchor-target" data-qid="11" title="Official excerpt for Question 11 (Congiu 2022, p. 202-203)">Boosts (Hertwig &amp; Grüne-Yanoff 2017) build and empower long-term decision competencies and heuristics, whereas nudges alter the immediate architecture.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q17_en" class="source-anchor-target" data-qid="17" title="Official excerpt for Question 17 (Congiu 2022, p. 203)">Boosts aim for lasting cognitive empowerment that persists after the intervention ends, unlike nudges whose effects often decay after withdrawal.</mark>
        </p>

        <h3 class="doc-art-h2">6. Default Effects in Organ Donation</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q21_en" class="source-anchor-target" data-qid="21" title="Official excerpt for Question 21 (Congiu 2022, p. 204)">Presumed consent defaults yield dramatically higher donation rates, though behavioral compliance must be distinguished from public acceptability and autonomy.</mark>
        </p>
      </div>"""

pattern_congiu_both = r'<!-- VIEWPORT : CONGIU & MOSCATI \(2022\) - FRANÇAIS -->[\s\S]*?<!-- VIEWPORT : BVA NUDGE UNIT - FRANÇAIS -->'
replacement_congiu_both = f"{congiu_fr_html}\n    \n\n{congiu_en_html}\n    \n\n      <!-- VIEWPORT : BVA NUDGE UNIT - FRANÇAIS -->"

assert re.search(pattern_congiu_both, html), "Impossible de localiser le bloc Congiu dans index.html !"
html = re.sub(pattern_congiu_both, replacement_congiu_both, html, count=1)
print("✅ Viewports Congiu & Moscati 2022 (FR & EN) actualisés avec succès.")

# -----------------------------------------------------------------------------
# ÉTAPE D : MISE À JOUR DU VIEWPORT UX RESEARCHER (FR & EN)
# -----------------------------------------------------------------------------
ux_fr_html = """      <!-- VIEWPORT : UX RESEARCHER - FRANÇAIS -->
      <div class="reader-viewport" id="viewport_doc_ux_researcher_fr" style="display: none;">
        <h2 class="doc-art-title">Guide Méthodologique UX Researcher (Konrad) — Recherche Utilisateur &amp; Pratique Clinique</h2>
        <ul class="doc-list">
          <li><strong>Source officielle :</strong> Guide métier et transcription <em>Qu'est-ce qu'un UX Researcher</em> (Konrad / Nielsen Norman Group)</li>
          <li><strong>Cadre pédagogique :</strong> PSY7010 - Séance 06 : Ergonomie commerciale et recherche en expérience utilisateur</li>
          <li><strong>Thématiques clés :</strong> Recherche générative (découverte) vs évaluative, Qualitatif vs quantitatif, Neutralité scientifique, Empathie, Analyse et communication produit.</li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Qu'est-ce qu'un UX Researcher ?</h3>
        <p class="doc-para">
          Le chercheur en expérience utilisateur (UX Researcher) est le garant de la voix des utilisateurs au sein du cycle de conception logicielle ou matérielle. Sa mission fondamentale consiste à identifier les modèles mentaux, les besoins réels, les blocages cognitifs et les comportements effectifs des usagers afin de guider les décisions de design et d'ingénierie.
        </p>

        <h3 class="doc-art-h2">2. Recherche Générative (Découverte) vs Recherche Évaluative</h3>
        <p class="doc-para">
          <mark id="anchor_ux_q18" class="source-anchor-target" data-qid="18" title="Extrait officiel pour la Question 18 (Guide UX Konrad)">La recherche générative (ou recherche de découverte) intervient en amont de toute conception : elle explore le problème, les pratiques existantes et les motivations intrinsèques des usagers sans présupposer une solution technique. À l'opposé, la recherche évaluative intervient pendant et après la conception pour mesurer la conformité, l'utilisabilité et l'efficacité d'un prototype ou d'un produit existant face aux tâches prescrites (l. 4–6).</mark>
        </p>

        <h3 class="doc-art-h2">3. Complémentarité Méthodologique : Qualitatif vs Quantitatif</h3>
        <p class="doc-para">
          Les approches qualitatives (entretiens approfondis, observations directes, tests d'utilisabilité modérés sur 5 à 8 participants) répondent à la question du « Pourquoi ? » en révélant les raisonnements et les frustrations. Les approches quantitatives (analyses de clics, taux de complétion, métriques de temps sur tâche, sondages à large échelle) répondent à la question du « Combien ? » et mesurent l'ampleur statistique d'un phénomène.
        </p>

        <h3 class="doc-art-h2">4. Conception et Validité des Personas de Recherche</h3>
        <p class="doc-para">
          Un persona de recherche scientifiquement valide n'est ni un profil marketing fictif ni une simple fiche démographique. C'est un modèle comportemental synthétique fondé sur des régularités empiriques observées sur le terrain, documentant les objectifs, les compétences cognitives, le niveau de familiarité technologique et les stratégies de contournement des utilisateurs réels.
        </p>

        <h3 class="doc-art-h2">5. Déontologie et Posture Clinique du Modérateur</h3>
        <p class="doc-para">
          Lors d'un test d'utilisabilité, le chercheur doit adopter une neutralité clinique absolue. Il ne doit jamais orienter le participant, ni justifier les choix de conception de l'équipe.
        </p>

        <h3 class="doc-art-h2">6. Qualités Professionnelles du Chercheur UX</h3>
        <p class="doc-para">
          <mark id="anchor_ux_q24" class="source-anchor-target" data-qid="24" title="Extrait officiel pour la Question 24 (Guide UX Konrad)">Une pratique rigoureuse de la recherche UX articule quatre compétences fondamentales décrites dans le guide : 1) l'empathie auprès des utilisateurs (l. 68–69) ; 2) l'esprit d'analyse pour s'assurer d'extraire l'essentiel des données (l. 70) ; 3) l'ouverture et la neutralité scientifique sans questions orientées (l. 72–73) ; et 4) la capacité à communiquer auprès de l'équipe produit pour éclairer et améliorer la conception (l. 75–76).</mark>
        </p>
      </div>"""

ux_en_html = """      <!-- VIEWPORT : UX RESEARCHER - ENGLISH -->
      <div class="reader-viewport" id="viewport_doc_ux_researcher_en" style="display: none;">
        <h2 class="doc-art-title">UX Research Methodological Guide — Clinical Practice &amp; Evaluation</h2>
        <ul class="doc-list">
          <li><strong>Framework:</strong> UX Research Handbook (Konrad / Nielsen Norman Group)</li>
          <li><strong>Academic Focus:</strong> PSY7010 - Applied Psychological Sciences</li>
          <li><strong>Core Topics:</strong> Generative vs. Evaluative research, Qual/Quant complementarity, Scientific neutrality, Product communication.</li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Discovery vs. Evaluative Research</h3>
        <p class="doc-para">
          <mark id="anchor_ux_q18_en" class="source-anchor-target" data-qid="18" title="Official excerpt for Question 18 (UX Guide)">Generative (discovery) research investigates problem spaces and user mental models prior to design formulation, whereas evaluative research validates usability metrics and interface friction on existing prototypes (lines 4–6).</mark>
        </p>

        <h3 class="doc-art-h2">2. Qualitative vs. Quantitative Insights</h3>
        <p class="doc-para">
          Qualitative inquiry explains the underlying 'Why' behind behaviors through in-depth observation, while quantitative research quantifies the 'How many' and statistically benchmarks performance.
        </p>

        <h3 class="doc-art-h2">3. Professional Attributes of UX Researchers</h3>
        <p class="doc-para">
          <mark id="anchor_ux_q24_en" class="source-anchor-target" data-qid="24" title="Official excerpt for Question 24 (UX Guide)">Key competencies include active empathy for users (lines 68–69), analytical skills to extract key insights (line 70), scientific openness and neutrality to avoid bias (lines 72–73), and effective communication to product teams (lines 75–76).</mark>
        </p>
      </div>"""

pattern_ux_both = r'<!-- VIEWPORT : UX RESEARCHER - FRANÇAIS -->[\s\S]*?<!-- VIEWPORT : UX RESEARCHER - ENGLISH -->[\s\S]*?</div>\s*</div>'
pattern_ux_exact = r'<!-- VIEWPORT : UX RESEARCHER - FRANÇAIS -->[\s\S]*?<div class="reader-viewport" id="viewport_doc_af447_fr"'
replacement_ux_exact = f"{ux_fr_html}\n    \n\n{ux_en_html}\n    \n<div class=\"reader-viewport\" id=\"viewport_doc_af447_fr\""

assert re.search(pattern_ux_exact, html), "Impossible de localiser le bloc UX Researcher dans index.html !"
html = re.sub(pattern_ux_exact, replacement_ux_exact, html, count=1)
print("✅ Viewports UX Researcher (FR & EN) actualisés avec succès.")

# -----------------------------------------------------------------------------
# ÉTAPE E : ENREGISTREMENT DE INDEX.HTML
# -----------------------------------------------------------------------------
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("🎉 index.html mis à jour et sauvegardé avec succès en UTF-8 !")
