num1=10
num=num1
code=1
def sosu(a):
    cnt=0
    for i in range(a//2+1):
        if a%i==0:
            cnt+=1
    if cnt==1:
        return True
    else:
        return False
while True:
    for i in range(2,num+1):
        if i>=num1/num:
            code=0
            break
        if num%i==0:
            if sosu(i):
                num=int(num/i)
                break
    if code==0:
        break
print(num)

