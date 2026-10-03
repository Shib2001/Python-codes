# Comprehensions : are a concise way to create lists,sets,dictionaries,or generators in python 
# using a single line of code


#tYPES of compreshensions 

# List , set , dictionary , Generator 


# 1. let's see how are we gonna use comprehensions in lists 

# [expression for item in iterable if condition]

# menu = [
#     "Masala Chai",
#     "Iced Lemon Tea",
#     "Green Tea",
#     "Iced Peach Tea",
#     "Ginger chai"
# ]

# iced_tea = [tea for tea in menu if "Iced" in tea]

# print(iced_tea)
#__________________________________________________________________________________________________________________________________

# SET COMPREHENSIONS 

# menu = [
#     "Masala Chai",
#     "Iced Lemon Tea",
#     "Green Tea",
#     "Iced Peach Tea",
#     "Ginger chai",
#     "Masala Chai",
#     "Ginger chai"
# ]

# unique_chai = {chai for chai in menu} # agr itna bhi print krenge toh we"ll get unique values in there 


# unique_chai = {chai for chai in menu if len(chai)< 13}

# print(unique_chai)



# DICTIONARY ______________________________________________________________________________________________________________________________________

# tea_prices_inr = {
#     "Masala chai":40,
#     "Green Tea":50,
#     "Lemon Tea":200
# }


# tea_prices_usd = {tea:price/80 for tea, price in tea_prices_inr.items()} # yaha pr ye .items key value pairs me pura data de deta h to iterate through 
# print(tea_prices_usd)



# Generators ________________________________________________________________________________________________________________________________________


daily_sales = [5,10,5,3,4,5,3,15]

total_cups = sum(sale for sale in daily_sales if sale >  5)

print(total_cups)

# 3 Now iske print krke you won't get the desirable value , so we can use methods such as filters map or sum to the whole comprehension