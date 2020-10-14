class MyString:
    def __init__(self, s):
        self.s = s
    def __truediv__(self, other):
        return self.s.split(other)
s = MyString('Python Programmer is Good')
t = s / ' '
print(type(t))
print(t)



class car:
    def __init__(self, hp):
        self.hp = hp
    def __add__(self, other):
        if isinstance(other, car):
            return car(self.hp + other.hp)
        elif isinstance(other, int):
            return car(self.hp + other)

bmw = car(100)
print(bmw + 10)
print((bmw + 10).hp)



class car:
    def __init__(self, hp):
        self.hp = hp
    def __add__(self, other):
        if isinstance(other, car):
            return car(self.hp + other.hp)
        elif isinstance(other, int):
            return self.hp + other

bmw = car(100)
print(bmw + 10)



class car:
    def __init__(self, hp):
        self.hp = hp
    def __add__(self, other):
        if isinstance(other, car):
            return car(self.hp + other.hp)
        elif isinstance(other,f = open('D:/share/abc.txt', 'w')    # 경로, 모드(w: 쓰기, a: 추가, r: 읽기)
for i in range(1, 11):
    f.write('{}번째\t'.format(i))
f.close() int):
            return car(self.hp + other)
    def __radd__(self, other):    # +의 앞뒤의 변수를 거꾸로 순서로 집어넣음
        return self.hp + other

bmw = car(100)
print(bmw + 10)
print((bmw + 10).hp)

print(22 + bmw)