import os, re, csv
import requests 
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=1&acq=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C&qdt=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84'
soup = bs(ur.urlopen(url).read(), 'html.parser')
# soup

table = soup.find('h6', {'class':'blind _blind'})
print(table.text)
print()

hotkeys = soup.find_all('span', {"class":"tit"})
# hotkeys = soup.select("span.tit")
for key in hotkeys:
    print(key.text)