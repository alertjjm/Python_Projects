num=int(input("정수를 입력하시오: "))
def yaksu(a):
    yaklist=[]
    for i in range(1,a):
        if a%i==0:
            yaklist.append(i)
    return yaklist

def yakprint(b,c):
    str1=str(b)+"="
    for i in range(len(c)):
        str1=str1+str(c[i])+"+"
    print(str1[:-1])

for i in range(1,num+1):
    yaklist=yaksu(i)
    yaksum=0
    for j in range(len(yaklist)):
        yaksum=yaksum+yaklist[j]
    if yaksum==i:
        yakprint(i,yaklist)