"""

Multilevel inheritance is a type of inheritance in object-oriented programming where a class is derived from another class,
and then another class is derived from this second class, forming a chain of inheritance.
In simpler terms, it involves creating a hierarchy of classes where each class inherits from the class above it.

"""

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name of the Employee is {self.name}")

obj=Employee("Ratnesh")
obj.show()

class Programmer(Employee):
    def __init__(self, language, name):
        super().__init__(name)
        self.language = language

    def show(self):
        print(f"The language of the Programmer is {self.language}")

obj1=Programmer("Python", "Ratnesh")
obj1.show()

class ProgrammerDomain(Programmer):
    def __init__(self, language, name, domain):
        super().__init__(language, name)
        self.domain=domain

    def show(self):
        print(f"The domain of the Programmer is {self.domain}")

obj2= ProgrammerDomain("Python", "Ratnesh", "Back-end")
obj2.show()