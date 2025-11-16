import pandas as pd

person = pd.DataFrame({
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
})

address = pd.DataFrame({
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
})


result = pd.merge(person,address,on = 'personId' ,how = 'left')
result = ['firstName','lastName','city','state']
print(result)

