import random

#BMI 계산하여 레이블을 리턴
def bmi_check(w,h):
    bmi=w/(h/100)**2
    if 25>bmi>=18.5:
        return "normal"
    elif bmi<18.5:
        return "thin"
    elif bmi>=25:
        return "fat"
#출력파일 준비
fp=open("./bmi/bmi.csv",'w',encoding='utf-8')
fp.write("height,weight,label\r\n")
#무작위 데이터 생성
cnt={"fat":0,"normal":0,"thin":0}
for i in range(20000):
    height=random.randint(120,200)
    weight=random.randint(35,80)
    label=bmi_check(weight,height)
    cnt[label]+=1
    fp.write("{0},{1},{2}\r\n".format(height,weight,label))
fp.close()
print("ok")
print(cnt)
