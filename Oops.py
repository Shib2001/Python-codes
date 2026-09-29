# # #Classes and objects


# class Student:

#     college_name = "Gretaer noida institute of technology"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in the database")

#     def welcome(self):
#         print("Welcome to the class", self.name)

# s1 = Student("karan", 89)
# print(s1.name, s1.marks, s1.college_name)

# # #simlarly 

# s2 = Student("arjuna",89)
# print(s2.name, s2.marks, s2.college_name)

# #Class and instance attributes

# #Now let's suppose maine college name upar de diya ab i know idhar college name 
# #change ni hone vaala wo same rhega but name and marks change ho skte h 
# #isilye we defined it using the self dot 
# # so idhar college name was class attribute and self dot was instance attribute


# Calling a method
# s1.welcome()
# s2.welcome()

# #________________________________________________________


# Practice question : 


# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


#     def average(self, other_student):
#         return(self.marks + other_student.marks) / 2


# # m1 = Student("shiv",90) 
# print("The student is",m1.name,"and his marks are",m1.marks,)


# m2 = Student("karan", 89)
# print("The student is",m2.name,"and his marks are",m2.marks)


# m1 = Student("shiv",800)
# m2 = Student("Karan",90)


# print("Avaerage marks for the subjects are", m1.average(m2))



# class Account:

#     def __init__(self, balance, account):
#         self.balance = balance
#         self.account = account

# # Now we have to create a method to deposit and withdraw money from the account.


#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount deposited:", amount)
#         print("Current balance:", self.balance)

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else: 
#             self.balance -= amount
#             print("Amount withdrawn:", amount)
#             print("Current balance:", self.balance)

# my_account = Account(1000, "AC83788393")

# # my_account.deposit(1500)
# my_account.withdraw(33500)









