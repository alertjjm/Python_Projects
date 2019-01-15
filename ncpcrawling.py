from urllib import parse
from selenium import webdriver
import selenium
url='https://nvd.nist.gov/ncp/repository?startIndex=' #뒤에 페이지별로 0 20 40 60 80***460 480 500
browser=webdriver.PhantomJS()
browser.implicitly_wait(2)
data='Name (Version),Target,Product Category,Authority,Last Modified,Resources\n'
for i in range(0,26):
    temp=20*i
    url_temp=url+str(temp)
    browser.get(url_temp)
    print(str(i+1)+'페이지에 접속')
    for j in range(2,22):
        cssselector='''//*[@id="p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_NCPRepository_ChecklistResultListView_ResultsTable"]/tbody/tr['''+str(j)+''']/td[1]/a'''
        try:
            temp=browser.find_element_by_xpath(cssselector).text
            temp = temp.replace(',', '.')
            temp = temp.replace('\n', '')
            data += temp + ','
        except selenium.common.exceptions.NoSuchElementException:
            print(cssselector+'에서 오류가 났습니다!')

        for k in ['product','prodCategory','org','lastModified']:
            cssselector='''#p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_NCPRepository_ChecklistResultListView_ResultsTable > tbody > tr:nth-child('''+str(j)+''') > td.'''+k
            try:
                temp=browser.find_element_by_css_selector(cssselector)
                temp = temp.text
                temp = temp.replace(',', '.')
                temp = temp.replace('\n', '')
                data += temp + ','
            except selenium.common.exceptions.NoSuchElementException:
                print(cssselector + '에서 오류가 났습니다!')
        cssselector='''//*[@id="p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_NCPRepository_ChecklistResultListView_ResultsTable"]/tbody/tr['''+str(j)+''']/td[6]'''
        try:
            temp = browser.find_element_by_xpath(cssselector)
            temp1 = '<'
            temp = temp.text
            temp = temp.replace(',', '.')
            temp = temp.replace('\n', '> <')
            temp1 += temp
            data += temp1 + ','
            print(j - 1, '번째 항목 Succeed')
            data += '>\n'
        except selenium.common.exceptions.NoSuchElementException:
            print(cssselector + '에서 오류가 났습니다!')

data=data.replace(',\n','\n')
try:
    f = open("C:\crawl\crawled.csv", 'w',encoding='utf-8')
except IOError:
    print("파일을 찾지 못했습니다")
else:
    print('파일을 찾았습니다')
data=data.replace(',>','>')
f.write(data)
f.close()

