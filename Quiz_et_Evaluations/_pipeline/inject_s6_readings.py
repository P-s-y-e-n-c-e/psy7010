# -*- coding: utf-8 -*-
"""
Script d'injection des lectures intégrales de la Séance 06 dans index.html.
Remplace les résumés tronqués par les textes intégraux bilingues avec fiches de synthèse en tête.
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))

import build_chen_readings
import build_s6_viewports

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    start_marker = '<!-- VIEWPORT : CHEN (2024) - FRANÇAIS -->'
    end_marker = '<div class="reader-viewport" id="viewport_doc_af447_fr"'

    p1 = html.find(start_marker)
    p2 = html.find(end_marker)

    if p1 == -1 or p2 == -1 or p1 >= p2:
        raise ValueError(f"Impossible de localiser les délimiteurs S6 dans index.html ! p1={p1}, p2={p2}")

    print(f"Bloc S6 existant localisé de {p1} à {p2} (taille actuelle : {p2 - p1} caractères).")

    # Assembler les nouveaux viewports S6
    chen_fr = build_chen_readings.get_chen_html_fr()
    chen_en = build_chen_readings.get_chen_html_en()
    congiu_fr = build_s6_viewports.get_congiu_html_fr()
    congiu_en = build_s6_viewports.get_congiu_html_en()
    bva = build_s6_viewports.get_bva_html()
    ux = build_s6_viewports.get_ux_html()

    new_s6_block = (
        chen_fr + "\n\n" +
        chen_en + "\n\n" +
        congiu_fr + "\n\n" +
        congiu_en + "\n\n" +
        bva + "\n\n" +
        ux + "\n\n"
    )

    # Backup avant remplacement
    with open('Quiz_et_Evaluations/_pipeline/backup_index_before_s6_full_readings.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Sauvegarde effectuée : backup_index_before_s6_full_readings.html")

    updated_html = html[:p1] + new_s6_block + html[p2:]

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print(f"✅ Injection réussie dans index.html ! Nouveau bloc S6 : {len(new_s6_block)} caractères.")

if __name__ == '__main__':
    main()
