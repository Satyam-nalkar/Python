# collection = {1,2,3,4,"hello World"}
# print(collection)
# print(type(collection)) 
# print(len(collection)) 

# collection = set()    # for empty set
# print(type(collection))


collection = set()
collection.add(1) 
collection.add(2) 
collection.add(2) 
collection.add(3) 
collection.add("string")
collection.add((1,2,3,4)) 
  
collection.remove(1) 
# collection.clear()
print(len(collection))
print(collection.pop())
print(collection.pop())