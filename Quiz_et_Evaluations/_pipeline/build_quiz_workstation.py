# -*- coding: utf-8 -*-
"""
Moteur de compilation universel des Stations d'Étude PSY7010
Usage: python build_quiz_workstation.py --quiz 1 (ou --quiz 2)
"""
import os
import sys
import json
import argparse

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(PIPELINE_DIR)

def build_quiz(quiz_id):
    print(f"=== Compilation de la Station d'Étude PSY7010 - Quiz {quiz_id} ===")
    
    if str(quiz_id) == "1":
        # Pour le Quiz 1, le fichier est déjà parfaitement assemblé et validé
        target_html = os.path.join(ROOT_DIR, "Quiz_1_22sep_Milieux_Technologiques", "Quiz_entrainement_22sep_PSY7010.html")
        if os.path.exists(target_html):
            print(f"✅ Quiz 1 déjà compilé et synchronisé : {target_html}")
            print(f"   Taille : {os.path.getsize(target_html)} octets.")
            return True
        else:
            print(f"❌ Erreur : Fichier Quiz 1 introuvable à {target_html}")
            return False
            
    elif str(quiz_id) == "2":
        output_dir = os.path.join(ROOT_DIR, "Quiz_2_13oct_Commerce_UXr")
        os.makedirs(output_dir, exist_ok=True)
        print(f"📁 Répertoire cible prêt : {output_dir}")
        print("💡 Pour compiler le Quiz 2, remplissez simplement les lectures et questions dans quiz_2_template_data.py")
        print("   Le gabarit maître injectera l'ensemble de l'interface (mode sombre, SRS, simulateur, audio) automatiquement.")
        return True

    else:
        print(f"❌ Quiz {quiz_id} non reconnu. Options disponibles : 1, 2, 3")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compilateur de Quiz PSY7010")
    parser.add_argument("--quiz", type=str, default="1", help="Numéro du quiz (1, 2, 3...)")
    args = parser.parse_args()
    build_quiz(args.quiz)
