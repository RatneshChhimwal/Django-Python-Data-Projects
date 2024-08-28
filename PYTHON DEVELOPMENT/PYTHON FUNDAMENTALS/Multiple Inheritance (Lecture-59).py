class Employee:                                                         # We defined a class 'Employee'
    def __init__(self, name):                                           # We defined a constructor for Employee with a 'name' parameter
        self.name = name                                                # We initialize the 'name' attribute with the provided value

    def show(self):                                                     # We created a function/method 'show' for Employee
        print(f"The name of the employee is {self.name}")               # Printing the f-string

class Programmer:                                                       # We defined a class 'Programmer'
    def __init__(self, language):                                       # We defined a constructor for Programmer with a 'language' parameter
        self.language = language                                        # We initialize the 'language' attribute with the provided value

    def show(self):                                                     # Define a method 'show' for Programmer
        print(f"The language of the Programmer is {self.language}")     # Printing the f-string

class ProgrammerEmployee(Employee, Programmer):                         # We define a class 'ProgrammerEmployee' with multiple inheritance from both Employee and Programmer
    def __init__(self, name, language):                                 # We define a constructor for ProgrammerEmployee with 'name' and 'language' parameters
        super().__init__(name)                                          # We call the constructor of the first parent class (Employee) using 'super()' for the name attribute
        Programmer.__init__(self, language)                             # We call the constructor of the second parent class (Programmer)

        """
        
        IMPORTANT:------------------------------------------------------------------------------------------------------
        
        Note that we used 'super()' keyword for the first base class 'Employee', 
        So we did not pass the 'self' argument as the super() function takes care of passing the correct instance (self) to the parent class's method,
        Meanwhile for calling the constructor of the second parent class 'Programmer',
        We had to write the name of the class as well as pass the 'self' argument along with the attribute.
        
        """

Obj1 = ProgrammerEmployee("Ratnesh", "Python")          # We created an instance of ProgrammerEmployee named 'Obj1'
Obj1.show()                                                            # Calling the 'show' method on Obj1

"""
IMPORTANT:
Thanks to the Method Resolution Order (MRO), the 'show' method of the initial base class, 'Employee,' will be invoked.
If we were to rearrange the order of the two base classes in the child class definition in line-15
the 'show' method of the 'Programmer' class would take precedence."
"""
