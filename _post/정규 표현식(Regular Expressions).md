# 정규 표현식(Regular Expressions)

Created: Oct 26, 2020 11:22 AM
Updated: Oct 26, 2020 4:12 PM

# 정규 표현식(Regular Expressions)

- 복잡한 문자열을 처리할 때 사용하는 기법
- 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용

# 정규 표현식의 기초, 메타 문자

- 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자

### 문자 클래스[]

- []사이의 문자들과 매치
- []안의 두 문자 사이에 하이픈(-)을 사용 시, 두 문자 사이의 범위(From - To)를 의미

> [a-zA-Z] : 알파벳 모두
[0-9] : 숫자

- 문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대(not)라는 의미

> [^0-9]정규 표현식 : 숫자가 아닌 문자만 매치

- **[자주 사용하는 문자 클래스]**

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled.png)

### Dot(.)

- 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨

> a.b

> a[.]b

### 반복 (*)

- 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다는 의미

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%201.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%201.png)

### 반복 (+)

- 최소 1번 이상 반복될 때 사용

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%202.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%202.png)

### 반복 ({m,n}, ?)

- 반복 횟수가 m부터 n까지 매치(m 또는 n을 생략할 수도 있음)

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%203.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%203.png)

> {1,}은 +와 동일하고, {0,}은 *와 동일

- **?** 메타문자가 의미하는 것은 {0, 1}

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%204.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%204.png)

## 정규 표현식을 지원하는 re 모듈

- 정규 표현식을 지원하기 위해 re(regular expression의 약어) 모듈을 제공
- 패턴이란 정규식을 컴파일한 결과

```python
import re
p = re.compile('ab*')   
# re.compile을 사용하여 정규 표현식(ab*)을 컴파일
# re.compile의 결과로 돌려주는 객체 p(컴파일된 패턴 객체)를 사용하여 그 이후의 작업을 수행
```

- **[컴파일된 패턴 객체]**

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%205.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%205.png)

## 컴파일 옵션

### DOTALL(S)

- `.` 이 줄바꿈 문자(\n)를 포함하여 모든 문자와 매치할 수 있도록 한다.

```python
import re
p = re.compile('a.b')

m = p.match('a\nb')
print(m)
# None
```

```python
import re
p = re.compile('a.b', re.DOTALL)

m = p.match('a\nb')
print(m)
```

### IGNORECASE(I)

- 대소문자에 관계없이 매치할 수 있도록 한다.

```python
import re
p = re.compile('[a-z]', re.I)

print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
```

### MULTILINE(M)

- ^는 문자열의 처음을 의미하고, $는 문자열의 마지막을 의미
- 정규식이 ^python인 경우 문자열의 처음은 항상 python으로 시작해야 매치
- 정규식이 python$이라면 문자열의 마지막은 항상 python으로 끝나야 매치

```python
import re
p = re.compile("^python\s\w+")  
# python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))    # 첫 번째 줄만 매치
```

- 여러줄과 매치할 수 있도록 한다. (`^`, `$` 메타문자의 사용과 관계가 있는 옵션이다)
- re.MULTILINE 또는 re.M
- ^ 메타 문자가 문자열 전체가 아닌 각 줄의 처음이라는 의미

```python
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```

### VERBOSE(X)

- verbose 모드를 사용할 수 있도록 한다.
- 정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게 된다.

```python
import re
p = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

m = p.match('python')
print(m)    # None
```

## 정규식을 이용한 문자열 검색

- 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행
- **match 객체**란 정규식의 검색 결과로 돌려주는 객체

![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%206.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%206.png)

### match

- 문자열의 처음부터 정규식과 매치되는지 조사

```python
p = re.compile(정규표현식)
m = p.match( '문자열' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
```

- 정규식에 부합

```python
import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)
# "python" 문자열은 [a-z]+ 정규식에 부합되므로 match 객체를 돌려줌
```

- 정규식에 부합하지 않음

```python
import re
p = re.compile('[a-z]+')

m = p.match("3 python")
print(m)
# 처음에 나오는 문자 3이 정규식 [a-z]+에 부합되지 않으므로 None을 돌려줌
```

### search

- 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색

```python
import re
p = re.compile('[a-z]+')

m = p.search("3 python")
print(m)
# "3 " 이후의 "python" 문자열과 매치됨
```

### findall

- 문자열의 단어를 각각 정규식과 매치해서 리스트로 돌려줌

```python
import re
p = re.compile('[a-z]+')

result = p.findall("life is too short")
print(result)
```

### finditer

- 결과로 반복 가능한 객체(iterator object)를 돌려줌
- 반복 가능한 객체가 포함하는 각각의 요소는 match 객체

```python
import re
p = re.compile('[a-z]+')

result = p.finditer("life is too short")
print(result)
# <callable_iterator object at 0x00E51EC8>

for r in result: print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>
```

### match 객체의 메서드

