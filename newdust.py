import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

frame = pd.read_csv('dust-dongjak.csv',encoding='utf-8', names=['1','2','3','4','5','6','7','8'],nrows=10)
date = pd.DataFrame(frame['1'][1:],dtype='int32')
micro = pd.DataFrame(frame['7'][1:],dtype='int32')
smicro = pd.DataFrame(frame['8'][1:],dtype='int32')

print(frame[['1','7','8']])

print()

plt.plot(np.arange(9),micro)
plt.plot(np.arange(9),smicro)
plt.show()
