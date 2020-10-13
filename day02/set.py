a = {1, 2, 3}

print(a, type(a))
print(len(a))
print(2 in a)
print(2 not in a)

s = {}    # 리스트처럼li = [] 가 되지 않음. 우선순위가 dict보다 낮음
print(type(s))
# <class 'dict'>

s1 = set()
print(type(s1))
# <class 'set'>

s = {1, 2, 3}

s.add(4)    
print(s)

s.add(1)
print(s)

s.discard(2)
print(s)

s.remove(3)
print(s)

s.update({2, 3})
print(s)

s.clear()
print(s)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = {len(s) for s in strings}    # 자료형 set은 중복을 제거함
print(lens)