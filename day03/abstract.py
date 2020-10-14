# from 모듈(파일) import 변수, 함수, 클래스

from abc import *    # 추상 클래스를 만들때 필요한 모듈
class bone(metaclass=ABCMeta):
    @abstractmethod
    def wheel(self):
        pass

    @abstractmethod
    def body(self):
        pass

# 추상 클래스를 상속받은 클래스는 모든 함수를 오버라이드 해야 함
class car(bone):    
    def wheel(self):
        print('22인치')
    def body(self):
        print('티타늄')

bmw = car()
bmw.wheel()