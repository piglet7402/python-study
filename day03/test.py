# person 클래스 생성
# 인스턴스 변수 :  이름, 나이
# person를 상속받은 content 클래스 생성
# 인스턴스 변수 : 전화번호

# container 클래스를 만듬
# 클래스 변수로 content(연락처)를 담는 빈 리스트 작성하여
# 아래의 번호를 입력하여 내용을 확인, 수정 등이 가능하도록 만들기
# 1. 생성
# 2. 수정
# 3. 조회
# 4. 삭제
# 5. 종료

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class content(person):
    def __init__(self, name, age, tel):
        super().__init__(name, age)
        self.tel = tel


class container():
    li = []
    def create(self):
        name = input("이름 : ")
        age = input("나이 :")
        tel = input("연락처 : ")
        # print(name, age, tel)
        p1 = content(name, age, tel)
        print(p1)
        result = self.li.append(p1)
        print(result)
    def modify(self):
        pass
    def view(self):
        self.li.show()
    def delete(self):

        self.li.remove()

def display_head():
    title = '연락처 프로그램'
    print('='*32)
    print(title.center(26,'='))
    print('='*32)

def display():
    print('1. 생성')
    print('2. 수정')
    print('3. 조회')
    print('4. 삭제')
    print('5. 종료')

def main():
    display_head()
    con1 = container()    # container(리스트)를 담을 그릇이 필요하여 생성
    while True:
        display()
        select = int(input("번호를 입력해 주세요 : "))
        if select == 1:
            con1.create()
        elif select == 2:
            con1.modify()
        elif select == 3:
            con1.view()
        elif select == 4:
            con1.delete()
        else:
            break

main()
