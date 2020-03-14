import random
import time
random.seed()
n = random.randint(1, 50)
print("게임을 시작합니다.")
count=0
while True:
    count=count+1
    if count==6:
        print("fail")
        print("정답은 ",n,"이었습니다")
        break
    user_n=int(input(str(count)+"번째 기회입니다. 숫자를 말해주세요: "))
    if n==user_n:
        print("CORRECT")
        print("고생하셨습니다. 게임이 종료됩니다.")
        break
    elif n>user_n:
        print("up")
    elif n<user_n:
        print("down")
