t = (1, 2, 3, 4, 5, 6)
a, *b = t
print(a, b)
# 1 [2, 3, 4, 5, 6]

*a, b = t
print(a, b)
# [1, 2, 3, 4, 5] 6

a, b, *c = t
print(a, b, c)
# 1 2 [3, 4, 5, 6]

a, *b, c = t
print(a, b, c)
# 1 [2, 3, 4, 5] 6