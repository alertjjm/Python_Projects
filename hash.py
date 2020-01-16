from hashlib import sha1
import random
j=0
for k in range(10000000-1,99999999+1):
    j=j+1
    ha=str(k)+"salt_for_you"
    print("process: "+str(j))
    answer=ha
    for i in range(500):
        ha=sha1(ha.encode('utf-8')).hexdigest()
    if(ha=="d5b297e3e8a4d5a24f931cf5337e357a9e166dd3"):
        break
    if(k%500==0):
        print(ha)
print(answer)