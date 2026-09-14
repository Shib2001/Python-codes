# Inheritance

# When one class(child/derived) derives the properties & methods of another class(parent/base)


# A static method is a normal function placed inside a class because it is logically related to that class.

# The important thing is:

# A static method does NOT need information from the object (self) or the class (cls).

# That's basically it.

# Single-level-inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started ....")

#     @staticmethod
#     def stop():
#         print("car stopped....")


# class ToyotaCar(Car): # here i inherited all of the car properties 
#     def __init__(self, name):
#         self.name = name


# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.name)
# print(car2.start())



# Multi-level-inheritance

# class Car: # Base Parent
#     @staticmethod
#     def start():
#         print("car started ....")

#     @staticmethod
#     def stop():
#         print("car stopped....")


# class ToyotaCar(Car): # derived Child
#     def __init__(self,brand):
#         self.brand = brand


# class Fortuner(ToyotaCar): #derived Grandchild
#     def __init__(self, type):
#         self.type = type



# car1 = Fortuner("EV CAR")
# car1.start()
# car1.stop()


# Multiple inheritance : where a derived class can take the properties from multiple inherited base class


class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC ="Welcome to class C"

c1 = C()


print(c1.varC)
print(c1.varB)
print(c1.varA)