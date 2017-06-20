import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6, 7, 8],
             'Visitors': [34, 64, 82, 25, 93, 47, 78, 56],
             'Bounce_rate': [67, 44, 35, 63, 75, 62, 43, 62]}

df = pd.DataFrame(web_stats)


# print (df)
# print df.set_index('Day',inplace=True)
print df[['Visitors', 'Day']]
# print df.Visitors
# print df.Day.tolist()
# print np.array(df[['Visitors', 'Day']])
# df2 = pd.DataFrame(np.array(df[['Visitors', 'Day']]))
# print df2

######################################################################
