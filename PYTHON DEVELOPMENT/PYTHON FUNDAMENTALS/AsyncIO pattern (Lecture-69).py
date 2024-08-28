#Async IO in Python:

# REFER TO 'Example asyncio.py' and 'Example non-asyncio.py' FOR BETTER UNDERSTANDING OF THE TOPIC

"""

Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.
In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python.
With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle
large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications,
network services, or data processing pipelines, async IO is an essential tool for any Python developer.

"""

import asyncio                                  # Firstly, we import the 'asyncio' module

async def my_async_function():                  #  We define a function 'my_async_function' The async keyword is used to define an asynchronous function

    # An asynchronous function is a special type of function that can be paused during its execution, allowing other tasks to run concurrently.

    # asynchronous code here

    await asyncio.sleep(5)                      # Inside the function 'my_async_function' we define the sleep for '1' second
    return "Hello, Async World!"                # We return the string "Hello, Async World!"

def second_non_async_function():
    return "Hello this is the non-async-function"

async def main():                               # We define a function 'main' The async keyword is used to define an asynchronous function
    result = await my_async_function()          # We define a variable 'result' with the 'await' keyword to tell the event loop to pause and wait for the asynchronous function (my_async_function() to complete before moving on to the next line of code
    print(result)                               # We print the value of the variable 'result'


    L = await asyncio.gather(
            my_async_function(),
            my_async_function(),
            my_async_function(),
        )

    print(L)
    print(second_non_async_function())


asyncio.run(main())

# REFER TO 'Example asyncio.py' FOR BETTER UNDERSTANDING OF THE TOPIC

