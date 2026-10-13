# -*- coding: utf-8 -*-
with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re

# Questions 1 to 24 (EN anchors)
missing_en = []
for qid in range(1, 25):
    pattern = rf'id=[\"\']anchor_[a-z0-9_]+q{qid}_en[\"\']'
    m = re.findall(pattern, html)
    if not m:
        missing_en.append(qid)
    else:
        print(f'Q{qid}_en: found {m}')

if missing_en:
    print('⚠️ Missing EN anchors for questions:', missing_en)
else:
    print('✅ ALL 24 EN QUESTION ANCHORS VERIFIED IN index.html!')
