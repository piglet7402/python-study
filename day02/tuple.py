t = (1, 2, 3)
print(t, type(t))

t = 1, 2, 'python'    # 소괄호를 생략한 형태도 가능
print(t, type(t))

print(t[:])    # print(t)와 같음
print(t * 2)
print(t + (3, 4, 5))    # 출력할 때 1번만 붙여줌
print(len(t))
print(5 in t)