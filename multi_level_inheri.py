# Single Inheritance

'''class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())  '''


class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand

class fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = fortuner("diesel")
car1.start()