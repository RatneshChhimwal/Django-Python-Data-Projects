# Super Keyword

"""

The super() keyword in Python is used to refer to the parent class.
It is especially useful when a class inherits from multiple parent classes, and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class.
However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

"""

# EXAMPLE FOR 'super' KEYWORD IN A SIMPLE INHERITANCE SCENARIO:

class ParentClass:                              # We defined a class named 'ParentClass'
    def parent_method(self):                    # The class contains a method 'parent_method' that takes no input argument and prints a string when called
        print("This is the parent method.\n")

class ChildClass(ParentClass):                  # We also define a class 'ChildClass' inherited from 'ParentClass'
    def child_method(self):                     # The class contains a 'chile_method' that takes no input argument and prints a string when called
        print("This is the child method.\n")

    def parent_method(self):                    # We define another method named same as 'parent_method' but inside the ChildClass
        print("This is the parent method from child class\n")

        """
        Now, here if we would simply call the 'parent_method' for any object of the ChildClass, The string "This is the parent method from child class" will be printed,
        To call the 'parent_method' from the 'ParentClass' we need to use the keyword 'super' as below:
        """

        super().parent_method()


child_object = ChildClass()        # We create an object for the class 'ChildClass'
child_object.child_method()        # We call the 'child_method' on the object for the class 'ChildClass'

child_object.parent_method()       # Here, firstly, the 'parent_method' of the child class is called which then executes the line 'super().parent_method()' from line 31


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# IMPORTANT: ************************************************************************************************************************************************************** b
"""
The 'super' keyword can also be used to call the constructor of the parent class in the child class, As shown below:
"""

""" In the below example, The parent class 'Employee' was defined with 2 attributes (name and id),
Later on the child class 'Programmer' had to use another attribute (lang), So instead of defining the all attributes again, We use 'super' keyword as shown in line 60
"""

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)




