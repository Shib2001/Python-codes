# Pure vs Impure Functions




# So here we have pure functions where we are not manipulatiing the global value, the impure function is the 
#exact opposite 
# def pure_chai(cups):
#     return cups * 10


# total_chai = 0

# def impure_chai(cups):
#     global total_chai
#     total_chai = total_chai + cups



# Lambda functions : 
# A lambda function is a small , one-line function that you write without giving it a normal function name.

# mtlb me ek function define krna chahta hu without using def keyword

# they are mostly used for functions like map(), filter() , sorted()

    # example :


numbers = [1,4,3,4,3,4,3,4]

# without lambda 

def double(x):
    return x * 2
result = map(double , numbers)
print(list(result))


# with lambda 

# lambda syntax :

# lambda arguments: expression

# numbers = [1,4,3,4,3,4,3,4]

# result = map(lambda x: x*2, numbers)

# print(list(result))