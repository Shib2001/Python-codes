# # orders = ["masala" , "ginger"]

# # print(orders[2]) # Now we most probably will get error something like list out of range ( this is also known as indexError)




# foods = {"masala":45, "milk":78}

# try :
#     foods["diary"] # this is how we throw an error 
# except KeyError:
#     print("The key that you are trying to access does not exist ")



# 1. What does raise mean?
# Normally Python raises errors automatically:
# orders = ["masala", "ginger"]print(orders[2])


# Python raises:
# IndexError: list index out of range

# But sometimes you want to tell Python that something is wrong yourself.
# That's where raise comes in:
# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")


# Output:
# ValueError: Age cannot be negative

# You are basically saying:
# "Python, I have detected a problem. Stop the program and raise this error."



# Raise + try except 


# foods = {"masala": 45, "milk":78}

# try : 
#     if "diary" not in foods:
#         raise KeyError("The key 'diary' does not exist ")
# except KeyError as e:
#     print(e)


# def brew_chai(flavor):
#     if flavor not in ["masala", "ginger","elaichi"]:
#         raise ValueError("Unsupported chai flavor....")
#     print(f"brewing {flavor} chai for you")

# brew_chai("mint")
# print(brew_chai)


# Custom errors ____________________________________________________________________________________________________________________


class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    return balance - amount


# balance = 10000000
# amount = 500000


# try:

#      withdraw(balance, amount)
#      print(f"Your amount {amount} has been succefully withdrawn  , your current balance is {balance}")

# except InsufficientBalanceError as e:
#     print(e)

# Finally example ____________________________________________________________________________________________________

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    return balance - amount

balance = 10000000
amount = 500000


try:
    new_balance = withdraw(balance, amount)

except InsufficientBalanceError as e:
    print(e)

else:
    print(f"Withdrawal successful of amount {amount}")

finally:
    print(f"Transaction process completed , Your current balance is {new_balance}")