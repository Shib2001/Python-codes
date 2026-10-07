# # Examples of Concurrency ( This is multithreading )



import threading
import time

# def take_orders():
#     for i in range(1, 4):
#         print(f"Taking order for {i}")
#         time.sleep(1)

# def prepare_food():
#     for i in range(1, 4):
#         print(f"Preparing food for {i}")
#         time.sleep(2)

#         # this is a synchronous task so we use time.sleep here 

# # Create the threads : A thread is another worker inside your program that can execute a task independently.
# # so here we created the threads to do the multiple works for taking orders and preparing foods 

# orders_thread = threading.Thread(target=take_orders)
# food_threads = threading.Thread(target=prepare_food)



# # let's invoke them 

# orders_thread.start() # here we have started this thread to work 
# food_threads.start() # same goes for this 

# # You might be wondering here why didn't we just simply call them ? 
# # because 
# # # Main Thread
# #      ↓
# # take_orders()
# #      ↓
# # WAIT until finished
# #      ↓
# # prepare_food()





# # wait for both to finish ____________________________________________________________________________________


# orders_thread.join() # that's the exact meaning of join that the thread of taking orders will wait until the thread of preparing food has finished 
# food_threads.join()

# print(f"All orders taken and preparing food for all ")




# Another example ____________________________________________________________________________________________________________

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk Boiled")


def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Done with bun toast")


start = time.time()

t1 = threading.Thread(target=boil_milk)
t2= threading.Thread(target=toast_bun)


t1.start()
t1.join()
t2.start()
t2.join()


end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")