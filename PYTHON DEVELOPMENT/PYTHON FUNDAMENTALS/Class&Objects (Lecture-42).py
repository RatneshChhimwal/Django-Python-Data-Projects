# Python Class and Objects:

"""
Class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods).
The user-defined objects are created using the class keyword.
"""

# Creating a Class:

class Details:              # We use the keyword 'class' followed by the name of the class (Details)
    name = "Rohan"          # Setting default values during attribute definition, like the 'name' attribute here, is advisable.
    age = 20                # SYNTAX: attribute = value

# Creating an Object:

""" Object is the instance of the class used to access the properties of the class Now lets create an object of the class."""

# Example:

obj1 = Details()            # We define the name of the object (obj1) then the class it is defined for

# Now we can print values:

class Details:              # Keyword 'class' followed by the name of the class
    name = "Rohan"          # Attribute 'name'
    age = 20                # Attribute 'age'
obj1 = Details()            # Object 'obj1' followed by the name of the class
print(obj1.name)            # Prints Object.attribute (Rohan)
print(obj1.age)             # Prints Object.attribute (20)

# If we wanted to create another object for the same class:

obj2= Details()             # New object for the class 'Details'
obj2.name = 'Shubham'       # Here, we have updated the attribute 'name' to hold the string 'Shubham'
obj2.age = 23               # Here, we have updated the attribute 'age' to hold integer value 23

print(obj2.name)            # Prints 'Shubham'
print(obj2.age)             # Prints 23
