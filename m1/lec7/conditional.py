import pandas as pd


df = pd.DataFrame({
    'animal': ['falcon', 'falcon',
               'parrot', 'parrot',
               'chicken', 'chicken'],
    'type': ['wild', 'captive',
             'wild', 'captive',
             'wild', 'captive'],
    'weight': [2., 3., 0.3, 0.4, 5., 7.],
    'max speed': [380., 370., 26., 24., 12., 10]})


# df of captive animals that weigh more than 1 pound
df1 = df[(df['weight']>1) & (df['type']=='captive')]

#max speed > 24 only specific cols
df2 = df.loc[df['max speed']>24, ['animal', 'type', 'max speed']]

# count non null of each col
df2.count()

# count obs have weight < 7 in df
df[df['weight']<7].count()
df.loc[df.weight<7, ['weight']].count()





















