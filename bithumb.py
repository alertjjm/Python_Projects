import requests
import time
import datetime
import pandas as pd
cnt=1
f=open('C:\isang\\bithumb.csv','w')
tempredatastr=[]
f.write("buy, sell\n")
while cnt<10000:
    r=requests.get('https://api.bithumb.com/public/ticker/BTC')
    datastr=r.json()
    print(datastr)
    f.write(datastr['data']['buy_price'])
    f.write(',')
    f.write(datastr['data']['sell_price'])
    f.write("\n")
    cnt=cnt+1
    time.sleep(0.1)
    timestamp=int(datastr['data']['date'])
    print(datetime.datetime.fromtimestamp(timestamp/1000))
f.close()
