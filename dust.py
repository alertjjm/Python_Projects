# -*- coding: utf-8 -*-
#동작구 대기상태를 월별로 분석했습니다.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

fn='seoul air status.csv'
f=open(fn,encoding='UTF-8') #csv파일 한글 문제로 UTF-8로 인코딩
r=csv.reader(f)
hd=next(r)

date=[] #측정날짜
nitrodx=[] #이산화질소
ozone=[] #오존
carbonmono=[] #일산화탄소
sulfur=[] #아황산가스
micro=[] #미세먼지
supermicro=[] #초미세먼지

for i in r:
    if i[1]=="동작구":
        if i[2] and i[3] and i[4] and i[5] and i[6] and i[7]: #모든 데이터가 있는 경우에만
            f_d=datetime.strptime(i[0],'%Y%m%d')
            date.append(f_d)
            nitrodx.append(float(i[2]))
            ozone.append(float(i[3]))
            carbonmono.append(float(i[4]))
            sulfur.append(float(i[5]))
            micro.append(int(i[6]))
            supermicro.append(int(i[7]))

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\malgun.ttf").get_name()
rc('font', family=font_name)


fig=plt.figure(dpi=128, figsize=(10,8)) #이산화질소, 오존, 일산화탄소, 아황산가스 농도 비교
plt.title("2016.06~2017.06 동작구 이산화질소, 오존, 일산화탄소, 아황산가스 농도 비교")
plt.ylabel("단위: ppm, 노랑:이산화질소, 갈색: 오존, 초록: 일산화탄소, 보라: 아황산가스", fontsize=9)
plt.xlabel("월별", fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.plot(date, nitrodx, c='yellow')
plt.plot(date, ozone, c='brown')
plt.plot(date, carbonmono, c='green')
plt.plot(date, sulfur, c='purple')
plt.fill_between(date,carbonmono, sulfur,  facecolor='orange', alpha=0.1)

fig.autofmt_xdate()
plt.show()


#첫번째 그래프를 닫기(X) 하면 두번째 그래프 보여줌
fig2=plt.figure(dpi=128, figsize=(10,8)) #미세먼지와 초미세먼지 농도 비교
plt.title("2016.06~2017.06 동작구 미세먼지와 초미세먼지 농도 비교")
plt.ylabel("단위: ㎍/㎥, 빨강: 미세먼지, 파랑: 초미세먼지", fontsize=12)
plt.xlabel("월별", fontsize=14)
plt.plot(date, micro, c='red')
plt.plot(date, supermicro, c='blue')
plt.fill_between(date, micro, supermicro, facecolor='yellow', alpha=0.5)

fig2.autofmt_xdate()
plt.show()