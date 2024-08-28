# FUNCTION ARGUMENTS:

# There are four types of arguments that we can provide in a function:

#1 - Default Arguments : Default arguments are provided while creating a func. The func computes for the default value if no value is provided later on during func call.

def average(a=9, b=1):          # We created func 'average' and defined default valued arguments 'a=9' & b='1'
    average_return=(a+b)/2      # We created a  variable 'average_return' and defined calculation for average of 2 values, creating a function within the 'average' func
    return average_return       # We returned the value of func 'average_return' to the func 'average'
print(average())                # We printed the 'average' func with no arguments, So the calculation is done for default values in step 1, Printing 5.0



#2 - Keyword arguments: We can provide arguments with key = value, interpreter recognizes the arguments by the parameter name. Hence, the order does not matter.

# We will consider the same 'average' function as above and just pass the arguments as 'keyword arguments'

print(average(b=9,a=21))        # Here we have used the keywords (parameter names) to pass the argument values, also the order has been changed defining 'b' first.



#3 - Required arguments: When args are defined without default values, then we need to pass the args in the correct order & the number of arguments should match.

# We will create a new function 'sum' to represent the same

def sum(a,b,c):                 # We defined a func 'sum' which takes 3 arguments, Although we did not predefine default values for all 3 arguments
    sum_return = (a+b+c)        # We created the var 'sum_return' which holds the sum of all 3 arguments, Creating a function within the main 'sum' function
    return sum_return           # We return the function

print(sum(2,4,8))      # As we did not predefine default values for all 3 arguments, We pass values for the same in the defined order itself

# *********** The above function would have not worked if we did not define values for 'a','b' & 'c', That is why they are called 'REQUIRED ARGUMENTS' *****************


