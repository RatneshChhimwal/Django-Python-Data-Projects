# SETS:

'''
Sets are unordered collection of data items. They store multiple items in a single variable.
Set items are separated by commas and enclosed within curly brackets {}.
Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.
'''

set1 = {"Carla", 19, False, 5.9, 19}
print(set1)

#NOTE: Know that the values inside the set 'set1' above will be printed in random order.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# TO ACCESS THE VALUES OF A SET, WE CAN USE THE 'for-in' LOOP, AS BELOW:

set1 = {"Carla", 19, False, 5.9}
for item in set1:
    print(item)


#NOTE: Know that the values printed upon accessing the set 'set1' above will again be in random order.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# IMPORTANT: To create an empty set, We have to use the method 'set' as below:

set2= set()
print(type(set2))

# We had to use the method 'set' as defining an empty set with '{}', creates a dictionary instead


