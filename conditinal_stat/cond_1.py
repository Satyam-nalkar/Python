# age = 21
# if(age >= 18):
#     print("can vote an apply licence")
#     print("can drive")
# else:
#     print("can not vote")




# light = "greens"
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look") 
# else:
#     print("ligt is broken")
# print("end of code")




# num = 5
# if(num > 2):
#     print("greater than 2")
# elif(num > 3):
#     print("greater than 3")



marks =int(input("Enter student marks: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student:",grade)  
