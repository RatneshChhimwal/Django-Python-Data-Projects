# In python, we can raise custom errors by using the 'raise' keyword.

"""
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
This is useful when we want to do something when a particular exception is raised.
For example, sending an error report to the admin, calling an api, etc.
"""

# EXAMPLE:

inp=int(input("Enter a number between 10 and 20"))              # We asked for a user integer input between 10 and 20 with variable 'inp'

if inp<10 or inp>20:                                            # We define the 'if' condition for the user input
    raise ValueError("Value is not between 10 and 20")          # Here the 'raise' keyword is used to raise a specific built-in class of error
else:
    print(inp)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# IMPORTANT: HERE WE HAVE THE SAME PROGRAM AS ABOVE, BUT IN THIS VERSION< THE USER IS ALLOWED TO ENTER THE STRING 'quit' ALSO, REFER BELOW:


inp1=input("Enter a number between 10 and 20")

if inp1=="quit":        # Here we started a primary/main 'if-else' loop where we let the user pass on with string 'quit' as input
    print(inp1)
else:                   # The 'else' part of the primary/main 'if-else' loop contains a secondary 'if-else' loop
    inp1=int(inp1)      # We convert 'inp1' to an integer here, not in the subsequent 'if' statement, due to the precedence of the boolean operation inside the brackets

    if inp1<10 or inp1>20:

        # We could not write the above as: 'if int(inp1)<10 or int(inp1)>20' as the condition inside the brackets would have been checked first and then converted to int

        raise ValueError("Value is not between 10 and 20")
    else:
        print(inp1)


