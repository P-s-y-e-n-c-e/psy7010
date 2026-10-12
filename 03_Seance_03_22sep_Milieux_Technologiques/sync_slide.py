#!/usr/bin/env python3
"""
sync_slide.py — Synchronisation temps réel des diapositives & offsets ENCORA pour PSY7010
Usage:
    python sync_slide.py <slide_number> [HH:MM:SS]

Exemple:
    python sync_slide.py 3
    python sync_slide.py 3 10:00:03
"""

import sys
import re
import os
import json
from datetime import datetime, timedelta
from pathlib import Path

# Constantes de synchronisation Séance 03 (22 sept 2026)
T0_REC1_STR = "09:56:00"  # S24
T0_REC2_STR = "09:54:00"  # S24D

WORKSPACE_DIR = Path(r"g:\My Drive\UQAM\Maitrise (2194)\PSY7010\03_Seance_03_22sep_Milieux_Technologiques")
BRAIN_DIR = Path(r"C:\Users\Psyence\.gemini\antigravity\brain\9fc66e12-291d-4f7c-b246-276f84c15211")

NOTES_PATH = WORKSPACE_DIR / "notes_seance_03_2026-09-22.md"
WORKSPACE_HTML = WORKSPACE_DIR / "diaporama_cours_03.html"
BRAIN_HTML = BRAIN_DIR / "diaporama_cours_03.html"
BRAIN_META = BRAIN_DIR / "diaporama_cours_03.html.metadata.json"

def format_offset(target_dt, t0_dt):
    diff = int((target_dt - t0_dt).total_seconds())
    prefix = "-" if diff < 0 else ""
    abs_sec = abs(diff)
    h = abs_sec // 3600
    m = (abs_sec % 3600) // 60
    s = abs_sec % 60
    if h > 0:
        return f"{prefix}{h:02d}:{m:02d}:{s:02d}"
    return f"{prefix}{m:02d}:{s:02d}"

def sync_slide(slide_num, time_str=None):
    today = datetime.now().date()
    t0_rec1 = datetime.strptime(f"{today} {T0_REC1_STR}", "%Y-%m-%d %H:%M:%S")
    t0_rec2 = datetime.strptime(f"{today} {T0_REC2_STR}", "%Y-%m-%d %H:%M:%S")

    if time_str:
        current_dt = datetime.strptime(f"{today} {time_str}", "%Y-%m-%d %H:%M:%S")
    else:
        current_dt = datetime.now()
        time_str = current_dt.strftime("%H:%M:%S")

    offset_rec1 = format_offset(current_dt, t0_rec1)
    offset_rec2 = format_offset(current_dt, t0_rec2)

    slide_idx = slide_num - 1
    slide_pad = f"{slide_num:02d}"

    print(f"[{time_str} EDT] Transition vers Diapositive D{slide_pad}")
    print(f"• Offset Rec 1 (S24)  : {offset_rec1}")
    print(f"• Offset Rec 2 (S24D) : {offset_rec2}")

    # 1. Mise à jour de l'artefact HTML (Brain & Workspace)
    for html_path in [BRAIN_HTML, WORKSPACE_HTML]:
        if html_path.exists():
            content = html_path.read_text(encoding="utf-8")
            # Remplacer renderSlide(\d+) par renderSlide(slide_idx)
            new_content = re.sub(r"renderSlide\(\s*\d+\s*\);(\s*<\/script>)", f"renderSlide({slide_idx});\\1", content)
            if new_content != content:
                html_path.write_text(new_content, encoding="utf-8")
                print(f"  -> Mis à jour : {html_path.name} (actif: diapo {slide_num})")

    # 2. Mise à jour du metadata artifact pour forcer le rafraîchissement UI
    if BRAIN_META.exists():
        try:
            meta = json.loads(BRAIN_META.read_text(encoding="utf-8"))
            meta["client_version"] = meta.get("client_version", 1) + 1
            BRAIN_META.write_text(json.dumps(meta, indent=2), encoding="utf-8")
        except Exception:
            pass

    # 3. Mise à jour de notes_seance_03_2026-09-22.md
    if NOTES_PATH.exists():
        notes = NOTES_PATH.read_text(encoding="utf-8")

        # Remplacement dans la table ENCORA
        # Format: | **D03** | *--:--:--* | *--:--:--* | *--:--:--* | ...
        pattern_table = rf"(\|\s*\*\*D{slide_pad}\*\*\s*\|\s*)[^|]+(\|\s*)[^|]+(\|\s*)[^|]+(\|)"
        replacement_table = rf"\g<1>`{time_str}` \g<2>`{offset_rec1}` \g<3>`{offset_rec2}` \g<4>"
        notes = re.sub(pattern_table, replacement_table, notes)

        # Remplacement sous l'en-tête de section de la diapo
        # Format: ### Diapositive D03 : ...
        # *(Heure réelle : ...)*
        pattern_section = rf"(###\s*Diapositive\s*D{slide_pad}\s*:[^\n]*\n)(?:\*\([^\)]*\)\*\n)?"
        replacement_section = rf"\g<1>*(Heure réelle : {time_str} EDT | Offset S24 : {offset_rec1} | Offset S24D : {offset_rec2})*\n"
        notes = re.sub(pattern_section, replacement_section, notes)

        NOTES_PATH.write_text(notes, encoding="utf-8")
        print(f"  -> Notes mises à jour dans notes_seance_03_2026-09-22.md")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_slide.py <slide_num> [HH:MM:SS]")
        sys.exit(1)
    
    s_num = int(sys.argv[1])
    t_str = sys.argv[2] if len(sys.argv) > 2 else None
    sync_slide(s_num, t_str)
