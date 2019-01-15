import re

str = '127.0.0.1 - - [18/Jan/2018:23:21:44 -0800] "GET /admin/ HTTP/1.1" 200 137'
reg = re.compile(r'^([.0-9]+) - - \[(.*?)\] "(.*)" ([0-9]+) ([0-9]+)$').findall(str)
f = open('C:\isang\ixest_1.txt','w')
f.write(reg[0])
f.close()
print(reg)