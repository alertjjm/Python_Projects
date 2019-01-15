
try:
    f = open("C:\isang\iaccess.log",'r')
except IOError:
    print('파일을 찾지 못했습니다')
else:
    print('파일을 찾았습니다')
count=1
temp=f.read()
temp=temp.replace(" - - [",",")
temp=temp.replace(" -0800] ",",")
temp=temp.replace('1.1" ', '1.1",')
f = open("C:\isang\iaccesslogfile.csv",'w')
f.write('IP,Date,Action,Trash\n')
f.write(temp)
f.close()
