# 튜플(Tuple)

Created: Oct 23, 2020 9:55 AM
Updated: Oct 25, 2020 7:46 PM

# 튜플

- 리스트는 []으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
- 튜플은 그 값을 바꿀 수 없다.(값의 생성, 삭제, 수정)
- 단 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 함
- 요소가 2개 이상이면 마지막 콤마는 붙이지 않음

```python
t1 = ()
t2 = (1,)    # 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
t3 = (1, 2, 3)
t4 = 1, 2, 3     # 괄호( )를 생략해도 무방하다
t5 = ('a', 'b', ('ab', 'cd'))
```

### 변수를 만드는 여러 가지 방법(튜플 언패킹)

- 튜플로 a, b에 값을 대입
- 튜플은 괄호를 생략 가능

```python
a, b = ('python', 'life')
(a1, b1) = 'python', 'life'

print(a)
print(b)

print(a1)
print(b1)

================================

test = ('abcd', 'efgh', 'ijkl')
a, b, c = test

print(a)
print(b)
print(c)
```

### 인덱싱

```python
t1 = (1, 2, 'a', 'b')
print(t1[0])
```

### 슬라이싱

```python
t1 = (1, 2, 'a', 'b')
print(t1[1:])
```

### 튜플 더하기

```python
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2)
```

```python
test1 = ('abcd', 'efgh', 'ijkl')
test2 = ('mnop',)
print(id(test1))

test1 = test1 + test2
print(id(test1))
print(test1)
```

### 튜플 곱하기

```python
t2 = (3, 4)
print(t2 * 3)
```

### 튜플 길이 구하기

```python
t1 = (1, 2, 'a', 'b')
print(len(t1))
```