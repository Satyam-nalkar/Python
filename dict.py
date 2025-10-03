employee = {
   "name": "Alice",
   "age": 30,
   "city": "New York",
   "occupation": "Engineer"
}


print(employee.keys())  



print(employee.values())  



print(employee.items())  



print(employee.get("city"))  


employee.update({"age": 31})
print(employee["age"])  


removed = employee.pop("occupation")
print(removed)      
print(employee)      



employee.clear()
print(employee)  

print(employee)
