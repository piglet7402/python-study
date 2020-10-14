f = open('D:/share/abc.txt', 'w')    # 경로, 모드(w: 쓰기, a: 추가, r: 읽기)
for i in range(1, 11):
    f.write('{}번째\n'.format(i))
f.close()



f = open('D:/share/abc.txt', 'r')
li = f.readlines()
# print(li)
for i in li:
    print(i)
for index, i in enumerate(li):
    print('{} : {}'.format(index + 1, i), end='')
f.close()



f = open('D:/share/abc.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()



f = open('D:/share/abc.txt', 'r')
text = f.read()
print(text)
f.close()



fr = open('D:/share/abc.txt', 'r')
fw = open('D:/share/abc_bak.txt', 'w')
text = fr.read()
print(text)
fw.write(text)
fr.close()
fw.close()


# mycopy.py 파일로 생성하기
import sys
args = sys.argv[1:]
print(args, type(args))

fr = open(args[0], 'r')
fw = open(args[1], 'w')
text = fr.read()
fw.write(text)
fr.close()
fw.close()