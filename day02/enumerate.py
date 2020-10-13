i = 0
for value in ['red', 'yellow', 'blue', 'white', 'gray']:
    print('{0}: {1}'.format(i, value))
    i += 1

# 위 아래를 비교
# enumerate 함수를 사용했을 때(리스트의 값과 순번을 함께 전달함)
for i, value in enumerate(['RED', 'YelloW', 'BLUE', 'WHite', 'grAY']):
    print('{0}: {1}'.format(i, value))



seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
z = zip(seq1, seq2)
print(z)
print(type(z))

for t in z:
	print(t, type(t))

z = zip(seq1, seq2)
for idx, (a, b) in enumerate(z):
	print('%d: %s, %s' % (idx, a, b))

d1 = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
seq1, seq2 = zip(*d1)
print(seq1)
print(seq2)