from urllib import parse
from selenium import webdriver
b=input('교수를 입력:')
b=parse.quote(b)
url="https://cau.everytime.kr/lecture?keyword="+str(b)
USER="아이디"#여기에 아이디 입력해얗마
PASS="비밀번호"#여기에 비밀번호 입력해야함
browser=webdriver.PhantomJS()
browser.implicitly_wait(3)
url_login="https://cau.everytime.kr/login"
browser.get(url_login)
print("로그인 페이지에 접근합니다...")
#browser.save_screenshot("naver2.png")
e=browser.find_element_by_name("userid")
e.clear()
e.send_keys(USER)
e=browser.find_element_by_name("password")
e.clear()
e.send_keys(PASS)
#browser.save_screenshot("login.png")
form=browser.find_element_by_css_selector("#container > form > p.submit > input")
form.submit()
print("로그인 버튼을 클릭합니다...")
browser.get(url)
hreflist=browser.find_elements_by_css_selector('#container > div.wrap > div > a')
print(len(hreflist))
totaldata=''
for i in range(len(hreflist)):
    browser.get(url)
    print(i+1,'번째에 접근중...',i+1,'/',len(hreflist))
    hlink='#container > div.wrap > div > a:nth-child'+'('+str(i+2)+')'
    browser.find_element_by_css_selector(hlink).click()
    k=browser.find_element_by_css_selector('#container > div.head > div > h2').text
    totaldata=totaldata+'<과목: '+str(k)+'>'+'\n'
    t=browser.find_elements_by_css_selector('#container > div.side.leftside > div.articles > article > p.text')
    for j in range(len(t)):
        totaldata=totaldata+str(j+1)+'. '+t[j].text+'\n'+'\n'
    totaldata=totaldata+'\n'+'='*200+'\n'
print(totaldata)
browser.quit()