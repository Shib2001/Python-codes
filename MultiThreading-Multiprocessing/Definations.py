
# Concurrency 

# Time →

# Task A: ███     ███     ███
# Task B:    ███     ███     ███




# Parallelism_______________________________________________________



# Person 1 → Task A: ███████████
# Person 2 → Task B: ███████████


#_____________________________________________________________________________________________________



# Examples of Concurrency and Parallelism



import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for {i}")
        time.sleep(1)

def prepare_food():
    for i in range(1, 4):
        print(f"Preparing food for {i}")
        time.sleep(2)

        # this is a synchronous task so we use time.sleep here 

# Create the threads 

orders_thread = threading.Thread(target=take_orders)
food_threads = threading.Thread(target=prepare_food)



# let's invoke them 

orders_thread.start()
food_threads.start()



# wait for both to finish 


orders_thread.join()
food_threads.join()

print(f"All orders taken and preparing food for all ")


