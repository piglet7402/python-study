def func_1():    # 입, 출력이 모두 없는 함수
    print("func1")

func_1()


def func_2(num):    # 입력만 있는 함수(출력은 없음)
    print(num * 2,'입니다')

func_2(3)


def func_3():    # 출력만 있는 함수(입력은 없음)
    return 10
result = func_3()
print(result)


def func_4(a, b):    # 입, 출력이 모두 있는 함수
    if a > b:
        return a
    else:
        return b
print(func_4(4, 7))