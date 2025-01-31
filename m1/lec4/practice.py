import seaborn as sns
import pandas as pd

# Load Titanic dataset
df = sns.load_dataset("titanic")

# --- SUBSETTING ROWS (OBSERVATIONS) ---

# 1. Extract passengers who paid a fare greater than $50.


# 2. Randomly select 10% of the passengers.


# 3. Randomly select 5 passengers from the dataset.


# 4. Find the top 3 passengers who paid the highest fare.


# 5. Find the bottom 3 passengers with the lowest fare.


# 6. Select only passengers in rows 10 to 20 using positional indexing (iloc).


# 7. Extract all passengers aged above 60.


# 8. Find all passengers who embarked from 'Southampton' (embark_town) and had a fare above $100.


# 9. Replace all missing age values with 0.


# 10. Print passengers from index positions 5 to 15.


# 11. Select and print rows corresponding to passengers with index labels between 100 and 110.


# 12. Extract all passengers who were in first-class (class column).


# --- SUBSETTING COLUMNS (VARIABLES) ---

# 13. Extract the 'age' column in two different ways.


# 14. Extract the 'age' column and only include passengers between rows 50 and 100.


# 15. Select multiple columns: 'age', 'fare', and 'class'.


# 16. Use regex to select all columns starting with 'p' (e.g., 'pclass', 'parch').


# 17. Select all columns between 'embarked' and 'fare' (inclusive).


# 18. Select the columns at index positions 2 and 5 using iloc.


# 19. Find passengers older than 50 and extract only the 'age' and 'fare' columns.


# --- SUBSETTING BOTH ROWS AND COLUMNS ---

# 20. Retrieve row 15 and columns 'age', 'fare', and 'sex' (in that order).


# 21. Change the value at row index 0, column 'fare' to 999.


# 22. Extract all rows where 'fare' is greater than $100, but only return the 'fare' and 'class' columns.


# 23. Select all passengers up to index 50, but only include the 'sex' and 'age' columns.


# 24. Find all passengers in 'first class' who survived and extract 'age', 'sex', and 'fare'.


# 25. Extract all male passengers in third class and return only their 'age' and 'fare'.


