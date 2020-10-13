s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)    # 합집합
print(s3)

s4 = s1.intersection(s2)    # 교집합
print(s4)

s4 = s1.difference(s2)    # s1 - s2. 차집합
print(s4)

s5 = s1.symmetric_difference(s2)    # 합집합 - 교집합
print(s5)

print(s1.issuperset(s4))    # s4가 s1의 부분집합이냐?
print(s5.issuperset(s1))    # s1가 s5의 부분집합이냐?
print(s2.issubset(s3))    # s2가 s3의 부분집합이냐?