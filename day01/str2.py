a = 10
b = 20
print(a, b)
print(str(a) + str(b))
print('{} + {}'.format(a, b))
print('%d + %d = %d' % (a, b, a + b))
print('{} + %d = {}'.format(a, a + b) % b)


a = "plus"
b = "total"
print("{} + %(aa)d = {} %(bb)d".format(a, b) % {'aa' : 10, 'bb' : 20})