import pandas as pd

# Creating a sample DataFrame
df = pd.DataFrame({
    'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot', 'Chicken', 'Chicken'],
    'Type': ['Wild', 'Captive', 'Wild', 'Captive', 'Wild', 'Captive'],
    'Weight': [2.0, 3.0, 0.3, 0.4, 5.0, 7.0],  # Weight in pounds
    'Max_Speed': [380.0, 370.0, 26.0, 24.0, 12.0, 10.0]  # Speed in km/h
})

# Filtering for captive animals that weigh more than 1 pound
df_captive_heavy = df[(df['Weight'] > 1) & (df['Type'] == 'Captive')]
print("Captive animals weighing more than 1 pound:\n", df_captive_heavy)

# Filtering for animals with max speed greater than 24 km/h, selecting only relevant columns
df_fast_animals = df.loc[df['Max_Speed'] > 24, ['Animal', 'Type', 'Max_Speed']]
print("\nAnimals with Max Speed greater than 24 km/h:\n", df_fast_animals)

# Counting non-null values for each column in df_fast_animals
count_non_null = df_fast_animals.count()
print("\nCount of non-null values per column in fast animals dataframe:\n", count_non_null)

# Counting observations where Weight is less than 7
count_weight_below_7 = df[df['Weight'] < 7].count()
print("\nCount of observations where Weight < 7:\n", count_weight_below_7)

# Alternative method: Counting only 'Weight' column where Weight is less than 7
count_weight_only = df.loc[df['Weight'] < 7, ['Weight']].count()
print("\nCount of observations (only 'Weight' column) where Weight < 7:\n", count_weight_only)





















