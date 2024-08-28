
"""

ThreadPoolExecutor is used in Python to manage and execute multiple threads concurrently in a pool.
Instead of creating and managing threads individually, ThreadPoolExecutor allows you to submit tasks,
and it takes care of assigning those tasks to available threads in the pool.
This helps in efficiently utilizing resources and handling multiple tasks concurrently.
It simplifies the process of parallelizing tasks and managing the execution of functions in a multithreaded environment.

"""
import time                                             # We import the 'time' module
from concurrent.futures import ThreadPoolExecutor       # We import the 'ThreadPoolExecutor' class from the module 'concurrent.futures'

def func(seconds):                                      # We defined a function 'func' which takes the argument 'seconds' whenever called
    print(f"Sleeping for {seconds} seconds")            # The function 'func' prints an f-string
    time.sleep(seconds)                                 # The argument value of 'seconds' is passed to the method 'time.sleep()'
    return seconds                                      # We return the argument 'seconds'

def poolingDemo():                                      # We created a function 'poolingDemo()'
  with ThreadPoolExecutor() as executor:                # ThreadPoolExecutor() here is used as a context manager with the 'with' statement

      # The 'with' statement ensures that the 'ThreadPoolExecutor' is properly initialized and closed/shutdown after the block of code inside the 'with' statement is executed.

    future1 = executor.submit(func, 3)
      # We use the 'submit' function with the 'ThreadPoolExecutor()' instance (executor), providing 'func' and '3' as arguments, storing the results in the variable 'future1'.
    future2 = executor.submit(func, 2)
      # We use the 'submit' function with the 'ThreadPoolExecutor()' instance (executor), providing 'func' and '3' as arguments, storing the results in the variable 'future2'.
    future3 = executor.submit(func, 4)
      # We use the 'submit' function with the 'ThreadPoolExecutor()' instance (executor), providing 'func' and '3' as arguments, storing the results in the variable 'future3'.

    print(future1.result())
    print(future2.result())
    print(future3.result())

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      # Most of the time, We will have URLs or Addresses in the form of a list, So to map the 'func' with iterables from the list as argument, We use the 'executer.map' method

    l = [3, 5, 1, 2]                                # We have a list 'l'
    results = executor.map(func, l)        # We use the '.map' method with 'executor' passing 'func' and the list 'l' as args and store the result inside 'results'
    for result in results:                          # We iterate through 'results'
      print(result)                                 # Printing 'results'

poolingDemo()                                       # Calling the function 'poolingDemo()'