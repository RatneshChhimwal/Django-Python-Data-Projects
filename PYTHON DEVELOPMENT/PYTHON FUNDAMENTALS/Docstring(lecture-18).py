# DOCSTRING:

'''
A docstring in Python is a special string used to document your code.
It helps explain the purpose of modules, classes, functions, or methods.
You enclose docstrings within triple quotes (\''' or \""") right after your code's definition.
'''

# EXAMPLE:

def floor_div(a,b):             # Here we have defined a func 'floor_div' that takes 2 arguments 'a' & 'b'

    """Takes 2 integer values for variable 'a' & 'b' and return the floor division for the same"""              # *** THIS DOCSTING TELLS US THE PURPOSE OF THE FUNCTION

    c=a//b                      # Here we defined a variable 'c' that computes and stores the value of 'a//b'
    return c                    # Returning the variable 'c'

print(floor_div(10,2))    # Printing the function with values for arguments 'a' & 'b'

print(floor_div.__doc__)        # This is the command to print the 'docstring' specified in the function

