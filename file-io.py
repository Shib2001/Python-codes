#it is basically used to read and write files in python. 
# It is a built-in module that provides functions to work with files. 
# The file-io module allows you to open, read, write, and close files in various formats such as text files, binary files, and more.
#  It also provides methods for handling file paths and directories.


# f = open("file.txt", "r")  # Open a file in read mode
# data = f.read() #we can specify the number of bytes to read from the file as f.read(5) or f.read(6)
# there is aslo f.readline() - which reads a single line from the file and f.readlines() - which reads all the lines from the file and returns them as a list of strings.
# print(data)  # Print the contents of the file
# print(type(data))  # Print the type of the data read from the file
# f.close()  # Close the file



#also some useful methods of file-io module are:

#'r": Read mode - Opens a file for reading (default mode). The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.
#'w": Write mode - Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
#'x': Exclusive creation mode - Opens a file for exclusive creation. If the file already exists, it raises an error. If the file does not exist, it creates a new file.
#'a': Append mode - Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
#'b': Binary mode - Opens a file in binary mode. This is used for non-text files such as images or audio files.
#'t': Text mode - Opens a file in text mode (default mode). This is used for text files.
#'+': Update mode - Opens a file for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.


#-------------------------------------------------------------------------------------------------------------

#WRITE MODE 

f = open("file.txt","a")

new = f.write("ndshgsdhgsadhgdhdhasgdhsgds")
print(new)

f.close()


# Another way to create a file if that doesn't exist 
f = open("sample.txt","w") #this will create a new file if it doesn't exist, if it exists it will raise an error
f.close()

# As you can see in the python-codes that file has been automatically created in the same directory as the python file.


# WITH SYNTAX 



with open("file.txt","w") as f:
    data = f.write("Hello, World!")
    print(data)