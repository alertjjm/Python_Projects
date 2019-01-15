def idnum(bn):
    for i in range(0, n):
        if (bn[i])[7] == "1":
            print("생년월일은", str(19) + (bn[i])[0:2], "년", (bn[i])[2:4], "월", (bn[i])[4:6], "일")
            print("성별은 남성입니다.")
        elif (bn[i])[7] == "2":
            print("생년월일은", str(19) + (bn[i])[0:2], "년", (bn[i])[2:4], "월", (bn[i])[4:6], "일")
            print("성별은 여자입니다.")
        elif (bn[i])[7] == "3":
            print("생년월일은", str(20) + (bn[i])[0:2], "년", (bn[i])[2:4], "월", (bn[i])[4:6], "일")
            print("성별은 남자입니다.")
        elif (bn[i])[7] == "4":
            print("생년월일은", str(20) + (bn[i])[0:2], "년", (bn[i])[2:4], "월", (bn[i])[4:6], "일")
            print("성별은 여자입니다.")

def sorting(alist):
    length=len(alist)
    for i in range(length):
        A=alist[i][0:5]
        if A[0]=='0':
            A='1'+A
        for j in range(i+1,length):
            B=alist[j][0:5]
            if B[0]=='0':
                B='1'+B
            if int(A)<int(B):
                temp=alist[i]
                alist[i]=alist[j]
                alist[j]=temp
    return alist

list = []
n = 0
while True:
    a = input("주민등록번호를 입력하시오:")
    if a == "end":
        break
    list.append(a)
    n = n + 1
idnum(list)
maxlist=sorting(list)
print(maxlist)


