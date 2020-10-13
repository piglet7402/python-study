a = int(input("첫번째 숫자 : "))
b = int(input("두번째 숫자 : "))
c = int(input("세번째 숫자 : "))

su = a + b + c
print(su)
av = (a + b + c)/3
print(av)

def max_1(a, b, c):
    if a < b :
        if b < c :
            return c
        else:
            return b
    else:
        if a < c :
            return c
        else:
            return a
print("최대값은 %d 입니다." % max_1(a, b, c))


a1 = int(input("1번째 숫자 : "))
b1 = int(input("2번째 숫자 : "))
c1 = int(input("3번째 숫자 : "))

su1 = sum([a1, b1, c1])
print(su1)

'''
av1 = average(a1, b1, c1)
print(av1)
'''

ma = max(a1, b1, c1)
print(ma)

a, b, c = map(int, input('a b c : ').split())
su2 = a + b + c
av2 = su2 / 3.0

print('sum : {}, avg : {}'.format(su2, av2))
print('max :', max(a, b, c))