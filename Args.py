# # Arguments vs parameters 


# # Parameter = variable in function defination.
# # Arguments = actual value you pass to the function .


# # example :

# def greet(name): #here name is parameters
#     print("Hello", name)

# greet("Shiv")   #Shiv is argument here the values that we are passing to the parameters 


# Positional arguments : also known as kwargs keyword arguments

# def make_chai(tea,milk,sugar):
#     print(tea,milk,sugar)

#     make_chai("Wah taj","Yes","No")

#     #So instead of doing this we write it as 

# make_chai(tea="Green", milk = "butter dahi" ,sugar="Medium", )


# Now sometimes there could be mix of args and kwargs 

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinammon","Cardamom",sweetener="Honey", foam="yes", size="Large")

#just notice the result and you will understand the concept here 