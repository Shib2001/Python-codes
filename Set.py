#Set is the collection of unordered items.
#Each element in the set must be unique and immutable.

# Random = {1,2,3,2,3,2,3,2,"hrllo","hrllo",9.0,8.00,9.00}

# print(Random)
# print(type(Random))

#and check in the print humesa unordered values print hui h 

#How to create a empty set ? , mind you it woudn't be like {} that is dictionary 

#Answer is Random = set();

#Now most important thing 

#_______________________________________________________________________________________

# Set are immutable which means uski values ko hum change or replace ni kr skte 
# which means hume usme cheezien add aur remove kr skte h 
# in short set is mutable , but it's element are immutable 



Random = {1,2,3,2,3,2,3,2,"hrllo","hrllo",9.0,8.00,9.00}

Random2 = {1,2,3,2,3,2,3878378347834,2,"hrllo","hrllo",9.0,8.00,9.00,"sjgfjsdfjfgfgshjfgydtewytb eatr"}

Randwa = Random.union(Random2)

print(Randwa)

#Union combines both set values & returns new 

#Combines common values and returns new : intersection