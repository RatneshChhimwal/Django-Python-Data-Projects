# Difference between Instance and Class variables:

# Class Variables -------------

"""
Class variables are defined at the class level and are shared among all instances of the class.
They are defined outside any method and are usually used to store information that is common to all instances of the class.
For example, a class variable can be used to store the number of instances of a class that have been created.
"""

# Instance Variables ---------

"""
Instance variables are defined at the instance level and are unique to each instance of the class.
They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
For example, an instance variable can be used to store the name of an employee in a class that represents an employee.
"""

# EXAMPLE BELOW:

class Employee:
  companyName = "Apple"
  noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees +=1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()

"""

In the above example, We created a class 'Employee' and defined 2 Class variable companyName & noOfEmployees,
The variable 'companyName' holds the default company name 'Apple'
for each object created from the class 'Employee' and variable 'noOfEmployees' is initialized at value '0'
and will be incremented with each object created.

Further, We defined a constructor and defined 2 instance variables 'name' & and 'raise_amount'
We also created a function 'showDetails' which displays the details of the employee from the created object 

"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

NOTE:****

Instance variables are unique to each object, allowing customization of attributes for specific instances.
Modifying an instance variable, like emp1.raise_amount = 0.3, affects only that object.
In contrast, class variables are shared among all instances.
Modifying a class variable with an instance, as in emp1.companyName = "Apple India", creates a new instance variable for that object.
To change a class variable for all instances, it's recommended to use the class name directly, such as Employee.companyName = "Apple India".

"""