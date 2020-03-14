import requests
import time
def bring():
    btc = requests.get("https://api.bithumb.com/public/transaction_history/").json()['data'][0]
    t_date=btc["transaction_date"]
    t_type=btc["type"]
    if(t_type=="bid"):
        t_type="매수"
    else:
        t_type="매도"
    t_unit=btc['units_traded']
    t_price=btc["price"]
    print(t_type,"거래 발생!!!")
    print("시간: ",t_date)
    print(t_price,"원에 BTC",t_unit,"개가",t_type,"거래 성사되었습니댜!!")
    print("="*200)

while(True):
    bring()
    time.sleep(5)