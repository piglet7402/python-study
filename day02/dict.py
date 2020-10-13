d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

print(d['basketball'])    # key 값을 통해 value 를 찾음(value 를 통해 찾을 순 없음)
d['volleyball'] = 6    # key, value 를 추가
print(d)

print(len(d))    # 길이 확인
print('soccer' in d)
print('volleyball' not in d)

d = dict()
print(d, type(d))

d = dict(one=1, two=2) # keyword arguments
print(d)

d = dict([('one', 1), ('two', 2)]) # tuple list
print(d)

keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)



d = {}
d = dict(a = 1, b = 2, c = 3, d = 4)
print(d)

d.setdefault('f', 5)    # key:value값 추가
print(d)

d['g'] = 6    # key:value값 추가
print(d)

d.update(a = 100)    # 해당 key의 value값 변경
print(d)

d.pop('a')
print(d)

key1 = d.keys()
print(key1)
print(type(key1))
for key in key1:
 print('{0}:{1}'.format(key, d[key]))

values = d.values()
print(values)
print(type(values))

items = d.items()
print(items)
print(type(items))

d.clear()
print(d)


strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s: len(s) for s in strings}    # 문자열과 문자열 길이를 함께 저장
print(dicts)