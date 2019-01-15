from selenium import webdriver
USER="chelsea2936"
PASS="sdr2936"
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

###산업보안관리
browser.get("https://cau.everytime.kr/lecture/view/1684252")
print("산업보안관리에 접근하였습니다..")
data1=[]
#과목명
data1.append("산업보안 관리 (영어A강의)")
#평점
data1.append('평점: '+browser.find_element_by_xpath('//*[@id="container"]/div[3]/div[1]/div[1]/span/span[1]').text)
t=browser.find_elements_by_css_selector('#container > div.side.leftside > div.articles > article > p.text')
#강의평
for i in range(len(t)):
    data1.append(t[i].text)

###경영과 보안
browser.get("https://cau.everytime.kr/lecture/view/954772")
print("경영과 보안에 접근하였습니다..")
data1=[]
#과목명
data1.append("경영과 보안")
#평점
data1.append('평점: '+browser.find_element_by_xpath('//*[@id="container"]/div[3]/div[1]/div[1]/span/span[1]').text)
t=browser.find_elements_by_css_selector('#container > div.side.leftside > div.articles > article > p.text')
#강의평
for i in range(len(t)):
    data1.append(t[i].text)
###
###
###



browser.quit()