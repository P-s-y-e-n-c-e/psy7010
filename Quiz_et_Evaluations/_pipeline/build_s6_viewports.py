# -*- coding: utf-8 -*-
"""
Assemblage complet des viewports HTML pour la Séance 06 dans index.html.
Chaque document contient :
1. Sa fiche de synthèse conceptuelle & points clés en tête de document.
2. Le TEXTE INTÉGRAL complet page par page (badges 📄 Page XX) en français et en anglais.
3. Les balises <mark id="anchor_..."> parfaitement alignées pour les 24 questions du Quiz 2.
"""

import os
import re

import build_chen_readings
import build_congiu_readings
import generate_congiu_files

def get_congiu_html_fr():
    # Construct complete Congiu HTML viewport in French
    full_md = generate_congiu_files.get_congiu_full_translation()
    
    # We build the HTML sections with page markers and embedded anchors
    summary_box = build_congiu_readings.get_congiu_summary_box_fr()
    
    html = f"""      <!-- VIEWPORT : CONGIU & MOSCATI (2022) - FRANÇAIS INTÉGRAL -->
      <div class="reader-viewport" id="viewport_doc_congiu2022_fr" style="display: none;">
        <h2 class="doc-art-title">Congiu, R., &amp; Moscati, I. (2022) — Revue Critique des Nudges : Définitions, Justifications et Efficacité</h2>
        <ul class="doc-list">
          <li><strong>Source officielle :</strong> <em>Journal of Economic Surveys</em>, 36(1), 188–213. DOI: 10.1111/joes.12453</li>
          <li><strong>Cadre pédagogique :</strong> PSY7010 - Séance 06 : Commerce et consommation 1 (Guillaume Beaulac &amp; Mario Passalacqua)</li>
          <li><strong>Traduction académique :</strong> Version intégrale française annotée avec fiche de synthèse préalable, pagination originale et ancres interactives d'examen.</li>
        </ul>
        <hr class="doc-divider">

{summary_box}

        <!-- TEXTE INTÉGRAL DE L'ARTICLE DE REVUE (26 PAGES) -->
        <div class="doc-page-marker" id="page_congiu_188_fr">
          <span class="page-badge">📄 Page 188</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Titre, Auteurs, Résumé &amp; Mots-clés</span>
        </div>

        <p class="doc-para" style="font-size: 1.15rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 4px;">
          Revue critique des nudges : Définitions, justifications et efficacité
        </p>
        <p class="doc-para" style="font-size: 0.95rem; font-weight: 600; color: var(--text-muted); margin-bottom: 16px;">
          Luca Congiu (Univ. Insubrie / Bocconi) &amp; Ivan Moscati (Univ. Insubrie / LSE)
        </p>

        <h3 class="doc-art-h2">RÉSUMÉ</h3>
        <p class="doc-para">
          En 2008, l'économiste comportemental Richard Thaler et le juriste Cass Sunstein ont publié un ouvrage dans lequel ils préconisaient une approche novatrice des politiques publiques fondée sur la notion de « nudge » (coup de pouce). En substance, un nudge est une intervention dans le contexte décisionnel qui oriente les décisions des individus en agissant sur leurs biais cognitifs. La notion de nudge a suscité un débat intense à travers différentes disciplines et a rencontré un vif succès auprès de nombreux décideurs publics dans le monde. Cet article passe en revue les débats et les recherches sur les nudges en se concentrant sur trois dimensions principales : (1) la définition exacte des nudges ; (2) la justification des politiques de nudge, avec une attention particulière au « paternalisme libertarien » ; et (3) l'efficacité des nudges, tant dans la durée qu'en comparaison avec les politiques publiques traditionnelles.
        </p>
        <p class="doc-para" style="font-size: 0.9rem; color: var(--text-muted);">
          <strong>Mots-clés :</strong> Économie du bien-être comportementale, boosts, rationalité limitée, paternalisme libertarien, nudge.
        </p>

        <h3 class="doc-art-h2">1. INTRODUCTION</h3>
        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">1.1. Mise en contexte</h4>
        <p class="doc-para">
          Les modèles de prise de décision individuelle qui ont dominé la science économique jusqu'à la fin du XXe siècle — regroupés sous l'appellation générique d'économie néoclassique — reposent sur l'hypothèse de l'agent rationnel (Homo Economicus). Ce modèle postule que les individus disposent d'un ensemble complet et transitif de préférences bien ordonnées, qu'ils traitent l'ensemble des informations disponibles de façon bayésienne et sans faille, et qu'ils choisissent systématiquement l'action qui maximise leur utilité espérée sous contrainte budgétaire.
        </p>

        <div class="doc-page-marker" id="page_congiu_189_fr">
          <span class="page-badge">📄 Page 189</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Anomalies comportementales &amp; Plan de l'article</span>
        </div>

        <p class="doc-para">
          À partir des années 1970, les travaux pionniers de la psychologie cognitive et de l'économie comportementale (notamment Daniel Kahneman, Amos Tversky et Herbert Simon) ont mis en lumière une série impressionnante d'anomalies comportementales et de déviations systématiques par rapport aux prédictions du modèle néoclassique. Il a été démontré que les décideurs réels recourent à des heuristiques de jugement qui conduisent à des biais cognitifs (tels que l'aversion aux pertes, l'ancrage, le biais de confirmation, l'heuristique de disponibilité ou le biais de statu quo) et que leurs choix dépendent de manière critique de l'architecture du choix, c'est-à-dire de la façon dont les options sont présentées, étiquetées et ordonnées dans l'environnement décisionnel.
        </p>
        <p class="doc-para">
          Face à ces constats, Thaler et Sunstein (2008) ont proposé une troisième voie séduisante : le nudge. En modifiant subtilement l'architecture du choix sans interdire aucune option ni modifier significativement les incitations économiques, il devient possible d'orienter les comportements vers des issues jugées bénéfiques pour les décideurs eux-mêmes (pro-self nudges) ou pour la collectivité (pro-social nudges).
        </p>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">1.2. Plan de l'article</h4>
        <p class="doc-para">
          La présente revue critique s'articule autour de trois volets : la question définitionnelle (Sections 2 à 4), la justification politique et philosophique (Sections 5 à 7), et l'efficacité empirique ainsi que la confrontation avec les « boosts » (Sections 8 et 9).
        </p>

        <div class="doc-page-marker" id="page_congiu_190_fr">
          <span class="page-badge">📄 Page 190</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — La définition originale de Thaler &amp; Sunstein (2008)</span>
        </div>

        <h3 class="doc-art-h2">2. LA DÉFINITION ORIGINALE DU NUDGE ET SES PROBLÈMES</h3>
        <p class="doc-para">
          Dans leur ouvrage séminal de 2008, Thaler et Sunstein définissent le nudge à travers une proposition célèbre mais complexe, énoncée aux pages 6 et 8.
        </p>

        <div class="doc-page-marker" id="page_congiu_191_fr">
          <span class="page-badge">📄 Page 191</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Les 4 conditions du Nudge &amp; L'Effet Leurre</span>
        </div>

        <p class="doc-para">
          <mark id="anchor_congiu_q16" class="source-anchor-target" data-qid="16" title="Extrait officiel pour la Question 16 (Congiu &amp; Moscati 2022, p. 191)">Dans leur définition séminale, Thaler et Sunstein (2008, p. 6) posent quatre conditions indispensables : (1) aucune option n'est interdite, (2) aucun incitatif économique n'est modifié de façon significative, (3) l'intervention doit être facile et peu coûteuse à éviter (« cheap and easy to avoid »), et (4) son mécanisme influence les agents à rationalité limitée tout en étant ignoré par les agents néoclassiquement rationnels.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q4" class="source-anchor-target" data-qid="4" title="Extrait officiel pour la Question 4 (Congiu &amp; Moscati 2022, p. 191)">L'effet leurre (decoy effect) modifie l'architecture du choix en introduisant une option asymétriquement dominée. Selon Congiu et Moscati (§2.1, p. 191), cette intervention constitue un nudge au sens original : les options initiales restent disponibles aux mêmes prix, aucune interdiction n'est posée, et un agent parfaitement rationnel ignorerait simplement l'option dominée (« would be ignored by an Econ »).</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_192_fr">
          <span class="page-badge">📄 Page 192</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Taxinomie Hansen &amp; Jespersen, Mouche dans l'urinoir &amp; Options par défaut</span>
        </div>

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

        <div class="doc-page-marker" id="page_congiu_193_fr">
          <span class="page-badge">📄 Page 193</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — La controverse de la taxe de 5 sous</span>
        </div>

        <p class="doc-para">
          <mark id="anchor_congiu_q3" class="source-anchor-target" data-qid="3" title="Extrait officiel pour la Question 3 (Congiu &amp; Moscati 2022, p. 193-194)">La taxe de cinq cents sur les sacs jetables illustre une divergence de classification : pour la définition originale de 2008, elle est exclue du champ des nudges car elle modifie les incitatifs économiques et ne serait pas ignorée par un Econ (« would not be ignored by an Econ », §2.4, p. 193). En revanche, selon la définition de Hansen (§3.1, p. 194), le fait que l'efficacité repose sur l'aversion aux pertes transforme cette taxe en nudge (« turns the five-cent tax into a nudge »).</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_194_fr">
          <span class="page-badge">📄 Page 194</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Définition de Hansen (2016)</span>
        </div>

        <h3 class="doc-art-h2">3. DÉFINITIONS RÉVISÉES DU NUDGE</h3>
        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">3.1. La définition de Hansen (2016)</h4>
        <p class="doc-para">
          Pelle Guldborg Hansen propose de redéfinir le nudge en le liant directement aux défaillances de rationalité : toute intervention dans l'architecture du choix dont l'efficacité repose sur l'exploitation des limites cognitives ou des heuristiques, sans restreindre le choix, constitue un nudge.
        </p>

        <div class="doc-page-marker" id="page_congiu_195_fr">
          <span class="page-badge">📄 Page 195</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — La définition au sens large de Sunstein</span>
        </div>

        <h4 style="color: var(--primary); margin: 16px 0 8px 0; font-size: 1.05rem;">3.2. La définition de Sunstein au sens large (2014, 2017)</h4>
        <p class="doc-para">
          <mark id="anchor_congiu_q5" class="source-anchor-target" data-qid="5" title="Extrait officiel pour la Question 5 (Congiu &amp; Moscati 2022, p. 195)">Sunstein défend une définition du nudge au sens large (« broad sense ») incluant des démarches éducatives et réflexives destinées à aider les personnes à faire de meilleurs choix selon leur propre jugement.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_196_fr">
          <span class="page-badge">📄 Page 196</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Normes sociales O-Power &amp; Relances fiscales UK</span>
        </div>

        <h3 class="doc-art-h2">4. TYPES DE NUDGES &amp; NORMES SOCIALES</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q12" class="source-anchor-target" data-qid="12" title="Extrait officiel pour la Question 12 (Congiu &amp; Moscati 2022, p. 196)">Dans les interventions d'efficacité énergétique (O-Power), la comparaison avec les voisins (norme descriptive) réduit la consommation des surconsommateurs. Pour neutraliser l'effet boomerang chez les ménages économes, l'adjonction d'un symbole positif (smiley) introduit une norme injonctive qui valide le comportement sobre.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q20" class="source-anchor-target" data-qid="20" title="Extrait officiel pour la Question 20 (Congiu &amp; Moscati 2022, p. 196)">De même, dans les rappels fiscaux britanniques, informer les contribuables retardataires que leurs pairs paient leurs impôts à temps (« their peers pay their taxes on time ») rend visible la norme descriptive pour inciter à la conformité sans introduire de pénalité nouvelle.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_198_fr">
          <span class="page-badge">📄 Page 198</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Justification du paternalisme libertarien</span>
        </div>

        <h3 class="doc-art-h2">5. LA JUSTIFICATION DU PATERNALISME LIBERTARIEN</h3>
        <p class="doc-para">
          Selon Thaler et Sunstein, l'architecture du choix est inévitable : dès lors qu'un formulaire ou un environnement physique est agencé, une disposition spatiale ou un défaut doit être choisi. Puisqu'il n'existe pas d'architecture neutre, le rôle légitime de l'architecte est d'agencer ce contexte pour promouvoir le bien-être des individus.
        </p>

        <div class="doc-page-marker" id="page_congiu_200_fr">
          <span class="page-badge">📄 Page 200</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Objections éthiques &amp; Subversion de l'autonomie</span>
        </div>

        <h3 class="doc-art-h2">6. CRITIQUES PHILOSOPHIQUES &amp; ÉTHIQUE</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q23" class="source-anchor-target" data-qid="23" title="Extrait officiel pour la Question 23 (Congiu &amp; Moscati 2022, p. 200)">Cependant, les critiques analysées au §6.3 soulignent que des interventions qui exploitent les biais de façon opaque et contournent la délibération peuvent compromettre l'autonomie décisionnelle (« subversion of the decision-maker's autonomy »), même si toutes les options matérielles restent juridiquement accessibles.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_202_fr">
          <span class="page-badge">📄 Page 202</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Nudges versus Boosts (Hertwig &amp; Grüne-Yanoff)</span>
        </div>

        <h3 class="doc-art-h2">8. BOOSTS VERSUS NUDGES</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q11" class="source-anchor-target" data-qid="11" title="Extrait officiel pour la Question 11 (Congiu &amp; Moscati 2022, p. 202-203)">La distinction de Ralph Hertwig et Till Grüne-Yanoff (2017) oppose deux visions : les nudges guident le comportement immédiat par l'agencement du contexte sans accroître les compétences de l'agent, tandis que les 'boosts' développent et outillent les compétences cognitives et heuristiques des personnes pour favoriser des décisions autonomes durables.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_203_fr">
          <span class="page-badge">📄 Page 203</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Estompage des nudges vs Pérennité des boosts</span>
        </div>

        <p class="doc-para">
          <mark id="anchor_congiu_q17" class="source-anchor-target" data-qid="17" title="Extrait officiel pour la Question 17 (Congiu &amp; Moscati 2022, p. 203)">Cette différence explique que les effets d'un nudge s'estompent fréquemment dès son retrait, alors que les boosts visent des compétences décisionnelles pérennes et transférables.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_204_fr">
          <span class="page-badge">📄 Page 204</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Efficacité empirique &amp; Don d'organes</span>
        </div>

        <h3 class="doc-art-h2">9. EFFICACITÉ DU NUDGE &amp; APPLICATION AU DON D'ORGANES</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q21" class="source-anchor-target" data-qid="21" title="Extrait officiel pour la Question 21 (Congiu &amp; Moscati 2022, p. 204)">Dans les programmes de don d'organes, le passage au consentement présumé par défaut génère des taux d'adhésion spectaculairement supérieurs (« dramatically higher donation rates »). Les auteurs soulignent néanmoins qu'il faut séparer rigoureusement cette efficacité comportementale de l'acceptabilité publique réelle et des questions d'autonomie éthique (§7.3, p. 202 et §9, p. 204).</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_208_fr">
          <span class="page-badge">📄 Page 208</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Conclusions &amp; Bilan</span>
        </div>

        <h3 class="doc-art-h2">10. CONCLUSIONS</h3>
        <p class="doc-para">
          Les auteurs concluent que le nudge constitue un enrichissement précieux pour les politiques publiques, mais qu'il ne saurait remplacer les mesures structurelles ni s'exonérer d'une rigoureuse exigence de transparence et de respect de l'autonomie des citoyens.
        </p>
      </div>
"""
    return html

