# TUPLES:

'''
Tuples in Python are like lists but immutable, meaning their elements cannot be changed once defined.
They are created using parentheses and can store a collection of items, similar to lists.
'''


tup=(1,2,3,4,5,6)       # Here we defined a tuple 'tup' and assigned it a list of immutable values
print(tup)              # Prints the tuple
print(type(tup))        # Prints the type of 'tup' which is a 'tuple' class


# VALUES OF THE TUPLE CAN ONLY BE ACCESSED & NOT MODIFIED *********

print(tup[0])           # Prints the value of the tuple at the index '0 (zero)' - 1
print(tup[1])           # Prints the value of the tuple at the index '1' - 2
print(tup[2])           # Prints the value of the tuple at the index '2' - 3



# 'if' condition in tuples: -------------------------------------------------------------------------------------------------------------------------------------------------

i=int(input("Enter a value from 1-10\n"))

if i in tup:
    print("Value is present in the tuple")
else:
    print("Value is not present in the tuple")



# Slicing of a tuple **************

print(tup[1:4])


# IMPORTANT: WE CAN CONVERT A TUPLE INTO A LIST BY USING THE 'list()' CONSTRUCTOR, AS BELOW:

lis= list(tup)          # CONVERTS THE TUPLE 'tup' INTO A LIST 'lis'
print(lis)              # PRINTS '[1, 2, 3, 4, 5, 6]'
