a = 10
b = 5
print(a, b)
temp = a
a = b
b = temp
print(a, b)


a, b = b, a
print(a, b)


a = 10
b = 5
print(a, b)
a ^= b    # a = a ^ b
b ^= a    # b = b ^ a
a ^= b    # a = a ^ b
print(a, b)