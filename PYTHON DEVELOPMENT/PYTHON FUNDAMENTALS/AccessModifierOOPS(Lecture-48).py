# Access Specifiers/Modifiers:

"""
Access specifiers or access modifiers in python programming are used to
limit the access of class variables and class methods
outside the class while implementing the concepts of inheritance.
"""

# Types of access specifiers:--------------------

"""
- Public access modifier
- Private access modifier
- Protected access modifier
"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Public Access Specifier in Python--------------

"""
All the variables and methods (member functions) in python are by default public.
Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Private Access Modifier------------------------

"""
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class.
We cannot use private members outside of class.

n Python, there is no strict concept of "private" access modifiers like in some other programming languages.
However, a convention has been established to indicate that a variable or method should be considered private
by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only,
not a strict rule. Code outside the class can still access these "private" variables and methods,
but it is generally understood that they should not be accessed or modified.
"""

# The Basic example of private access attribute is below:

class employee:                     # We defined a class employee
    def __init__(self):             # Defined a constructor to initialize that takes argument 'self'
        self.__name="harry"         # Defined an attribute '__name' which holds the string 'harry'

obj=employee()                      # Created an object 'obj' for class 'employee'
# print(obj.__name)                 # Now, because we defined the attribute name with 2 underscores in front, we cannot access it directly like this

print(obj._employee__name)          # Rather, We will have to put in '_' followed by the name of the class before the attribute to access the attribute (_employee__name)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Protected Access Modifier----------------------

"""

In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class
that is intended to be accessed only by the class itself and its subclasses.
In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_).
For example, if a class has a method called _my_method,
it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention,
and does not actually provide any protection or restrict access to the member.
The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

"""




