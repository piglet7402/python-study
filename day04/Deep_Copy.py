import copy

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.deepcopy(x)
print(x, (id(x))
print(y, (id(y))