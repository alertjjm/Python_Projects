n=int(input("몇 번째 피보나치 수를 출력할까요? : "))
a=1
b=1
fivo=[1,]
for i in range(n-1):
    c=a
    a=b
    b=c+b
    fivo.append(a)
print(n,"번째까지의 피보나치 수열은 다음과 같습니다: ",fivo)
print(n,"번째 피보나치 수는 ",fivo[n-1],"입니다")