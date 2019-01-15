list_kk=[["kf", "3"], "6", "dfea", "65", 12, 66, "kk", 9]

def litost(list):
    b=''
    for i in range(0,len(list)):
        if type(list[i]) == type([1]):
            for j in range(0,len(list[i])):
                b=b+str(list[i][j])+','
        else:
            b=b+str(list[i])+','
    return b[:-1]


result=litost(list_kk)
print(result)