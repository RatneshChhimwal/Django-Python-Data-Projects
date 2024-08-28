# LISTS: (DATA TYPE)

'''

1- Lists are ordered collection of data items.
2- They store multiple items in a single variable.
3- List items are separated by commas and enclosed within square brackets [].
4- Lists are changeable meaning we can alter them after creation.

'''

Marks=[30,40,50,60,70,80]        # Here we have defined a list 'Marks' with 3 integer values enclosed inside square brackets, separated by commas.
print(Marks)                     # Here we are printing the list 'Marks'
print(type(Marks))               # Here we are printing the type of the list 'Marks'

print(Marks[2])                  # We can access the individual values from the list by defining the index for the value

print(Marks[1:4])                # Similar to strings, We can access a sub-list from the main list by defining index range
print(Marks[:3])                 # Another example of sub-string (prints [30,40,50]) from index zero to index 2 (index '3' in not included, similar to strings)
print(Marks[2:])                 # Another example of sub-string (prints [50,60,70,80]) from index two to the last index




# ****** We can also check if a particular list contains a particular value using 'if' conditions as below: ****************************************************************

if 70 in Marks:                                            # We define the value to be searched followed by keyword 'in' and the name of the list in the 'if' condition
    print("This value is present in the list Marks")
else:
    print("This value is not present in the list Marks")




# We can also create a program where we take the value to be searched from the user as below: -------------------------------------------------------------------------------

i=int(input("Enter a value"))                               # Here we are taking the 'input' from the user and assigning it to the variable 'i'

if i in Marks:                                              # We are checking for the value stored in the variable 'i' in the list 'Marks'
    print("This value is present in the list Marks")
else:
    print("This value is not present in the list Marks")




