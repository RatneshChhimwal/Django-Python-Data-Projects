# Multithreading in Python:

# IMPORTANT: Refer to 'threadpool-executor.py' for alternative methods of multi-threading

"""

Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process.
In Python, we can use the threading module to implement multithreading.
The threading module provides a simple and efficient way to implement multithreading in Python.
Whether you need to create a new thread, run a function across multiple input values, or synchronize access to shared resources

"""

import threading                                        # We imported the 'threading' module
import time                                             # We imported the 'time' module
from concurrent.futures import ThreadPoolExecutor       # We imported the 'ThreadPoolExecutor' class from the module 'concurrent.futures'


# To demonstrate how multi-threading works without getting into a time-consuming task, we have used the 'time.sleep()' method below:

def func(seconds):                                      # We defined a function 'func' which takes the argument 'seconds' whenever called
    print(f"Sleeping for {seconds} seconds")            # The function 'func' prints an f-string
    time.sleep(seconds)                                 # The argument value of 'seconds' is passed to the method 'time.sleep()'
    return seconds                                      # We return the argument value 'seconds'

time1=time.perf_counter()                               # We use 'time.perf_counter()' to print the time it took for all the function calls below and assign it to time1
func(4)                                                 # First function call
func(3)                                                 # Second function call
func(2)                                                 # Third function call
time2=time.perf_counter()                               # We use 'time.perf_counter()' to print the time it took for all the function calls below and assign it to time2
print(time2-time1)                                      # We print the difference 'time2-time1'

t1=threading.Thread(target=func,args=[4])               # We use the 'Thread' class from 'threading' module with 'target=func' and 'args=[4]' and assign the result to 't1'
t2=threading.Thread(target=func,args=[3])               # We use the 'Thread' class from 'threading' module with 'target=func' and 'args=[4]' and assign the result to 't2'
t3=threading.Thread(target=func,args=[2])               # We use the 'Thread' class from 'threading' module with 'target=func' and 'args=[4]' and assign the result to 't3'

time1=time.perf_counter()                               # We use 'time.perf_counter()' to print the time it took for all the function calls below and assign it to time1

t1.start()                                              # We call the 'start' function on 't1'
t2.start()                                              # We call the 'start' function on 't2'
t3.start()                                              # We call the 'start' function on 't3'

"""
Joining multiple threads or processes after they have been started is essential
for ensuring that the main program doesn't finish execution
before all the threads or processes complete their tasks.

Joining threads/processes is crucial especially when they depend on each other's results or need to share resources
"""

t1.join()                                              # We 'join' the first thread t1
t2.join()                                              # We 'join' the second thread t2
t3.join()                                              # We 'join' the third thread t3

time2=time.perf_counter()                              # We use 'time.perf_counter()' to print the time it took for all the function calls below and assign it to time2
print(time2-time1)                                     # We print the difference 'time2-time1'
