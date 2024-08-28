# DECORATORS:

"""

Python decorators are a powerful and versatile tool that allows you to modify the behavior of functions and methods.
They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.

"""

# EXAMPLE:--------------------------------------------------------------------------------------------------------------

"""
Suppose, we have an add function that takes two arguments 'a' and 'b' and returns their sum.
Now we want to decorate this function, so that whenever this function is called with any values for the arguments,
It returns the sum but puts a 'Good Morning' string before and a 'Bye-Bye' string after the result
"""

# The below is an example of a greet() function with each line explained

def greet(fx):                          # We created a function greet(), That will be used with any function 'fx' as argument
    def mfx(*args,**kwargs):            # We create a function 'mfx()', This function is the one that prints our strings before and after the function fx
        print("Good Morning")           # First print for string 'Good Morning'
        fx(*args,**kwargs)              # The function 'fx' greet function is to be used on
        print("Bye-Bye")                # Second print for string 'Bye-Bye'
    return mfx                          # We return the function 'mfx' back to the 'greet()' function itself

# IMPORTANT:************************************************************************************************************

"""

The '*args' and '**kwargs' are used to handle multiple arguments in functions without specifying how many in advance.

*args - allows you to pass a variable number of non-keyword arguments to a function.
**kwargs - allows you to pass a variable number of keyword arguments to a function.

"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Now, we have created the 'greet()' function is created, We can simply use it with the 'add()' function while definition itself, As below:

@greet                      # We use the '@' symbol to put the decorator function before any function definition
def add(a,b):               # The 'a' and 'b' will be used through '*args' and '**kwargs'
    print(a+b)

add(2,4)