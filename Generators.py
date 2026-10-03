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

