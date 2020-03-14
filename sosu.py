def is_sosu(num):
    if(num==1):
        return False
    count=0
    i=1
    while(i*i<=num):
        if(num%i==0):
            count=count+1
        i=i+1
    if(count==1):
        return True
    else:
        return False

n=int(input("숫자:"))
j=2
max=0
while(j*j<=n):
    if(n%j==0 and is_sosu(j)):
        max=j
    j=j+1
print(max)