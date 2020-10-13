li = []
print(li, type(li)

li = list()
print(li, type(li)

li1 = [1, 2, 3, 4, 5]
li2 = ['a', 2, 3, 'b', 5]
print(li2)

l = [1, 2, 'python']
#    0  1      2
#   -3  -2     -1
print(l[-2], l[-1], l[0], l[1], l[2])
print(l[1:3])
print(l * 2)
print(l + [3, 4, 5])
print(len(l))    # 리스트의 크기
print(2 in l)    # 리스트 안에 값이 있는지 확
del l[0]
print(l)

li3 = list(range(10))
print(li3)

li1 = [1, 2, 3, 4, 5]
li2 = ['a', 2, 3, 'b', 5]
print(li2)

li3 = list(range(10))
print(li3)

li4 = list(range(1, 10))    # start, end - 1
print(li4)

li5 = list(range(0, 100, 3))    # start, end - 1, 건너뛸 개수
print(li5)

li6 = list(range(10, 0, -1))
print(li6)

a = ['apple', 'banana', 10, 20]
print(a)
a[2] = a[2] + 90
print(a)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = [len(s) for s in strings]
print(lens)


li = []
print(li, type(li))

li = [i for i in range(10)]    # 빈 리스트에 값을 추가하는 방법
print(li, type(li))

li = [(i * 2 + 1) for i in range(10)]
print(li, type(li))

def odd(i):
    return i * 2 + 1
li = [odd(i) for i in range(10)]
print(li, type(li))

li = [i for i in range(10) if i % 2 == 1]
print(li, type(li))

# 구구단 출력
li = ['{} * {} = {}'.format(i, j, i * j) for i in range(1, 10)
                                            for j in range(1, 10)]
print(li, type(li))


# 1 ~ 100중에 3, 6, 9가 들어간 숫자 출력
odds = [i for i in range(1, 101) if '3' in str(i) or 
                                    '6' in str(i) or '9' in str(i)]
print(odds)