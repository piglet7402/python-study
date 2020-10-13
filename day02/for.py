# 0 ~ 9 출력
for a in range(10):
    print(a, end=' ')

print()
# 1 ~ 10 출력
for a in range(1, 11):
    print(a, end=' ')

print()
# 1 ~ 100까지의 짝수
for a in range(1, 101):
    if a % 2 == 0:
        print(a, end=' ')

print()
# 1 ~ 100까지의 3의 배수
for a in range(1, 101):
    if a % 3 == 0:
        print(a, end=' ')

print()
# 1 ~ 10까지의 합
sum = 0
for a in range(1, 11):
    sum = sum + a    # sum += a
print(sum)

# 1 ~ 100까지의 홀수의 합
sum = 0
for a in range(1, 101):
    if a % 2 != 0:
        sum = sum + a    # sum += a
print(sum)

'''
sum = 0
for a in range(1, 101, 2):
    sum += a
print(sum)
'''

# 두 수를 입력하여 작은 수에서 큰 수까지 출력
a = int(input('Num1 : '))
b = int(input('Num2 : '))
if a > b:
    for c in range(b, a + 1):
        print(c, end=' ')
else:
    for c in range(a, b + 1):
        print(c, end=' ')

'''
a, b = map(int, input("num1, 2 : ").split())
if a > b:    # 무조건 a를 작은수로 만들기
    a, b = b, a
for c in range(a, b + 1):
    print(c)
'''

print()
# 반복문을 중첩하여 구구단 출력
'''
for a in range(1,10):
    for b in range(1,10):
        print('{} * {} = {}'.format(a, b, a * b))
    print()

for a in range(1, 10):
    for b in range(1,10):
        print('%d * %d = %d\t' % (b, a, a * b), end='')
    print()

for a in range(1, 10):
    for b in range(1,10):
        print('{} * {} = {}\t'.format(a, b, a * b), end='')
    print()
'''