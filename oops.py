class Student:

#     college_name = "ABC College"
#     # name = "karan kumar"
#     name = "anonymous"
    
#     # default constructor
#     def __init__(self):
#         print("adding new student in Database..") 
    
    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..") 


    def welcome(self):
        print("welcome Student",self.name)
  
    def get_marks(self):
        return self.marks


s1 = Student("karan",97)
s1.welcome()

print(s1.get_marks())
# s1 = Student("karan",97)
# print(s1.name)

# s2 = Student("Arjun",88)
# print(s2.name,s2.marks)

# print(s2.college_name)

# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
