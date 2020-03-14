import time
from selenium import webdriver
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()

def clipboard_input(css, user_input):
    papercliper.copy(user_input)  # input을 클립보드로 복사
    browser.find_element_by_css_selector(css).click()  # element focus 설정
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # Ctrl+V 전달
    time.sleep(1)


url="https://mail.naver.com/"
browser.get(url)
clipboard_input("#id","chelsea2936")
a=random.random()
time.sleep(a)
clipboard_input("#pw","jjm7356")

browser.find_element_by_css_selector("#log\.login").click()
browser.find_element_by_css_selector("#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault").click()
e=browser.find_element_by_css_selector("#toInput")
e.clear()
e.send_keys("warginian@naver.com")
e=browser.find_element_by_css_selector("#subject")
e.clear()
e.send_keys("yian hihi")
e=browser.find_element_by_css_selector("body")
e.clear()
e.send_keys("hello")
browser.find_element_by_css_selector("#sendBtn").click()
