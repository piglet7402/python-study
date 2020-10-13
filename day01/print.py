a = 1
b = 2

print('{}더하기 {}는 {}입니다.'. format(a, b, a + b))
print('{1}더하기 {0}는 {2}입니다.'. format(a, b, a + b))

print(a, end='')    # end=''으로 인하여 줄 바꿈이 안됨
print('더하기')
print('곱하기')