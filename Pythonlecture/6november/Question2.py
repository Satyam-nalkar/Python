import pandas as pd
import numpy as np

'''students = pd.DataFrame({
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva', np.nan],
    'Math_Score': [85, np.nan, 78, 92, np.nan, 88],
    'Science_Score': [90, np.nan, np.nan, 85, 95, np.nan]
})


# 2.1
print("Original Dataset:")
print(students)

# 1 Remove all rows with ANY missing values
removed_any = students.dropna()
print("\n1. Rows removed if ANY value is missing:")
print(removed_any)

# 2 Remove rows ONLY if ALL values are missing
removed_all = students.dropna(how='all')
print("\n2. Rows removed only if ALL values are missing:")
print(removed_all)

# 3 Fill missing Math_Score with the average
students['Math_Score'] = students['Math_Score'].fillna(students['Math_Score'].mean())

# 4 Fill missing Science_Score with 0
students['Science_Score'] = students['Science_Score'].fillna(0)

# 5 Fill missing Name with "Unknown"
students['Name'] = students['Name'].fillna('Unknown')

print("\n Dataset after filling missing values:")
print(students)'''



#2.2
sales_data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Price': ['29.99', '15.50', '89.00'],   # Should be float
    'Quantity': ['5', '3', '7'],            # Should be int
    'Is_Weekend': ['True', 'False', 'False']  # Should be boolean
})

print(" Original Dataset:")
print(sales_data)
print("\nData Types Before Conversion:")
print(sales_data.dtypes)

# 1 Convert Price to float
sales_data['Price'] = sales_data['Price'].astype(float)

# 2 Convert Quantity to integer
sales_data['Quantity'] = sales_data['Quantity'].astype(int)

# 3 Convert Is_Weekend to boolean
sales_data['Is_Weekend'] = sales_data['Is_Weekend'].map({'True': True, 'False': False})

# 4 Convert Date to datetime
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

print("\ Cleaned Dataset:")
print(sales_data)
print("\nData Types After Conversion:")
print(sales_data.dtypes)

