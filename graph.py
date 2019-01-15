import requests
import time
import datetime
import matplotlib.pyplot as plt
cnt=1
x_value=[]
buy_value=[]
sell_value=[]
tempredatastr=[]
while cnt<70000:
    try:
        r=requests.get('https://api.bithumb.com/public/ticker/BTC')
    except ValueError :
        print("its a value error")
    try:
        datastr=r.json()
    except ValueError :
        print("its a value error")
    print(datastr)
    buy_value.append(float(datastr['data']['buy_price']))
    sell_value.append(float(datastr['data']['sell_price']))
    timestamp=float(datastr['data']['date'])
    timestamp=int(timestamp)
    x_value.append(datetime.datetime.fromtimestamp(timestamp/1000))
    cnt=cnt+1
    time.sleep(0.2)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title("Bitcoin Price-Bithumb")
plt.plot(x_value, buy_value, 'r', label='Buy Price')
plt.plot(x_value, sell_value, 'b', label='Sell Price')
plt.legend()
plt.show()
