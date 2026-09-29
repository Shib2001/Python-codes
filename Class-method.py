# Class method : a class method is bound to the class and recives the class as an implicit first argument.

# Note - static method can't access or modify class state and 



class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)   # here cls is same as self which we used in instance method 


Student.show_school()