# 딕셔너리(dict)

Created: Oct 23, 2020 10:32 AM
Updated: Oct 23, 2020 11:46 AM

# 딕셔너리

- 대응 관계를 나타낼 수 있는 자료형
- Key와 Value를 한 쌍으로 갖는 자료형
- 연관 배열(Associative array) 또는 해시(Hash)라고 함
- 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻음
- Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있음
- 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분
- Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있음

### 딕셔너리 쌍 추가

```python
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
a[3] = [1,2,3]
print(a)
```

### 딕셔너리 요소 삭제

- del 함수를 사용해서 del 변수명[key]처럼 입력
- 지정한 Key에 해당하는 {key : value} 쌍이 삭제

```python
a = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
del a[1]
print(a)
```

### Key 사용해 Value 얻기

- 요솟값을 얻고자 할 때 Key를 사용해서 Value를 구하는 방법
- 어떤 Key의 Value를 얻기 위해서는 변수명[Key]를 사용
- Key는 고유한 값(변하지 않는 값)
- Key에 리스트는 쓸 수 없다(리스트는 변경 가능한 자료형)
- 튜플은 Key로 쓸 수 있다(튜플은 변경이 불가능한 자료형)
- 존재하지 않는 키로 값을 가져오려고 할 경우, 에러 발생

```python
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])
```

```python
a = {1:'a', 2:'b'}
print(a[1])
# 딕셔너리 변수에서 [ ] 안의 숫자 1은 두 번째 요소를 뜻하는 것이 아니라 Key에 해당하는 1을 나타냄
```

- 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨

```python
a = {1:'a', 1:'b'}
print(a)
```

### Key 리스트 만들기(keys)

- 딕셔너리의 Key만을 모아서 dict_keys 객체를 돌려줌
- 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없음

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)
```

- 버전별 차이

    ![%E1%84%83%E1%85%B5%E1%86%A8%E1%84%89%E1%85%A7%E1%84%82%E1%85%A5%E1%84%85%E1%85%B5(dict)%2010c3b034551f4af596465274e379b239/Untitled.png](%E1%84%83%E1%85%B5%E1%86%A8%E1%84%89%E1%85%A7%E1%84%82%E1%85%A5%E1%84%85%E1%85%B5(dict)%2010c3b034551f4af596465274e379b239/Untitled.png)

### Value 리스트 만들기(values)

- 딕셔너리의 Value만을 모아서 dict_values 객체를 돌려줌

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.values())

for k in a.values():
    print(k)
```

### Key, Value 쌍 얻기(items)

- items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려줌
- 리스트를 사용하는 것과 동일하게 사용 가능

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.items())
```

### Key: Value 쌍 모두 지우기(clear)

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.clear()
print(a)
```

### Key로 Value얻기(get)

- get(x) 함수는 x라는 Key에 대응되는 Value를 돌려줌

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
```

- 존재하지 않는 키로 값을 가져오려고 할 경우, None을 리턴
- 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때 사용

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('foo'))
print(a.get('foo', 'bar'))    # bar라는 default값 설정
```

### 해당 Key가 딕셔너리 안에 있는지 조사하기(in)

- 딕셔너리 안에 있으면 True, 없으면 False 반환

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)
```