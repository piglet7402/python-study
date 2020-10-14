from xml.etree.ElementTree import *

person = Element('person')    # <person> </person>
name = Element('name')    # <name> </name>

name.text = 'gilddong'
person.append(name)

age = Element('age')
age.text = '22'
person.append(age)

SubElement(person, 'address').text = '서울'

tel = Element('tel')
tel.text = '010-1111-2222'
person.insert(1, tel)

person.remove(tel)

person.attrib['date'] = "2020-09-17"

dump(person)    # 출력하기
ElementTree(person).write('d:/share/person.xml')    # 파일로 생성