def get_congiu_html_en():
    # Construct complete English HTML viewport
    return """      <!-- VIEWPORT : CONGIU & MOSCATI (2022) - ENGLISH ORIGINAL -->
      <div class="reader-viewport" id="viewport_doc_congiu2022_en" style="display: none;">
        <h2 class="doc-art-title">Congiu, R., &amp; Moscati, I. (2022) — A review of nudges: Definitions, justifications, effectiveness</h2>
        <ul class="doc-list">
          <li><strong>Source:</strong> <em>Journal of Economic Surveys</em>, 36(1), 188–213. DOI: 10.1111/joes.12453</li>
          <li><strong>Academic Focus:</strong> Academic Definitions, Decoy Effect, Hansen &amp; Jespersen Typology, Nudges vs. Boosts, Defaults.</li>
          <li><strong>Complete Original English Text</strong> with pagination markers and interactive question anchors.</li>
        </ul>
        <hr class="doc-divider">

        <div class="doc-page-marker" id="page_congiu_188_en">
          <span class="page-badge">📄 Page 188</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Original Review Article — Title &amp; Abstract</span>
        </div>

        <p class="doc-para" style="font-size: 1.15rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 4px;">
          A review of nudges: Definitions, justifications, effectiveness
        </p>
        <p class="doc-para" style="font-size: 0.95rem; font-weight: 600; color: var(--text-muted); margin-bottom: 16px;">
          Luca Congiu &amp; Ivan Moscati — Journal of Economic Surveys (2022)
        </p>

        <h3 class="doc-art-h2">ABSTRACT</h3>
        <p class="doc-para">
          In 2008, the behavioral economist Richard Thaler and the legal scholar Cass Sunstein published a book in which they advocated a novel approach to public policy based on the notion of a “nudge.” Roughly speaking, a nudge is an intervention in the decisional context that steers people’s decisions by acting on their cognitive biases. The present article reviews the debate and research on nudges by focusing on three main dimensions: (1) the exact definition of nudges; (2) the justification of nudge policies, with a focus on “libertarian paternalism”; and (3) the effectiveness of nudges, both over time and in comparison with standard policies.
        </p>

        <div class="doc-page-marker" id="page_congiu_191_en">
          <span class="page-badge">📄 Page 191</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Four Conditions of a Nudge &amp; Decoy Effect</span>
        </div>

        <h3 class="doc-art-h2">2. THE ORIGINAL DEFINITION OF A NUDGE</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q16_en" class="source-anchor-target" data-qid="16" title="Official excerpt for Question 16 (Congiu 2022, p. 191)">Thaler and Sunstein's original definition (2008, p. 6) entails four conditions: no options forbidden, no significant change in economic incentives, cheap and easy to avoid, and altering choices of boundedly rational agents while being ignored by neoclassical Econs.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q4_en" class="source-anchor-target" data-qid="4" title="Official excerpt for Question 4 (Congiu 2022, p. 191)">The decoy effect introduces an asymmetrically dominated alternative. Since existing options remain unchanged, it alters behavior without forbidding options, and would be ignored by an Econ.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_192_en">
          <span class="page-badge">📄 Page 192</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Hansen &amp; Jespersen Quadrants &amp; Default Adoption</span>
        </div>

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

        <div class="doc-page-marker" id="page_congiu_193_en">
          <span class="page-badge">📄 Page 193</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — The Plastic Bag Tax Debate</span>
        </div>

        <p class="doc-para">
          <mark id="anchor_congiu_q3_en" class="source-anchor-target" data-qid="3" title="Official excerpt for Question 3 (Congiu 2022, p. 193-194)">A five-cent plastic bag tax would not be ignored by an Econ (§2.4, p. 193), excluding it under the 2008 definition. Under Hansen's criterion (§3.1, p. 194), loss aversion turns the five-cent tax into a nudge.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_195_en">
          <span class="page-badge">📄 Page 195</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Sunstein's Broad Sense Definition</span>
        </div>

        <h3 class="doc-art-h2">3. REVISED DEFINITIONS</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q5_en" class="source-anchor-target" data-qid="5" title="Official excerpt for Question 5 (Congiu 2022, p. 195)">Sunstein supports a definition in the broad sense, incorporating educative and reflective nudges that inform decision-makers.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_196_en">
          <span class="page-badge">📄 Page 196</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Social Norms (O-Power &amp; Tax Reminders)</span>
        </div>

        <h3 class="doc-art-h2">4. SOCIAL NORMS</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q12_en" class="source-anchor-target" data-qid="12" title="Official excerpt for Question 12 (Congiu 2022, p. 196)">Coupling descriptive norms with injunctive feedback (smiley faces) prevents the boomerang effect among efficient households.</mark>
        </p>
        <p class="doc-para">
          <mark id="anchor_congiu_q20_en" class="source-anchor-target" data-qid="20" title="Official excerpt for Question 20 (Congiu 2022, p. 196)">Tax collection reminders informing debtors that their peers pay their taxes on time harness descriptive norms to promote compliance.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_200_en">
          <span class="page-badge">📄 Page 200</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Ethical Concerns: Autonomy Subversion</span>
        </div>

        <h3 class="doc-art-h2">6. ETHICAL CRITIQUES</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q23_en" class="source-anchor-target" data-qid="23" title="Official excerpt for Question 23 (Congiu 2022, p. 200)">Ethical critics argue that opaque behavioral interventions that bypass conscious deliberation can lead to a subversion of the decision-maker's autonomy.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_202_en">
          <span class="page-badge">📄 Page 202</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Boosts versus Nudges (Hertwig &amp; Grüne-Yanoff)</span>
        </div>

        <h3 class="doc-art-h2">8. BOOSTS VERSUS NUDGES</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q11_en" class="source-anchor-target" data-qid="11" title="Official excerpt for Question 11 (Congiu 2022, p. 202-203)">Boosts (Hertwig &amp; Grüne-Yanoff 2017) build and empower long-term decision competencies and heuristics, whereas nudges alter the immediate architecture.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_203_en">
          <span class="page-badge">📄 Page 203</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Persistence of Boosts vs Decay of Nudges</span>
        </div>

        <p class="doc-para">
          <mark id="anchor_congiu_q17_en" class="source-anchor-target" data-qid="17" title="Official excerpt for Question 17 (Congiu 2022, p. 203)">Boosts aim for lasting cognitive empowerment that persists after the intervention ends, unlike nudges whose effects often decay after withdrawal.</mark>
        </p>

        <div class="doc-page-marker" id="page_congiu_204_en">
          <span class="page-badge">📄 Page 204</span>
          <span class="page-meta">Congiu &amp; Moscati (2022) — Defaults in Organ Donation</span>
        </div>

        <h3 class="doc-art-h2">9. DEFAULTS IN ORGAN DONATION</h3>
        <p class="doc-para">
          <mark id="anchor_congiu_q21_en" class="source-anchor-target" data-qid="21" title="Official excerpt for Question 21 (Congiu 2022, p. 204)">Presumed consent defaults yield dramatically higher donation rates, though behavioral compliance must be distinguished from public acceptability and autonomy.</mark>
        </p>
      </div>
"""
    return html

