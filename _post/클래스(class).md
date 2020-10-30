# 클래스(class)

Created: Oct 22, 2020 9:44 AM
Tags: Constructor, Overriding, __init__, class, object, 생성자
Updated: Oct 22, 2020 3:50 PM

# 클래스 와 객체

## 클래스

- 똑같은 무언가를 계속해서 만들어 내는 설계도면

## 객체(인스턴스)

- 클래스로 만든 피조물
- **[객체와 인스턴스의 차이]**

    클래스로 만든 객체를 인스턴스라고도 한다.
    객체와 인스턴스의 차이는 무엇일까?
    a = Cookie() 이렇게 만든 a는 객체이다.
    그리고 a 객체는 Cookie의 인스턴스이다.
    즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
    "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며
    "a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.

## 클래스 만들기

```python
class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second

a = FourCal()    # a 객체 생성
b = FourCal()    # b 객체 생성

a.setdata(4, 2)
b.setdata(3, 7)

print(a.first)    # 4
print(b.first)    # 3

id(a.first)
id(b.first)
```

- 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지
- id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수

- 함수(메서드)의 self 매개변수

![https://user-images.githubusercontent.com/25416425/46248374-8192a080-c453-11e8-8c0e-aa1e4a8f7c72.png](https://user-images.githubusercontent.com/25416425/46248374-8192a080-c453-11e8-8c0e-aa1e4a8f7c72.png)

- 함수(메서드) 호출 방법 2가지

    ```python
    a = Cook()
    Cook.add(a, 4, 2)
    # 클래스.메서드 형태로 호출하면 반드시 첫 번째 매개변수 self에 전달할 객체를 입력해야 함

    a = Cook()
    a.add(4, 2)
    # 객체.메서드 형태로 호출하면 반드시 self를 생략해야 함
    ```

## 생성자(Constructor)

- 객체에 초기값을 설정해야 할 경우
- 객체가 생성될 때 자동으로 호출되는 메서드

```python
class FourCal:
    def __init__(self, first, second):    # setdata란 이름 대신
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
```

# 상속

- 기존 클래스는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용

```python
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):    # MoreFourCal 클래스는 FourCal 클래스를 상속함
    def pow(self):
        result = self.first ** self.second
        return result
```

### 메서드 오버라이딩(Overriding, 덮어쓰기)

- 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
- 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출

```python
class SafeFourCal(FourCal):    # SafeFourCal 클래스는 FourCal 클래스를 상속
    def div(self):    # 메서드 오버라이딩
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
```

### 클래스 변수

- 클래스 안에 변수를 선언한 것
- 클래스 변수는 클래스로 만든 모든 객체에 공유됨

```python
class Family:
    lastname = "김"
	
print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)
```