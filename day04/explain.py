def explain(func):
    def wrapper():
        print(func.__name__, '함수시작')
        func()
        print(func.__name__, '함수종료')
    return wrapper    # explain 함수의 주소를 리턴

def view():
    print('view')
a = explain(view)    
a()



def explain(func):
    def wrapper():
        print(func.__name__, '함수시작')
        func()
        print(func.__name__, '함수종료')
    return wrapper    # explain함수의 주소를 리턴

@explain    # 데코레이터
def view():
    print('view')

view()    ''' a = explain(view)    
              a() '''