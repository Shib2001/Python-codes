# #1. Local Scope : a variable created inside a function is local to that function. 

# # def greet():
# #     name = "Shiv"
# #     print(name)

# # greet()
# # print(name) #This will show error because we created a vriable name inside greet() function we can't call it outside the function 


# #2. Enclosing scope : This happens with nested functions. The inner functions can access vairables from the outer function.

# # def outer():
# #     name = "Shiv"

# # def inner():
# #     print(name)

# #     inner()

# # outer()


# #3 Global Scope : A variable created outside all functions is global 

# name = "shiv" 

# def greet():
#     print(name)

# greet()
# print(name)