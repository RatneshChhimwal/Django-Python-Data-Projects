"""
In Python, is and == are both comparison operators that can be used to check if two values are equal.
However, there are some important differences between the two that you should be aware of.

The 'is' operator compares the identity of two objects, while the == operator compares the values of the objects.
This means that 'is' operator returns 'True' if the objects being compared are the exact same object in memory,
while '==' operator returns 'True' if the objects have the same value.
"""

# For example:

A = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# In the above example, the list 'A' & 'B' are two separate lists with different memory paths

# IMPORTANT: The 'is' operator returns 'True' for variable holding immutable values

""" In Python, strings and integers are immutable,
which means that once they are created, their value cannot be changed.
This means that, for strings and integers, is and == will always return the same result: """

a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # The 'is' operator will return 'True' here as the immutable string assigned to both variable 'a' & 'b' have the same memory path
a = 5
b = 5
print(a == b)  # True
print(a is b)  # True