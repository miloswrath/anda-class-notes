import numpy as np
import pandas as pd

# Create a DataFrame with sequential numbers from 0 to 24
# The DataFrame has 5 rows and 5 columns, with named indexes and column labels
df2 = pd.DataFrame(np.arange(25).reshape((5,5)),
                   index = ['California', 'Colorado', 'Nevada', 'Florida', 'Georgia'],
                   columns = ['one', 'two', 'three', 'four', 'five'])

# --- SUBSETTING ROWS (OBSERVATIONS) ---

# Extract rows where the value in column 'one' is greater than 10
df2[df2.one > 10]

# Randomly select 50% of the rows
df2.sample(frac=.5)

# Randomly select 3 rows
df2.sample(n=3)

# Select the top 2 rows with the highest values in column 'four'
df2.nlargest(2, 'four')

# Select the bottom 2 rows with the lowest values in column 'four'
df2.nsmallest(2, 'four')

# Select rows by position (rows 2 and 3, not including 4)
df2[2:4]

# Select rows by position explicitly using iloc
df2.iloc[2:4]

# Slice the first two rows
df2[:2]

# Extract rows where column 'three' has values greater than 10
df2[df2.three > 10]

# Return a boolean DataFrame where values less than 5 are True
df2 < 5

# Assign all values less than 5 to be 0
df2[df2 < 5] = 0

# Select rows between 'Nevada' and 'Florida' (inclusive)
df2['Nevada':'Florida']

# Select rows based on numerical index positions (rows 1 and 2)
df2[1:3]

# Select only row 2 but reshape as a Series
df2.iloc[2]

# --- SUBSETTING COLUMNS (VARIABLES) ---

# Select a single column (two different ways)
df2.two
df2['two']

# Select a specific column and slice specific rows
state_series = df2['two'][2:4]
state_series

# Select multiple columns by name
df2[['three', 'one']]

# Use regex to select columns whose names start with 'o'
df2.filter(regex='^o')

# Select all columns between 'two' and 'three' (inclusive) using loc
df2.loc[:, 'two':'three']

# Select columns by position using iloc (columns at index 1 and 4)
df2.iloc[:, [1, 4]]

# --- SUBSET BOTH ROWS AND COLUMNS ---

# Select row 2 and specific columns (3, 0, and 1) in that order
df2.iloc[2, [3, 0, 1]]

# Modify a specific value: Set row index 0, column index 2 ('three') to 999
df2.iloc[0,2] = 999
df2

# Slice DataFrame to include only columns 0 to 3 and rows where 'three' > 10
df2.iloc[:, :3][df2.three > 10]

# Use loc to select rows up to 'Nevada' and columns up to 'three' (inclusive)
df2.loc[:'Nevada', :'three']

# Use loc with logical condition and column selection
df2.loc[df2.two > 10, ['two', 'five']]

# Select a specific row ('Colorado') and multiple columns ['two', 'three']
df2.loc['Colorado', ['two', 'three']]


