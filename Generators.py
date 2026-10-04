# # Generator in Python — Definition

# # A generator in Python is a special type of function that produces values one at a time instead of returning all values at once.

# # It uses the yield keyword instead of return.

# # Simple definition to remember:

# # A generator is a function that generates values one by one using yield, saving memory by not storing all values at once.


# Generator vs Normal Function

# Normal function:

# def numbers():
#     return [1, 2, 3]

# It creates and returns the whole list at once.

# Generator:

# def numbers():
#     yield 1
#     yield 2
#     yield 3

# It produces one value at a time, which is especially useful for large amounts of data.

# Key point: yield pauses the function and remembers its state. When the next value is requested, it continues from where it stopped.

# ANother example 

# def Food_items():
#     yield "Meat : Butter chicken"
#     yield "Vegan : Soya chicken"
#     yield "Diary : Butter Milk"


# foods = Food_items()

# for items in foods:
#     print(items)


# Infinte genrators 

# def infinite_food():
#     count = 1
#     while True:
#         yield f"Refil #{count}"
#         count += 1


# refill = infinite_food()

# for _ in range (7):
#     print(next(refill))


# How can we send the values to the generators and how can we store the value in yeield 



# def Samosa_center():
# #     print("Welcome to our shop ! what would you like to have ?")
# #     order = yield # as you can see here we are storing the value in yeild 
# #     while True:
# #         print(f"Preparing: {order}")
# #         order = yield # we wrote this for getting mutiple orders , if we comment this only the first order would run and that too infinietly 

# # stall = Samosa_center()
# # next(stall) #Start the generator

# # stall.send("Masala Chai") # here we are sendibg the value to the genrator
# # stall.send("Meat samosa")



# Close generators 

def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "waiting for the chai order"
    except:
        print("Stall closed , No more chai")

stall = chai_stall()
print(next(stall))
stall.close() # and this is how we close a generator 