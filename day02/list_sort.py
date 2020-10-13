l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)    # 내림차순으로 정렬
print(l)


l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key=str)    # 문자로 인식하여 첫번째 수를 기반으로 정렬
print(l)

l.sort(key=int)
print(l)