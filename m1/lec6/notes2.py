import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'A':['foo', 'foo', 'ooo', 'ooo', 'foo', 'bar', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
    'C': ['small', 'large', 'large', 'small', 'small', 'large', 'small', 'small', 'large'],
    'D': [1,2,2,3,3,4,5,6,7],
    'E': [2,4,5,5,6,6,8,9,9],
    })

pv_table = pd.pivot_table(df, values='E', index=['A'], columns=['C'], aggfunc='sum')

pv_table.plot(kind='bar', rot=0, figsize=(8,4), title='Pivot Table')










