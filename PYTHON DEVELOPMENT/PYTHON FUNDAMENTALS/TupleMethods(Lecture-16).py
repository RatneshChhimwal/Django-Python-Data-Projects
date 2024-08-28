# As we previously learned that tuples are immutable, Which means they can not be altered directly, So rather we have to convert it to a list first as below:

tup1=(34,56,76,87,36,90,76,87,36,87)        # We have created a tuple 'tup1' with few values

temp=list(tup1)                             # We created a temporary list 'list' and used 'list()' method to store the values from tuple 'tup1' inside that list
temp.append(100)                            # Now we can use all methods available for a list with the values from the tuple 'tup1'
print(tup1)                                 # Note: Remember the main tuple 'tup1' is not updated from the methods used on list 'temp'
print(temp)                                 # All updates are done on the list 'temp'



temp.pop(2)                                 # 'pop' method allows us to pop-out (remove) any value from the list by taking the index for the value as the argument
print(temp)                                 # prints a list with the value '76' with index '2' removed from the list




print(temp.count(87))                       # 'count' method prints back the number of times a value has occurred in the list 'temp'




temp.insert(2,45)           # 'insert' allows us to insert any value in the list at any index --- Syntax: ListName.insert(index, value(object))
print(temp)




temp.sort()                                # 'sort()' allows us to sort the list 'temp' in increasing(ascending) order
print(temp)


#NOTE: Once the updates are done the updated list can be again converted into a tuple using the 'tuple()' method as below:

tup1=tuple(temp)                           # Converts the list 'temp' into tuple 'tup1'
print(tup1)                                # Prints 'tup1'

