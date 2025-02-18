import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# create date range index
days_index = pd.date_range('01-01-2025', periods=50, freq='D')

df = pd.DataFrame({'first':np.arange(50),
                   'second':np.arange(100,150)},
                    index=days_index)

# add new column computed
df['product'] = df['first']*df['second']

# partition index into three
# specify bins=3 ~equal width

df['cut'] = pd.cut(df.index, bins=3, labels=['old', 'medium', 'new'])


'''

Bin values into discrete intervals

Use `cut` when you need to segment and sort data values into bins

The cut func is also useful for going from a continuous to categorical variable

'''

df['cut_again'] = pd.cut(df.second, bins=3, labels=['old', 'medium', 'new'])


'''

passing an interval index for bins results in those categories exactly

note that values not covered by the interval index are set to NaN

'''

bins_tuples = pd.IntervalIndex.from_tuples([(0,20),(20,30),(30,40),(40,100)])

df['bin_ages'] = pd.cut(df['first'], bins=bins_tuples)


'''

interval index from arrays, note NaNs!

'''

bins_tuples = pd.IntervalIndex.from_arrays([-1, 20, 30, 40], [20, 30, 40, 100])

df['bin_ages_arrays'] = pd.cut(df['first'], bins=bins_tuples)


# quantile based discretization function
# discretize into equal sized quantile pockets

pd.qcut(df['first'], 4, labels=['bad', 'ok', 'good', 'excellent'])











