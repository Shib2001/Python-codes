# #Classes and objects 


# # class Student: # this is class
# #     name = "Karan"

# # s1 = Student() # this is object
# # print(s1)



# #Constructors


class Student:

    college_name = "Gretaer noida institute of technology"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in the database")

s1 = Student("karan",89)
print(s1.name, s1.marks , s1.college_name)

# #simlarly 

s2 = Student("arjuna",89)
print(s2.name , s2.marks, s1.college_name)

#Class and instance attributes

#Now let's suppose maine college name upar de diya ab i know idhar college name 
#change ni hone vaala wo same rhega but name and marks change ho skte h 
#isilye we defined it using the self dot 
# so idhar college name was class attribute and self dot was instance attribute

#________________________________________________________





