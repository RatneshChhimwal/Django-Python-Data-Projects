"""
The dir(), __dict__() and help() attribute/methods in python make it easy for us to understand how classes resolve various functions and executes code.
"""

"""
dir():The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
It is a useful tool for discovering what you can do with an object.
"""

# EXAMPLE:
x = [1, 2, 3]
print(dir(x))

"""
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes.
It is a useful tool for introspection.
"""

"""
help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.
"""

# Example for both the '__dict__' attribute and 'help()' method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
print(p.__dict__)

print(help(Person))

