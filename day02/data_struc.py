def f(t):    # 값이 복사가 됨
    t = 20
    print(id(t))
a = 10    # int형, 변경 불가능, call by value
f(a)
print(a, type(a))    # 실 매개변수
print(id(a))



def h(t):
    t = (10, 20, 30)
a = (1, 2, 3)    # 튜플, 변경 불가능
h(a)
print(a, type(a))



def g(t):
    t[0] = 0
    print(id(t))

a = [1, 2, 3]    # 리스트, 변경가능 함
g(a)    # call by reference
print(a, type(a))
print(id(a))