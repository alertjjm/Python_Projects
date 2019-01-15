try:
    f = open("C:\isang\ss.txt", 'r')
except IOError:
    print("파일을 찾지 못했습니다")
else:
    print('파일을 찾았습니다')
payload=''
trash=f.readline()
header=''
totalheader=[]
totalpayload=[]
ttemp=[]
while True :
    data=f.readline()
    if not data:
        totalheader.append(header)
        header = ''
        totalpayload.append(payload)
        payload=''
        break
    if 'Payload:' in data:
        while True:
            data=f.readline()
            if '------------------------------------------------------------------------' in data:
                totalheader.append(header)
                header=''
                totalpayload.append(payload)
                payload=''
                break
            elif not data: break
            else:
                temp=data
                temp.replace('\n','')
                payload=payload+temp[48:63]

    else:
        temp1=data
        header=header+temp1
print(header)
f.close()
f=open("C:\isang\dy.txt", 'w')
i=0
for line in totalpayload:
    f.write(totalheader[i])
    i+=1
    f.write(line)
    f.write('----------\n')
f.close()