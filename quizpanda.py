from pandas import Series, DataFrame

data={
    'kor':[100,44,66,98,10],
    'eng':[11, 22, 57, 77, 100],
    'mat':[100, 35, 46, 98, 11]
}
frame=DataFrame(data, columns=['kor', 'eng', 'mat'],index=[201,44,56,78,99])
frame['total']=frame.sum(axis=1)
frame['avg']=frame['total']/5

print(frame)

