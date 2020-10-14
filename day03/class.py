class car:
    def run(self):
        print("달린다.")

# 인스턴스명 = 클래스명()
# 인스턴스 = 객체
bus = car()
bus.run()
car().run()


class car:
    def run(self):
        print("달린다.")

    def fast(self):
        print("더 빨리")
        self.run()    # bus.run()과 같음

# 인스턴스명 = 클래스명()
# 인스턴스 = 객체
bus = car(50)

# bus.run()    # car().run() 와 같음
# bus.fast()

print(isinstance(bus, car))


class car:
		# maigc method, 생성자, 초기화 함수
    def __init__(self, hd_size, pw):    # 인스턴스(객체) 생성시 자동으로 호출되는 함수
        self.handle = hd_size   # 인스턴스 변수
        self.power = pw
    def display(self):
        print('handle_size : ' + str(self.handle))
        print('마력 : ' + str(self.power))

    def run(self):
        print("달린다.")
    def fast(self):
        print("더 빨리")
        self.run()    # bus.run()과 같음

# 인스턴스명 = 클래스명()
# 인스턴스 = 객체
bus = car(50, 500)
taxi = car(30, 300)

# print(bus.handle, bus.power)
# print(taxi.handle, taxi.power)

bus.display()
taxi.display()


# 리스트를 사용
class car:
    def __init__(self, *aabb):    # 인스턴스(객체) 생성시 자동으로 호출되는 함수
        self.handle = aabb[0]   # 인스턴스 변수
        self.power = aabb[1]
    def display(self):
        print('handle_size : ' + str(self.handle))
        print('마력 : ' + str(self.power))

    def run(self):
        print("달린다.")
    def fast(self):
        print("더 빨리")
        self.run()    # bus.run()과 같음

# 인스턴스명 = 클래스명()
# 인스턴스 = 객체
bus = car(50, 500)
taxi = car(30, 300)

li = ['20', '600']
sport = car(*li)

bus.display()
taxi.display()
sport.display()


# dict(사전)을 사용
# dict(사전)인수는 함수의 인수 중에 제일 마지막에 있어야 함
# dict가 마지막에 있어야 스택의 가장 밑(맨 처음에 들어감)에 위치 함
class car:
    def __init__(self, **aabb):    # 인스턴스(객체) 생성시 자동으로 호출되는 함수
        self.handle = aabb['a']   # 인스턴스 변수
        self.power = aabb['b']
    def display(self):
        print('handle_size : ' + str(self.handle))
        print('마력 : ' + str(self.power))

    def run(self):
        print("달린다.")
    def fast(self):
        print("더 빨리")
        self.run()    # bus.run()과 같음

# 인스턴스명 = 클래스명()
# 인스턴스 = 객체

dd = dict(a = 10, b = 20)
print(dd)

mini = car(**dd)
mini.display()