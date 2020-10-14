import requests    # url 주소에 있는 내용을 요청

webpage = requests.get('https://www.naver.com')
print(webpage.text)

from bs4 import BeautifulSoup    # 웹페이지를 더 보기 쉽게
soup = BeautifulSoup(webpage.content, 'html.parser')
print(soup)

print(soup.p)    # p태그로 시작하는 것을 출력
print(soup.h1)    # h1태그로 시작하는 것을 출력
print(soup.find_all("h2"))    # h2태그로 시작하는 모든 것을 출력