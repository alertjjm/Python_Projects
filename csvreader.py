import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
col_name=[]
data=pd.read_csv('C:\crawl\oil.csv',encoding='utf-8')

# The plot method on Series and DataFrame is just a simple wr

#  plot() is a convenience to plot all of the columns with labels:
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure(); df.plot();
