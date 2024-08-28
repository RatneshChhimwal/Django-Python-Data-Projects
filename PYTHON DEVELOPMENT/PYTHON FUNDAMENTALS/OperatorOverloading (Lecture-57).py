"""

Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types.
This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes,
just as you would for built-in data types like int, float, and str.

"""

"""

In the below example the '+' operator is overloaded by the __add__ method for the class 'Vector'.
When you use the + operator between two instances of a class, if the class has a __add__ method defined, that method is automatically called.


"""

class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k)
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))