# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()



# f = open("demo.txt","r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
 
# f.close()


 
# f = open("demo.txt","a")

# f.write("\nThen I'll move to ReactJS")
# f.close()


# f = open("demo.txt","r+")
# f.write("abc")
# f.close()


# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)


with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data")
