class cal:
    # 정적 메소드 : 인스턴스(객체) 없이도 호출할 수 있는 메소드
    # ()안에 self가 자동으로 붙지 않음
    @staticmethod
    def add(a, b):
        return a + b

print(cal.add(10, 5))

a = {1, 2}
b = {3, 4, 5}
print(type(a), type(b))
print(set.union(a, b))