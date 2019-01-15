what=[]
for i in range(0,5):
    dk=int(input(""))
    what.append(dk)
for i in range(0,5):
    if what[i]==-1:
        index=i
if index==0 or index==1:
    if what[4]-what[3]==what[3]-what[2]:
        cha=what[4]-what[3]
        idx=1
    else:
        what[4]/what[3]
        idx=2
if index==2:
    if what[1]-what[0]==what[4]-what[3]:
        cha=what[1]-what[0]
        idx=1
    else:
        bi=what[1]/what[0]
        idx=2
else:
    if what[2]-what[1]==what[1]-what[0]:
        cha=what[2]-what[1]
        idx=1
    else:
        bi=what[2]/what[1]
        idx=2

if idx==1:
    if index==0:
        what[index]=what[index+1]-cha
    else:
        what[index]=what[index-1]+cha
    print(what)
if idx==2:
    if index==0:
        what[index]=int(what[index+1]/bi)
    else:
        what[index]=int(what[index-1]*bi)
    print(what)