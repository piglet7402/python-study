def outter(): #outter라는 함수 안에
    string = "hello"
    def inner_f(): #inner 함수를 넣었다
        print(string)
    return inner_f()

f = outter()



def outter(): #outter라는 함수 안에
    string = "hello"
    def inner_f(): #inner 함수를 넣었다
        print(string)
    return inner_f

f = outter()    # 클로져
f()


def aaa(text):
    tag = text
    def bbb(ttt):
        hhh = ttt
        print("<{0}>{1}</{0}>".format(tag, ttt))
    return bbb

f = aaa('html')
f("hello")