# WHILE-LOOP STATEMENTS:

'''

A 'while loop' in Python is a control structure that repeatedly executes a block of code as long as a specified condition is true.

'''

p=1              # We define the starting value for the var 'p' as '0'(zero)
while p<5:       # We defined the 'while' condition for the code to run till value of 'p' is less than '5'
    print(p)     # We are constantly printing 'p' for every value it stores
    p=p+1        # We defined the 'iteration' condition as increment by '1' for every previous value of 'p'

print("The loop can no longer execute as the value for \'p\' is now 5 which does not satisfy the while condition in line 18")


# Mostly these 'while' loops are not used with numbers and are used for much complex functions, Example below:

n=int(input("Enter a number more than 5\n"))            # Here we have defined a var 'n' taking user input
print(n)                                                # This simply prints the input by the user for var 'n'
while n<5:                                              # Here we have defined the condition for the loop inside 'while' to be executed till user input is less than 5
  n=int(input("The value should be more than 5"))       # Putting the same input code here means the user will be prompted to input till the value is less than 5
else:                                                   # This 'else' clarifies that the 'print' below runs when the 'while' condition is not met.
    print("Now the number is okay")                     # This 'print' statement is outside the 'while' loop & will be executed once the input is more than 5
