a = [1, 2, 3]
print(a)

a.append(5)    # 뒤에 1개 추가
print(a)

a.insert(3, 4)    # 3번째에 4를 삽입
print(a)

print(a.count(2))    # 해당 값의 개수
a.reverse()    # 값을 거꾸로 출력
print(a)

a.sort()    # 정렬(오름차순)
print(a)

a.remove(3)    # 해당 값을 삭제
print(a)

a.extend([6, 7, 8])   # 뒤에 확장
print(a)
[1, 2, 4, 5, 6, 7, 8]

a.append([9, 10])   # 뒤에 1개 추가
print(a)
[1, 2, 4, 5, 6, 7, 8, [9, 10]]