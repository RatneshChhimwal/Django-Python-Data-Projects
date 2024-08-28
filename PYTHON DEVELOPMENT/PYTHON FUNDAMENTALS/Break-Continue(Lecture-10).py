# BREAK STATEMENTS:

'''
A 'break' statement is used to exit or terminate a loop prematurely, helps the user skip over the very loop it lies within.
It allows you to immediately stop the execution of the loop and continue with the next code outside the loop.
'''

for i in range(1,21):               # We defined a var 'i' with range arguments starting from '1' till 'n' as '21' (will print 'i' till 20 (n-1))
    print("5 X", i, "=", 5*i)       # We print the string "5 X" with values of 1 incrementing, then a string holding "=" and then arithmetic operation '5*i'

# This will print the table for '5' till 20
# Now if we wanted to break this loop at i=10, then we can use the 'break' statement as below:

    if i==10:                       # We defined the condition 'if'
        break                       # 'Break' statement

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CONTINUE STATEMENTS:

'''
A 'continue' statement is used to skip the current iteration of a loop and move to the next iteration.
It allows you to bypass the remaining code inside the current loop iteration and continue with the next iteration.
'''

for j in range(1,21):                                       # We defined a var 'j' with range from '1' till '20' (n-1)
    if j==10:                                               # We pre-define an 'if' condition for when 'j' is equal to '10'
        print("This iteration has been skipped over")       # This prints the string 'This iteration has been skipped over'
        continue                                            # The 'continue' statement skips the step with var 'j' is equal to '10' & prints the string given above
    print("3 X",j,"=",3*j)                                  # While the condition 'j=10' has been skipped, we are inside the 'if' condition printing the table to 3 till 20



