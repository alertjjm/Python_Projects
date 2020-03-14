import os
import sys
from datetime import datetime
from selenium import webdriver
import time


if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    browser = webdriver.Chrome(chromedriver_path)
else:
    browser = webdriver.Chrome()

browser.get("https://coronaboard.kr/")
result=browser.find_element_by_css_selector("body > div.top.container").text
result=result.split("\n")
print(result)
result_world=result[0]+"-\n\n"
result_world=result_world+result[3]+": "+result[1]+result[2]+"\n"
result_world=result_world+result[6]+": "+result[4]+result[5]+"\n"
result_world=result_world+result[9]+": "+result[7]+result[8]+"\n"
result_world=result_world+result[11]+": "+result[10]+"\n"
result_world=result_world+result[14]+": "+result[12]+result[13]+"\n"


result_han=result[15]+"-\n\n"
result_han=result_han+result[18]+": "+result[16]+result[17]+"\n"
result_han=result_han+result[21]+": "+result[19]+result[20]+"\n"
result_han=result_han+result[24]+": "+result[22]+result[23]+"\n"
result_han=result_han+result[26]+": "+result[25]+"\n"
result_han=result_han+result[29]+": "+result[27]+result[28]+"\n"
result_han=result_han+result[32]+": "+result[30]+result[31]+"\n"
result_han=result_han+result[35]+": "+result[33]+result[34]+"\n"

result=result_world+"////////////"+"\n"+result_han
result=result.replace("*","")
print(result)










url='''http://atc.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=top&dum=dum&'''
url2='''http://atc.airforce.mil.kr:8081/user/emailPicViewSameMembers.action?siteId=last2&searchName=%EB%B0%B0%EC%88%9C%EA%B7%9C&searchBirth=19971222'''
url3='''http://atc.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=top&dum=dum&command2=writeEmail&searchCate=&searchVal=&page=1'''

browser.implicitly_wait(2)

browser.get(url)
print("인터넷 편지 쓰기 사이트로 이동...")

e=browser.find_element_by_id('searchName')
e.clear()
e.send_keys('배순규')
e=browser.find_element_by_id('birthYear')
e.clear()
e.send_keys('1997')
e=browser.find_element_by_id('birthMonth')
e.clear()
e.send_keys('12')
e=browser.find_element_by_id('birthDay')
e.clear()
e.send_keys('22')
e=browser.find_element_by_id('btnNext')
e.click()
browser.implicitly_wait(5)
browser.switch_to.window(browser.window_handles[1])

e=browser.find_element_by_css_selector('#emailPic-container > ul > li > input')
e.click()

browser.implicitly_wait(3)
browser.switch_to.window(browser.window_handles[0])

e=browser.find_element_by_id("btnNext")
e.click()

browser.get(url3)
time.sleep(1)
browser.find_element_by_css_selector("#emailPic-container > form > div.UIview > table > tbody > tr:nth-child(3) > td > div:nth-child(1) > span > input").click()
time.sleep(1)
browser.switch_to.window(browser.window_handles[1])
e=browser.find_element_by_css_selector("#keyword")
e.clear()
e.send_keys("신도림로 87")
time.sleep(1)
e=browser.find_element_by_css_selector("#searchContentBox > fieldset > span > input[type=button]:nth-child(2)").click()
time.sleep(1)
e=browser.find_element_by_css_selector("#roadAddrDiv1 > b").click()
e=browser.find_element_by_css_selector("#rtAddrDetail")
e.clear()
e.send_keys("111-2403")
e=browser.find_element_by_css_selector("#resultData > div > a").click()


browser.switch_to.window(browser.window_handles[0])

e=browser.find_element_by_id('senderName')
e.clear()
e.send_keys('종민봇py')
e=browser.find_element_by_id('relationship')
e.clear()
e.send_keys('program')
now=datetime.now()
t=''
t=t+str(now.year)+str(now.month)+str(now.day)+"."+str(now.hour)+":"+str(now.minute)
e=browser.find_element_by_id('title')
e.clear()
e.send_keys(t)
e=browser.find_element_by_id("contents")
e.clear()
e.send_keys(result)
e=browser.find_element_by_id('password')
e.clear()
e.send_keys("2424")
e=browser.find_element_by_css_selector("#emailPic-container > form > div.UIbtn > span.wizBtn.large.Ngray.submit > input")
e.click()
time.sleep(1)
browser.find_element_by_css_selector("#emailPic-container > div > div > div.messageBtn > span > input[type=button]").click()
browser.close()