t1 = 'ABCabc123'

print(t1.isalpha())    # False
print(t1.isdigit())    # False
print(t1.isalnum())    # True
print(t1.isupper())    # False
print(t1.islower())    # False
print(t1.count('A'))
print(t1.find('B'))
print(t1.rfind('z'))
#print(t1.rindex('z'))
print(t1.replace('A', 'Z'))    # ZBCabc123

s = "i like Python"

print(s.upper())    # 모두 대문자로 변경
print(s.lower())    # 모두 소문자로 변경
print(s.swapcase())    # 대소문자 변경
print(s.capitalize())    # 문장상 맨 앞만 대문자로
print(s.title())    # 단어별 앞자리를 대문자로