
# SETs in python are similar to sets in mathematics, and similar actions can be done upon them.


""" Joining Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics. """

''' 1- union() and update():
The union() and update() methods prints all items that are present in the two sets.
The union() method returns a new set whereas update() method adds item into the existing set from another set.'''

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)


# Output:{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}


# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)                              # Here we have updated the set 'cities'
print(cities)


# Output:{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}



#-----------------------------------------------------------------------------------------------------------------------


''' 2- intersection and intersection_update():
The intersection() and intersection_update() methods prints only items that are similar to both the sets.
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.'''

# Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)


# Output:{'Madrid', 'Tokyo'}


#Example :

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)                 # Here we have updated the set 'cities' with 'intersection_update'.
print(cities)


# Output:{'Tokyo', 'Madrid'}


#-----------------------------------------------------------------------------------------------------------------------


''' 3- symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.'''

# NOTE: SYMMETRIC DIFFERENCE MEANS 'A union B minus A intersection B'

#Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)


# Output:{'Seoul', 'Kabul', 'Berlin', 'Delhi'}


#Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)


# Output:{'Kabul', 'Delhi', 'Berlin', 'Seoul'}


''' 4- difference() and difference_update():
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets.
The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.'''

# Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)                # Stores the values present in 'cities' which are not present in 'cities2' inside 'cities3'
print(cities3)


# Output:{'Tokyo', 'Madrid', 'Berlin'}

# Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))                   # We updated the set 'cities' with difference


# Output:{'Tokyo','Berlin','Madrid'}

# ----------------------------------------------------------------------------------------------------------------------

print(cities.isdisjoint(cities2))  # 'isdisjoint' checks if the two sets have no common values, In this case it prints 'FALSE', As cities and cities2 have common values.

# ----------------------------------------------------------------------------------------------------------------------

print(cities.issuperset(cities2)) # 'issuperset' checks if the values in set 'cities2' are already present in set 'cities', Prints 'FALSE' here too.

# ----------------------------------------------------------------------------------------------------------------------

print(cities.issubset(cities2)) # 'issubset' checks if the values in set 'cities' are already present in the set 'cities2', Prints 'FALSE' here too.


# IMPORTANT: 'issubset' method is opposite of 'issuperset', meaning is 'set1 is a superset of set2', then 'set2 is a subset of set1'



#-----------------------------------------------------------------------------------------------------------------------



# BELOW-MENTIONED ARE SOME OF THE BASIC METHODS THAT ARE USED ON SETS

MainSet= {1,2,3,4,5,6,7,8}

print(MainSet)
print(type(MainSet))

MainSet.add(9)                  # 'add()' method allows us to insert a value inside the set
print(MainSet)

MainSet.remove(5)               # 'remove()' method allows us to remove any value from the set
print(MainSet)


print(MainSet.pop())            # 'pop()' method allows us to pop out any random value from inside the set


MainSet.clear()                 # 'clear()' method allows us to clear a set of its values
print(MainSet)

