def fivo(num):
    a = 1
    b = 1
    list_chi = []
    for i in range(num):
        c = a
        a = b
        b = c + b
        list_chi += [a]
    return list_chi


def chick(man):
    result_man = fivo(man).index(man)
    return fivo(result_man).pop()


man = int(input("몇명을 먹일 것인가?"))
man_copy = man
list_count = []
coun = 0
result_man = 0
ending = 0

if man in fivo(man):
    print(chick(man), "마리를 시키시오")
else:
    for i in range(man_copy):
        if (man - i) in fivo(man_copy):
            coun = 0
            for j in range(len(list_count)):
                coun += list_count[j]
            if man - ((man - i) + coun) >= 0:
                list_count += [man - i]
        else:
            pass
    for num in list_count:
        if num == 1:
            print(ending + 1, "마리를 시키시오")
            exit()
        else:
            ending += chick(num)

    print(ending, "마리를 시키시오")