import xml.etree.ElementTree as EE

f = EE.parse('d:/share/person.xml')    # xml파일 읽어오기
top = f.getroot()
print(top)
print(top.tag)

for i in top:
    print(i.tag, i.text)