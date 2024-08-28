
# Inheritance in python:

"""

When a class derives from another class.
The child class will inherit all the public and protected properties and methods from the parent class.
In addition, it can have its own properties and methods, this is called as inheritance.

"""

# SYNTAX FOR AN INHERITED CLASS:----------------------------------------------------------------------------------------------------------------------------------------------

"""
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
"""

# EXAMPLE OF INHERITANCE BELOW:-----------------------------------------------------------------------------------------------------------------------------------------------

class Employee:                                                     # We created a class 'Employee'
  def __init__(self, name, id):                                     # Class 'Employee' constructor that mandates the objects to be created with arguments 'name' & 'id'
    self.name = name                                                # Class 'Employee' has 2 attributes 'self.name' and 'self.id'
    self.id = id

  def showDetails(self):                                            # The class 'Employee' also has a function 'showDetails'
    print(f"The name of Employee: {self.id} is {self.name}")        # The function 'showDetails' prints an f-string

    """
    Now, Suppose there is a sub-class of Employees called 'Programmer'
    These programmers are a type of employee only but has additional details or behaviors related to programming languages,
    which are encapsulated in the Programmer class.
    So, We define a class 'Programmer' inherited from the class 'Employee' as below
    """


class Programmer(Employee):                                         # The class 'Programmer' in inherited from class 'Employee'
  def showLanguage(self):                                           # Class 'Programmer' contains a function 'showLanguage' that prints a string
    print("The default langauge is Python")                         # The print string


e1 = Employee("Rohan Das", 400)                            # An object 'e1' is created for class 'Employee' with values for argument 'name' and 'id'
e1.showDetails()                                                    # The function 'showDetails' is called for the object 'e1'
e2 = Programmer("Harry", 4100)                            # Object 'e2' is created for inherited class 'Programmer' with arguments of base class 'Employee'
e2.showDetails()                                                    # The function 'showDetails' is called for the object 'e2'
e2.showLanguage()                                                   # The function 'showLanguage' is called for the object 'e2'
