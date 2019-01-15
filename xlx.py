from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://www1.president.go.kr/petitions/95138')
bsObj=BeautifulSoup(html, "html.parser")

nameList=bsObj.findAll("div", {"class":"cspv_participant"})
title=nameList[0].find('span').text
title=title.replace(',','')
print(title)