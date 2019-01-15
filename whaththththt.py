import random
def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]<list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list

def jungbok(list):
    clist=[]
    for i in range(len(list)):
        if list[i] not in clist:
            clist.append(list[i])
    return clist

alist=[]
for i in range(30):
    alist.append(random.randint(1,100)) #alist에 1~100사이 정수 30개 넣기

alist=jungbok(alist) #alist에서 중복 제거
alist=bubblesort(alist) #중복제거한 alist에서 버블정렬
print(alist)
