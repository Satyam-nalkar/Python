import pandas as pd


employee = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})


unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)


if len(unique_salaries) >= 2:
    result = pd.DataFrame({'SecondHighestSalary': [unique_salaries[1]]})
else:
    result = pd.DataFrame({'SecondHighestSalary': [None]})

print(result)
