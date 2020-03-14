def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
num=int(input("1,2,3,4 중 고르시오:"))
a=input("정수 두개 입력해").split()
a[0]=int(a[0])
a[1]=int(a[1])
if(num==1):
    print(subtract(a[0],a[1]))
elif(num==2):
    print(add(a[0],a[1]))
elif(num==3):
    print(mul(a[0],a[1]))
elif(num==4):
    print(div(a[0],a[1]))
