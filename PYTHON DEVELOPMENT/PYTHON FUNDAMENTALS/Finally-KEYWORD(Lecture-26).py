# FINALLy KEYWORD, EXCEPTION HANDLING:

"""

The finally code block is also a part of exception handling.
When we handle exception using the try and except block, we can include a finally block at the end.
The finally block is always executed,
It is generally used for doing the concluding tasks like closing file resources, closing database connection ending the program execution with a delightful message.

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SYNTAX FOR 'finally' CODE BLOCK:

"""
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXAMPLE:

lis=[9,8,7,6,5,4,3,2,1]                             # We have a list 'lis'
print(lis)

def funfinal():                                     # We defined a function 'funfinal'
    try:
        i=int(input("Enter the index"))
        return lis[i]                               # returns the value of 'lis' at the index i
    except IndexError:
        print("invalid index")
    finally:
        print("This will always be printed")

x=funfinal()                                        # We created variable 'x' that stores the value of function 'funfinal' call
print(x)


# IMPORTANT: REASON WHY WE USED 'FINALLY' AND NOT JUST 'PRINT' STATEMENT IS BECAUSE WHEN THE 'try-except' CONDITION IS USED INSIDE A FUNCTION, THE 'print' IS NOT EXECUTED

