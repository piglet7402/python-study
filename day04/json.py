# Json 파일

li = [  {'name':'홍길동', 'kor':60, 'eng':80, 'mat':90},
        {'name':'김철수', 'kor':50, 'eng':10, 'mat':40},
        {'name':'박무기', 'kor':70, 'eng':90, 'mat':20},
      ]

import json
with open('d:/share/point.json', 'w') as f:
    json.dump(li, f, ensure_ascii=False)