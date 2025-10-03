# Question 1st
'''cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain america","shaktiman"]

# print(heroes[0],end=" ")
# print(heroes[1],end=" ")

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)
print()  '''



# Question 2nd
'''n = 5

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5) '''



# Question 3rd
# def converter(usd_val):
#     inr_val = usd_val * 83 
#     print(usd_val,"USD =",inr_val , "INR")

# converter(1)  


n = int(input("Enter the number "))
def even_odd(n):
    if(n % 2 == 0):
        print("This is even number")
    else:
        print("This is odd number")

even_odd(n)   


