# -*- coding: utf-8 -*-
with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re

# Questions 1 to 24
missing = []
for qid in range(1, 25):
    # Anchor can be anchor_chen_q{qid}, anchor_congiu_q{qid}, anchor_bva_q{qid}, anchor_ux_q{qid}
    pattern = rf'id=[\"\']anchor_[a-z0-9_]+q{qid}[\"\']'
    m = re.findall(pattern, html)
    if not m:
        missing.append(qid)
    else:
        print(f'Q{qid}: found {m}')

if missing:
    print('❌ Missing anchors for questions:', missing)
else:
    print('✅ ALL 24 QUESTION ANCHORS VERIFIED IN index.html!')
