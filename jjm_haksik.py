from selenium import webdriver
from urllib import parse
url="https://bds.bablabs.com/restaurants?campus_id=biV2tiK41v"
browser=webdriver.PhantomJS()
browser.implicitly_wait(1)
browser.get(url)
print("밥대생 페이지에 접근합니다...")
totaldata=''
for k in range(6):
    menu=browser.find_element_by_css_selector("body > main > div > div.row.justify-content-center.bab-store-content-row > div > div:nth-child("+str(k+2)+") > div.card-body.store-card-main-body.store-card-main-body-list > div:nth-child(1) > div > a > h4").text
    totaldata=totaldata +'<'+menu+'>'+'\n'
    menu1=browser.find_elements_by_css_selector("body > main > div > div.row.justify-content-center.bab-store-content-row > div > div:nth-child("+str(k+2)+") > div.card-body.store-card-menu-body > div > ul")
    for i in menu1:
        totaldata=totaldata+i.text+'\n'
    totaldata=totaldata+'='*110+'\n'
print(totaldata)
browser.quit()