# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi",self.name,"your avg score is:", sum/3)   

#     @staticmethod   
#     def hello():
#         print("hello")


# s1 = Student("tony stark",[99,98,97])
# s1.get_avg()

# s1.name = "Ironman" 
# s1.get_avg()
# s1.hello() 




class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False  

    def start(self):
        self.clutch = True
        self.acc  = True
        print("car started..")


car1 = Car()
car1.start() 