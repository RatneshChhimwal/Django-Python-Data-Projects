# 'for-else' LOOP:

"""
A "for-else" loop in Python is a loop construct that combines a for loop with an else block.
The else block is executed when the for loop completes normally (without encountering a break statement).
It's often used to specify actions to be taken after a successful loop iteration.
"""

# IMPORTANT: Do remember this line from the definition: 'The else block is executed when the for loop completes normally (without encountering a break statement).'

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXAMPLE OF A 'for-else' LOOP:

for i in range(6):
    print(i)

else:
    print("No further iterations, as the last value i.e. \'5\' has been iterated ")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXAMPLE OF 'for-else' LOOP WITH 'break' STATEMENT

for i in range(7):
    print(f"the value is {i}")
    if i==4:                        # Neither 'i' nor the 'else' condition will be printed further because we used the 'break' statement
        break                       # The 'else' is only supposed to be printed once the 'for' loop is printed as intended

else:
    print("This \'else\' statement will not be printed")