![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%207.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%207.png)

```python
import re
p = re.compile('[a-z]+')

m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
```

### 정규식 백슬래시 문제

- \ 문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용
- \\ 문자를 전달하려면 파이썬은 \\\\처럼 백슬래시를 4개나 사용

# 메타문자

### |

- or과 동일한 의미로 사용

```python
import re
p = re.compile('Crow|Servo')

m = p.match('CrowHello')
print(m)
```

### ^

- 문자열의 맨 처음과 일치함을 의미
- re.MULTILINE을 사용할 경우에는 여러 줄의 문자열일 때 각 줄의 처음과 일치

```python
import re
print(re.search('^Life', 'Life is too short'))
# <re.Match object; span=(0, 4), match='Life'>

m = re.search('^Life', 'My Life')
print(m)
# None
```

### $

- ^ 메타 문자와 반대의 경우
- 문자열의 끝과 매치함을 의미

```python
import re
print(re.search('short$', 'Life is too short, you need python'))
# None

m = re.search('short$', 'Life is too short')
print(m)
# <re.Match object; span=(12, 17), match='short'>
```

### \A

- 문자열의 처음과 매치됨을 의미
- ^ 메타 문자와 동일한 의미
- re.MULTILINE 옵션을 사용할 경우, 줄과 상관없이 전체 문자열의 처음하고만 매치

### \Z

- 문자열의 끝과 매치됨을 의미
- re.MULTILINE 옵션을 사용할 경우, 전체 문자열의 끝과 매치

### \b

- 단어 구분자(Word boundary)
- 보통 단어는 whitespace에 의해 구분

```python
import re
p = re.compile(r'\bclass\b')    # 앞뒤가 whitespace로 구분된 class라는 단어와 매치

m = p.search('no class at all')
print(m)

n = p.search('the declassified algorithm')
print(n)    # None
```

### \B

- \b 메타 문자와 반대의 경우
- whitespace로 구분된 단어가 아닌 경우에만 매치

```python
import re
p = re.compile(r'\Bclass\B')    # class 단어의 앞뒤에 whitespace가 하나라도 있는 경우에는 매치가 안 됨

m = p.search('no class at all')
print(m)    # None

n = p.search('the declassified algorithm')
print(n)
```

# 그루핑(Grouping)

- 문자열이 계속해서 반복되는지 조사하는 정규식
- 그룹을 만들어 주는 메타 문자는 ( )
- 그룹을 중첩되게 사용하는 것도 가능
- **[group 메서드 인덱스]**

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%208.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%208.png)

- group()

```python
import re
p = re.compile('(ABC)+')    # ABC라는 그룹이 최소 1번 이상 반복

m = p.search('ABCABCABC OK?')
print(m)
print(m.group())
```

- group(1)

```python
import re
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")  
# (문자 또는 숫자)가 최소 1번 이상 반복되는 것을 그룹으로 하고 <- 1번 그룹
# 공백부터 뒤의 숫자와 '-' 는 그룹으로 묶지 않음
# 총 그룹이 1개 뿐

m = p.search("park 010-1234-1234")
print(m.group(1))
print(m.group(2))   # 에러(IndexError: no such group)
```

- group(2)

```python
import re
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
# (문자 또는 숫자)가 최소 1번 이상 반복되는 것을 그룹으로 하고 <- 1번 그룹
# 공백 뒤의 (숫자와 '-')를 그룹으로 묶음 <- 2번 그룹
# 총 그룹이 2개

m = p.search("park 010-1234-1234")
print(m.group(1))
print(m.group(2))
```

- group(3)

```python
import re
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# (문자 또는 숫자)가 최소 1번 이상 반복되는 것을 그룹으로 하고 <- 1번 그룹
# 공백 뒤의 (숫자와 '-')를 그룹으로 묶고 <- 2번 그룹
# 2번 그룹의 숫자들 중 처음의 '-' 나오기 전까지를 그룹으로 묶음 <- 3번 그룹 
# 총 그룹이 3개

m = p.search("park 010-1234-1234")
print(m.group(1))
print(m.group(2))
print(m.group(3))
```

### 그루핑된 문자열 재참조하기

- 한 번 그루핑한 문자열을 재참조(Backreferences)할 수 있다
- 2개의 동일한 단어를 연속적으로 사용해야만 매치

```python
import re
p = re.compile(r'(\b\w+)\s+\1')

m = p.search('Paris in the the spring').group()
print(m)
```

### 그루핑된 문자열에 이름 붙이기

- 그룹을 인덱스가 아닌 이름(Named Groups)으로 참조
- (?P<그룹명>...)

```python
import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# (\w+) --> (?P<name>\w+)
# (?P<그룹명>...)

m = p.search("park 010-1234-1234")
print(m.group("name"))
```

```python
import re
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')

m = p.search('Paris in the the spring').group()
print(m)
```

