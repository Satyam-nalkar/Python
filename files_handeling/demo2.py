# # import os 
# # os.remove("sample.txt")

# with open("practice.txt","w") as f:
#     f.write("Hi everyone \nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")
 


'''with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)  '''


def check_for_word():
    word = "xlearning"
    with open("practice.txt","r")as f:
        data = f.read()
    if(word in data):
        print("Found")
    else:
        print("not found")

 
def check_for_line():     
    word = "learning" 
    data = True
    line_no = 1
    with open("practice.txt","r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return   
            line_no += 1 

    return -1
check_for_line()

   