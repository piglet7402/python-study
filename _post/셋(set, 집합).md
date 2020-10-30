# 셋(set, 집합)

Created: Oct 23, 2020 11:46 AM
Updated: Oct 23, 2020 1:05 PM

# 셋(set)

- 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
- set()의 괄호 안에 리스트 또는 문자열을 입력하여 만들 수 있음
- 비어 있는 집합 자료형은 s = set()로 만들수 있음
- 중복을 허용하지 않음
- 순서가 없다(Unordered)
- 인덱싱으로 값을 얻을 수 없음 ← 순서가 없기(unordered) 때문에
- 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후 해야 함

```python
s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)
```

### 교집합

- "&" 기호를 이용
- intersection 함수를 사용해도 동일한 결과

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
```

### 합집합

- 중복해서 포함된 값은 한 개씩만 표현
- "|" 기호를 사용
- union 함수를 사용

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 | s2)
print(s1.union(s2))
```

### 차집합

- 빼기(-) 기호를 사용
- difference 함수를 사용

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))
```

### 값 1개 추가하기(add)

```python
s1 = set([1, 2, 3])
s1.add(4)
print(s1)
```

### 값 여러 개 추가하기(update)

```python
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)
```

### 특정 값 제거하기(remove)

```python
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
```