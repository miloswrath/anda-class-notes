import pandas as pd
import numpy as np  # Needed for generating random data

# ==========================
# CREATING DATAFRAMES (DFs)
# ==========================

# 1. Constructing an Empty DataFrame
# An empty DataFrame is useful as a placeholder when building data dynamically.
df = pd.DataFrame()
print("Empty DataFrame:\n", df)

# ----------------------------------------

# 2. Constructing a DataFrame from a Dictionary of Lists
# Each key in the dictionary becomes a column, and the lists represent row values.
data = {
    'Name': ['mary', 'joe', 'josh', 'requis', 'mcdiggle'],  # Column 'Name'
    'Age': [33, 55, 66, 12, 20]  # Column 'Age'
}
df = pd.DataFrame(data)
print("\nDataFrame from Dictionary:\n", df)

# ----------------------------------------

# 3. Constructing a DataFrame from a List of Tuples
# Each tuple represents a row, and column names are specified separately.
data = [
    ('mary', 33),
    ('joe', 55),
    ('josh', 66),
    ('requis', 12),
    ('mcdiggle', 20)
]
df = pd.DataFrame(data, columns=['name', 'age'])
print("\nDataFrame from List of Tuples:\n", df)

# ----------------------------------------

# 4. Constructing a DataFrame from a Pandas Series
# A Series is a one-dimensional labeled array; here, we convert it into a DataFrame.
series_data = {
    'Iowa': 35000,
    'Texas': 71000,
    'Oregon': 283742,
    'Utah': 28734672938  # Notice the large value
}
series1 = pd.Series(series_data)  # Creating a Series
df = pd.DataFrame(series1, columns=['Blunts Smoked per Day'])  # Converting to DataFrame
print("\nDataFrame from Series:\n", df)

# ----------------------------------------

# 5. Constructing a DataFrame from Random Integers
# Generates a DataFrame with random integers between 0 and 100.
df = pd.DataFrame(
    np.random.randint(0, 101, size=(100, 4)),  # 100 rows, 4 columns
    columns=list('ABCD')  # Column labels A, B, C, D
)
print("\nDataFrame with Random Integers:\n", df.head())  # Show first few rows

# ----------------------------------------

# 6. Constructing a DataFrame from a Normal Distribution
# Random values follow a normal distribution (mean=0, std=1).
df = pd.DataFrame(
    np.random.randn(2, 4),  # 2 rows, 4 columns
    columns=list('EFGH'),  # Column labels E, F, G, H
    index=['one', 'two']  # Custom row index, one and two for the two rows
)
print("\nDataFrame from Normal Distribution:\n", df)












