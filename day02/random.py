import random as r

print(r.random())    # 0 ~ 1.0 미만의 랜덤한 값 출력
print(r.uniform(2, 3))    # 2.0 ~ 3.0 미만의 랜덤한 값 출력
print(r.randint(1, 100))    # 1 ~ 100 미만의 랜덤한 값 출력
print(r.randrange(10, 20, 2))    # 10 ~ 20 미만의 짝수의 랜덤한 값 출력

li = list(range(1, 10))
r.shuffle(li)    # 값을 섞움
print(li)