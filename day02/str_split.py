s = 'spam and ham'

t = s.split()
print(t)

t1 = s.split(' and ')    # and 를 기준으로 자름
print(t1)

s2 = ":".join(t1)
print(s2)

s3 = "one:two:three:fore:five"
print(s3.split(':', 2))    # 앞에서부터 2개만 나눔
	['one', 'two', 'three:fore:five']

print(s3.rsplit(':', 2))    # 뒤에서부터 2개만 나눔
	['one:two:three', 'fore', 'five']

name = 'hong gil dong'
a = name.split()
print(a)
b = a[1] + a[2] + '.' + a[0] + '@daum.net'
print(b)
gildong.hong@daum.net

lines = '''1st line
2nd line
3rd line
4th line
'''
print(lines.splitlines())