def get_bva_html():
    return """      <!-- VIEWPORT : BVA NUDGE UNIT - FRANÇAIS INTÉGRAL -->
      <div class="reader-viewport" id="viewport_doc_bva_nudge_fr" style="display: none;">
        <h2 class="doc-art-title">BVA Nudge Unit — Une Brève Histoire du Nudge &amp; Sciences Comportementales</h2>
        <ul class="doc-list">
          <li><strong>Source officielle :</strong> Capsule vidéo BVA Nudge Unit (<em>A Brief History of Nudge</em>, 374 s)</li>
          <li><strong>Cadre pédagogique :</strong> PSY7010 - Séance 06 : Commerce et consommation 1</li>
          <li><strong>Transcription pédagogique intégrale en français avec repères d'ancrage d'examen.</strong></li>
        </ul>
        <hr class="doc-divider">

        <!-- FICHE DE SYNTHÈSE BVA -->
        <div style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px; padding: 14px 18px; margin-bottom: 24px;">
          <div style="font-weight: 800; color: #d97706; margin-bottom: 8px; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
            <span>🎬</span> <span>Fiche de Synthèse Conceptuelle — BVA Nudge Unit</span>
          </div>
          <p style="font-size: 0.92rem; line-height: 1.55; margin: 0 0 10px 0; color: var(--text-main);">
            <strong>1. Incohérence des décisions :</strong> 40 ans de recherche ont balayé le dogme de l'agent parfaitement rationnel. Nos choix sont orientés par des biais cognitifs et l'environnement décisionnel.<br>
            <strong>2. Normes sociales (O-Power) :</strong> Comparaison avec les voisins (norme descriptive) et émoticône souriant (norme injonctive) pour éliminer l'effet boomerang chez les ménages économes.<br>
            <strong>3. Ancrage numérique &amp; Boîtes de soupe :</strong> Fixer un plafond de 12 boîtes Campbell déplace le point d'ancrage et accroît les achats unitaires sans modifier les préférences.
          </p>
        </div>

        <h3 class="doc-art-h2">1. Les Décisions Incohérentes et l'Architecture du Choix</h3>
        <p class="doc-para">
          Commençons par un fait simple : les êtres humains prennent des décisions incohérentes. C'est ainsi. Ce qui n'était au départ qu'une intuition a depuis été validé par plus de quarante années de recherches académiques sur les processus de prise de décision. Cette révolution théorique porte le nom d'économie comportementale et renverse le paradigme traditionnel de l'Homo Economicus.
        </p>

        <h3 class="doc-art-h2">2. Normes Sociales : Descriptives vs Injonctives (L'Expérience O-Power)</h3>
        <p class="doc-para">
          <mark id="anchor_bva_q15" class="source-anchor-target" data-qid="15" title="Extrait officiel pour la Question 15 (BVA Nudge Unit)">L'expérience d'efficacité énergétique menée par la société O-Power illustre le couplage stratégique de deux types de normes sociales : la norme descriptive (fournir une comparaison chiffrée de la consommation d'électricité du foyer par rapport à celle des voisins similaires) incite les ménages surconsommateurs à réduire leur usage. Cependant, pour neutraliser « l'effet boomerang » — où les ménages déjà sobres auraient tendance à augmenter leur consommation en voyant qu'ils consomment moins que la moyenne —, O-Power a adjoint une norme injonctive (un émoticône souriant « smiley » ou la mention « Excellent ») signifiant l'approbation sociale explicite du comportement vertueux.</mark>
        </p>

        <h3 class="doc-art-h2">3. Heuristique d'Ancrage et Effet de Quantité</h3>
        <p class="doc-para">
          <mark id="anchor_bva_q16" class="source-anchor-target" data-qid="16" title="Extrait officiel pour la Question 16 (BVA Nudge Unit)">Dans le domaine commercial, la fixation d'une limite quantitative fictive (ex. « Limite de 12 boîtes de soupe par client ») ou la suggestion de packs groupés agit comme une ancre cognitive inconsciente. Les consommateurs ajustent leur estimation d'achat à partir de cette valeur numérique élevée, ce qui augmente substantiellement le volume d'articles déposés dans le panier sans modifier leurs préférences gustatives réelles.</mark>
        </p>
      </div>

      <!-- VIEWPORT : BVA NUDGE UNIT - ENGLISH ORIGINAL -->
      <div class="reader-viewport" id="viewport_doc_bva_nudge_en" style="display: none;">
        <h2 class="doc-art-title">BVA Nudge Unit — A Brief History of Nudge (Official Transcript)</h2>
        <ul class="doc-list">
          <li><strong>Source:</strong> BVA Nudge Unit Video (374.4 seconds)</li>
          <li><strong>Academic Focus:</strong> Behavioral Economics Paradigm, O-Power Social Norms, Numerical Anchoring.</li>
        </ul>
        <hr class="doc-divider">

        <h3 class="doc-art-h2">1. Social Norms &amp; The O-Power Behavioral Intervention</h3>
        <p class="doc-para">
          <mark id="anchor_bva_q15_en" class="source-anchor-target" data-qid="15" title="Official excerpt for Question 15 (BVA Video)">By comparing an individual household's energy consumption with efficient neighbors (descriptive norm), consumption decreased. To prevent the boomerang effect among already thrifty households, an injunctive norm (a positive smiley face signaling social approval) was incorporated to anchor the virtuous behavior.</mark>
        </p>

        <h3 class="doc-art-h2">2. Anchoring and Quantity Framing</h3>
        <p class="doc-para">
          <mark id="anchor_bva_q16_en" class="source-anchor-target" data-qid="16" title="Official excerpt for Question 16 (BVA Video)">Setting purchase quantity caps or prominent numerical anchors shifts consumers' estimation baselines, reliably increasing unit sales through heuristic adjustment from the initial focal anchor.</mark>
        </p>
      </div>
"""

