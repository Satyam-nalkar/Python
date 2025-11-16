import pandas as pd

# Load data
df = pd.read_csv("bmw_with_missing_data.csv")

# 1. Missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2. Remove rows with missing prices
df = df.dropna(subset=['price'])

# 3. Fill missing years with most common year
most_common_year = df['year'].mode()[0]
df['year'] = df['year'].fillna(most_common_year)

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Convert price to numeric and drop invalid
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])

# 6. Average price after cleaning
average_price = df['price'].mean()
print("Average price after cleaning:", average_price)
