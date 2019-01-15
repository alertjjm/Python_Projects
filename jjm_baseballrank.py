from selenium import webdriver
from urllib import parse
url="http://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo"
browser=webdriver.PhantomJS()
browser.implicitly_wait(1)
browser.get(url)
print("네이버 야구 페이지에 접근합니다...")
#for j in range(12):
#    data=browser.find_elements_by_css_selector('#content > div > div > div:nth-child(3) > table > thead > tr > th:nth-child('+str(j+1)+')')
data=[]
for i in range(10):
    data.append(browser.find_element_by_css_selector('#regularTeamRecordList_table > tr:nth-child('+str(i+1)+')').text)
    data[i]=data[i].replace('\n','. ',1)
    data[i]=data[i].replace('\n',' ',1)
    data[i]=data[i].split(' ')
    data[i][0]=data[i][0].ljust(7)
for i in range(10):
    if data[i][1] in ['SK', 'LG', 'KT', 'KIA', 'NC']:
        data[i][1]=data[i][1].ljust(9)
    else:
        data[i][1]=data[i][1].ljust(7)
    for j in range(2, 11):
        data[i][j]=data[i][j].ljust(7)
    data[i][11]=' '+data[i][11]
print('등수    팀    경기수   승     패     무     승률  게임차  연속    출루율 장타율  최근 10경기')
print('--------------------------------------------------------------------------------------------')
for i in range(10):
    for j in range(12):
        print(data[i][j],end='')
    print('\n')
browser.quit()