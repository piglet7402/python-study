# 문자열

Created: Oct 1, 2020 9:52 AM
Updated: Oct 25, 2020 4:06 PM

# 문자열

- 문자열의 요솟값은 바꿀 수 있는 값이 아님(immutable한 자료형)
- 슬라이싱을 사용하면 문자열을 변경 가능함
- 문자열 끝에는 \t 가 생략되어 있음

### 문자열을 만드는 방법_총 4가지

```python
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
가장 깊은 밤에 더 빛나는 별빛
밤이 깊을수록 더 빛나는 별빛
"""
print(sentence3)

sentence4 = '''Life is too short, You need python'''
print(sentence4)
```

### 문자열 더해서 연결하기(Concatenation)

```python
head = "Python"
tail = " is fun!"
print(head + tail)
```

### 문자열 곱하기

```python
a = "python"
print(a * 2)
```

### 문자열 길이 구하기 - len 함수 사용

```python
a = "Life is too short"
print(len(a))
```

### 인덱싱

- 변수명[오프셋]는 문자열 안의 특정한 값을 뽑아내는 역할
- 문자열을 뒤에서부터 읽기 위해 마이너스(-) 기호를 붙이는 것
- 0과 -0은 똑같은 것이기 때문에 a[-0]은 a[0]과 똑같은 값을 보여 줌

```python
a = "Life is too short"
print(a[0])
print(a[-1])    # 뒤에서부터 첫 번째 문자는 가장 마지막 문자
```

### 슬라이싱

- 단어를 뽑아내는 방법
- 변수명[시작 오프셋:끝 오프셋]를 지정할 때 끝 번호에 해당하는 것은 포함하지 않음
- 변수명[시작 오프셋:끝 오프셋:스텝]

```python
test = "911208-1665716"

print("성별 : " + test[7])
print("년도 : " + test[0:2])    # 0번째 부터 2번째 직전까지
print("월 : " + test[2:4])    # 2번재 부터 4번째 전까지
print("일 : " + test[4:6])    # 4번째 부터 5번째 까지

print("생년월일 : " + test[:6])    # 0번째 부터 6번째 전까지

print("뒤 7자리 : " + test[7:14])
print("뒤 7자리 : " + test[7:])    # 7번째 부터 끝까지

print("뒤 7자리(뒤에서 부터) : " + test[-7:-1])
print("뒤 7자리(뒤에서 부터) : " + test[-7:])
```

```python
# -*- coding: cp949 -*- 

test = "abcdefghijklmnopqrstuvwxyz"
print(test[:])  # 처음부터 끝까지 추출
print(test[20:])    # 20번째 오프셋부터 문자열 끝까지 추출
print(test[:15])    # 처음부터 15번째 전(14) 문자열을 추출
print(test[-7:])    # 끝에서 7번째 부터 끝까지 추출
print("2칸씩 건너뛴 문자 : %s" % test[::2])

# 끝에서 부터 시작 지점순으로 출력
print(test[-1::-1])
print(test[::-1])
```

### 문자열 처리 함수

```python
python = "Python is Amazing"

print(python.lower())    # 모두 소문자로 출력
print(python.upper())    # 모두 대문자로 출력
print(python[0].isuppper())    # 0번째 글자가 대문자인지 확인

print(len(python))    # 글자 길이 출력
print(python.replace("Python", "Java"))    # 앞의 글자를 뒤의 글자로 바꿔서 출력

index = python.index("n")    # 글자 n이 어느 위치에 있는지 확인
print(index)

index = python.index("n", index + 1)    # 6번째 이후부터 글자 n이 있는 위치 
print(index)

index = python.index("Java")    # 해당 글자가 없으면 에러 발생
print(index)

print(python.find("Java"))    # index와 같은 역할을 하지만 해당 글자가 없으면 -1 리턴

print(python.count("n")    # 글자 n이 나오는 개수
```

### 문자열 포맷

```python
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

# %s는 정수, 한 문자도 잘 출력됨
print("나는 %s살 입니다." % 20)    # 오류 안남

print("나는 %s색과 %s색을 좋아합니다." % ("파랑", "주황"))
```

```python
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파랑", "주황"))

print("나는 {0}색과 {1}색을 좋아합니다.".format("파랑", "주황"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파랑", "주황"))
```

```python
print("나는 {age}살 이며, {color}색을 좋아합니다.".format(age = 20, color = "파랑"))
```

- 아래 방법은 python 3.6 버전 이상에서 가능

```python
age = 20
color = "파랑"
print(f"나는 {age}살 이며, {color}색을 좋아합니다.")
```

```python
# -*- coding: cp949 -*-    # <-- VScode에서 한글 에러 발생시 추가

age = 20
color = "파랑"
print(f"나는 {age}살 이며, {color}색을 좋아합니다.")
```

```python
# -*- coding: cp949 -*- 

age = 20
color = "파랑"
print(f"나는 {age + 1}살 이며, {color}색을 좋아합니다.")
```

