import sys

x = object()
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))
# 레퍼런스 값이 준다.

del x
print(sys.getrefcount(y))