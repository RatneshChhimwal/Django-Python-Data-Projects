# LIST METHODS:

'''
List methods in Python are functions that can be used to manipulate or perform various operations on lists. Some commonly used list methods include:
'''

l = [2,3,4,5,3,5,7,4,3,7,9,2,1,6]   # We created a list 'l' containing multiple values

print(l)

l.append(9)            # The 'append' method allows us to input/insert value at the end of the list

print(l)               # This now prints the updated list 'l'





l.sort()               # The 'sort' method allows us to sort the values inside a list in ascending (increasing) order

print(l)               # This now prints the updated list 'l'





l.reverse()            # The 'reverse' method just sorts the values inside the list in descending (decreasing) order, Vice-versa of 'sort' method
print(l)               # This now prints the updated list 'l'





print(l.index(7))      # 'index' method returns the first occurrence index for a specified value. In this case, it returns '2' for arg '7' in last version of list 'l'.





m=l.copy()             # 'copy' method allows us to make a copy of the last updated version of a list (l) and assign it to a new variable (m).
print(m)
m.append(3)            # Important: Any changes done in copied list 'm' will not affect the main list 'l', Here the value '3' is appended only in list 'm'
print(m)
print(l)





print(l.count(5))     # 'count' method prints out the number of times an argument value has occurred in the list, Prints '2' here as '5' has occurred twice in list 'l'





l.insert(2,7)   # The 'insert' method allows us to insert a value inside a list at a defined index, Syntax 'l.insert(Index,Value to be inserted)'





n=[8,1,9,2]                    # We created a new list 'n' to define the working of the 'extend' method as below:
l.extend(n)                    # 'extend' function allows us to insert a separate list 'n' at the end of an existing list 'l'
print(l)                       # This now prints the updated list 'l'

# NOTE: The 'extend' method updates the main list 'l' too, So to avoid this, We can simply define a new list (k) which holds concatenated list of 'l' & 'n' as below:

k=l+n
print(k)





