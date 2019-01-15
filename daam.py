num1=int(input())
num=num1
i=1
result=1
def is_sosu(n):
    cnt=0
    print(n,"이 소수인지 찾는 중...")
    for i in range(1,n//2+1):
        if n%i==0:
            cnt+=1
            if cnt>1:
                return False
    if cnt==1:
        return True
    else:
        return False

while i*i <=num1:
    if num%i==0:
        print(i,'로 나누어 떨어짐')
        num=int(num/i)
        if is_sosu(i) and result<i:
            result=i
        if is_sosu(num) and result<num:
            result=num
    i+=1

print('결과는:',result)