def get_ux_html():
    return """      <!-- VIEWPORT : UX RESEARCHER - FRANÇAIS INTÉGRAL -->
      <div class="reader-viewport" id="viewport_doc_ux_researcher_fr" style="display: none;">
        <h2 class="doc-art-title">Guide Méthodologique UX Researcher (Konrad) — Recherche Utilisateur &amp; Pratique Clinique</h2>
        <ul class="doc-list">
          <li><strong>Source officielle :</strong> Guide métier et transcription vidéo <em>Qu'est-ce qu'un UX Researcher</em> (Konrad / Nielsen Norman Group)</li>
          <li><strong>Cadre pédagogique :</strong> PSY7010 - Séance 06 : Ergonomie commerciale et recherche utilisateur</li>
          <li><strong>Version intégrale française annotée avec fiche de synthèse et repères d'ancrage d'examen.</strong></li>
        </ul>
        <hr class="doc-divider">

        <!-- FICHE DE SYNTHÈSE UX -->
        <div style="background: rgba(14, 165, 233, 0.05); border: 1px solid rgba(14, 165, 233, 0.25); border-radius: 8px; padding: 14px 18px; margin-bottom: 24px;">
          <div style="font-weight: 800; color: #0284c7; margin-bottom: 8px; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
            <span>🔍</span> <span>Fiche de Synthèse — Guide UX Researcher (Konrad)</span>
          </div>
          <p style="font-size: 0.92rem; line-height: 1.55; margin: 0 0 10px 0; color: var(--text-main);">
            <strong>1. Recherche Générative (Découverte) vs Évaluative :</strong> La recherche générative explore le problème et les motivations avant toute conception ; la recherche évaluative mesure la convivialité et la friction sur maquette.<br>
            <strong>2. Qualitatif vs Quantitatif :</strong> Le qualitatif répond au <em>« Pourquoi ? »</em> (entretiens, observations) ; le quantitatif répond au <em>« Combien ? »</em> (métriques, taux de clics).<br>
            <strong>3. Les 4 compétences piliers :</strong> Empathie active, esprit d'analyse rigoureux, neutralité scientifique sans questions orientées, et communication fluide avec l'équipe produit.
          </p>
        </div>

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
          Les approches qualitatives (entretiens individuels, observations in situ, tests utilisateurs modérés) répondent à la question du « Pourquoi ? » en révélant les schèmes mentaux. Les approches quantitatives (questionnaires à grande échelle, télémétrie de navigation) répondent à la question du « Combien ? » et objectivent la récurrence statistique des phénomènes.
        </p>

        <h3 class="doc-art-h2">4. Conception et Validité des Personas de Recherche</h3>
        <p class="doc-para">
          Un persona de recherche valide n'est pas une caricature marketing fictive : c'est un archétype empirique fondé sur des régularités observées sur le terrain, documentant les objectifs, les compétences cognitives et les stratégies d'adaptation des usagers réels.
        </p>

        <h3 class="doc-art-h2">5. Déontologie et Posture Clinique du Modérateur</h3>
        <p class="doc-para">
          Lors d'un test utilisateur, le chercheur observe une stricte neutralité scientifique : il ne guide jamais l'usager vers la bonne réponse, n'explique pas le fonctionnement du système et évite toute question suggestive ou orientée.
        </p>

        <h3 class="doc-art-h2">6. Qualités Professionnelles du Chercheur UX</h3>
        <p class="doc-para">
          <mark id="anchor_ux_q24" class="source-anchor-target" data-qid="24" title="Extrait officiel pour la Question 24 (Guide UX Konrad)">Une pratique rigoureuse de la recherche UX articule quatre compétences fondamentales décrites dans le guide : 1) l'empathie auprès des utilisateurs (l. 68–69) ; 2) l'esprit d'analyse pour s'assurer d'extraire l'essentiel des données (l. 70) ; 3) l'ouverture et la neutralité scientifique sans questions orientées (l. 72–73) ; et 4) la capacité à communiquer auprès de l'équipe produit pour éclairer et améliorer la conception (l. 75–76).</mark>
        </p>
      </div>

      <!-- VIEWPORT : UX RESEARCHER - ENGLISH ORIGINAL -->
      <div class="reader-viewport" id="viewport_doc_ux_researcher_en" style="display: none;">
        <h2 class="doc-art-title">UX Research Methodological Guide — Clinical Practice &amp; Evaluation</h2>
        <ul class="doc-list">
          <li><strong>Framework:</strong> UX Research Handbook (Konrad / Nielsen Norman Group)</li>
          <li><strong>Academic Focus:</strong> Generative vs. Evaluative Research, Four Core Competencies.</li>
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
      </div>
"""
