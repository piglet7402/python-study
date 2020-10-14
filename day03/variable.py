x = 10    # 전역변수
def f1():
    print(x)

f1()
print(x)

def f2():
    y = 10  # 지역변수
    print(y)

f2()
print(y)



x = 10    # 전역변수
def f1():
    x = 20    # 지역변수
    print(x)

f1()
print(x)



x = 10    # 전역변수
def f1():
    global x    # 지역변수를 전역변수로 선언
    x = 20    # 지역변수
    print(x)

f1()
print(x)



def f1():
    global x
    x = 20    # 지역변수
    print(x)

f1()
print(x)



def f1():
    x = 20
    # print(x)
    print(locals())

f1()
print(locals())    # 현재 위치에서는 전역변수를 출력하는 상황



def adding():
    w = 2
    b = 1
    tot = 0
    def addition(x):
        nonlocal tot    # 해당 변수에서 가장 가까운 변수를 사용
        tot = tot + x * w + b
        print(tot)
    return addition
cal = adding()
cal(1)
cal(2)