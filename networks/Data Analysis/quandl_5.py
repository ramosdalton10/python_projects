import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as pyt
from  matplotlib import style
import cv2
style.use('fivethirtyeight')

api_key = 'vZ78dv-uSU8P2VijSfmB'

def state_lists():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    # print abbv
# print state_lists()
# api_key = open('quandlapikey.txt','r').read()
# print state_lists()
def data_states():
    states = state_lists()
    main_df = pd.DataFrame()
    for stat in states:
        query = ("FMAC/HPI_"+str(stat))
        df = quandl.get(query,authtoken=api_key)
        #         df = quandl.get('FMAC/HPI_OK',authtoken=api_key)
        if main_df.empty:
             main_df = df
             # print main_df
        else:
             main_df =  main_df.join(df,lsuffix='left')
    # print main_df.head()
    with open('pickle_data','wb') as f:
        pickle.dump(main_df,f)
# data_states()
with open('pickle_data','rb') as f:
    House_data = pickle.load(f)
# print House_data
House_data.plot()
pyt.legend().remove()
pyt.show()