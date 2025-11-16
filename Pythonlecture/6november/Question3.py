import pandas as pd

# Sample BMW dataset for demonstration
bmw = pd.DataFrame({
    'model': ['1 Series', '3 Series', 'X1', 'X3', '5 Series', 'X5', '3 Series'],
    'year': [2015, 2017, 2018, 2016, 2020, 2019, 2015],
    'price': [12000, 18000, 22000, 27000, 35000, 45000, 16000],
    'mileage': [55000, 42000, 38000, 30000, 25000, 20000, 60000],
    'fuelType': ['Petrol', 'Diesel', 'Diesel', 'Petrol', 'Hybrid', 'Diesel', 'Petrol'],
    'transmission': ['Manual', 'Automatic', 'Manual', 'Automatic', 'Automatic', 'Automatic', 'Manual']
})

print(" BMW Dataset:")
print(bmw)


# 1 Find all cars from 2016 or later
cars_2016 = bmw[bmw['year'] >= 2016]
print("\n1. Cars from 2016 or later:")
print(cars_2016)

# 2 Find cars with price between 15000 and 25000
mid_price = bmw[(bmw['price'] >= 15000) & (bmw['price'] <= 25000)]
print("\n2. Cars priced between 15000 and 25000:")
print(mid_price)

# 3 Find diesel cars with mileage less than 40000
diesel_low_mileage = bmw[(bmw['fuelType'] == 'Diesel') & (bmw['mileage'] < 40000)]
print("\n3. Diesel cars with mileage less than 40000:")
print(diesel_low_mileage)

# 4 Find the cheapest car for each fuel type
cheapest_per_fuel = bmw.loc[bmw.groupby('fuelType')['price'].idxmin()]
print("\n4. Cheapest car for each fuel type:")
print(cheapest_per_fuel)


# 1 Group by fuel type and find average price
avg_price_fuel = bmw.groupby('fuelType')['price'].mean()
print("\n1. Average price by fuel type:")
print(avg_price_fuel)

# 2 Group by year and count how many cars
cars_per_year = bmw.groupby('year')['model'].count()
print("\n2. Number of cars by year:")
print(cars_per_year)

# 3 Group by transmission type and find max, min, and average mileage
mileage_stats = bmw.groupby('transmission')['mileage'].agg(['max', 'min', 'mean'])
print("\n3. Mileage stats by transmission:")
print(mileage_stats)

# 4 Find the most expensive car in each model category
most_expensive_by_model = bmw.loc[bmw.groupby('model')['price'].idxmax()]
print("\n4. Most expensive car in each model category:")
print(most_expensive_by_model)