# 🟢 Easy
# 1. Simple Calculator

# Topics: Variables, Inputs, Type conversions
# Question: Write a program that asks the user to input two numbers, converts them to integers, and then prints out their sum and their product.
# 💡 Hint: Use the input() function to get the user's input, but remember it returns a string. You'll need to wrap it with int() before performing mathematical operations.



# var1 = int(input("number: "))

# var2 = int(input("number: "))

# print(f"the sum of {var1} and {var2} is {var1} + {var2}")
# print(f"The product of {var1} and {var2} is {var1 * var2}")




# 2. Slicing a Message

# Topics: Strings, Slicing, Indexing
# Question: Given the string message = "Python is awesome!", write code to extract the word "Python", the word "awesome", and the exclamation mark ! using slicing and indexing.
# 💡 Hint: Slicing syntax is [start:stop]. Remember that Python uses 0-based indexing, and the stop index is exclusive. You can also use negative indexing for the last character.



# msg = "Python is awesome!"


# #Word 1 : Python 

# print(msg[0:6])


# #Word 2 : awesome

# print(msg[10:17])


# #Word 3 : ! 

# print(msg[17])



# 3. Fruit Basket Management

# Topics: Lists, List-fun
# Question: Create a list containing 4 of your favorite fruits. Next, use a list function to add "Mango" to the end of the list. Finally, use another function to remove the second fruit from your list and print the updated list.
# 💡 Hint: Look into the .append() method for adding an item to the end, and the .pop() method or del keyword for removing an item at a specific index.


# fruits = ["apple", "watermelon", "rasberry", "peach"]

# fruits.append("mango")

# fruits.pop(1)

# print(fruits)





# 🟡 Medium
# 4. Leap Year Checker

# Topics: Conditions, Ternary, Calculation
# Question: Write a program that asks for a year and determines if it is a leap year. Try to use a ternary operator to assign the string "Leap Year" or "Not a Leap Year" to a variable, then print it.
# 💡 Hint: A year is a leap year if it is divisible by 4. However, if it ends in 00 (divisible by 100), it must also be divisible by 400. A ternary operator in Python looks like: value_if_true if condition else value_if_false.



# year = int(input("Please enter the year:"))

# if(year%4==0):
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")




# 5. Grade Book Analyzer

# Topics: Dictionaries, forloops, Conditions
# Question: You are given a dictionary of student test scores: scores = {"Alice": 85, "Bob": 92, "Charlie": 78}. Write a for loop to iterate through this dictionary and print each student's name alongside a letter grade (>= 90 is 'A', >= 80 is 'B', otherwise 'C').
# 💡 Hint: You can easily iterate through both keys and values in a dictionary simultaneously by using the .items() method in your for loop.



# Students ={
#     "Alice":85,
#     "Bob":92,
#     "Charlie":78
# }



# for name, score in Students.items():

#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     else:
#         grade = "C"

#     print(name, grade)


# 6. Factorial Finder

# Topics: Functions, Recursions
# Question: Write a recursive function called calculate_factorial(n) that takes an integer and returns its factorial. Test it by finding the factorial of 5.
# 💡 Hint: The factorial of a number n is n * calculate_factorial(n-1). Don't forget your base case to stop the recursion: the factorial of 1 (or 0) is simply 1!
# 7. Unique Word Counter

# Topics: file-io, Set, String-fun
# Question: Create a file named sample.txt with a few sentences of text. Write a script that reads this file line by line, splits the lines into words, and adds all the words to a set. Finally, print the total number of unique words in the file.
# 💡 Hint: Use the with open(...) context manager to read the file safely. The .split() method will break sentences into words. A set is perfect here because it automatically discards duplicate entries.
# 🔴 Hard
# 8. Vehicle Fleet

# Topics: Oops, Inheritance, Polymorphism
# Question: Create a base class called Vehicle with an __init__ method that sets make and model. Then, create a subclass called Car that inherits from Vehicle but also has a num_doors attribute. Implement a display_info() method in both classes using method overriding to print their specific details.
# 💡 Hint: Inside the Car class's __init__ method, use super().__init__(make, model) to call the parent class's constructor before setting the new num_doors attribute.
# 9. Employee Tracking

# Topics: Oops(part-2), Class-method
# Question: Create a class called Employee. It should have a class attribute called total_employees that increments by 1 every time a new Employee object is initialized. Write a @classmethod that prints out the current value of total_employees. Instantiate 3 employees and call the class method to verify the count.
# 💡 Hint: A class attribute is defined directly inside the class, outside of the __init__ method. Your class method should take cls as its first parameter (instead of self) and access the variable via cls.total_employees.
# 10. Persistent To-Do List Application

# Topics: Loops, Conditions, Inputs, file-io, Oops
# Question: Build a simple, interactive To-Do List app using OOP. Create a TaskManager class with methods to add_task(task), view_tasks(), and save_to_file(). Use a while loop to show the user a menu with choices (1. Add, 2. View, 3. Save & Exit). The program should keep running until the user chooses to exit, at which point it writes all tasks to a text file.
# 💡 Hint: Keep a list of strings inside your TaskManager instance to hold the tasks. When saving, iterate over that list and write each string followed by a newline \n to your file.