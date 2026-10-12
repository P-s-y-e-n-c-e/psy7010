# -*- coding: utf-8 -*-
import json

with open('index.html', encoding='utf-8') as f:
    html = f.read()

with open('Quiz_et_Evaluations/_pipeline/s6_master_24_questions.json', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions: {len(questions)}")
found_count = 0
missing = []

for q in questions:
    aid = q['anchor_id']
    qid = q['id']
    doc = q['doc_id']
    found = aid in html
    if found:
        found_count += 1
        print(f"Q{qid:02d} [{doc}] {aid} -> FOUND")
    else:
        missing.append((qid, doc, aid))
        print(f"Q{qid:02d} [{doc}] {aid} -> MISSING")

print(f"\nSummary: {found_count} found, {len(missing)} missing.")
