import pandas as pd
import numpy as np


movies = pd.DataFrame({
    'Title': ['Inception', 'The Dark Knight', 'Interstellar', 'Avengers: Endgame', 'Parasite'],
    'Year': [2010, 2008, 2014, 2019, np.nan],   
    'Genre': ['Sci-Fi', 'Action', 'Sci-Fi', 'Superhero', 'Thriller'],
    'Rating': [8.8, 9.0, 8.6, 8.4, 8.6],
    'Duration': [148, 152, 169, 181, 132]
})


print("First 3 rows:")
print(movies.head(3))


print("\nColumn names and data types:")
print(movies.dtypes)


print("\nBasic statistics:")
print(movies.describe())


print("\nMissing values in each column:")
print(movies.isnull().sum())


# 2.1
'''students = pd.DataFrame({
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva', np.nan],
    'Math_Score': [85, np.nan, 78, 92, np.nan, 88],
    'Science_Score': [90, np.nan, np.nan, 85, 95, np.nan]
})
print(students.dropna())
print()
print(students.dropna(how = 'all'))

print()

students['Math_Score'].fillna()
students['Math_Score']=students['Math_Score'].fillna(0) '''
