"""

Exception handling in Python is a method for dealing with errors and unexpected issues in your code.
It uses "try" and "except" blocks to catch and manage these errors, ensuring that your program can continue running smoothly even when problems occur.

"""

num = input("Enter a number:")
for i in range(1, 11):                          # This is a for loop to print the multiplication table
    print(f"{num} X {i} = {int(num) * i} ")     # Prints f-string

print("We want to print this line")

# Above loop prints the multiplication table till a numeric value is entered, if otherwise, Throws an error as the input is being converted into an 'int' during 'print'
# If an error occurs, The print statement at line '12' will also not be printed as the whole program will be interrupted/terminated

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# THE 'try-except' method:

try:
    for i in range(1, 11):
        print(f"{num} X {i} = {int(num) * i} ")
except:                                             # All types of Exceptions/Errors are handled here, This prints 'Error occurred' as soon as faced with an error
    print("Error occurred")

print("We want to print this line")                 # This line is printed when 'try-except' is used even if an error occurs


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# IMPORTANT: Note that we can handle specific exceptions. example: In the below code, we can focus on the error when the input is not a numerical value. (value-error)

# ValueError

a=input("enter a number")

try:
    for f in range(0,int(a)+1):             # The following 'for' loop takes the user input 'a' then adds it with values of 'f' with range '0' to 'a'
        print(a+f)                          # Suppose we had 'a' as 3, then 'f' will have value 0,1,2,3 consecutively and '(a+f)' prints (3,4,5,6)

except ValueError:                          # Here we used 'ValueError' exception type to ensure the value entered as input 'a' is of an integer type
    print("Invalid input type")             # Exception handled


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2- IndexError: In the below code, we can focus on the error when a wrong index is not a called. (index-error)

l=[1,2,3,4,5]                                           # Here we have a list 'l'
print(l)

k=int(input("enter the index you want to fetch"))       # We take a user input integer for the index value we need to fetch from list 'l'

try:
    print(l[k])
except IndexError:                                      # Any index out of bounds of length of list 'l' is handled
    print("print invalid index")