### 문자 개수 세기(count)

```python
a = "hobby"
print(a.count('b'))
```

### 위치 알려주기(find , index)

- 문자열이 없으면 find는 -1을 반환
- 문자열이 없으면 index는 에러 발생

```python
a = "Python is the best choice"
print(a.find('b'))
print(a.index('t'))
```

### 문자열 삽입(join)

- 문자열 리스트를 하나의 문자열로 결합

```python
print(",".join('abcd'))    # 문자열의 각각의 문자 사이에 ','를 삽입
```

### 소문자를 대문자로 바꾸기(upper)

```python
a = "hi"
print(a.upper())
```

### 대문자를 소문자로 바꾸기(lower)

```python
a = "HI"
print(a.lower())
```

### 첫번째 단어를 대문자로 바꾸기

```python
test = "abcd efgh ijkl"
print(test.capitalize())
```

### 모든 단어의 첫글자를 대문자로 바꾸기

```python
test = "abcd efgh ijkl"
print(test.title())
```

### 대소문자 변경하기

```python
test = "AbCd Efgh IjKl"
print(test.swapcase())
```

### 왼쪽 공백 지우기(lstrip)

```python
a = "    HI    "
print(a.lstrip())
```

### 오른쪽 공백 지우기(rstrip)

```python
a = "    HI    "
print(a.rstrip())
```

### 양쪽 공백 지우기(strip)

```python
a = "    HI    "
print(a.strip())
```

### 문자열 바꾸기(replace)

- replace(바뀌게 될 문자열, 바꿀 문자열, 바꿀 횟수)
- 마지막 인수를 생략하면 모든 인스턴스를 바꿈
- 문자열 안의 특정한 값을 다른 값으로 치환

```python
a = "Life is too short"
print(a.replace("Life", "Your leg"))
```

### 문자열 나누기(split)

- split 함수는 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나눔
- 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나눔
- 나눈 값은 리스트에 하나씩 들어감

```python
a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))
```

### 검색과 선택

```python
test = "abcd efgh ijkl"
print(test.startswith('abcd'))    # 문자열 앞에 abcd로 시작하는지
print(test.endswith('ijkl'))    # 문자열 끝에 ijkl로 끝나는지
```

### 정렬 및 공백

```python
test = "AbCd"
print(test.center(30))    # 가운데 정렬
print(test.ljust(30))    # 왼쪽 정렬
print(test.rjust(30))    # 오른쪽 정렬
```

```python
print("%10s" % 'hi')    # 전체 길이가 10인 공간에 오른쪽 정렬하고 남은 공간은 공백
print("%-10sjane" % 'hi')    # 전체 길이가 10인 공간에 왼쪽 정렬을 하고 남은 공간을 공백으로한 후, 나머지 글자를 입력
```

```python
print("{0:<10}".format("hi"))    # 전체 길이가 10인 공간에 왼쪽 정렬하고 남은 공간은 공백
print("{0:>10}".format("hi"))    # 전체 길이가 10인 공간에 오른쪽 정렬하고 남은 공간은 공백
print("{0:^10}".format("hi"))    # 전체 길이가 10인 공간에 가운데 정렬하고 남은 공간은 공백
```

- 공백 채우기

```python
print("{0:=^10}".format("hi"))     # 전체 길이가 10인 공간에 가운데 정렬하고 남은 공간은 =로 채움
print("{0:!^10}".format("hi"))     # 전체 길이가 10인 공간에 가운데 정렬하고 남은 공간은 !로 채움
```

### 소수점 표현

```python
print("%0.4f" % 3.123456)    # 소수점 4번째 자리까지만 출력
print("%10.4f" % 3.123456)    # 전체 길이가 10인 공간에 소수점 4번째 자리까지만 출력하고 오른쪽 정렬
```

```python
print("{0:0.4f}".format(3.123456))    # 소수점 4번째 자리까지만 출력
print("{0:10.4f}".format(3.123456))    # 전체 길이가 10인 공간에 소수점 4번째 자리까지만 출력하고 오른쪽 정렬
```

### 탈출 문자

```python
# \n 줄 바꿈(이스케이프 코드)
print("가장 깊은 밤에 더 빛나는 별빛**\n**밤이 깊을수록 더 빛나는 별빛")

# \" 또는 \' 는 문장 안에서 따옴표를 그대로 출력
print("저는 '아미' 입니다.")
print('저는 "아미" 입니다.')
print("저는 **\"**아미\" 입니다.")

# \\ 는 문장 내에선 \ 로 출력됨
print("c:**\\**User**\\**Desktop**\\**test")

# \r 커서를 문장 맨 앞으로 이동
print("Red apple**\r**Pine")    # \r로 인해 'Red '가 'Pine'으로 덮어쓰기 됨

# \b 한글자 삭제(백 스페이스)
print("Redd\bApple")

# \t 탭 역할
print("Red\tApple")

# }} 또는 {{ 를 이용해 중괄호를 문자로 사용
print("{{ and }}".format())
```
