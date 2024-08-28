# LOOPS:

'''

Loops in Python are control structures that allow you to repeatedly execute a block of code until a certain condition is met.
They are used for automating repetitive tasks and iterating through data structures.

'''


# 'FOR' LOOP STATEMENTS ************************************************************************************************

'''

'for loops' can iterate over a sequence of iterable objects in python.
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

'''


# BELOW IS THE EXAMPLE OF 'for' LOOP FOR A STRING:

name = 'Hitesh'      # We have the string 'Hitesh' assigned to a var 'name'
for i in name:       # We used 'for', then defined a variable 'i' that will start iterating through the string assigned to name one by one
    print(i)         # We print(i) again and again for every character of the string 'Hitesh' & A list is printed with every character



# ********** We can also put conditional statements inside a running 'for' loop, Example below: **********

    if (i)=="t":      # We are currently inside the 'for' loop using a separate 'if' statement
        print("The above character has the index 2")   # Further indentation for print



# BELOW IS THE EXAMPLE OF 'for' LOOP FOR A LIST:

Colors=["Red","Blue","Yellow","Green"] # A list 'Colors'

for Color in Colors:
    print(Color) # This prints all entries of the list separately in a list

# As var 'Color' now contains items from 'Colors' list, we can further access individual characters too. For example, 'Red' can be split into 'R', 'e', 'd', As seen below:

    for j in Color: # We create the variable 'j' to hold letter from the individual entries
        print(j)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# RANGE FUNCTION:

'''
The range function in Python generates a sequence of numbers, often used in 'for loops' to iterate over a range of values.

'''

# Suppose we need to print all natural numbers from 1 till 10, Instead of using 'print' again n again, we can use 'Range' func as below:

for k in range(11): # The range func starts with '0' by default & prints values till 'n-1' values, That is why we put the argument for the func as '11'
    print(k) # This will print all numbers starting from '0' till the 'n-1' value which is 10



# We can define the start & end point inside the range func too, Suppose we only needed to print from 5 to 10, The same would've been as below:

for l in range(5,11): # We defined the var 'l' with '5' as the starting argument and '11' as the ending 'n' value inside the 'range' function
    print(l)



# We can also define the 'step' argument inside the 'range' function which specifies the interval between numbers in the generated sequence, Example below:

for m in range(1,21,2): # We defined the var 'm' which with '1' as starting argument and '21' as ending value & defined the interval(step) of the sequence as '2'
    print(m) # This will print the list as follows (1,3,5,7... till 19) with space of '2' digits & will print only till the last value that satisfies the range (19)

