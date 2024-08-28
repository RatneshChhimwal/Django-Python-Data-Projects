# FUNCTIONS:

'''

A 'function' is like a mini-program that you create to do a particular job.
You give it a name, and it contains a set of instructions that you can use over and over again in your code.
Functions make your code more organized and easier to understand because you can break it into smaller, reusable parts.

'''

# REFER TO THE CODE BELOW TO UNDERSTAND WHY WE NEED FUNCTIONS:
# Suppose we had to calculate 'geometric mean' for 2 sets of variables 'a','b' & 'c','d', So as per our knowledge till now, it would be done as below:

a=4
b=6
Gmean1=(a*b)/(a+b)
print(Gmean1)

c=8
d=10
Gmean2=(c*d)/(c+d)
print(Gmean2)

# We calculated the mean here twice for simple values, but it won't work for complex cases. So, we can create a func to do the same for any two arguments when needed.

# Here's how we define a function:

def Gmean(a,b):                     # We write 'def' to start the definition of the func, followed by the name of the func and then the number of args it would intake
    Gmean = (a * b) / (a + b)       # Here we define the functionalities of the function we created
    print(Gmean)                    # Printing the function

# Now if we wanted to calculate mean for any number of pairs of values we can directly the created func 'Gmean' for those values as arguments

print(Gmean(8,10)) # This prints two things: The 'Gmean,' which is '4.44' in this case, and 'none' below it because there's no 'return' statement.



# WHAT IS A 'RETURN' STATEMENT ? ******************************************************************************************************************************************


'''

The return statement is required to enable a function to pass computed results back to the caller.
Without it, the calculated value remains within the function, inaccessible outside the code.
So, no computation can be done with the value if just calculated and not returned.

'''

# Here's how we can write the same code for function definition with the return statement:

def Gmean3(a,b):                        # We defined a function named 'Gmean3' that takes two parameters, a and b
    Gmean_Result = (a * b) / (a + b)    # This line computes the geometric mean using the formula & assigns the result to the variable Gmean_Result.
    return Gmean_Result                 # This line ensures that the computed geometric mean (Gmean_Result) is returned when the function is called.

print(Gmean3(8,10))               # This prints the geometric mean for values (8,10) passed as arguments for the function 'Gmean3'




# ******************************************** IMPORTANT ***************************************************************

# BELOW ARE 2 METHODS FOR DEFINING A FUNCTION FOR FLOOR DIVISION:

# REMEMBER: ''' floor_div3 works with any value provided by the user, while floor_div2 is designed to work with the argument you pass when calling the func directly. '''

# 1st METHOD ---------------------

def floor_div2(a):
    b=a//2
    return b

print(floor_div2(12))


# 2nd METHOD -----------------------

c=int(input("Enter a number"))

def floor_div3(c):
    b=(c//2)
    return b

print(floor_div2(c))