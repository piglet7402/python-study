def add10(a):
    return a + 10

a = add10(20)
print(a)

# Lambda 함수 (익명 함수)
add10 = lambda a : a + 10
print(add10(20))
print((lambda a : a + 10)(30))

li = ['1', '2', '3']
a = map(int, li)
a = list(a)
print(a)
print(list(map(int, li)))

li = [1, 2, 3]
def mul(x):
    return x * 10
print(list(map(mul, li)))
print(list(map(lambda x : x * 10, li)))

a = 2
def test(x):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
print(test(a))
print((lambda x : "even" if a % 2 == 0 else "odd")(a))


# 1 ~ 10까지 숫자를 리스트로 만들기
# 짝수만 even으로 출력
li = list(range(1, 11))
print(list(map(lambda x : "even" if x % 2 == 0 else x, li)))

# if ~ else문 중복하기
li = [-2, 0, 3]
print(list(map(lambda x : "음수" if x < 0 else '0' if x == 0 else "양수", li)))


# filter(함수, 리스트)
# 함수에 정의된 조건에 맞는 요소
def func(x):
    return x > 3
print(list(filter(func,[1, 2, 3, 4, 5])))
print(list(filter(lambda x : x > 3, [1, 2, 3, 4, 5])))


# reduce 함수 사용해보기
from functools import reduce
def func(x, y):
    print(x, y)
    return x + y
li = [1, 2, 3, 4, 5]
print(reduce(func, li))