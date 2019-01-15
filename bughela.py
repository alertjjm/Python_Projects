# -*- coding: utf-8 -*-
import random

response1="땡"
response2="틀렸다"
response3="아닌데?"
response4="딩동댕!"
MY_PASSWORD="my password"

def is_correct(guess,password):
    if guess==password:
        guess_correct=True
    else:
        guess_correct=False
    return guess_correct

print("안녕\n")
users_guess=input("입력해봐")

true_or_false=is_correct(users_guess,MY_PASSWORD)

while true_or_false==False:
    computer_response=random.randint(1,3)
    if computer_response==1:
        print(response1)
    elif computer_response==2:
        print(response2)
    else:
        print(response3)
    users_guess=input("\n다음은?")
    true_or_false=is_correct(users_guess,MY_PASSWORD)
print(response4)
input("\n\n\n엔터 눌러")