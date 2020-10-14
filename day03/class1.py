class car:
    pass

bus = car()
bus.number = 10    # 인스턴스(객체) 변수
print(bus.number)



class car:
    # __slots__ = ['number', 'power']    # 나열된 2개의 속성만 허용

bus = car()
bus.number = 10
bus.power = 400
# bus.wheel = 70
print(bus.number)
print(bus.power)



class car:
    def __init__(self):
        self.aa = 10
        self.__bb = 20
    def get_bb(self):    # __로 시작하는 변수는 멤버 메소드로만 접근 가능
        print(self.__bb)

bus = car()
print(bus.aa)
print(bus.get_bb())
print(bus.bb)   # __bb의 값 확인 불가능



class car:
    def __init__(self):
        self.aa = 10
        self.__bb = 20
    def __get_bb(self):    # 비공개 메서드
        print(self.__bb)
    def get_get_bb(self):    # __get_bb() 함수
        self.__get_bb()

bus = car()
print(bus.aa)
print(bus.get_get_bb())
print(bus.get_bb())    # 비공개 메서드라 값 확인 불가
print(bus.bb)   # __bb의 값 확인 불가능



class car:
    number = []    # 클래스 변수, 모든 인스턴스(객체)가 공유
    def add_num(self, x):
        # self.number.append(x)    #아래와 같은 내용임
        car.number.append(x)

bus1 = car()
bus2 = car()
bus1.add_num(10)
print(bus1.number)

bus2.add_num(20)
print(bus2.number)
print(car.number)



class car:
    number = []    # 클래스 변수, 모든 인스턴스(객체)가 공유
    __flag = 80    # 비공개 클래스 변수
    def add_num(self, x):
        # self.number.append(x)
        car.number.append(x)
    def view_flag(self):
        print(car.__flag)

bus1 = car()
bus1.view_flag()