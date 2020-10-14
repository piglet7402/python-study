class old_car:
    pass

class new_car(old_car):
    pass

print(issubclass(new_car, old_car))



class old_car:
    def __init__(self):
        self.power = 100
    def run(self):
        print('달린다')
    def dp_power(self):
        print(self.power)

class new_car(old_car):
    pass

n1 = new_car()
n1.run()
n1.dp_power()



class old_car:
    def __init__(self):
        self.power = 100
    def run(self):
        print('달린다')
    def dp_power(self):
        print(self.power)

class new_car(old_car):
    def __init__(self):    # 생성자 함수 사용시, 부모생성자의 명시적 호출이 필요
        self.sport = 1000
        super().__init__()    # 부모 생성자 호출
    pass

n1 = new_car()
n1.run()
n1.dp_power()



class old_car:
    def __init__(self):
        self.power = 100
    def run(self):
        print('달린다')
    def dp_power(self):
        print(self.power)

class new_car(old_car):
    def __init__(self):    # 생성자 함수 사용시, 부모생성자의 명시적 호출이 필요
        self.sport = 1000
        super().__init__()    # 부모 생성자 호출
    def run(self):    # 메소드 오버라이드(부모 클래스에도 있는 것을 덮어씀)
        print('더 빨리', end=' ')
        super().run()    # 부모 클래스의 함수 호출

n1 = new_car()
n1.run()
n1.dp_power()



class sport:
    def run(self):
        print('스포츠로 달린다.')

class sedan:
    def run(self):
        print('편안하게 달린다.')

class car(sport, sedan):
    pass

suv = car()
suv.run()

print(car.mro())    # Method Resolurion Order(함수를 해결하기 위한 순서)