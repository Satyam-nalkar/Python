# for i in range(1,5):
#     print("hello",i)


# nums = [1,4,9,16,25,36,49,64,81,100]   

# for el in nums:
#     print(el)



# num = int(input("Enter a number: "))
# for i in range(1,11):
#         print(f"{num} * {i} = {num*i}")



# num = int(input("Enter a number: "))
# for i in range(10,0,-1):
#         print(f"{num} * {i} = {num*i}")
        



# row = int(input("Enter number of rows: "))
# for i in range(1,row+1):
#     # for j in range(1,i+1):
#         print(" * " *i,end=" ")
#         print()



row = int(input("Enter number of rows: "))
for i in range(1,row + 1):
    # for j in range(1,i+1):
        print(" " * (row - i),end=" ")
        print("* " * i)