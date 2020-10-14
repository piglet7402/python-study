import json
with open('d:/share/point.json', 'r') as f:
    data = json.load(f)

# print(data)
for i in data:    # 리스트에서 dict 를 i에 할당
    print(i)
print('@' * 20)

for i in data:
    for k, v in i.items():
        print(k, v)
    print('#' * 20)

for i in data:
    sum = 0
    a = 0
    for k, v in i.items():
        print(k, v)
        if type(v) == str:
            continue
        elif type(v) == int:
            sum += v
            a += 1
    print('=' * 20)
    print("sum : %d" % sum)
    print("avg : {}".format(sum / a))
    print('#' * 20)

# if문 대신 isinstance를 사용할 경우
for i in data:
    sum = 0
    a = 0
    for k, v in i.items():
        print(k, v)
        if isinstance(v, int):
            sum += v
    print('=' * 20)
    print("sum : %d" % sum)
    print("avg : {}".format(sum / 3))
    print('#' * 20)