import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
# print df[0][1]
for x in df[0][1][1:]:
    print x