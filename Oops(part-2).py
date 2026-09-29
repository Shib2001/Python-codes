#del is a Python statement used to remove a reference to an object, or to delete an attribute, item, or other target from a namespace/container.


# class Student:
#     def __init__(self,name,marks,phone):
#         self.name = name
#         self.marks = marks
#         self.phone = phone 


# s1 = Student("vicky",89,882316381)
# del s1.name
# print(s1.marks)
# print(s1.phone)


# Now what i printed above was public attributes the name and marks and phone i can print it outside the class Student scope 
# Now we will private attributes 


# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # we made the acc password as private attribute by putting the two underscores 

# acc1= Account("38273287","bdshds")


# print(acc1.acc_no)
# print(acc1.__acc_pass)