## 전방 탐색(Lookahead Assertions)

```python
import re
p = re.compile(".+:")

m = p.search("http://google.com")
print(m.group())    # http:
```

### 긍정형 전방 탐색

```python
import re
p = re.compile(".+(?=:)")
# ".+:" -> ".+(?=:)"
# : 에 해당하는 문자열이 검색에는 포함되지만 검색 결과에는 제외됨

m = p.search("http://google.com")
print(m.group())    # http
```

```python
import re
p = re.compile(".*[.].*$")    # 파일명 + . + 확장자를 나타내는 정규식

x = p.search("foo.bar")
print(x.group())

y = p.search("autoexec.bat")
print(y.group())

z = p.search("sendmail.cf")
print(z.group())
```

```python
import re
p = re.compile(".*[.][^b].*$")    # 확장자가 b라는 문자로 시작하면 안 된다는 의미

# x = p.search("foo.bar")
# print(x.group())
# foo.bar라는 파일마저 걸러 낸다;;;;

# y = p.search("autoexec.bat")
# print(y.group())    # 제외됨

z = p.search("sendmail.cf")
print(z.group())
```

```python
import re
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])$")

x = p.search("foo.bar")
print(x.group())    # 제외되지 않음

# y = p.search("autoexec.bat")
# print(y.group())    # 제외됨

z = p.search("sendmail.cf")
print(z.group())    # 확장자의 문자 개수가 2개인 케이스를 포함하지 못하고 에러 발생;;
```

### 부정형 전방 탐색

- 문자열이 있는지 조사하는 과정에서 문자열이 소비되지 않음
- 판단 이후 정규식 매치가 진행

```python
import re
p = re.compile(".*[.](?!bat$).*$")  # 확장자가 bat가 아닌 경우에만 통과된다는 의미

x = p.search("foo.bar")
print(x.group())    # 제외되지 않음

# y = p.search("autoexec.bat")
# print(y.group())    # 제외됨

z = p.search("sendmail.cf")
print(z.group())    # 제외되지 않음
```

# 문자열 바꾸기

- sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 변경
- sub("바꿀 문자열", "대상 문자열")
- 바꾸기 횟수를 제어

```python
import re
p = re.compile('(blue|white|red)')

m = p.sub('colour', 'blue socks and red shoes')
# blue 또는 white 또는 red라는 문자열이 colour라는 문자열로 바뀌는 것
print(m)

n = p.sub('colour', 'blue socks and red shoes', count=1)
print(n)
```

- **[subn 메서드]**

    ![%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%209.png](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2%20%E1%84%91%E1%85%AD%E1%84%92%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8(Regular%20Expressions)%2055ccc969420d4fcd8f794e5afdb53ce8/Untitled%209.png)

### sub 메서드 사용 시 참조 구문 사용하기

```python
import re
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# (문자 또는 숫자)가 최소 1번 이상 반복되는 것을 그룹으로 하고 그룹명은 name <- 1번 그룹
# 공백 뒤의 (숫자와 '-')를 그룹으로 묶고 그룹명은 phone <- 2번 그룹
# 2번 그룹의 숫자들 중 처음의 '-' 나오기 전까지를 그룹으로 묶음. 그룹명은 없음 <- 3번 그룹 
# 총 그룹이 3개

print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# phone그룹, name그룹 순서로 출력

m = p.sub("\g<2> \g<1>", "park 010-1234-1234")
# 그룹 2번, 그룹 1번 순서로 출력
print(m)
```

### sub 메서드의 매개변수로 함수 넣기

- sub 메서드 첫 번째 매개변수로 함수를 넣을 수도 있음
- 해당 함수의 첫 번째 매개변수에는 정규식과 매치된 match 객체가 입력
- 매치되는 문자열은 함수의 반환 값으로 바뀌게 됨

```python
import re

def hexrepl(match): # match 객체를 입력으로 받아 16진수로 변환하여 돌려주는 함수
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')    # 숫자가 최소 1번 이상 반복되는 것
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
# 정규식과 매치된 match 객체 : 65490 , 49152 

print(m)
# Call 0xffd2 for printing, 0xc000 for user code.
```

# Greedy와 Non-Greedy

- * 메타 문자는 0부터 무한대로 반복되는 것
- non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용
- non-greedy는 가능한 한 가장 최소한의 반복을 수행

```python
import re
s = '<html><head><title>Title</title>'

m = len(s)
print(m)

print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
# '.' 으로 \n을 제외한 모든 문자를
# * 메타 문자로 0부터 무한대로 반복되는 것
# 매치할 수 있는 최대한의 문자열인 <html><head><title>Title</title> 문자열을 모두 소비

print(re.match('<.*?>', s).group())
# non-greedy 문자인 ?를 사용하면 *의 무한대를 제한
# 가능한 한 가장 최소한의 반복을 수행
# **?** 메타문자가 의미하는 것은 {0, 1}
```