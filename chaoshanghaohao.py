import random
money=int(input('현재 가지고 있는 예산을 설정하세요: '))
while True:
    while True:
        user=input('홀/짝을 입력하세요, 게임을 그만하고 싶으시다면 그만 을 입력해 주세요: ')
        if user=='홀' or user=='짝' or user=='그만':
            break
        else:
            print('입력 오류! (홀, 짝, 그만) 중 하나로 다시 입력해주세요!')
    if user=='그만':
        print('그만 을 입력하셨습니다... 게임을 종료합니다')
        print('최종 예산은',money,'입니다.')
        break
    while True:
        bet=int(input('배팅할 금액을 입력하세요: '))
        if bet>money:
            print('배팅 금액은 예산보다 높으면 안됩니다! 다시 입력해 주세요...')
        else:
            break
    print('주사위 1 를 굴립니다....')
    dice1=random.randint(1,6)
    print('주사위 2 를 굴립니다...')
    dice2=random.randint(1,6)
    sum=dice1+dice2
    print('주사위 2개의 합: ',sum)
    if sum%2==0:
        print('결과는 (짝)입니다!')
        result='짝'
    elif sum%2==1:
        print('결과는 (홀)입니다!')
        result='홀'
    if user==result:
        print('맞췄습니다!')
        money+=bet
    else:
        print('틀렸습니다!')
        money-=bet
    if money<=0:
        print('예산을 모두 잃었습니다... 게임을 종료합니다...')
        break
    print('예산: ', money)

