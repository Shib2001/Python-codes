from multiprocessing import Process
import time


def take_orders():
    for i in range(1, 4):
        print(f"Taking order for {i}")
        time.sleep(1)


def prepare_food():
    for i in range(1, 4):
        print(f"Preparing food for {i}")
        time.sleep(2)


if __name__ == "__main__":

    orders_process = Process(target=take_orders)
    food_process = Process(target=prepare_food)

    orders_process.start()
    food_process.start()

    orders_process.join()
    food_process.join()

    print("All orders taken and food prepared")


# What does __main__ or __name__ actually do 


#     Imagine your file contains:

# Create Process
#      ↓
# Start Process
#      ↓
# Child loads the file again
#      ↓
# Create Process again
#      ↓
# Start Process again
#      ↓
# Child loads the file again
#      ↓
# Create Process again...

# This could continue creating processes recursively.

# Python therefore stops it and gives:

# RuntimeError:
# An attempt has been made to start a new process
# before the current process has finished bootstrapping.

# The if __name__ == "__main__": acts like a safety gate:

#              Python file
#                   │
#           Is it the main file?
#              /          \
#            YES          NO
#             │            │
#             ↓            ↓
#        Create/start    Don't create
#        processes       new processes

# So we write:

# if __name__ == "__main__":
#     p = Process(target=task)
#     p.start()
#     p.join()

# The child process can load the file safely, because the process-creation code is protected by the if.

# Easy way to remember

# Process() → Create the worker

# .start() → Start the worker

# .join() → Wait for the worker

# __name__ == "__main__" → Only the original/main process should execute this process-creation code.

# This protection is especially important when using multiprocessing on Windows.