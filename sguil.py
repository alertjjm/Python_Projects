import re

try:
    f = open("C:\isang\sguillog.txt", 'r')
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
                a=48
                temp=data
                temp.replace('\n','')
                while True:
                    if temp[a]=='\n':
                        break
                    payload=payload+temp[a]
                    a=a+1


    else:
        temp1=data
        header=header+temp1
print(header)
f.close()
f=open("C:\isang\header33.txt", 'w')
f.write('----------')
for line in totalheader:
    f.write(line)
    f.write('----------')
f.close()
filename = "C:\isang\header33.txt"
fd = open(filename, 'r')
data = fd.read()
fd.close()
replace = ['Count:',
           'Seq= Ack= Off= Res= Flags=........ Win= urp= chksum=',
           "len= chksum=", 'Protocol: ', 'Seq=']
for r in replace:
    data = data.replace(r,'')

replace = [ ' Event#', " -> dport=",'\n',' -> ', 'IPVer=', ' hlen=',
    ' tos=', ' dlen=', ' ID=', ' flags=', ' offset=', ' ttl=',
    ' chksum=', ' sport=', ' Ack=', ' Off=', ' Res=',
    ' Flags=', ' Win=',' urp=', ' chksum='     ]
spliter = "----------"
for r in replace:
    data = data.replace(r,',')
i=0
data=data.replace(spliter,'\n',1)
while True:
    templine=','+totalpayload[i]
    data=data.replace(spliter,templine,1)
    i=i+1
    if i==len(totalpayload):
        break
data=data.replace(',,',',')
pat = re.compile("(\d)[.](\d*)[ ](\d{4}-\d{2}-\d{2})")
data = pat.sub("\g<1>,\g<2>,\g<3>", data)
print(data)
fd = open("C:\isang\sguilloginterpret.csv", "w")
fd.write("count,event,main_id,datetime,EventMessage,src_ip,dst_ip,ipver,hlen,tos,dlen,id,flags,offset,ttl,chksum,protocol,src_port,dst_port,protocol,dummy,seq,ack,off,res,flags,win,urp,chksum")
fd.writelines(data)
fd.close()