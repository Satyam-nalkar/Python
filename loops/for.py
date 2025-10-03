'''veggies = ["potato","brinjal","ladyfinger","cucumber"]
nums = [1,2,3,4,5]

# for val in nums:  

for val in veggies:  
    print(val)  '''



'''tup = [1,2,3,4,2,8,9]

for num in tup:
    print(num) '''



'''str = "apnacollege"

for char in str:
    if(char == 'o') :
        print("o found")
        break
    print(char)

print("End")'''


# Question 1

'''nums = [1,4,9,16,25,36,49,64,81,100]
                
for el in nums:
    print(el)'''                


# Question 2

tup  = (1,4,9,16,25,36,49,64,81,100)

idx = 0
x = 49
for el in tup:
    if tup[idx] == x :
        print("the number is found at index",idx)
        break
    idx += 1