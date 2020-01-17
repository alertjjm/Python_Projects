from urllib import parse
from selenium import webdriver
id="chelsea2936"
pw="sdr2936735^"
browser=webdriver.PhantomJS()
browser.implicitly_wait(3)
url_login="https://webhacking.kr/login.php"
browser.get(url_login)
print("로그인 페이지에 접근합니다...")
e=browser.find_element_by_name("id")
e.clear()
e.send_keys(id)
e=browser.find_element_by_name("pw")
e.clear()
e.send_keys(pw)
LoginBtn=browser.find_element_by_css_selector("body > div > div.main-content > div:nth-child(3) > div.panel-body > form > input")
LoginBtn.submit()
browser.implicitly_wait(3)
urlweb="https://webhacking.kr/challenge/code-4/"
browser.get(urlweb)
html=browser.page_source
idx=html.find('value="')
captcha=html[idx+7:idx+17]

nickname=browser.find_element_by_name("id")
nickname.clear()
nickname.send_keys("h")
comment=browser.find_element_by_name("cmt")
comment.clear()
comment.send_keys("h")
capt=browser.find_element_by_name("captcha")
capt.clear()
capt.send_keys(captcha)
enter=browser.find_element_by_css_selector("body > form > table > tbody > tr:nth-child(4) > td:nth-child(1) > input[type=button]").submit()
