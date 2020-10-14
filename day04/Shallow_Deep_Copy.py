import copy

a = [[1, 2, 3], "world"]
b = copy.copy(a)
print(a is b)    # id를 비교
print(a[0] is b[0])    # 값을 비교

c = copy.deepcopy(a)
print(a is c)
print(a[0] is c[0])    # False
print(a[1] is c[1])    # True




a = []
a.append([])
a.append([])
print(a)

a[0].append(1)
a[0].append(2)
a[1].append(3)
a[1].append(4)
print(a)

b = a    # 겉과 안 모두 같음
a[1].append(5)
print(a, id(a))
print(b, id(b))
print(a, id(a[0]))
print(b, id(b[0]))
print()

c = copy.copy(a)    # 얕은 복사. c = a[:] 와 같음. 겉은 같지만 안은 다름
a[1].append(6)
print(a, id(a))
print(c, id(c))
print(a, id(a[0]))
print(c, id(c[0]))
print()

d = copy.deepcopy(a)    # 깊은 복사. 겉과 안 모두 다름
a[1].append(7)
print(a, id(a))
print(d, id(d))
print(a, id(a[0]))
print(d, id(d[0]))