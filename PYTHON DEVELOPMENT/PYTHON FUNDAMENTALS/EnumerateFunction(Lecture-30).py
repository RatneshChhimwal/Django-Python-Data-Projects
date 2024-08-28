# ENUMERATE FUNCTION:

"""

The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string)
and get the index and value of each element in the sequence at the same time.

"""

# Suppose we are iterating through a list & at some point we want to know the index which we are at, or we want a particular action to be performed at a particular index

# The First simple approach for the above result would be as below: -------------------------------------------------------------------------------------------------------

marks =[20,38,46,98,67,45,67]                       # We define a list 'marks'

index =0                                            # We defined a variable 'index' which holds the value '0' to begin with
for mark in marks:                                  # We defined a variable 'mark' which iterates through the list 'marks'
    print(mark)                                     # print 'mark'
    if index==3:                                    # A sub-'if' condition which is assigned with a string to print when value of the variable 'index' is '3'
        print("Above value was at 3rd index")
    elif index==6:                                  # We wrote this 'elif' condition just to print the distinction '-'s below for separation from the second approach
        print("-----------------------------")

# IMPORTANT: An 'if-elif-else' statement does not necessarily require an 'else' statement as we have done in this example

    index +=1                                       # This is how we increment the value of variable 'index' to '3' along with the variable 'mark' adjacently

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# THE SECOND APPROACH TO ACHIEVE THE SAME WOULD BE TO USE THE ENUMERATE FUNCTION AS BELOW:

marks =[20,38,46,98,67,45,67]                       # Not Needed, Yet we defined list 'marks' again

for index1,mark1 in enumerate(marks):               # We defined 'index1' and 'mark1' as 2 variables where 'index1' holds the index and 'mark1' holds the value at that index
    print(mark1)
    if index1==3:
        print("Above value was at 3rd index")