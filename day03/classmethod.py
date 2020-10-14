class car:
    cnt = 0
    def __init__(self):
        car.cnt += 1
    # 클래스 메소드 : 클래스와 연관 있는 메소드. ()안에 알아서 cls가 붙음
    @classmethod
    def view_cnt(cls):
        print('{}개의 인스턴스가 생성됨'.format(cls.cnt))

ob1 = car()
ob2 = car()

car.view_cnt()