import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a sample DataFrame
df = pd.DataFrame({
    'Category': ['foo', 'foo', 'ooo', 'ooo', 'foo', 'bar', 'bar', 'bar', 'bar'],
    'Group': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
    'Size': ['small', 'large', 'large', 'small', 'small', 'large', 'small', 'small', 'large'],
    'Value_1': [1, 2, 2, 3, 3, 4, 5, 6, 7],
    'Value_2': [2, 4, 5, 5, 6, 6, 8, 9, 9],
})

# Creating a pivot table with sum aggregation
pivot_table = pd.pivot_table(df, values='Value_2', index=['Category'], columns=['Size'], aggfunc='sum')

# Plotting pivot table as a bar chart
pivot_table.plot(kind='bar', rot=0, figsize=(8, 4), title='Pivot Table - Sum of Value_2 by Size')
plt.ylabel("Sum of Value_2")
plt.show()

# Creating a second dataset for animal speeds
df_animals = pd.DataFrame({
    'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot', 'Chicken', 'Chicken'],
    'Type': ['Wild', 'Captive', 'Wild', 'Captive', 'Wild', 'Captive'],
    'Max_Speed': [380., 370., 26., 24., 12., 10]
})

# Pivot table to compute mean speed per animal
df_animal_pivot = df_animals.pivot_table(index='Animal', values='Max_Speed', aggfunc='mean')
df_animal_pivot.rename(columns={'Max_Speed': 'Mean Speed'}, inplace=True)

# Plotting mean speed per animal as a bar chart
df_animal_pivot.plot(kind='bar', rot=0, figsize=(8, 4), title='Mean Speed by Animal')
plt.ylabel("Speed (km/h)")
plt.show()

# Pivot table to compute mean speed per type (Wild/Captive)
df_type_pivot = df_animals.pivot_table(index='Type', values='Max_Speed', aggfunc='mean')
df_type_pivot.rename(columns={'Max_Speed': 'Mean Speed'}, inplace=True)

# Plotting mean speed per type as a pie chart
df_type_pivot.plot(kind='pie', subplots=True, figsize=(8, 4), title='Mean Speed by Type', autopct='%1.1f%%')
plt.ylabel("")
plt.show()

# Multi-index pivot table (Animal & Type)
df_multi_pivot = df_animals.pivot_table(index=['Animal', 'Type'], values='Max_Speed', aggfunc='mean')
df_multi_pivot.rename(columns={'Max_Speed': 'Mean Speed'}, inplace=True)

# Plotting multi-index pivot as a pie chart
df_multi_pivot.plot(kind='pie', subplots=True, figsize=(8, 4), title='Mean Speed by Animal & Type', colors=['red'])
plt.ylabel("")
plt.show()

# Resetting index to convert multi-index pivot back to a flat DataFrame
df_reset = df_multi_pivot.reset_index()
print(df_reset)




















