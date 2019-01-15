import tkinter as tk
import tkinter.font
import random
from tkinter import messagebox

def combination():
    ii=random.randint(0,8)
    o=random.randint(0,2)
    d=random.randint(0,10)
    if d==0 or d==1:
        b=2
    else:
        b=random.randint(0,1)
    Inning=["1회","2회","3회","4회","5회","6회","7회","8회","9회"]
    Outcount=["무사","1사","2사"]
    Runningstate=[0,0,0]
    Ballstate=["플라이","땅볼",""]
    Defenseposition=["1루쪽 번트","3루쪽 번트","투수","포수","1루수","2루수","3루수","유격수","좌익수","중견수","우익수"]

    for i in range(3):
        Runningstate[i]=random.randint(0,1)

    if Runningstate[0]==1 and Runningstate[1]==0 and Runningstate[2]==0:
        run="1루"
    elif Runningstate[0]==0 and Runningstate[1]==1 and Runningstate[2]==0:
        run="2루"
    elif Runningstate[0]==0 and Runningstate[1]==0 and Runningstate[2]==1:
        run="3루"
    elif Runningstate[0]==1 and Runningstate[1]==1 and Runningstate[2]==0:
        run="1루/2루"
    elif Runningstate[0]==1 and Runningstate[1]==0 and Runningstate[2]==1:
        run="1루/3루"
    elif Runningstate[0]==0 and Runningstate[1]==1 and Runningstate[2]==1:
        run="2루/3루"
    elif Runningstate[0]==1 and Runningstate[1]==1 and Runningstate[2]==1:
        run="만루"
    elif Runningstate[0]==0 and Runningstate[1]==0 and Runningstate[2]==0:
        run="없음"
    else:
        run="주자 에러"

    baseballresult=Inning[ii]+" "+Outcount[o]+"에 주자 "+run+" "+Defenseposition[d]+" "+Ballstate[b]
    return baseballresult
combinationmessage=[combination()]
window=tk.Tk()
window.title('Daslgis')
window.geometry('1000x600')
font=tk.font.Font(family="맑은 고딕",size=20)
font2=tk.font.Font(family="맑은 고딕",size=50)
baseballtitle=tk.Label(window,text='야구 퀴즈',font=font,width=15, height=2, fg="blue", relief="raised")
baseballtitle.pack(padx=20,pady=50)
description1=tk.Label(window,text="이 야구 퀴즈는 특정한 상황이 주어지면 주자는 어떻게 행동해야 하는지, 수비는 어떻게 행동해야 하는지를 시뮬레이션 해볼 수 있는 프로그램입니다.")
description1.pack()
description2=tk.Label(window,text="정답을 입력하신 후, 제출을 하시면 txt파일에 기록이 차곡차곡쌓입니다.")
description2.pack()
description3=tk.Label(window,text="copyright by JJM")
description3.pack(side="bottom")
message=tk.Label(window, text=combinationmessage[len(combinationmessage)-1], font=font,width=40, relief="sunken",anchor="center")
message.pack(padx=40,pady=50)
e1=tk.Entry(window,width=100,xscrollcommand=True)
e1.pack(padx=10,pady=10)
def answerentry():
    text=e1.get()
    if(text==""):
        messagebox.showinfo("오류", "아무것도 입력하지 않았습니다")
    else:
        messagebox.showinfo("확인","정답이 정상적으로 제출되었습니다")
        f=open("baseball_answer.txt",'a')
        file_result=combinationmessage[len(combinationmessage)-1]+": "+text+"\n"
        f.write(file_result)
        f.close()
        e1.delete(0,"end")
def refresh():
    combinationmessage.append(combination())
    message.config(text=combinationmessage[len(combinationmessage)-1], font=font,width=100, relief="flat",anchor="center")
    e1.delete(0,"end")

submitbtn=tk.Button(window,text="정답 제출",command=answerentry)
submitbtn.pack(padx=10,pady=10)
refreshbtn=tk.Button(window,text="문제 새로고침",command=refresh)
refreshbtn.pack(padx=10,pady=10)


window.mainloop()
