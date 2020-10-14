def outer_f():
    a = 'st'
    def inner_f():
        print(a)
    return inner_f()

outer_f()



def outer_f1():
    a = 'st'
    def inner_f1():
        print(a)
    return inner_f1

(outer_f1())()