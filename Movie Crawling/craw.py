import requests
from bs4 import BeautifulSoup
import re
import parser

j = 1

name = input("영화제목  입력: ")

name = parser2.par(name)
req = requests.get(name)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
tag = soup.findAll('a', attrs={'class':'go_report2'})
tag2 = soup.findAll('span', attrs={'class':'st_on'})

tag = str(tag)
tag2 = str(tag2)

p = re.search('.*(\d.\d\d).*', tag2)
p = p.group(1)

print("\n\n관람객 평점:",p)
print("")

han = re.compile('[^ ㄱ-ㅣ가-힣]+')
p = han.sub('', tag)

hana = re.compile('신고')
p = hana.sub('', p)

l = p.split("      ")

print("상위 5개 댓글")

for i in l:
    print(j,".",i)
    j+=1



