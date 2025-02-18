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

df = pd.DataFrame({
    'animal': ['falcon', 'falcon',
               'parrot', 'parrot',
               'chicken', 'chicken'],
    'type': ['wild', 'captive',
             'wild', 'captive',
             'wild', 'captive'],
    'max speed': [380., 370., 26., 24., 12., 10]})


# Group by column aggfunc mean
df_pivot = df.pivot_table(index='animal', values='max speed', aggfunc='mean')
df_pivot = df_pivot.rename(columns={'max speed':'mean speed'})
df_pivot.plot(kind='bar', rot=0, figsize=(8,4), title='Mean speed by animal')

df_pivot = df.pivot_table(index='type', values='max speed', aggfunc='mean')
df_pivot = df_pivot.rename(columns={'max speed':'mean speed'})
df_pivot.plot(kind='pie', subplots=True, figsize=(8,4), title='Mean speed by animal')

# use multi index
df_pivot = df.pivot_table(index=['animal', 'type'], values='max speed', aggfunc='mean')
df_pivot = df_pivot.rename(columns={'max speed':'mean speed'})
df_pivot.plot(kind='pie', subplots=True, figsize=(8,4), title='Mean speed by animal', color=['red'])

# reverse pivot, make index go into columns
df_pivot.reset_index()




















