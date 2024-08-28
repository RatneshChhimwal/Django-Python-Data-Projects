# Class-Method:

"""

A class method is a type of method that is bound to the class and not the instance of the class.
In other words, it operates on the class as a whole, rather than on a specific instance of the class.
Class methods are defined using the "@classmethod" decorator, followed by a function definition.
The first argument of the function is always "cls," which represents the class itself.

"""


class Employee:  # We defined a class 'Employee'
    company = "Apple"  # We defined a class variable 'company' with value 'Apple'

    def show(self):  # We defined a method/function 'show' which prints an f-String
        print(f"The name is {self.name} and company is {self.company}")  # f-String

    @classmethod  # '@classmethod' decorator to define the changes done will be on class level
    def changeCompany(cls, newCompany):  # We defined a function 'changeCompany' with 2 arguments 'cls' and 'newCompany'
        cls.company = newCompany  # cls.company = newCompany, using the '@classmethod' decorator, the 'newCompany' defined with the object will update the value of the class variable 'company'


e1 = Employee()
print(Employee.company)
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
e2 = Employee()
e2.changeCompany("Microsoft")
print(Employee.company)