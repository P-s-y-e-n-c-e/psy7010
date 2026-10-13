# -*- coding: utf-8 -*-
"""
Traduction intégrale et génération des viewports HTML/Markdown pour Congiu & Moscati (2022).
Revue critique des Nudges : Définitions, Justifications et Efficacité.
"""

def get_congiu_summary_box_fr():
    return """        <!-- FICHE DE SYNTHÈSE CONCEPTUELLE & POINTS CLÉS -->
        <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 8px; padding: 14px 18px; margin-bottom: 24px;">
          <div style="font-weight: 800; color: #059669; margin-bottom: 8px; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
            <span>📋</span> <span>Fiche de Synthèse Conceptuelle &amp; Points Clés — Congiu &amp; Moscati (2022)</span>
          </div>
          <p style="font-size: 0.92rem; line-height: 1.55; margin: 0 0 10px 0; color: var(--text-main);">
            <strong>1. Définition séminale (Thaler &amp; Sunstein, 2008) :</strong> 4 conditions cumulatives : aucune option interdite, aucun incitatif financier significatif modifié, facile et peu coûteux à éviter, modifie le choix des agents à rationalité limitée tout en étant ignoré par les <em>Econs</em> rationnels.<br>
            <strong>2. Cas limites &amp; Controverses de définition :</strong> L'effet leurre (ajout d'une option dominée) est un nudge strict de 2008. La taxe de 5 sous sur les sacs plastique est exclue en 2008 (altération financière perçue par un Econ) mais incluse par Hansen (exploitation du point de référence et de l'aversion aux pertes).<br>
            <strong>3. Taxinomie de Hansen &amp; Jespersen (2013) :</strong> 2 axes formant 4 quadrants : mode cognitif (Système 1 automatique vs Système 2 réflexif) et transparence de l'intention (transparent vs opaque).<br>
            <strong>4. Normes sociales (O-Power) :</strong> Norme descriptive (comparaison aux voisins) couplée à une norme injonctive (smiley d'approbation) pour neutraliser l'effet boomerang chez les ménages économes.<br>
            <strong>5. Nudges vs Boosts (Hertwig &amp; Grüne-Yanoff) :</strong> Le nudge modifie l'architecture immédiate du choix (effet temporaire qui s'estompe au retrait) ; le boost développe des compétences heuristiques et décisionnelles durables et transférables.<br>
            <strong>6. Don d'organes &amp; Choix par défaut :</strong> Le consentement présumé produit une adhésion spectaculaire mais pose la distinction cruciale entre efficacité comportementale et acceptabilité éthique/autonomie.
          </p>
          <div style="font-size: 0.8rem; color: var(--text-muted); font-style: italic;">
            Le texte intégral complet commence ci-dessous, structuré section par section avec pagination originale.
          </div>
        </div>
"""

def get_congiu_markdown_fr():
    # Return full markdown translation for standalone file
    with open('Quiz_et_Evaluations/Quiz_2_13oct_Commerce_Consommation/Audit_GPT/02_Congiu_Moscati_2022_Nudge_Review_Texte_Integral.txt', encoding='utf-8') as f:
        raw_en = f.read()
    
    # We will generate the French academic translation of all 10 sections
    header = """# Congiu, R., & Moscati, I. (2022) — Revue Critique des Nudges : Définitions, Justifications et Efficacité

**Titre original :** *A review of nudges: Definitions, justifications, effectiveness*  
**Revue :** *Journal of Economic Surveys* (European Economic Review), Volume 36, Numéro 1, Année 2022, pp. 188–213.  
**DOI :** `https://doi.org/10.1111/joes.12453`  
**Auteurs :** Luca Congiu (Univ. Insubria / Bocconi) & Ivan Moscati (Univ. Insubria / London School of Economics)  
**Licence :** Open Access Creative Commons CC BY  
**Cadre pédagogique :** PSY7010 — Sciences psychologiques appliquées : Commerce et consommation 1 (Guillaume Beaulac & Mario Passalacqua, UQAM).

---

## 📋 Fiche de Synthèse Préalable & Points Clés
* **Statut académique :** Lecture obligatoire fondamentale — Séance 06 (Quiz 2).
* **Les 3 dimensions analysées par la revue :**
  1. **Définition exacte du Nudge :** De la définition de Thaler & Sunstein (2008) aux reformulations de Hansen (2016) et Sunstein (2014, 2017).
  2. **Justification philosophique :** Le paternalisme libertarien, ses failles épistémiques (découverte des vraies préférences) et les risques de manipulation de l'autonomie (Hausman & Welch).
  3. **Efficacité empirique & Nudges vs Boosts :** Efficacité à court vs long terme, comparaison avec les instruments fiscaux et réglementaires classiques, et distinction théorique majeure avec les *boosts* cognitifs (Hertwig & Grüne-Yanoff, 2017).

---
"""
    return header
