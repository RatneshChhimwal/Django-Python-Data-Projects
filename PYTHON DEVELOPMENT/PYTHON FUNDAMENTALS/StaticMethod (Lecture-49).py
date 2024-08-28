# STATIC METHODS:

"""
Static methods in Python are methods that belong to a class rather than an instance of the class.
They are defined using the '@staticmethod' decorator and do not have access to the instance of the class (i.e. self).
They are called on the class itself, not on an instance of the class.
Static methods are often used to create utility functions that don't need access to instance data.
"""

"""
Static methods are functions within a class designed to execute calculations internally, independent of specific instances
In the example below, we are using the 'add' function upon 2 variable 'a' & 'b'
This is rather a simple example of calculation, but suppose if we wanted to perform higher level of calculation,
Also, now this method is linked and shipped with the class itself, So the user of the class can also use the static method defined inside
"""

class Math:
    def __init__(self, num):        # We defined a constructor with 'num' argument
        self.num = num

    def addtonum(self, n):          # We defined a function 'addtonum' with 'n' as argument
        self.num = self.num + n     # Self.num is updated with addition of 'n' to the previously defined 'num'

    @staticmethod                   # We used the decorator '@staticmethod' to define the static method
    def add(a, b):                  # We defined the static method/function 'add' with 2 arguments 'a' & 'b'
        return a + b


# result = Math.add(1, 2)
# print(result) # Output: 3

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2))