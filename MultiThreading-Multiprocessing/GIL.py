# GIL : Global Interpreter Lock


# Definition:
# The GIL (Global Interpreter Lock) is a lock in CPython that allows only one thread at a time to execute Python bytecode within a process.
# Why do we use it?
# The GIL helps protect Python's memory management and internal data structures from being accessed by multiple threads at the same time, making CPython simpler and safer.


# suppose we have a memory box and inside that there is a small box on top left corner which has a value of 4 , 
# and now two thread are working to change the value of that 4 value simuletaneosuly , the other thread wait for the lock to be released 

#              Shared Resource
#                    🔒
#                     │
#         ┌───────────┴───────────┐
#         ↓                       ↓
#      Thread 1                Thread 2
#      gets lock               waits
#         ↓                       │
#     uses resource              │
#         ↓                       │
#    releases lock ───────────────┘
#                                 ↓
#                            Thread 2
#                            gets lock





