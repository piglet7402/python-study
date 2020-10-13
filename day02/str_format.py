f = 'name : {}, age : {}'
print(f)
print(f.format("둘리", 10))

print('name: {0}, age: {1}'.format('둘리', 10))
print('name: {1}, age: {0}'.format(30, '마이콜'))

print('{:3}의 제곱근은 {:.5}입니다.'.format(2, 2**0.5))
# 공간은 3개를 사용하지만 2만 있으므로 앞에 2개의 공란이 있음

print('{1:03}의 제곱근은 {0:.5}입니다.'.format(2**0.5, 2))
# 1번째 포맷순서에 3개의 공간을 주며 공란을 0으로 채움
# 0번째 포맷순서에 소수점을 5개 전까지만 출력

f = "name: {name}, age: {age}"
print(f.format_map({'name':'도우넛', 'age': 10 }))