
# SCRIPT NOTES FROM LECTURE 3

import numpy as np
import pandas as pd
import os

# array size = 100 randint 0 < x < 800
ar = np.random.randint(0,801,size=(100))

#array min and max
ar.min()
ar.max()

#reshape to 4, 25
ar = ar.reshape((25,4))

# Compute sum of vals in column one (or second column)
ar[:, 1].sum()

# add 1000 to each value in column 15
ar[15] = ar[15]+1000

# find max of column 2
ar[:, 2].max()

# make a new columns with the sum of columns 1 and 2
new_column = ar[:,1]+ar[:,2]
ar = np.column_stack((ar, new_column))

# Print mean of new column
ar[:,-1].mean()

# assign less than 400 w -1
ar[ar < 400] = -1

# slice off first row
ar = ar[1:, :]

# slice off first two columns
ar = ar[:, 2:]

# only keep > 500
ar[ar > 500]

















