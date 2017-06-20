import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

df = pd.read_csv('ZILL-S00013_C.csv')
df.set_index('Date',inplace=True)
print df.head()
df.to_csv('new_csv.csv')
pf = pd.read_csv('new_csv.csv',index_col=0)
pf.to_csv('new_csv2.csv',header=False)
pf = pd.read_csv('new_csv2.csv',names=['Date','Price'],index_col=0)
# print pf
print pf.head()
pf.to_html('prices.html')


