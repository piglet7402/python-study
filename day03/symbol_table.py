g_a = 1
g_b = 'symbol'

def f():
    l_a = 2
    l_b = 'table'
    print(locals())

for i in range(3):
    g_c = 3
    g_d = 'python'
    print(locals())

f()
print(globals())