def fivo_func(num):
    a = 1
    b = 1
    fivo = [1,]
    while True:
        c = a
        a = b
        b = c + b
        fivo.append(a)
        if a>=num:
            break
    return fivo
def fivonachicken(num):
    temp = []
    result = 0
    if num in fivo_func(num):
        result = fivo_func(num)[(fivo_func(num).index(num)) - 1]
        return result
    else:
        for i in range(num):
            if (num - i) in fivo_func(num):
                sum=0
                for element in temp:
                    sum+=element
                if num >= ((num - i) + sum):
                    temp.append(num - i)
            else:
                pass
        for i in temp:
            result += fivo_func(i)[(fivo_func(i).index(i) - 1)]
    return result

man = int(input("자애로운 자여, 몇명이나 먹이려고 하는고? "))
print(fivonachicken(man))